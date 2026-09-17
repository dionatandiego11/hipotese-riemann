# Relatório M3 — espectroscopia inversa por blocos

**ID:** `run_20260913_154009_m3_b01-b02-b03-b04-b05-b06-b07-b08-b09-b10`
**Blocos:** b01, b02, b03, b04, b05, b06, b07, b08, b09, b10
**Duração:** 1717.3 s; pico de memória 178 MB
**Comando:** `/home/dionatandiego11/Downloads/hipotese-riemann/src/riemann_spectra/__main__.py m3 --config configs/m4_v1_bh.toml --blocks b01,b02,b03,b04,b05,b06,b07,b08,b09,b10 --workers 4`

Protocolo congelado em 2026-09-13T14:44:12.793174+00:00 (config `871622b37aad6afb…`, módulos `5885b75ea98233af…`).

## Resumo por bloco

| Bloco | Índices | L | FWHM | Catálogo | Detectáveis | Detecções | S | Sem corresp. | S nulo máx | p | Recuperação | Decisões alteráveis por z refinado | mediana abs(razão−1) `band_conjugate` | mediana abs(razão−1) `band_no_conjugate` | mediana abs(razão−1) `centers_conjugate` | Δ perturbação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| b01 | 10001–13000 | 2519 | 0.007 | 47 | 28 | 28 | 28 | 0 | 1 | 0.001 | 1.000 | 0 | 3.319e-08 | 3.393e-08 | 2.517e-07 | 3.110e-08 |
| b02 | 13001–16000 | 2454 | 0.007 | 47 | 26 | 25 | 25 | 0 | 0 | 0.001 | 0.962 | 1 | 3.495e-08 | 3.329e-08 | 2.696e-07 | 3.327e-08 |
| b03 | 16001–19000 | 2402 | 0.007 | 47 | 27 | 26 | 26 | 0 | 1 | 0.001 | 0.963 | 1 | 3.589e-08 | 3.541e-08 | 2.785e-07 | 5.668e-08 |
| b04 | 19001–22000 | 2360 | 0.007 | 47 | 26 | 26 | 26 | 0 | 1 | 0.001 | 1.000 | 0 | 3.533e-08 | 3.597e-08 | 2.681e-07 | 3.459e-08 |
| b05 | 22001–25000 | 2325 | 0.007 | 47 | 27 | 27 | 27 | 0 | 0 | 0.001 | 1.000 | 0 | 3.086e-08 | 3.007e-08 | 2.325e-07 | 5.355e-08 |
| b06 | 25001–28000 | 2296 | 0.007 | 47 | 27 | 27 | 27 | 0 | 0 | 0.001 | 1.000 | 0 | 3.260e-08 | 3.818e-08 | 2.490e-07 | 4.248e-08 |
| b07 | 28001–31000 | 2269 | 0.007 | 47 | 26 | 26 | 26 | 0 | 1 | 0.001 | 1.000 | 1 | 5.685e-08 | 7.147e-08 | 4.344e-07 | 4.671e-08 |
| b08 | 31001–34000 | 2246 | 0.007 | 47 | 26 | 26 | 26 | 0 | 1 | 0.001 | 1.000 | 0 | 3.628e-08 | 3.675e-08 | 2.764e-07 | 1.550e-08 |
| b09 | 34001–37000 | 2225 | 0.008 | 47 | 26 | 26 | 26 | 0 | 0 | 0.001 | 1.000 | 0 | 2.955e-08 | 3.384e-08 | 2.284e-07 | 4.691e-08 |
| b10 | 37001–40000 | 2207 | 0.008 | 47 | 27 | 27 | 27 | 0 | 1 | 0.001 | 1.000 | 0 | 4.210e-08 | 4.597e-08 | 3.214e-07 | 7.917e-08 |

Definições: *Detecções* são máximos locais de z = |F|/σ_nulo, avaliado na malha para zeros, controles e sintéticos,
acima do limiar FWER do nulo de permutação de espaçamentos, obtidos sem catálogo. O limiar e o escore global usam
conjuntos nulos independentes. *S* conta linhas r log p com uma detecção a menos da tolerância calibrada (um a um).
*p* compara S com a mesma cadeia aplicada a cada realização nula. *Recuperação* é a fração das linhas cujo
coeficiente de referência excede o limite de detecção previsto pelo nulo. As colunas de razão e fase vêm da
**medição direcionada** nos períodos conhecidos (ajuste conjunto com a resposta da janela), que não é detecção cega.

## Critérios pré-registrados por família de blocos

