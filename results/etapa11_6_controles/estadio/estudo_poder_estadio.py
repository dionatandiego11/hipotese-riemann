"""
Estudo de poder do `ctrl-estadio-v1` (ADENDO_ESTADIO_2 §2 e ADENDO_ESTADIO_3 §2). Só espectros substitutos; nenhum
nível real do bilhar.

Por réplica: níveis GOE com a densidade de Weyl do quarto de estádio no intervalo do bloco; com sinal = densidade exata
da família bouncing ball injetada (D1-E); sem sinal = só o fundo. Em cada réplica roda a cadeia completa do instrumento
com as realizações reduzidas do adendo 3 e avalia E-C1, E-C1o, E-C4 e E-C2bb.

Uso (da raiz):
  .venv/bin/python3 results/etapa11_6_controles/estadio/estudo_poder_estadio.py --blocos G,g01,g04 --replicas 40
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import instrumento_estadio as ie  # noqa: E402

REDUCED = {"shuffle_sigma_realizations": 60, "shuffle_threshold_realizations": 300, "shuffle_score_realizations": 0,
           "goe_sigma_realizations": 4, "goe_threshold_realizations": 8, "goe_score_realizations": 0,
           "synthetic_realizations": 3, "phase_control_realizations": 100, "precision_perturbations": 2}


def wilson(k, n, z=1.96):
    if n == 0:
        return (None, None)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def replicate(block, cfg, lines, seed, with_signal, tmp: Path):
    rng = np.random.default_rng(seed)
    k0, k1 = block["k_min"], block["k_max"]
    n = int(round(float(ie.n_bar(k1) - ie.n_bar(k0))))
    y = ie.goe_central_levels(n, cfg["goe_retained_fraction"], rng)
    x0, x1 = float(ie.n_bar(k0)), float(ie.n_bar(k1))
    x = x0 + (y - y[0]) * (x1 - x0) / (y[-1] - y[0])
    guess = np.linspace(k0, k1, n)
    lv = ie.inject_bouncing_ball(x, k_guess=guess) if with_signal else ie.inverse_n_bar(x, k_guess=guess)
    res = ie.run_block_estadio(lv, {"name": block["name"]}, cfg, lines, tmp, np.random.SeedSequence(seed + 1), workers=1)
    ev = ie.evaluate_block(res, tmp / block["name"], cfg, lines)
    out = {"E_C1": ev["E_C1"], "E_C1o": ev["E_C1o"], "E_C4": ev["E_C4"], "n_detected": ev["n_detected"],
           "threshold_z": res["null_summary"]["shuffle"]["threshold_z"],
           "matching_tolerance": res["synthetic_calibration"]["matching_tolerance"], "n_levels": len(lv)}
    if "E_C2bb" in res:
        out["abs_ratio_minus_1"] = res["E_C2bb"]["abs_ratio_minus_1"]
        out["E_C2bb"] = bool(res["E_C2bb"]["abs_ratio_minus_1"] <= cfg["criteria"]["bb_ratio_tolerance"])
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--blocos", default="G,g01,g04")
    ap.add_argument("--replicas", type=int, default=40)
    ap.add_argument("--saida", type=Path, default=HERE / "estudo_poder_estadio.json")
    a = ap.parse_args(argv)
    cfg = ie.load_config(HERE / "ctrl_estadio_v1.toml")
    cfg.update(REDUCED)
    lines = ie.load_o1()
    blocks = {b["name"]: b for b in cfg["blocks"]}
    tmp = HERE / "_poder_tmp"
    tmp.mkdir(exist_ok=True)
    out = {"design": {"replicas": a.replicas, "reduced": REDUCED, "adendo": "ADENDO_ESTADIO_3.md"}, "blocks": {}}
    t0 = time.time()
    for name in [b.strip() for b in a.blocos.split(",")]:
        b = blocks[name]
        rows = {"com_sinal": [], "sem_sinal": []}
        conds = ["com_sinal"] + (["sem_sinal"] if name == "G" else [])
        for cond in conds:
            for i in range(a.replicas):
                seed = 900000 + hash((name, cond)) % 1000 * 1000 + i * 7
                rows[cond].append(replicate(b, cfg, lines, seed, cond == "com_sinal", tmp))
                if (i + 1) % 5 == 0:
                    print(f"{name}/{cond}: {i + 1}/{a.replicas} réplicas ({time.time() - t0:.0f} s)", flush=True)
        summ = {}
        for cond, rs in rows.items():
            if not rs:
                continue
            m = {}
            for key in ("E_C1", "E_C1o", "E_C4", "E_C2bb"):
                vals = [r[key] for r in rs if key in r]
                if vals:
                    k = int(sum(vals))
                    lo, hi = wilson(k, len(vals))
                    m[key] = {"p": k / len(vals), "k": k, "n": len(vals), "ic95": [lo, hi]}
            if any("abs_ratio_minus_1" in r for r in rs):
                v = np.array([r["abs_ratio_minus_1"] for r in rs if "abs_ratio_minus_1" in r])
                m["abs_ratio_minus_1"] = {"mediana": float(np.median(v)), "min": float(v.min()), "max": float(v.max())}
            m["limiar_z_medio"] = float(np.mean([r["threshold_z"] for r in rs]))
            m["tolerancia_media"] = float(np.mean([r["matching_tolerance"] for r in rs]))
            m["n_niveis"] = int(rs[0]["n_levels"])
            summ[cond] = m
        out["blocks"][name] = {"resumo": summ, "replicas": rows}
        a.saida.write_text(json.dumps(out, indent=2), encoding="utf-8")
        print(f"== {name}: {json.dumps(summ, indent=2, default=str)}", flush=True)
    out["seconds"] = round(time.time() - t0, 1)
    a.saida.write_text(json.dumps(out, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
