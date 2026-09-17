# Protocolo de auditoria independente — cadeia certificada da Cauda Projetada (Etapa 11.3b)

**Versão:** 1.0 (17/09/2026). **Destinatário:** auditor independente, sem participação na produção do certificado.
**Estado do objeto auditado:** vigente e congelado. Manifesto `results/etapa11_r5/MANIFESTO_CERT.csv`, SHA-256
`2a2cd3bdc4547c090b29c932ee61142e81ca0f06d0eab5a017fec09c38578d19`, 59 entradas.

---

## 0. O que se pede ao auditor

Verificar, sem contato com o autor, se:
1. os artefatos são os registrados (integridade);
2. os scripts, reexecutados num ambiente limpo, reproduzem as tabelas de decisão;
3. o código implementa o que as declarações e as derivações dizem, com atenção especial aos pontos que **já falharam** (§5);
4. as derivações matemáticas que o código usa estão corretas;
5. as afirmações do registro não excedem o que foi estabelecido (§8).

**O que o certificado afirma, em forma curta.** Para o corte (d₁, Δ) = (8, 2) e o estimador primário `band_conjugate` de m4
(30 blocos, zeros 10.001–100.000):
- **(N), incondicional na base de confiança declarada:** o valor registrado `fit_ratio_to_theory` coincide com o estimador
  matemático a_k de M^math aplicado a F^tab a menos de ε_k (≤ 6,27·10⁻¹¹ nas 461 linhas elegíveis).
- **(T), condicional a RH (F5 e J1 bibliográficas) e a H-tab:** |r̂_k − 1| ≤ ε_k + total^γ_k ≤ 10⁻⁶ nas 461/461 linhas
  elegíveis e em 1.024 dos 1.410 pares.

**O que não afirma:**
- prova de RH;
- C2 inteiro (elegibilidade, agregação por fração, critério de fase Q);
- S1, S3a, S3c;
- H1, que continua aberta.

O corte (8, 2) foi escolhido **depois** de uma avaliação exploratória. Detalhes em
`docs/ETAPA11_3B_H1_CAUDA_PROJETADA.md` §II.10–§II.24.

---

## 1. Ambiente

**Ambiente de produção (registrado):**

| Item | Versão |
|---|---|
| SO | Linux 7.0.0-31-generic x86_64, glibc 2.39 |
| CPU | 4 núcleos (x86-64; aritmética SSE/AVX, sem x87) |
| Python | 3.12.3 |
| NumPy | 2.5.3 (BLAS/LAPACK: scipy-openblas 0.3.34) |
| SciPy | 1.18.1 |
| mpmath | 1.4.1 |
| Demais | `requirements.txt` (19 pacotes fixados) |

**Preparação de ambiente limpo:**

```bash
# trabalhar numa CÓPIA do projeto: a reexecução sobrescreve saídas vigentes
cp -a hipotese-riemann hipotese-riemann-auditoria && cd hipotese-riemann-auditoria
rm -rf .venv && python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python3 -c "import sys, numpy, scipy, mpmath; print(sys.version, numpy.__version__, scipy.__version__, mpmath.__version__)"
```

**Todos os comandos rodam da raiz do projeto com `.venv/bin/python3`.** Os scripts usam caminhos relativos à raiz. Com o
Python do sistema, falham por falta de numpy; isso aconteceu uma vez nesta produção.

**Sensibilidade a versão:**
- As decisões usam frações exatas e intervalos, então outra versão de numpy/mpmath deveria dar as mesmas **marcações**.
  Os números exportados podem diferir nos últimos dígitos se o arredondamento dirigido de `mpmath.iv` mudar.
- A reprodução bit a bit de `lstsq` (diagnóstico T29) depende de BLAS/LAPACK.

---

## 2. Integridade

### 2.1 Manifesto do certificado

```bash
cd results/etapa11_r5
sha256sum MANIFESTO_CERT.csv   # esperado: 2a2cd3bd…16470f0 (valor completo no cabeçalho)
sha256sum -c <(awk -F, 'NR>1 {print $2"  "$1}' MANIFESTO_CERT.csv)
for d in DECLARACAO_CERT DECLARACAO_CERT_CORRECAO1 DECLARACAO_CERT_CORRECAO2 DECLARACAO_CERT_RECONF_C1C2 \
         DECLARACAO_CERT_CONTAMINACAO DECLARACAO_CERT_DENSIDADE DECLARACAO_CERT_ORDENADAS DECLARACAO_CERT_NUMERICO; do
  [ "$(sha256sum $d.md | cut -d' ' -f1)" = "$(cut -d' ' -f1 $d.sha256)" ] && echo "ok $d" || echo "DIVERGE $d"; done
```