Família completa: True. Holm entre 10 blocos, alpha = 0.05. Blocos contíguos não são independentes.

| Bloco | C1: p(S) | p(S) Holm | recuperação (claras) | sem corresp. | inconclusivos | C1 bloco | C2: elegíveis | fração ≤ tol. | Q | p(Q) Holm | C2 bloco |
|---|---|---|---|---|---|---|---|---|---|---|---|
| b01 | 0.001 | 0.010 | 1.000 | 0 | 1 | passa | 13 | 1.000 | 1.000 | 0.010 | passa |
| b02 | 0.001 | 0.010 | 1.000 | 0 | 3 | passa | 12 | 1.000 | 1.000 | 0.010 | passa |
| b03 | 0.001 | 0.010 | 1.000 | 0 | 5 | passa | 12 | 1.000 | 1.000 | 0.010 | passa |
| b04 | 0.001 | 0.010 | 1.000 | 0 | 1 | passa | 12 | 1.000 | 1.000 | 0.010 | passa |
| b05 | 0.001 | 0.010 | 1.000 | 0 | 2 | passa | 12 | 1.000 | 1.000 | 0.010 | passa |
| b06 | 0.001 | 0.010 | 1.000 | 0 | 1 | passa | 13 | 1.000 | 1.000 | 0.010 | passa |
| b07 | 0.001 | 0.010 | 1.000 | 0 | 2 | passa | 12 | 1.000 | 1.000 | 0.010 | passa |
| b08 | 0.001 | 0.010 | 1.000 | 0 | 3 | passa | 12 | 1.000 | 1.000 | 0.010 | passa |
| b09 | 0.001 | 0.010 | 1.000 | 0 | 2 | passa | 12 | 1.000 | 1.000 | 0.010 | passa |
| b10 | 0.001 | 0.010 | 1.000 | 0 | 2 | passa | 12 | 1.000 | 1.000 | 0.010 | passa |

- **C1 (recuperação de frequências):** 10/10 blocos passam; blocos com detecção sem correspondência no catálogo: 0 (máximo pré-registrado 2); replicado em todos os blocos: **True**.
- **C2 (concordância de coeficientes, tolerância 1e-06, fração mínima 0.95, Q ≥ 0.9):** 10/10 blocos passam; replicado em todos os blocos: **True**.
- **C3 (compatibilidade estatística):** avaliada na execução M2 correspondente.

## Interpretação e limites

- A análise mede a transformada de uma janela finita de zeros e compara com a referência −log p/(π p^{r/2}).
  A concordância é um resultado numérico (categoria B). A justificativa exata da observável finita pela fórmula
  explícita — classe de funções-teste, termos e erros — ainda não foi estabelecida no projeto.
  A concordância não demonstra RH nem identifica um Hamiltoniano.
- O "fundo" entre linhas nos zeros não é ruído estatístico: é vazamento determinístico de outras linhas pelos lóbulos
  laterais da janela. A escala de ruído usada para decidir detecções vem, portanto, dos controles nulos.
- Linhas abaixo do limite de detecção do nulo não são evidência de ausência; ver colunas de detectabilidade prevista.
- Os valores-p são limitados inferiormente por 1/(B+1) e medem incompatibilidade com o nulo declarado.

## Detalhes por bloco

### bloco b01 (zeros 10001–13000)

