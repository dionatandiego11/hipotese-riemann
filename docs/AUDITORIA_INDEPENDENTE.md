# Auditoria por implementação independente (13/09/2026)

**Escopo:** três blocos já analisados (10.001–13.000; 22.001–25.000; 67.001–70.000). Nenhum zero com índice > 70.000 foi lido.
**Objetivo:** procurar erros compartilhados entre as execuções m4-v1 e m4-v2, que usaram o mesmo código.
**Resultado:** o núcleo determinístico concorda quantitativamente. As grandezas com controles aleatórios são compatíveis
dentro das incertezas pré-registradas. Quatro verificações determinísticas ficaram **fora da tolerância**; todas foram
investigadas e atribuídas a aproximações numéricas da referência, de efeito desprezível sobre as conclusões, ou a um
defeito de desenho do próprio plano. Nenhum erro científico compartilhado foi encontrado **dentro do que esta auditoria
consegue detectar** (ver §6).

## 1. Método e limites de independência

- **Código:** `independent/riemann_indep/` (`core.py`, `stats.py`, `spectral.py`, `pipeline.py`). Um teste verifica que
  não há importação de `riemann_spectra`. Hashes dos módulos em `results/independent_audit_20260913/manifest_independent.json`.
- **Especificação e plano congelados antes da comparação:** `independent/SPEC_REVIEW.md` (25 ambiguidades e resoluções,
  derivações conferidas) e `independent/COMPARISON_PLAN.md` (blocos, orçamentos, tolerâncias D1–D9 e S1–S13), com
  SHA-256 em `independent/PLAN.lock.json` (congelado 20:25 UTC). A implementação rodou antes de qualquer arquivo de
  referência por bloco ser aberto (`compare.py` é o único script que os lê).
- **A comparação não é cega.** O mesmo agente escreveu `src/` e a implementação independente, e já conhecia os
  resultados agregados (contagens, inconclusivos log 127 e log 131). Escolhas de projeto podem ter sido repetidas por
  memória; a mitigação foi usar caminhos numéricos deliberadamente diferentes e registrar as ambiguidades por escrito.
- **Caminhos numéricos diferentes:**
  - transformada: soma direta e recorrência de fasores, em vez de NUFFT;
  - termo médio: forma fechada com Si/Ci, em vez de Gauss–Legendre;
  - inversa de N̄: W de Lambert;
  - GUE: tridiagonal reescrito e validado contra GUE denso;
  - máximos: supressão de não-máximos manual;
  - mínimos quadrados: LAPACK `gelsy`;
  - matching: guloso, com atribuição ótima como sensibilidade;
  - CUE: Clenshaw–Curtis, forma de Toeplitz e derivação por Chebyshev;
  - dados: lidos do arquivo bruto, e não do CSV processado.
- **Orçamentos independentes:** σ 200; limiar 1.999; escore 1.999; GUE 100 + 199; M2 299 + 299; sementes 7001–7003.
  Custo: 9–11 min por bloco.

## 2. Validação com exemplos conhecidos (antes da comparação)

12 testes em `independent/tests/`, todos aprovados:
- ausência de dependência de `src/`;
- termo suave × quadratura oscilatória mpmath (erro < 1e-11);
- resposta de Hann × integral numérica e FWHM = 4π/L exata;
- recorrência × soma direta (≤ 1e-9);
- inversão de N̄ (≤ 1e-9);
- amplitude e fase por injeção nos níveis (≤ 2e-3);
- ajuste com lóbulo conjugado exato no modelo (≤ 1e-10);
- GUE tridiagonal × denso (KS);
- cobertura do IC do quantil (≥ 0,94);
- R₂ e K_c de Poisson iguais a 1;
- CUE N = 2 analítico (≤ 1e-9) e variância de p₀ = 0,18;
- recusa de índices > 70.000.

Verificações adicionais:
- GUE denso × tridiagonal em N = 300: variância local 0,1780 ± 0,0027 × 0,1791 ± 0,0026; KS p = 0,84;
- K_c do GUE acompanha a rampa τ.

## 3. Resultado das verificações pré-registradas

