"""
Testes do avaliador v3 (ADENDO_H004_2 §5). Mostram que a mudança em relação à v2 **se limita à identificação e à
validação das entradas**: a análise é a mesma, e sobre entradas equivalentes as duas versões produzem a seção
`blocks` idêntica. Sem rede, sem dado real: os zeros são substitutos e as saídas do controle são fabricadas.

Os blocos são reduzidos por monkeypatch (2 blocos de 300 níveis) só para o teste caber em segundos; os blocos
declarados da H-004 continuam os da declaração.

  .venv/bin/python3 -m pytest results/registro_hipoteses/H-004/test_preditor_v3.py -q
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import numpy as np
import pytest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "results/etapa11_6_controles/dirichlet"))

import preditor_pr1_v2 as v2  # noqa: E402
import preditor_pr1_v3 as v3  # noqa: E402

TEST_BLOCKS = {"chi_m4": [("t01", 1, 300), ("t02", 301, 600)],
               "chi_5": [("u01", 1, 300), ("u02", 301, 600)]}


def surrogate_zeros(ch, ic, n=12000):
    """Níveis substitutos a partir da contagem suave; nenhum zero real."""
    return ic.fold_chi(np.arange(1.0, n + 1.0) + 0.25 * np.sin(np.arange(1.0, n + 1.0)), ch.q, ch.kappa)


@pytest.fixture(scope="module")
def cenario(tmp_path_factory):
    P, ic, dz = v2._import_chain()
    base = tmp_path_factory.mktemp("v3")
    control, dados_v2, dados_v3 = base / "controle", base / "dados_v2", base / "dados_v3"
    for d in (control, dados_v2, dados_v3):
        d.mkdir(parents=True, exist_ok=True)
    for chname, blist in TEST_BLOCKS.items():
        ch = dz.CHARACTERS[chname]
        g = surrogate_zeros(ch, ic)
        txt = "\n".join(f"{x:.9f}" for x in g) + "\n"
        zf2 = dados_v2 / f"zeros_{chname}_12000.txt"
        zf3 = dados_v3 / f"zeros_{chname}_12000_completo.txt"
        zf2.write_text(txt, encoding="utf-8")
        zf3.write_text(txt, encoding="utf-8")            # mesmo conteúdo: a análise tem de dar o mesmo
        sha = v2.sha256(zf2)
        (dados_v2 / f"manifest_{chname}_12000.json").write_text(json.dumps(
            {"n_zeros": 12000, "all_checks_passed": True, "output_sha256": sha}), encoding="utf-8")
        (dados_v3 / f"manifesto_d3_{chname}.json").write_text(json.dumps(
            {"n_trabalho": 12000, "saida": {"sha256": sha}, "certificado_final": {"passed": True},
             "verificacoes": {k: {"passed": True} for k in ("V1", "V2", "V3", "V4")}}), encoding="utf-8")
        cat = ic.chi_catalog_module(ch).prime_power_catalog(0.5, 5.0)
        for name, i0, i1 in blist:
            bd = control / name
            bd.mkdir(parents=True, exist_ok=True)
            sub = g[i0 - 1:i1]
            (bd / "block_metrics.json").write_text(json.dumps(
                {"instrument": {"A": float(sub[0]), "B": float(sub[-1])}}), encoding="utf-8")
            with open(bd / "arithmetic_matches.csv", "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["period_theoretical", "coefficient_theoretical", "fit_coefficient_real"])
                for j, c in enumerate(cat):
                    ct = float(c["coefficient_theoretical"])
                    w.writerow([repr(float(c["period_theoretical"])), repr(ct), repr(ct + 1e-9 * (1 + j % 3))])
    return {"P": P, "ic": ic, "dz": dz, "control": control, "dados_v2": dados_v2, "dados_v3": dados_v3}


def _blocks(module, precond, control, dados, cenario, zeros_name):
    ok, notes, zeros = precond(control, dados, cenario["P"], cenario["ic"], cenario["dz"])
    assert ok is True and notes == [], notes      # pré-condições válidas: nada de comparar saídas bloqueadas
    assert zeros is not None and all(len(v) == 12000 for v in zeros.values())
    out = {}
    for chname, blist in TEST_BLOCKS.items():
        zf = dados / zeros_name.format(ch=chname)
        out.update(cenario["P"].evaluate_dirichlet(
            control, zf, chname, [{"name": n, "first_index": i0, "last_index": i1} for n, i0, i1 in blist],
            seed=module.SEEDS[chname]))
    return out


def test_v3_reusa_a_analise_da_v2():
    """A mudança é de carregamento: v3 aponta para os mesmos objetos de análise da v2."""
    assert v3.classify is v2.classify_v2
    assert v3.SEEDS is v2.SEEDS
    own = {n for n, o in vars(v3).items() if callable(o) and getattr(o, "__module__", "") == "preditor_pr1_v3"}
    assert own == {"_import_v2", "extra_hashes", "current_dependencies", "dependency_diff",
                   "dataset_files", "preconditions_d3", "main"}, own


def test_equivalencia_das_secoes_blocks(cenario, monkeypatch):
    monkeypatch.setattr(v2, "BLOCKS", TEST_BLOCKS)
    monkeypatch.setattr(v3, "BLOCKS", TEST_BLOCKS)
    b2 = _blocks(v2, v2.preconditions, cenario["control"], cenario["dados_v2"], cenario, "zeros_{ch}_12000.txt")
    b3 = _blocks(v3, v3.preconditions_d3, cenario["control"], cenario["dados_v3"], cenario,
                 "zeros_{ch}_12000_completo.txt")
    # as duas versões chegaram à análise e produziram resultado não vazio
    assert set(b2) == set(b3) == {"t01", "t02", "u01", "u02"}
    for name, v in b3.items():
        for k in ("e_obs", "e_prev", "noise"):
            arr = np.asarray(v[k], dtype=float)
            assert arr.size > 0, (name, k)
            assert np.all(np.isfinite(arr)), (name, k)
        assert np.all(np.asarray(v["noise"], dtype=float) > 0), name
        assert v["metrics"] is not None
    assert any(int(np.sum(np.asarray(v["selected"], dtype=bool))) > 0 for v in b3.values()), \
        "nenhuma linha selecionada em bloco algum: equivalência sem análise efetiva"
    assert json.dumps(b2, sort_keys=True) == json.dumps(b3, sort_keys=True)


def test_v3_rejeita_hash_que_nao_corresponde(cenario, monkeypatch, tmp_path):
    monkeypatch.setattr(v3, "BLOCKS", TEST_BLOCKS)
    d = tmp_path / "dados_ruins"
    d.mkdir()
    for chname in TEST_BLOCKS:
        src = cenario["dados_v3"] / f"zeros_{chname}_12000_completo.txt"
        (d / src.name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        man = json.loads((cenario["dados_v3"] / f"manifesto_d3_{chname}.json").read_text(encoding="utf-8"))
        man["saida"]["sha256"] = "0" * 64
        (d / f"manifesto_d3_{chname}.json").write_text(json.dumps(man), encoding="utf-8")
    ok, notes, zeros = v3.preconditions_d3(cenario["control"], d, cenario["P"], cenario["ic"], cenario["dz"])
    assert ok is False and zeros is None and any("SHA-256" in n for n in notes)


@pytest.mark.parametrize("quebra", ["V2_reprovada", "V2_ausente", "certificado_falso"])
def test_v3_exige_as_cinco_verificacoes(cenario, monkeypatch, tmp_path, quebra):
    monkeypatch.setattr(v3, "BLOCKS", TEST_BLOCKS)
    d = tmp_path / f"dados_{quebra}"
    d.mkdir()
    for chname in TEST_BLOCKS:
        src = cenario["dados_v3"] / f"zeros_{chname}_12000_completo.txt"
        (d / src.name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        man = json.loads((cenario["dados_v3"] / f"manifesto_d3_{chname}.json").read_text(encoding="utf-8"))
        if quebra == "V2_reprovada":
            man["verificacoes"]["V2"]["passed"] = False
        elif quebra == "V2_ausente":
            del man["verificacoes"]["V2"]
        else:
            man["certificado_final"]["passed"] = False
        (d / f"manifesto_d3_{chname}.json").write_text(json.dumps(man), encoding="utf-8")
    ok, notes, _ = v3.preconditions_d3(cenario["control"], d, cenario["P"], cenario["ic"], cenario["dz"])
    assert ok is False and notes


def test_v3_rejeita_bordas_diferentes(cenario, monkeypatch, tmp_path):
    monkeypatch.setattr(v3, "BLOCKS", {"chi_m4": [("t01", 1, 300)], "chi_5": [("u01", 1, 300)]})
    control = tmp_path / "controle_ruim"
    for name in ("t01", "u01"):
        bd = control / name
        bd.mkdir(parents=True)
        for f in ("block_metrics.json", "arithmetic_matches.csv"):
            (bd / f).write_text((cenario["control"] / name / f).read_text(encoding="utf-8"), encoding="utf-8")
        bm = json.loads((bd / "block_metrics.json").read_text(encoding="utf-8"))
        bm["instrument"]["A"] += 1e-3
        (bd / "block_metrics.json").write_text(json.dumps(bm), encoding="utf-8")
    ok, notes, zeros = v3.preconditions_d3(control, cenario["dados_v3"], cenario["P"], cenario["ic"], cenario["dz"])
    assert ok is False and zeros is None and any("bordas" in n for n in notes)


def test_dependencias_incluem_transitivas_e_configuracao():
    """§ do ADENDO_H004_2 reforçado: a seção `arquivos` cobre v1, v2, v3, a configuração do controle e o código do
    passe D3 — o hash da v2, sozinho, não congela as dependências transitivas."""
    extra = v3.extra_hashes()
    assert set(extra) == set(v3.EXTRA_FILES)
    assert all(len(h) == 64 and all(c in "0123456789abcdef" for c in h) for h in extra.values())
    dep = v3.current_dependencies()
    assert "preditor_pr1.py" in " ".join(dep["modules"]) and "preditor_pr1_v2.py" in " ".join(dep["modules"])
    assert any(k.endswith("instrumento_chi.py") for k in dep["modules"])
    assert v3.dependency_diff(dep, dep) == {}
    adulterado = {"modules": dict(dep["modules"]), "arquivos": dict(dep["arquivos"])}
    alvo = "results/etapa11_6_controles/dirichlet/ctrl_dirichlet_v1.toml"
    adulterado["arquivos"][alvo] = "0" * 64
    d = v3.dependency_diff(adulterado, dep)
    assert list(d) == [f"arquivos/{alvo}"]
