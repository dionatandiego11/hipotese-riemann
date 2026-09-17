# Relatório M3 — espectroscopia inversa por blocos

**ID:** `run_20260913_144429_m3_b01-b02-b03-b04-b05-b06-b07-b08-b09-b10`
**Blocos:** b01, b02, b03, b04, b05, b06, b07, b08, b09, b10
**Duração:** 3315.2 s; pico de memória 190 MB
**Comando:** `/home/dionatandiego11/Downloads/hipotese-riemann/src/riemann_spectra/__main__.py m3 --config configs/m4_v1.toml --blocks b01,b02,b03,b04,b05,b06,b07,b08,b09,b10 --workers 4`

Protocolo congelado em 2026-09-13T14:44:12.490876+00:00 (config `8d98c02e23363429…`, módulos `5885b75ea98233af…`).

## Resumo por bloco

| Bloco | Índices | L | FWHM | Catálogo | Detectáveis | Detecções | S | Sem corresp. | S nulo máx | p | Recuperação | Decisões alteráveis por z refinado | mediana abs(razão−1) `band_conjugate` | mediana abs(razão−1) `band_no_conjugate` | mediana abs(razão−1) `centers_conjugate` | Δ perturbação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| b01 | 10001–13000 | 2519 | 0.005 | 47 | 34 | 34 | 34 | 0 | 1 | 1.000e-04 | 1.000 | 1 | 2.338e-10 | 2.193e-10 | 9.149e-10 | 6.730e-10 |
| b02 | 13001–16000 | 2454 | 0.005 | 47 | 34 | 34 | 34 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 2.233e-10 | 2.555e-10 | 8.349e-10 | 6.435e-10 |
| b03 | 16001–19000 | 2402 | 0.005 | 47 | 35 | 34 | 34 | 0 | 1 | 1.000e-04 | 0.971 | 1 | 3.881e-10 | 3.881e-10 | 2.941e-10 | 6.330e-10 |
| b04 | 19001–22000 | 2360 | 0.005 | 47 | 34 | 34 | 34 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 2.790e-10 | 2.845e-10 | 8.425e-10 | 5.826e-10 |
| b05 | 22001–25000 | 2325 | 0.005 | 47 | 35 | 34 | 34 | 0 | 1 | 1.000e-04 | 0.971 | 1 | 2.801e-10 | 2.779e-10 | 1.117e-09 | 6.543e-10 |
| b06 | 25001–28000 | 2296 | 0.005 | 47 | 35 | 35 | 35 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 2.548e-10 | 2.733e-10 | 9.783e-10 | 6.323e-10 |
| b07 | 28001–31000 | 2269 | 0.006 | 47 | 34 | 34 | 34 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 1.672e-10 | 1.668e-10 | 4.359e-10 | 6.628e-10 |
| b08 | 31001–34000 | 2246 | 0.006 | 47 | 33 | 33 | 33 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 2.377e-10 | 2.420e-10 | 3.464e-10 | 7.887e-10 |
| b09 | 34001–37000 | 2225 | 0.006 | 47 | 34 | 34 | 34 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 3.497e-10 | 3.420e-10 | 4.070e-10 | 7.157e-10 |
| b10 | 37001–40000 | 2207 | 0.006 | 47 | 35 | 35 | 35 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 3.332e-10 | 3.298e-10 | 4.182e-10 | 6.090e-10 |

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
| b01 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 16 | 1.000 | 1.000 | 0.010 | passa |
| b02 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 16 | 1.000 | 1.000 | 0.010 | passa |
| b03 | 1.000e-04 | 0.001 | 1.000 | 0 | 1 | passa | 16 | 1.000 | 1.000 | 0.010 | passa |
| b04 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 16 | 1.000 | 1.000 | 0.010 | passa |
| b05 | 1.000e-04 | 0.001 | 1.000 | 0 | 1 | passa | 16 | 1.000 | 1.000 | 0.010 | passa |
| b06 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 16 | 1.000 | 1.000 | 0.010 | passa |
| b07 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 16 | 1.000 | 1.000 | 0.010 | passa |
| b08 | 1.000e-04 | 0.001 | 1.000 | 0 | 1 | passa | 16 | 1.000 | 1.000 | 0.010 | passa |
| b09 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 16 | 1.000 | 1.000 | 0.010 | passa |
| b10 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 16 | 1.000 | 1.000 | 0.010 | passa |

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