| Código | Tolerância | baixo (b01) | intermediário (b05) | alto (c10) |
|---|---|---|---|---|
| D1 | n_t igual; dt, FWHM, W0 rel ≤ 1e-10 | **FORA** dt rel 2.50e-10 | **FORA** dt rel -1.20e-10 | ✓ dt rel -8.15e-11 |
| D2 | máx abs ≤ 1e-8 | **FORA** máx 4.09e-10 | **FORA** máx 3.20e-09 | **FORA** máx 5.48e-09 |
| D3 | máx ≤ 1e-7; mediana ≤ 1e-8 | **FORA** máx 2.88e-05; med 7.44e-09 | **FORA** máx 1.18e-05; med 3.67e-09 | **FORA** máx 6.41e-06; med 2.90e-09 |
| D4 | máx abs ≤ 1e-8 | ✓ máx 1.22e-10 | ✓ máx 3.36e-10 | ✓ máx 3.55e-09 |
| D9 | mesmas entradas; períodos ≤ 1e-14 | ✓ 47 = 47 | ✓ 47 = 47 | ✓ 47 = 47 |
| D5 | máx abs Δrazão ≤ 1e-9 (3 variantes, 47 linhas) | ✓ máx 5.67e-13 | ✓ máx 1.18e-11 | ✓ máx 3.26e-11 |
| S1 | mediana ≤ 0,03; p99 ≤ 0,08 | ✓ med 0.0109; p99 0.0474 | ✓ med 0.0107; p99 0.0510 | ✓ med 0.0124; p99 0.0445 |
| S2 | KS p ≥ 0,001 | ✓ p 0.9199 | ✓ p 0.3940 | ✓ p 0.0107 |
| S3 | ICs se sobrepõem | ✓ ref [3.307; 3.336] ind [3.283; 3.353] | ✓ ref [3.283; 3.313] ind [3.278; 3.346] | ✓ ref [3.269; 3.297] ind [3.238; 3.304] |
| S4 | faixa binomial 99,9% | ✓ 0.0345 (faixa 0.0345–0.0665) | ✓ 0.0415 (faixa 0.0345–0.0665) | ✓ 0.0420 (faixa 0.0345–0.0665) |
| S5 | linhas claramente decididas com mesmo status | ✓ 0 divergências; 7 não decididas | ✓ 0 divergências; 6 não decididas | ✓ 0 divergências; 8 não decididas |
| S6 | |z_ind/z_ref − 1| ≤ 0,05 em ≥ 95% das detectadas em ambas | ✓ 1.000 ≤5%; máx 0.032 | ✓ 0.970 ≤5%; máx 0.057 | ✓ 1.000 ≤5%; máx 0.033 |
| S7 | |ΔS| ≤ nº não claramente decididas; sem correspondência = 0 | ✓ S 34/34 | ✓ S 33/34 | ✓ S 33/32 |
| S8 | p_ind ≤ 0,01 | ✓ 0.0005 / 0.0001 | ✓ 0.0005 / 0.0001 | ✓ 0.0005 / 0.0001 |
| S9 | razão ∈ [0,5; 2]; separação igual/adjacente | ✓ razão 1.26; sep 1.25/1.25 | ✓ razão 0.91; sep 1.25/1.25 | ✓ razão 1.08; sep 1.25/1.25 |
| S10 | vereditos por bloco iguais | ✓ C1 True/True; C2 True/True | ✓ C1 True/True; C2 True/True | ✓ C1 True/True; C2 True/True |
| D6 | |ΔR|, |ΔQ| ≤ 1e-9 se o conjunto elegível for igual | ✓ ΔQ 0.0e+00; mesmo conjunto: True | ✓ ΔQ 3.9e-12; mesmo conjunto: False | ✓ ΔQ 2.5e-12; mesmo conjunto: False |
| S11 | ambos ≤ 0,01 | ✓ 0.001 / 0.001 | ✓ 0.001 / 0.001 | ✓ 0.001 / 0.001 |
| D7 | Var, CDF, R₂ rel ≤ 1e-10; K_c abs ≤ 1e-8 + rel 1e-8 | ✓ Var 0.0000; K rel 2.52e-11 | ✓ Var 0.0000; K rel 2.51e-12 | ✓ Var 0.0000; K rel 7.13e-11 |
| S12 | piso: p_ind ≤ 2/300; senão |Δp| ≤ 3·EP + 0,01 | ✓ todos dentro | ✓ todos dentro | ✓ todos dentro |
| D8 | P₀ ≤ 1e-7; P₁ ≤ 1e-4; CDF ≤ 1e-6; distâncias ≤ 1e-6 | **FORA** CDF 3.92e-05; dist 6.15e-06 | **FORA** CDF 3.23e-05; dist 5.24e-06 | **FORA** CDF 2.72e-05; dist 3.99e-06 |
| S13 | razão ∈ [0,75; 1,33] | ✓ 0.997 | ✓ 1.036 | ✓ 1.033 |

(✓ dentro da tolerância; **FORA** fora da tolerância. Valores completos em `results/independent_audit_20260913/comparison.json`.)