**Esperado:** 59/59 `SUCESSO` e 8 `ok`. As entradas marcadas "histórico" (execuções substituídas e a rodada 1 de testes de
ρ_ord) também devem conferir.

### 2.2 Entradas fora do manifesto (conferir separadamente)

| Entrada | Como conferir | Esperado |
|---|---|---|
| `data/raw/zeros1` | `sha256sum`; comparar com `data/raw/data_manifest.json` | `3436c916a7878261ac183fd7b9448c9a4736b8bbccf1356874a6ce1788541632` |
| `data/processed/zeros_100k.csv` | `sha256sum`; comparar com `data/raw/manifests/odlyzko_zeros1_first100000.json` e com `data_sha256` do run m4-v3. É lido pelos scripts do certificado (seleção float e T22) | `1af728cf4a1e23c5faacd8f6f0a7547715c8e1103cd4456c28ccc4297d192100` |
| `data/processed/zeros_40k.csv`, `zeros_70k.csv` | `data_sha256` dos runs m4-v1 e m4-v2 (que leram esses arquivos, não o de 100k) | hashes conferem com os manifestos dos runs. **Conferido pelo autor:** valores idênticos, linha a linha, aos de `zeros_100k.csv` |
| Runs de m4: `results/run_20260913_144429_m3_b01*`, `…173045_m3_c01*`, `…220906_m3_d01*` | `manifest.json` de cada run (`config_sha256`, `data_file`, `data_sha256`, `code.modules`, `protocol_lock`); o certificado lê `metrics.json` (A, B, E_c) e `tables/<bloco>/arithmetic_matches.csv` (`fit_ratio_to_theory`) | coerência com os manifestos dos runs |
| `src/riemann_spectra/` | hash de cada módulo contra `code.modules` dos manifestos dos runs | **Conferido pelo autor:** `src/` atual idêntico a m4-v3 em todos os módulos. m4-v1 e m4-v2 diferem só em `periods.py` e `cue.py` (versão anterior; PROTOCOLO §11.2), o que explica T29 |
| Fontes DLMF | `archive/fontes_etapa11/MANIFESTO.csv` (§§5.9, 5.11, 25.2, 25.10; versão 1.2.7) | hashes do manifesto do arquivo |

### 2.3 Limitação: anterioridade das declarações

**O projeto não está sob controle de versão (git) e não tem carimbo de tempo externo.**
- Os scripts verificam o hash de cada declaração ao rodar. Isso prova que o conteúdo da declaração não mudou desde a
  execução.
- **Não prova** que a declaração foi escrita antes do código ou do cálculo.
- A anterioridade é registro do próprio projeto (datas em `docs/ANDAMENTO.md`, `11.md` e §II.17–§II.24). O auditor deve
  tratá-la como **autodeclarada**.

---

## 3. Cadeia das declarações do certificado

| # | Declaração (SHA-256, prefixo) | Objeto | Script / testes | Saídas vigentes | Documento |
|---|---|---|---|---|---|
| 1 | `DECLARACAO_CERT.md` (b7a7980c) | M^math; posto; ‖a_k‖₁; S^abs em (13, 15]; B^{RH″} | `cert_calculo.py` / `cert_testes.py` | `cert_blocos.csv`, `cert_tabela.csv`, `cert_resumo.json` | §II.17 |
| 2 | `DECLARACAO_CERT_CORRECAO1.md` (0a693179) | extremos exatos (Fraction); `W_iv`; decisão exata | idem (T1–T6) | — | §II.18 |
| 3 | `DECLARACAO_CERT_CORRECAO2.md` (75eee940) | binary64: potência, `sup_str`, sqrt, π, finitude; lema de `isum` | idem (T7–T8) | — | §II.19 |
| 4 | `DECLARACAO_CERT_RECONF_C1C2.md` (a8253e9c) | c₁, c₂ recalculados internamente (execução 4 vigente) | idem (T9) | — | §II.20 |
| 5 | `DECLARACAO_CERT_CONTAMINACAO.md` (1d46bced) | P_k em (5, 6] ponto a ponto; C_k em (6, 13] por células; resíduo contra 𝒦 | `cert_contaminacao.py` / `cert_contaminacao_testes.py` (T10–T15) | `cert_contaminacao_*` | §II.21 |
| 6 | `DECLARACAO_CERT_DENSIDADE.md` (6a69c0d7) | ρ_Δ: cota de Binet, janela [A*, B*] | `cert_densidade.py` / `cert_densidade_testes.py` (T16–T21) | `cert_densidade_*` | §II.22 |
| 7 | `DECLARACAO_CERT_ORDENADAS.md` (a3382442) | ρ_ord sob H-tab: Lipschitz, parcela linear de pior caso, borda | `cert_ordenadas.py` / `cert_ordenadas_testes.py` (T22–T27) | `cert_ordenadas_*` (e rodada 1 de testes, histórica) | §II.23 |
| 8 | `DECLARACAO_CERT_NUMERICO.md` (a120c1e2) | ρ_num: X_k = a_k·F^tab, termo suave por momentos, ε_k, (N) e (T), alarme | `cert_numerico.py` / `cert_numerico_testes.py` (T28–T34) | `cert_numerico_*` | §II.24 |