Protocolo `m4-v1`. `blind_peaks.csv` SHA-256 `e6b3cb78b2bc8771e4dc4c291914a995696cbfa876e1992a42b8670a321ee0d2` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [9878.655, 12397.778], L = 2519.1 |
| FWHM medida | 0.005 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 7217 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.432e-10 (máx. |F| = 147.3) |
| Quadratura: mudança ao reduzir painel pela metade | 4.086e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.923e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.3361 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.044 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4608 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.3070, 3.3361] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 16; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 16; 1.000 |
| Tolerância de matching (quantil 0.99) | 5.503e-04 = 0.110 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 198 |
| Detecções (nulo primário / secundário) | 34 / 29 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 34 |
| Escore S; nulo (conjunto independente, B=9999) | 34; média 3.000e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.044 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.338e-10 / 2.069e-09; 1.006e-09 / 6.338e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.193e-10 / 2.071e-09; 1.008e-09 / 6.338e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 9.149e-10 / 1.226e-08; 5.850e-09 / 6.465e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.019e-08 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.730e-10 / 3.778e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.444; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.300; p = 0.001 |
| Linhas não detectadas | 13 |
| Tempo (s) | instrument: 0.8, null_shuffle: 170.2, null_gue: 58.9, synthetic: 24.0, arithmetic: 47.4 |

Figuras: `tables/b01/spectrum_z.png`, `tables/b01/coefficients.png`, `tables/b01/synthetic_calibration.png`.

### bloco b02 (zeros 13001–16000)

Protocolo `m4-v1`. `blind_peaks.csv` SHA-256 `cc80788af1559025f77d7b72a14c87db5122726ef598dad0047c7b016bb093ec` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [12398.692, 14852.514], L = 2453.8 |
| FWHM medida | 0.005 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 7030 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.517e-10 (máx. |F| = 143.2) |
| Quadratura: mudança ao reduzir painel pela metade | 5.389e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.679e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.3238 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.047 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4640 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2997, 3.3238] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 16; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 16; 1.000 |
| Tolerância de matching (quantil 0.99) | 6.802e-04 = 0.133 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 197 |
| Detecções (nulo primário / secundário) | 34 / 26 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 34 |
| Escore S; nulo (conjunto independente, B=9999) | 34; média 3.000e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.048 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.233e-10 / 8.501e-10; 7.346e-10 / 6.565e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.555e-10 / 8.561e-10; 7.396e-10 / 6.565e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 8.349e-10 / 9.213e-09; 5.475e-09 / 7.056e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 9.406e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.435e-10 / 3.604e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.415; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.302; p = 0.001 |
| Linhas não detectadas | 13 |
| Tempo (s) | instrument: 0.6, null_shuffle: 137.8, null_gue: 56.2, synthetic: 29.8, arithmetic: 45.5 |

Figuras: `tables/b02/spectrum_z.png`, `tables/b02/coefficients.png`, `tables/b02/synthetic_calibration.png`.

### bloco b03 (zeros 16001–19000)