Protocolo `m4-v1-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `79eb5c25d8996d0e8893752d87ed193b10d667992d915e9e0abdeabda7da0ee8` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [9878.655, 12397.778], L = 2519.1 |
| FWHM medida | 0.007 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 5414 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.032e-10 (máx. |F| = 105.4) |
| Quadratura: mudança ao reduzir painel pela metade | 3.067e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.089e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2838 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.052 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3448 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2071, 3.2838] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 13; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 13; 1.000 |
| Tolerância de matching (quantil 0.99) | 9.275e-04 = 0.139 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 174 |
| Detecções (nulo primário / secundário) | 28 / 23 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 28 |
| Escore S; nulo (conjunto independente, B=999) | 28; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.052 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=13); todas as 47 linhas | 3.319e-08 / 1.372e-07; 7.536e-08 / 9.106e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=13); todas as 47 linhas | 3.393e-08 / 1.441e-07; 7.564e-08 / 9.390e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=13); todas as 47 linhas | 2.517e-07 / 1.051e-06; 6.012e-07 / 6.911e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.195e-06 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 3.110e-08 / 1.656e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.469; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.322; p = 0.001 |
| Linhas não detectadas | 19 |
| Tempo (s) | instrument: 0.7, null_shuffle: 17.9, null_gue: 57.1, synthetic: 24.7, arithmetic: 71.8 |

Figuras: `tables/b01/spectrum_z.png`, `tables/b01/coefficients.png`, `tables/b01/synthetic_calibration.png`.

### bloco b02 (zeros 13001–16000)

Protocolo `m4-v1-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `bd802427d35a205553b73ca1617310e59be20ad88903c7ce5d2c40e164938647` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [12398.692, 14852.514], L = 2453.8 |
| FWHM medida | 0.007 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 5273 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.766e-10 (máx. |F| = 102.9) |
| Quadratura: mudança ao reduzir painel pela metade | 3.850e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.700e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.3294 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.028 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3766 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2455, 3.3294] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 3 (dos quais com correspondência no catálogo: 3) |
| Linhas claramente detectáveis; recuperação entre elas | 12; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 12; 1.000 |
| Tolerância de matching (quantil 0.99) | 6.904e-04 = 0.101 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 183 |
| Detecções (nulo primário / secundário) | 25 / 22 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 25; média 0.000, máx. 0 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.028 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 0.962; detectáveis perdidas: 89 |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.495e-08 / 8.038e-08; 6.838e-08 / 1.088e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.329e-08 / 6.861e-08; 6.400e-08 / 1.065e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 2.696e-07 / 6.150e-07; 5.179e-07 / 1.227e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 6.953e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 3.327e-08 / 1.585e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.497; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.339; p = 0.001 |
| Linhas não detectadas | 22 |
| Tempo (s) | instrument: 0.7, null_shuffle: 19.8, null_gue: 59.9, synthetic: 36.6, arithmetic: 50.5 |

Figuras: `tables/b02/spectrum_z.png`, `tables/b02/coefficients.png`, `tables/b02/synthetic_calibration.png`.

### bloco b03 (zeros 16001–19000)

Protocolo `m4-v1-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `71d68ce345cab884b5f37df5d0c66c95b7ee3962bb471ffc79e8a05cde57dc82` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [14853.311, 17255.318], L = 2402.0 |
| FWHM medida | 0.007 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 5162 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 3.902e-10 (máx. |F| = 100.1) |
| Quadratura: mudança ao reduzir painel pela metade | 3.459e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 6.119e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.3043 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.028 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3444 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2236, 3.3043] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 5 (dos quais com correspondência no catálogo: 5) |
| Linhas claramente detectáveis; recuperação entre elas | 12; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 12; 1.000 |
| Tolerância de matching (quantil 0.99) | 7.665e-04 = 0.110 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 163 |
| Detecções (nulo primário / secundário) | 26 / 22 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 27 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.028 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 0.963; detectáveis perdidas: 97 |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.589e-08 / 1.044e-07; 6.720e-08 / 7.739e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.541e-08 / 1.002e-07; 6.232e-08 / 7.677e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 2.785e-07 / 7.983e-07; 5.087e-07 / 8.999e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 9.027e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 5.668e-08 / 2.079e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.495; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.346; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.9, null_shuffle: 16.5, null_gue: 55.2, synthetic: 46.1, arithmetic: 54.5 |

Figuras: `tables/b03/spectrum_z.png`, `tables/b03/coefficients.png`, `tables/b03/synthetic_calibration.png`.

### bloco b04 (zeros 19001–22000)

Protocolo `m4-v1-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `a6012ee62ae81e07380f839414d042002201f1f4889aa1c1fe190676ce93cdc3` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [17256.388, 19616.305], L = 2359.9 |
| FWHM medida | 0.007 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 5071 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 3.068e-10 (máx. |F| = 98.6) |
| Quadratura: mudança ao reduzir painel pela metade | 4.388e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 6.889e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.3026 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.037 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3319 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1948, 3.3026] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 12; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 12; 1.000 |
| Tolerância de matching (quantil 0.99) | 0.001 = 0.191 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 175 |
| Detecções (nulo primário / secundário) | 26 / 21 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.037 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.533e-08 / 7.832e-08; 4.579e-08 / 2.492e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.597e-08 / 8.750e-08; 4.890e-08 / 2.836e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 2.681e-07 / 5.917e-07; 3.464e-07 / 5.963e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 6.792e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 3.459e-08 / 1.179e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.474; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.350; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.9, null_shuffle: 22.5, null_gue: 57.0, synthetic: 62.2, arithmetic: 41.1 |

Figuras: `tables/b04/spectrum_z.png`, `tables/b04/coefficients.png`, `tables/b04/synthetic_calibration.png`.

