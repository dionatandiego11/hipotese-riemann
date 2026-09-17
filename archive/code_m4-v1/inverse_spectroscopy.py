"""
riemann_spectra.inverse_spectroscopy
Orquestração das Etapas 7-9 (M3) para um bloco contíguo de zeros — protocolo m3-v3.

Ordem obrigatória dentro de `run_block`:
  1. instrumento F_w (janela e densidade da configuração) e diagnósticos (Etapa 7);
  2. nulos (sem catálogo), em TRÊS conjuntos independentes de sementes:
       sigma  -> perfil sigma_nulo(t);
       limiar -> distribuição do máximo de z, limiar FWER e p ajustado por pico;
       escore -> distribuição nula do escore global S, com o limiar já fixado;
     calibração sintética com linhas em períodos aleatórios uniformes (Etapa 8);
  3. detecção nos zeros, gravação de blind_peaks.csv e dos nulos, hash (congelamento);
  4. SOMENTE ENTÃO: módulo aritmético, matching, escore global, medição direcionada (Etapa 9).

Simetria (correção m3-v3): a estatística de decisão é z = |F(t_k)|/sigma(t_k) no ponto da malha,
idêntica para zeros, controles e sintéticos. A amplitude refinada por soma direta é apenas descritiva.
"""

import csv
import json
import logging
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
    classify_detection,
    detect_blind_peaks,
    max_statistic,
    null_noise_profile,
    threshold_interval,
)
from riemann_spectra.unfolding import d_bar_rvm, n_bar_rvm
from riemann_spectra.utils import compute_file_sha256

logger = logging.getLogger("riemann_spectra.inverse_spectroscopy")

# ---------------------------------------------------------------------------
# Instrumento: todos os parâmetros vêm da configuração (nenhum padrão implícito)
# ---------------------------------------------------------------------------

_WORKER_CACHE: Dict[Tuple, OscillatoryTransform] = {}


def instrument_params(g: np.ndarray, cfg: Dict[str, Any]) -> Tuple:
    """Tupla hashable com TODOS os parâmetros do instrumento, validados contra a configuração."""
    required = ["t_min", "t_max", "points_per_fwhm", "window", "density", "quadrature_panel_length", "quadrature_order"]
    missing = [k for k in required if k not in cfg]
    if missing:
        raise KeyError(f"Configuração M3 sem chaves obrigatórias: {missing}")
    return (float(g[0]), float(g[-1]), float(cfg["t_min"]), float(cfg["t_max"]), float(cfg["points_per_fwhm"]),
            str(cfg["window"]), str(cfg["density"]), float(cfg["quadrature_panel_length"]), int(cfg["quadrature_order"]))


def _instrument(params: Tuple) -> OscillatoryTransform:
    if params not in _WORKER_CACHE:
        _WORKER_CACHE.clear()
        A, B, t_min, t_max, ppf, window, density, panel, order = params
        _WORKER_CACHE[params] = OscillatoryTransform(
            A, B, t_min, t_max, points_per_fwhm=ppf, panel_length=panel, quad_order=order, density=density, window=window
        )
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
    return np.abs(tr.transform(_null_levels(kind, gammas, seed_state, gue_fraction))) ** 2


def _task_max(args) -> Tuple[float, np.ndarray, np.ndarray]:
    """Mesma rota dos zeros, sem `evaluator`: máximo de z na malha e candidatos (período refinado, z na malha)."""
    kind, gammas, seed_state, params, gue_fraction, sigma, fwhm, cand_z = args
    tr = _instrument(params)
    F = tr.transform(_null_levels(kind, gammas, seed_state, gue_fraction))
    peaks = detect_blind_peaks(tr.t_grid, F, fwhm, sigma, candidate_z=cand_z)
    return max_statistic(F, sigma), np.array([p["period"] for p in peaks]), np.array([p["z"] for p in peaks])


