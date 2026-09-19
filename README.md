# hipotese-riemann — espectroscopia inversa dos zeros da zeta

**English summary.** Reproducibility package for a computer-assisted, *conditional* certification of windowed inverse
spectroscopy of Riemann zeta zeros. For the primary estimator of the frozen M4 pipeline (Hann window, conjugate-lobe
band fit), cut (d₁, Δ) = (8, 2) and 30 blocks of 3,000 zeros (indices 10,001–100,000), interval-arithmetic bounds show
that the recorded per-line ratio `fit_ratio_to_theory` satisfies |r̂_k − 1| ≤ 10⁻⁶ on all 461 eligible lines, linking the
windowed transform to the von Mangoldt prime-power coefficients through the Guinand–Weil explicit formula. This holds
**conditionally on RH** and on the table-fidelity hypothesis **H-tab** (declared accuracy 3·10⁻⁹ of the zero table),
within a declared computational trust base. The explicit formula is taken from Connes' Theorem 6 (read); Jensen's
formula is now checked in Titchmarsh, *The Theory of Functions* (1939), §3.61 (J1 resolved, 17/09/2026); Weil's original
1952 statement (F5) is still a pending bibliographic check, not an additional hypothesis. The numerical-fidelity part (N) is
unconditional. The cut was chosen after an exploratory evaluation. This is **not** a proof of RH; the full C2 criterion,
S1/S3a/S3c and H1 remain open; the independent audit has **not** yet been carried out. Documentation is in Portuguese.