## 4. Investigação das verificações fora da tolerância (`diagnose_discrepancies.py`, `diagnostics.json`)

| Código | Causa identificada | Evidência | Efeito nas conclusões |
|---|---|---|---|
| D1 | **(ii) aproximação numérica da referência.** A FWHM de Hann é exatamente 4π/L (W(2π/L)/W(0) = 0,5 exato), mas a referência a obtém por `brentq` com tolerância absoluta padrão. Erro relativo de 0,8–2,5·10⁻¹⁰ | independente: erro 0 (≤ 1e-16); referência: 2,5e-10 (b01), 1,2e-10 (b05), 8,1e-11 (c10, dentro) | Malha deslocada ≤ 1,1·10⁻⁹ em t, contra FWHM ≈ 5·10⁻³ |
| D3 | **Consequência de D1**, não da transformada. O plano comparou F em malhas que diferem ~10⁻⁹, onde F varia ~2·10⁵ por unidade de t | Na **mesma malha**: máx abs 6,4e-10 / 3,2e-9 / 5,5e-9 e medianas ~1e-11 (dentro de D3) | Variação de F nos picos detectados ≤ 6·10⁻⁸ relativa, contra incerteza estatística de σ ~10⁻² |
| D2 | **Condição do plano** ("malha idêntica") não satisfeita por D1. Os valores estão dentro da tolerância | Na mesma malha: máx 4,1e-10 / 3,2e-9 / 5,5e-9 ≤ 1e-8 | Nenhum |
| D8 | **(ii) aproximação numérica da referência.** A predição CUE usa interpolação linear de P₁ numa malha de passo 0,025 | Com a mesma interpolação, as implementações concordam a 1,3–1,9·10⁻⁸. Erro da interpolação: 2,7–3,9·10⁻⁵ na CDF | Distâncias RMS à predição corrigida mudam ≤ 6·10⁻⁶ (≤ 0,1%); variância predita ≤ 3·10⁻⁶. Análise secundária inalterada |

Também registrado: **(vi) defeito do plano.** D1 (1e-10) e a condição de malha idêntica em D2/D3 foram fixados sem
considerar a tolerância do localizador de raízes da referência. O plano não foi alterado; as verificações continuam
marcadas como fora da tolerância, com a causa acima.

Observações dentro da tolerância, mas próximas dos limites:
- S4 em b01: a fração do conjunto-escore independente, 0,0345, está exatamente no limite inferior da faixa binomial;
- S2 em c10: KS p = 0,011;
- S6 em b05: 0,970, contra mínimo de 0,95.

Todas são compatíveis com variação Monte Carlo e não mostram padrão consistente entre blocos.

Nulo GUE secundário (sem tolerância pré-registrada): as contagens diferem (26 × 29; 25 × 26; 20 × 24). Os ICs do
limiar se sobrepõem nos três blocos, com KS p = 0,79 / 0,63 / 0,997 e σ com diferença mediana de 1,6%. As diferenças
vêm da largura do IC com 199 realizações.

## 5. Linhas não claramente decididas (S5)

Nenhuma linha claramente decidida mudou de status. Nas linhas abaixo, z está a menos de 5% da faixa inconclusiva
combinada; o status pode mudar com a realização de Monte Carlo de σ e do limiar, como previsto.

| Bloco | Linha | Status ref (z) | Status ind (z) | z previsto ref / ind |
|---|---|---|---|---|
| baixo_b01 | 2^3 | not_detected (3.227) | not_detected (3.208) | 3.227 / 3.208 |
| baixo_b01 | 5^2 | detected (3.546) | detected (3.514) | 3.561 / 3.529 |
| baixo_b01 | 113 | detected (3.491) | detected (3.542) | 3.520 / 3.569 |
| baixo_b01 | 127 | detected (3.382) | detected (3.408) | 3.384 / 3.411 |
| baixo_b01 | 131 | not_detected (3.269) | inconclusive (3.297) | 3.287 / 3.320 |
| baixo_b01 | 137 | not_detected (3.284) | not_detected (3.178) | 3.310 / 3.203 |
| baixo_b01 | 139 | not_detected (3.249) | not_detected (3.192) | 3.264 / 3.206 |
| intermediario_b05 | 5^2 | detected (3.406) | detected (3.419) | 3.420 / 3.433 |
| intermediario_b05 | 113 | detected (3.467) | detected (3.559) | 3.482 / 3.571 |
| intermediario_b05 | 127 | detected (3.349) | inconclusive (3.336) | 3.377 / 3.365 |
| intermediario_b05 | 131 | inconclusive (3.297) | inconclusive (3.284) | 3.328 / 3.318 |
| intermediario_b05 | 137 | not_detected (3.179) | not_detected (3.244) | 3.179 / 3.244 |
| intermediario_b05 | 139 | not_detected (3.166) | not_detected (3.222) | 3.167 / 3.224 |
| alto_c10 | 5^2 | not_detected (3.178) | inconclusive (3.241) | 3.180 / 3.242 |
| alto_c10 | 107 | detected (3.559) | detected (3.462) | 3.574 / 3.479 |
| alto_c10 | 109 | detected (3.502) | detected (3.429) | 3.508 / 3.434 |
| alto_c10 | 113 | detected (3.422) | detected (3.413) | 3.422 / 3.413 |
| alto_c10 | 127 | inconclusive (3.286) | detected (3.343) | 3.287 / 3.345 |
| alto_c10 | 131 | not_detected (3.255) | not_detected (3.229) | 3.256 / 3.230 |
| alto_c10 | 137 | not_detected (3.100) | not_detected (3.175) | 3.114 / 3.189 |
| alto_c10 | 139 | not_detected (3.108) | not_detected (3.128) | 3.130 / 3.152 |