Protocolo `m4-v1`. `blind_peaks.csv` SHA-256 `fac1999e2eadec0788ec55d0452997be0f6a7353b8566e2904b990b0dd15bb68` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [14853.311, 17255.318], L = 2402.0 |
| FWHM medida | 0.005 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6882 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 5.587e-10 (máx. |F| = 140.6) |
| Quadratura: mudança ao reduzir painel pela metade | 4.437e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.700e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.3157 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.045 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4935 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2921, 3.3157] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 16; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 16; 1.000 |
| Tolerância de matching (quantil 0.99) | 6.255e-04 = 0.120 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 197 |
| Detecções (nulo primário / secundário) | 34 / 26 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 35 |
| Escore S; nulo (conjunto independente, B=9999) | 34; média 4.000e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.047 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 0.971; detectáveis perdidas: 131 |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=16); todas as 47 linhas | 3.881e-10 / 1.161e-09; 9.405e-10 / 4.054e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 3.881e-10 / 1.165e-09; 9.301e-10 / 4.054e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.941e-10 / 2.206e-09; 1.410e-09 / 6.702e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.329e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.330e-10 / 4.323e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.403; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.268; p = 0.001 |
| Linhas não detectadas | 13 |
| Tempo (s) | instrument: 0.6, null_shuffle: 142.2, null_gue: 55.2, synthetic: 43.8, arithmetic: 46.1 |

Figuras: `tables/b03/spectrum_z.png`, `tables/b03/coefficients.png`, `tables/b03/synthetic_calibration.png`.

### bloco b04 (zeros 19001–22000)

Protocolo `m4-v1`. `blind_peaks.csv` SHA-256 `9fa0e70fe627e0110abccab49058431954c29c0fe6a82b9369e1ded7f43243f7` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [17256.388, 19616.305], L = 2359.9 |
| FWHM medida | 0.005 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6761 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 3.004e-10 (máx. |F| = 137.6) |
| Quadratura: mudança ao reduzir painel pela metade | 5.620e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.437e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.3061 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.046 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3653 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2760, 3.3061] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 16; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 16; 1.000 |
| Tolerância de matching (quantil 0.99) | 9.991e-04 = 0.188 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 210 |
| Detecções (nulo primário / secundário) | 34 / 27 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 34 |
| Escore S; nulo (conjunto independente, B=9999) | 34; média 8.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.047 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.790e-10 / 1.160e-09; 9.252e-10 / 6.541e-08 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.845e-10 / 1.156e-09; 9.213e-10 / 6.540e-08 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 8.425e-10 / 4.444e-09; 2.907e-09 / 1.483e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 4.513e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 5.826e-10 / 4.808e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.443; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.292; p = 0.001 |
| Linhas não detectadas | 13 |
| Tempo (s) | instrument: 0.6, null_shuffle: 139.3, null_gue: 63.2, synthetic: 64.0, arithmetic: 41.5 |

Figuras: `tables/b04/spectrum_z.png`, `tables/b04/coefficients.png`, `tables/b04/synthetic_calibration.png`.

### bloco b05 (zeros 22001–25000)

Protocolo `m4-v1`. `blind_peaks.csv` SHA-256 `eba2b335dcee4d85e07f854933380381f8273cc1ab991a363b7a85b0101b1919` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [19617.382, 21942.592], L = 2325.2 |
| FWHM medida | 0.005 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6662 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.407e-10 (máx. |F| = 135.4) |
| Quadratura: mudança ao reduzir painel pela metade | 3.195e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.135e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.3132 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.046 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.5412 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2828, 3.3132] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 16; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 16; 1.000 |
| Tolerância de matching (quantil 0.99) | 6.182e-04 = 0.114 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 205 |
| Detecções (nulo primário / secundário) | 34 / 26 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 35 |
| Escore S; nulo (conjunto independente, B=9999) | 34; média 6.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.047 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 0.971; detectáveis perdidas: 131 |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.801e-10 / 2.136e-09; 6.778e-10 / 3.668e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.779e-10 / 2.126e-09; 6.730e-10 / 3.668e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 1.117e-09 / 9.363e-09; 7.675e-09 / 4.890e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 8.717e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.543e-10 / 4.754e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.429; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.291; p = 0.001 |
| Linhas não detectadas | 13 |
| Tempo (s) | instrument: 0.6, null_shuffle: 176.7, null_gue: 85.5, synthetic: 103.0, arithmetic: 46.3 |

