"""
riemann_spectra.spectral_pipeline
M1 (verificações de fundação e controles) e M2 (Etapas 4-6) com envelopes de controles
submetidos aos mesmos estimadores.
"""

import csv
import json
import logging
import math
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np

from riemann_spectra.controls import (
    generate_gue_central_levels,
    generate_gue_dense,
    generate_gue_tridiagonal,
    generate_poisson_spectrum,
    shuffle_spacings,
)
from riemann_spectra.form_factor import compute_spectral_form_factor
from riemann_spectra.statistics import (
    compute_pair_correlation,
    compute_spacing_statistics,
    poisson_cdf,
    wigner_gue_cdf,
)
from riemann_spectra.unfolding import inverse_n_bar, n_bar_rvm, n_bar_theta, unfold_spectrum
from riemann_spectra.utils import compute_file_sha256

logger = logging.getLogger("riemann_spectra.spectral_pipeline")

BLOCKS = [("pilot", 1, 1000), ("dev", 1001, 4000), ("val", 4001, 7000), ("holdout", 7001, 10000), ("full", 1, 10000)]


# ---------------------------------------------------------------------------
# M1
# ---------------------------------------------------------------------------

def run_m1(zeros: np.ndarray, cfg: Dict[str, Any], run_dir: Path, seq: np.random.SeedSequence) -> Tuple[Dict, List[str], List[str]]:
    rng = np.random.default_rng(seq)
    m: Dict[str, Any] = {}
    findings: List[str] = []
    limits: List[str] = []

    # dados
    manifest_path = Path(cfg.get("raw_data_dir", "data/raw")) / "data_manifest.json"
    val_path = Path(cfg.get("processed_data_dir", "data/processed")) / "data_validation.json"
    with open(manifest_path, encoding="utf-8") as f:
        dman = json.load(f)
    raw_ok = compute_file_sha256(dman["raw_file"]["path"]) == dman["raw_file"]["sha256"]
    proc_ok = compute_file_sha256(dman["processed_file"]["path"]) == dman["processed_file"]["sha256"]
    with open(val_path, encoding="utf-8") as f:
        dval = json.load(f)
    diffs = np.diff(zeros)
    m["data"] = {
        "raw_sha256_matches_manifest": raw_ok,
        "processed_sha256_matches_manifest": proc_ok,
        "strictly_increasing": bool(np.all(diffs > 0)),
        "all_finite": bool(np.all(np.isfinite(zeros))),
        "mpmath_sample_size": dval["sample_size"],
        "mpmath_max_abs_error": dval["max_absolute_error_observed"],
        "mpmath_all_within_tolerance": dval["all_within_tolerance"],
    }
    if not (raw_ok and proc_ok and m["data"]["strictly_increasing"] and dval["all_within_tolerance"]):
        raise RuntimeError(f"Falha na auditoria dos dados: {m['data']}")
    findings.append(
        f"B: hashes de dados conferem com o manifesto; {len(zeros)} ordenadas finitas e estritamente crescentes; "
        f"amostra de {dval['sample_size']} índices recalculada com mpmath (máx. |erro| = {dval['max_absolute_error_observed']:.2e})."
    )
    limits.append("A validação por amostra não certifica completude da tabela nem localização rigorosa de todos os zeros.")

    # unfolding: inversão
    x = n_bar_rvm(zeros)
    inv_err = float(np.max(np.abs(inverse_n_bar(x) - zeros)))
    m["unfolding_inverse_max_abs_error"] = inv_err
    if inv_err > 1e-8:
        raise RuntimeError(f"Inversão de Nbar com erro {inv_err:.2e}")

    # invariância por permutação da ordem dos níveis
    perm = rng.permutation(zeros)
    xp = n_bar_rvm(perm)
    r2a = compute_pair_correlation(x, 5.0, 50)["bins"]["r2_empirical"]
    r2b = compute_pair_correlation(xp, 5.0, 50)["bins"]["r2_empirical"]
    tau = np.linspace(0.05, 1.5, 30)
    ka = compute_spectral_form_factor(x, tau, n_blocks=4)["k_connected"]
    kb = compute_spectral_form_factor(xp, tau, n_blocks=4)["k_connected"]
    m["permutation_invariance"] = {
        "r2_max_abs_diff": float(np.max(np.abs(np.subtract(r2a, r2b)))),
        "sff_max_abs_diff": float(np.max(np.abs(np.subtract(ka, kb)))),
    }

    # Poisson
    n_poi = 20000
    poi_fixed = generate_poisson_spectrum(n_poi, length=n_poi, fixed_count=True, rng=rng)
    poi_free = generate_poisson_spectrum(n_poi, length=n_poi, fixed_count=False, rng=rng)
    m["control_poisson"] = {
        "fixed_count": {"n": len(poi_fixed), "density": (len(poi_fixed) - 1) / (poi_fixed[-1] - poi_fixed[0]), "spacing_var": float(np.var(np.diff(poi_fixed), ddof=1))},
        "random_count": {"n": len(poi_free), "density": len(poi_free) / n_poi, "spacing_var": float(np.var(np.diff(poi_free), ddof=1))},
        "convention": "comparações com zeros usam contagem fixa (mesmo n que o bloco)",
    }

    # GUE denso vs tridiagonal (mesma dimensão, mesma normalização e unfolding)
    dim, reps = 400, 30
    s_dense, s_tri = [], []
    for _ in range(reps):
        b, _ = generate_gue_dense(dim, bulk_fraction=1.0, rng=rng)
        s_dense.append(np.diff(b))
        b, _ = generate_gue_tridiagonal(dim, bulk_fraction=1.0, rng=rng)
        s_tri.append(np.diff(b))
    s_dense = np.concatenate(s_dense)
    s_tri = np.concatenate(s_tri)
    grid = np.linspace(0, 4, 400)
    cd = np.searchsorted(np.sort(s_dense), grid, side="right") / len(s_dense)
    ct = np.searchsorted(np.sort(s_tri), grid, side="right") / len(s_tri)
    m["control_gue_dense_vs_tridiagonal"] = {
        "matrix_dim": dim, "realizations": reps, "bulk_interval": "[-0.5, 0.5] do semicírculo",
        "dense_mean": float(s_dense.mean()), "dense_var": float(s_dense.var(ddof=1)),
        "tridiagonal_mean": float(s_tri.mean()), "tridiagonal_var": float(s_tri.var(ddof=1)),
        "cdf_sup_distance": float(np.max(np.abs(cd - ct))),
        "n_spacings_each": int(min(len(s_dense), len(s_tri))),
    }
    findings.append(
        f"B: controles verificados — permutar a ordem dos níveis altera R2 em {m['permutation_invariance']['r2_max_abs_diff']:.1e} e K_c em "
        f"{m['permutation_invariance']['sff_max_abs_diff']:.1e}; inversão de Nbar com erro {inv_err:.1e}; GUE denso e tridiagonal (N={dim}, {reps} matrizes) "
        f"com variâncias de espaçamento {m['control_gue_dense_vs_tridiagonal']['dense_var']:.4f} e {m['control_gue_dense_vs_tridiagonal']['tridiagonal_var']:.4f} "
        f"e distância sup entre CDFs {m['control_gue_dense_vs_tridiagonal']['cdf_sup_distance']:.3f}."
    )
    return m, findings, limits