- **log 127:** detectada ou inconclusiva conforme a implementação em b05 e c10 (z = 3,29–3,35, junto ao limiar).
- **log 131:** inconclusiva ou não detectada em todos os blocos, nas duas implementações (z = 3,23–3,30).
- **Elegibilidade C2:** mudou uma linha por bloco. p = 53 em b05 foi elegível só na referência; p = 47 em c10, só na
  independente; nos dois casos o z previsto está junto à margem de 1,5. Os vereditos C1 e C2 dos três blocos coincidem.
- **Matching:** o guloso especificado e a atribuição ótima deram o mesmo S nos três blocos.

## 6. Dependências compartilhadas e o que esta auditoria não verifica

| Dependência | Situação |
|---|---|
| Autor e conhecimento prévio | Compartilhados (§1). Independência parcial |
| Especificação (PROTOCOLO) | Compartilhada. Revisada por derivação em SPEC_REVIEW; um erro conceitual comum, como uma escolha de nulo inadequada, não seria detectado por concordância |
| Fórmulas de referência (N̄ de Riemann–von Mangoldt, −log p/(π p^{r/2}), Bogomolny et al.) | Compartilhadas. A concordância dos coeficientes com a teoria a ~10⁻¹⁰ é um teste externo da normalização, mas não da interpretação |
| Dados (`data/raw/zeros1`) | Compartilhados. Lidos por caminhos diferentes; validação mpmath por amostra, não completa |
| NumPy/SciPy/LAPACK, `scipy.special` | Compartilhadas. Caminhos distintos reduzem, mas não eliminam, um erro de biblioteca comum |
| Linguagem e plataforma | Compartilhadas |

**Não verificado:**
- implementação por outra pessoa ou em outra linguagem;
- densidade θ na cadeia completa;
- inversão harmônica;
- recálculo completo dos zeros;
- os blocos restantes de m4-v1 e m4-v2;
- a análise de robustez Blackman–Harris.

## 7. Conclusões

1. **Transformada, termo médio, coeficientes e fase.** Por caminhos numéricos diferentes, as duas implementações
   concordam a ≤ 6·10⁻⁹ em F na mesma malha e a ≤ 3,3·10⁻¹¹ nas razões ao teórico das 47 linhas, nas três variantes
   de estimador. R e Q concordam a ≤ 4·10⁻¹². A normalização C = 2a·e^{−iE_cT} e o sinal foram reproduzidos.
2. **Estatística local (M2).** Variância de espaçamentos, CDF, R₂ e K_c são idênticos a ≤ 7·10⁻¹¹. Os valores-p dos
   envelopes são compatíveis, com rejeições nos pisos e R₂ não rejeitado nas duas implementações.
3. **Detecção e calibração.** σ, a distribuição do máximo nulo, os limiares e as tolerâncias sintéticas são compatíveis
   dentro das incertezas. As decisões coincidem em todas as linhas claramente decididas. As diferenças se concentram em
   linhas junto ao limiar, que já eram relatadas como inconclusivas ou variáveis.
4. **Erros encontrados na referência.** Duas aproximações numéricas: FWHM por `brentq` e interpolação linear de P₁ no CUE.
   Os efeitos, de ≤ 10⁻⁷ nas grandezas de decisão e ≤ 0,1% na análise secundária, não alteram C1, C2 ou C3. Não
   exigem nova versão para as conclusões atuais. Uma correção futura deve criar nova versão, preservando os resultados
   anteriores.
