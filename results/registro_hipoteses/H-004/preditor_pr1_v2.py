"""
H-004 (P-R1) — avaliação v2 (ADENDO_H004_1.md). NÃO muda a previsão: importa as funções de previsão de
`preditor_pr1.py` (v1, hash conferido) e acrescenta:
  (a) conferência de todas as dependências carregadas de dentro do repositório contra `dependencias_v2.json`;
  (b) as condições de inconclusão da declaração (V1–V4 do controle) e as dos casos degenerados (ruído zero ou não
      finito, denominador nulo, bloco sem linhas selecionadas, arquivos incompletos ou incompatíveis).
Nenhum desses casos pode produzir "sucesso" calculado parcialmente.

Uso (da raiz, depois da execução do controle):
  .venv/bin/python3 results/registro_hipoteses/H-004/preditor_pr1_v2.py \
      --controle <pasta do instrumento_chi> --dados results/etapa11_6_controles/dados --saida <arquivo.json>
Congelamento das dependências (feito uma vez, antes dos dados; registrado no adendo):
  .venv/bin/python3 results/registro_hipoteses/H-004/preditor_pr1_v2.py --congelar-dependencias
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "results/etapa11_6_controles/dirichlet"))

V1_SHA256 = "5eede5b6fdada6537f75ff092095216f057f0640c0c1ca0c75ae04132d411394"
DEPS_FILE = HERE / "dependencias_v2.json"
BLOCKS = {"chi_m4": [("e02", 3001, 6000), ("e03", 6001, 9000), ("e04", 9001, 12000)],
          "chi_5": [("f02", 3001, 6000), ("f03", 6001, 9000), ("f04", 9001, 12000)]}
SEEDS = {"chi_m4": 20260923, "chi_5": 20260924}      # as mesmas da v1 (main de preditor_pr1.py)


def sha256(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _import_chain():
    if sha256(HERE / "preditor_pr1.py") != V1_SHA256:
        raise SystemExit("preditor_pr1.py (v1) difere do hash declarado; avaliação abortada")
    import preditor_pr1 as P          # noqa: F401
    import instrumento_chi as ic      # noqa: F401
    import dirichlet_zeros as dz      # noqa: F401
    return P, ic, dz


def loaded_repo_modules() -> dict:
    out = {}
    for name, mod in sorted(sys.modules.items()):
        f = getattr(mod, "__file__", None)
        if not f:
            continue
        p = Path(f).resolve()
        if ROOT in p.parents and ".venv" not in p.parts and p.suffix == ".py":
            out[str(p.relative_to(ROOT))] = sha256(p)
    out[str(Path(__file__).resolve().relative_to(ROOT))] = sha256(Path(__file__))
    return out


def check_dependencies() -> dict:
    frozen = json.loads(DEPS_FILE.read_text(encoding="utf-8"))["modules"]
    now = loaded_repo_modules()
    diff = {k: (frozen.get(k), now.get(k)) for k in set(frozen) | set(now) if frozen.get(k) != now.get(k)}
    return {"ok": not diff, "differences": diff}


# ------------------------------------------------------------------ regras (declaração §4 + adendo)

def classify_v2(blocks: dict, preconditions_ok: bool, precondition_notes: list) -> dict:
    """blocks: nome → {"e_obs", "e_prev", "noise", "selected"} (listas). Regras do ADENDO_H004_1 §2."""
    notes = list(precondition_notes)
    if not preconditions_ok:
        return {"verdict": "inconclusivo", "reason": "pré-condições", "notes": notes}
    eo_all, ep_all, s_all, per_ok = [], [], [], 0
    per_block = {}
    for name, v in blocks.items():
        eo, ep, s, sel = (np.asarray(v[k], dtype=float) for k in ("e_obs", "e_prev", "noise", "selected"))
        sel = sel.astype(bool)
        if not (np.all(np.isfinite(eo)) and np.all(np.isfinite(ep)) and np.all(np.isfinite(s)) and np.all(s > 0)):
            return {"verdict": "inconclusivo", "reason": f"valores não finitos ou ruído não positivo no bloco {name}",
                    "notes": notes}
        if sel.sum() == 0:
            per_block[name] = {"n_selected": 0, "EF": None}
            continue
        zo, zr = eo[sel] / s[sel], (eo[sel] - ep[sel]) / s[sel]
        den = float(np.sum(zo ** 2))
        ef = (1.0 - float(np.sum(zr ** 2)) / den) if den > 0 else None
        per_block[name] = {"n_selected": int(sel.sum()), "EF": ef}
        if ef is not None and ef >= 0.5:
            per_ok += 1
        eo_all.append(eo[sel]); ep_all.append(ep[sel]); s_all.append(s[sel])
    if not eo_all:
        return {"verdict": "inconclusivo", "reason": "nenhuma linha selecionada", "per_block": per_block, "notes": notes}
    eo, ep, s = (np.concatenate(x) for x in (eo_all, ep_all, s_all))
    n = len(eo)
    den = float(np.sum((eo / s) ** 2))
    if not (den > 0 and math.isfinite(den)):
        return {"verdict": "inconclusivo", "reason": "denominador de EF nulo ou não finito", "per_block": per_block, "notes": notes}
    EF = 1.0 - float(np.sum(((eo - ep) / s) ** 2)) / den
    S = float(np.mean(np.sign(eo) == np.sign(ep)))
    if n < 30:
        verdict = "inconclusivo"
        reason = "menos de 30 linhas selecionadas"
    elif EF >= 0.9 and S >= 0.9 and per_ok >= 5:
        verdict, reason = "sucesso", "EF >= 0,9, S >= 0,9 e EF >= 0,5 em >= 5 de 6 blocos"
    elif EF < 0.5 or S < 0.7:
        verdict, reason = "falha", "EF < 0,5 ou S < 0,7"
    else:
        verdict, reason = "inconclusivo", "entre os limiares"
    return {"verdict": verdict, "reason": reason, "pooled": {"n_selected": n, "EF": EF, "S": S},
            "blocks_with_EF_ge_0.5": per_ok, "per_block": per_block, "notes": notes}


def preconditions(control_dir: Path, data_dir: Path, P, ic, dz) -> tuple:
    notes, ok = [], True
    zeros = {}
    for ch in ("chi_m4", "chi_5"):
        man = data_dir / f"manifest_{ch}_12000.json"
        zf = data_dir / f"zeros_{ch}_12000.txt"
        if not (man.exists() and zf.exists()):
            return False, notes + [f"{ch}: manifesto ou arquivo de zeros ausente"], None
        m = json.loads(man.read_text(encoding="utf-8"))
        if not m.get("all_checks_passed"):
            ok = False
            notes.append(f"{ch}: V1–V4 não aprovadas no manifesto do cálculo")
        if m.get("n_zeros") != 12000 or m.get("output_sha256") != sha256(zf):
            return False, notes + [f"{ch}: manifesto incompatível com o arquivo de zeros"], None
        zeros[ch] = np.loadtxt(zf, dtype=np.float64)
        cat_periods = [c["period_theoretical"] for c in ic.chi_catalog_module(dz.CHARACTERS[ch]).prime_power_catalog(0.5, 5.0)]
        for name, i0, i1 in BLOCKS[ch]:
            bd = control_dir / name
            if not ((bd / "arithmetic_matches.csv").exists() and (bd / "block_metrics.json").exists()):
                return False, notes + [f"{name}: saída do controle ausente"], None
            bm = json.loads((bd / "block_metrics.json").read_text(encoding="utf-8"))
            g = zeros[ch][i0 - 1:i1]
            if abs(bm["instrument"]["A"] - g[0]) > 1e-9 or abs(bm["instrument"]["B"] - g[-1]) > 1e-9:
                return False, notes + [f"{name}: bordas do controle diferem do arquivo de zeros"], None
            rows = list(csv.DictReader(open(bd / "arithmetic_matches.csv", encoding="utf-8")))
            per = [float(r["period_theoretical"]) for r in rows]
            if len(per) != len(cat_periods) or max(abs(a - b) for a, b in zip(per, cat_periods)) > 1e-12:
                return False, notes + [f"{name}: catálogo do controle incompatível"], None
    return ok, notes, zeros


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--congelar-dependencias", action="store_true")
    ap.add_argument("--controle", type=Path)
    ap.add_argument("--dados", type=Path)
    ap.add_argument("--saida", type=Path)
    a = ap.parse_args(argv)
    P, ic, dz = _import_chain()
    if a.congelar_dependencias:
        DEPS_FILE.write_text(json.dumps({"modules": loaded_repo_modules()}, indent=2, sort_keys=True), encoding="utf-8")
        print(f"dependências congeladas em {DEPS_FILE.name}")
        return 0
    dep = check_dependencies()
    if not dep["ok"]:
        print(json.dumps({"verdict": "abortado", "reason": "dependências mudaram", "differences": dep["differences"]}, indent=2))
        return 2
    ok, notes, zeros = preconditions(a.controle, a.dados, P, ic, dz)
    blocks = {}
    if ok and zeros is not None:
        for ch, blist in BLOCKS.items():
            res = P.evaluate_dirichlet(a.controle, a.dados / f"zeros_{ch}_12000.txt", ch,
                                       [{"name": n, "first_index": i0, "last_index": i1} for n, i0, i1 in blist], seed=SEEDS[ch])
            blocks.update(res)
    cls = classify_v2(blocks, ok and zeros is not None, notes)
    out = {"dependencies": dep, "preconditions_ok": ok, "notes": notes, "blocks": blocks, "classification": cls,
           "v1_sha256": V1_SHA256}
    a.saida.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(cls, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
