"""
Comparação descritiva m4-v1 (zeros 10.001–40.000) × m4-v2 (40.001–70.000), itens fixados em PROTOCOLO §10.3.
Somente leitura. Não há teste estatístico entre faixas (alturas diferentes; blocos contíguos não independentes).
"""
import csv, json
from collections import Counter
from pathlib import Path

import numpy as np

RES = Path("results")


def find(pattern):
    runs = sorted(RES.glob(pattern))
    if len(runs) != 1:
        raise SystemExit(f"esperada exatamente 1 execução para {pattern}, encontradas {[r.name for r in runs]}")
    return runs[0]


RUNS = {
    "m4-v1": {"m2": find("run_*_m2_m4_v1_m2"), "prefix": "b"},
    "m4-v2": {"m2": find("run_*_m2_m4_v2_m2"), "prefix": "c"},
}
# BH: há duas execuções com o mesmo padrão por versão; distinguir pelo protocol_version da configuração resolvida
for v in RUNS:
    p = RUNS[v]["prefix"]
    cands = sorted(RES.glob(f"run_*_m3_{p}01-{p}02-{p}03-{p}04-{p}05-{p}06-{p}07-{p}08-{p}09-{p}10"))
    bh = [c for c in cands if "blackman" in (c / "config_resolved.toml").read_text()]
    prim = [c for c in cands if "blackman" not in (c / "config_resolved.toml").read_text()]
    assert len(bh) == 1 and len(prim) == 1, (v, cands)
    RUNS[v]["bh"], RUNS[v]["primary"] = bh[0], prim[0]
    RUNS[v].pop("prefix")


def rows(run, b):
    return list(csv.DictReader(open(run / "tables" / b / "arithmetic_matches.csv")))