5. **O que não mudou.** Concordância entre implementações não é evidência a favor de RH nem de um Hamiltoniano. O
   resultado mostra que os achados numéricos de m4-v1 e m4-v2 não dependem dos detalhes de implementação auditados.

## 8. Reprodução

```bash
.venv/bin/python -m pytest -q independent/tests   # conftest.py adiciona o caminho
.venv/bin/python results/independent_audit_20260913/run_independent.py        # ~30 min
.venv/bin/python results/independent_audit_20260913/compare.py
.venv/bin/python results/independent_audit_20260913/diagnose_discrepancies.py
```

## 9. Fechamento documental das verificações fora da tolerância (registrado antes de m4-v3)

As quatro verificações abaixo **permanecem registradas como falhas do critério pré-registrado** em
`independent/COMPARISON_PLAN.md`. O diagnóstico e as comparações posteriores explicam as falhas, mas **não as
reclassificam como aprovações**. As comparações posteriores foram feitas depois de ver o resultado original, portanto
não são pré-registradas.

| Código | Resultado pré-registrado | Diagnóstico | Comparação posterior (não pré-registrada) | Situação |
|---|---|---|---|---|
| D1 | **Falha** em b01 e b05; passou em c10 | FWHM da referência obtida por `brentq` com tolerância absoluta padrão (erro relativo ≤ 2,5·10⁻¹⁰); valor exato 4π/L | Impacto na malha ≤ 1,1·10⁻⁹ em t | Fechada como falha explicada; corrigida em m4-v3 (§10) |
| D2 | **Falha** nos três blocos | A condição de malha idêntica não se verificou, por consequência de D1 | Na mesma malha: ≤ 5,5·10⁻⁹, dentro do limite numérico de 10⁻⁸ | Fechada como falha de condição do plano |
| D3 | **Falha** nos três blocos | Deslocamento de malha de D1 somado à inclinação de F (~2·10⁵ por unidade de t) | Na mesma malha: máx ≤ 5,5·10⁻⁹, mediana ~10⁻¹¹; efeito em |F| nos picos ≤ 6·10⁻⁸ relativo | Fechada como falha explicada; o plano de m4-v3 compara nas mesmas coordenadas |
| D8 | **Falha** nos três blocos | Interpolação linear de P₁ (passo 0,025) na análise CUE da referência; erro ≤ 3,9·10⁻⁵ na CDF | Com a mesma interpolação: ≤ 1,9·10⁻⁸; efeito ≤ 6·10⁻⁶ nas distâncias RMS (≤ 0,1%) | Fechada como falha explicada; corrigida em m4-v3 (§10) |

Arquivo legível por máquina: `results/independent_audit_20260913/closure.json`.
Os resultados de m4-v1, m4-v2 e desta auditoria não são alterados.

## 10. Correções numéricas incorporadas em m4-v3 (antes de acessar a faixa final)

Todas foram verificadas **só em dados já analisados** (20 blocos de m4-v1/m4-v2; `results/m4_v3_impact/`).

1. **FWHM** por raiz em unidades adimensionais com tolerância de máquina: erro relativo 2,5·10⁻¹⁰ → 2,2·10⁻¹⁶.
2. **CUE** com P₁ e p₁ avaliados exatamente em α·s: diferença máxima de 3,9·10⁻⁵ na CDF eliminada; distâncias RMS mudam
   ≤ 6,2·10⁻⁶.
3. **Quadratura do termo suave em coordenadas locais.** Encontrada no ensaio prévio do script de comparação m4-v3,
   sobre blocos de m4-v2 já analisados:
   - nós e pesos formados a partir de números ~10⁴–10⁵ tinham arredondamento com padrão regular (pesos por
     `diff(linspace(A, B))`, fases por E − E_c), que produzia erro de até 1,03·10⁻⁸ (bloco c08);
   - a hipótese de erro da NUFFT foi descartada, porque a largura do kernel não alterou o erro;
   - também foi descartado truncamento da quadratura, porque refinar não convergia.
   Com coordenadas locais o erro fica ≤ 2,0·10⁻¹⁰ contra a forma fechada independente.

Impacto conjunto nos 20 blocos: F muda ≤ 2,9·10⁻⁵ (sobretudo pelo deslocamento de malha de 1), z nos candidatos
≤ 6,4·10⁻⁸ relativo, **nenhuma mudança de classificação**. O ensaio também revelou um defeito do script de
comparação (0/0 em bins de R₂ nulos), corrigido antes do congelamento.