**Execuções substituídas, preservadas para auditoria:**
- `cert_calculo_exec1_pendente.py` e `cert_*_exec1_pendente.*` (**inválida**: enclausuramento);
- `cert_calculo_exec2.py` e `cert_*_exec2.*` (substituída);
- `cert_calculo_exec3.py` e `cert_*_exec3.*` (substituída).

**Contexto anterior, não certificado:** `DECLARACAO.md` (R5), `DECLARACAO_CRUZAMENTO.md`, `DECLARACAO_PRH.md`,
`DECLARACAO_PRH2.md`, `DECLARACAO_THETA.md`, `DECLARACAO_ZDEC.md` e `DECLARACAO_PRH3.md`. São avaliações exploratórias ou
híbridas. **É delas que vem a escolha do corte (8, 2)** (§II.12, §II.16). A conferência declarada de ZDEC **falhou** e ficou
registrada como falha (§II.15.1).

---

## 4. Reexecução: ordem e custo (medido no ambiente de produção)

| Passo | Comando (da raiz, `.venv/bin/python3`) | O que faz | Tempo medido |
|---|---|---|---|
| 1 | verificação de §2 | integridade | segundos |
| 2 | `results/etapa11_r5/cert_numerico_testes.py` | **reaplica em cadeia T1–T34** (cada bateria chama a anterior e restaura os resultados vigentes) | ~15 min |
| 3 | `results/etapa11_r5/cert_calculo.py` | execução 4 (S^abs, B^{RH″}) | ~7 min |
| 4 | `results/etapa11_r5/cert_contaminacao.py --executar` | P_k, C_k | ~20 min |
| 5 | `results/etapa11_r5/cert_densidade.py --executar` | ρ_Δ | < 1 min |
| 6 | `results/etapa11_r5/cert_ordenadas.py --executar` | ρ_ord (~1,27·10⁶ pares zero × nó por bloco) | **~2 h** |
| 7 | `results/etapa11_r5/cert_numerico.py --executar` | ρ_num (mesma ordem de pares) | **~1,5 h** |

**Observações:**
- **Cada passo lê as saídas dos anteriores.** Rodar fora de ordem mistura saídas vigentes com regeneradas.
- **Tempos de máquina reais:** os passos 6 e 7, com 3 processos em 4 núcleos. Dá para parar e retomar só entre passos.
- **Comparação esperada:**
  - **tabelas de decisão** (`cert_*_tabela.csv`) idênticas byte a byte, salvo diferença de arredondamento dirigido
    entre versões;
  - `cert_*_blocos.csv` e `*_resumo.json` diferem só em campos de tempo (`segundos*`, `tempo_s`);
  - os arquivos `*_testes_resultado.json` também contêm tempos. Comparar sem esses campos.
- **Diagnóstico T29:** a reprodução bit a bit de `targeted_joint_fit` com o `src/` atual só se espera em m4-v3 (d01). Em
  b01 e c01 as diferenças são de ≤ 4,4·10⁻¹², porque esses runs usaram outra versão de `periods.py`. Não entra em
  decisão: o certificado compara com o valor **registrado**.

---

## 5. Histórico forense: onde o código já falhou (auditar com lupa)