Figuras: `tables/b05/spectrum_z.png`, `tables/b05/coefficients.png`, `tables/b05/synthetic_calibration.png`.

### bloco b06 (zeros 25001–28000)

Protocolo `m4-v1`. `blind_peaks.csv` SHA-256 `c40033216ef630df265f3a51deae6810d0c690ec69181d360cc46ea974cacee7` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [21942.661, 24238.384], L = 2295.7 |
| FWHM medida | 0.005 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6577 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.679e-10 (máx. |F| = 134.1) |
| Quadratura: mudança ao reduzir painel pela metade | 8.739e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.404e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2970 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.050 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3996 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2670, 3.2970] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 16; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 16; 1.000 |
| Tolerância de matching (quantil 0.99) | 6.300e-04 = 0.115 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 213 |
| Detecções (nulo primário / secundário) | 35 / 26 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 35 |
| Escore S; nulo (conjunto independente, B=9999) | 35; média 9.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.051 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.548e-10 / 9.997e-10; 8.598e-10 / 3.419e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.733e-10 / 9.900e-10; 8.501e-10 / 3.419e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 9.783e-10 / 9.334e-09; 9.503e-09 / 3.669e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 8.739e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.323e-10 / 5.217e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.428; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.278; p = 0.001 |
| Linhas não detectadas | 12 |
| Tempo (s) | instrument: 0.7, null_shuffle: 179.6, null_gue: 57.4, synthetic: 85.0, arithmetic: 47.8 |

Figuras: `tables/b06/spectrum_z.png`, `tables/b06/coefficients.png`, `tables/b06/synthetic_calibration.png`.

### bloco b07 (zeros 28001–31000)

Protocolo `m4-v1`. `blind_peaks.csv` SHA-256 `28fc6eb3a89fb83cd04ad26b64842d209d6f3b9be6793e829c6b343b91a19aea` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [24239.882, 26508.693], L = 2268.8 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6500 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.404e-10 (máx. |F| = 131.8) |
| Quadratura: mudança ao reduzir painel pela metade | 4.066e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.258e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2877 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.051 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.5810 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2631, 3.2877] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 16; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 16; 1.000 |
| Tolerância de matching (quantil 0.99) | 7.320e-04 = 0.132 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 195 |
| Detecções (nulo primário / secundário) | 34 / 24 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 34 |
| Escore S; nulo (conjunto independente, B=9999) | 34; média 9.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.053 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=16); todas as 47 linhas | 1.672e-10 / 4.915e-10; 4.915e-10 / 4.214e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 1.668e-10 / 4.864e-10; 4.864e-10 / 4.213e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 4.359e-10 / 4.940e-09; 3.007e-09 / 8.133e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 5.104e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.628e-10 / 3.971e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.436; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.307; p = 0.001 |
| Linhas não detectadas | 13 |
| Tempo (s) | instrument: 0.6, null_shuffle: 162.1, null_gue: 57.9, synthetic: 76.2, arithmetic: 42.1 |

Figuras: `tables/b07/spectrum_z.png`, `tables/b07/coefficients.png`, `tables/b07/synthetic_calibration.png`.

### bloco b08 (zeros 31001–34000)

