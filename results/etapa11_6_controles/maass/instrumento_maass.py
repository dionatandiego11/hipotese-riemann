"""
Instrumento m4-v3 aplicado aos parâmetros espectrais R de formas de Maass ímpares de PSL(2,Z) — `ctrl-maass-v1`
(DECLARACAO_MAASS.md, SHA-256 5db97004…; ADENDO_MAASS_1.md, 4efb9020…; D1M_DERIVACAO_MAASS.md, 773a077b…;
catálogo G1_CATALOGO_GEODESICAS.md, 8705bd7f…).

O código congelado de `riemann_spectra` NÃO é editado; este arquivo só importa funções dele (mesmo desenho do
`instrumento_chi.py` do controle Dirichlet). Diferenças em relação a `inverse_spectroscopy.run_block`, todas declaradas:

  1. variável R; densidade suave d̄(R) = dN̄/dR com N̄(R) = R²/24 + βR log R + γR + δ₀, β, γ, δ₀ ajustados por mínimos
     quadrados à escada N(R_j) = j − ½ do bloco (declaração §5); a mesma N̄ faz o unfolding dos nulos e das linhas
     sintéticas;
  2. catálogo = linhas de G1 em [t_min, t_max] (comprimentos 2 arccosh(n/2) e 2 arcsinh(n/2), coeficientes do
     ADENDO_MAASS_1 §2), no formato que `arithmetic_comparison` espera ("prime" = traço n, "repetition" = 1);
  3. nulo de Poisson no lugar do GUE (declaração §5); como consequência, o fundo das linhas sintéticas de calibração
     também é Poisson (espaçamentos exponenciais), e não GUE;
  4. critérios M-C1, M-C2s, M-C2a+, M-C2a−, M-C4, M-C4s (declaração §5 com o adendo 1);
  5. linhas sintéticas isoladas por realização limitadas pela FWHM, com mais realizações (ADENDO_MAASS_2, 19/09/2026);
  6. blocos por segmento sem lacuna (S2 primário, S1 descritivo), conferência de lacunas, conferência do ajuste suave
     e orçamento sintético pelo mínimo de d̄ (ADENDO_MAASS_3, 19/09/2026);
  7. uma linha sintética isolada por realização quando só uma cabe (ADENDO_MAASS_4, 19/09/2026).

Uso (da raiz):
  .venv/bin/python3 results/etapa11_6_controles/maass/instrumento_maass.py \
      --config results/etapa11_6_controles/maass/ctrl_maass_v1.toml \
      --dados Mass-Forms/lmfdb_maass_rigor_0919_1121.txt --saida <pasta> --workers 2
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

from riemann_spectra import arithmetic as _ar
from riemann_spectra.controls import shuffle_spacings
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

logger = logging.getLogger("ctrl_maass")
HERE = Path(__file__).resolve().parent
EXPECTED_DATA_SHA256 = "f4ca1d21"          # prefixo registrado na declaração §2
FIRST_ODD_R = 9.5336952                    # declaração §2 (conferência B)

# ---------------------------------------------------------------------------
# 1. Dados (conferência B da declaração §2)
# ---------------------------------------------------------------------------


def load_maass(path: Path) -> Dict[str, Any]:
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.startswith('"'):
                continue
            parts = line.rstrip("\n").split("\t")
            label, level, weight, char, R, sym, fricke = parts[:7]
            rows.append({"label": label.strip('"'), "level": int(level), "weight": int(weight), "char": char,
                         "R": float(R), "R_str": R, "symmetry": int(sym)})
    R_all = np.array([r["R"] for r in rows])
    odd = np.array([r["R"] for r in rows if r["symmetry"] == 1])
    checks = {
        "n_forms": len(rows),
        "all_level_1_weight_0": all(r["level"] == 1 and r["weight"] == 0 for r in rows),
        "strictly_increasing": bool(np.all(np.diff(R_all) > 0)),
        "n_odd": int(len(odd)), "n_even": int(sum(r["symmetry"] == 0 for r in rows)),
        "first_odd_R": float(odd[0]) if len(odd) else None,
        "first_odd_ok": bool(len(odd) and abs(odd[0] - FIRST_ODD_R) < 1e-6),
        "R_max": float(R_all.max()) if len(rows) else None,
        "sha256": compute_file_sha256(path),
    }
    checks["sha256_matches_declaration"] = checks["sha256"].startswith(EXPECTED_DATA_SHA256)
    # ADENDO_MAASS_3 §2.1: lacunas = espaçamento > 10 espaçamentos médios locais (12/R) no setor ímpar
    if len(odd) > 1:
        ratio = np.diff(odd) / (12.0 / odd[:-1])
        checks["odd_gaps"] = [{"after_index": int(i + 1), "R_left": float(odd[i]), "R_right": float(odd[i + 1]),
                               "mean_spacings": float(ratio[i])} for i in np.where(ratio > 10.0)[0]]
    checks["passed"] = bool(checks["all_level_1_weight_0"] and checks["strictly_increasing"] and checks["first_odd_ok"]
                            and checks["sha256_matches_declaration"])
    return {"odd": odd, "even": np.array([r["R"] for r in rows if r["symmetry"] == 0]), "checks": checks}


# ---------------------------------------------------------------------------
# 2. Contagem e densidade suaves (declaração §5)
# ---------------------------------------------------------------------------


def fit_smooth(R: np.ndarray, first_index: int) -> Dict[str, float]:
    """Mínimos quadrados para N(R_j) − R_j²/24 = βR log R + γR + δ₀, com N(R_j) = j − ½ (índice global j)."""
    R = np.asarray(R, dtype=np.float64)
    j = first_index + np.arange(len(R))
    y = (j - 0.5) - R * R / 24.0
    X = np.column_stack([R * np.log(R), R, np.ones_like(R)])
    (beta, gamma, delta), *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ np.array([beta, gamma, delta])
    return {"beta": float(beta), "gamma": float(gamma), "delta": float(delta), "rms_residual": float(np.sqrt(np.mean(resid ** 2))),
            "max_abs_residual": float(np.max(np.abs(resid)))}


def n_bar(R, p):
    R = np.asarray(R, dtype=np.float64)
    return R * R / 24.0 + p["beta"] * R * np.log(R) + p["gamma"] * R + p["delta"]


def d_bar(R, p):
    R = np.asarray(R, dtype=np.float64)
    return R / 12.0 + p["beta"] * (np.log(R) + 1.0) + p["gamma"]


def inverse_n_bar(x, p, R_guess=None, tol=1e-12, max_iter=80):
    x = np.atleast_1d(np.asarray(x, dtype=np.float64))
    R = np.sqrt(24.0 * np.maximum(x, 1.0)) if R_guess is None else np.asarray(R_guess, dtype=np.float64).copy()
    for _ in range(max_iter):
        step = (n_bar(R, p) - x) / np.maximum(d_bar(R, p), 1e-12)
        R = np.maximum(R - step, 0.5 * R)
        if np.max(np.abs(step)) < tol * max(1.0, float(np.max(R))):
            break
    return R


# ---------------------------------------------------------------------------
# 3. Instrumento (construtor copiado de OscillatoryTransform com a densidade trocada)
# ---------------------------------------------------------------------------


class MaassTransform(OscillatoryTransform):
    def __init__(self, A, B, t_min, t_max, smooth_params, points_per_fwhm=8.0, panel_length=0.5, quad_order=8, window="hann"):
        if not (B > A > 0):
            raise ValueError("A janela deve satisfazer B > A > 0.")
        window_coefficients(window)
        self.sp = dict(smooth_params)
        self.window = window
        self.A, self.B = float(A), float(B)
        self.L = self.B - self.A
        self.E_c = 0.5 * (self.A + self.B)
        self.response = measure_window_response(self.L, window)
        self.dt = self.response["fwhm"] / points_per_fwhm
        self.n_t = int(math.floor((t_max - t_min) / self.dt)) + 1
        self.t_grid = t_min + self.dt * np.arange(self.n_t)
        self.density = "maass_fit"
        self.panel_length = panel_length
        self.quad_order = quad_order
        self._quad_offsets, self._quad_weights = local_gauss_legendre_panels(self.L, panel_length, quad_order)
        self._quad_nodes = self.A + self._quad_offsets
        self._quad_u = self._quad_offsets - 0.5 * self.L
        self._quad_coeffs = self._window_at_offsets(self._quad_offsets) * d_bar(self._quad_nodes, self.sp) * self._quad_weights
        self.smooth = nufft_uniform_t(self._quad_u, self._quad_coeffs, self.t_grid[0], self.dt, self.n_t)

    def diagnostics(self, levels, n_check=64, seed=0):
        rng = np.random.default_rng(seed)
        idx = np.sort(rng.choice(self.n_t, size=min(n_check, self.n_t), replace=False))
        F_grid = self.transform(levels)
        F_direct = self.evaluate(levels, self.t_grid[idx])
        off2, w2 = local_gauss_legendre_panels(self.L, 0.5 * self.panel_length, self.quad_order)
        c2 = self._window_at_offsets(off2) * d_bar(self.A + off2, self.sp) * w2
        smooth2 = nufft_uniform_t(off2 - 0.5 * self.L, c2, self.t_grid[0], self.dt, self.n_t)
        return {"n_t": self.n_t, "dt": self.dt, "max_abs_F": float(np.max(np.abs(F_grid))),
                "nufft_vs_direct_max_abs_error": float(np.max(np.abs(F_grid[idx] - F_direct))),
                "quadrature_halving_max_abs_change": float(np.max(np.abs(smooth2 - self.smooth))),
                "quadrature_nodes": int(len(self._quad_nodes)), "smooth_params": self.sp}


_CACHE: Dict[Tuple, MaassTransform] = {}


def instrument_params(g, cfg, sp) -> Tuple:
    return (float(g[0]), float(g[-1]), float(cfg["t_min"]), float(cfg["t_max"]), float(cfg["points_per_fwhm"]), str(cfg["window"]),
            float(cfg["quadrature_panel_length"]), int(cfg["quadrature_order"]), sp["beta"], sp["gamma"], sp["delta"])


def _sp_of(params):
    return {"beta": params[8], "gamma": params[9], "delta": params[10]}


def _instrument(params) -> MaassTransform:
    if params not in _CACHE:
        A, B, t_min, t_max, ppf, window, panel, order = params[:8]
        _CACHE.clear()
        _CACHE[params] = MaassTransform(A, B, t_min, t_max, _sp_of(params), points_per_fwhm=ppf, panel_length=panel,
                                        quad_order=order, window=window)
    return _CACHE[params]


# ---------------------------------------------------------------------------
# 4. Nulos (shuffle e Poisson) e linhas sintéticas, com unfolding por N̄
# ---------------------------------------------------------------------------


def shuffled_levels(g, rng, sp):
    x = n_bar(g, sp)
    return inverse_n_bar(shuffle_spacings(np.diff(x), origin_x=float(x[0]), rng=rng), sp, R_guess=g)


def poisson_unfolded(n, x0, x1, rng):
    s = rng.exponential(1.0, size=n - 1)
    y = np.concatenate([[0.0], np.cumsum(s)])
    return x0 + y * (x1 - x0) / y[-1]


def poisson_levels(g, rng, sp):
    x0, x1 = float(n_bar(g[0], sp)), float(n_bar(g[-1], sp))
    return inverse_n_bar(poisson_unfolded(len(g), x0, x1, rng), sp, R_guess=g)


def inject_lines(x, T, C, sp, R_guess=None, tol=1e-11, max_iter=60):
    """Resolve N̄(R) + Σ Re[C e^{iRT}/(iT)] = x (mesma construção de `controls.inject_density_lines`)."""
    x = np.asarray(x, dtype=np.float64)
    T = np.asarray(T, dtype=np.float64)
    C = np.asarray(C, dtype=np.complex128)
    R = inverse_n_bar(x, sp, R_guess=R_guess)
    for _ in range(max_iter):
        ph = np.exp(1j * np.outer(R, T))
        f = n_bar(R, sp) + np.real(ph @ (C / (1j * T))) - x
        fp = d_bar(R, sp) + np.real(ph @ C)
        if np.any(fp <= 0):
            raise ValueError("Densidade modulada não positiva: reduza os coeficientes injetados.")
        step = f / fp
        R = R - step
        if np.max(np.abs(step)) < tol:
            break
    return R


def _null_levels(kind, g, seed_state, sp):
    rng = np.random.default_rng(seed_state)
    if kind == "shuffle":
        return shuffled_levels(g, rng, sp)
    if kind == "poisson":
        return poisson_levels(g, rng, sp)
    raise ValueError(kind)


def _task_power(args):
    kind, g, seed_state, params = args
    return np.abs(_instrument(params).transform(_null_levels(kind, g, seed_state, _sp_of(params)))) ** 2


def _task_max(args):
    kind, g, seed_state, params, sigma, fwhm, cand_z = args
    tr = _instrument(params)
    F = tr.transform(_null_levels(kind, g, seed_state, _sp_of(params)))
    peaks = detect_blind_peaks(tr.t_grid, F, fwhm, sigma, candidate_z=cand_z)
    return max_statistic(F, sigma), np.array([p["period"] for p in peaks]), np.array([p["z"] for p in peaks])


def _task_synthetic(args):
    """Cópia de `inverse_spectroscopy._task_synthetic` com fundo de Poisson e N̄ ajustada."""
    g, seed_state, params, sigma, fwhm, thr, n_lines, z_range, pair_sep = args
    sp = _sp_of(params)
    rng = np.random.default_rng(seed_state)
    tr = _instrument(params)
    t_min, t_max = params[2], params[3]
    x0, x1 = float(n_bar(g[0], sp)), float(n_bar(g[-1], sp))
    x = poisson_unfolded(len(g), x0, x1, rng)
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
    budget = 0.8 * float(np.min(d_bar(np.linspace(g[0], g[-1], 2001), sp)))   # ADENDO_MAASS_3 §2.4
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
    F = tr.transform(inject_lines(x, T, C, sp, R_guess=inverse_n_bar(x, sp, R_guess=g)))
    peaks = detect_blind_peaks(tr.t_grid, F, fwhm, sigma, candidate_z=min(3.0, thr))
    per = np.array([p["period"] for p in peaks if p["z"] >= thr])
    out = []
    for k in range(len(T)):
        err = float(per[int(np.argmin(np.abs(per - T[k])))] - T[k]) if len(per) else float("inf")
        out.append({"T": float(T[k]), "z_true": float(z_true[k]), "error": err, "coef_modulus": float(coef_mod[k])})
    return out


# ---------------------------------------------------------------------------
# 5. Catálogo G1 no formato de `arithmetic_comparison`
# ---------------------------------------------------------------------------


def load_g1_lines(path: Path = HERE / "catalogo_g1_linhas.csv") -> List[Dict[str, Any]]:
    with open(path, encoding="utf-8") as f:
        return [{"length": float(r["comprimento"]), "delta": int(r["delta"]), "trace": int(r["traco"]),
                 "n_classes": int(r["n_classes"]), "coefficient": float(r["coeficiente_da_linha"])} for r in csv.DictReader(f)]


def g1_catalog_module(lines: List[Dict[str, Any]]) -> SimpleNamespace:
    def catalog(t_min, t_max):
        cat = [{"prime": ln["trace"], "repetition": 1, "delta": ln["delta"], "period_theoretical": ln["length"],
                "coefficient_theoretical": ln["coefficient"]} for ln in lines if t_min <= ln["length"] <= t_max]
        cat.sort(key=lambda c: c["period_theoretical"])
        for i, c in enumerate(cat):
            c["catalog_index"] = i
        return cat

    return SimpleNamespace(prime_power_catalog=catalog, flag_unresolved=_ar.flag_unresolved, match_one_to_one=_ar.match_one_to_one,
                           targeted_joint_fit=_ar.targeted_joint_fit, detection_limit_coefficient=_ar.detection_limit_coefficient)


# ---------------------------------------------------------------------------
# 6. Bloco (mesma ordem de `inverse_spectroscopy.run_block`)
# ---------------------------------------------------------------------------


def run_block_maass(R_odd, block, cfg, lines, out_dir: Path, seed_seq, workers=1) -> Dict[str, Any]:
    name = block["name"]
    i0, i1 = block["first_index"], block["last_index"]
    g = np.asarray(R_odd[i0 - 1:i1], dtype=np.float64)
    sp = fit_smooth(g, i0)
    # ADENDO_MAASS_3 §2.3: resíduo quadrático médio <= 2 níveis e d̄ > 0 no segmento
    dmin = float(np.min(d_bar(np.linspace(g[0], g[-1], 2001), sp)))
    fit_ok = bool(sp["rms_residual"] <= cfg.get("smooth_fit_max_rms", 2.0) and dmin > 0)
    if not fit_ok:
        raise ValueError(f"[{name}] ajuste suave reprovado (rms={sp['rms_residual']:.3f}, min d̄={dmin:.3f}); bloco não avaliado")
    cand_z = cfg["candidate_z"]
    params = instrument_params(g, cfg, sp)
    bdir = out_dir / name
    bdir.mkdir(parents=True, exist_ok=True)
    timings: Dict[str, float] = {}
    result: Dict[str, Any] = {"block": block, "protocol_version": cfg["protocol_version"], "smooth_fit": sp, "n_levels": len(g)}
    ss_shuffle, ss_poisson, ss_syn, ss_diag, ss_prec, ss_phase = seed_seq.spawn(6)

    t0 = time.perf_counter()
    tr = _instrument(params)
    fwhm = tr.response["fwhm"]
    F = tr.transform(g)
    result["instrument"] = tr.to_metadata()
    result["instrument_diagnostics"] = tr.diagnostics(g, n_check=64, seed=int(ss_diag.generate_state(1)[0]))
    timings["instrument"] = time.perf_counter() - t0

    executor = ProcessPoolExecutor(max_workers=workers) if workers > 1 else None
    try:
        nulls: Dict[str, Dict[str, Any]] = {}
        for kind, child in (("shuffle", ss_shuffle), ("poisson", ss_poisson)):
            n_sigma, n_thr, n_score = cfg[f"{kind}_sigma_realizations"], cfg[f"{kind}_threshold_realizations"], cfg[f"{kind}_score_realizations"]
            t0 = time.perf_counter()
            s_sigma, s_thr, s_score = child.spawn(3)
            powers = _map(executor, _task_power, [(kind, g, s, params) for s in s_sigma.spawn(n_sigma)])
            sigma = null_noise_profile(np.sqrt(np.array(powers)), tr.t_grid, cfg["noise_smooth_window"])
            res_thr = _map(executor, _task_max, [(kind, g, s, params, sigma, fwhm, cand_z) for s in s_thr.spawn(n_thr)])
            null_max = np.array([r[0] for r in res_thr])
            interval = threshold_interval(null_max, cfg["alpha"], cfg["threshold_confidence"])
            res_score = (_map(executor, _task_max, [(kind, g, s, params, sigma, fwhm, cand_z) for s in s_score.spawn(n_score)])
                         if n_score > 0 else [])
            nulls[kind] = {"sigma": sigma, "null_max": null_max, "threshold": interval["z_high"], "interval": interval,
                           "score_set_peaks": [(r[1], r[2]) for r in res_score], "score_set_max": np.array([r[0] for r in res_score]),
                           "B_sigma": n_sigma, "B_threshold": n_thr, "B_score": n_score}
            timings[f"null_{kind}"] = time.perf_counter() - t0
            logger.info(f"[{name}] nulo {kind}: limiar z={interval['point_threshold']:.4f} ({timings[f'null_{kind}']:.1f} s)")

        primary = cfg["primary_null"]
        sigma_p, thr_p = nulls[primary]["sigma"], nulls[primary]["threshold"]
        t0 = time.perf_counter()
        n_syn, seps, n_lines = cfg["synthetic_realizations"], cfg["synthetic_pair_separations_fwhm"], cfg["synthetic_lines_per_realization"]
        # ADENDO_MAASS_2: n_iso linhas isoladas por realização (separação de 10 FWHM precisa caber na janela),
        # com realizações suficientes para o mesmo total de linhas de m4-v3.
        n_iso = min(n_lines, int(math.floor((cfg["t_max"] - cfg["t_min"] - 0.1) / (2.0 * 10.0 * fwhm))))
        if n_iso < 1:                       # ADENDO_MAASS_4: n_iso >= 1 (antes, >= 2 pelo adendo 2)
            raise ValueError(f"[{name}] FWHM {fwhm:.4f} grande demais para a calibração sintética (n_iso = {n_iso}).")
        n_syn_iso = int(math.ceil(n_syn * n_lines / n_iso))
        result["synthetic_isolated_design"] = {"n_iso_per_realization": n_iso, "isolated_realizations": n_syn_iso,
                                               "addendum": "ADENDO_MAASS_2.md"}
        s_iso, s_pair = ss_syn.spawn(2)
        iso = [row for rows in _map(executor, _task_synthetic,
                                    [(g, s, params, sigma_p, fwhm, thr_p, n_iso, (0.5 * thr_p, 4.0 * thr_p), None)
                                     for s in s_iso.spawn(n_syn_iso)]) for row in rows]
        pair_seeds = s_pair.spawn(n_syn)
        pair_rows = []
        for k, sep in enumerate(seps):
            tasks = [(g, s, params, sigma_p, fwhm, thr_p, 2 * max(1, n_lines // 4), (2.0 * thr_p, 4.0 * thr_p), sep)
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
    secondary = "poisson" if primary == "shuffle" else "shuffle"
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
    result["detected_periods_primary"] = [p["period"] for p in peaks if p["detected_primary"]]

    t0 = time.perf_counter()
    result["arithmetic"] = arithmetic_comparison(g1_catalog_module(lines), tr, g, peaks, nulls, primary, tol, res_sep,
                                                 bdir, cfg, ss_prec, ss_phase)
    timings["arithmetic"] = time.perf_counter() - t0
    result["timings_seconds"] = timings
    with open(bdir / "block_metrics.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, default=_json_default)
    return result


# ---------------------------------------------------------------------------
# 7. Critérios (declaração §5 com ADENDO_MAASS_1 §2)
# ---------------------------------------------------------------------------


def _b(v: str) -> bool:
    return str(v).strip() == "True"


def absence_lines(t_min, t_max) -> Dict[str, List[float]]:
    zeta = sorted({math.log(n) for n in range(2, 149) if t_min <= math.log(n) <= t_max})
    scatt = sorted({2 * math.log(n) for n in range(2, 13) if t_min <= 2 * math.log(n) <= t_max})
    return {"zeta_log_n": zeta, "scattering_2log_n": scatt}


def evaluate_block(res: Dict[str, Any], bdir: Path, cfg: Dict[str, Any], lines) -> Dict[str, Any]:
    crit = cfg["criteria"]
    ar = res["arithmetic"]
    fwhm = res["instrument"]["response"]["fwhm"] if "response" in res["instrument"] else res["synthetic_calibration"].get("fwhm")
    thr = res["null_summary"][cfg["primary_null"]]["threshold_z"]
    tol = res["synthetic_calibration"]["matching_tolerance"]
    with open(bdir / "arithmetic_matches.csv", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    by_len = {round(ln["length"], 9): ln for ln in lines}
    info = []
    for r in rows:
        T = float(r["period_theoretical"])
        ln = by_len[round(T, 9)]
        info.append({"T": T, "delta": ln["delta"], "trace": ln["trace"], "c": float(r["coefficient_theoretical"]),
                     "re_C": float(r["fit_coefficient_real"]), "limit": float(r["detection_limit_coefficient"]),
                     "resolved": _b(r["resolved"]), "clear": _b(r["clearly_detectable"]), "detected": _b(r["detected"])})
    Ts = np.array([x["T"] for x in info])
    signs = np.array([x["delta"] for x in info])
    for x in info:
        opp = Ts[signs != x["delta"]]
        x["opposite_sign_within_fwhm"] = bool(len(opp) and np.min(np.abs(opp - x["T"])) < fwhm)
        x["sigma_c"] = x["limit"] / thr
    eligible = [x for x in info if x["resolved"] and x["clear"] and not x["opposite_sign_within_fwhm"]]
    clear = [x for x in info if x["clear"]]
    rec = float(np.mean([x["detected"] for x in clear])) if clear else None
    n_det = ar["detected_peaks_primary"]
    unmatched_frac = (ar["unmatched_detections"] / n_det) if n_det else 0.0
    m_c1 = bool(rec is not None and rec >= crit["recovery_min"] and unmatched_frac <= crit["unmatched_fraction_max"])
    sign_viol = [x["T"] for x in eligible if np.sign(x["re_C"]) != np.sign(x["c"])]
    m_c2s = bool(eligible) and not sign_viol

    def amp(delta):
        el = [x for x in eligible if x["delta"] == delta]
        if not el:
            return {"n_eligible": 0, "fraction_within": None, "passes": False}
        ok = [abs(x["re_C"] - x["c"]) <= crit["amplitude_z"] * x["sigma_c"] for x in el]
        return {"n_eligible": len(el), "fraction_within": float(np.mean(ok)),
                "passes": bool(np.mean(ok) >= crit["amplitude_fraction_min"]),
                "lines": [{"T": x["T"], "c": x["c"], "re_C": x["re_C"], "sigma_c": x["sigma_c"],
                           "ratio": x["re_C"] / x["c"]} for x in el]}

    a_plus, a_minus = amp(1), amp(-1)
    minus_desc = []
    for x in [e for e in eligible if e["delta"] == -1]:
        l = x["T"]
        c_sinh = x["c"] * math.cosh(l / 2) / math.sinh(l / 2)
        minus_desc.append({"T": l, "ratio_H_cosh": x["re_C"] / x["c"], "ratio_H_sinh": x["re_C"] / c_sinh})
    det = np.array(res["detected_periods_primary"])
    absent = {}
    for key, tl in absence_lines(res["instrument"]["t_min"] if "t_min" in res["instrument"] else cfg["t_min"],
                                 res["instrument"]["t_max"] if "t_max" in res["instrument"] else cfg["t_max"]).items():
        cand = [t for t in tl if np.min(np.abs(Ts - t)) > fwhm]
        hits = [t for t in cand if len(det) and np.min(np.abs(det - t)) <= tol]
        absent[key] = {"n_lines": len(cand), "n_detected": len(hits), "detected": hits,
                       "fraction": (len(hits) / len(cand)) if cand else 0.0}
    m_c4 = absent["zeta_log_n"]["fraction"] <= crit["absence_fraction_max"]
    m_c4s = absent["scattering_2log_n"]["fraction"] <= crit["absence_fraction_max"]
    return {"M_C1": m_c1, "recovery_clear": rec, "n_clear": len(clear), "unmatched_fraction": unmatched_frac,
            "M_C2s": m_c2s, "sign_violations": sign_viol, "n_eligible": len(eligible),
            "M_C2a_plus": a_plus["passes"], "amplitude_plus": a_plus, "M_C2a_minus": a_minus["passes"], "amplitude_minus": a_minus,
            "M_C2a_minus_descriptive_cosh_vs_sinh": minus_desc,
            "M_C4": bool(m_c4), "M_C4s": bool(m_c4s), "absence": absent,
            "passes": bool(m_c1 and m_c2s and a_plus["passes"] and a_minus["passes"] and m_c4 and m_c4s)}


# ---------------------------------------------------------------------------
# 8. Execução
# ---------------------------------------------------------------------------


def load_config(path: Path) -> Dict[str, Any]:
    with open(path, "rb") as f:
        return tomllib.load(f)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Instrumento m4-v3 em autovalores de Maass ímpares (ctrl-maass-v1).")
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--dados", type=Path, required=True)
    ap.add_argument("--saida", type=Path, required=True)
    ap.add_argument("--blocos", default="")
    ap.add_argument("--workers", type=int, default=1)
    args = ap.parse_args(argv)
    cfg = load_config(args.config)
    args.saida.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                        handlers=[logging.FileHandler(args.saida / "execution.log"), logging.StreamHandler()])
    data = load_maass(args.dados)
    with open(args.saida / "data_checks.json", "w", encoding="utf-8") as f:
        json.dump(data["checks"], f, indent=2)
    if not data["checks"]["passed"]:
        logger.error(f"conferência B dos dados falhou: {data['checks']}")
        return 2
    lines = load_g1_lines()
    blocks = cfg["blocks"]
    # ADENDO_MAASS_3 §2.1–2.2: nenhum bloco pode conter lacuna de dados
    for b in blocks:
        inside = [gp for gp in data["checks"].get("odd_gaps", []) if b["first_index"] < gp["after_index"] + 1 <= b["last_index"]]
        if inside:
            logger.error(f"bloco {b['name']} contém lacuna de dados: {inside}")
            return 3
    if args.blocos:
        wanted = [b.strip() for b in args.blocos.split(",") if b.strip()]
        blocks = [b for b in blocks if b["name"] in wanted]
    root = np.random.SeedSequence(cfg["seed"])
    seqs = root.spawn(len(cfg["blocks"]))
    t0 = time.perf_counter()
    summary = {"protocol_version": cfg["protocol_version"], "data_checks": data["checks"], "blocks": {}}
    for b in blocks:
        pos = [x["name"] for x in cfg["blocks"]].index(b["name"])
        res = run_block_maass(data["odd"], b, cfg, lines, args.saida, seqs[pos], workers=args.workers)
        summary["blocks"][b["name"]] = evaluate_block(res, args.saida / b["name"], cfg, lines)
    primary = cfg["primary_block"]
    summary["primary_block"] = primary
    summary["passes"] = summary["blocks"].get(primary, {}).get("passes")
    manifest = {"protocol_version": cfg["protocol_version"], "config_sha256": compute_file_sha256(args.config),
                "data_sha256": data["checks"]["sha256"],
                "g1_lines_sha256": compute_file_sha256(HERE / "catalogo_g1_linhas.csv"),
                "script_sha256": {p.name: compute_file_sha256(p) for p in sorted(HERE.glob("*.py"))},
                "seconds": time.perf_counter() - t0}
    with open(args.saida / "criteria_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False, default=_json_default)
    with open(args.saida / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(json.dumps({"passes": summary["passes"], **{n: {k: v[k] for k in ("M_C1", "M_C2s", "M_C2a_plus", "M_C2a_minus", "M_C4", "M_C4s", "passes")}
                                                         for n, v in summary["blocks"].items()}}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