| # | Ponto | O que falhou | Onde foi corrigido | O que verificar |
|---|---|---|---|---|
| F1 | Conversão de extremos intervalares | `iv.mpf(mpf(ck.a))` e `mn` com `mpf` na precisão comum invertiam a direção do arredondamento (`ck_inf` acima do extremo superior em 28/47 linhas) | adendo 1; `_q`, `lo_q`, `hi_q`, `pt_lo`, `float_dn/up` | nenhum `.a`/`.b` ou `mpf(` sobre extremos (T6); toda conversão passa por `Fraction` |
| F2 | `W_iv`, ramo \|v\| ≈ 1 (e v ≈ 0) | intervalos **disjuntos** da função (21/27 casos sensíveis) | adendo 1; ramos decididos por frações exatas; asserção de denominador | T1/T2; derivação das fatorações sinc em §II.18 |
| F3 | Decisão final | `mpf(tot.b) <= mpf(TAU)` com conversão comum | adendo 1; `hi_q(tot) <= Fraction(1, 10**6)` | T5 |
| F4 | Operações binary64 fora da base declarada | `vmn**4`, `math.sqrt(2)`, `math.pi` e ausência de verificação de finitude | adendo 2 (L1–L5) | T8; asserções `np.isfinite` em `I` |
| F5 | Soma intervalar `isum` | justificativa do fator de erro | adendo 2; **lema de somação em §II.19.2** | hipóteses (H-a)–(H-c); fator γ_m/(1 − γ_m) < 2mε para mε ≤ 0,1 |
| F6 | Exportação `sup_str` | string não conferida contra o extremo superior | adendo 2; `sup_chk` com asserção | T7 |
| F7 | c₁, c₂ herdados | strings de 6 dígitos de arquivo antigo, sem os intervalos originais | adendo 3; `phi_constants` (malha com cobertura exata e pontas analíticas) | T9; monotonias das pontas em §II.20.2 |
| F8 | Peso χ de S^abs | a definição declarada tem χ, a implementação não | registrado em §II.21: `cell_sums` sem χ majora a soma completa dos módulos | que `cell_sums()` realmente não aplica χ e que a dominação (1 − χ ≤ 1) está correta |
| F9 | Fronteira dos regimes em u = 6 | teste exigia menor termo = 404 (não é potência de primo) | correção do T11 (completude e disjunção) | T11; nenhum n em (e⁵, e¹³] fora ou em dois regimes |
| F10 | Cota de densidade herdada | `density_error_certified.py` anterior aos adendos, com janela [A − 10⁻⁶, B + 10⁻⁶] | DECLARACAO_CERT_DENSIDADE; janela [A*, B*] = [E_c ∓ L/2] | derivação de Binet (DLMF 5.11.2, §5.11(ii)); T16–T21; os 15 blocos com [A*, B*] ≠ [A, B] |
| F11 | Testes de ρ_ord, rodada 1 | meta-condição pós-execução; comparação decimal × CSV; critério relativo do T25 | 3 correções **após** ver a rodada 1 (rodada 1 preservada) | se as correções não afrouxam a decisão (não afrouxam por construção: decisão por intervalos); piso ‖a_k‖₁S₂\|fl(E) − E_dec\| |
| F12 | ρ_ord: bordas e resto | f″ salta nas bordas; zeros de índice fora de I que entram na janela | §II.23.2: resto lipschitziano; η e contagem Z1 | T24 (pior razão 0,9988: cota apertada); T26 |
| F13 | ρ_num: termo suave | cancelamento dos termos de fronteira em J_m; corte K; alarme | §II.24.3; dps 60; K com ρ_K ≤ 10⁻²⁰; alarme de consistência | T30 (desvio: primitiva fechada em vez de `quad`); T31; T34; recorrência C_m/S_m e sinal de J_m = C_m − iS_m |

---

## 6. Revisão matemática (o que a reexecução não testa)