Protocolo `m4-v1`. `blind_peaks.csv` SHA-256 `cb6f4654a774b2bf0c5a985af8700420b326038a75b5fb27d359c951348b1086` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [26509.950, 28755.619], L = 2245.7 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6434 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 7.855e-11 (máx. |F| = 131.3) |
| Quadratura: mudança ao reduzir painel pela metade | 1.578e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.947e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.3055 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.042 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.6787 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2764, 3.3055] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 16; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 16; 1.000 |
| Tolerância de matching (quantil 0.99) | 0.001 = 0.191 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 209 |
| Detecções (nulo primário / secundário) | 33 / 23 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 33 |
| Escore S; nulo (conjunto independente, B=9999) | 33; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.044 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.377e-10 / 9.216e-10; 6.848e-10 / 1.631e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.420e-10 / 9.084e-10; 6.906e-10 / 1.631e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 3.464e-10 / 7.055e-09; 5.851e-09 / 1.283e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 7.257e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.887e-10 / 5.587e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.422; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.292; p = 0.001 |
| Linhas não detectadas | 14 |
| Tempo (s) | instrument: 0.5, null_shuffle: 190.4, null_gue: 59.5, synthetic: 73.2, arithmetic: 46.5 |

Figuras: `tables/b08/spectrum_z.png`, `tables/b08/coefficients.png`, `tables/b08/synthetic_calibration.png`.

### bloco b09 (zeros 34001–37000)

Protocolo `m4-v1`. `blind_peaks.csv` SHA-256 `34fdee448cb1d28b0232277b86084b8ef94763de7f97fcb0ae0d8d73f43f5776` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [28757.060, 30982.396], L = 2225.3 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6376 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 3.696e-10 (máx. |F| = 129.4) |
| Quadratura: mudança ao reduzir painel pela metade | 5.379e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.011e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2998 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.047 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3849 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2749, 3.2998] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 16; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 16; 1.000 |
| Tolerância de matching (quantil 0.99) | 5.599e-04 = 0.099 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 195 |
| Detecções (nulo primário / secundário) | 34 / 26 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 34 |
| Escore S; nulo (conjunto independente, B=9999) | 34; média 3.000e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.048 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=16); todas as 47 linhas | 3.497e-10 / 2.605e-09; 1.010e-09 / 9.085e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 3.420e-10 / 2.601e-09; 1.013e-09 / 9.085e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 4.070e-10 / 6.111e-09; 4.570e-09 / 1.144e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 4.224e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.157e-10 / 4.324e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.425; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.285; p = 0.001 |
| Linhas não detectadas | 13 |
| Tempo (s) | instrument: 0.5, null_shuffle: 223.5, null_gue: 54.5, synthetic: 54.5, arithmetic: 36.2 |

Figuras: `tables/b09/spectrum_z.png`, `tables/b09/coefficients.png`, `tables/b09/synthetic_calibration.png`.

### bloco b10 (zeros 37001–40000)

Protocolo `m4-v1`. `blind_peaks.csv` SHA-256 `4efa94f219334f44bb39a4018f68fdecc01a9d452ddf39a780c565f06a759ff5` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [30983.188, 33190.012], L = 2206.8 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6323 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.089e-10 (máx. |F| = 128.4) |
| Quadratura: mudança ao reduzir painel pela metade | 5.104e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 1.117e-13 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2922 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.048 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3897 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2585, 3.2922] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 16; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 16; 1.000 |
| Tolerância de matching (quantil 0.99) | 5.881e-04 = 0.103 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 199 |
| Detecções (nulo primário / secundário) | 35 / 26 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 35 |
| Escore S; nulo (conjunto independente, B=9999) | 35; média 8.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.049 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=16); todas as 47 linhas | 3.332e-10 / 1.660e-09; 9.162e-10 / 6.625e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 3.298e-10 / 1.657e-09; 9.187e-10 / 6.625e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 4.182e-10 / 2.735e-09; 3.711e-09 / 5.115e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 2.514e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.090e-10 / 4.481e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.418; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.293; p = 0.001 |
| Linhas não detectadas | 12 |
| Tempo (s) | instrument: 0.5, null_shuffle: 138.3, null_gue: 55.3, synthetic: 53.9, arithmetic: 36.1 |

Figuras: `tables/b10/spectrum_z.png`, `tables/b10/coefficients.png`, `tables/b10/synthetic_calibration.png`.