out = {"runs": {v: {k: str(x) for k, x in d.items()} for v, d in RUNS.items()}, "versions": {}}
for v, d in RUNS.items():
    fam = json.load(open(d["primary"] / "family_summary.json"))
    famb = json.load(open(d["bh"] / "family_summary.json"))
    m2 = json.load(open(d["m2"] / "metrics.json"))
    blocks = list(fam["blocks"])
    per = {}
    det_counter = Counter()
    det_sets = {}
    for b in blocks:
        bm = json.load(open(d["primary"] / "tables" / b / "block_metrics.json"))
        ar = bm["arithmetic"]
        rr = rows(d["primary"], b)
        det = {(int(r["prime"]), int(r["repetition"])) for r in rr if r["detected"] == "True"}
        det_sets[b] = det
        det_counter.update(det)
        inc = [(int(x["nearest_prime"]), int(x["nearest_repetition"]), float(x["z"])) for x in csv.DictReader(open(d["primary"] / "tables" / b / "inconclusive_candidates.csv"))]
        rb = {(int(r["prime"]), int(r["repetition"])): float(r["fit_ratio_to_theory"]) for r in rows(d["bh"], b)}
        rh = {(int(r["prime"]), int(r["repetition"])): r for r in rr}
        elig = [k for k, r in rh.items() if r["resolved"] == "True" and r["clearly_detectable"] == "True"]
        bh_det = {(int(r["prime"]), int(r["repetition"])) for r in rows(d["bh"], b) if r["detected"] == "True"}
        mb = m2["blocks"][b]
        cue = mb["cue_secondary"]
        per[b] = {
            "indices": [bm["block"]["first_index"], bm["block"]["last_index"]],
            "E_range": [bm["instrument"]["A"], bm["instrument"]["B"]],
            "L": bm["instrument"]["L"],
            "detected": len(det), "inconclusive": ar["inconclusive_candidates"], "inconclusive_lines": inc,
            "unmatched": ar["unmatched_detections"], "p_S": ar["p_value_global_mc"],
            "threshold_interval": [ar["threshold_interval"]["z_low"], ar["threshold_interval"]["z_high"]],
            "score_set_fraction_above": bm["null_summary"]["shuffle"]["score_set_fraction_max_above_threshold"],
            "clearly_detectable": ar["clearly_detectable"], "recovery_clear": ar["recovery_among_clearly_detectable"],
            "C2_eligible": ar["coefficient_agreement"]["n_eligible"],
            "C2_fraction": ar["coefficient_agreement"]["fraction_within_tolerance"],
            "C2_max": ar["coefficient_agreement"]["max_abs_ratio_minus_1"],
            "C2_median": ar["coefficient_agreement"]["median_abs_ratio_minus_1"],
            "all47_max_abs_ratio_minus_1": ar["targeted_fit"]["variants"]["band_conjugate"]["all_catalog_lines"]["max_abs_ratio_minus_1"],
            "Q": ar["phase_coherence"]["Q_observed"], "p_Q": ar["phase_coherence"]["p_value_Q"],
            "C1_pass": fam["blocks"][b]["C1_block_pass"], "C2_pass": fam["blocks"][b]["C2_block_pass"],
            "gue_detected": bm["freeze"]["n_detected_secondary"],
            "BH_detected": len(bh_det), "BH_subset_of_hann": bh_det <= det,
            "BH_C1_pass": famb["blocks"][b]["C1_block_pass"], "BH_C2_pass": famb["blocks"][b]["C2_block_pass"],
            "hann_bh_max_ratio_diff_eligible": float(max(abs(float(rh[k]["fit_ratio_to_theory"]) - rb[k]) for k in elig)) if elig else None,
            "hann_bh_median_ratio_diff_all": float(np.median([abs(float(rh[k]["fit_ratio_to_theory"]) - rb[k]) for k in rh])),
            "spacing_variance": mb["spacing_variance"],
            "gue_env_var_95": mb["envelope_tests"]["gue"]["spacing_var_ensemble_q025_q975"],
            "C3_p": {f"{ref}_{st}": mb["envelope_tests"][ref][st]["p_value_mc"] for ref in ("gue", "poisson") for st in ("cdf", "r2", "k_connected")},
            "cue_N_eff": cue["N_eff"], "cue_rms_limit": cue["rms_cdf_distance_to_limit"], "cue_rms_corrected": cue["rms_cdf_distance_to_cue_corrected"],
            "cue_noise": cue["sampling_noise_rms_gue_ensemble"], "cue_var_pred": cue["spacing_variance_cue_corrected"],
        }
    n = len(blocks)
    in_all = sorted(k for k, c in det_counter.items() if c == n)
    variable = sorted((k, c) for k, c in det_counter.items() if c < n)
    var = np.array([per[b]["spacing_variance"] for b in blocks])
    Emid = np.array([np.mean(per[b]["E_range"]) for b in blocks])
    slope = float(np.polyfit(np.log(Emid), var, 1)[0])
    out["versions"][v] = {
        "blocks": per,
        "family": {
            "C1_blocks_passing": fam["C1_blocks_passing"], "C1_replicated": fam["C1_replicated_all_blocks"],
            "C1_blocks_with_unmatched": fam["C1_blocks_with_unmatched_detection"],
            "C2_blocks_passing": fam["C2_blocks_passing"], "C2_replicated": fam["C2_replicated_all_blocks"],
            "BH_C1_replicated": famb["C1_replicated_all_blocks"], "BH_C2_replicated": famb["C2_replicated_all_blocks"],
            "C3_rejections": {k: m2["family_holm"][k]["n_rejected"] for k in m2["family_holm"]},
        },
        "lines_detected_in_all_blocks": [f"{p}^{r}" if r > 1 else str(p) for p, r in in_all],
        "lines_variable": [(f"{p}^{r}" if r > 1 else str(p), c) for (p, r), c in variable],
        "spacing_variance_range": [float(var.min()), float(var.max())],
        "spacing_variance_slope_vs_logE": slope,
        "perf": {k: json.load(open(d[k] / "manifest.json"))["performance"] for k in ("primary", "bh", "m2")},
    }