**Arquivo permanente (Zenodo):** [doi:10.5281/zenodo.22811040](https://doi.org/10.5281/zenodo.22811040) — cópia imutável
da versão `v1-certified-computer-assisted-verification-package` (commit `e436709`). DOI conceitual, para todas as versões:
[10.5281/zenodo.22811039](https://doi.org/10.5281/zenodo.22811039). Para reproduzir os resultados exatamente como
certificados, use a cópia do DOI de versão; commits posteriores (como o que acrescentou este DOI) não fazem parte dela.

## Estado do certificado (17/09/2026)

- Derivações e resultados: [docs/ETAPA11_3B_H1_CAUDA_PROJETADA.md](docs/ETAPA11_3B_H1_CAUDA_PROJETADA.md) §II.17–§II.24.
- Artefatos, declarações prévias e manifesto de 59 hashes: [results/etapa11_r5/](results/etapa11_r5/)
  (`MANIFESTO_CERT.csv`).
- Protocolo de auditoria independente (ambiente, integridade, ordem e custo de reexecução, pontos forenses):
  [docs/PROTOCOLO_AUDITORIA_CERTIFICADO.md](docs/PROTOCOLO_AUDITORIA_CERTIFICADO.md). **Auditoria ainda não realizada.**

Verificação rápida de integridade (da raiz, após clonar):

```bash
cd results/etapa11_r5 && sha256sum -c <(awk -F, 'NR>1 {print $2"  "$1}' MANIFESTO_CERT.csv)   # esperado: 59 × SUCESSO
```

O repositório usa `.gitattributes` com `* -text` para que o git não altere nenhum byte (vários CSVs usam CRLF e os hashes
dependem dos bytes exatos).

## Dados e fontes

- **Zeros da zeta:** tabela `zeros1` de **Andrew M. Odlyzko** (primeiros 100.000 zeros, precisão declarada 3·10⁻⁹),
  obtida de <https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros1> e redistribuída aqui só para reprodução, com
  atribuição (`data/raw/zeros1`, SHA-256 `3436c916…`; manifestos em `data/raw/`). A página de origem não declara licença
  de redistribuição; esse ponto está registrado como pendência.
- **Fontes bibliográficas consultadas** (PDFs do arXiv, SIAM Review, páginas da DLMF): **não** são redistribuídas.
  [archive/fontes_etapa11/MANIFESTO.csv](archive/fontes_etapa11/MANIFESTO.csv) registra URL, versão, data e SHA-256 de cada
  uma, para conferência dos mesmos bytes.
- **Licença do código:** MIT ([LICENSE](LICENSE)).

---

Este projeto parte de um prompt de pesquisa original (não publicado neste repositório) para investigar quais informações espectrais e aritméticas podem ser recuperadas dos zeros da função zeta. O primeiro objetivo científico será um experimento reproduzível com 10.000 zeros, controles estatísticos e detecção de períodos sem consultar previamente um catálogo de primos.

**Estado (19/09/2026):** Etapas 0–10 validadas (M1–M4, zeros 1–100.000). Etapa 11 em execução: matriz de classes de operadores com evidências conferidas, subetapa 11.3b encerrada com itens abertos registrados e controles da 11.6 em preparação. Resumo e próxima tarefa em [docs/ESTADO_ATUAL.md](docs/ESTADO_ATUAL.md).

**Registro anterior (14/09/2026):** M1–M3 executados com 10.000 zeros (protocolo m3-v3, após a auditoria de [docs/ANALISE_RESULTADOS.md](docs/ANALISE_RESULTADOS.md)). Etapa 10 de M4 concluída; Etapa 11 (classes de operadores) pendente: zeros 10.001–40.000 (m4-v1) e 40.001–70.000 (m4-v2, replicação com o mesmo código e as mesmas regras) analisados sob protocolos pré-registrados. Auditoria por implementação independente em três blocos: [docs/AUDITORIA_INDEPENDENTE.md](docs/AUDITORIA_INDEPENDENTE.md). A faixa 70.001–100.000 foi analisada em m4-v3 (implementação primária + reprodução independente). C1 e C2 foram replicados em 10/10 blocos; a regra R2 foi acionada por um erro de desenho do plano e investigada. Ver [relatório consolidado, §5 e §9](docs/RELATORIO_CONSOLIDADO.md). Estado detalhado e evidências em [docs/ANDAMENTO.md](docs/ANDAMENTO.md). O laboratório complementar de Collatz está planejado, ainda sem execução.

## Documentos

- **Ponto de retomada (estado atual, regras e próxima tarefa): [docs/ESTADO_ATUAL.md](docs/ESTADO_ATUAL.md).**

- [Plano de implementação](PLANO_IMPLEMENTACAO.md): etapas, fórmulas, entregáveis, testes e critérios para avançar.
- [Plano complementar Collatz](docs/PLANO_COLLATZ.md): etapas CL0–CL5 para zetas dinâmicas, filtros aritméticos, operadores e limites da reconstrução inversa; primeira entrega proposta: CL0–CL1.
- Instruções de trabalho do agente (`AGENTS.md`) e prompt original (`prompt.txt`): mantidos fora do repositório público; as regras científicas relevantes estão refletidas no plano e em `docs/ANDAMENTO.md`.

## Ordem de trabalho

1. Preparar o protocolo, a estrutura de código e a base de zeros.
2. Validar os controles e os estimadores de estatística espectral.
3. Recuperar períodos a partir das ordenadas originais dos zeros.
4. Comparar os períodos encontrados com primos e suas potências, medindo erros e significância.
5. Ampliar a análise, procurar falhas e avaliar classes de operadores.
6. Experimentar Hamiltonianos apenas após validar os instrumentos de análise.

A primeira entrega cobre as etapas 0–3 do plano: ambiente reproduzível, dados auditados e geradores de controle. O experimento mínimo completo cobre as etapas 0–9. A conclusão da investigação exige também as etapas 10–13, com registro explícito de extensões não executadas.

## Comandos disponíveis

```bash
python -m venv .venv && .venv/bin/pip install -r requirements.txt && .venv/bin/pip install -e .
.venv/bin/python -m pytest -q                                   # testes rápidos, sem rede

.venv/bin/python -m riemann_spectra data fetch    --config configs/main.toml
.venv/bin/python -m riemann_spectra data validate --config configs/main.toml

.venv/bin/python -m riemann_spectra run --config configs/pilot.toml --milestone M2 --workers 4
.venv/bin/python -m riemann_spectra run --config configs/main.toml  --milestone M2 --workers 4   # ~17 min

.venv/bin/python -m riemann_spectra data validate --config configs/main.toml --force-new-record   # ~1 min

.venv/bin/python -m riemann_spectra m3 --config configs/m3_protocol_v3.toml --blocks pilot,dev,val --workers 4      # ~6 min
.venv/bin/python -m riemann_spectra protocol freeze --config configs/m3_protocol_v3.toml
.venv/bin/python -m riemann_spectra m3 --config configs/m3_protocol_v3.toml --blocks holdout,full --workers 4       # exige lock idêntico; ~20 min
.venv/bin/python -m riemann_spectra m3 --config configs/m3_protocol_v3_bh.toml --blocks pilot,dev,val,holdout,full --workers 4  # variante BH

# M4 (m4-v1): dados até 40.000, congelamento e execução
.venv/bin/python -m riemann_spectra data fetch    --config configs/data_first40000.toml
.venv/bin/python -m riemann_spectra data validate --config configs/data_first40000.toml
.venv/bin/python -m riemann_spectra m3  --config configs/m4_v1.toml    --blocks b01,b02,b03,b04,b05,b06,b07,b08,b09,b10 --workers 4  # ~55 min
.venv/bin/python -m riemann_spectra m3  --config configs/m4_v1_bh.toml --blocks b01,b02,b03,b04,b05,b06,b07,b08,b09,b10 --workers 4  # ~30 min
.venv/bin/python -m riemann_spectra run --config configs/m4_v1_m2.toml --milestone M2 --workers 4                                  # ~70 min

# M4 (m4-v2): replicação em 40.001–70.000 (configs/data_first70000.toml, m4_v2*.toml; blocos c01..c10)
.venv/bin/python results/analysis_m4_v1_v2_comparacao/compare_m4_v1_v2.py

.venv/bin/python -m riemann_spectra report --run-id <ID>
```

Cada execução cria `results/<run_id>/` com `manifest.json` (hashes de dados, configuração e módulos; ambiente),
`config_resolved.toml`, `metrics.json`, `report.md`, `tables/`, `figures/` e `logs/`.
