"""Diagnóstico das verificações fora da tolerância (D1, D2, D3, D8). Não altera nenhuma das implementações."""
import json, math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, "independent"); sys.path.insert(0, "src")
from riemann_indep import core, spectral
from riemann_spectra.periods import OscillatoryTransform, hann_response as ref_W
from riemann_spectra import cue as ref_cue
from riemann_spectra.cli import load_zeros_csv

OUT = Path("results/independent_audit_20260913")
REF = {"baixo_b01": ("b01", "results/run_20260913_144429_m3_b01-b02-b03-b04-b05-b06-b07-b08-b09-b10", "data/processed/zeros_40k.csv", 10001, 13000),
       "intermediario_b05": ("b05", "results/run_20260913_144429_m3_b01-b02-b03-b04-b05-b06-b07-b08-b09-b10", "data/processed/zeros_40k.csv", 22001, 25000),
       "alto_c10": ("c10", "results/run_20260913_173045_m3_c01-c02-c03-c04-c05-c06-c07-c08-c09-c10", "data/processed/zeros_70k.csv", 67001, 70000)}
diag = {}
for label, (b, run, csvf, i0, i1) in REF.items():
    g = core.read_raw_zeros("data/raw/zeros1", i0, i1)
    L = g[-1] - g[0]
    bm = json.loads(Path(run, "tables", b, "block_metrics.json").read_text())
    rn = np.load(Path(run, "tables", b, "nulls.npz"))
    ia = np.load(OUT / label / "arrays.npz")
    d = {}
    # (1) FWHM exata de Hann: |W| = W(0)/2 em ω = 2π/L (W = L/4), logo FWHM = 4π/L
    exact = 4 * math.pi / L
    d["W_at_2pi_over_L_over_W0"] = float(ref_W(2 * math.pi / L, L) / ref_W(0.0, L))
    d["fwhm_rel_error_reference"] = bm["instrument"]["response"]["fwhm"] / exact - 1
    d["fwhm_rel_error_independent"] = core.fwhm_hann(L) / exact - 1
    d["grid_max_abs_shift"] = float(np.max(np.abs(rn["t_grid"] - ia["t"])))
    d["same_input_data"] = bool(np.array_equal(g, load_zeros_csv(Path(csvf))[i0 - 1:i1]))
    # (2) implementação independente avaliada na malha da referência
    t_ref = rn["t_grid"]
    F_ind_on_ref = core.discrete_sum(g, t_ref, g[0], g[-1]) - core.smooth_term(t_ref, g[0], g[-1])
    F_ref = rn["F_real"] + 1j * rn["F_imag"]
    dd = np.abs(F_ind_on_ref - F_ref)
    tr = OscillatoryTransform(g[0], g[-1], 0.5, 5.0, points_per_fwhm=8.0)
    ds = np.abs(core.smooth_term(t_ref, g[0], g[-1]) - tr.smooth)
    d["F_same_grid_max_abs"] = float(dd.max()); d["F_same_grid_median_abs"] = float(np.median(dd))
    d["smooth_same_grid_max_abs"] = float(ds.max()); d["smooth_same_grid_median_abs"] = float(np.median(ds))
    # efeito do deslocamento da malha sobre z nos máximos detectados (relativo)
    peaks = json.loads((OUT / label / "blind_peaks.json").read_text())
    idx = [p["i"] for p in peaks]
    d["relative_change_F_at_peaks_due_to_grid_shift_max"] = float(np.max(np.abs(np.abs(ia["F"][idx]) / np.abs(F_ind_on_ref[idx]) - 1)))
    # (3) CUE: predição com a interpolação linear usada pela referência, a partir dos P1 independentes
    sg = np.linspace(0, 4, 161)
    corr_i = spectral.CUECorrection()
    ne, al = float(spectral.n_eff(np.median(g))), float(spectral.alpha_bblm(np.median(g)))
    P1g = corr_i.P1(sg)
    pred_interp_style = corr_i.P0(sg) + np.interp(al * sg, sg, P1g, right=float(P1g[-1])) / (al * ne * ne)
    corr_r = ref_cue.first_correction(sg)
    pred_r = ref_cue.zeros_prediction(corr_r, float(np.median(g)))
    exact_pred = corr_i.P0(sg) + corr_i.P1(al * sg) / (al * ne * ne)
    d["cue_pred_diff_same_interpolation"] = float(np.max(np.abs(pred_interp_style - pred_r["cdf"])))
    d["cue_linear_interpolation_error_in_reference"] = float(np.max(np.abs(pred_r["cdf"] - exact_pred)))
    diag[label] = d
(OUT / "diagnostics.json").write_text(json.dumps(diag, indent=1))
print(json.dumps(diag, indent=1))
