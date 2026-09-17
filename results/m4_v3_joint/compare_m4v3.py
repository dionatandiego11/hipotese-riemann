"""
Comparação primária (src, m4-v3) × reprodução independente nos blocos d01–d10, conforme independent/M4V3_PLAN.md.
Avalia D1–D9 e S1–S13 por bloco, vereditos de família e as regras de interrupção R1–R4.
"""
import csv, hashlib, json, math, sys
from pathlib import Path

import numpy as np
from scipy.stats import binom, ks_2samp

sys.path.insert(0, "src"); sys.path.insert(0, "independent")
from riemann_spectra.periods import OscillatoryTransform  # primária
from riemann_spectra import cue as ref_cue
from riemann_spectra.cli import load_zeros_csv
from riemann_indep import core as icore, stats as istats  # reprodução

import os

DRY = os.environ.get("M4V3_COMPARE_DRYRUN")  # teste do script em dados já analisados (m4-v2), antes do congelamento
PFX, VERSION, M2PROFILE, ZFILE = ("d", "m4-v3", "m4_v3_m2", "data/processed/zeros_100k.csv")
IND, OUT = Path("results/m4_v3_independent"), Path("results/m4_v3_joint")
if DRY:
    PFX, VERSION, M2PROFILE, ZFILE = ("c", "m4-v2", "m4_v2_m2", "data/processed/zeros_70k.csv")
    IND, OUT = Path(DRY), Path(DRY)
else:
    lock = json.loads(Path("independent/M4V3_PLAN.lock.json").read_text())
    for f, h in lock["files"].items():
        assert hashlib.sha256(Path(f).read_bytes()).hexdigest() == h, f"alterado após congelamento: {f}"

RES = Path("results")
cands = sorted(RES.glob("run_*_m3_" + "-".join(f"{PFX}{i:02d}" for i in range(1, 11))))
prim = [c for c in cands if f'protocol_version = "{VERSION}"' in (c / "config_resolved.toml").read_text()]
assert len(prim) == 1, cands
RUN = prim[0]
m2runs = sorted(RES.glob(f"run_*_m2_{M2PROFILE}"))
assert len(m2runs) == 1
M2RUN = m2runs[0]
SEPS = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0]
zeros = load_zeros_csv(Path(ZFILE))
prim_m2 = json.loads((M2RUN / "metrics.json").read_text())
prim_family = json.loads((RUN / "family_summary.json").read_text())
sg = np.linspace(0, 4, 161)
corr_ref = ref_cue.first_correction(sg)


def chk(code, ok, value, rule):
    return {"code": code, "pass": bool(ok), "value": value, "rule": rule}