def _task_synthetic(args) -> List[Dict[str, float]]:
    """Linhas injetadas em níveis GUE; mesma estatística de decisão (z na malha)."""
    gammas, seed_state, params, gue_fraction, sigma, fwhm, thr, n_lines, z_range, pair_sep = args
    rng = np.random.default_rng(seed_state)
    tr = _instrument(params)
    t_min, t_max = params[2], params[3]
    n = len(gammas)
    y, _ = generate_gue_central_levels(n, gue_fraction, rng)
    x0, x1 = float(n_bar_rvm(gammas[0])), float(n_bar_rvm(gammas[-1]))
    x = x0 + (y - y[0]) * (x1 - x0) / (y[-1] - y[0])
    margin = 0.05
    if pair_sep is None:
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
    coef_mod = z_true * sig_T * 2.0 / tr.response["gain_W0"]
    C = coef_mod * np.exp(1j * rng.uniform(0, 2 * np.pi, size=len(T)))
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
    F = tr.transform(inject_density_lines(x, T, C))
    peaks = detect_blind_peaks(tr.t_grid, F, fwhm, sigma, candidate_z=min(3.0, thr))
    per = np.array([p["period"] for p in peaks if p["z"] >= thr])
    out = []
    for k in range(len(T)):
        err = float(per[int(np.argmin(np.abs(per - T[k])))] - T[k]) if len(per) else float("inf")
        out.append({"T": float(T[k]), "z_true": float(z_true[k]), "error": err, "coef_modulus": float(coef_mod[k])})
    return out


