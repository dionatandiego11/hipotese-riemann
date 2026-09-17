"""
Comparação implementação independente × referência, com as tolerâncias de independent/COMPARISON_PLAN.md
(congelado em independent/PLAN.lock.json). Primeiro e único ponto em que arquivos de referência por bloco são abertos.
Intermediários determinísticos não gravados pela referência (termo suave, F em T_k, P₀/P₁ CUE) são regenerados
chamando o código de referência (`src/riemann_spectra`), o que é legítimo para a comparação.
"""
import csv, hashlib, json, math, sys
from pathlib import Path

import numpy as np
from scipy.stats import binom, ks_2samp

sys.path.insert(0, "src")
from riemann_spectra.periods import OscillatoryTransform  # referência
from riemann_spectra import cue as ref_cue  # referência
from riemann_spectra.cli import load_zeros_csv  # referência (leitura de dados)

OUT = Path("results/independent_audit_20260913")
plan = json.loads(Path("independent/PLAN.lock.json").read_text())
assert hashlib.sha256(Path("independent/COMPARISON_PLAN.md").read_bytes()).hexdigest() == plan["COMPARISON_PLAN.md"]

REF = {
    "baixo_b01": ("b01", "results/run_20260913_144429_m3_b01-b02-b03-b04-b05-b06-b07-b08-b09-b10", "results/run_20260913_160910_m2_m4_v1_m2", "data/processed/zeros_40k.csv"),
    "intermediario_b05": ("b05", "results/run_20260913_144429_m3_b01-b02-b03-b04-b05-b06-b07-b08-b09-b10", "results/run_20260913_160910_m2_m4_v1_m2", "data/processed/zeros_40k.csv"),
    "alto_c10": ("c10", "results/run_20260913_173045_m3_c01-c02-c03-c04-c05-c06-c07-c08-c09-c10", "results/run_20260913_184711_m2_m4_v2_m2", "data/processed/zeros_70k.csv"),
}
SEPS = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0]


def check(code, ok, value, rule):
    return {"code": code, "pass": bool(ok), "value": value, "rule": rule}


def csv_rows(p):
    return list(csv.DictReader(open(p)))