report = {"primary_run": str(RUN), "primary_m2_run": str(M2RUN), "blocks": {}}
ind_fam = {"p_S": [], "p_Q": [], "rec": [], "unm": [], "frac": [], "Q": [], "C3": {}}
for i in range(1, 11):
    b = f"{PFX}{i:02d}"
    bm = json.loads((RUN / "tables" / b / "block_metrics.json").read_text())
    rn = np.load(RUN / "tables" / b / "nulls.npz")
    rrows = list(csv.DictReader(open(RUN / "tables" / b / "arithmetic_matches.csv")))
    rinc = list(csv.DictReader(open(RUN / "tables" / b / "inconclusive_candidates.csv")))
    rm2 = prim_m2["blocks"][b]
    ind = json.loads((IND / b / "summary.json").read_text())
    il = json.loads((IND / b / "lines.json").read_text())
    ia = np.load(IND / b / "arrays.npz")
    im2 = np.load(IND / b / "m2_arrays.npz")
    g = zeros[bm["block"]["first_index"] - 1:bm["block"]["last_index"]]
    inst = bm["instrument"]
    C = []
    # D1 malhas próprias
    C.append(chk("D1", ind["n_t"] == inst["n_t"] and abs(ind["dt"] / inst["dt"] - 1) <= 1e-10 and abs(ind["fwhm"] / inst["response"]["fwhm"] - 1) <= 1e-10
                 and abs(ind["W0"] / inst["response"]["gain_W0"] - 1) <= 1e-10,
                 {"n_t": [ind["n_t"], inst["n_t"]], "dt_rel": ind["dt"] / inst["dt"] - 1, "fwhm_rel": ind["fwhm"] / inst["response"]["fwhm"] - 1}, "D1"))
    # D2/D3 nas mesmas coordenadas (malha da primária)
    t_ref = rn["t_grid"]
    tr = OscillatoryTransform(g[0], g[-1], 0.5, 5.0, points_per_fwhm=8.0)
    sm_ind = icore.smooth_term(t_ref, g[0], g[-1])
    F_ind_ref_grid = icore.discrete_sum(g, t_ref, g[0], g[-1]) - sm_ind
    F_ref = rn["F_real"] + 1j * rn["F_imag"]
    dS = np.abs(sm_ind - tr.smooth)
    dF = np.abs(F_ind_ref_grid - F_ref)
    C.append(chk("D2", dS.max() <= 1e-8, {"max_abs": float(dS.max())}, "mesmas coordenadas, ≤ 1e-8"))
    C.append(chk("D3", dF.max() <= 1e-7 and np.median(dF) <= 1e-8, {"max_abs": float(dF.max()), "median_abs": float(np.median(dF))}, "mesmas coordenadas"))
    T = np.array([float(r["period_theoretical"]) for r in rrows])
    FT = tr.evaluate(g, T)
    FTi = np.array([complex(*l["F_at_T"]) for l in il])
    C.append(chk("D4", np.max(np.abs(FT - FTi)) <= 1e-8, {"max_abs": float(np.max(np.abs(FT - FTi)))}, "≤ 1e-8"))
    Ti = np.array([l["T"] for l in il])
    C.append(chk("D9", len(Ti) == len(T) and np.max(np.abs(Ti - T)) <= 1e-14, {"n": [len(Ti), len(T)]}, "catálogo"))
    d5 = {}
    for vi, vr in (("ratio_band_conjugate", "fit_ratio_to_theory"), ("ratio_band_no_conjugate", "ratio_to_theory__band_no_conjugate"),
                   ("ratio_centers_conjugate", "ratio_to_theory__centers_conjugate")):
        d = np.array([abs(l[vi] - float(r[vr])) for l, r in zip(il, rrows)])
        d5[vi] = float(d.max())
    C.append(chk("D5", max(d5.values()) <= 1e-9, d5, "≤ 1e-9"))
    # S1–S4
    dev = np.abs(ia["sigma"] / rn["shuffle_sigma"] - 1) if len(ia["sigma"]) == len(rn["shuffle_sigma"]) else np.array([np.inf])
    C.append(chk("S1", np.median(dev) <= 0.03 and np.quantile(dev, 0.99) <= 0.08, {"median": float(np.median(dev)), "p99": float(np.quantile(dev, 0.99))}, "S1"))
    ks = ks_2samp(rn["shuffle_null_max"], ia["null_max"])
    C.append(chk("S2", ks.pvalue >= 0.001, {"p": float(ks.pvalue)}, "S2"))
    riv, iiv = bm["null_summary"]["shuffle"]["threshold_interval"], ind["shuffle_interval"]
    C.append(chk("S3", max(riv["z_low"], iiv["z_low"]) <= min(riv["z_high"], iiv["z_high"]), {"ref": [riv["z_low"], riv["z_high"]], "ind": [iiv["z_low"], iiv["z_high"]]}, "S3"))
    Bs = len(ia["score_max"])
    lo, hi = binom.ppf(0.0005, Bs, 0.05) / Bs, binom.ppf(0.9995, Bs, 0.05) / Bs
    C.append(chk("S4", lo <= ind["score_fraction_above"] <= hi, {"ind": ind["score_fraction_above"], "band": [lo, hi]}, "S4"))
    # S5–S7
    inc_ref = {(int(x["nearest_prime"]), int(x["nearest_repetition"])): float(x["z"]) for x in rinc}
    gi = np.clip(np.round((T - t_ref[0]) / (t_ref[1] - t_ref[0])).astype(int), 0, len(t_ref) - 1)
    zgr = np.abs(F_ref[gi]) / rn["shuffle_sigma"][gi]
    hi_max, lo_min = max(riv["z_high"], iiv["z_high"]), min(riv["z_low"], iiv["z_low"])
    lines, mism, unclear, zr = [], [], [], []
    for k, (r, l) in enumerate(zip(rrows, il)):
        key = (int(r["prime"]), int(r["repetition"]))
        sr = "detected" if r["detected"] == "True" else ("inconclusive" if r["inconclusive_candidate_within_tolerance"] == "True" else "not_detected")
        si = "detected" if l["detected"] else ("inconclusive" if l["inconclusive_near"] else "not_detected")
        z_r = float(r["z_primary"]) if r["z_primary"] else inc_ref.get(key, float(zgr[k]))
        z_i = l["z_peak"] if l["z_peak"] is not None else (l["z_inconclusive"] if l["z_inconclusive"] is not None else l["z_grid_nearest_T"])
        decided = min(z_r, z_i) > 1.05 * hi_max or max(z_r, z_i) < lo_min / 1.05
        name = f"{key[0]}^{key[1]}" if key[1] > 1 else str(key[0])
        row = {"line": name, "status_ref": sr, "status_ind": si, "z_ref": z_r, "z_ind": z_i, "decided": decided,
               "z_pred_ref": float(r["z_predicted"]), "z_pred_ind": l["z_pred"], "clear_ref": r["clearly_detectable"] == "True", "clear_ind": l["clear"],
               "resolved_ref": r["resolved"] == "True", "resolved_ind": l["resolved"]}
        lines.append(row)
        if decided and sr != si:
            mism.append(row)
        if not decided:
            unclear.append(name)
        if sr == "detected" and si == "detected":
            zr.append(abs(z_i / z_r - 1))
    zr = np.array(zr)
    C.append(chk("S5", not mism, {"mismatches": mism, "not_clearly_decided": unclear}, "S5"))
    C.append(chk("S6", len(zr) > 0 and np.mean(zr <= 0.05) >= 0.95, {"fraction": float(np.mean(zr <= 0.05)) if len(zr) else None}, "S6"))
    ar = bm["arithmetic"]
    C.append(chk("S7", abs(ind["S"] - ar["matched_S"]) <= len(unclear) and ind["unmatched"] == 0 and ar["unmatched_detections"] == 0,
                 {"S": [ind["S"], ar["matched_S"]], "unmatched": [ind["unmatched"], ar["unmatched_detections"]], "unclear": len(unclear)}, "S7"))
    C.append(chk("S8", ind["p_S"] <= 0.01 if ar["p_value_global_mc"] <= 1.5e-4 else True, {"ind": ind["p_S"], "ref": ar["p_value_global_mc"]}, "S8"))
    rsc = bm["synthetic_calibration"]
    C.append(chk("S9", 0.5 <= ind["tolerance"] / rsc["matching_tolerance"] <= 2 and abs(SEPS.index(ind["resolution_sep_fwhm"]) - SEPS.index(rsc["resolution_separation_fwhm"])) <= 1,
                 {"ratio": ind["tolerance"] / rsc["matching_tolerance"], "sep": [ind["resolution_sep_fwhm"], rsc["resolution_separation_fwhm"]]}, "S9"))
    fb = prim_family["blocks"][b]
    ref_c2 = (ar["coefficient_agreement"]["fraction_within_tolerance"] or 0) >= 0.95 and ar["phase_coherence"]["Q_observed"] >= 0.9
    C.append(chk("S10", fb["C1b_recovery_ok"] == ind["C1_block"] and ref_c2 == ind["C2_block"],
                 {"C1b": [ind["C1_block"], fb["C1b_recovery_ok"]], "C2": [ind["C2_block"], ref_c2], "clear": [ind["clear"], ar["clearly_detectable"]],
                  "eligible": [ind["eligible"], ar["coefficient_agreement"]["n_eligible"]]}, "S10"))
    same_el = [(l["line"]) for l in lines if l["clear_ref"] and l["resolved_ref"]] == [(l["line"]) for l in lines if l["clear_ind"] and l["resolved_ind"]]
    C.append(chk("D6", (not same_el) or (abs(ind["R"] - ar["phase_coherence"]["R_observed"]) <= 1e-9 and abs(ind["Q"] - ar["phase_coherence"]["Q_observed"]) <= 1e-9),
                 {"same_eligible": same_el, "Q": [ind["Q"], ar["phase_coherence"]["Q_observed"]]}, "D6"))
    C.append(chk("S11", ind["p_Q"] <= 0.01 and ar["phase_coherence"]["p_value_Q"] <= 0.01, {"ind": ind["p_Q"], "ref": ar["phase_coherence"]["p_value_Q"]}, "S11"))
    rc = list(csv.DictReader(open(M2RUN / "tables" / f"m2_{b}_spacing_cdf.csv")))
    rr2 = list(csv.DictReader(open(M2RUN / "tables" / f"m2_{b}_pair_correlation.csv")))
    rk = list(csv.DictReader(open(M2RUN / "tables" / f"m2_{b}_form_factor.csv")))
    cdf_r = np.array([float(x["cdf_zeros"]) for x in rc]); r2_r = np.array([float(x["r2_zeros"]) for x in rr2]); k_r = np.array([float(x["k_connected_zeros"]) for x in rk])
    dk = np.abs(im2["k"] - k_r)
    ok7 = abs(ind["m2"]["spacing_variance"] / rm2["spacing_variance"] - 1) <= 1e-10 and np.max(np.abs(im2["cdf"] - cdf_r)) <= 1e-10 \
        and np.all(np.abs(im2["r2"] - r2_r) <= 1e-10 * np.maximum(1.0, np.abs(r2_r))) and np.all(dk <= 1e-8 + 1e-8 * np.abs(k_r))
    # (R₂ comparado em escala absoluta/relativa sem divisão: bins com R₂ = 0 geravam 0/0 no ensaio prévio)
    C.append(chk("D7", ok7, {"k_max_abs": float(dk.max())}, "D7"))
    s12, ok12 = {}, True
    for refn in ("gue", "poisson"):
        for st in ("cdf", "r2", "k_connected"):
            pr, pi = rm2["envelope_tests"][refn][st]["p_value_mc"], ind["m2"][f"p_{refn}_{st}"]
            ok = pi <= 2 / 300 if pr <= 0.001 + 1e-12 else abs(pi - pr) <= 3 * math.sqrt(pr * (1 - pr) / 300) + 0.01
            s12[f"{refn}_{st}"] = [pi, pr, ok]
            ok12 &= ok
            ind_fam["C3"].setdefault(f"{refn}_{st}", []).append(pi)
    C.append(chk("S12", ok12, s12, "S12"))
    pred_r = ref_cue.zeros_prediction(corr_ref, float(np.median(g)))
    rcs = rm2["cue_secondary"]
    d8 = {"P0": float(np.max(np.abs(im2["cue_P0"] - corr_ref["P0"]))), "P1": float(np.max(np.abs(im2["cue_P1"] - corr_ref["P1"]))),
          "pred_cdf": float(np.max(np.abs(im2["cue_pred_cdf"] - pred_r["cdf"]))),
          "rms_limit": abs(ind["cue"]["rms_limit"] - rcs["rms_cdf_distance_to_limit"]), "rms_corr": abs(ind["cue"]["rms_corrected"] - rcs["rms_cdf_distance_to_cue_corrected"])}
    C.append(chk("D8", d8["P0"] <= 1e-7 and d8["P1"] <= 1e-4 and d8["pred_cdf"] <= 1e-6 and d8["rms_limit"] <= 1e-6 and d8["rms_corr"] <= 1e-6, d8, "D8"))
    C.append(chk("S13", 0.75 <= ind["cue"]["noise"] / rcs["sampling_noise_rms_gue_ensemble"] <= 1.33, {"ratio": ind["cue"]["noise"] / rcs["sampling_noise_rms_gue_ensemble"]}, "S13"))
    report["blocks"][b] = {"checks": C, "lines": lines, "counts": {"detected": [ind["n_detected"], bm["freeze"]["n_detected_primary"]],
                                                                 "inconclusive": [ind["n_inconclusive"], bm["freeze"]["n_inconclusive_primary"]]}}
    ind_fam["p_S"].append(ind["p_S"]); ind_fam["p_Q"].append(ind["p_Q"]); ind_fam["rec"].append(ind["recovery_clear"])
    ind_fam["unm"].append(ind["unmatched"]); ind_fam["frac"].append(ind["C2_fraction"]); ind_fam["Q"].append(ind["Q"])