# ---------------------------------------------------------------------------
# M2
# ---------------------------------------------------------------------------

def _cdf_on(s: np.ndarray, grid: np.ndarray) -> np.ndarray:
    return np.searchsorted(np.sort(s), grid, side="right") / len(s)


def _block_statistics(levels_unfolded: np.ndarray, cfg: Dict[str, Any], tau: np.ndarray, n_sff_blocks: int) -> Dict[str, Any]:
    s = np.diff(levels_unfolded)
    grid = np.linspace(0, cfg.get("s_max", 5.0), 1001)
    r2 = compute_pair_correlation(levels_unfolded, cfg.get("s_max", 5.0), cfg.get("s_bins", 50))
    sff = compute_spectral_form_factor(levels_unfolded, tau, n_blocks=n_sff_blocks)
    return {
        "mean": float(s.mean()),
        "var": float(s.var(ddof=1)),
        "cdf": _cdf_on(s, grid),
        "r2": np.array(r2["bins"]["r2_empirical"]),
        "k_connected": np.array(sff["k_connected"]),
    }


def _task_gue_block(args):
    n, frac, seed, cfg, tau, n_sff_blocks = args
    y, _ = generate_gue_central_levels(n, frac, np.random.default_rng(seed))
    return _block_statistics(y, cfg, tau, n_sff_blocks)


def _task_poisson_block(args):
    n, seed, cfg, tau, n_sff_blocks = args
    y = generate_poisson_spectrum(n, length=float(n - 1), fixed_count=True, rng=np.random.default_rng(seed))
    return _block_statistics(y, cfg, tau, n_sff_blocks)


def _envelope_test(obs: Dict[str, Any], ens: List[Dict[str, Any]], key: str) -> Dict[str, Any]:
    """
    Distância L2 ao valor médio do ensemble; calibração por leave-one-out no próprio ensemble:
    p = (1 + #{d_b >= d_obs}) / (B + 1).
    """
    arr = np.array([e[key] for e in ens])
    B = len(arr)
    mean = arr.mean(axis=0)
    d_obs = float(np.sqrt(np.mean((obs[key] - mean) ** 2)))
    d_null = []
    for b in range(B):
        mean_loo = (mean * B - arr[b]) / (B - 1)
        d_null.append(float(np.sqrt(np.mean((arr[b] - mean_loo) ** 2))))
    d_null = np.array(d_null)
    return {
        "distance_obs": d_obs,
        "distance_null_median": float(np.median(d_null)),
        "p_value_mc": float((1 + np.sum(d_null >= d_obs)) / (B + 1)),
        "B": B,
        "q025": np.quantile(arr, 0.025, axis=0),
        "q975": np.quantile(arr, 0.975, axis=0),
        "mean": mean,
    }