| Peça | Local | Hipóteses a conferir |
|---|---|---|
| Admissibilidade 𝒜 e forma de referência | ETAPA11_3B_ADMISSIBILIDADE; Connes (arquivado) | F5 (Weil, bibliográfica) |
| Contagem local Z1 (10,5·log(T + 8)) | ETAPA11_3B_Z1_CONTAGEM | J1 (Jensen, bibliográfica); DLMF 25.2.1 e 25.2.10 |
| S3b | ETAPA11_3B_H1_R5_ESTIMADOR §2.1 | F1 subsumida por RH |
| P-RH, Lemas 1–5 | §II.9 | RH |
| Lema 5′ (polos por oscilação) | §II.11 | — |
| P-RH-trunc | §II.13 | — |
| Lema 4′ | §II.15.2 | — |
| Lema de somação binary64 | §II.19.2 | (H-a)–(H-c) |
| Identidade contra 𝒦 e dominação por S^abs | §II.21.1 | a_k·ℓ_n = δ_kn; χ ≡ 0 em (−∞, 13] |
| Cota de Binet para ρ_Δ | §II.22.2 | DLMF 5.11.2, §5.11(ii), 25.10.2 |
| ρ_ord: Lipschitz, borda | §II.23.2 | **H-tab (não certificada)** |
| ρ_num: resto de ln(1 + y), recorrência dos momentos, a_k·M_𝒦 = c_k | §II.24.3 | posto certificado |

**Base de confiança computacional:**
- IEEE-754 binary64 com arredondamento ao mais próximo, sem precisão estendida e com finitude verificada;
- arredondamento dirigido correto de `mpmath.iv` (log, exp, sin, cos, sqrt, π) na versão 1.4.1;
- inteiros exatos do Python;
- crivo conferido por duas implementações.

---

## 7. Resultados a reproduzir (conferência mínima)

| Etapa | Elegíveis | Todos os pares | Pior caso elegível |
|---|---|---|---|
| Execução 4 (U₂ = 15) | 461/461 | 1.178 | 6,45224274·10⁻⁷ |
| Contaminação (𝒦) | 461/461 | 1.093 | 6,6090905·10⁻⁷ |
| Densidade ρ_Δ | 461/461 | 1.089 | 6,62126197·10⁻⁷ |
| Ordenadas ρ_ord (H-tab) | 461/461 | 1.024 | 7,31323657·10⁻⁷ |
| Numérico (T) | 461/461 | 1.024 | 7,313615663·10⁻⁷ (ε + total^γ) |

**Mais:**
- (N): ε_k^sup ≤ 6,27·10⁻¹¹ nos elegíveis e ≤ 4,10·10⁻¹⁰ em todos;
- parada bit a bit `[]` em todas as etapas;
- alarme de consistência sem disparos (maior razão 0,609);
- posto 94 com ρ ≤ 8,612·10⁻¹³.

**Verificações cruzadas feitas pelo autor** (autoverificação, sem valor de auditoria), todas com 0 violações:
- recomputação das decisões (T) a partir das colunas gravadas;
- cadeia total_exec4 ≤ contaminação ≤ densidade ≤ ordenadas nos 1.410 pares (vale por construção);
- r̂_k − 1 ∈ [q_inf − ε, q_sup + ε].

---

## 8. Limites que o auditor deve confirmar que o registro respeita

- **Não é prova de RH.** (T) é condicional a RH, F5, J1 e H-tab.
- **(N) diz respeito aos dados tabulados e ao número registrado,** não aos zeros verdadeiros.
- **O corte (8, 2) foi escolhido após a exploração.** Nenhum outro corte foi certificado.
- **A elegibilidade das 461 linhas** foi calculada pelo pipeline e **não** é certificada.
- **A monotonicidade dos totais vale por construção** (soma de cotas em módulo). Não informa nada sobre sinais.
- **ε_k é dominado pela largura dos intervalos.** Não é "precisão do código".
- **Não é C2 inteiro;** S1, S3a, S3c e H1 continuam abertos.
- **A anterioridade das declarações é autodeclarada** (§2.3).

---

## 9. Relatório do auditor (modelo)

1. **Ambiente usado:** versões e SO; divergências em relação a §1.
2. **Integridade:** resultado de §2.1 e §2.2; entradas que não conferiram.
3. **Reexecução:** passos executados; tabelas idênticas (sim/não; diferenças); tempos.
4. **Pontos forenses F1–F13:** para cada um, "conferido sem achado", "achado" (com descrição e severidade) ou "não
   examinado".
5. **Revisão matemática (§6):** peças conferidas; erros ou lacunas.
6. **Limites (§8):** trechos do registro que excedem o estabelecido.
7. **Conclusão:** "certificado sustentado", "sustentado com ressalvas" ou "não sustentado", com justificativa.

**Regra do projeto para achados:** nenhum achado é corrigido silenciosamente. Cada correção exige nova declaração, e a
execução afetada é preservada e marcada, como nas execuções 1 a 3.