report = {"plan_lock": plan, "blocks": {}}
for label, (b, run, m2run, csvfile) in REF.items():
    ind = json.loads((OUT / label / "summary.json").read_text())
    ind_lines = json.loads((OUT / label / "lines.json").read_text())
    ia = np.load(OUT / label / "arrays.npz")
    im2 = np.load(OUT / label / "m2_arrays.npz")
    bm = json.loads(Path(run, "tables", b, "block_metrics.json").read_text())
    rn = np.load(Path(run, "tables", b, "nulls.npz"))
    rrows = csv_rows(Path(run, "tables", b, "arithmetic_matches.csv"))
    rinc = csv_rows(Path(run, "tables", b, "inconclusive_candidates.csv"))
    rm2 = json.loads(Path(m2run, "metrics.json").read_text())["blocks"][b]
    fam = json.loads(Path(run, "family_summary.json").read_text())["blocks"][b]
    C = []
    inst = bm["instrument"]

    # ---------------- D1 instrumento
    C.append(check("D1", ind["n_t"] == inst["n_t"] and abs(ind["dt"] / inst["dt"] - 1) <= 1e-10 and abs(ind["fwhm"] / inst["response"]["fwhm"] - 1) <= 1e-10
                   and abs(ind["W0"] / inst["response"]["gain_W0"] - 1) <= 1e-10,
                   {"n_t": [ind["n_t"], inst["n_t"]], "dt_rel": ind["dt"] / inst["dt"] - 1, "fwhm_rel": ind["fwhm"] / inst["response"]["fwhm"] - 1,
                    "W0_rel": ind["W0"] / inst["response"]["gain_W0"] - 1}, "n_t igual; dt, FWHM, W0 rel ≤ 1e-10"))
    t_ref = rn["t_grid"]
    grid_same = len(t_ref) == len(ia["t"]) and np.max(np.abs(t_ref - ia["t"])) < 1e-12

    # ---------------- D2/D3/D4 transformada (regenera intermediários da referência)
    g = load_zeros_csv(Path(csvfile))[bm["block"]["first_index"] - 1:bm["block"]["last_index"]]
    tr = OscillatoryTransform(g[0], g[-1], 0.5, 5.0, points_per_fwhm=8.0, panel_length=0.5, quad_order=8, density="rvm", window="hann")
    dS = np.abs(tr.smooth - ia["smooth"])
    C.append(check("D2", grid_same and dS.max() <= 1e-8, {"max_abs": float(dS.max()), "median_abs": float(np.median(dS))}, "máx abs ≤ 1e-8"))
    F_ref = rn["F_real"] + 1j * rn["F_imag"]
    dF = np.abs(F_ref - ia["F"])
    C.append(check("D3", grid_same and dF.max() <= 1e-7 and np.median(dF) <= 1e-8, {"max_abs": float(dF.max()), "median_abs": float(np.median(dF)),
                   "max_abs_F": float(np.abs(F_ref).max())}, "máx ≤ 1e-7; mediana ≤ 1e-8"))
    T = np.array([float(r["period_theoretical"]) for r in rrows])
    FT_ref = tr.evaluate(g, T)
    FT_ind = np.array([complex(*l["F_at_T"]) for l in ind_lines])
    C.append(check("D4", np.max(np.abs(FT_ref - FT_ind)) <= 1e-8, {"max_abs": float(np.max(np.abs(FT_ref - FT_ind)))}, "máx abs ≤ 1e-8"))

    # ---------------- D9 catálogo
    Ti = np.array([l["T"] for l in ind_lines])
    same_cat = len(Ti) == len(T) and np.max(np.abs(Ti - T)) <= 1e-14 and all(int(r["prime"]) == l["p"] and int(r["repetition"]) == l["r"] for r, l in zip(rrows, ind_lines))
    C.append(check("D9", same_cat, {"n": [len(Ti), len(T)]}, "mesmas entradas; períodos ≤ 1e-14"))

    # ---------------- D5 coeficientes
    d5 = {}
    for vi, vr in (("ratio_band_conjugate", "fit_ratio_to_theory"), ("ratio_band_no_conjugate", "ratio_to_theory__band_no_conjugate"),
                   ("ratio_centers_conjugate", "ratio_to_theory__centers_conjugate")):
        d = np.array([abs(l[vi] - float(r[vr])) for l, r in zip(ind_lines, rrows)])
        d5[vi] = {"max_abs": float(d.max()), "median_abs": float(np.median(d)), "worst_line": f"{ind_lines[int(d.argmax())]['p']}^{ind_lines[int(d.argmax())]['r']}"}
    C.append(check("D5", all(v["max_abs"] <= 1e-9 for v in d5.values()), d5, "máx abs Δrazão ≤ 1e-9 (3 variantes, 47 linhas)"))

    # ---------------- S1 σ
    ratio_sig = ia["sigma"] / rn["shuffle_sigma"]
    dev = np.abs(ratio_sig - 1)
    C.append(check("S1", np.median(dev) <= 0.03 and np.quantile(dev, 0.99) <= 0.08,
                   {"median": float(np.median(dev)), "p99": float(np.quantile(dev, 0.99)), "max": float(dev.max()),
                    "argmax_t": float(t_ref[int(dev.argmax())])}, "mediana ≤ 0,03; p99 ≤ 0,08"))
    # ---------------- S2/S3/S4 limiares
    ks = ks_2samp(rn["shuffle_null_max"], ia["null_max"])
    C.append(check("S2", ks.pvalue >= 0.001, {"ks_stat": float(ks.statistic), "p": float(ks.pvalue)}, "KS p ≥ 0,001"))
    riv = bm["null_summary"]["shuffle"]["threshold_interval"]
    iiv = ind["shuffle_interval"]
    C.append(check("S3", max(riv["z_low"], iiv["z_low"]) <= min(riv["z_high"], iiv["z_high"]),
                   {"ref": [riv["z_low"], riv["point_threshold"], riv["z_high"]], "ind": [iiv["z_low"], iiv["point"], iiv["z_high"]]}, "ICs se sobrepõem"))
    Bs = len(ia["score_max"])
    lo, hi = binom.ppf(0.0005, Bs, 0.05) / Bs, binom.ppf(0.9995, Bs, 0.05) / Bs
    C.append(check("S4", lo <= ind["score_fraction_above"] <= hi, {"ind": ind["score_fraction_above"], "band": [lo, hi],
                   "ref": bm["null_summary"]["shuffle"]["score_set_fraction_max_above_threshold"]}, "faixa binomial 99,9%"))

    # ---------------- S5/S6/S7 decisões por linha
    inc_by_line = {}
    for x in rinc:
        inc_by_line[(int(x["nearest_prime"]), int(x["nearest_repetition"]))] = float(x["z"])
    sig_ref = rn["shuffle_sigma"]
    gi = np.clip(np.round((T - t_ref[0]) / (t_ref[1] - t_ref[0])).astype(int), 0, len(t_ref) - 1)
    z_grid_ref = np.abs(F_ref[gi]) / sig_ref[gi]
    hi_max = max(riv["z_high"], iiv["z_high"])
    lo_min = min(riv["z_low"], iiv["z_low"])
    per_line = []
    mismatches_clear, unclear = [], []
    zr_det = []
    for k, (r, l) in enumerate(zip(rrows, ind_lines)):
        key = (int(r["prime"]), int(r["repetition"]))
        st_ref = "detected" if r["detected"] == "True" else ("inconclusive" if r.get("inconclusive_candidate_within_tolerance") == "True" else "not_detected")
        st_ind = "detected" if l["detected"] else ("inconclusive" if l["inconclusive_near"] else "not_detected")
        z_ref = float(r["z_primary"]) if r["z_primary"] else inc_by_line.get(key, float(z_grid_ref[k]))
        z_ind = l["z_peak"] if l["z_peak"] is not None else (l["z_inconclusive"] if l["z_inconclusive"] is not None else l["z_grid_nearest_T"])
        clear_above = min(z_ref, z_ind) > 1.05 * hi_max
        clear_below = max(z_ref, z_ind) < lo_min / 1.05
        decided = clear_above or clear_below
        name = f"{key[0]}^{key[1]}" if key[1] > 1 else str(key[0])
        row = {"line": name, "T": T[k], "status_ref": st_ref, "status_ind": st_ind, "z_ref": z_ref, "z_ind": z_ind,
               "z_pred_ref": float(r["z_predicted"]), "z_pred_ind": l["z_pred"], "clearly_decided": decided}
        per_line.append(row)
        if decided and st_ref != st_ind:
            mismatches_clear.append(row)
        if not decided:
            unclear.append(row)
        if st_ref == "detected" and st_ind == "detected":
            zr_det.append(abs(z_ind / z_ref - 1))
    C.append(check("S5", len(mismatches_clear) == 0, {"mismatches_clearly_decided": mismatches_clear, "not_clearly_decided": [u["line"] for u in unclear]},
                   "linhas claramente decididas com mesmo status"))
    zr_det = np.array(zr_det)
    C.append(check("S6", len(zr_det) and np.mean(zr_det <= 0.05) >= 0.95, {"fraction_within_5pct": float(np.mean(zr_det <= 0.05)), "max": float(zr_det.max()),
                   "median": float(np.median(zr_det))}, "|z_ind/z_ref − 1| ≤ 0,05 em ≥ 95% das detectadas em ambas"))
    S_ref = bm["arithmetic"]["matched_S"]
    C.append(check("S7", abs(ind["S"] - S_ref) <= len(unclear) and ind["unmatched"] == 0 and bm["arithmetic"]["unmatched_detections"] == 0,
                   {"S": [ind["S"], S_ref], "S_optimal_ind": ind["S_optimal"], "unmatched": [ind["unmatched"], bm["arithmetic"]["unmatched_detections"]],
                    "not_clearly_decided": len(unclear)}, "|ΔS| ≤ nº não claramente decididas; sem correspondência = 0"))
    C.append(check("S8", ind["p_S"] <= 0.01, {"ind": ind["p_S"], "ref": bm["arithmetic"]["p_value_global_mc"]}, "p_ind ≤ 0,01"))
    rsc = bm["synthetic_calibration"]
    rs_i, rs_r = SEPS.index(ind["resolution_sep_fwhm"]), SEPS.index(rsc["resolution_separation_fwhm"])
    C.append(check("S9", 0.5 <= ind["tolerance"] / rsc["matching_tolerance"] <= 2.0 and abs(rs_i - rs_r) <= 1,
                   {"tolerance_ratio": ind["tolerance"] / rsc["matching_tolerance"], "res_sep": [ind["resolution_sep_fwhm"], rsc["resolution_separation_fwhm"]]},
                   "razão ∈ [0,5; 2]; separação igual/adjacente"))
    ar = bm["arithmetic"]
    ref_c1 = fam["C1b_recovery_ok"]
    ref_c2 = (ar["coefficient_agreement"]["fraction_within_tolerance"] or 0) >= 0.95 and ar["phase_coherence"]["Q_observed"] >= 0.9
    C.append(check("S10", ref_c1 == ind["C1_block"] and ref_c2 == ind["C2_block"],
                   {"C1_recovery": [ind["C1_block"], ref_c1], "C2": [ind["C2_block"], ref_c2], "clear": [ind["clear"], ar["clearly_detectable"]],
                    "eligible": [ind["eligible"], ar["coefficient_agreement"]["n_eligible"]], "recovery_clear": [ind["recovery_clear"], ar["recovery_among_clearly_detectable"]],
                    "C2_fraction": [ind["C2_fraction"], ar["coefficient_agreement"]["fraction_within_tolerance"]]}, "vereditos por bloco iguais"))
    elig_ref = [(r["prime"], r["repetition"]) for r in rrows if r["resolved"] == "True" and r["clearly_detectable"] == "True"]
    elig_ind = [(str(l["p"]), str(l["r"])) for l in ind_lines if l["resolved"] and l["clear"]]
    same_elig = elig_ref == elig_ind
    C.append(check("D6", (not same_elig) or (abs(ind["R"] - ar["phase_coherence"]["R_observed"]) <= 1e-9 and abs(ind["Q"] - ar["phase_coherence"]["Q_observed"]) <= 1e-9),
                   {"same_eligible_set": same_elig, "R": [ind["R"], ar["phase_coherence"]["R_observed"]], "Q": [ind["Q"], ar["phase_coherence"]["Q_observed"]],
                    "eligible_only_ref": sorted(set(elig_ref) - set(elig_ind)), "eligible_only_ind": sorted(set(elig_ind) - set(elig_ref))},
                   "|ΔR|, |ΔQ| ≤ 1e-9 se o conjunto elegível for igual"))
    C.append(check("S11", ind["p_Q"] <= 0.01 and ar["phase_coherence"]["p_value_Q"] <= 0.01, {"ind": ind["p_Q"], "ref": ar["phase_coherence"]["p_value_Q"]}, "ambos ≤ 0,01"))

    # ---------------- D7 M2 determinístico
    rc = csv_rows(Path(m2run, "tables", f"m2_{b}_spacing_cdf.csv"))
    rr2 = csv_rows(Path(m2run, "tables", f"m2_{b}_pair_correlation.csv"))
    rk = csv_rows(Path(m2run, "tables", f"m2_{b}_form_factor.csv"))
    cdf_ref = np.array([float(x["cdf_zeros"]) for x in rc])
    r2_ref = np.array([float(x["r2_zeros"]) for x in rr2])
    k_ref = np.array([float(x["k_connected_zeros"]) for x in rk])
    var_rel = abs(ind["m2"]["spacing_variance"] / rm2["spacing_variance"] - 1)
    dcdf = float(np.max(np.abs(im2["cdf"] - cdf_ref)))
    dr2 = float(np.max(np.abs(im2["r2"] / r2_ref - 1)))
    dk = np.abs(im2["k"] - k_ref)
    okk = bool(np.all(dk <= 1e-8 + 1e-8 * np.abs(k_ref)))
    C.append(check("D7", var_rel <= 1e-10 and dcdf <= 1e-10 and dr2 <= 1e-10 and okk,
                   {"var_rel": var_rel, "cdf_max_abs": dcdf, "r2_max_rel": dr2, "k_max_abs": float(dk.max()), "k_max_rel": float(np.max(dk / np.abs(k_ref)))},
                   "Var, CDF, R₂ rel ≤ 1e-10; K_c abs ≤ 1e-8 + rel 1e-8"))
    # ---------------- S12 M2 p-valores
    s12 = {}
    ok12 = True
    for ref_name in ("gue", "poisson"):
        for st in ("cdf", "r2", "k_connected"):
            pr = rm2["envelope_tests"][ref_name][st]["p_value_mc"]
            pi = ind["m2"][f"p_{ref_name}_{st}"]
            if pr <= 0.001 + 1e-12:
                ok = pi <= 2 / 300
            else:
                ok = abs(pi - pr) <= 3 * math.sqrt(pr * (1 - pr) / 300) + 0.01
            s12[f"{ref_name}_{st}"] = {"ind": pi, "ref": pr, "pass": ok}
            ok12 &= ok
    C.append(check("S12", ok12, s12, "piso: p_ind ≤ 2/300; senão |Δp| ≤ 3·EP + 0,01"))
    # ---------------- D8 / S13 CUE
    sg = np.linspace(0, 4, 161)
    corr_ref = ref_cue.first_correction(sg)
    pred_ref = ref_cue.zeros_prediction(corr_ref, float(np.median(g)))
    dP0 = float(np.max(np.abs(im2["cue_P0"] - corr_ref["P0"])))
    dP1 = float(np.max(np.abs(im2["cue_P1"] - corr_ref["P1"])))
    dpred = float(np.max(np.abs(im2["cue_pred_cdf"] - pred_ref["cdf"])))
    rc_ = rm2["cue_secondary"]
    ddl = abs(ind["cue"]["rms_limit"] - rc_["rms_cdf_distance_to_limit"])
    ddc = abs(ind["cue"]["rms_corrected"] - rc_["rms_cdf_distance_to_cue_corrected"])
    C.append(check("D8", dP0 <= 1e-7 and dP1 <= 1e-4 and dpred <= 1e-6 and ddl <= 1e-6 and ddc <= 1e-6,
                   {"P0_max_abs": dP0, "P1_max_abs": dP1, "pred_cdf_max_abs": dpred, "rms_limit_diff": ddl, "rms_corrected_diff": ddc,
                    "argmax_pred_s": float(sg[int(np.argmax(np.abs(im2["cue_pred_cdf"] - pred_ref["cdf"])))]),
                    "var_corrected": [ind["cue"]["var_corrected"], rc_["spacing_variance_cue_corrected"]]},
                   "P₀ ≤ 1e-7; P₁ ≤ 1e-4; CDF ≤ 1e-6; distâncias ≤ 1e-6"))
    nr = ind["cue"]["noise"] / rc_["sampling_noise_rms_gue_ensemble"]
    C.append(check("S13", 0.75 <= nr <= 1.33, {"ratio": nr}, "razão ∈ [0,75; 1,33]"))

    report["blocks"][label] = {"checks": C, "lines": per_line,
                               "summary": {"n_detected": [ind["n_detected"], bm["freeze"]["n_detected_primary"]],
                                           "n_inconclusive": [ind["n_inconclusive"], bm["freeze"]["n_inconclusive_primary"]],
                                           "gue_detected": [ind["n_detected_gue"], bm["freeze"]["n_detected_secondary"]]}}

(OUT / "comparison.json").write_text(json.dumps(report, indent=1, default=float))
for label, blk in report["blocks"].items():
    print(f"== {label}: {sum(c['pass'] for c in blk['checks'])}/{len(blk['checks'])} verificações dentro da tolerância; detecções ind/ref {blk['summary']}")
    for c in blk["checks"]:
        if not c["pass"]:
            print("   FORA:", c["code"], c["rule"], json.dumps(c["value"], default=float)[:600])
