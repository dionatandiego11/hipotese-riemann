"""Impacto final das três correções numéricas de m4-v3 nos 20 blocos já analisados (m4-v1, m4-v2). Somente leitura."""
import csv, json, sys, time
from pathlib import Path
import numpy as np
sys.path.insert(0, "src"); sys.path.insert(0, "independent")
from riemann_spectra.periods import OscillatoryTransform, classify_detection
from riemann_spectra.cli import load_zeros_csv
from riemann_indep import core
out = {}
for pfx, run, zf in [("b", "results/run_20260913_144429_m3_b01-b02-b03-b04-b05-b06-b07-b08-b09-b10", "data/processed/zeros_40k.csv"),
                     ("c", "results/run_20260913_173045_m3_c01-c02-c03-c04-c05-c06-c07-c08-c09-c10", "data/processed/zeros_70k.csv")]:
    z = load_zeros_csv(Path(zf))
    for i in range(1, 11):
        b = f"{pfx}{i:02d}"
        bm = json.load(open(f"{run}/tables/{b}/block_metrics.json")); rn = np.load(f"{run}/tables/{b}/nulls.npz")
        g = z[bm["block"]["first_index"] - 1:bm["block"]["last_index"]]
        t0 = time.time(); tr = OscillatoryTransform(g[0], g[-1], 0.5, 5.0, points_per_fwhm=8.0); tinit = time.time() - t0
        ex = core.smooth_term(tr.t_grid, g[0], g[-1])
        F_new = tr.transform(g); F_old = rn["F_real"] + 1j * rn["F_imag"]
        F_ind = core.discrete_sum(g, tr.t_grid, g[0], g[-1]) - ex
        peaks = list(csv.DictReader(open(f"{run}/tables/{b}/blind_peaks.csv"))); iv = bm["null_summary"]["shuffle"]["threshold_interval"]
        idx = [int(np.argmin(np.abs(rn["t_grid"] - float(p["grid_period"])))) for p in peaks]
        zn = np.abs(F_new[idx]) / rn["shuffle_sigma"][idx]; zo = np.array([float(p["z"]) for p in peaks])
        out[b] = {"smooth_vs_closed_form_max": float(np.max(np.abs(tr.smooth - ex))),
                  "F_vs_independent_same_grid_max": float(np.max(np.abs(F_new - F_ind))),
                  "F_vs_m4v2_max": float(np.max(np.abs(F_new - F_old))), "z_candidates_rel_change_max": float(np.max(np.abs(zn / zo - 1))),
                  "classification_changes": int(sum(classify_detection(a, iv) != classify_detection(c, iv) for a, c in zip(zo, zn))),
                  "fwhm_rel_error_new": tr.response["fwhm"] / (4 * np.pi / tr.L) - 1, "init_seconds": tinit}
json.dump(out, open("results/m4_v3_impact/impact_final.json", "w"), indent=1)
agg = lambda k: max(abs(v[k]) for v in out.values())  # noqa: E731
print("termo suave × forma fechada: %.2e | F × independente (mesma malha): %.2e | F × m4-v2: %.2e | Δz rel: %.2e | mudanças de classificação: %d | FWHM erro rel: %.1e | init: %.2f s" % (
    agg("smooth_vs_closed_form_max"), agg("F_vs_independent_same_grid_max"), agg("F_vs_m4v2_max"), agg("z_candidates_rel_change_max"),
    sum(v["classification_changes"] for v in out.values()), agg("fwhm_rel_error_new"), agg("init_seconds")))
