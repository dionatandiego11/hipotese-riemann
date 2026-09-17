"""
riemann_spectra.inverse_spectroscopy
Orquestração das Etapas 7-9 (M3) para um bloco contíguo de zeros.

Ordem obrigatória dentro de `run_block`:
  1. instrumento F_w e diagnósticos (Etapa 7);
  2. nulos (sem catálogo): perfil sigma(t) e distribuição do máximo; calibração sintética
     com linhas em períodos aleatórios uniformes (Etapa 8);
  3. detecção nos zeros, gravação de blind_peaks.csv e dos nulos, hash (congelamento);
  4. SOMENTE ENTÃO: módulo aritmético, matching, escore global, medição direcionada (Etapa 9).
"""

import csv
import json
import logging
import math
import os
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np

from riemann_spectra.controls import (
    generate_gue_central_levels,
    gue_energy_levels_like,
    inject_density_lines,
    shuffled_energy_levels_like,
)
from riemann_spectra.periods import (
    OscillatoryTransform,
    adjusted_p_values,
    calibrate_threshold,
    detect_blind_peaks,
    max_statistic,
    null_noise_profile,
)
from riemann_spectra.unfolding import d_bar_rvm, n_bar_rvm
from riemann_spectra.utils import compute_file_sha256

logger = logging.getLogger("riemann_spectra.inverse_spectroscopy")

# ---------------------------------------------------------------------------
# Trabalho paralelo reprodutível: cada realização tem sua própria SeedSequence
# ---------------------------------------------------------------------------

_WORKER_CACHE: Dict[Tuple, OscillatoryTransform] = {}


def _instrument(params: Tuple) -> OscillatoryTransform:
    if params not in _WORKER_CACHE:
        _WORKER_CACHE.clear()
        A, B, t_min, t_max, ppf = params
        _WORKER_CACHE[params] = OscillatoryTransform(A, B, t_min, t_max, points_per_fwhm=ppf)
    return _WORKER_CACHE[params]


def _null_levels(kind: str, gammas: np.ndarray, seed_state: Any, gue_fraction: float) -> np.ndarray:
    rng = np.random.default_rng(seed_state)
    if kind == "shuffle":
        return shuffled_energy_levels_like(gammas, rng)
    if kind == "gue":
        return gue_energy_levels_like(gammas, gue_fraction, rng)
    raise ValueError(kind)


def _task_power(args) -> np.ndarray:
    kind, gammas, seed_state, params, gue_fraction = args
    tr = _instrument(params)
    F = tr.transform(_null_levels(kind, gammas, seed_state, gue_fraction))
    return np.abs(F) ** 2


def _task_max(args) -> Tuple[float, np.ndarray, np.ndarray]:
    kind, gammas, seed_state, params, gue_fraction, sigma, fwhm, cand_z = args
    tr = _instrument(params)
    F = tr.transform(_null_levels(kind, gammas, seed_state, gue_fraction))
    peaks = detect_blind_peaks(tr.t_grid, F, fwhm, sigma, candidate_z=cand_z)
    per = np.array([p["period"] for p in peaks])
    zz = np.array([p["z"] for p in peaks])
    return max_statistic(F, sigma), per, zz


