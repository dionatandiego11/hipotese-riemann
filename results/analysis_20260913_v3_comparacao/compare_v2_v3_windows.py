"""
Comparação descritiva (somente leitura) das execuções M3 v2 e v3 (Hann e Blackman-Harris).
Não altera decisões; mede: linhas por bloco em cada versão/janela, linhas limítrofes na faixa de
incerteza Monte Carlo do limiar (bootstrap dos máximos nulos) e concordância dos coeficientes.
"""
import csv, json, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, "src")
from riemann_spectra.periods import calibrate_threshold  # noqa: E402

RUNS = {
    "v2_hann": {"pilot": "run_20260913_023918_m3_pilot-dev-val", "dev": "run_20260913_023918_m3_pilot-dev-val",
                "val": "run_20260913_023918_m3_pilot-dev-val", "holdout": "run_20260913_024706_m3_holdout-full",
                "full": "run_20260913_024706_m3_holdout-full"},
    "v3_hann": {"pilot": "run_20260913_130157_m3_pilot-dev-val", "dev": "run_20260913_130157_m3_pilot-dev-val",
                "val": "run_20260913_130157_m3_pilot-dev-val", "holdout": "run_20260913_130758_m3_holdout-full",
                "full": "run_20260913_130758_m3_holdout-full"},
}
bh = sorted(Path("results").glob("run_*_m3_pilot-dev-val-holdout-full"))[-1].name
RUNS["v3_blackman_harris"] = {b: bh for b in ["pilot", "dev", "val", "holdout", "full"]}

rng = np.random.default_rng(20260913)
out = {"runs": RUNS, "blocks": {}}
lines_table = []
for block in ["pilot", "dev", "val", "holdout", "full"]:
    out["blocks"][block] = {}
    det_sets = {}
    for label, runs in RUNS.items():
        bdir = Path("results") / runs[block] / "tables" / block
        rows = list(csv.DictReader(open(bdir / "arithmetic_matches.csv")))
        nulls = np.load(bdir / "nulls.npz")
        m = nulls["shuffle_null_max"]
        thr = calibrate_threshold(m, 0.05)
        boot = np.array([calibrate_threshold(rng.choice(m, len(m)), 0.05) for _ in range(2000)])
        lo, hi = np.quantile(boot, [0.025, 0.975])
        peaks = list(csv.DictReader(open(bdir / "blind_peaks.csv")))
        zcol = "z"
        borderline = [float(p["period"]) for p in peaks if lo <= float(p[zcol]) <= hi]
        det = {(r["prime"], r["repetition"]) for r in rows if r["detected"] == "True"}
        det_sets[label] = det
        sel = [r for r in rows if r["detected"] == "True"]
        ratio_dev = np.array([abs(float(r["fit_ratio_to_theory"]) - 1) for r in sel])
        out["blocks"][block][label] = {
            "run": runs[block],
            "threshold": thr, "threshold_bootstrap_95": [float(lo), float(hi)],
            "n_detected": len(det),
            "n_candidates_in_threshold_band": len(borderline),
            "candidate_periods_in_band": borderline,
            "median_abs_ratio_minus_1_detected": float(np.median(ratio_dev)) if len(ratio_dev) else None,
            "max_abs_ratio_minus_1_detected": float(np.max(ratio_dev)) if len(ratio_dev) else None,
        }
    all_lines = set().union(*det_sets.values())
    out["blocks"][block]["differences"] = {
        "v2_hann_not_v3_hann": sorted(det_sets["v2_hann"] - det_sets["v3_hann"]),
        "v3_hann_not_v2_hann": sorted(det_sets["v3_hann"] - det_sets["v2_hann"]),
        "hann_v3_not_bh": sorted(det_sets["v3_hann"] - det_sets["v3_blackman_harris"]),
        "bh_not_hann_v3": sorted(det_sets["v3_blackman_harris"] - det_sets["v3_hann"]),
        "detected_in_all_three": len(set.intersection(*det_sets.values())),
        "detected_in_any": len(all_lines),
    }

# concordância de coeficientes entre janelas (mesmas linhas, estimador primário de cada execução v3)
coef = {}
for block in ["dev", "val", "holdout", "full"]:
    rh = {(r["prime"], r["repetition"]): float(r["fit_ratio_to_theory"]) for r in csv.DictReader(open(Path("results") / RUNS["v3_hann"][block] / "tables" / block / "arithmetic_matches.csv"))}
    rb = {(r["prime"], r["repetition"]): float(r["fit_ratio_to_theory"]) for r in csv.DictReader(open(Path("results") / RUNS["v3_blackman_harris"][block] / "tables" / block / "arithmetic_matches.csv"))}
    d = np.array([abs(rh[k] - rb[k]) for k in rh])
    coef[block] = {"median_abs_ratio_difference_hann_vs_bh_all47": float(np.median(d)), "max": float(np.max(d))}
out["coefficient_agreement_between_windows"] = coef
Path("results/analysis_20260913_v3_comparacao/comparison.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
for block, v in out["blocks"].items():
    print(block, {k: (v[k]["n_detected"], v[k]["n_candidates_in_threshold_band"]) for k in RUNS}, v["differences"])
print(json.dumps(coef, indent=1))