# ---- família independente
names = [f"{PFX}{i:02d}" for i in range(1, 11)]
hS, hQ = istats.holm(ind_fam["p_S"]), istats.holm(ind_fam["p_Q"])
ind_blocks = {b: {"C1": bool(hS[k] <= 0.05 and (ind_fam["rec"][k] or 0) >= 0.95), "C2": bool((ind_fam["frac"][k] or 0) >= 0.95 and ind_fam["Q"][k] >= 0.9 and hQ[k] <= 0.05),
                  "p_S_holm": float(hS[k]), "p_Q_holm": float(hQ[k])} for k, b in enumerate(names)}
ind_c1_rep = all(v["C1"] for v in ind_blocks.values()) and sum(u > 0 for u in ind_fam["unm"]) <= 2
ind_c2_rep = all(v["C2"] for v in ind_blocks.values())
ind_c3 = {k: istats.holm(v) for k, v in ind_fam["C3"].items()}
prim_c3 = prim_m2["family_holm"]
family = {"primary": {"C1_replicated": prim_family["C1_replicated_all_blocks"], "C2_replicated": prim_family["C2_replicated_all_blocks"],
                      "C1_blocks": prim_family["C1_blocks_passing"], "C2_blocks": prim_family["C2_blocks_passing"],
                      "blocks_with_unmatched": prim_family["C1_blocks_with_unmatched_detection"],
                      "C3_rejections": {k: v["n_rejected"] for k, v in prim_c3.items()}},
          "independent": {"C1_replicated": ind_c1_rep, "C2_replicated": ind_c2_rep, "C1_blocks": sum(v["C1"] for v in ind_blocks.values()),
                          "C2_blocks": sum(v["C2"] for v in ind_blocks.values()), "blocks_with_unmatched": sum(u > 0 for u in ind_fam["unm"]),
                          "C3_rejections": {k: int(sum(p <= 0.05 for p in v)) for k, v in ind_c3.items()}, "blocks": ind_blocks}}

