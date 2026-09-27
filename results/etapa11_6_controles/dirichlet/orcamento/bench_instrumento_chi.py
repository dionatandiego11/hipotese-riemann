"""
Orçamento do instrumento `ctrl-dirichlet-v1` medido **só com níveis sintéticos** (ADENDO_REGISTRO_v2_2 §3.3 e revisão
do usuário de 25/09/2026). Nenhum zero real é lido: as bordas de cada bloco vêm de N̄_χ⁻¹ nos índices do bloco, que
estão na configuração, e os níveis são substitutos GUE com a mesma contagem, densidade e grade.

Mede separadamente as etapas que o próprio instrumento cronometra (construção/transformada, nulo shuffle, nulo GUE,
calibração sintética, comparação aritmética) com as realizações reduzidas por um fator, para extrapolar depois.

Uso (da raiz do repositório):
  OMP_NUM_THREADS=1 .venv/bin/python3 results/etapa11_6_controles/dirichlet/orcamento/bench_instrumento_chi.py \
      --carater chi_m4 --bloco e02 --escala 0.01 --saida <arquivo.json>
"""
from __future__ import annotations

import argparse
import json
import os
import resource
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import instrumento_chi as ic  # noqa: E402

# contagens declaradas em ctrl_dirichlet_v1.toml, com o mínimo que o código aceita
SCALED = {"shuffle_sigma_realizations": 4, "shuffle_threshold_realizations": 20, "shuffle_score_realizations": 20,
          "gue_sigma_realizations": 4, "gue_threshold_realizations": 4, "gue_score_realizations": 0,
          "synthetic_realizations": 2, "phase_control_realizations": 10, "precision_perturbations": 2}


def surrogate_levels(i0: int, i1: int, ch, cfg, rng) -> np.ndarray:
    """Níveis substitutos GUE no intervalo de E que os índices i0..i1 ocupam pela contagem suave. Sem dado real."""
    n = i1 - i0 + 1
    base = ic.fold_chi(np.linspace(float(i0), float(i1), n), ch.q, ch.kappa)
    return ic.gue_levels_chi(base, cfg["gue_retained_fraction"], rng, ch.q, ch.kappa)


def cpu_seconds() -> float:
    r = resource.getrusage(resource.RUSAGE_SELF)
    c = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime + c.ru_utime + c.ru_stime


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--carater", required=True, choices=sorted(ic.CHARACTERS))
    ap.add_argument("--bloco", required=True)
    ap.add_argument("--escala", type=float, required=True, help="fator sobre as contagens declaradas")
    ap.add_argument("--config", type=Path, default=HERE.parent / "ctrl_dirichlet_v1.toml")
    ap.add_argument("--saida", type=Path, required=True)
    ap.add_argument("--tmp", type=Path, required=True)
    ap.add_argument("--semente", type=int, default=777001)
    a = ap.parse_args(argv)

    cfg_all = ic.load_config(a.config)
    ch = ic.CHARACTERS[a.carater]
    ccfg = cfg_all["characters"][ch.name]
    cfg = {k: v for k, v in cfg_all.items() if k != "characters"}
    block = next(b for b in ccfg["blocks"] if b["name"] == a.bloco)

    declared = {k: cfg[k] for k in SCALED}
    used = {}
    for k, minimum in SCALED.items():
        v = int(round(declared[k] * a.escala))
        used[k] = max(minimum, v) if declared[k] > 0 else 0
        cfg[k] = used[k]

    rng = np.random.default_rng(a.semente)
    t_lv = time.perf_counter()
    levels = surrogate_levels(block["first_index"], block["last_index"], ch, cfg, rng)
    # run_block_chi fatia gammas[i0-1:i1]; o prefixo é preenchido com a contagem suave e nunca é usado no bloco
    prefix = (ic.fold_chi(np.arange(1.0, block["first_index"]), ch.q, ch.kappa)
              if block["first_index"] > 1 else np.empty(0))
    gammas = np.concatenate([prefix, levels])
    t_lv = time.perf_counter() - t_lv

    a.tmp.mkdir(parents=True, exist_ok=True)
    cpu0, wall0 = cpu_seconds(), time.perf_counter()
    res = ic.run_block_chi(gammas, block, cfg, ch, a.tmp, np.random.SeedSequence(a.semente + 1), workers=1)
    cpu, wall = cpu_seconds() - cpu0, time.perf_counter() - wall0

    out = {"carater": ch.name, "bloco": block["name"], "indices": [block["first_index"], block["last_index"]],
           "n_niveis": int(len(levels)), "A": float(levels[0]), "B": float(levels[-1]),
           "fonte_dos_niveis": "substitutos GUE a partir de N̄_χ⁻¹ nos índices do bloco; nenhum zero real lido",
           "escala": a.escala, "realizacoes_declaradas": declared, "realizacoes_usadas": used,
           "segundos_por_etapa": res["timings_seconds"], "segundos_cpu_total": cpu, "segundos_parede_total": wall,
           "segundos_gerar_niveis": t_lv,
           "grade": {"n_pontos": int(len(res["instrument"]["t_grid"])) if "t_grid" in res.get("instrument", {}) else None,
                     "fwhm": res["instrument"].get("response", {}).get("fwhm")},
           "n_picos_candidatos": res["freeze"]["n_candidates"],
           "omp_num_threads": os.environ.get("OMP_NUM_THREADS"),
           "script_sha256": ic.compute_file_sha256(Path(__file__)),
           "instrumento_sha256": ic.compute_file_sha256(HERE.parent / "instrumento_chi.py"),
           "config_sha256": ic.compute_file_sha256(a.config),
           "quando": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    a.saida.parent.mkdir(parents=True, exist_ok=True)
    a.saida.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("bloco", "escala", "segundos_por_etapa", "segundos_cpu_total",
                                          "segundos_parede_total", "n_picos_candidatos")}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