v1, v2 = out["versions"]["m4-v1"], out["versions"]["m4-v2"]
s1, s2 = set(v1["lines_detected_in_all_blocks"]), set(v2["lines_detected_in_all_blocks"])
out["differences"] = {
    "in_all_blocks_only_v1": sorted(s1 - s2), "in_all_blocks_only_v2": sorted(s2 - s1),
    "n_in_all_blocks": [len(s1), len(s2)],
}
(Path(__file__).parent / "comparison.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))

def agg(v, key, f):
    vals = [b[key] for b in out["versions"][v]["blocks"].values() if b[key] is not None]
    return f(vals)

print("| Quantidade | m4-v1 (10.001–40.000) | m4-v2 (40.001–70.000) |")
print("|---|---|---|")
for label, key, f, fmt in [
    ("Detecções por bloco (mín–máx)", "detected", lambda x: (min(x), max(x)), "{}–{}"),
    ("Inconclusivos (total)", "inconclusive", sum, "{}"),
    ("Detecções sem correspondência (total)", "unmatched", sum, "{}"),
    ("p(S) máximo", "p_S", max, "{:.1e}"),
    ("Claramente detectáveis por bloco", "clearly_detectable", lambda x: (min(x), max(x)), "{}–{}"),
    ("Recuperação entre claras (mín)", "recovery_clear", min, "{:.3f}"),
    ("Elegíveis C2 por bloco", "C2_eligible", lambda x: (min(x), max(x)), "{}–{}"),
    ("Fração C2 ≤ tolerância (mín)", "C2_fraction", min, "{:.3f}"),
    ("Máx |razão−1| elegíveis", "C2_max", max, "{:.2e}"),
    ("Mediana |razão−1| elegíveis (máx entre blocos)", "C2_median", max, "{:.2e}"),
    ("Máx |razão−1| nas 47 linhas", "all47_max_abs_ratio_minus_1", max, "{:.2e}"),
    ("Q (mín)", "Q", min, "{:.4f}"),
    ("Detecções nulo GUE por bloco", "gue_detected", lambda x: (min(x), max(x)), "{}–{}"),
    ("Detecções BH por bloco", "BH_detected", lambda x: (min(x), max(x)), "{}–{}"),
    ("Hann×BH máx Δrazão elegíveis", "hann_bh_max_ratio_diff_eligible", max, "{:.2e}"),
    ("Var(s) (mín–máx)", "spacing_variance", lambda x: (min(x), max(x)), "{:.4f}–{:.4f}"),
    ("CUE N_eff (mín–máx)", "cue_N_eff", lambda x: (min(x), max(x)), "{:.2f}–{:.2f}"),
    ("CUE RMS ao limite (mín–máx)", "cue_rms_limit", lambda x: (min(x), max(x)), "{:.4f}–{:.4f}"),
    ("CUE RMS à corrigida (mín–máx)", "cue_rms_corrected", lambda x: (min(x), max(x)), "{:.4f}–{:.4f}"),
    ("CUE Var predita (mín–máx)", "cue_var_pred", lambda x: (min(x), max(x)), "{:.4f}–{:.4f}"),
]:
    a, b = agg("m4-v1", key, f), agg("m4-v2", key, f)
    fa = fmt.format(*a) if isinstance(a, tuple) else fmt.format(a)
    fb = fmt.format(*b) if isinstance(b, tuple) else fmt.format(b)
    print(f"| {label} | {fa} | {fb} |")
for k in ("C1_blocks_passing", "C1_replicated", "C1_blocks_with_unmatched", "C2_blocks_passing", "C2_replicated", "BH_C1_replicated", "BH_C2_replicated"):
    print(f"| {k} | {v1['family'][k]} | {v2['family'][k]} |")
for k in v1["family"]["C3_rejections"]:
    print(f"| C3 rejeições {k} | {v1['family']['C3_rejections'][k]} | {v2['family']['C3_rejections'][k]} |")
print(f"| Linhas detectadas em todos os blocos | {len(s1)} | {len(s2)} |")
print(f"| Inclinação Var(s) vs log E | {v1['spacing_variance_slope_vs_logE']:.4f} | {v2['spacing_variance_slope_vs_logE']:.4f} |")
print("apenas v1:", out["differences"]["in_all_blocks_only_v1"], "| apenas v2:", out["differences"]["in_all_blocks_only_v2"])
print("variáveis v1:", v1["lines_variable"], "| variáveis v2:", v2["lines_variable"])
