"""Testes das regras de classificação de H-004 v2 (ADENDO_H004_1 §2), com casos artificiais. Sem dados reais."""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
import preditor_pr1_v2 as V


def blk(eo, ep, s, sel):
    return {"e_obs": list(eo), "e_prev": list(ep), "noise": list(s), "selected": list(sel)}


def good_blocks(n=6, m=8, scale=1.0, sign_flip=False, noise_obs=0.0, seed=0):
    rng = np.random.default_rng(seed)
    out = {}
    for b in range(n):
        ep = rng.uniform(1e-9, 1e-7, m) * rng.choice([-1, 1], m)
        eo = (-ep if sign_flip else ep) * scale + rng.normal(0, noise_obs, m)
        out[f"b{b}"] = blk(eo, ep, np.full(m, 1e-11), np.ones(m, bool))
    return out


def test_success():
    assert V.classify_v2(good_blocks(), True, [])["verdict"] == "sucesso"


def test_failure_sign():
    assert V.classify_v2(good_blocks(sign_flip=True), True, [])["verdict"] == "falha"


def test_failure_scale():
    assert V.classify_v2(good_blocks(scale=0.0, noise_obs=1e-8), True, [])["verdict"] == "falha"


def test_preconditions_fail_is_inconclusive():
    assert V.classify_v2(good_blocks(), False, ["V1–V4"])["verdict"] == "inconclusivo"


def test_zero_or_nonfinite_noise_inconclusive():
    b = good_blocks(); b["b0"]["noise"][0] = 0.0
    assert V.classify_v2(b, True, [])["verdict"] == "inconclusivo"
    b = good_blocks(); b["b1"]["e_prev"][2] = float("nan")
    assert V.classify_v2(b, True, [])["verdict"] == "inconclusivo"


def test_zero_denominator_inconclusive():
    b = good_blocks()
    for v in b.values():
        v["e_obs"] = [0.0] * len(v["e_obs"])
    assert V.classify_v2(b, True, [])["verdict"] == "inconclusivo"


def test_block_without_selection_counts_as_not_ok():
    b = good_blocks()
    b["b0"]["selected"] = [False] * len(b["b0"]["selected"])
    b["b1"]["selected"] = [False] * len(b["b1"]["selected"])
    r = V.classify_v2(b, True, [])
    assert r["per_block"]["b0"]["EF"] is None and r["blocks_with_EF_ge_0.5"] == 4 and r["verdict"] != "sucesso"


def test_too_few_lines_inconclusive():
    assert V.classify_v2(good_blocks(n=6, m=4), True, [])["verdict"] == "inconclusivo"   # 24 < 30
