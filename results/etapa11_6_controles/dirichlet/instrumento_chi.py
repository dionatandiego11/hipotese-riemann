"""
Instrumento m4-v3 adaptado a L(s, χ) — controle `ctrl-dirichlet-v1` (declaração §§3 e 5; D1 §§3–4).

O código congelado de `riemann_spectra` NÃO é editado (o lock `package` de m4-v3 cobre todos os
módulos do pacote); este arquivo fica fora do pacote e só IMPORTA funções dele. Diferenças em
relação a `riemann_spectra.inverse_spectroscopy.run_block`, todas declaradas:

  1. densidade suave d̄_χ(E) = (1/2π) log(qE/2π) (P2) no termo suave do instrumento, no unfolding
     dos controles nulos (shuffle e GUE) e na injeção de linhas sintéticas;
     contagem suave N̄_χ(E) = (E/2π)(log(qE/2π) − 1) + κ/4 − 1/8 (primitiva de d̄_χ; a constante
     vem do termo constante de θ_χ/π por Stirling e não afeta espaçamentos);
  2. catálogo com coeficientes c_χ(n) = −Λ(n)χ(n)/(π√n) (P1); linhas com χ(n) = 0 ficam no catálogo
     com coeficiente 0 ("ausentes previstas");
  3. janela exigida B > A > 2π/q (em vez de 2π), pois o primeiro zero de L(s, χ₋₄) está abaixo de 2π.

Todo o resto (malha, janela de Hann, quadratura, NUFFT, detector, nulos, limiar, calibração
sintética, matching, medição direcionada, teste de fase) é a mesma função do pacote.
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import math
import sys
import time
import tomllib
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, List, Tuple

import numpy as np
from scipy.special import digamma

from riemann_spectra import arithmetic as _ar
from riemann_spectra.controls import generate_gue_central_levels, shuffle_spacings
from riemann_spectra.inverse_spectroscopy import (
    _json_default,
    _map,
    arithmetic_comparison,
    summarize_synthetic,
)
from riemann_spectra.periods import (
    OscillatoryTransform,
    adjusted_p_values,
    classify_detection,
    detect_blind_peaks,
    local_gauss_legendre_panels,
    max_statistic,
    measure_window_response,
    null_noise_profile,
    nufft_uniform_t,
    threshold_interval,
    window_coefficients,
)
from riemann_spectra.replication import evaluate_m3_family
from riemann_spectra.utils import compute_file_sha256

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dirichlet_zeros import CHARACTERS, Character  # noqa: E402

logger = logging.getLogger("ctrl_dirichlet")
TWO_PI = 2.0 * math.pi

# ---------------------------------------------------------------------------
# 1. Densidade e contagem suaves com q (P2)
# ---------------------------------------------------------------------------


def d_bar_chi(E, q: int):
    return (1.0 / TWO_PI) * np.log(q * np.asarray(E, dtype=np.float64) / TWO_PI)


def n_bar_chi(E, q: int, kappa: int):
    E = np.asarray(E, dtype=np.float64)
    y = E / TWO_PI
    return y * (np.log(q * y) - 1.0) + 0.25 * kappa - 0.125


def d_theta_chi(E, q: int, kappa: int):
    """Densidade exata θ_χ′(E)/π = (1/2π)[Re ψ(a + iE/2) + log(q/π)] (diagnóstico, D1 §4)."""
    a = 0.25 + 0.5 * kappa
    E = np.asarray(E, dtype=np.float64)
    return (np.real(digamma(a + 0.5j * E)) + math.log(q / math.pi)) / TWO_PI


def inverse_n_bar_chi(x, q: int, kappa: int, tol: float = 1e-12, max_iter: int = 80):
    """Newton em N̄_χ(E) = x no domínio E > 2π/q (onde d̄_χ > 0)."""
    x = np.atleast_1d(np.asarray(x, dtype=np.float64))
    E_min = TWO_PI / q * (1.0 + 1e-9)
    E = np.maximum(TWO_PI * np.maximum(x, 1.0) / np.maximum(np.log(np.maximum(q * np.maximum(x, 1.0), 2.0)), 0.5), E_min * 2)
    for _ in range(max_iter):
        f = n_bar_chi(E, q, kappa) - x
        fp = d_bar_chi(E, q)
        step = f / np.maximum(fp, 1e-15)
        E_new = np.maximum(E - step, E_min + 0.5 * (E - E_min))
        done = np.max(np.abs(E_new - E)) < tol * max(1.0, float(np.max(E)))
        E = E_new
        if done:
            break
    return E


def unfold_chi(g, q, kappa):
    x = n_bar_chi(g, q, kappa)
    return x, np.diff(x)


def fold_chi(x, q, kappa):
    return inverse_n_bar_chi(x, q, kappa)


# ---------------------------------------------------------------------------
# 2. Instrumento com d̄_χ (cópia do construtor de OscillatoryTransform com a densidade trocada)
# ---------------------------------------------------------------------------


class ChiTransform(OscillatoryTransform):
    """
    Mesmo instrumento de `OscillatoryTransform`; o construtor é reescrito só para (i) usar d̄_χ no termo
    suave e (ii) exigir A > 2π/q. `transform`, `evaluate`, `_select` e `_window_at_offsets` são herdados.
    """

    def __init__(self, A, B, t_min, t_max, q, kappa, points_per_fwhm=8.0, panel_length=0.5, quad_order=8, window="hann"):
        if not (B > A > TWO_PI / q):
            raise ValueError("A janela deve satisfazer B > A > 2π/q.")
        window_coefficients(window)
        self.q, self.kappa = int(q), int(kappa)
        self.window = window
        self.A, self.B = float(A), float(B)
        self.L = self.B - self.A
        self.E_c = 0.5 * (self.A + self.B)
        self.response = measure_window_response(self.L, window)
        self.dt = self.response["fwhm"] / points_per_fwhm
        self.n_t = int(math.floor((t_max - t_min) / self.dt)) + 1
        self.t_grid = t_min + self.dt * np.arange(self.n_t)
        self.density = f"chi_q{self.q}"
        self.panel_length = panel_length
        self.quad_order = quad_order
        self._quad_offsets, self._quad_weights = local_gauss_legendre_panels(self.L, panel_length, quad_order)
        self._quad_nodes = self.A + self._quad_offsets
        self._quad_u = self._quad_offsets - 0.5 * self.L
        self._quad_coeffs = self._window_at_offsets(self._quad_offsets) * d_bar_chi(self._quad_nodes, self.q) * self._quad_weights
        self.smooth = nufft_uniform_t(self._quad_u, self._quad_coeffs, self.t_grid[0], self.dt, self.n_t)

    def diagnostics(self, levels, n_check=64, seed=0):
        rng = np.random.default_rng(seed)
        idx = np.sort(rng.choice(self.n_t, size=min(n_check, self.n_t), replace=False))
        F_grid = self.transform(levels)
        F_direct = self.evaluate(levels, self.t_grid[idx])
        off2, w2 = local_gauss_legendre_panels(self.L, 0.5 * self.panel_length, self.quad_order)
        c2 = self._window_at_offsets(off2) * d_bar_chi(self.A + off2, self.q) * w2
        smooth2 = nufft_uniform_t(off2 - 0.5 * self.L, c2, self.t_grid[0], self.dt, self.n_t)
        c_alt = self._window_at_offsets(self._quad_offsets) * d_theta_chi(self._quad_nodes, self.q, self.kappa) * self._quad_weights
        smooth_alt = nufft_uniform_t(self._quad_u, c_alt, self.t_grid[0], self.dt, self.n_t)
        return {
            "n_t": self.n_t, "dt": self.dt, "points_per_fwhm": self.response["fwhm"] / self.dt,
            "max_abs_F": float(np.max(np.abs(F_grid))),
            "nufft_vs_direct_max_abs_error": float(np.max(np.abs(F_grid[idx] - F_direct))),
            "quadrature_halving_max_abs_change": float(np.max(np.abs(smooth2 - self.smooth))),
            "density_chi_vs_theta_chi_max_abs_change": float(np.max(np.abs(smooth_alt - self.smooth))),
            "quadrature_nodes": int(len(self._quad_nodes)),
        }


_CACHE: Dict[Tuple, ChiTransform] = {}


def instrument_params(g, cfg, ch: Character) -> Tuple:
    return (float(g[0]), float(g[-1]), float(cfg["t_min"]), float(cfg["t_max"]), float(cfg["points_per_fwhm"]),
            str(cfg["window"]), ch.q, ch.kappa, float(cfg["quadrature_panel_length"]), int(cfg["quadrature_order"]))


def _instrument(params) -> ChiTransform:
    if params not in _CACHE:
        A, B, t_min, t_max, ppf, window, q, kappa, panel, order = params
        _CACHE.clear()
        _CACHE[params] = ChiTransform(A, B, t_min, t_max, q, kappa, points_per_fwhm=ppf, panel_length=panel,
                                      quad_order=order, window=window)
    return _CACHE[params]


# ---------------------------------------------------------------------------
# 3. Controles nulos e linhas sintéticas com unfolding por N̄_χ (mesma lógica de `riemann_spectra.controls`)
# ---------------------------------------------------------------------------


def shuffled_levels_chi(g, rng, q, kappa):
    x, s = unfold_chi(np.asarray(g, dtype=np.float64), q, kappa)
    return fold_chi(shuffle_spacings(s, origin_x=float(x[0]), rng=rng), q, kappa)


def gue_levels_chi(g, fraction, rng, q, kappa):
    g = np.asarray(g, dtype=np.float64)
    n = len(g)
    y, _ = generate_gue_central_levels(n, fraction, rng)
    x0, x1 = float(n_bar_chi(g[0], q, kappa)), float(n_bar_chi(g[-1], q, kappa))
    return fold_chi(x0 + (y - y[0]) * (x1 - x0) / (y[-1] - y[0]), q, kappa)


def inject_lines_chi(x, T, C, q, kappa, tol=1e-11, max_iter=60):
    """Resolve N̄_χ(E) + Σ Re[C e^{iET}/(iT)] = x (mesma construção de `controls.inject_density_lines`)."""
    x = np.asarray(x, dtype=np.float64)
    T = np.asarray(T, dtype=np.float64)
    C = np.asarray(C, dtype=np.complex128)
    E = fold_chi(x, q, kappa)
    for _ in range(max_iter):
        ph = np.exp(1j * np.outer(E, T))
        f = n_bar_chi(E, q, kappa) + np.real(ph @ (C / (1j * T))) - x
        fp = d_bar_chi(E, q) + np.real(ph @ C)
        if np.any(fp <= 0):
            raise ValueError("Densidade modulada não positiva: reduza os coeficientes injetados.")
        step = f / fp
        E = E - step
        if np.max(np.abs(step)) < tol:
            break
    return E


def _null_levels(kind, g, seed_state, fraction, q, kappa):
    rng = np.random.default_rng(seed_state)
    if kind == "shuffle":
        return shuffled_levels_chi(g, rng, q, kappa)
    if kind == "gue":
        return gue_levels_chi(g, fraction, rng, q, kappa)
    raise ValueError(kind)


def _task_power(args):
    kind, g, seed_state, params, fraction = args
    tr = _instrument(params)
    return np.abs(tr.transform(_null_levels(kind, g, seed_state, fraction, params[6], params[7]))) ** 2


def _task_max(args):
    kind, g, seed_state, params, fraction, sigma, fwhm, cand_z = args
    tr = _instrument(params)
    F = tr.transform(_null_levels(kind, g, seed_state, fraction, params[6], params[7]))
    peaks = detect_blind_peaks(tr.t_grid, F, fwhm, sigma, candidate_z=cand_z)
    return max_statistic(F, sigma), np.array([p["period"] for p in peaks]), np.array([p["z"] for p in peaks])


def _task_synthetic(args):
    """Cópia de `inverse_spectroscopy._task_synthetic` com N̄_χ e d̄_χ."""
    g, seed_state, params, fraction, sigma, fwhm, thr, n_lines, z_range, pair_sep = args
    q, kappa = params[6], params[7]
    rng = np.random.default_rng(seed_state)
    tr = _instrument(params)
    t_min, t_max = params[2], params[3]
    n = len(g)
    y, _ = generate_gue_central_levels(n, fraction, rng)
    x0, x1 = float(n_bar_chi(g[0], q, kappa)), float(n_bar_chi(g[-1], q, kappa))
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
    budget = 0.8 * float(d_bar_chi(g[0], q))
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
    F = tr.transform(inject_lines_chi(x, T, C, q, kappa))
    peaks = detect_blind_peaks(tr.t_grid, F, fwhm, sigma, candidate_z=min(3.0, thr))
    per = np.array([p["period"] for p in peaks if p["z"] >= thr])
    out = []
    for k in range(len(T)):
        err = float(per[int(np.argmin(np.abs(per - T[k])))] - T[k]) if len(per) else float("inf")
        out.append({"T": float(T[k]), "z_true": float(z_true[k]), "error": err, "coef_modulus": float(coef_mod[k])})
    return out


# ---------------------------------------------------------------------------
# 4. Catálogo com χ (P1)
# ---------------------------------------------------------------------------


def chi_catalog_module(ch: Character) -> SimpleNamespace:
    """Módulo substituto passado a `arithmetic_comparison`: só `prime_power_catalog` muda."""

    def prime_power_catalog(t_min, t_max):
        cat = _ar.prime_power_catalog(t_min, t_max)
        for c in cat:
            chi_n = ch(c["prime"]) ** c["repetition"]
            c["chi"] = chi_n
            c["coefficient_zeta"] = c["coefficient_theoretical"]
            c["coefficient_theoretical"] = c["coefficient_zeta"] * chi_n
        return cat

    return SimpleNamespace(
        prime_power_catalog=prime_power_catalog,
        flag_unresolved=_ar.flag_unresolved,
        match_one_to_one=_ar.match_one_to_one,
        targeted_joint_fit=_ar.targeted_joint_fit,
        detection_limit_coefficient=_ar.detection_limit_coefficient,
    )


# ---------------------------------------------------------------------------
# 5. Bloco (mesma ordem de `inverse_spectroscopy.run_block`)
# ---------------------------------------------------------------------------


def run_block_chi(gammas, block, cfg, ch: Character, out_dir: Path, seed_seq, workers=1) -> Dict[str, Any]:
    name = block["name"]
    i0, i1 = block["first_index"], block["last_index"]
    if i1 > len(gammas):
        raise ValueError(f"Bloco {name} pede índice {i1}, mas só há {len(gammas)} zeros.")
    g = np.asarray(gammas[i0 - 1:i1], dtype=np.float64)
    alpha, fraction, cand_z = cfg["alpha"], cfg["gue_retained_fraction"], cfg["candidate_z"]
    params = instrument_params(g, cfg, ch)
    bdir = out_dir / name
    bdir.mkdir(parents=True, exist_ok=True)
    timings: Dict[str, float] = {}
    result: Dict[str, Any] = {"block": block, "protocol_version": cfg["protocol_version"],
                              "character": {"name": ch.name, "q": ch.q, "kappa": ch.kappa}}
    ss_shuffle, ss_gue, ss_syn, ss_diag, ss_prec, ss_phase = seed_seq.spawn(6)

    t0 = time.perf_counter()
    tr = _instrument(params)
    fwhm, W0 = tr.response["fwhm"], tr.response["gain_W0"]
    F = tr.transform(g)
    result["instrument"] = tr.to_metadata()
    result["instrument_diagnostics"] = tr.diagnostics(g, n_check=64, seed=int(ss_diag.generate_state(1)[0]))
    timings["instrument"] = time.perf_counter() - t0

    executor = ProcessPoolExecutor(max_workers=workers) if workers > 1 else None
    try:
        nulls: Dict[str, Dict[str, Any]] = {}
        for kind, child in (("shuffle", ss_shuffle), ("gue", ss_gue)):
            n_sigma, n_thr, n_score = cfg[f"{kind}_sigma_realizations"], cfg[f"{kind}_threshold_realizations"], cfg[f"{kind}_score_realizations"]
            t0 = time.perf_counter()
            s_sigma, s_thr, s_score = child.spawn(3)
            powers = _map(executor, _task_power, [(kind, g, s, params, fraction) for s in s_sigma.spawn(n_sigma)])
            sigma = null_noise_profile(np.sqrt(np.array(powers)), tr.t_grid, cfg["noise_smooth_window"])
            res_thr = _map(executor, _task_max, [(kind, g, s, params, fraction, sigma, fwhm, cand_z) for s in s_thr.spawn(n_thr)])
            null_max = np.array([r[0] for r in res_thr])
            interval = threshold_interval(null_max, alpha, cfg["threshold_confidence"])
            res_score = (_map(executor, _task_max, [(kind, g, s, params, fraction, sigma, fwhm, cand_z) for s in s_score.spawn(n_score)])
                         if n_score > 0 else [])
            nulls[kind] = {"sigma": sigma, "null_max": null_max, "threshold": interval["z_high"], "interval": interval,
                           "score_set_peaks": [(r[1], r[2]) for r in res_score],
                           "score_set_max": np.array([r[0] for r in res_score]),
                           "B_sigma": n_sigma, "B_threshold": n_thr, "B_score": n_score}
            timings[f"null_{kind}"] = time.perf_counter() - t0
            logger.info(f"[{name}] nulo {kind}: limiar z={interval['point_threshold']:.4f} ({timings[f'null_{kind}']:.1f} s)")

        primary = cfg["primary_null"]
        sigma_p, thr_p = nulls[primary]["sigma"], nulls[primary]["threshold"]
        t0 = time.perf_counter()
        n_syn, seps, n_lines = cfg["synthetic_realizations"], cfg["synthetic_pair_separations_fwhm"], cfg["synthetic_lines_per_realization"]
        s_iso, s_pair = ss_syn.spawn(2)
        iso = [row for rows in _map(executor, _task_synthetic,
                                    [(g, s, params, fraction, sigma_p, fwhm, thr_p, n_lines, (0.5 * thr_p, 4.0 * thr_p), None)
                                     for s in s_iso.spawn(n_syn)]) for row in rows]
        pair_seeds = s_pair.spawn(n_syn)
        pair_rows = []
        for k, sep in enumerate(seps):
            tasks = [(g, s, params, fraction, sigma_p, fwhm, thr_p, 2 * max(1, n_lines // 4), (2.0 * thr_p, 4.0 * thr_p), sep)
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
    tol, res_sep = calib["matching_tolerance"], calib["resolution_separation"]

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
    np.savez_compressed(null_npz, t_grid=tr.t_grid, F_real=F.real, F_imag=F.imag,
                        **{f"{k}_sigma": v["sigma"] for k, v in nulls.items()},
                        **{f"{k}_null_max": v["null_max"] for k, v in nulls.items()})
    result["freeze"] = {"blind_peaks_sha256": compute_file_sha256(blind_csv), "nulls_npz_sha256": compute_file_sha256(null_npz),
                        "frozen_before_arithmetic": True, "n_candidates": len(peaks),
                        "n_detected_primary": int(sum(p["detected_primary"] for p in peaks))}
    with open(bdir / "freeze.json", "w", encoding="utf-8") as f:
        json.dump(result["freeze"], f, indent=2)
    result["null_summary"] = {k: {"threshold_z": v["threshold"], "threshold_interval": v["interval"]} for k, v in nulls.items()}

    t0 = time.perf_counter()
    result["arithmetic"] = arithmetic_comparison(chi_catalog_module(ch), tr, g, peaks, nulls, primary, tol, res_sep,
                                                 bdir, cfg, ss_prec, ss_phase)
    timings["arithmetic"] = time.perf_counter() - t0
    result["timings_seconds"] = timings
    with open(bdir / "block_metrics.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, default=_json_default)
    return result


# ---------------------------------------------------------------------------
# 6. Critérios D-C1, D-C1z, D-C2, D-C2s, D-C2z (declaração §5)
# ---------------------------------------------------------------------------


def _read_matches(path: Path) -> List[Dict[str, Any]]:
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _b(v: str) -> bool:
    return str(v).strip() == "True"


def evaluate_criteria(results: Dict[str, Dict[str, Any]], out_dir: Path, cfg: Dict[str, Any], ch: Character) -> Dict[str, Any]:
    crit = cfg["criteria"]
    fam = evaluate_m3_family(results, crit)  # reaproveita C1b, contagem de blocos com detecção sem correspondência e C2
    per_block = {}
    for name in results:
        rows = _read_matches(out_dir / name / "arithmetic_matches.csv")
        info = []
        for r in rows:
            p, rep = int(r["prime"]), int(r["repetition"])
            chi_n = ch(p) ** rep
            c_zeta = -math.log(p) / (math.pi * p ** (rep / 2.0))
            info.append({"n": p ** rep, "chi": chi_n, "c_zeta": c_zeta, "re_C": float(r["fit_coefficient_real"]),
                         "limit": float(r["detection_limit_coefficient"]), "resolved": _b(r["resolved"]),
                         "clear": _b(r["clearly_detectable"]), "detected": _b(r["detected"])})
        zero_resolved = [x for x in info if x["chi"] == 0 and x["resolved"]]
        eligible = [x for x in info if x["resolved"] and x["clear"]]
        minus = [x for x in eligible if x["chi"] == -1]
        zeta_dev = [abs(x["re_C"] / x["c_zeta"] - 1.0) for x in eligible]
        per_block[name] = {
            "D_C1z_detected_zero_lines": [x["n"] for x in zero_resolved if x["detected"]],
            "D_C2z_violations": [x["n"] for x in zero_resolved if abs(x["re_C"]) > x["limit"]],
            "D_C2s_minus_lines": [x["n"] for x in minus],
            "D_C2s_sign_violations": [x["n"] for x in minus if not (x["re_C"] / x["c_zeta"] < 0)],
            "zeta_hypothesis_fraction_within_tol": (float(np.mean(np.array(zeta_dev) <= crit["ratio_tolerance"])) if zeta_dev else None),
        }
    d_c1 = bool(fam["C1_family_unmatched_ok"] and all(v["C1b_recovery_ok"] for v in fam["blocks"].values()))
    d_c1z = all(not v["D_C1z_detected_zero_lines"] for v in per_block.values())
    d_c2 = bool(fam["C2_replicated_all_blocks"])
    d_c2s = all(not v["D_C2s_sign_violations"] and (not v["D_C2s_minus_lines"] or
                (v["zeta_hypothesis_fraction_within_tol"] is not None and v["zeta_hypothesis_fraction_within_tol"] < crit["coefficient_fraction_min"]))
                for v in per_block.values())
    d_c2z = all(not v["D_C2z_violations"] for v in per_block.values())
    return {
        "character": ch.name,
        "D_C1": d_c1, "D_C1z": d_c1z, "D_C2": d_c2, "D_C2s": d_c2s, "D_C2z": d_c2z,
        "passes": bool(d_c1 and d_c1z and d_c2 and d_c2s and d_c2z),
        "per_block": per_block,
        "family_m3_style": fam,
        "note": "C1a (p global de S com Holm) é reportado em family_m3_style mas não é critério desta declaração.",
    }


# ---------------------------------------------------------------------------
# 7. Execução
# ---------------------------------------------------------------------------


def load_config(path: Path) -> Dict[str, Any]:
    with open(path, "rb") as f:
        return tomllib.load(f)


def load_zeros_txt(path: Path) -> np.ndarray:
    return np.loadtxt(path, dtype=np.float64)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Instrumento m4-v3 em zeros de L(s, χ) (ctrl-dirichlet-v1).")
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--carater", required=True, choices=sorted(CHARACTERS))
    ap.add_argument("--zeros", type=Path, required=True, help="arquivo de zeros produzido por dirichlet_zeros.py")
    ap.add_argument("--saida", type=Path, required=True)
    ap.add_argument("--blocos", default="", help="lista separada por vírgulas (padrão: todos os do caractere)")
    ap.add_argument("--workers", type=int, default=1)
    args = ap.parse_args(argv)

    cfg_all = load_config(args.config)
    ch = CHARACTERS[args.carater]
    ccfg = cfg_all["characters"][ch.name]
    cfg = {k: v for k, v in cfg_all.items() if k != "characters"}
    blocks = ccfg["blocks"]
    if args.blocos:
        wanted = [b.strip() for b in args.blocos.split(",") if b.strip()]
        blocks = [b for b in blocks if b["name"] in wanted]
    args.saida.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                        handlers=[logging.FileHandler(args.saida / "execution.log"), logging.StreamHandler()])
    zeros = load_zeros_txt(args.zeros)
    root = np.random.SeedSequence(ccfg["seed"])
    seqs = root.spawn(len(ccfg["blocks"]))
    results = {}
    t0 = time.perf_counter()
    for b in blocks:
        pos = [x["name"] for x in ccfg["blocks"]].index(b["name"])
        results[b["name"]] = run_block_chi(zeros, b, cfg, ch, args.saida, seqs[pos], workers=args.workers)
    summary = evaluate_criteria(results, args.saida, cfg, ch)
    summary["blocks_evaluated"] = [b["name"] for b in blocks]
    summary["complete_family"] = len(blocks) == len(ccfg["blocks"])
    manifest = {
        "protocol_version": cfg["protocol_version"],
        "config_sha256": compute_file_sha256(args.config),
        "zeros_file": str(args.zeros), "zeros_sha256": compute_file_sha256(args.zeros),
        "script_sha256": {p.name: compute_file_sha256(p) for p in sorted(Path(__file__).resolve().parent.glob("*.py"))},
        "seconds": time.perf_counter() - t0,
    }
    with open(args.saida / "criteria_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False, default=_json_default)
    with open(args.saida / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(json.dumps({k: summary[k] for k in ("character", "D_C1", "D_C1z", "D_C2", "D_C2s", "D_C2z", "passes")}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