def run_m2(zeros: np.ndarray, cfg: Dict[str, Any], run_dir: Path, seq: np.random.SeedSequence, workers: int = 1) -> Tuple[Dict, List[str], List[str]]:
    from riemann_spectra.reporting import plot_m2_block

    s_max = cfg.get("s_max", 5.0)
    n_bins = cfg.get("s_bins", 50)
    B_gue = cfg.get("m2_gue_realizations", 99)
    B_poi = cfg.get("m2_poisson_realizations", 99)
    frac = cfg.get("gue_retained_fraction", 0.6)
    n_sff_blocks = cfg.get("sff_blocks", 10)
    tau = np.linspace(0.02, 2.0, cfg.get("sff_tau_points", 100))
    grid = np.linspace(0, s_max, 1001)
    m: Dict[str, Any] = {"blocks": {}}
    findings: List[str] = []
    limits: List[str] = [
        "Blocos contíguos de um espectro determinístico não são amostras independentes.",
        "Envelopes GUE usam uma matriz por realização (níveis centrais), sem concatenação de matrizes.",
        "Valores-p do envelope medem incompatibilidade com o ensemble finito do mesmo tamanho, não com o limite assintótico.",
    ]
    block_seqs = seq.spawn(len(BLOCKS))
    executor = ProcessPoolExecutor(max_workers=workers) if workers > 1 else None
    try:
        for (name, i0, i1), bseq in zip(BLOCKS, block_seqs):
            if i1 > len(zeros):
                m["blocks"][name] = {"status": "não executado: zeros insuficientes"}
                continue
            g = zeros[i0 - 1:i1]
            n = len(g)
            x_rvm = n_bar_rvm(g)
            x_theta = n_bar_theta(g)
            obs = _block_statistics(x_rvm, cfg, tau, n_sff_blocks)
            s = np.diff(x_rvm)
            st = compute_spacing_statistics(s, s_bins=n_bins, s_max=s_max)
            s_theta = np.diff(x_theta)
            seeds_g, seeds_p = bseq.spawn(2)
            tasks_g = [(n, frac, sd, cfg, tau, n_sff_blocks) for sd in seeds_g.spawn(B_gue)]
            tasks_p = [(n, sd, cfg, tau, n_sff_blocks) for sd in seeds_p.spawn(B_poi)]
            if executor is None:
                ens_g = [_task_gue_block(t) for t in tasks_g]
                ens_p = [_task_poisson_block(t) for t in tasks_p]
            else:
                ens_g = list(executor.map(_task_gue_block, tasks_g, chunksize=4))
                ens_p = list(executor.map(_task_poisson_block, tasks_p, chunksize=4))

            tests = {}
            for label, ens in (("gue", ens_g), ("poisson", ens_p)):
                tests[label] = {k: _envelope_test(obs, ens, k) for k in ("cdf", "r2", "k_connected")}
                tests[label]["spacing_var_ensemble_q025_q975"] = np.quantile([e["var"] for e in ens], [0.025, 0.975]).tolist()

            # faixas fixas para R2
            edges = np.linspace(0, s_max, n_bins + 1)
            centers = 0.5 * (edges[:-1] + edges[1:])
            r2 = compute_pair_correlation(x_rvm, s_max, n_bins)
            bands = {}
            for lo, hi in ((0.0, 1.0), (1.0, 2.0), (2.0, s_max)):
                mk = (centers >= lo) & (centers < hi)
                bands[f"{lo:g}-{hi:g}"] = float(np.mean((np.array(r2["bins"]["r2_empirical"])[mk] - np.array(r2["bins"]["r2_gue"])[mk]) ** 2))

            outside_r2 = float(np.mean((obs["r2"] < tests["gue"]["r2"]["q025"]) | (obs["r2"] > tests["gue"]["r2"]["q975"])))
            outside_k = float(np.mean((obs["k_connected"] < tests["gue"]["k_connected"]["q025"]) | (obs["k_connected"] > tests["gue"]["k_connected"]["q975"])))
            blk = {
                "indices": [i0, i1],
                "gamma_range": [float(g[0]), float(g[-1])],
                "n_levels": n,
                "spacing_mean_before_renormalization": st["mean"],
                "spacing_variance": st["variance"],
                "spacing_skewness": st["skewness"],
                "spacing_kurtosis": st["kurtosis"],
                "ks_distance_wigner_surmise": st["ks_distance_wigner"],
                "wasserstein_wigner_surmise": st["wasserstein_distance_wigner"],
                "ks_distance_poisson": st["ks_distance_poisson"],
                "wasserstein_poisson": st["wasserstein_distance_poisson"],
                "theta_vs_rvm_unfolding": {
                    "max_abs_x_difference": float(np.max(np.abs(x_theta - x_rvm))),
                    "spacing_variance_theta": float(np.var(s_theta, ddof=1)),
                    "max_abs_spacing_difference": float(np.max(np.abs(s_theta - s))),
                },
                "r2_band_mse_vs_montgomery": bands,
                "r2_fraction_bins_outside_gue_95_band": outside_r2,
                "sff_fraction_tau_outside_gue_95_band": outside_k,
                "envelope_tests": {
                    lab: {k: {kk: vv for kk, vv in t.items() if kk in ("distance_obs", "distance_null_median", "p_value_mc", "B")} for k, t in tt.items() if isinstance(t, dict)}
                    | {"spacing_var_ensemble_q025_q975": tt["spacing_var_ensemble_q025_q975"]}
                    for lab, tt in tests.items()
                },
            }
            m["blocks"][name] = blk

            tdir = run_dir / "tables"
            with open(tdir / f"m2_{name}_spacing_cdf.csv", "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["s", "cdf_zeros", "cdf_gue_mean", "cdf_gue_q025", "cdf_gue_q975", "cdf_poisson_ensemble_mean", "cdf_wigner_surmise", "cdf_poisson"])
                for i, sv in enumerate(grid):
                    w.writerow([sv, obs["cdf"][i], tests["gue"]["cdf"]["mean"][i], tests["gue"]["cdf"]["q025"][i], tests["gue"]["cdf"]["q975"][i], tests["poisson"]["cdf"]["mean"][i], float(wigner_gue_cdf(sv)), float(poisson_cdf(sv))])
            with open(tdir / f"m2_{name}_pair_correlation.csv", "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["bin_low", "bin_high", "count", "r2_zeros", "r2_montgomery_bin_average", "r2_gue_q025", "r2_gue_q975", "r2_poisson_mean"])
                for i in range(n_bins):
                    w.writerow([edges[i], edges[i + 1], r2["bins"]["counts"][i], obs["r2"][i], r2["bins"]["r2_gue"][i], tests["gue"]["r2"]["q025"][i], tests["gue"]["r2"]["q975"][i], tests["poisson"]["r2"]["mean"][i]])
            with open(tdir / f"m2_{name}_form_factor.csv", "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["tau", "k_connected_zeros", "k_gue_mean", "k_gue_q025", "k_gue_q975", "k_poisson_mean", "k_gue_limit_min_tau_1"])
                for i, tv in enumerate(tau):
                    w.writerow([tv, obs["k_connected"][i], tests["gue"]["k_connected"]["mean"][i], tests["gue"]["k_connected"]["q025"][i], tests["gue"]["k_connected"]["q975"][i], tests["poisson"]["k_connected"]["mean"][i], min(tv, 1.0)])
            plot_m2_block(run_dir / "figures", name, grid, obs, tests, edges, r2, tau)

            logger.info(f"[M2 {name}] var(s)={st['variance']:.4f} p_GUE(cdf,r2,K)=({tests['gue']['cdf']['p_value_mc']:.3f},{tests['gue']['r2']['p_value_mc']:.3f},{tests['gue']['k_connected']['p_value_mc']:.3f}) p_Poisson(cdf)={tests['poisson']['cdf']['p_value_mc']:.3f}")
            findings.append(
                f"B/{name} (zeros {i0}–{i1}): média de espaçamento {st['mean']:.4f} e variância {st['variance']:.4f} antes de renormalização "
                f"(envelope GUE 95% da variância {tests['gue']['spacing_var_ensemble_q025_q975'][0]:.4f}–{tests['gue']['spacing_var_ensemble_q025_q975'][1]:.4f}); "
                f"p do envelope GUE (CDF, R2, K_c) = {tests['gue']['cdf']['p_value_mc']:.3f}, {tests['gue']['r2']['p_value_mc']:.3f}, {tests['gue']['k_connected']['p_value_mc']:.3f}; "
                f"p do envelope Poisson (CDF) = {tests['poisson']['cdf']['p_value_mc']:.3f} (B={B_gue}/{B_poi})."
            )
    finally:
        if executor is not None:
            executor.shutdown()
    m["settings"] = {"B_gue": B_gue, "B_poisson": B_poi, "gue_retained_fraction": frac, "sff_blocks": n_sff_blocks, "s_bins": n_bins, "s_max": s_max}
    return m, findings, limits
