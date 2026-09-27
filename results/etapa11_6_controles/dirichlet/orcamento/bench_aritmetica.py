"""
Decomposição do custo da etapa aritmética do `ctrl-dirichlet-v1`: separa o controle de fase das perturbações de
precisão variando **uma contagem por vez**, com o resto do pipeline calculado uma única vez. Só níveis sintéticos.

  OMP_NUM_THREADS=1 .venv/bin/python3 results/etapa11_6_controles/dirichlet/orcamento/bench_aritmetica.py \
      --carater chi_m4 --bloco e02 --saida bench_aritmetica.json
"""
from __future__ import annotations

import argparse
import json
import resource
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))
import instrumento_chi as ic  # noqa: E402
from bench_instrumento_chi import surrogate_levels  # noqa: E402
from riemann_spectra.inverse_spectroscopy import arithmetic_comparison  # noqa: E402
from riemann_spectra.periods import (adjusted_p_values, classify_detection, detect_blind_peaks,  # noqa: E402
                                     null_noise_profile, threshold_interval)

COMBOS = [(10, 2), (999, 2), (10, 20), (999, 20)]   # (phase_control_realizations, precision_perturbations)


def cpu() -> float:
    a, b = resource.getrusage(resource.RUSAGE_SELF), resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime + a.ru_stime + b.ru_utime + b.ru_stime


def threads() -> int:
    return int([l.split()[1] for l in Path("/proc/self/status").read_text().splitlines() if l.startswith("Threads:")][0])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--carater", required=True, choices=sorted(ic.CHARACTERS))
    ap.add_argument("--bloco", required=True)
    ap.add_argument("--config", type=Path, default=HERE.parent / "ctrl_dirichlet_v1.toml")
    ap.add_argument("--saida", type=Path, required=True)
    ap.add_argument("--tmp", type=Path, required=True)
    ap.add_argument("--semente", type=int, default=777101)
    a = ap.parse_args(argv)

    cfg_all = ic.load_config(a.config)
    ch = ic.CHARACTERS[a.carater]
    cfg = {k: v for k, v in cfg_all.items() if k != "characters"}
    block = next(b for b in cfg_all["characters"][ch.name]["blocks"] if b["name"] == a.bloco)
    rng = np.random.default_rng(a.semente)
    g = surrogate_levels(block["first_index"], block["last_index"], ch, cfg, rng)

    params = ic.instrument_params(g, cfg, ch)
    tr = ic._instrument(params)
    fwhm = tr.response["fwhm"]
    F = tr.transform(g)
    ss = np.random.SeedSequence(a.semente + 1)
    s_sig, s_thr, s_prec, s_phase = ss.spawn(4)
    frac, cand_z = cfg["gue_retained_fraction"], cfg["candidate_z"]
    # nulo mínimo, só para a etapa aritmética ter sigma e limiar (não é o nulo declarado)
    powers = [ic._task_power(("shuffle", g, s, params, frac)) for s in s_sig.spawn(8)]
    sigma = null_noise_profile(np.sqrt(np.array(powers)), tr.t_grid, cfg["noise_smooth_window"])
    res = [ic._task_max(("shuffle", g, s, params, frac, sigma, fwhm, cand_z)) for s in s_thr.spawn(40)]
    null_max = np.array([r[0] for r in res])
    interval = threshold_interval(null_max, cfg["alpha"], cfg["threshold_confidence"])
    nulls = {"shuffle": {"sigma": sigma, "null_max": null_max, "threshold": interval["z_high"], "interval": interval,
                         "score_set_peaks": [], "score_set_max": np.array([]), "B_sigma": 8, "B_threshold": 40,
                         "B_score": 0}}
    peaks = detect_blind_peaks(tr.t_grid, F, fwhm, sigma, candidate_z=cand_z, evaluator=lambda t: tr.evaluate(g, t))
    # anotação dos picos como em run_block_chi; aqui o nulo secundário é o mesmo (é medição de tempo, não de critério)
    for pk in peaks:
        pk["p_adjusted_primary"] = float(adjusted_p_values([pk["z"]], null_max)[0])
        pk["class_primary"] = classify_detection(pk["z"], interval)
        pk["detected_primary"] = pk["class_primary"] == "detected"
        pk["z_secondary"] = pk["z"]
        pk["p_adjusted_secondary"] = pk["p_adjusted_primary"]
        pk["class_secondary"] = pk["class_primary"]
        pk["detected_secondary"] = pk["detected_primary"]
        pk["fwhm_instrument"] = fwhm
    a.tmp.mkdir(parents=True, exist_ok=True)
    rows = []
    for phase, prec in COMBOS:
        c = dict(cfg); c["phase_control_realizations"] = phase; c["precision_perturbations"] = prec
        d = a.tmp / f"arit_{phase}_{prec}"; d.mkdir(parents=True, exist_ok=True)
        t0, c0 = time.perf_counter(), cpu()
        arithmetic_comparison(ic.chi_catalog_module(ch), tr, g, peaks, nulls, "shuffle",
                              0.05 * fwhm, 1.0 * fwhm, d, c, s_prec.spawn(1)[0], s_phase.spawn(1)[0])
        rows.append({"phase": phase, "precision": prec, "parede_s": time.perf_counter() - t0, "cpu_s": cpu() - c0,
                     "threads": threads()})
        print(json.dumps(rows[-1]), flush=True)
    # decomposição: custo = base + p*fase + q*precisão
    A = np.array([[1.0, r["phase"], r["precision"]] for r in rows])
    y = np.array([r["cpu_s"] for r in rows])
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ beta
    out = {"carater": ch.name, "bloco": a.bloco, "n_niveis": int(len(g)), "n_picos": len(peaks),
           "nulo_usado": {"B_sigma": 8, "B_threshold": 40, "nota": "nulo mínimo, não o declarado; serve só para a etapa rodar"},
           "medicoes": rows, "decomposicao": {"base_s": beta[0], "s_por_realizacao_de_fase": beta[1],
                                              "s_por_perturbacao_de_precisao": beta[2],
                                              "rms_s": float(np.sqrt(np.mean(resid ** 2)))},
           "declarado": {"phase_control_realizations": cfg_all["phase_control_realizations"],
                         "precision_perturbations": cfg_all["precision_perturbations"]},
           "segundos_por_bloco_declarado": float(beta[0] + beta[1] * cfg_all["phase_control_realizations"]
                                                 + beta[2] * cfg_all["precision_perturbations"]),
           "script_sha256": ic.compute_file_sha256(Path(__file__)), "quando": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    a.saida.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("decomposicao", "segundos_por_bloco_declarado")}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