### bloco b05 (zeros 22001–25000)

Protocolo `m4-v1-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `1619a43b6bdd23330f8976691b7b3e3f1f77a953ec959d4b169f75179216f2cf` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [19617.382, 21942.592], L = 2325.2 |
| FWHM medida | 0.007 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4997 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.330e-10 (máx. |F| = 97.0) |
| Quadratura: mudança ao reduzir painel pela metade | 2.290e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 5.594e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2555 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.046 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4605 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1816, 3.2555] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 2 (dos quais com correspondência no catálogo: 2) |
| Linhas claramente detectáveis; recuperação entre elas | 12; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 12; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.459e-04 = 0.117 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 175 |
| Detecções (nulo primário / secundário) | 27 / 20 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 27 |
| Escore S; nulo (conjunto independente, B=999) | 27; média 0.000, máx. 0 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.048 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.086e-08 / 8.698e-08; 5.388e-08 / 6.097e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.007e-08 / 8.804e-08; 4.878e-08 / 5.961e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 2.325e-07 / 6.583e-07; 4.136e-07 / 5.309e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 7.463e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 5.355e-08 / 1.639e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.479; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.328; p = 0.001 |
| Linhas não detectadas | 20 |
| Tempo (s) | instrument: 0.7, null_shuffle: 22.1, null_gue: 56.6, synthetic: 57.4, arithmetic: 39.2 |

Figuras: `tables/b05/spectrum_z.png`, `tables/b05/coefficients.png`, `tables/b05/synthetic_calibration.png`.

### bloco b06 (zeros 25001–28000)

Protocolo `m4-v1-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `4479fe94030135687a53cf345e4365914ed6b1af2a0a23a9e8328989ad66b41e` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [21942.661, 24238.384], L = 2295.7 |
| FWHM medida | 0.007 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4934 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.197e-10 (máx. |F| = 96.4) |
| Quadratura: mudança ao reduzir painel pela metade | 6.241e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.778e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2798 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.048 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4247 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2106, 3.2798] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 13; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 13; 1.000 |
| Tolerância de matching (quantil 0.99) | 9.266e-04 = 0.127 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 188 |
| Detecções (nulo primário / secundário) | 27 / 19 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 27 |
| Escore S; nulo (conjunto independente, B=999) | 27; média 0.000, máx. 0 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.049 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=13); todas as 47 linhas | 3.260e-08 / 6.017e-08; 6.017e-08 / 1.312e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=13); todas as 47 linhas | 3.818e-08 / 8.491e-08; 6.156e-08 / 1.274e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=13); todas as 47 linhas | 2.490e-07 / 4.615e-07; 5.000e-07 / 8.987e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 5.224e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 4.248e-08 / 1.448e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.470; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.318; p = 0.001 |
| Linhas não detectadas | 20 |
| Tempo (s) | instrument: 0.6, null_shuffle: 18.0, null_gue: 56.5, synthetic: 57.7, arithmetic: 37.7 |

Figuras: `tables/b06/spectrum_z.png`, `tables/b06/coefficients.png`, `tables/b06/synthetic_calibration.png`.

### bloco b07 (zeros 28001–31000)

