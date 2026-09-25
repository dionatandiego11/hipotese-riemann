"""
Instrumento m4-v3 aplicado aos níveis k do quarto de estádio — `ctrl-estadio-v1`
(DECLARACAO_ESTADIO.md `c7ce5d5b…`; D1E_DERIVACAO_ESTADIO.md `c0c28ed9…`; O1_CATALOGO_ORBITAS.md `0f7cb16e…`;
ADENDO_ESTADIO_1.md `a1496aca…`; ADENDO_ESTADIO_2.md `ea251f00…`).

O código congelado de `riemann_spectra` NÃO é editado; este arquivo só importa funções dele (mesmo desenho de
`instrumento_chi.py` e `instrumento_maass.py`). Diferenças declaradas em relação a `inverse_spectroscopy.run_block`:

  1. variável k; densidade suave d̄(k) = A_q k/2π − L_q/4π e contagem N̄₀(k) = A_q k²/4π − L_q k/4π (declaração §3, P3),
     com A_q = 1 + π/4 e L_q = 4 + π/2; a constante C da fórmula de Weyl não entra (não afeta densidade nem diferenças);
  2. catálogo O1 (6 comprimentos em t ≤ 5). A amplitude prevista existe só para a linha L = 2 (família bouncing ball):
     |C̄_bb| entra como `coefficient_theoretical` (para limite de detecção e z previsto) e o valor complexo C̄_bb é
     calculado à parte para E-C2bb. As demais linhas entram com coeficiente 0 ("amplitude não prevista"; Gutzwiller é
     descritivo, declaração §5);
  3. nulos: shuffle (primário) e GOE (β-Hermite tridiagonal de Dumitriu–Edelman com β = 1) no lugar do GUE; o fundo das
     linhas sintéticas de calibração também é GOE;
  4. calibração sintética com n_iso limitado pela FWHM (ADENDO_ESTADIO_1 §2.5, mesma regra dos adendos 2 e 4 do Maass);
  5. blocos: G (primário, todos os níveis) para E-C1, E-C1o e E-C4; g01–g04 para E-C2bb (ADENDO_ESTADIO_1).

Uso (da raiz):
  .venv/bin/python3 results/etapa11_6_controles/estadio/instrumento_estadio.py \
      --config results/etapa11_6_controles/estadio/ctrl_estadio_v1.toml --niveis <arquivo.txt> --saida <pasta>
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
from scipy.linalg import eigvalsh_tridiagonal
from scipy.special import j0, j1

from riemann_spectra import arithmetic as _ar
from riemann_spectra.controls import semicircle_cdf, shuffle_spacings
from riemann_spectra.inverse_spectroscopy import _json_default, _map, arithmetic_comparison, summarize_synthetic
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
from riemann_spectra.utils import compute_file_sha256

logger = logging.getLogger("ctrl_estadio")
HERE = Path(__file__).resolve().parent
TWO_PI = 2 * math.pi
A_Q = 1.0 + math.pi / 4.0          # área do quarto de estádio (a = b = 1)
L_Q = 4.0 + math.pi / 2.0          # comprimento de Dirichlet
A_RECT, B_RAD = 1.0, 1.0           # trecho reto e raio


# ---------------------------------------------------------------------------
# 1. Contagem e densidade suaves (declaração §3, P3)
# ---------------------------------------------------------------------------


def n_bar(k):
    k = np.asarray(k, dtype=np.float64)
    return A_Q * k * k / (4 * math.pi) - L_Q * k / (4 * math.pi)


def d_bar(k):
    k = np.asarray(k, dtype=np.float64)
    return A_Q * k / TWO_PI - L_Q / (4 * math.pi)


def inverse_n_bar(x, k_guess=None, tol=1e-12, max_iter=80):
    x = np.atleast_1d(np.asarray(x, dtype=np.float64))
    k = np.sqrt(np.maximum(4 * math.pi * x / A_Q, 1.0)) if k_guess is None else np.asarray(k_guess, dtype=np.float64).copy()
    for _ in range(max_iter):
        step = (n_bar(k) - x) / np.maximum(d_bar(k), 1e-12)
        k = np.maximum(k - step, 0.5 * k)
        if np.max(np.abs(step)) < tol * max(1.0, float(np.max(k))):
            break
    return k


# ---------------------------------------------------------------------------
# 2. Linha bouncing ball (D1-E §2): densidade e contagem exatas da família
# ---------------------------------------------------------------------------


def d_bb(k, m_max=10, a=A_RECT, b=B_RAD):
    k = np.asarray(k, dtype=np.float64)
    return (a * b * k / math.pi) * sum(j0(2 * b * m * k) for m in range(1, m_max + 1))


def n_fl_bb(k, m_max=10, a=A_RECT, b=B_RAD):
    k = np.asarray(k, dtype=np.float64)
    return (a * k / TWO_PI) * sum(j1(2 * b * m * k) / m for m in range(1, m_max + 1))


def C_bb_exact(k, a=A_RECT, b=B_RAD):
    """C(k) da linha L = 2b: d₁(k) = Re[C(k) e^{2ibk}] (D1-E §2 iii)."""
    from scipy.special import hankel1
    return (a * b * np.asarray(k, dtype=np.float64) / math.pi) * hankel1(0, 2 * b * np.asarray(k, dtype=np.float64)) \
        * np.exp(-2j * b * np.asarray(k, dtype=np.float64))


def C_bb_predicted(A, B, catalog_T, window="hann", points_per_fwhm=8.0, n_quad=200001):
    """
    C̄_bb do bloco: o próprio estimador congelado aplicado ao sinal analítico F_bb (D1-E §3), com as bordas reais e o
    catálogo do bloco.
    """
    L, Ec = B - A, 0.5 * (A + B)
    resp = measure_window_response(L, window)
    k = np.linspace(A, B, n_quad)
    w = np.sin(math.pi * (k - A) / L) ** 2
    dens = d_bb(k)
    h = (B - A) / (n_quad - 1)
    wt = np.full(n_quad, h)
    wt[0] = wt[-1] = h / 2

    def F(t):
        t = np.atleast_1d(np.asarray(t, dtype=np.float64))
        return np.array([np.sum(wt * w * dens * np.exp(-1j * (k - Ec) * tt)) for tt in t])

    cat = [{"catalog_index": i, "period_theoretical": T, "coefficient_theoretical": 1.0} for i, T in enumerate(catalog_T)]
    fit = _ar.targeted_joint_fit(F, cat, L, Ec, half_width=0.5 * resp["fwhm"], window=window, sampling="band",
                                 include_conjugate=True)
    return {T: complex(f["coefficient_real"], f["coefficient_imag"]) for T, f in zip(catalog_T, fit)}


# ---------------------------------------------------------------------------
# 3. Instrumento
# ---------------------------------------------------------------------------


class StadiumTransform(OscillatoryTransform):
    def __init__(self, A, B, t_min, t_max, points_per_fwhm=8.0, panel_length=0.5, quad_order=8, window="hann"):
        if not (B > A > 0):
            raise ValueError("A janela deve satisfazer B > A > 0.")
        window_coefficients(window)
        self.window, self.A, self.B = window, float(A), float(B)
        self.L, self.E_c = self.B - self.A, 0.5 * (self.A + self.B)
        self.response = measure_window_response(self.L, window)
        self.dt = self.response["fwhm"] / points_per_fwhm
        self.n_t = int(math.floor((t_max - t_min) / self.dt)) + 1
        self.t_grid = t_min + self.dt * np.arange(self.n_t)
        self.density, self.panel_length, self.quad_order = "weyl_quarter_stadium", panel_length, quad_order
        self._quad_offsets, self._quad_weights = local_gauss_legendre_panels(self.L, panel_length, quad_order)
        self._quad_nodes = self.A + self._quad_offsets
        self._quad_u = self._quad_offsets - 0.5 * self.L
        self._quad_coeffs = self._window_at_offsets(self._quad_offsets) * d_bar(self._quad_nodes) * self._quad_weights
        self.smooth = nufft_uniform_t(self._quad_u, self._quad_coeffs, self.t_grid[0], self.dt, self.n_t)

    def diagnostics(self, levels, n_check=64, seed=0):
        rng = np.random.default_rng(seed)
        idx = np.sort(rng.choice(self.n_t, size=min(n_check, self.n_t), replace=False))
        F_grid = self.transform(levels)
        off2, w2 = local_gauss_legendre_panels(self.L, 0.5 * self.panel_length, self.quad_order)
        c2 = self._window_at_offsets(off2) * d_bar(self.A + off2) * w2
        smooth2 = nufft_uniform_t(off2 - 0.5 * self.L, c2, self.t_grid[0], self.dt, self.n_t)
        return {"n_t": self.n_t, "dt": self.dt, "max_abs_F": float(np.max(np.abs(F_grid))),
                "nufft_vs_direct_max_abs_error": float(np.max(np.abs(F_grid[idx] - self.evaluate(levels, self.t_grid[idx])))),
                "quadrature_halving_max_abs_change": float(np.max(np.abs(smooth2 - self.smooth))),
                "quadrature_nodes": int(len(self._quad_nodes))}


_CACHE: Dict[Tuple, StadiumTransform] = {}


def instrument_params(g, cfg) -> Tuple:
    return (float(g[0]), float(g[-1]), float(cfg["t_min"]), float(cfg["t_max"]), float(cfg["points_per_fwhm"]),
            str(cfg["window"]), float(cfg["quadrature_panel_length"]), int(cfg["quadrature_order"]))


def _instrument(params) -> StadiumTransform:
    if params not in _CACHE:
        A, B, t_min, t_max, ppf, window, panel, order = params
        _CACHE.clear()
        _CACHE[params] = StadiumTransform(A, B, t_min, t_max, points_per_fwhm=ppf, panel_length=panel,
                                          quad_order=order, window=window)
    return _CACHE[params]


# ---------------------------------------------------------------------------
# 4. Nulos (shuffle e GOE) e linhas sintéticas
# ---------------------------------------------------------------------------


def goe_central_levels(n, retained_fraction, rng):
    """β-Hermite tridiagonal (Dumitriu–Edelman) com β = 1; mesma construção do gerador GUE congelado."""
    dim = int(math.ceil(n / retained_fraction))
    diag = rng.normal(0.0, 1.0, size=dim)
    k = 1.0 * np.arange(dim - 1, 0, -1, dtype=np.float64)
    sub = np.sqrt(rng.gamma(shape=k / 2.0, scale=2.0)) / math.sqrt(2.0)
    scale = 1.0 / math.sqrt(2.0 * dim)
    ev = eigvalsh_tridiagonal(diag * scale, sub * scale)
    u = dim * semicircle_cdf(ev)
    s = (dim - n) // 2
    return u[s:s + n]


def shuffled_levels(g, rng):
    x = n_bar(g)
    return inverse_n_bar(shuffle_spacings(np.diff(x), origin_x=float(x[0]), rng=rng), k_guess=g)


def goe_levels(g, fraction, rng):
    n = len(g)
    y = goe_central_levels(n, fraction, rng)
    x0, x1 = float(n_bar(g[0])), float(n_bar(g[-1]))
    return inverse_n_bar(x0 + (y - y[0]) * (x1 - x0) / (y[-1] - y[0]), k_guess=g)


def inject_lines(x, T, C, k_guess=None, tol=1e-11, max_iter=60):
    x = np.asarray(x, dtype=np.float64)
    T = np.asarray(T, dtype=np.float64)
    C = np.asarray(C, dtype=np.complex128)
    k = inverse_n_bar(x, k_guess=k_guess)
    for _ in range(max_iter):
        ph = np.exp(1j * np.outer(k, T))
        f = n_bar(k) + np.real(ph @ (C / (1j * T))) - x
        fp = d_bar(k) + np.real(ph @ C)
        if np.any(fp <= 0):
            raise ValueError("Densidade modulada não positiva: reduza os coeficientes injetados.")
        k = k - f / fp
        if np.max(np.abs(f / fp)) < tol:
            break
    return k


def inject_bouncing_ball(x, k_guess=None, m_max=10, tol=1e-11, max_iter=60):
    """Injeta a densidade exata da família (D1-E): resolve N̄₀(k) + N_fl^bb(k) = x."""
    x = np.asarray(x, dtype=np.float64)
    k = inverse_n_bar(x, k_guess=k_guess)
    for _ in range(max_iter):
        f = n_bar(k) + n_fl_bb(k, m_max) - x
        fp = d_bar(k) + d_bb(k, m_max)
        if np.any(fp <= 0):
            raise ValueError("Densidade modulada não positiva na injeção bouncing ball.")
        k = k - f / fp
        if np.max(np.abs(f / fp)) < tol:
            break
    return k


def _null_levels(kind, g, seed_state, fraction):
    rng = np.random.default_rng(seed_state)
    if kind == "shuffle":
        return shuffled_levels(g, rng)
    if kind == "goe":
        return goe_levels(g, fraction, rng)
    raise ValueError(kind)


def _task_power(args):
    kind, g, seed_state, params, fraction = args
    return np.abs(_instrument(params).transform(_null_levels(kind, g, seed_state, fraction))) ** 2


def _task_max(args):
    kind, g, seed_state, params, fraction, sigma, fwhm, cand_z = args
    tr = _instrument(params)
    F = tr.transform(_null_levels(kind, g, seed_state, fraction))
    peaks = detect_blind_peaks(tr.t_grid, F, fwhm, sigma, candidate_z=cand_z)
    return max_statistic(F, sigma), np.array([p["period"] for p in peaks]), np.array([p["z"] for p in peaks])


def _task_synthetic(args):
    """Cópia de `inverse_spectroscopy._task_synthetic` com fundo GOE e N̄₀ do estádio."""
    g, seed_state, params, fraction, sigma, fwhm, thr, n_lines, z_range, pair_sep = args
    rng = np.random.default_rng(seed_state)
    tr = _instrument(params)
    t_min, t_max = params[2], params[3]
    n = len(g)
    y = goe_central_levels(n, fraction, rng)
    x0, x1 = float(n_bar(g[0])), float(n_bar(g[-1]))
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
    budget = 0.8 * float(np.min(d_bar(np.linspace(g[0], g[-1], 2001))))
    keep = np.zeros(len(T), dtype=bool)
    used = 0.0
    step = 1 if pair_sep is None else 2
    for kk in range(0, len(T) - step + 1, step):
        cost = float(np.sum(coef_mod[kk:kk + step]))
        if used + cost <= budget:
            keep[kk:kk + step] = True
            used += cost
    if not keep.any():
        return []
    T, z_true, coef_mod, C = T[keep], z_true[keep], coef_mod[keep], C[keep]
    F = tr.transform(inject_lines(x, T, C, k_guess=inverse_n_bar(x, k_guess=g)))
    peaks = detect_blind_peaks(tr.t_grid, F, fwhm, sigma, candidate_z=min(3.0, thr))
    per = np.array([p["period"] for p in peaks if p["z"] >= thr])
    out = []
    for kk in range(len(T)):
        err = float(per[int(np.argmin(np.abs(per - T[kk])))] - T[kk]) if len(per) else float("inf")
        out.append({"T": float(T[kk]), "z_true": float(z_true[kk]), "error": err, "coef_modulus": float(coef_mod[kk])})
    return out


# ---------------------------------------------------------------------------
# 5. Catálogo O1
# ---------------------------------------------------------------------------


def load_o1(path: Path = HERE / "catalogo_o1.csv") -> List[Dict[str, Any]]:
    fam, out = {}, []
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            L = float(r["comprimento"])
            key = round(L, 9)
            if key in fam:
                continue
            fam[key] = True
            out.append({"length": L, "family": r["familia"] == "1", "boundary": r["orbita_de_fronteira"] == "1",
                        "n_outer": int(r["reflexoes_externas"])})
    return sorted(out, key=lambda x: x["length"])


def o1_catalog_module(lines, C_pred):
    """`coefficient_theoretical` = |C̄_bb| na linha L = 2; 0 nas demais (amplitude não prevista)."""
    def catalog(t_min, t_max):
        cat = []
        for i, ln in enumerate(l for l in lines if t_min <= l["length"] <= t_max):
            T = ln["length"]
            c = abs(C_pred[T]) if abs(T - 2.0) < 1e-9 and T in C_pred else 0.0
            cat.append({"prime": int(round(T * 1000)), "repetition": 1, "period_theoretical": T,
                        "coefficient_theoretical": c, "bb": abs(T - 2.0) < 1e-9})
        cat.sort(key=lambda c: c["period_theoretical"])
        for i, c in enumerate(cat):
            c["catalog_index"] = i
        return cat

    return SimpleNamespace(prime_power_catalog=catalog, flag_unresolved=_ar.flag_unresolved,
                           match_one_to_one=_ar.match_one_to_one, targeted_joint_fit=_ar.targeted_joint_fit,
                           detection_limit_coefficient=_ar.detection_limit_coefficient)


# ---------------------------------------------------------------------------
# 6. Bloco
# ---------------------------------------------------------------------------


def run_block_estadio(levels, block, cfg, lines, out_dir: Path, seed_seq, workers=1) -> Dict[str, Any]:
    name = block["name"]
    g = np.asarray(levels, dtype=np.float64)
    if "k_min" in block:
        g = g[(g >= block["k_min"]) & (g < block["k_max"])]
    if len(g) < 100:
        raise ValueError(f"[{name}] poucos níveis: {len(g)}")
    cand_z, fraction = cfg["candidate_z"], cfg["goe_retained_fraction"]
    params = instrument_params(g, cfg)
    bdir = out_dir / name
    bdir.mkdir(parents=True, exist_ok=True)
    timings: Dict[str, float] = {}
    tr = _instrument(params)
    fwhm = tr.response["fwhm"]
    T_cat = [ln["length"] for ln in lines if cfg["t_min"] <= ln["length"] <= cfg["t_max"]]
    C_pred = C_bb_predicted(float(g[0]), float(g[-1]), T_cat, window=cfg["window"])
    result: Dict[str, Any] = {"block": block, "protocol_version": cfg["protocol_version"], "n_levels": len(g),
                             "C_bb_predicted": {str(T): [C_pred[T].real, C_pred[T].imag] for T in T_cat}}
    ss_shuffle, ss_goe, ss_syn, ss_diag, ss_prec, ss_phase = seed_seq.spawn(6)
    F = tr.transform(g)
    result["instrument"] = tr.to_metadata()
    result["instrument_diagnostics"] = tr.diagnostics(g, n_check=64, seed=int(ss_diag.generate_state(1)[0]))

    executor = ProcessPoolExecutor(max_workers=workers) if workers > 1 else None
    try:
        nulls: Dict[str, Dict[str, Any]] = {}
        for kind, child in (("shuffle", ss_shuffle), ("goe", ss_goe)):
            n_sigma, n_thr, n_score = cfg[f"{kind}_sigma_realizations"], cfg[f"{kind}_threshold_realizations"], cfg[f"{kind}_score_realizations"]
            t0 = time.perf_counter()
            s_sigma, s_thr, s_score = child.spawn(3)
            powers = _map(executor, _task_power, [(kind, g, s, params, fraction) for s in s_sigma.spawn(n_sigma)])
            sigma = null_noise_profile(np.sqrt(np.array(powers)), tr.t_grid, cfg["noise_smooth_window"])
            res_thr = _map(executor, _task_max, [(kind, g, s, params, fraction, sigma, fwhm, cand_z) for s in s_thr.spawn(n_thr)])
            null_max = np.array([r[0] for r in res_thr])
            interval = threshold_interval(null_max, cfg["alpha"], cfg["threshold_confidence"])
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
        n_iso = min(n_lines, int(math.floor((cfg["t_max"] - cfg["t_min"] - 0.1) / (2.0 * 10.0 * fwhm))))
        if n_iso < 1:
            raise ValueError(f"[{name}] FWHM {fwhm:.4f} grande demais para a calibração sintética")
        n_syn_iso = int(math.ceil(n_syn * n_lines / n_iso))
        result["synthetic_isolated_design"] = {"n_iso_per_realization": n_iso, "isolated_realizations": n_syn_iso}
        s_iso, s_pair = ss_syn.spawn(2)
        iso = [row for rows in _map(executor, _task_synthetic,
                                    [(g, s, params, fraction, sigma_p, fwhm, thr_p, n_iso, (0.5 * thr_p, 4.0 * thr_p), None)
                                     for s in s_iso.spawn(n_syn_iso)]) for row in rows]
        pair_seeds = s_pair.spawn(n_syn)
        pair_rows = []
        for kk, sep in enumerate(seps):
            tasks = [(g, s, params, fraction, sigma_p, fwhm, thr_p, 2 * max(1, n_lines // 4), (2.0 * thr_p, 4.0 * thr_p), sep)
                     for s in pair_seeds[kk::len(seps)]]
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
    secondary = "goe" if primary == "shuffle" else "shuffle"
    for p in peaks:
        gi = p["grid_index"]
        p["p_adjusted_primary"] = float(adjusted_p_values([p["z"]], nulls[primary]["null_max"])[0])
        p["class_primary"] = classify_detection(p["z"], nulls[primary]["interval"])
        p["detected_primary"] = p["class_primary"] == "detected"
        p["z_secondary"] = float(np.abs(F[gi]) / nulls[secondary]["sigma"][gi])
        p["class_secondary"] = classify_detection(p["z_secondary"], nulls[secondary]["interval"])
        p["detected_secondary"] = p["class_secondary"] == "detected"
        p["fwhm_instrument"] = fwhm
    blind_csv = bdir / "blind_peaks.csv"
    cols = ["grid_period", "period", "fwhm_instrument", "z", "p_adjusted_primary", "class_primary", "detected_primary",
            "z_secondary", "class_secondary", "detected_secondary", "z_refined", "amplitude_real", "amplitude_imag",
            "modulus", "phase_rad", "null_noise_rms"]
    with open(blind_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["peak_id"] + cols)
        for kk, p in enumerate(peaks):
            w.writerow([kk] + [repr(p[c]) if isinstance(p[c], float) else p[c] for c in cols])
    result["freeze"] = {"blind_peaks_sha256": compute_file_sha256(blind_csv), "frozen_before_arithmetic": True,
                        "n_candidates": len(peaks), "n_detected_primary": int(sum(p["detected_primary"] for p in peaks))}
    with open(bdir / "freeze.json", "w", encoding="utf-8") as f:
        json.dump(result["freeze"], f, indent=2)
    result["null_summary"] = {k: {"threshold_z": v["threshold"], "threshold_interval": v["interval"]} for k, v in nulls.items()}
    result["detected_periods_primary"] = [p["period"] for p in peaks if p["detected_primary"]]

    result["arithmetic"] = arithmetic_comparison(o1_catalog_module(lines, C_pred), tr, g, peaks, nulls, primary, tol,
                                                 res_sep, bdir, cfg, ss_prec, ss_phase)
    # E-C2bb: razão complexa medida/prevista na linha L = 2
    fitc = _ar.targeted_joint_fit(lambda t: tr.evaluate(g, t),
                                  o1_catalog_module(lines, C_pred).prime_power_catalog(cfg["t_min"], cfg["t_max"]),
                                  tr.L, tr.E_c, half_width=cfg["targeted_fit_half_width_fwhm"] * fwhm, window=tr.window,
                                  sampling="band", include_conjugate=True)
    idx = [i for i, T in enumerate(T_cat) if abs(T - 2.0) < 1e-9]
    if idx:
        C_hat = complex(fitc[idx[0]]["coefficient_real"], fitc[idx[0]]["coefficient_imag"])
        result["E_C2bb"] = {"C_hat": [C_hat.real, C_hat.imag], "C_pred": [C_pred[2.0].real, C_pred[2.0].imag],
                            "ratio": [(C_hat / C_pred[2.0]).real, (C_hat / C_pred[2.0]).imag],
                            "abs_ratio_minus_1": abs(C_hat / C_pred[2.0] - 1.0)}
    result["timings_seconds"] = timings
    with open(bdir / "block_metrics.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, default=_json_default)
    return result


# ---------------------------------------------------------------------------
# 7. Critérios (declaração §5 com ADENDO_ESTADIO_1 e 2)
# ---------------------------------------------------------------------------


def evaluate_block(res: Dict[str, Any], bdir: Path, cfg: Dict[str, Any], lines) -> Dict[str, Any]:
    crit = cfg["criteria"]
    fwhm = res["instrument"]["response"]["fwhm"]
    tol = res["synthetic_calibration"]["matching_tolerance"]
    det = np.array(res["detected_periods_primary"])
    T_cat = np.array([ln["length"] for ln in lines if cfg["t_min"] <= ln["length"] <= cfg["t_max"]])
    # E-C1 (ADENDO_ESTADIO_2 §1): pico "detected" correspondido a L = 2 pela tolerância calibrada
    e_c1 = bool(len(det) and np.min(np.abs(det - 2.0)) <= tol)
    matched = [bool(len(T_cat) and np.min(np.abs(T_cat - p)) <= tol) for p in det]
    e_c1o = bool(len(det) == 0 or (sum(not m for m in matched) / len(det)) <= crit["unmatched_fraction_max"])
    zeta_lines = [math.log(n) for n in range(2, 149) if cfg["t_min"] <= math.log(n) <= cfg["t_max"]]
    cand = [t for t in zeta_lines if len(T_cat) == 0 or np.min(np.abs(T_cat - t)) > fwhm]
    hits = [t for t in cand if len(det) and np.min(np.abs(det - t)) <= tol]
    e_c4 = bool(len(cand) == 0 or len(hits) / len(cand) <= crit["absence_fraction_max"])
    out = {"E_C1": e_c1, "E_C1o": e_c1o, "E_C4": e_c4, "n_detected": int(len(det)),
           "unmatched": int(sum(not m for m in matched)), "zeta_hits": hits}
    if "E_C2bb" in res:
        out["E_C2bb"] = bool(res["E_C2bb"]["abs_ratio_minus_1"] <= crit["bb_ratio_tolerance"])
        out["abs_ratio_minus_1"] = res["E_C2bb"]["abs_ratio_minus_1"]
    return out


def load_config(path: Path) -> Dict[str, Any]:
    with open(path, "rb") as f:
        return tomllib.load(f)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Instrumento m4-v3 em níveis do quarto de estádio (ctrl-estadio-v1).")
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--niveis", type=Path, required=True)
    ap.add_argument("--saida", type=Path, required=True)
    ap.add_argument("--blocos", default="")
    ap.add_argument("--workers", type=int, default=1)
    a = ap.parse_args(argv)
    cfg = load_config(a.config)
    a.saida.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                        handlers=[logging.FileHandler(a.saida / "execution.log"), logging.StreamHandler()])
    levels = np.loadtxt(a.niveis, dtype=np.float64)
    lines = load_o1()
    blocks = cfg["blocks"]
    if a.blocos:
        want = [b.strip() for b in a.blocos.split(",")]
        blocks = [b for b in blocks if b["name"] in want]
    root = np.random.SeedSequence(cfg["seed"])
    seqs = root.spawn(len(cfg["blocks"]))
    summary = {"protocol_version": cfg["protocol_version"], "blocks": {}}
    for b in blocks:
        pos = [x["name"] for x in cfg["blocks"]].index(b["name"])
        res = run_block_estadio(levels, b, cfg, lines, a.saida, seqs[pos], workers=a.workers)
        summary["blocks"][b["name"]] = evaluate_block(res, a.saida / b["name"], cfg, lines)
    prim = cfg["primary_block"]
    bb_blocks = [b["name"] for b in cfg["blocks"] if b.get("for_e_c2bb")]
    summary["passes"] = bool(summary["blocks"].get(prim, {}).get("E_C1") and summary["blocks"].get(prim, {}).get("E_C1o")
                             and summary["blocks"].get(prim, {}).get("E_C4")
                             and all(summary["blocks"].get(n, {}).get("E_C2bb") for n in bb_blocks if n in summary["blocks"]))
    with open(a.saida / "criteria_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False, default=_json_default)
    print(json.dumps(summary["blocks"], indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