# ---- regras de interrupção
stops = {}
d_fail = [(b, c["code"]) for b, blk in report["blocks"].items() for c in blk["checks"] if c["code"].startswith("D") and not c["pass"]]
stops["R1"] = {"triggered": bool(d_fail), "failures": d_fail}
s_fail = [(b, c["code"]) for b, blk in report["blocks"].items() for c in blk["checks"] if c["code"].startswith("S") and not c["pass"]]
from collections import Counter
cnt = Counter(code for _, code in s_fail)
stops["R2"] = {"triggered": any(v >= 3 for v in cnt.values()), "isolated_failures": s_fail, "count_by_code": dict(cnt)}
r3_unexplained = []
for crit in ("C1", "C2"):
    for b in names:
        pb = prim_family["blocks"][b][f"{crit}_block_pass"]
        ib = ind_blocks[b][crit]
        if pb == ib:
            continue
        blk = report["blocks"][b]
        s5 = [c for c in blk["checks"] if c["code"] == "S5"][0]
        margin_lines = [l for l in blk["lines"] if (l["clear_ref"] != l["clear_ind"] or l["resolved_ref"] != l["resolved_ind"]) and
                        not (abs(l["z_pred_ref"] / (1.5 * report["blocks"][b]["checks"][[c["code"] for c in blk["checks"]].index("S3")]["value"]["ref"][1]) - 1) <= 0.05
                             or abs(l["z_pred_ind"] / (1.5 * report["blocks"][b]["checks"][[c["code"] for c in blk["checks"]].index("S3")]["value"]["ind"][1]) - 1) <= 0.05)]
        p_key = "p_S_holm" if crit == "C1" else "p_Q_holm"
        p_prim = prim_family["blocks"][b]["C1_p_S_holm" if crit == "C1" else "C2_p_Q_holm"]
        explained = s5["pass"] and not margin_lines and max(p_prim, ind_blocks[b][p_key]) <= 0.10
        if not explained:
            r3_unexplained.append({"criterion": crit, "block": b, "primary": pb, "independent": ib, "margin_lines_outside_5pct": [l["line"] for l in margin_lines]})