def _map(executor, fn, tasks):
    if executor is None:
        return [fn(t) for t in tasks]
    return list(executor.map(fn, tasks, chunksize=max(1, len(tasks) // 32)))


def _json_default(o):
    if isinstance(o, np.floating):
        return float(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(type(o))


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
    if i1 > len(gammas):
        raise ValueError(f"Bloco {name} pede índice {i1}, mas só há {len(gammas)} zeros carregados.")
    g = np.asarray(gammas[i0 - 1:i1], dtype=np.float64)
    alpha = cfg["alpha"]
    gue_fraction = cfg["gue_retained_fraction"]
    cand_z = cfg["candidate_z"]
    params = instrument_params(g, cfg)
    bdir = out_dir / name
    bdir.mkdir(parents=True, exist_ok=True)
    timings: Dict[str, float] = {}
    result: Dict[str, Any] = {"block": block, "protocol_version": cfg.get("protocol_version")}
    # sementes: todas geradas de uma vez, com papéis fixos
    ss_shuffle, ss_gue, ss_syn, ss_diag, ss_prec, ss_phase = seed_seq.spawn(6)

    # 1. Instrumento --------------------------------------------------------
    t0 = time.perf_counter()
    tr = _instrument(params)
    fwhm = tr.response["fwhm"]
    W0 = tr.response["gain_W0"]
    F = tr.transform(g)
    diag = tr.diagnostics(g, n_check=64, seed=int(ss_diag.generate_state(1)[0]))
    result["instrument"] = tr.to_metadata()
    result["instrument_diagnostics"] = diag
    timings["instrument"] = time.perf_counter() - t0
    logger.info(f"[{name}] janela={tr.window} densidade={tr.density} n={len(g)} L={tr.L:.1f} FWHM={fwhm:.3e} n_t={tr.n_t}; "
                f"NUFFT-direto={diag['nufft_vs_direct_max_abs_error']:.2e}")

    executor = ProcessPoolExecutor(max_workers=workers) if workers > 1 else None
    try:
        nulls: Dict[str, Dict[str, Any]] = {}
        for kind, child in (("shuffle", ss_shuffle), ("gue", ss_gue)):
            n_sigma = cfg[f"{kind}_sigma_realizations"]
            n_thr = cfg[f"{kind}_threshold_realizations"]
            n_score = cfg[f"{kind}_score_realizations"]
            t0 = time.perf_counter()
            s_sigma, s_thr, s_score = child.spawn(3)
            powers = _map(executor, _task_power, [(kind, g, s, params, gue_fraction) for s in s_sigma.spawn(n_sigma)])
            sigma = null_noise_profile(np.sqrt(np.array(powers)), tr.t_grid, cfg["noise_smooth_window"])
            del powers
            res_thr = _map(executor, _task_max, [(kind, g, s, params, gue_fraction, sigma, fwhm, cand_z) for s in s_thr.spawn(n_thr)])
            null_max = np.array([r[0] for r in res_thr])
            interval = threshold_interval(null_max, alpha, cfg["threshold_confidence"])
            thr = interval["z_high"]  # regra estrita: detecção exige z acima do limite superior do intervalo
            res_score = (_map(executor, _task_max, [(kind, g, s, params, gue_fraction, sigma, fwhm, cand_z) for s in s_score.spawn(n_score)])
                         if n_score > 0 else [])
            nulls[kind] = {
                "sigma": sigma,
                "null_max": null_max,
                "threshold": thr,
                "interval": interval,
                "score_set_peaks": [(r[1], r[2]) for r in res_score],
                "score_set_max": np.array([r[0] for r in res_score]),
                "B_sigma": n_sigma, "B_threshold": n_thr, "B_score": n_score,
            }
            timings[f"null_{kind}"] = time.perf_counter() - t0
            logger.info(f"[{name}] nulo {kind}: B_sigma={n_sigma} B_limiar={n_thr} B_escore={n_score} "
                        f"limiar z={interval['point_threshold']:.4f}, faixa inconclusiva [{interval['z_low']:.4f}, {interval['z_high']:.4f}] "
                        f"({timings[f'null_{kind}']:.1f} s)")

        primary = cfg["primary_null"]
        sigma_p, thr_p = nulls[primary]["sigma"], nulls[primary]["threshold"]

        t0 = time.perf_counter()
        n_syn = cfg["synthetic_realizations"]
        seps = cfg["synthetic_pair_separations_fwhm"]
        s_iso, s_pair = ss_syn.spawn(2)
        n_lines = cfg["synthetic_lines_per_realization"]
        iso_tasks = [(g, s, params, gue_fraction, sigma_p, fwhm, thr_p, n_lines, (0.5 * thr_p, 4.0 * thr_p), None) for s in s_iso.spawn(n_syn)]
        iso = [row for rows in _map(executor, _task_synthetic, iso_tasks) for row in rows]
        pair_seeds = s_pair.spawn(n_syn)
        pair_rows = []
        for k, sep in enumerate(seps):
            tasks = [(g, s, params, gue_fraction, sigma_p, fwhm, thr_p, 2 * max(1, n_lines // 4), (2.0 * thr_p, 4.0 * thr_p), sep)
                     for s in pair_seeds[k::len(seps)]]
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
    logger.info(f"[{name}] sintético: {calib['n_isolated_lines']} linhas; tolerância={tol:.3e} ({tol/fwhm:.3f} FWHM); "
                f"separação resolvida={res_sep/fwhm:.2f} FWHM")

    # 3. Detecção nos zeros (decisão na malha) e congelamento -------------------
    peaks = detect_blind_peaks(tr.t_grid, F, fwhm, sigma_p, candidate_z=cand_z, evaluator=lambda t: tr.evaluate(g, t))
    secondary = "gue" if primary == "shuffle" else "shuffle"
    for p in peaks:
        gi = p["grid_index"]
        p["p_adjusted_primary"] = float(adjusted_p_values([p["z"]], nulls[primary]["null_max"])[0])
        p["class_primary"] = classify_detection(p["z"], nulls[primary]["interval"])
        p["detected_primary"] = p["class_primary"] == "detected"
        p["z_secondary"] = float(np.abs(F[gi]) / nulls[secondary]["sigma"][gi])
        p["p_adjusted_secondary"] = float(adjusted_p_values([p["z_secondary"]], nulls[secondary]["null_max"])[0])
        p["class_secondary"] = classify_detection(p["z_secondary"], nulls[secondary]["interval"])
        p["detected_secondary"] = p["class_secondary"] == "detected"
        p["fwhm_instrument"] = fwhm

    blind_csv = bdir / "blind_peaks.csv"
    cols = ["grid_period", "period", "fwhm_instrument", "z", "p_adjusted_primary", "class_primary", "detected_primary",
            "z_secondary", "p_adjusted_secondary", "class_secondary", "detected_secondary",
            "z_refined", "amplitude_real", "amplitude_imag", "modulus", "phase_rad", "null_noise_rms"]
    with open(blind_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["peak_id"] + cols)
        for k, p in enumerate(peaks):
            w.writerow([k] + [repr(p[c]) if isinstance(p[c], float) else p[c] for c in cols])
    null_npz = bdir / "nulls.npz"
    np.savez_compressed(
        null_npz, t_grid=tr.t_grid, F_real=F.real, F_imag=F.imag,
        **{f"{k}_sigma": v["sigma"] for k, v in nulls.items()},
        **{f"{k}_null_max": v["null_max"] for k, v in nulls.items()},
        **{f"{k}_score_set_max": v["score_set_max"] for k, v in nulls.items()},
    )
    n_refined_would_differ = int(sum(classify_detection(p["z_refined"], nulls[primary]["interval"]) != p["class_primary"] for p in peaks))
    freeze = {
        "blind_peaks_csv": str(blind_csv),
        "blind_peaks_sha256": compute_file_sha256(blind_csv),
        "nulls_npz_sha256": compute_file_sha256(null_npz),
        "frozen_before_arithmetic": True,
        "decision_statistic": "z na malha (idêntica para zeros, controles e sintéticos)",
        "n_candidates": len(peaks),
        "decision_rule": "detected se z > limite superior do IC do quantil; inconclusivo dentro do IC; não detectado abaixo",
        "n_detected_primary": int(sum(p["detected_primary"] for p in peaks)),
        "n_inconclusive_primary": int(sum(p["class_primary"] == "inconclusive" for p in peaks)),
        "n_detected_secondary": int(sum(p["detected_secondary"] for p in peaks)),
        "n_inconclusive_secondary": int(sum(p["class_secondary"] == "inconclusive" for p in peaks)),
        "n_candidates_whose_decision_would_change_with_refined_z": n_refined_would_differ,
    }
    with open(bdir / "freeze.json", "w", encoding="utf-8") as f:
        json.dump(freeze, f, indent=2)
    result["freeze"] = freeze
    result["null_summary"] = {
        k: {
            "B_sigma": v["B_sigma"], "B_threshold": v["B_threshold"], "B_score": v["B_score"],
            "threshold_z": v["threshold"],
            "threshold_interval": v["interval"],
            "null_max_quantiles": np.quantile(v["null_max"], [0.05, 0.5, 0.95]).tolist(),
            "score_set_fraction_max_above_threshold": float(np.mean(v["score_set_max"] >= v["threshold"])) if len(v["score_set_max"]) else None,
            "sigma_at_t": {str(tt): float(np.interp(tt, tr.t_grid, v["sigma"])) for tt in (0.7, 1.0, 2.0, 3.0, 4.0, 4.9)},
        } for k, v in nulls.items()
    }
    result["zeros_background"] = {
        "median_abs_F_over_sigma_primary": float(np.median(np.abs(F) / sigma_p)),
        "median_abs_F_over_sigma_secondary": float(np.median(np.abs(F) / nulls[secondary]["sigma"])),
        "note": "Mediana ao longo de toda a malha, incluindo linhas.",
    }
    logger.info(f"[{name}] congelado: {freeze['n_detected_primary']} detecções, {freeze['n_inconclusive_primary']} inconclusivas ({primary}); "
                f"decisões que mudariam com z refinado: {n_refined_would_differ}; SHA-256 {freeze['blind_peaks_sha256'][:16]}…")

    # 4. Comparação aritmética (após o congelamento) --------------------------
    from riemann_spectra import arithmetic as ar  # importação deliberadamente tardia

    t0 = time.perf_counter()
    result["arithmetic"] = arithmetic_comparison(ar, tr, g, peaks, nulls, primary, tol, res_sep, bdir, cfg, ss_prec, ss_phase)
    timings["arithmetic"] = time.perf_counter() - t0
    result["timings_seconds"] = timings
    with open(bdir / "block_metrics.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, default=_json_default)
    return result


def summarize_synthetic(iso: List[Dict], pairs: List[Dict], fwhm: float, thr: float, cfg: Dict[str, Any]) -> Dict[str, Any]:
    """Tolerância de matching, curva de recuperação e separação mínima resolvida."""
    iso_z = np.array([r["z_true"] for r in iso])
    iso_err = np.array([r["error"] for r in iso])
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
        ok = float(np.mean([abs(r["error"]) <= tol for r in rows])) if rows else 0.0
        sep_curve.append({"separation_fwhm": sep, "n_lines": len(rows), "fraction_lines_recovered": ok})
        if res_sep is None and rows and ok >= cfg["resolution_recovery_target"]:
            res_sep = sep
    res_sep_status = "medida"
    if res_sep is None:
        res_sep = max(seps) if seps else 2.0
        res_sep_status = "não atingiu a meta; usada a maior separação testada"
    return {
        "n_isolated_lines": int(len(iso)),
        "matching_tolerance": tol,
        "matching_tolerance_fwhm": tol / fwhm,
        "matching_tolerance_quantile": q,
        "recovery_curve": curve,
        "pair_resolution_curve": sep_curve,
        "resolution_separation_fwhm": float(res_sep),
        "resolution_separation": float(res_sep * fwhm),
        "resolution_separation_status": res_sep_status,
    }


def _fit_summary(fit: List[Dict[str, Any]], mask: np.ndarray, reps: np.ndarray) -> Dict[str, Any]:
    ratios = np.array([f["ratio_to_theory"] for f in fit])
    phases = np.array([f["phase_error_rad"] for f in fit])
    if not mask.any():
        return {"status": "nenhuma linha selecionada"}
    rep_mask = mask & (reps > 1)
    return {
        "n_lines": int(mask.sum()),
        "median_abs_ratio_minus_1": float(np.median(np.abs(ratios[mask] - 1.0))),
        "max_abs_ratio_minus_1": float(np.max(np.abs(ratios[mask] - 1.0))),
        "median_abs_phase_error_rad": float(np.median(np.abs(phases[mask]))),
        "median_abs_ratio_minus_1_repetitions": float(np.median(np.abs(ratios[rep_mask] - 1.0))) if rep_mask.any() else None,
        "fit_residual_rms": fit[0]["fit_residual_rms"],
        "design_condition_number": fit[0]["design_condition_number"],
    }


def arithmetic_comparison(ar, tr, g, peaks, nulls, primary, tol, res_sep, bdir, cfg, ss_prec, ss_phase) -> Dict[str, Any]:
    fwhm = tr.response["fwhm"]
    W0 = tr.response["gain_W0"]
    catalog = ar.prime_power_catalog(float(tr.t_grid[0]), float(tr.t_grid[-1]))
    ar.flag_unresolved(catalog, res_sep)
    reps = np.array([c["repetition"] for c in catalog])

    crit = cfg["criteria"]
    interval = nulls[primary]["interval"]
    det_peaks = [p for p in peaks if p["class_primary"] == "detected"]
    inc_peaks = [p for p in peaks if p["class_primary"] == "inconclusive"]
    assign, summary = ar.match_one_to_one(np.array([p["period"] for p in det_peaks]), catalog, tol)
    _, summary_incl = ar.match_one_to_one(np.array([p["period"] for p in det_peaks + inc_peaks]), catalog, tol)

    # Escore global S (regra estrita) calibrado no conjunto "escore", independente do conjunto do limiar.
    # Sensibilidade: S incluindo inconclusivos, com a mesma regra (z >= limite inferior) nos nulos.
    thr_p = interval["z_high"]
    null_scores, null_scores_incl, null_dets = [], [], []
    for per, zz in nulls[primary]["score_set_peaks"]:
        strict = per[zz > interval["z_high"]] if len(per) else per
        loose = per[zz >= interval["z_low"]] if len(per) else per
        null_scores.append(ar.match_one_to_one(strict, catalog, tol)[1]["n_matched"])
        null_scores_incl.append(ar.match_one_to_one(loose, catalog, tol)[1]["n_matched"])
        null_dets.append(len(strict))
    null_scores = np.array(null_scores)
    null_scores_incl = np.array(null_scores_incl)
    B = len(null_scores)
    S = summary["n_matched"]
    S_incl = summary_incl["n_matched"]
    p_global = float((1 + np.sum(null_scores >= S)) / (B + 1)) if B else None
    p_global_incl = float((1 + np.sum(null_scores_incl >= S_incl)) / (B + 1)) if B else None

    # Medição direcionada: estimador primário e variantes de sensibilidade (declaradas no protocolo)
    half = cfg["targeted_fit_half_width_fwhm"] * fwhm
    evaluator = lambda t: tr.evaluate(g, t)  # noqa: E731
    variants = {}
    for vname, vcfg in cfg["targeted_fit_variants"].items():
        variants[vname] = ar.targeted_joint_fit(evaluator, catalog, tr.L, tr.E_c, half_width=half, window=tr.window,
                                                sampling=vcfg["sampling"], include_conjugate=vcfg["include_conjugate"])
    primary_fit_name = cfg["targeted_fit_primary"]
    fit = variants[primary_fit_name]

    sig_T = np.interp([c["period_theoretical"] for c in catalog], tr.t_grid, nulls[primary]["sigma"])
    inc_periods = np.array([p["period"] for p in inc_peaks])
    rows = []
    for k, c in enumerate(catalog):
        lim = ar.detection_limit_coefficient(sig_T[k], thr_p, W0)
        z_pred = abs(c["coefficient_theoretical"]) * W0 / (2.0 * sig_T[k])
        pk = det_peaks[assign[k]] if k in assign else None
        near_inc = bool(len(inc_periods) and np.min(np.abs(inc_periods - c["period_theoretical"])) <= tol)
        fr = fit[k]
        row = {
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
            "predicted_detectable": bool(abs(c["coefficient_theoretical"]) >= lim),
            "z_predicted": z_pred,
            "clearly_detectable": bool(z_pred >= crit["clear_margin"] * thr_p),
            "detected": pk is not None,
            "inconclusive_candidate_within_tolerance": near_inc and pk is None,
            "resolved": c["resolved"],
            "nearest_neighbor_separation": c["nearest_neighbor_separation"],
        }
        for vname, vfit in variants.items():
            if vname != primary_fit_name:
                row[f"ratio_to_theory__{vname}"] = vfit[k]["ratio_to_theory"]
        rows.append(row)
    with open(bdir / "arithmetic_matches.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if v is None else v) for k, v in r.items()})

    used = set(assign.values())
    unmatched = [p for i, p in enumerate(det_peaks) if i not in used]
    Tcat = np.array([c["period_theoretical"] for c in catalog])
    with open(bdir / "unmatched_detections.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["period", "z", "p_adjusted", "modulus", "nearest_catalog_period", "distance_fwhm"])
        for p in unmatched:
            j = int(np.argmin(np.abs(Tcat - p["period"])))
            w.writerow([p["period"], p["z"], p["p_adjusted_primary"], p["modulus"], Tcat[j], abs(Tcat[j] - p["period"]) / fwhm])

    with open(bdir / "inconclusive_candidates.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["period", "z", "z_low", "z_high", "nearest_catalog_period", "nearest_prime", "nearest_repetition", "distance_fwhm"])
        for p in inc_peaks:
            j = int(np.argmin(np.abs(Tcat - p["period"])))
            w.writerow([p["period"], p["z"], interval["z_low"], interval["z_high"], Tcat[j], catalog[j]["prime"], catalog[j]["repetition"],
                        abs(Tcat[j] - p["period"]) / fwhm])

    detectable = np.array([r["predicted_detectable"] for r in rows])
    clear = np.array([r["clearly_detectable"] for r in rows])
    detected = np.array([r["detected"] for r in rows])
    resolved = np.array([r["resolved"] for r in rows])
    good = resolved & clear
    ratios = np.array([r["fit_ratio_to_theory"] for r in rows])
    eligible_dev = np.abs(ratios[good] - 1.0)

    # Sensibilidade a perturbações de ±eps nas ordenadas (estimador primário)
    eps = cfg["declared_table_error"]
    rng_p = np.random.default_rng(ss_prec)
    pvcfg = cfg["targeted_fit_variants"][primary_fit_name]
    changes = []
    for _ in range(cfg["precision_perturbations"]):
        gp = g + rng_p.uniform(-eps, eps, size=len(g))
        fp = ar.targeted_joint_fit(lambda t: tr.evaluate(gp, t), catalog, tr.L, tr.E_c, half_width=half, window=tr.window,
                                   sampling=pvcfg["sampling"], include_conjugate=pvcfg["include_conjugate"])
        changes.append(np.array([x["ratio_to_theory"] for x in fp]) - ratios)
    changes = np.abs(np.array(changes))
    all_lines = np.ones(len(catalog), dtype=bool)
    return {
        "catalog_size": len(catalog),
        "catalog_primitive": int(np.sum(reps == 1)),
        "catalog_repetitions": int(np.sum(reps > 1)),
        "catalog_resolved": int(resolved.sum()),
        "matching_tolerance": tol,
        "detected_peaks_primary": len(det_peaks),
        "matched_S": S,
        "unmatched_detections": len(unmatched),
        "score_calibration_set": "independente do conjunto de limiar",
        "B_score": B,
        "null_S_mean": float(null_scores.mean()) if B else None,
        "null_S_max": int(null_scores.max()) if B else None,
        "null_detections_mean": float(np.mean(null_dets)) if B else None,
        "p_value_global_mc": p_global,
        "p_value_floor": 1.0 / (B + 1) if B else None,
        "inconclusive_candidates": len(inc_peaks),
        "inconclusive_matching_catalog": int(summary_incl["n_matched"] - S),
        "matched_S_including_inconclusive": S_incl,
        "p_value_global_mc_including_inconclusive": p_global_incl,
        "threshold_interval": interval,
        "predicted_detectable": int(detectable.sum()),
        "clearly_detectable": int(clear.sum()),
        "recovery_among_clearly_detectable": float(detected[clear].mean()) if clear.any() else None,
        "clear_margin": crit["clear_margin"],
        "recovery_among_predicted_detectable": float(detected[detectable].mean()) if detectable.any() else None,
        "coefficient_agreement": {
            "estimator": primary_fit_name,
            "eligible_rule": "resolvida e claramente detectável (z previsto >= margem x limite superior)",
            "n_eligible": int(good.sum()),
            "ratio_tolerance": crit["ratio_tolerance"],
            "fraction_within_tolerance": float(np.mean(eligible_dev <= crit["ratio_tolerance"])) if good.any() else None,
            "median_abs_ratio_minus_1": float(np.median(eligible_dev)) if good.any() else None,
            "max_abs_ratio_minus_1": float(np.max(eligible_dev)) if good.any() else None,
        },
        "detected_but_predicted_undetectable": int((detected & ~detectable).sum()),
        "missed_predicted_detectable": [(r["prime"], r["repetition"]) for r in rows if r["predicted_detectable"] and not r["detected"]],
        "targeted_fit": {
            "primary_estimator": primary_fit_name,
            "variants": {
                vname: {"resolved_and_detectable": _fit_summary(vf, good, reps), "all_catalog_lines": _fit_summary(vf, all_lines, reps)}
                for vname, vf in variants.items()
            },
            "max_abs_difference_between_variants_ratio_selected": float(np.max(np.ptp(
                np.array([[x["ratio_to_theory"] for x in vf] for vf in variants.values()])[:, good], axis=0))) if good.any() and len(variants) > 1 else None,
        },
        "phase_coherence": phase_coherence_test(tr, tr.transform(g), catalog, good, cfg["phase_control_realizations"], ss_phase),
        "precision_sensitivity": {
            "perturbation_half_width": eps,
            "realizations": int(cfg["precision_perturbations"]),
            "estimator": primary_fit_name,
            "median_abs_ratio_change_selected_lines": float(np.median(changes[:, good])) if good.any() else None,
            "max_abs_ratio_change_selected_lines": float(np.max(changes[:, good])) if good.any() else None,
            "note": "Sensibilidade a perturbações uniformes; não é intervalo de confiança nem limite para erros de janela, modelo ou truncamento.",
        },
    }


def phase_coherence_test(tr, F, catalog, mask, n_real, seed) -> Dict[str, Any]:
    """
    Duas estatísticas nas linhas selecionadas, com C_k lido na malha (ponto mais próximo de T_k):
      R = |media exp(i erro_k)|  — alinhamento; invariante a rotação comum de todas as fases;
      Q = media cos(erro_k)      — sensível ao sinal absoluto (Q = 1 se todas as fases coincidem com a referência).
    Controle: fases independentes uniformes por linha, preservando |F|. Não testa potência.
    """
    idx_lines = np.where(mask)[0]
    if len(idx_lines) == 0:
        return {"status": "não executado: nenhuma linha selecionada"}
    T = np.array([catalog[k]["period_theoretical"] for k in idx_lines])
    c = np.array([catalog[k]["coefficient_theoretical"] for k in idx_lines])
    gi = np.clip(np.round((T - tr.t_grid[0]) / tr.dt).astype(int), 0, tr.n_t - 1)

    def stats(values):
        err = np.angle(values * np.exp(-1j * tr.E_c * T)) - np.angle(c)
        return float(np.abs(np.mean(np.exp(1j * err)))), float(np.mean(np.cos(err)))

    R_obs, Q_obs = stats(F[gi])
    rng = np.random.default_rng(seed)
    null = np.array([stats(np.abs(F[gi]) * np.exp(1j * rng.uniform(0, 2 * np.pi, size=len(gi)))) for _ in range(n_real)])
    return {
        "n_lines": int(len(gi)),
        "R_observed": R_obs, "R_null_q95": float(np.quantile(null[:, 0], 0.95)),
        "p_value_R": float((1 + np.sum(null[:, 0] >= R_obs)) / (n_real + 1)),
        "Q_observed": Q_obs, "Q_null_q95": float(np.quantile(null[:, 1], 0.95)),
        "p_value_Q": float((1 + np.sum(null[:, 1] >= Q_obs)) / (n_real + 1)),
        "B": int(n_real),
        "note": "R mede alinhamento (invariante a rotação comum); Q testa também o sinal absoluto. Controle preserva |F|.",
    }
