# Orçamento medido do instrumento `ctrl-dirichlet-v1` e mapa de dependências da H-004 (25/09/2026)

Pedido do usuário em 25/09/2026, sob o `ADENDO_REGISTRO_v2_2` (`0b505348…`) e suas erratas 1 (`b56b0470…`) e 2
(`9deef4f6…`). **Nenhum bloco reservado foi aberto e nenhum zero real foi lido.** SHA-256 deste documento em
`ORCAMENTO_INSTRUMENTO.sha256`.

## 1. Método

- **Níveis sintéticos.** As bordas de cada bloco vêm de N̄_χ⁻¹ nos índices do bloco, que estão em
  `ctrl_dirichlet_v1.toml`; os níveis são substitutos GUE com a mesma contagem (3.000), a mesma densidade e a mesma
  grade. Script: `bench_instrumento_chi.py`. O prefixo do vetor de entrada existe só porque `run_block_chi` fatia
  `gammas[i0−1:i1]`, e é preenchido pela contagem suave; nunca entra no bloco.
- **Etapas medidas separadamente** pelos cronômetros que o próprio instrumento grava: construção/transformada
  (`instrument`), nulo shuffle, nulo GUE, calibração sintética e comparação aritmética (ajuste dirigido, controle de
  fase e perturbações de precisão).
- **Cinco execuções** com as realizações reduzidas por um fator, para ajustar custo = intercepto + coeficiente ×
  número de realizações e extrapolar às contagens declaradas. `OMP_NUM_THREADS=1` e CPU medida por `getrusage`.
- **Contenção:** as medições correram com três processos pesados na máquina (V2′ de χ₋₄, passe D3 de χ₅ e o diagnóstico
  do estádio) em 4 núcleos. Isso infla os tempos; o orçamento abaixo é, por isso, conservador.

## 2. Medições

| execução | escala | shuffle (realiz.) | GUE | sintética | aritmética (fase, precisão) | CPU total |
|---|---|---|---|---|---|---|
| e02 | 0,01 | 3,49 s (204) | 5,84 s (8) | 3,21 s (2) | 14,53 s (10, 2) | 22,1 s |
| e02 | 0,05 | 16,54 s (1.010) | 11,71 s (15) | 3,42 s (2) | 11,05 s (50, 2) | 35,7 s |
| e02 | 0,25 | 88,09 s (5.050) | 64,35 s (75) | 18,42 s (10) | 21,46 s (250, 5) | 148,7 s |
| e02 | 0,50 | 169,68 s (10.100) | 111,18 s (150) | 28,49 s (20) | 36,77 s (500, 10) | 288,0 s |
| f04 (χ₅) | 0,05 | 22,67 s (1.010) | 12,45 s (15) | 3,63 s (2) | 9,91 s (50, 2) | 33,5 s |

## 3. Ajustes por etapa e extrapolação a um bloco

| etapa | custo unitário ajustado | rms do ajuste | contagem declarada | segundos por bloco |
|---|---|---|---|---|
| construção + transformada | custo fixo | — | — | ~1,1 |
| nulo shuffle | 0,0169 s/realização (e02); **0,0225 s (f04)** | 1,4 s | 200 + 9.999 + 9.999 | **341** (e02) a **453** (f04) |
| nulo GUE | 0,748 s/realização | 3,7 s | 100 + 199 | **226** |
| calibração sintética | 1,43 s/realização | 1,7 s | 40 | **58** |
| comparação aritmética | 3,0 s/perturbação de precisão | 1,2 s | 20 perturbações, 999 de fase | **67** |

Sobre a aritmética: o coeficiente do controle de fase saiu **negativo** (−0,036 s) no ajuste de duas variáveis, ou seja
o termo de fase está **abaixo do ruído de medição** e não foi resolvido. O valor da tabela vem do ajuste só em
perturbações de precisão (intercepto 6,7 s + 3,0 s × 20 = 66,6 s), que é o mais defensável. Quem manda na etapa são as
20 perturbações de precisão, não as 999 realizações de fase.

**Extrapolação:** o maior ponto medido tem metade das realizações declaradas em todas as etapas, então a extrapolação é
de fator 2, não de ordens de grandeza.