def _task_synthetic(args) -> List[Dict[str, float]]:
    """Linhas injetadas em níveis GUE; retorna erro de localização e detecção por linha."""
    gammas, seed_state, params, gue_fraction, sigma, fwhm, thr, n_lines, z_range, pair_sep = args
    rng = np.random.default_rng(seed_state)
    tr = _instrument(params)
    A, B, t_min, t_max, _ = params
    n = len(gammas)
    y, _ = generate_gue_central_levels(n, gue_fraction, rng)
    x0, x1 = float(n_bar_rvm(gammas[0])), float(n_bar_rvm(gammas[-1]))
    x = x0 + (y - y[0]) * (x1 - x0) / (y[-1] - y[0])
    margin = 0.05
    if pair_sep is None:
        # linhas isoladas: períodos uniformes com separação mínima de 10 FWHM
        T = []
        while len(T) < n_lines:
            cand = rng.uniform(t_min + margin, t_max - margin)
            if all(abs(cand - u) > 10 * fwhm for u in T):
                T.append(cand)
        T = np.array(T)
    else:
        centers = rng.uniform(t_min + margin, t_max - margin, size=n_lines // 2)
        T = np.sort(np.concatenate([centers - 0.5 * pair_sep * fwhm, centers + 0.5 * pair_sep * fwhm]))
    sig_T = np.interp(T, tr.t_grid, sigma)
    z_true = rng.uniform(z_range[0], z_range[1], size=len(T))
    coef_mod = z_true * sig_T * 4.0 / tr.L
    C = coef_mod * np.exp(1j * rng.uniform(0, 2 * np.pi, size=len(T)))
    # orçamento de positividade: sum |C| <= 0.8 min dbar na janela; descarta linhas (pares inteiros)
    budget = 0.8 * float(d_bar_rvm(gammas[0]))
    keep = np.zeros(len(T), dtype=bool)
    used = 0.0
    step = 1 if pair_sep is None else 2
    for k in range(0, len(T) - step + 1, step):
        cost = float(np.sum(coef_mod[k:k + step]))
        if used + cost <= budget:
            keep[k:k + step] = True
            used += cost
    if not keep.any():
        return []
    T, z_true, coef_mod, C = T[keep], z_true[keep], coef_mod[keep], C[keep]
    E = inject_density_lines(x, T, C)
    F = tr.transform(E)
    peaks = detect_blind_peaks(tr.t_grid, F, fwhm, sigma, candidate_z=min(3.0, thr))
    det = [p for p in peaks if p["z"] >= thr]
    per = np.array([p["period"] for p in det])
    out = []
    for k in range(len(T)):
        if len(per):
            j = int(np.argmin(np.abs(per - T[k])))
            err = float(per[j] - T[k])
        else:
            err = float("inf")
        out.append({"T": float(T[k]), "z_true": float(z_true[k]), "error": err, "coef_modulus": float(coef_mod[k])})
    return out


def _map(executor, fn, tasks):
    if executor is None:
        return [fn(t) for t in tasks]
    return list(executor.map(fn, tasks, chunksize=max(1, len(tasks) // 32)))


# ---------------------------------------------------------------------------
# Execução de um bloco
# ---------------------------------------------------------------------------

def run_block(
    gammas: np.ndarray,
    block: Dict[str, Any],
    cfg: Dict[str, Any],
    out_dir: Path,
    seed_seq: np.random.SeedSequence,
    workers: int = 1,
) -> Dict[str, Any]:
    name = block["name"]
    i0, i1 = block["first_index"], block["last_index"]
    g = np.asarray(gammas[i0 - 1:i1], dtype=np.float64)
    t_min, t_max = cfg["t_min"], cfg["t_max"]
    ppf = cfg["points_per_fwhm"]
    alpha = cfg["alpha"]
    gue_fraction = cfg["gue_retained_fraction"]
    cand_z = cfg["candidate_z"]
    params = (float(g[0]), float(g[-1]), t_min, t_max, ppf)
    bdir = out_dir / name
    bdir.mkdir(parents=True, exist_ok=True)
    timings: Dict[str, float] = {}
    result: Dict[str, Any] = {"block": block}

    # 1. Instrumento --------------------------------------------------------
    t0 = time.perf_counter()
    tr = _instrument(params)
    fwhm = tr.response["fwhm"]
    F = tr.transform(g)
    diag = tr.diagnostics(g, n_check=64, seed=int(seed_seq.generate_state(1)[0]))
    result["instrument"] = tr.to_metadata()
    result["instrument_diagnostics"] = diag
    timings["instrument"] = time.perf_counter() - t0
    logger.info(f"[{name}] n={len(g)} L={tr.L:.1f} FWHM={fwhm:.3e} n_t={tr.n_t}; NUFFT-direto={diag['nufft_vs_direct_max_abs_error']:.2e}")

    children = seed_seq.spawn(3)
    executor = ProcessPoolExecutor(max_workers=workers) if workers > 1 else None
    try:
        nulls: Dict[str, Dict[str, Any]] = {}
        for kind, child, n_sigma, n_max in [
            ("shuffle", children[0], cfg["null_sigma_realizations"], cfg["null_max_realizations"]),
            ("gue", children[1], cfg["gue_sigma_realizations"], cfg["gue_max_realizations"]),
        ]:
            t0 = time.perf_counter()
            seeds = child.spawn(n_sigma + n_max)
            powers = _map(executor, _task_power, [(kind, g, s, params, gue_fraction) for s in seeds[:n_sigma]])
            sigma = null_noise_profile(np.sqrt(np.array(powers)), tr.t_grid, cfg["noise_smooth_window"])
            del powers
            res = _map(executor, _task_max, [(kind, g, s, params, gue_fraction, sigma, fwhm, cand_z) for s in seeds[n_sigma:]])
            null_max = np.array([r[0] for r in res])
            thr = calibrate_threshold(null_max, alpha)
            nulls[kind] = {
                "sigma": sigma,
                "null_max": null_max,
                "threshold": thr,
                "null_peaks": [(r[1], r[2]) for r in res],
            }
            timings[f"null_{kind}"] = time.perf_counter() - t0
            logger.info(f"[{name}] nulo {kind}: B_sigma={n_sigma} B_max={n_max} limiar z={thr:.3f} ({timings[f'null_{kind}']:.1f} s)")

        primary = cfg["primary_null"]
        sigma_p, thr_p = nulls[primary]["sigma"], nulls[primary]["threshold"]

        # 2b. Calibração sintética (sem catálogo; períodos aleatórios uniformes) --------
        t0 = time.perf_counter()
        syn_seeds = children[2].spawn(2 * cfg["synthetic_realizations"])
        n_lines = cfg["synthetic_lines_per_realization"]
        iso_tasks = [(g, s, params, gue_fraction, sigma_p, fwhm, thr_p, n_lines, (0.5 * thr_p, 4.0 * thr_p), None)
                     for s in syn_seeds[:cfg["synthetic_realizations"]]]
        iso = [row for rows in _map(executor, _task_synthetic, iso_tasks) for row in rows]
        pair_rows = []
        for k, sep in enumerate(cfg["synthetic_pair_separations_fwhm"]):
            sub = syn_seeds[cfg["synthetic_realizations"]:][k::len(cfg["synthetic_pair_separations_fwhm"])]
            tasks = [(g, s, params, gue_fraction, sigma_p, fwhm, thr_p, 2 * max(1, n_lines // 4), (2.0 * thr_p, 4.0 * thr_p), sep) for s in sub]
            for rows in _map(executor, _task_synthetic, tasks):
                for r in rows:
                    r["pair_separation_fwhm"] = sep
                    pair_rows.append(r)
        timings["synthetic"] = time.perf_counter() - t0
    finally:
        if executor is not None:
            executor.shutdown()

    calib = summarize_synthetic(iso, pair_rows, fwhm, thr_p, cfg)
    result["synthetic_calibration"] = calib
    tol = calib["matching_tolerance"]
    res_sep = calib["resolution_separation"]
    logger.info(f"[{name}] sintético: tolerância={tol:.3e} ({tol/fwhm:.3f} FWHM), separação resolvida={res_sep/fwhm:.2f} FWHM")

    # 3. Detecção nos zeros e congelamento -----------------------------------
    peaks = detect_blind_peaks(tr.t_grid, F, fwhm, sigma_p, candidate_z=cand_z, evaluator=lambda t: tr.evaluate(g, t))
    z_primary = np.array([p["z"] for p in peaks])
    p_adj_primary = adjusted_p_values(z_primary, nulls[primary]["null_max"])
    secondary = "gue" if primary == "shuffle" else "shuffle"
    sig_s = np.interp([p["period"] for p in peaks], tr.t_grid, nulls[secondary]["sigma"]) if peaks else np.array([])
    z_secondary = np.array([p["modulus"] for p in peaks]) / sig_s if peaks else np.array([])
    p_adj_secondary = adjusted_p_values(z_secondary, nulls[secondary]["null_max"])
    for k, p in enumerate(peaks):
        p["p_adjusted_primary"] = float(p_adj_primary[k])
        p["detected_primary"] = bool(p["z"] >= thr_p)
        p["z_secondary"] = float(z_secondary[k])
        p["p_adjusted_secondary"] = float(p_adj_secondary[k])
        p["detected_secondary"] = bool(z_secondary[k] >= nulls[secondary]["threshold"])

    blind_csv = bdir / "blind_peaks.csv"
    cols = ["period", "fwhm_instrument", "amplitude_real", "amplitude_imag", "modulus", "phase_rad",
            "null_noise_rms", "z", "p_adjusted_primary", "detected_primary",
            "z_secondary", "p_adjusted_secondary", "detected_secondary"]
    with open(blind_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["peak_id"] + cols)
        for k, p in enumerate(peaks):
            p["fwhm_instrument"] = fwhm
            w.writerow([k] + [repr(p[c]) if isinstance(p[c], float) else p[c] for c in cols])
    null_npz = bdir / "nulls.npz"
    np.savez_compressed(
        null_npz,
        t_grid=tr.t_grid,
        F_real=F.real, F_imag=F.imag,
        **{f"{k}_sigma": v["sigma"] for k, v in nulls.items()},
        **{f"{k}_null_max": v["null_max"] for k, v in nulls.items()},
    )
    freeze = {
        "blind_peaks_csv": str(blind_csv),
        "blind_peaks_sha256": compute_file_sha256(blind_csv),
        "nulls_npz_sha256": compute_file_sha256(null_npz),
        "frozen_before_arithmetic": True,
        "n_candidates": len(peaks),
        "n_detected_primary": int(sum(p["detected_primary"] for p in peaks)),
        "n_detected_secondary": int(sum(p["detected_secondary"] for p in peaks)),
    }
    with open(bdir / "freeze.json", "w", encoding="utf-8") as f:
        json.dump(freeze, f, indent=2)
    result["freeze"] = freeze
    result["null_summary"] = {
        k: {
            "B_max": int(len(v["null_max"])),
            "threshold_z": v["threshold"],
            "null_max_quantiles": np.quantile(v["null_max"], [0.05, 0.5, 0.95]).tolist(),
            "sigma_at_t": {str(tt): float(np.interp(tt, tr.t_grid, v["sigma"])) for tt in (0.7, 1.0, 2.0, 3.0, 4.0, 4.9)},
        } for k, v in nulls.items()
    }
    result["zeros_background"] = {
        "median_abs_F_over_sigma_primary": float(np.median(np.abs(F) / sigma_p)),
        "median_abs_F_over_sigma_secondary": float(np.median(np.abs(F) / nulls[secondary]["sigma"])),
        "note": "Mediana ao longo de toda a malha, incluindo linhas; mede o fundo entre linhas.",
    }
    logger.info(f"[{name}] congelado: {freeze['n_detected_primary']} detecções ({primary}), SHA-256 {freeze['blind_peaks_sha256'][:16]}…")

    # 4. Comparação aritmética (após o congelamento) --------------------------
    from riemann_spectra import arithmetic as ar  # importação deliberadamente tardia

    t0 = time.perf_counter()
    result["arithmetic"] = arithmetic_comparison(ar, tr, g, peaks, nulls, primary, secondary, tol, res_sep, bdir, cfg, seed_seq)
    timings["arithmetic"] = time.perf_counter() - t0
    result["timings_seconds"] = timings
    with open(bdir / "block_metrics.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, default=_json_default)
    return result


def _json_default(o):
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(type(o))


def summarize_synthetic(iso: List[Dict], pairs: List[Dict], fwhm: float, thr: float, cfg: Dict[str, Any]) -> Dict[str, Any]:
    """Tolerância de matching, curva de recuperação e separação mínima resolvida."""
    iso_z = np.array([r["z_true"] for r in iso])
    iso_err = np.array([r["error"] for r in iso])
    # detecção no sentido amplo: pico acima do limiar a menos de meia FWHM
    near = np.abs(iso_err) <= 0.5 * fwhm
    errs = np.abs(iso_err[near & (iso_z >= thr)])
    q = cfg["matching_tolerance_quantile"]
    tol = float(np.quantile(errs, q)) if len(errs) else 0.5 * fwhm
    tol = min(max(tol, 1e-12), 0.5 * fwhm)

    edges = np.array(cfg["recovery_curve_z_edges"]) * thr
    curve = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (iso_z >= lo) & (iso_z < hi)
        if m.sum() == 0:
            continue
        rec = np.abs(iso_err[m]) <= tol
        curve.append({
            "z_true_low": float(lo), "z_true_high": float(hi), "n": int(m.sum()),
            "recovery_rate": float(rec.mean()),
            "median_abs_error_detected": float(np.median(np.abs(iso_err[m][rec]))) if rec.any() else None,
        })

    sep_curve = []
    seps = sorted(set(r["pair_separation_fwhm"] for r in pairs))
    res_sep = None
    for sep in seps:
        rows = [r for r in pairs if r["pair_separation_fwhm"] == sep]
        ok = np.mean([abs(r["error"]) <= tol for r in rows])
        sep_curve.append({"separation_fwhm": sep, "n_lines": len(rows), "fraction_lines_recovered": float(ok)})
        if res_sep is None and ok >= cfg["resolution_recovery_target"]:
            res_sep = sep
    if res_sep is None:
        res_sep = max(seps) if seps else 2.0
    return {
        "n_isolated_lines": int(len(iso)),
        "matching_tolerance": tol,
        "matching_tolerance_fwhm": tol / fwhm,
        "matching_tolerance_quantile": q,
        "recovery_curve": curve,
        "pair_resolution_curve": sep_curve,
        "resolution_separation_fwhm": float(res_sep),
        "resolution_separation": float(res_sep * fwhm),
    }


def arithmetic_comparison(ar, tr, g, peaks, nulls, primary, secondary, tol, res_sep, bdir, cfg, seed_seq) -> Dict[str, Any]:
    fwhm = tr.response["fwhm"]
    catalog = ar.prime_power_catalog(float(tr.t_grid[0]), float(tr.t_grid[-1]))
    ar.flag_unresolved(catalog, res_sep)

    det_peaks = [p for p in peaks if p["detected_primary"]]
    det_periods = np.array([p["period"] for p in det_peaks])
    assign, summary = ar.match_one_to_one(det_periods, catalog, tol)

    # escore global S = número de linhas do catálogo com pico detectado correspondente
    thr_p = nulls[primary]["threshold"]
    null_scores = []
    null_false = []
    for per, zz in nulls[primary]["null_peaks"]:
        per_det = per[zz >= thr_p] if len(per) else per
        _, s = ar.match_one_to_one(per_det, catalog, tol)
        null_scores.append(s["n_matched"])
        null_false.append(len(per_det))
    null_scores = np.array(null_scores)
    B = len(null_scores)
    S = summary["n_matched"]
    p_global = float((1 + np.sum(null_scores >= S)) / (B + 1))

    # sensibilidade prevista por linha (limiar do nulo primário)
    sig_T = np.interp([c["period_theoretical"] for c in catalog], tr.t_grid, nulls[primary]["sigma"])
    fit = ar.targeted_joint_fit(lambda t: tr.evaluate(g, t), catalog, tr.L, tr.E_c, half_width=cfg["targeted_fit_half_width_fwhm"] * fwhm)

    rows = []
    for k, c in enumerate(catalog):
        lim = ar.detection_limit_coefficient(sig_T[k], thr_p, tr.L)
        detectable = abs(c["coefficient_theoretical"]) >= lim
        pk = det_peaks[assign[k]] if k in assign else None
        fr = fit[k]
        rows.append({
            "run_block": bdir.name,
            "prime": c["prime"],
            "repetition": c["repetition"],
            "period_theoretical": c["period_theoretical"],
            "period_observed": pk["period"] if pk else None,
            "absolute_error": abs(pk["period"] - c["period_theoretical"]) if pk else None,
            "error_in_fwhm": abs(pk["period"] - c["period_theoretical"]) / fwhm if pk else None,
            "fwhm_instrument": fwhm,
            "amplitude_real": pk["amplitude_real"] if pk else None,
            "amplitude_imag": pk["amplitude_imag"] if pk else None,
            "z_primary": pk["z"] if pk else None,
            "p_adjusted": pk["p_adjusted_primary"] if pk else None,
            "coefficient_theoretical": c["coefficient_theoretical"],
            "fit_coefficient_real": fr["coefficient_real"],
            "fit_coefficient_imag": fr["coefficient_imag"],
            "fit_ratio_to_theory": fr["ratio_to_theory"],
            "fit_phase_error_rad": fr["phase_error_rad"],
            "detection_limit_coefficient": lim,
            "predicted_detectable": bool(detectable),
            "detected": pk is not None,
            "resolved": c["resolved"],
            "nearest_neighbor_separation": c["nearest_neighbor_separation"],
        })
    with open(bdir / "arithmetic_matches.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if v is None else v) for k, v in r.items()})

    unmatched = [p for i, p in enumerate(det_peaks) if i not in set(assign.values())]
    with open(bdir / "unmatched_detections.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["period", "z", "p_adjusted", "modulus", "nearest_catalog_period", "distance_fwhm"])
        Tcat = np.array([c["period_theoretical"] for c in catalog])
        for p in unmatched:
            j = int(np.argmin(np.abs(Tcat - p["period"])))
            w.writerow([p["period"], p["z"], p["p_adjusted_primary"], p["modulus"], Tcat[j], abs(Tcat[j] - p["period"]) / fwhm])

    detectable = np.array([r["predicted_detectable"] for r in rows])
    detected = np.array([r["detected"] for r in rows])
    resolved = np.array([r["resolved"] for r in rows])
    ratios = np.array([r["fit_ratio_to_theory"] for r in rows])
    phases = np.array([r["fit_phase_error_rad"] for r in rows])
    good = resolved & detectable

    # sensibilidade à precisão declarada da tabela: perturbação uniforme em [-eps, eps]
    eps = cfg["declared_table_error"]
    rng_p = np.random.default_rng(seed_seq.spawn(2)[1])
    pert_changes = []
    for _ in range(cfg["precision_perturbations"]):
        gp = g + rng_p.uniform(-eps, eps, size=len(g))
        fit_p = ar.targeted_joint_fit(lambda t: tr.evaluate(gp, t), catalog, tr.L, tr.E_c,
                                      half_width=cfg["targeted_fit_half_width_fwhm"] * fwhm)
        pert_changes.append(np.array([fp["ratio_to_theory"] for fp in fit_p]) - ratios)
    pert_changes = np.abs(np.array(pert_changes))
    precision_sensitivity = {
        "perturbation_half_width": eps,
        "realizations": int(cfg["precision_perturbations"]),
        "median_abs_ratio_change_selected_lines": float(np.median(pert_changes[:, good])) if good.any() else None,
        "max_abs_ratio_change_selected_lines": float(np.max(pert_changes[:, good])) if good.any() else None,
        "median_abs_ratio_deviation_observed": float(np.median(np.abs(ratios[good] - 1.0))) if good.any() else None,
        "note": "Análise de sensibilidade; não é um modelo do erro real da tabela.",
    }

    # coerência de fase vs controle de fase (preserva |F| na malha; não testa potência)
    phase_test = phase_coherence_test(tr, g, catalog, good, cfg["phase_control_realizations"], seed_seq)

    return {
        "catalog_size": len(catalog),
        "catalog_primitive": int(sum(c["repetition"] == 1 for c in catalog)),
        "catalog_repetitions": int(sum(c["repetition"] > 1 for c in catalog)),
        "catalog_resolved": int(resolved.sum()),
        "matching_tolerance": tol,
        "detected_peaks_primary": len(det_peaks),
        "matched_S": S,
        "unmatched_detections": len(unmatched),
        "null_S_mean": float(null_scores.mean()),
        "null_S_max": int(null_scores.max()),
        "null_detections_mean": float(np.mean(null_false)),
        "p_value_global_mc": p_global,
        "p_value_floor": 1.0 / (B + 1),
        "B_null": B,
        "predicted_detectable": int(detectable.sum()),
        "recovery_among_predicted_detectable": float(detected[detectable].mean()) if detectable.any() else None,
        "detected_but_predicted_undetectable": int((detected & ~detectable).sum()),
        "missed_predicted_detectable": [(r["prime"], r["repetition"]) for r in rows if r["predicted_detectable"] and not r["detected"]],
        "targeted_fit": {
            "lines_resolved_and_detectable": int(good.sum()),
            "ratio_to_theory_median": float(np.median(ratios[good])) if good.any() else None,
            "ratio_to_theory_iqr": np.quantile(ratios[good], [0.25, 0.75]).tolist() if good.any() else None,
            "abs_phase_error_median_rad": float(np.median(np.abs(phases[good]))) if good.any() else None,
            "primitive_ratio_median": float(np.median(ratios[good & (np.array([r["repetition"] for r in rows]) == 1)])) if good.any() else None,
            "repetition_ratio_median": (float(np.median(ratios[good & (np.array([r["repetition"] for r in rows]) > 1)]))
                                        if (good & (np.array([r["repetition"] for r in rows]) > 1)).any() else None),
            "fit_residual_rms": fit[0]["fit_residual_rms"],
            "design_condition_number": fit[0]["design_condition_number"],
        },
        "phase_coherence": phase_test,
        "precision_sensitivity": precision_sensitivity,
    }


def phase_coherence_test(tr, g, catalog, mask, n_real, seed_seq) -> Dict[str, Any]:
    """
    Estatística R = |media_k exp(i (arg C_k - arg c_k))| nas linhas selecionadas, com C_k lido
    na malha (ponto mais próximo de T_k). Controle: fases aleatórias independentes por ponto
    da malha, preservando |F|. Este controle conserva a potência e só testa coerência de fase.
    """
    idx_lines = np.where(mask)[0]
    if len(idx_lines) == 0:
        return {"status": "não executado: nenhuma linha selecionada"}
    F = tr.transform(g)
    T = np.array([catalog[k]["period_theoretical"] for k in idx_lines])
    c = np.array([catalog[k]["coefficient_theoretical"] for k in idx_lines])
    gi = np.clip(np.round((T - tr.t_grid[0]) / tr.dt).astype(int), 0, tr.n_t - 1)

    def stat(values):
        # a fase de F no lóbulo principal é a da linha, e^{i E_c T}; usa-se T exato
        C = 2.0 * values * np.exp(-1j * tr.E_c * T)
        return float(np.abs(np.mean(np.exp(1j * (np.angle(C) - np.angle(c))))))

    R_obs = stat(F[gi])
    rng = np.random.default_rng(seed_seq.spawn(1)[0])
    null = np.array([stat(np.abs(F[gi]) * np.exp(1j * rng.uniform(0, 2 * np.pi, size=len(gi)))) for _ in range(n_real)])
    return {
        "n_lines": int(len(gi)),
        "R_observed": R_obs,
        "R_null_mean": float(null.mean()),
        "R_null_q95": float(np.quantile(null, 0.95)),
        "p_value_mc": float((1 + np.sum(null >= R_obs)) / (n_real + 1)),
        "B": int(n_real),
        "note": "Controle de fase preserva |F|; não testa existência de picos de potência.",
    }
