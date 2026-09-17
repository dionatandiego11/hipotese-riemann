"""
Impacto das correções m4-v3 (FWHM com precisão de máquina; CUE sem interpolação) apenas em dados já analisados:
20 blocos de m4-v1/m4-v2 e, para D1/D2/D3/D8, os três blocos da auditoria independente. Somente leitura dos resultados.
"""
import csv, json, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, "src"); sys.path.insert(0, "independent")
from riemann_spectra.periods import OscillatoryTransform, classify_detection
from riemann_spectra import cue
from riemann_spectra.cli import load_zeros_csv
from riemann_indep import core as icore, spectral as ispec

runs = {"b": ("results/run_20260913_144429_m3_b01-b02-b03-b04-b05-b06-b07-b08-b09-b10", "results/run_20260913_160910_m2_m4_v1_m2", "data/processed/zeros_40k.csv"),
        "c": ("results/run_20260913_173045_m3_c01-c02-c03-c04-c05-c06-c07-c08-c09-c10", "results/run_20260913_184711_m2_m4_v2_m2", "data/processed/zeros_70k.csv")}
out = {"blocks": {}}
sg = np.linspace(0, 4, 161)
corr = cue.first_correction(sg)
for pfx, (run, m2run, csvf) in runs.items():
    zeros = load_zeros_csv(Path(csvf))
    m2 = json.loads(Path(m2run, "metrics.json").read_text())["blocks"]
    for i in range(1, 11):
        b = f"{pfx}{i:02d}"
        bm = json.loads(Path(run, "tables", b, "block_metrics.json").read_text())
        rn = np.load(Path(run, "tables", b, "nulls.npz"))
        g = zeros[bm["block"]["first_index"] - 1:bm["block"]["last_index"]]
        tr = OscillatoryTransform(g[0], g[-1], 0.5, 5.0, points_per_fwhm=8.0)
        old_fwhm = bm["instrument"]["response"]["fwhm"]
        exact = 4 * np.pi / tr.L
        same_nt = tr.n_t == len(rn["t_grid"])
        shift = float(np.max(np.abs(tr.t_grid - rn["t_grid"]))) if same_nt else None
        F_new = tr.transform(g)
        F_old = rn["F_real"] + 1j * rn["F_imag"]
        sigma = rn["shuffle_sigma"]
        iv = bm["null_summary"]["shuffle"]["threshold_interval"]
        peaks = list(csv.DictReader(open(Path(run, "tables", b, "blind_peaks.csv"))))
        idx = [int(np.argmin(np.abs(rn["t_grid"] - float(p["grid_period"])))) for p in peaks]
        z_new = np.abs(F_new[idx]) / sigma[idx]
        z_old = np.array([float(p["z"]) for p in peaks])
        changed = [(float(p["period"]), float(zo), float(zn)) for p, zo, zn in zip(peaks, z_old, z_new)
                   if classify_detection(zo, iv) != classify_detection(zn, iv)]
        x = np.sort(np.diff(np.log(g / (2 * np.pi)) * g / (2 * np.pi) - g / (2 * np.pi)))  # não usado; espaçamentos abaixo
        from riemann_spectra.unfolding import n_bar_rvm
        s = np.sort(np.diff(n_bar_rvm(g)))
        emp = np.searchsorted(s, sg, side="right") / len(s)
        pred = cue.zeros_prediction(corr, float(np.median(g)))
        old_c = m2[b]["cue_secondary"]
        new_rms = float(np.sqrt(np.mean((emp - pred["cdf"]) ** 2)))
        mu = np.trapezoid(sg * pred["pdf"], sg)
        new_var = float(np.trapezoid(sg * sg * pred["pdf"], sg) - mu * mu)
        out["blocks"][b] = {
            "fwhm_rel_error_old": old_fwhm / exact - 1, "fwhm_rel_error_new": tr.response["fwhm"] / exact - 1,
            "n_t_same": same_nt, "grid_max_shift": shift,
            "F_max_abs_change_on_grid": float(np.max(np.abs(F_new - F_old))) if same_nt else None,
            "z_candidates_max_rel_change": float(np.max(np.abs(z_new / z_old - 1))),
            "classification_changes": changed,
            "cue_rms_corrected_old": old_c["rms_cdf_distance_to_cue_corrected"], "cue_rms_corrected_new": new_rms,
            "cue_var_corrected_old": old_c["spacing_variance_cue_corrected"], "cue_var_corrected_new": new_var,
        }
