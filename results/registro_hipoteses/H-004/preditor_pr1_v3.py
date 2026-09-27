"""
H-004 (P-R1) — avaliação v3 (ADENDO_H004_2.md, `a5d071be…`). **A análise não muda**: previsão, ruído, seleção,
limiares, medida primária e classificação são importados de `preditor_pr1_v2.py` (hash conferido), que por sua vez
importa a previsão de `preditor_pr1.py` (v1, hash conferido).

A **única** diferença em relação à v2 é a identificação e a validação das entradas, exigida pelo passe de completude
D3: a execução original dos zeros foi reprovada em V1 e V2 (o manifesto reprovado é preservado), e o dado analisado é
a lista corrigida, com manifesto próprio. Ver ADENDO_H004_2 §5.

Exige, por caractere, em `--dados`:
  zeros_<caractere>_12000_completo.txt   e   manifesto_d3_<caractere>.json
e confere: (1) SHA-256 do arquivo analisado igual ao campo `saida.sha256` do manifesto; (2) no manifesto,
`certificado_final.passed` e as verificações V1, V2, V3 e V4 todas verdadeiras; (3) bordas A e B de
`block_metrics.json` iguais às do arquivo analisado (10⁻⁹); (4) catálogo do controle idêntico ao do preditor.

Uso (da raiz, depois da execução do controle):
  .venv/bin/python3 results/registro_hipoteses/H-004/preditor_pr1_v3.py \
      --controle <pasta do instrumento_chi> --dados results/etapa11_6_controles/dirichlet/completude --saida <json>
  .venv/bin/python3 results/registro_hipoteses/H-004/preditor_pr1_v3.py --congelar-dependencias
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))

V2_SHA256 = "cc14e12f775e3fd08c5d2a8e09cb0e81581f3b3595b731b9a1ea9d340dcd0c46"
DEPS_FILE = HERE / "dependencias_v3.json"
CHECKS_REQUIRED = ("V1", "V2", "V3", "V4")
# arquivos que a varredura de módulos carregados não vê (não são .py importados) e que a execução também confere:
# a configuração do controle e o código que produziu o conjunto de dados, além dos três avaliadores.
EXTRA_FILES = ("results/etapa11_6_controles/dirichlet/ctrl_dirichlet_v1.toml",
               "results/etapa11_6_controles/dirichlet/completude/completude_d3.py",
               "results/registro_hipoteses/H-004/preditor_pr1.py",
               "results/registro_hipoteses/H-004/preditor_pr1_v2.py",
               "results/registro_hipoteses/H-004/preditor_pr1_v3.py")


def _import_v2():
    import preditor_pr1_v2 as v2
    if v2.sha256(HERE / "preditor_pr1_v2.py") != V2_SHA256:
        raise SystemExit("preditor_pr1_v2.py difere do hash declarado no ADENDO_H004_2; avaliação abortada")
    return v2


V2 = _import_v2()
sha256, BLOCKS, SEEDS, classify = V2.sha256, V2.BLOCKS, V2.SEEDS, V2.classify_v2


def extra_hashes() -> dict:
    """SHA-256 dos arquivos do EXTRA_FILES; erro explícito se algum faltar."""
    out = {}
    for rel in EXTRA_FILES:
        f = ROOT / rel
        if not f.exists():
            raise SystemExit(f"dependência declarada ausente: {rel}")
        out[rel] = sha256(f)
    return out


def current_dependencies() -> dict:
    mods = V2.loaded_repo_modules()
    mods[str(Path(__file__).resolve().relative_to(ROOT))] = sha256(Path(__file__))
    return {"modules": mods, "arquivos": extra_hashes()}


def dependency_diff(frozen: dict, now: dict) -> dict:
    """Diferenças nas duas seções; dicionário vazio significa que tudo bate."""
    diff = {}
    for section in ("modules", "arquivos"):
        a, b = frozen.get(section, {}) or {}, now.get(section, {}) or {}
        for k in sorted(set(a) | set(b)):
            if a.get(k) != b.get(k):
                diff[f"{section}/{k}"] = {"congelado": a.get(k), "agora": b.get(k)}
    return diff


def dataset_files(data_dir: Path, ch: str) -> tuple:
    return data_dir / f"zeros_{ch}_12000_completo.txt", data_dir / f"manifesto_d3_{ch}.json"


def preconditions_d3(control_dir: Path, data_dir: Path, P, ic, dz) -> tuple:
    """Mesma estrutura da v2, com a identidade do conjunto de dados do passe D3 (ADENDO_H004_2 §5)."""
    notes, ok = [], True
    zeros = {}
    for ch in ("chi_m4", "chi_5"):
        zf, man = dataset_files(data_dir, ch)
        if not (zf.exists() and man.exists()):
            return False, notes + [f"{ch}: lista corrigida ou manifesto D3 ausente"], None
        m = json.loads(man.read_text(encoding="utf-8"))
        if m.get("saida", {}).get("sha256") != sha256(zf):
            return False, notes + [f"{ch}: SHA-256 do arquivo analisado difere do manifesto D3"], None
        if m.get("n_trabalho") != 12000:
            return False, notes + [f"{ch}: manifesto D3 não declara 12.000 zeros de trabalho"], None
        if not m.get("certificado_final", {}).get("passed"):
            ok = False
            notes.append(f"{ch}: certificado D3-C1 não fecha no manifesto")
        checks = m.get("verificacoes", {})
        for k in CHECKS_REQUIRED:
            if k not in checks:
                ok = False
                notes.append(f"{ch}: {k} ausente no manifesto D3")
            elif not checks[k].get("passed"):
                ok = False
                notes.append(f"{ch}: {k} reprovada no manifesto D3")
        zeros[ch] = np.loadtxt(zf, dtype=np.float64)
        if len(zeros[ch]) != 12000:
            return False, notes + [f"{ch}: arquivo analisado não tem 12.000 zeros"], None
        cat_periods = [c["period_theoretical"]
                       for c in ic.chi_catalog_module(dz.CHARACTERS[ch]).prime_power_catalog(0.5, 5.0)]
        for name, i0, i1 in BLOCKS[ch]:
            bd = control_dir / name
            if not ((bd / "arithmetic_matches.csv").exists() and (bd / "block_metrics.json").exists()):
                return False, notes + [f"{name}: saída do controle ausente"], None
            bm = json.loads((bd / "block_metrics.json").read_text(encoding="utf-8"))
            g = zeros[ch][i0 - 1:i1]
            if abs(bm["instrument"]["A"] - g[0]) > 1e-9 or abs(bm["instrument"]["B"] - g[-1]) > 1e-9:
                return False, notes + [f"{name}: bordas do controle diferem do arquivo analisado"], None
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
    P, ic, dz = V2._import_chain()
    if a.congelar_dependencias:
        dep = current_dependencies()
        DEPS_FILE.write_text(json.dumps(dep, indent=2, sort_keys=True), encoding="utf-8")
        print(json.dumps({"congelado_em": DEPS_FILE.name, "n_modulos": len(dep["modules"]),
                          "arquivos": dep["arquivos"]}, indent=2, ensure_ascii=False))
        return 0
    if not DEPS_FILE.exists():
        print(json.dumps({"verdict": "abortado", "reason": "dependencias_v3.json ausente"}, indent=2))
        return 2
    frozen = json.loads(DEPS_FILE.read_text(encoding="utf-8"))
    now = current_dependencies()
    diff = dependency_diff(frozen, now)
    if diff:
        print(json.dumps({"verdict": "abortado", "reason": "dependências mudaram", "differences": diff}, indent=2))
        return 2
    ok, notes, zeros = preconditions_d3(a.controle, a.dados, P, ic, dz)
    blocks = {}
    if ok and zeros is not None:
        for ch, blist in BLOCKS.items():
            zf, _ = dataset_files(a.dados, ch)
            blocks.update(P.evaluate_dirichlet(a.controle, zf, ch,
                                               [{"name": n, "first_index": i0, "last_index": i1} for n, i0, i1 in blist],
                                               seed=SEEDS[ch]))
    cls = classify(blocks, ok and zeros is not None, notes)
    out = {"avaliador": "v3 (ADENDO_H004_2)",
           "dependencies": {"ok": True, "n_modules": len(now["modules"]), "arquivos": now["arquivos"]},
           "conjunto_de_dados": {ch: {"arquivo": str(dataset_files(a.dados, ch)[0]),
                                      "sha256": sha256(dataset_files(a.dados, ch)[0])}
                                 for ch in BLOCKS if dataset_files(a.dados, ch)[0].exists()},
           "preconditions_ok": ok, "notes": notes, "blocks": blocks, "classification": cls}
    if a.saida:
        a.saida.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"preconditions_ok": ok, "notes": notes, "classification": cls}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
