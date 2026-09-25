"""
Passe de completude D3 do `ctrl-dirichlet-v1` — ADENDO_DIRICHLET_3.md (`02340a5c…`).

A varredura por troca de sinal com passo d̄/8 perde **pares** de zeros separados por menos que um passo. Em χ₋₄ isso
reprovou V1 (déficit ≈ 14 em 12.000) e V2 (3.002 contra 3.000 no bloco alto). Este módulo implementa as Etapas A, B e C
do adendo e as re-verificações do §5, **sem alterar** `dirichlet_zeros.py` (`65056bc2…`), que é importado como está.

Uso (da raiz do repositório):
  .venv/bin/python3 results/etapa11_6_controles/dirichlet/completude/completude_d3.py \
      --carater chi_m4 --zeros results/etapa11_6_controles/dados/zeros_chi_m4_12000.txt
  ... e, depois, a V2' (longa, com retomada):
  .venv/bin/python3 .../completude_d3.py --carater chi_m4 --v2
"""
from __future__ import annotations

import argparse
import json
import signal
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import dirichlet_zeros as dz  # noqa: E402  (script congelado; importado, nunca alterado)

# --- constantes do adendo §3 (nenhuma é ajustável por linha de comando) -------------------------------------------
THRESHOLD_A = 1.6           # Etapa A: intervalos com s > 1,6 d̄
SCALE_A = 0.25              # passo d̄/32  (= step_fraction 1/8 × 0,25)
WINDOW = 200                # Etapa B: janelas de 200 zeros
TOL_LEVEL = 0.75            # |m_j − m_0| ≤ 0,75
TOL_STEP = 1.5              # |m_{j+1} − m_j| < 1,5
STAGE_C = ((1.1, 1.0 / 16.0), (0.8, 1.0 / 64.0))   # (limiar em d̄, step_scale) → d̄/128 e d̄/512
EDGE = 10 * dz.REFINE_TOL   # margem nas pontas do intervalo, como em rescan_large_gaps
N_WORK = 12000              # segmento inicial que vira o dado de trabalho
ADDENDUM_SHA = "02340a5ca804e4f0bfa453ac8b9820e162381d7c260c2944c4911843679b2350"


class Interrompido(Exception):
    pass


def _install_sigterm() -> None:
    def handler(signum, frame):
        raise Interrompido(f"sinal {signum}")
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, handler)


# --- funções puras -------------------------------------------------------------------------------------------------
def normalized_gaps(zeros, ch: dz.Character) -> np.ndarray:
    """s_i / d̄ no ponto médio de cada intervalo consecutivo."""
    z = np.asarray(zeros, dtype=float)
    mid = 0.5 * (z[:-1] + z[1:])
    dbar = np.array([dz.mean_spacing(float(t), ch.q) for t in mid])
    return np.diff(z) / dbar


def gaps_above(zeros, ch: dz.Character, threshold: float, lo_index: int = 0,
               hi_index: Optional[int] = None) -> List[int]:
    """Índices i (0-based) dos intervalos (z_i, z_{i+1}) com s > threshold·d̄, restritos a [lo_index, hi_index)."""
    r = normalized_gaps(zeros, ch)
    hi = len(r) if hi_index is None else min(hi_index, len(r))
    return [int(i) for i in np.where(r > threshold)[0] if lo_index <= i < hi]


def s_values(zeros, ch: dz.Character) -> np.ndarray:
    """S(n) = n − θ_χ(γ_n)/π (n em base 1)."""
    with mp.workdps(dz.DEFAULT_DPS):
        theta = np.array([float(dz.theta_chi(float(t), ch) / mp.pi) for t in zeros])
    return np.arange(1, len(zeros) + 1, dtype=float) - theta


def certificate(S: np.ndarray, window: int = WINDOW) -> Dict:
    """Certificado D3-C1 (adendo §3, Etapa B)."""
    n_win = len(S) // window
    med = [float(np.median(S[j * window:(j + 1) * window])) for j in range(n_win)]
    if not med:
        return {"passed": False, "note": "lista curta demais para o certificado", "n_windows": 0}
    level_bad = [j for j, m in enumerate(med) if abs(m - med[0]) > TOL_LEVEL]
    steps = [{"between_windows": [j, j + 1], "delta": med[j + 1] - med[j],
              "index_range": [j * window, min((j + 2) * window, len(S))],
              "deficit": int(round(-(med[j + 1] - med[j])))}
             for j in range(len(med) - 1) if abs(med[j + 1] - med[j]) >= TOL_STEP]
    return {"passed": not level_bad and not steps, "window": window, "n_windows": n_win,
            "median_first": med[0], "median_last": med[-1], "median_min": min(med), "median_max": max(med),
            "windows_off_level": level_bad, "steps": steps,
            "internal_spread": float(np.max(np.abs(np.diff(med)))) if len(med) > 1 else 0.0}


