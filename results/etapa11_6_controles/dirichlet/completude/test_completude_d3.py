"""
Testes obrigatórios do passe D3 (ADENDO_DIRICHLET_3.md §6, `02340a5c…`). Rodam antes de qualquer execução.

Sem rede. Dois testes avaliam Z_χ de verdade perto de t ≈ 3.900 e levam ~1 min cada; os outros são instantâneos.
Onde o teste usa região ou passo menores que os de produção, isso está dito no próprio teste: a regra de produção é a
do adendo §3, e o que se testa aqui é o invariante (detectar o degrau e recuperar o par), não o custo.

  .venv/bin/python3 -m pytest results/etapa11_6_controles/dirichlet/completude/test_completude_d3.py -q
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

import completude_d3 as cd
import dirichlet_zeros as dz

CH = dz.CHARACTERS["chi_m4"]
ZEROS = Path(__file__).resolve().parents[3] / "etapa11_6_controles" / "dados" / "zeros_chi_m4_12000.txt"
PAR_CONHECIDO = (3893.887460453, 3893.977078497)     # diagnóstico de 22/09/2026, intervalo do adendo §1


@pytest.fixture(scope="module")
def zeros():
    return [float(x) for x in np.loadtxt(ZEROS)]


def test_par_conhecido(zeros):
    """§6.1 — no intervalo declarado o passe acha exatamente os dois zeros do diagnóstico."""
    i = next(k for k, z in enumerate(zeros) if abs(z - 3893.1962) < 1e-3)
    found = cd.rescan_gap(CH, zeros[i], zeros[i + 1], cd.SCALE_A)
    assert len(found) == 2
    for got, esperado in zip(found, PAR_CONHECIDO):
        assert abs(got - esperado) < 1e-8


def test_invariancia_da_insercao(zeros):
    """§6.2 — a lista original é subconjunto ordenado da saída; nada é movido nem apagado."""
    corrigida = cd.merge(zeros, list(PAR_CONHECIDO))
    assert len(corrigida) == len(zeros) + 2
    assert corrigida == sorted(corrigida)
    it = iter(corrigida)
    assert all(any(abs(c - z) < 1e-15 for c in it) for z in zeros[:50])   # subsequência, na ordem
    assert set(zeros).issubset(set(corrigida))


def test_theta_bate_com_o_script_congelado(zeros):
    """§6.4 — S vem do mesmo θ do módulo congelado."""
    amostra = zeros[::1500]
    S = cd.s_values(amostra, CH)
    for k, t in enumerate(amostra):
        assert abs((k + 1 - dz.smooth_count(t, CH)) - S[k]) < 1e-12


def test_certificado_sem_degrau_em_trecho_completo(zeros):
    """Controle do certificado: num trecho sem déficit (índices 1–3.000) ele passa."""
    cert = cd.certificate(cd.s_values(zeros[:3000], CH))
    assert cert["passed"]
    assert cert["internal_spread"] < 0.1


def test_degrau_detectado_e_par_recuperado(zeros):
    """
    §6.3 — invariante: removendo um par conhecido, o certificado acusa degrau de −2 na janela certa e a Etapa C
    recupera os dois zeros. Região e passo reduzidos (8 intervalos, d̄/32) só para caber no orçamento do teste.
    """
    i = next(k for k, z in enumerate(zeros) if abs(z - 3893.1962) < 1e-3)
    trecho = cd.merge(zeros[i - 322:i + 278], list(PAR_CONHECIDO))     # 600 zeros, par na posição ~322
    com_falta = [z for z in trecho if z not in PAR_CONHECIDO]
    cert_ok = cd.certificate(cd.s_values(trecho, CH))
    cert_falta = cd.certificate(cd.s_values(com_falta, CH))
    assert cert_ok["passed"] and not cert_falta["passed"]
    assert len(cert_falta["steps"]) == 1
    passo = cert_falta["steps"][0]
    assert passo["deficit"] == 2
    assert passo["index_range"][0] <= 322 <= passo["index_range"][1]
    rec, log = cd.stage_c(CH, com_falta, cert_falta, region_override=(318, 326), rounds=((1.1, cd.SCALE_A),))
    assert len(rec) == 2
    for got, esperado in zip(sorted(rec), PAR_CONHECIDO):
        assert abs(got - esperado) < 1e-8
    assert cd.certificate(cd.s_values(cd.merge(com_falta, rec), CH))["passed"]