## 4. Orçamento dos 8 blocos

| | CPU acumulada | parede, 1 processo | parede, 4 trabalhadores |
|---|---|---|---|
| melhor caso (custo do e02) | **1,55 h** | 1,55 h | ~0,39 h |
| pior caso (custo do f04 no shuffle) | **1,8 h** | 1,8 h | ~0,45 h |
| com margem de ±30% sobre o pior caso | **1,3 a 2,4 h** | idem | ~0,6 h |

- **Fica abaixo do limiar de 4 horas-CPU** do §2 do adendo, ou seja **não é produção longa** pela nossa própria
  definição; os quatro requisitos do §3 não são exigidos, e vale a declaração normal do controle, já existente.
- **Retomada:** a granularidade é **por bloco**. `instrumento_chi.py` aceita `--blocos` e cada bloco grava a própria
  pasta (`blind_peaks.csv`, `nulls.npz`, `freeze.json`, `arithmetic_matches.csv`, `block_metrics.json`). **Não há
  checkpoint dentro do bloco:** uma interrupção no meio de um bloco perde aquele bloco (no máximo ~14 min de CPU) e
  nada dos anteriores. As sementes vêm de `SeedSequence(seed)` com `spawn` por posição do bloco na lista declarada, e o
  código seleciona a semente pela posição, não pela ordem de execução — reexecutar um bloco isolado reproduz o mesmo
  resultado.

## 5. Mapa de dependências da H-004

O preditor congelado (`preditor_pr1_v2.py`, `cc14e12f…`, e `preditor_pr1.py`) usa, por bloco:

| entrada | arquivo | etapa que a produz |
|---|---|---|
| `fit_coefficient_real`, `coefficient_theoretical`, `period_theoretical` | `arithmetic_matches.csv` | **comparação aritmética** |
| bordas A e B (conferidas contra o arquivo de zeros) | `block_metrics.json` | construção do instrumento |
| ordenadas do bloco | arquivo de zeros | — |
| ruído de arredondamento | recalculado pelo preditor (≈20 reajustes por bloco) | — |
| `all_checks_passed` e SHA-256 do arquivo de zeros | `manifest_<caractere>_12000.json` | pré-condição |

**Pertencem só ao controle:** nulo shuffle (20.198 realizações), nulo GUE (299), calibração sintética (40) e o detector
cego — eles alimentam os critérios D-C* sobre detecção sem catálogo, que a H-004 não usa.

**Custo do caminho dirigido hipotético** (construção + aritmética nos 6 blocos reservados, com o mínimo de nulo para a
aritmética rodar): **≈ 0,15 hora-CPU**, contra **1,55 a 1,8 h** do controle completo nos 8 blocos. A economia é de
menos de 2 horas-CPU e custaria um adendo, uma verificação de equivalência com o estimador declarado em dados antigos e
sintéticos, e código novo. **Não se justifica.** Recomendação: executar o controle como declarado.

## 6. Bloqueio que não é de custo

A pré-condição do preditor exige `manifest_<caractere>_12000.json` com `all_checks_passed: true` e `output_sha256`
igual ao do arquivo de zeros do mesmo diretório. O manifesto da execução original está com **false** e continuará — é o
registro do resultado reprovado (`ADENDO_DIRICHLET_3` §2) —, e o dado corrigido tem outro nome
(`zeros_chi_m4_12000_completo.txt`) e outro manifesto (`manifesto_d3_chi_m4.json`). **Nenhum arquivo será renomeado.**
Antes de rodar o instrumento é preciso um adendo à H-004 declarando qual é o conjunto de dados, com nomes e hashes, e
como a pré-condição é verificada sobre ele. Enquanto isso não existir, a H-004 fica `não executada` por pré-condição, e
não por orçamento.

## 7. O que este orçamento não estabelece

Não é análise de poder: não diz nada sobre a probabilidade de a H-004 ter sucesso, nem sobre os critérios D-C* do
controle. As ~83 linhas selecionáveis da triagem indicam material potencialmente informativo e **não** demonstram o
poder da decisão da H-004. O orçamento também não vale para outra configuração: mudar contagens, blocos ou faixa exige
medir de novo.

*Dionatan Resende & Claude Opus — 25/09/2026.*