def merge(zeros: List[float], recovered: List[float]) -> List[float]:
    """Insere os recuperados mantendo a ordem; a lista original é subconjunto da saída."""
    return sorted(list(zeros) + list(recovered))


# --- varredura dirigida --------------------------------------------------------------------------------------------
def rescan_gap(ch: dz.Character, lo: float, hi: float, step_scale: float,
               finder: Optional[dz.ZeroFinder] = None) -> List[float]:
    f = finder if finder is not None else dz.ZeroFinder(ch)
    return f.scan(lo + EDGE, t_stop=hi - EDGE, step_scale=step_scale)


def sweep(ch: dz.Character, zeros: List[float], indices: List[int], step_scale: float,
          state: Optional[Dict] = None, ckpt_path: Optional[Path] = None, every_seconds: float = 120.0,
          label: str = "A") -> Tuple[List[Dict], dz.ScanStats]:
    """
    Reexamina os intervalos `indices` com o passo dado. Com `state`/`ckpt_path`, grava progresso e retoma: os
    intervalos já feitos ficam em state['done'] e não são refeitos.
    """
    finder = dz.ZeroFinder(ch)
    state = state if state is not None else {}
    done = {int(k): v for k, v in state.get("done", {}).items()}
    dz._restore_stats(finder, state.get("stats"))
    t_last = time.monotonic()
    t0 = time.perf_counter()
    try:
        for k, i in enumerate(indices):
            if i in done:
                continue
            lo, hi = float(zeros[i]), float(zeros[i + 1])
            found = rescan_gap(ch, lo, hi, step_scale, finder)
            done[i] = {"interval": [lo, hi], "step_scale": step_scale, "found": [float(z) for z in found]}
            if found:
                print(f"[{label}] i={i + 1}: {len(found)} zero(s) em [{lo:.6f}, {hi:.6f}]"
                      + "".join(f"\n        {z:.9f}" for z in found), flush=True)
            if ckpt_path is not None and (time.monotonic() - t_last >= every_seconds or k + 1 == len(indices)):
                state["done"] = {str(a): b for a, b in done.items()}
                state["stats"] = dict(finder.stats.__dict__)
                state["updated"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
                dz._atomic_write_json(ckpt_path, state)
                t_last = time.monotonic()
                print(f"[{label}] {len(done)}/{len(indices)} intervalos; "
                      f"{sum(len(v['found']) for v in done.values())} zeros recuperados; "
                      f"{time.perf_counter() - t0:.0f} s", flush=True)
    finally:
        state["done"] = {str(a): b for a, b in done.items()}
        state["stats"] = dict(finder.stats.__dict__)
        if ckpt_path is not None:
            dz._atomic_write_json(ckpt_path, state)
    log = [done[i] | {"index": i + 1} for i in indices if i in done]
    return log, finder.stats


def stage_a(ch: dz.Character, zeros: List[float], state: Optional[Dict] = None,
            ckpt_path: Optional[Path] = None) -> Tuple[List[float], Dict]:
    idx = gaps_above(zeros, ch, THRESHOLD_A)
    print(f"[A] {len(idx)} intervalos acima de {THRESHOLD_A} d̄; passo d̄/32", flush=True)
    log, stats = sweep(ch, zeros, idx, SCALE_A, state=state, ckpt_path=ckpt_path, label="A")
    rec = [z for entry in log for z in entry["found"]]
    return rec, {"threshold": THRESHOLD_A, "step_scale": SCALE_A, "n_intervals": len(idx),
                 "n_recovered": len(rec), "intervals_with_zeros": [e for e in log if e["found"]],
                 "stats": dict(stats.__dict__)}


def stage_c(ch: dz.Character, zeros: List[float], cert: Dict, region_override: Optional[Tuple[int, int]] = None,
            rounds=STAGE_C) -> Tuple[List[float], Dict]:
    """Resíduo: para cada degrau do certificado, reexamina a região com limiar e passo mais finos (adendo §3, C)."""
    out: List[float] = []
    rounds_log = []
    cur = list(zeros)
    for r, (thr, scale) in enumerate(rounds, start=1):
        cert_now = certificate(s_values(cur, ch)) if r > 1 else cert
        if cert_now["passed"]:
            break
        per_step = []
        for st in cert_now["steps"]:
            lo_i, hi_i = region_override if region_override is not None else tuple(st["index_range"])
            idx = gaps_above(cur, ch, thr, lo_index=lo_i, hi_index=hi_i)
            print(f"[C{r}] degrau {st['delta']:+.2f} em {st['index_range']}: {len(idx)} intervalos > {thr} d̄", flush=True)
            log, stats = sweep(ch, cur, idx, scale, label=f"C{r}")
            found = [z for e in log for z in e["found"]]
            per_step.append({"step": st, "threshold": thr, "step_scale": scale, "n_intervals": len(idx),
                             "n_recovered": len(found), "intervals_with_zeros": [e for e in log if e["found"]],
                             "stats": dict(stats.__dict__)})
            out.extend(found)
            cur = merge(cur, found)
        rounds_log.append({"round": r, "per_step": per_step})
    return out, {"rounds": rounds_log}


# --- re-verificações -------------------------------------------------------------------------------------------------
def reverify(ch: dz.Character, work: List[float]) -> Dict:
    v1 = dz.v1_completeness(work, ch)
    v3 = dz.v3_second_evaluation(work, ch)
    v4 = dz.v4_reality(ch, work)
    return {"V1": v1, "V3": v3, "V4": v4}


def v2_prime(ch: dz.Character, work: List[float], state: Optional[Dict] = None,
             ckpt_path: Optional[Path] = None, first: int = 9001, last: int = N_WORK) -> Dict:
    """
    V2′ (adendo §5): recalcula o bloco com passo pela metade, aplica o passe de completude **à lista recomputada** e só
    então compara contagem e posições com a lista de trabalho. Com `ckpt_path`, grava progresso e retoma.
    """
    lo, hi = dz.v2_bounds(work, first, last)
    state = state if state is not None else {}
    finder = dz.ZeroFinder(ch, step_fraction=dz.STEP_FRACTION / 2.0)
    saved = state.get("scan")
    again: List[float] = []
    ck = None
    if ckpt_path is not None:
        ck = dz.Checkpointer(ckpt_path, state, every_zeros=25, every_seconds=120.0)
    if saved:
        dz._restore_stats(finder, saved.get("stats"))
        again = list(saved["zeros"])
        start, fa = float(saved["a"]), float(saved["fa"])
        print(f"[V2'] retomando em t={start:.4f} com {len(again)} zeros", flush=True)
    else:
        start, fa = lo, None
    hook = ck.scan_hook("scan", finder, extra=None) if ck else None
    again = finder.scan(start, t_stop=hi, zeros=again, fa_start=fa, on_step=hook)
    if ck:
        ck.end_scan()
    print(f"[V2'] varredura com passo d̄/16: {len(again)} zeros", flush=True)
    # passe de completude na lista recomputada (mesma Etapa A)
    rec, a_log = stage_a(ch, again)
    again_full = merge(again, rec)
    cert = certificate(s_values(again_full, ch))
    res = dz.v2_compare(work, again_full, first, last, finder.stats)
    res["completude_recomputada"] = {"n_recovered": a_log["n_recovered"], "certificate": cert}
    return res


# --- execução ----------------------------------------------------------------------------------------------------
def run(ch: dz.Character, zeros_path: Path, out_dir: Path, resume: bool = True) -> Dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    zeros = [float(x) for x in np.loadtxt(zeros_path)]
    src_sha = dz.sha256_of(zeros_path)
    ck_path = out_dir / f"progresso_d3_{ch.name}.json"
    state = json.loads(ck_path.read_text()) if (resume and ck_path.exists()) else {
        "adendo_sha256": ADDENDUM_SHA, "script_congelado_sha256": dz.sha256_of(Path(dz.__file__)),
        "entrada": str(zeros_path), "entrada_sha256": src_sha, "n_entrada": len(zeros),
        "iniciado": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    t0 = time.time()
    rec_a, a_log = stage_a(ch, zeros, state=state.setdefault("etapa_a", {}), ckpt_path=ck_path)
    corrected = merge(zeros, rec_a)
    cert_a = certificate(s_values(corrected, ch))
    print(f"[B] certificado depois da Etapa A: passed={cert_a['passed']} "
          f"medianas {cert_a['median_first']:+.3f} → {cert_a['median_last']:+.3f}", flush=True)
    rec_c, c_log = ([], {"rounds": []})
    if not cert_a["passed"]:
        rec_c, c_log = stage_c(ch, corrected, cert_a)
        corrected = merge(corrected, rec_c)
    cert = certificate(s_values(corrected, ch))
    work = corrected[:N_WORK]
    checks = reverify(ch, work)
    passed = bool(cert["passed"] and checks["V1"]["passed"] and checks["V3"]["passed"] and checks["V4"]["passed"])
    out_zeros = out_dir / f"zeros_{ch.name}_{N_WORK}_completo.txt"
    dz.write_zeros(out_zeros, work)
    (out_dir / f"recuperados_{ch.name}.json").write_text(json.dumps(
        {"etapa_a": a_log, "etapa_c": c_log, "recuperados": sorted(rec_a + rec_c)}, indent=2), encoding="utf-8")
    man = {"protocolo": "ctrl-dirichlet-v1", "passe": "D3", "adendo_sha256": ADDENDUM_SHA,
           "script_congelado_sha256": dz.sha256_of(Path(dz.__file__)),
           "script_d3_sha256": dz.sha256_of(Path(__file__)),
           "caractere": {"name": ch.name, "q": ch.q, "kappa": ch.kappa},
           "entrada": {"arquivo": str(zeros_path), "sha256": src_sha, "n": len(zeros)},
           "etapa_a": {k: v for k, v in a_log.items() if k != "intervals_with_zeros"},
           "n_recuperados_a": len(rec_a), "n_recuperados_c": len(rec_c),
           "certificado_apos_a": cert_a, "certificado_final": cert,
           "n_corrigida": len(corrected), "n_trabalho": len(work),
           "gamma_ultimo_original": zeros[-1], "gamma_ultimo_trabalho": work[-1],
           "verificacoes": checks, "passou": passed,
           "saida": {"arquivo": str(out_zeros), "sha256": dz.sha256_of(out_zeros)},
           "segundos": round(time.time() - t0, 1),
           "versoes": {"python": sys.version.split()[0], "mpmath": mp.__version__, "numpy": np.__version__},
           "terminado": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    dz._atomic_write_json(out_dir / f"manifesto_d3_{ch.name}.json", man)
    state["fase"] = "a_b_c_concluidas"
    dz._atomic_write_json(ck_path, state)
    print(json.dumps({k: man[k] for k in ("n_recuperados_a", "n_recuperados_c", "n_corrigida", "passou")}, indent=2))
    return man


def run_v2(ch: dz.Character, out_dir: Path) -> Dict:
    man_path = out_dir / f"manifesto_d3_{ch.name}.json"
    man = json.loads(man_path.read_text())
    work = [float(x) for x in np.loadtxt(out_dir / f"zeros_{ch.name}_{N_WORK}_completo.txt")]
    ck_path = out_dir / f"progresso_d3_v2_{ch.name}.json"
    state = json.loads(ck_path.read_text()) if ck_path.exists() else {"adendo_sha256": ADDENDUM_SHA}
    res = v2_prime(ch, work, state=state, ckpt_path=ck_path)
    man["verificacoes"]["V2"] = res
    man["passou"] = bool(man["certificado_final"]["passed"] and man["verificacoes"]["V1"]["passed"]
                         and res["passed"] and man["verificacoes"]["V3"]["passed"]
                         and man["verificacoes"]["V4"]["passed"])
    man["v2_terminado"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    dz._atomic_write_json(man_path, man)
    print(json.dumps({"V2": {k: res[k] for k in ("n_reference", "n_recomputed", "same_count",
                                                 "max_abs_difference", "passed")}, "passou": man["passou"]}, indent=2))
    return man


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Passe de completude D3 (ADENDO_DIRICHLET_3)")
    ap.add_argument("--carater", required=True, choices=sorted(dz.CHARACTERS))
    ap.add_argument("--zeros", type=Path, help="lista original (obrigatória fora de --v2)")
    ap.add_argument("--saida", type=Path, default=HERE)
    ap.add_argument("--v2", action="store_true", help="roda a V2' sobre a lista já corrigida")
    a = ap.parse_args(argv)
    _install_sigterm()
    ch = dz.CHARACTERS[a.carater]
    try:
        if a.v2:
            run_v2(ch, a.saida)
        else:
            if a.zeros is None:
                ap.error("--zeros é obrigatório")
            run(ch, a.zeros, a.saida)
    except Interrompido as e:
        print(f"Interrompido ({e}). Progresso gravado; rode o mesmo comando para retomar.", flush=True)
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())