# D1/D2/D3/D8 repetidos (determinísticos) contra a implementação independente nos três blocos auditados
aud = {"baixo_b01": ("b", 1, 10001, 13000), "intermediario_b05": ("b", 5, 22001, 25000), "alto_c10": ("c", 10, 67001, 70000)}
out["audit_deterministic_recheck"] = {}
ic = ispec.CUECorrection()
for lab, (pfx, i, i0, i1) in aud.items():
    g = icore.read_raw_zeros("data/raw/zeros1", i0, i1)
    tr = OscillatoryTransform(g[0], g[-1], 0.5, 5.0, points_per_fwhm=8.0)
    ins = icore.Instrument(g)
    ia = np.load(f"results/independent_audit_20260913/{lab}/arrays.npz")
    grid_diff = float(np.max(np.abs(tr.t_grid - ins.t)))
    dF = float(np.max(np.abs(tr.transform(g) - ia["F"])))
    dS = float(np.max(np.abs(tr.smooth - ia["smooth"])))
    pred_r = cue.zeros_prediction(corr, float(np.median(g)))
    pred_i = ispec.cue_prediction(ic, float(np.median(g)), sg)
    out["audit_deterministic_recheck"][lab] = {
        "D1_dt_rel": tr.dt / ins.dt - 1, "D1_pass": abs(tr.dt / ins.dt - 1) <= 1e-10 and tr.n_t == ins.n_t,
        "grid_max_diff": grid_diff, "D2_max_abs": dS, "D2_pass": grid_diff < 1e-12 and dS <= 1e-8,
        "D3_max_abs": dF, "D3_pass": grid_diff < 1e-12 and dF <= 1e-7,
        "D8_pred_cdf_max_abs": float(np.max(np.abs(pred_r["cdf"] - pred_i["cdf"]))),
        "D8_pass": float(np.max(np.abs(pred_r["cdf"] - pred_i["cdf"]))) <= 1e-6,
    }
Path("results/m4_v3_impact/impact.json").write_text(json.dumps(out, indent=1, default=float))
B = out["blocks"]
print("FWHM erro rel antigo máx %.2e -> novo máx %.2e" % (max(abs(v["fwhm_rel_error_old"]) for v in B.values()), max(abs(v["fwhm_rel_error_new"]) for v in B.values())))
print("deslocamento de malha máx %.2e; ΔF máx %.2e; Δz relativo máx %.2e; mudanças de classificação: %d" % (
    max(v["grid_max_shift"] for v in B.values()), max(v["F_max_abs_change_on_grid"] for v in B.values()),
    max(v["z_candidates_max_rel_change"] for v in B.values()), sum(len(v["classification_changes"]) for v in B.values())))
print("CUE RMS corrigida |Δ| máx %.2e (valores %.4f–%.4f); Var corrigida |Δ| máx %.2e" % (
    max(abs(v["cue_rms_corrected_new"] - v["cue_rms_corrected_old"]) for v in B.values()),
    min(v["cue_rms_corrected_new"] for v in B.values()), max(v["cue_rms_corrected_new"] for v in B.values()),
    max(abs(v["cue_var_corrected_new"] - v["cue_var_corrected_old"]) for v in B.values())))
print(json.dumps(out["audit_deterministic_recheck"], indent=1, default=float))