stops["R3"] = {"triggered": (family["primary"]["C1_replicated"] != family["independent"]["C1_replicated"] or
                             family["primary"]["C2_replicated"] != family["independent"]["C2_replicated"]) and bool(r3_unexplained),
               "family_verdicts_differ": [family["primary"]["C1_replicated"] != family["independent"]["C1_replicated"],
                                          family["primary"]["C2_replicated"] != family["independent"]["C2_replicated"]],
               "unexplained_block_differences": r3_unexplained}
r4 = {}
for k, v in ind_c3.items():
    pp = [prim_c3[k][b]["p_holm"] for b in names]
    band = sum((0.01 <= a <= 0.20) or (0.01 <= c <= 0.20) for a, c in zip(pp, v))
    diff = abs(family["primary"]["C3_rejections"][k] - family["independent"]["C3_rejections"][k])
    r4[k] = {"diff": int(diff), "blocks_in_band": int(band), "ok": bool(diff <= band)}
stops["R4"] = {"triggered": not all(x["ok"] for x in r4.values()), "by_pair": r4}
stops["joint_conclusion_suspended"] = any(stops[r]["triggered"] for r in ("R1", "R2", "R3", "R4"))
report["family"] = family
report["stop_rules"] = stops
(OUT / ("comparison_dryrun.json" if DRY else "comparison_m4v3.json")).write_text(json.dumps(report, indent=1, default=float))
for b, blk in report["blocks"].items():
    fails = [c["code"] for c in blk["checks"] if not c["pass"]]
    print(b, f"{sum(c['pass'] for c in blk['checks'])}/{len(blk['checks'])}", "fora:", fails, "detecções ind/prim", blk["counts"],
          "não decididas:", [c for c in blk["checks"] if c["code"] == "S5"][0]["value"]["not_clearly_decided"])
print(json.dumps(family, indent=1, default=float)[:1500])
print(json.dumps({k: (v["triggered"] if isinstance(v, dict) else v) for k, v in stops.items()}, indent=1))