Protocolo `m4-v1-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `026f1bd9c6f6458bec65e4d4067416610a2f6226715819774c34fd8a8051be82` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [24239.882, 26508.693], L = 2268.8 |
| FWHM medida | 0.007 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4876 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.430e-10 (máx. |F| = 94.4) |
| Quadratura: mudança ao reduzir painel pela metade | 2.912e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 5.708e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2524 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.052 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.6472 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1904, 3.2524] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 2 (dos quais com correspondência no catálogo: 2) |
| Linhas claramente detectáveis; recuperação entre elas | 12; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 12; 1.000 |
| Tolerância de matching (quantil 0.99) | 0.001 = 0.146 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 178 |
| Detecções (nulo primário / secundário) | 26 / 17 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.002, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.052 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=12); todas as 47 linhas | 5.685e-08 / 1.299e-07; 6.223e-08 / 8.044e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 7.147e-08 / 1.351e-07; 7.309e-08 / 8.663e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 4.344e-07 / 9.931e-07; 4.781e-07 / 5.160e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.128e-06 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 4.671e-08 / 1.942e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.485; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.318; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.6, null_shuffle: 15.2, null_gue: 55.5, synthetic: 57.3, arithmetic: 38.3 |

Figuras: `tables/b07/spectrum_z.png`, `tables/b07/coefficients.png`, `tables/b07/synthetic_calibration.png`.

### bloco b08 (zeros 31001–34000)

Protocolo `m4-v1-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `32bf0f3ab5462a98cb150c4e992816d106da0b090d343c362a0a35aceecd20dd` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [26509.950, 28755.619], L = 2245.7 |
| FWHM medida | 0.007 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4826 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 7.171e-11 (máx. |F| = 93.4) |
| Quadratura: mudança ao reduzir painel pela metade | 1.132e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 6.560e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2960 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.042 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.5842 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1885, 3.2960] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 3 (dos quais com correspondência no catálogo: 3) |
| Linhas claramente detectáveis; recuperação entre elas | 12; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 12; 1.000 |
| Tolerância de matching (quantil 0.99) | 6.302e-04 = 0.084 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 174 |
| Detecções (nulo primário / secundário) | 26 / 16 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.002, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.043 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.628e-08 / 6.521e-08; 3.849e-08 / 4.870e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.675e-08 / 6.311e-08; 4.198e-08 / 5.362e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 2.764e-07 / 4.894e-07; 2.903e-07 / 2.376e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 5.546e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 1.550e-08 / 1.300e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.475; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.325; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.6, null_shuffle: 15.4, null_gue: 56.6, synthetic: 57.2, arithmetic: 38.5 |

Figuras: `tables/b08/spectrum_z.png`, `tables/b08/coefficients.png`, `tables/b08/synthetic_calibration.png`.

### bloco b09 (zeros 34001–37000)

Protocolo `m4-v1-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `56d735713494168b2edd3e68d53cb51533a4bd24699db58dd8e1dc5accda3c18` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [28757.060, 30982.396], L = 2225.3 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4782 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.069e-10 (máx. |F| = 92.7) |
| Quadratura: mudança ao reduzir painel pela metade | 3.800e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.497e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2766 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.037 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3492 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1901, 3.2766] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 2 (dos quais com correspondência no catálogo: 2) |
| Linhas claramente detectáveis; recuperação entre elas | 12; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 12; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.997e-04 = 0.120 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 181 |
| Detecções (nulo primário / secundário) | 26 / 20 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.000, máx. 0 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.037 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=12); todas as 47 linhas | 2.955e-08 / 1.158e-07; 5.461e-08 / 7.915e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.384e-08 / 1.203e-07; 6.259e-08 / 8.341e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 2.284e-07 / 8.830e-07; 4.026e-07 / 6.018e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.003e-06 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 4.691e-08 / 1.963e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.476; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.322; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.6, null_shuffle: 17.0, null_gue: 56.1, synthetic: 57.6, arithmetic: 37.8 |

Figuras: `tables/b09/spectrum_z.png`, `tables/b09/coefficients.png`, `tables/b09/synthetic_calibration.png`.

### bloco b10 (zeros 37001–40000)

Protocolo `m4-v1-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `ca1fe733a270e7e7943e6d8e98856598cc377c8f6ff4effda3b25b91f4d1b19b` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [30983.188, 33190.012], L = 2206.8 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4742 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.667e-10 (máx. |F| = 92.2) |
| Quadratura: mudança ao reduzir painel pela metade | 3.871e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 5.939e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2019 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.073 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.2743 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1308, 3.2019] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 2 (dos quais com correspondência no catálogo: 2) |
| Linhas claramente detectáveis; recuperação entre elas | 12; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 12; 1.000 |
| Tolerância de matching (quantil 0.99) | 0.001 = 0.176 FWHM |
| Separação de pares com ≥90% recuperado | 1.50 FWHM (medida) |
| Linhas sintéticas isoladas | 184 |
| Detecções (nulo primário / secundário) | 27 / 20 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 27 |
| Escore S; nulo (conjunto independente, B=999) | 27; média 0.005, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.076 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=12); todas as 47 linhas | 4.210e-08 / 8.300e-08; 6.104e-08 / 4.764e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 4.597e-08 / 8.910e-08; 6.380e-08 / 4.905e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.214e-07 / 6.363e-07; 4.227e-07 / 3.620e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 7.254e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.917e-08 / 1.910e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.516; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.344; p = 0.001 |
| Linhas não detectadas | 20 |
| Tempo (s) | instrument: 0.6, null_shuffle: 16.7, null_gue: 55.5, synthetic: 58.5, arithmetic: 37.2 |

Figuras: `tables/b10/spectrum_z.png`, `tables/b10/coefficients.png`, `tables/b10/synthetic_calibration.png`.

