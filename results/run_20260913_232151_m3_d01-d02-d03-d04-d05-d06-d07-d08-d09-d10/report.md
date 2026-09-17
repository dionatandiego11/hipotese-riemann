# Relatório M3 — espectroscopia inversa por blocos

**ID:** `run_20260913_232151_m3_d01-d02-d03-d04-d05-d06-d07-d08-d09-d10`
**Blocos:** d01, d02, d03, d04, d05, d06, d07, d08, d09, d10
**Duração:** 2759.4 s; pico de memória 177 MB
**Comando:** `/home/dionatandiego11/Downloads/hipotese-riemann/src/riemann_spectra/__main__.py m3 --config configs/m4_v3_bh.toml --blocks d01,d02,d03,d04,d05,d06,d07,d08,d09,d10 --workers 4`

Protocolo congelado em 2026-09-13T22:08:46.578667+00:00 (config `11da83a019a45e6c…`, módulos `69b5744ce8f7beba…`).

## Resumo por bloco

| Bloco | Índices | L | FWHM | Catálogo | Detectáveis | Detecções | S | Sem corresp. | S nulo máx | p | Recuperação | Decisões alteráveis por z refinado | mediana abs(razão−1) `band_conjugate` | mediana abs(razão−1) `band_no_conjugate` | mediana abs(razão−1) `centers_conjugate` | Δ perturbação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| d01 | 70001–73000 | 2074 | 0.008 | 47 | 25 | 25 | 25 | 0 | 1 | 0.001 | 1.000 | 0 | 4.496e-08 | 4.351e-08 | 3.446e-07 | 8.167e-09 |
| d02 | 73001–76000 | 2065 | 0.008 | 47 | 26 | 26 | 26 | 0 | 1 | 0.001 | 1.000 | 0 | 5.716e-08 | 5.532e-08 | 4.266e-07 | 8.178e-08 |
| d03 | 76001–79000 | 2058 | 0.008 | 47 | 26 | 26 | 26 | 0 | 1 | 0.001 | 1.000 | 1 | 8.014e-08 | 7.544e-08 | 6.160e-07 | 6.934e-08 |
| d04 | 79001–82000 | 2049 | 0.008 | 47 | 25 | 25 | 25 | 0 | 0 | 0.001 | 1.000 | 0 | 5.978e-08 | 6.627e-08 | 4.588e-07 | 4.487e-08 |
| d05 | 82001–85000 | 2042 | 0.008 | 47 | 26 | 26 | 26 | 0 | 1 | 0.001 | 1.000 | 0 | 3.029e-08 | 3.454e-08 | 2.311e-07 | 2.605e-08 |
| d06 | 85001–88000 | 2036 | 0.008 | 47 | 26 | 26 | 26 | 0 | 0 | 0.001 | 1.000 | 0 | 8.388e-08 | 9.154e-08 | 6.381e-07 | 6.793e-08 |
| d07 | 88001–91000 | 2029 | 0.008 | 47 | 26 | 26 | 26 | 0 | 0 | 0.001 | 1.000 | 0 | 5.388e-08 | 5.080e-08 | 4.065e-07 | 7.401e-08 |
| d08 | 91001–94000 | 2022 | 0.008 | 47 | 26 | 26 | 26 | 0 | 0 | 0.001 | 1.000 | 0 | 4.790e-08 | 5.391e-08 | 3.700e-07 | 8.978e-08 |
| d09 | 94001–97000 | 2017 | 0.008 | 47 | 26 | 26 | 26 | 0 | 1 | 0.001 | 1.000 | 0 | 3.607e-08 | 2.741e-08 | 2.742e-07 | 3.281e-08 |
| d10 | 97001–100000 | 2010 | 0.008 | 47 | 26 | 26 | 26 | 0 | 1 | 0.001 | 1.000 | 0 | 2.817e-08 | 2.254e-08 | 2.089e-07 | 7.739e-08 |

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
| d01 | 0.001 | 0.010 | 1.000 | 0 | 2 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| d02 | 0.001 | 0.010 | 1.000 | 0 | 1 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| d03 | 0.001 | 0.010 | 1.000 | 0 | 0 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| d04 | 0.001 | 0.010 | 1.000 | 0 | 1 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| d05 | 0.001 | 0.010 | 1.000 | 0 | 2 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| d06 | 0.001 | 0.010 | 1.000 | 0 | 0 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| d07 | 0.001 | 0.010 | 1.000 | 0 | 0 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| d08 | 0.001 | 0.010 | 1.000 | 0 | 1 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| d09 | 0.001 | 0.010 | 1.000 | 0 | 1 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| d10 | 0.001 | 0.010 | 1.000 | 0 | 1 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |

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

### bloco d01 (zeros 70001–73000)

Protocolo `m4-v3-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `b0bfddae90a184708cb057dd4eab274018feb332dcecc6dfe016f6967112a39d` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [54512.241, 56585.923], L = 2073.7 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4456 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.319e-10 (máx. |F| = 86.8) |
| Quadratura: mudança ao reduzir painel pela metade | 1.402e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 6.469e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2906 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.031 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4176 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1938, 3.2906] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 2 (dos quais com correspondência no catálogo: 2) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 0.001 = 0.135 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 200 |
| Detecções (nulo primário / secundário) | 25 / 16 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 25 |
| Escore S; nulo (conjunto independente, B=999) | 25; média 0.002, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.032 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 4.496e-08 / 1.175e-07; 1.032e-07 / 1.296e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 4.351e-08 / 1.033e-07; 8.881e-08 / 1.257e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 3.446e-07 / 8.972e-07; 7.960e-07 / 2.121e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.015e-06 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 8.167e-09 / 1.892e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.504; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.335; p = 0.001 |
| Linhas não detectadas | 22 |
| Tempo (s) | instrument: 0.7, null_shuffle: 21.7, null_gue: 62.4, synthetic: 71.2, arithmetic: 44.4 |

Figuras: `tables/d01/spectrum_z.png`, `tables/d01/coefficients.png`, `tables/d01/synthetic_calibration.png`.

### bloco d02 (zeros 73001–76000)

Protocolo `m4-v3-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `6a9c5baee9d9fbe9ce1507086abd192b4fb2a765348128bea9434a2f745b0553` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [56586.415, 58651.793], L = 2065.4 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4439 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 6.245e-10 (máx. |F| = 86.7) |
| Quadratura: mudança ao reduzir painel pela metade | 6.664e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.181e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.3092 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.027 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4016 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1917, 3.3092] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 9.017e-04 = 0.111 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 182 |
| Detecções (nulo primário / secundário) | 26 / 17 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.027 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 5.716e-08 / 9.920e-08; 5.659e-08 / 5.480e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 5.532e-08 / 8.988e-08; 5.916e-08 / 5.528e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 4.266e-07 / 7.584e-07; 4.266e-07 / 4.209e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 8.576e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 8.178e-08 / 2.069e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.492; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.340; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.6, null_shuffle: 18.2, null_gue: 60.0, synthetic: 90.0, arithmetic: 46.4 |

Figuras: `tables/d02/spectrum_z.png`, `tables/d02/coefficients.png`, `tables/d02/synthetic_calibration.png`.

### bloco d03 (zeros 76001–79000)

Protocolo `m4-v3-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `7a387fa90ed2024eddab174b78d950144ed8d4a5d0c7d67478c5682c3aabe2ff` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [58652.565, 60710.110], L = 2057.5 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4422 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.500e-10 (máx. |F| = 85.8) |
| Quadratura: mudança ao reduzir painel pela metade | 7.005e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.334e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.3136 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.027 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.5238 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1963, 3.3136] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.731e-04 = 0.107 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 176 |
| Detecções (nulo primário / secundário) | 26 / 16 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.027 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 8.014e-08 / 1.391e-07; 1.109e-07 / 2.539e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 7.544e-08 / 1.331e-07; 1.079e-07 / 2.574e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 6.160e-07 / 1.059e-06; 8.580e-07 / 2.478e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.198e-06 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.934e-08 / 2.346e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.524; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.358; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 1.0, null_shuffle: 24.2, null_gue: 74.9, synthetic: 71.2, arithmetic: 40.2 |

Figuras: `tables/d03/spectrum_z.png`, `tables/d03/coefficients.png`, `tables/d03/synthetic_calibration.png`.

### bloco d04 (zeros 79001–82000)

Protocolo `m4-v3-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `b78d5575e8d39183b8c95d719c34d418f8c2a6600f3d35376bd0484854325c6b` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [60710.853, 62760.177], L = 2049.3 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4404 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.770e-10 (máx. |F| = 86.0) |
| Quadratura: mudança ao reduzir painel pela metade | 1.467e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.094e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.3040 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.030 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3842 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1993, 3.3040] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 0.001 = 0.125 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 196 |
| Detecções (nulo primário / secundário) | 25 / 17 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 25 |
| Escore S; nulo (conjunto independente, B=999) | 25; média 0.000, máx. 0 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.030 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 5.978e-08 / 1.380e-07; 9.513e-08 / 4.916e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 6.627e-08 / 1.645e-07; 9.582e-08 / 4.957e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 4.588e-07 / 1.054e-06; 7.255e-07 / 3.791e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.218e-06 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 4.487e-08 / 2.630e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.513; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.356; p = 0.001 |
| Linhas não detectadas | 22 |
| Tempo (s) | instrument: 0.6, null_shuffle: 20.1, null_gue: 58.1, synthetic: 71.2, arithmetic: 56.0 |

Figuras: `tables/d04/spectrum_z.png`, `tables/d04/coefficients.png`, `tables/d04/synthetic_calibration.png`.

### bloco d05 (zeros 82001–85000)

Protocolo `m4-v3-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `e6e4ff0c7b02f3e6f8f0e8e98498d76d459ba9da2cd0a2cfaa0573cd630a7de9` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [62761.148, 64803.459], L = 2042.3 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4389 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.285e-10 (máx. |F| = 85.7) |
| Quadratura: mudança ao reduzir painel pela metade | 2.003e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 5.740e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2836 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.031 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4421 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1509, 3.2836] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 2 (dos quais com correspondência no catálogo: 2) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.957e-04 = 0.109 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 203 |
| Detecções (nulo primário / secundário) | 26 / 18 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.002, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.031 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 3.029e-08 / 8.556e-08; 8.233e-08 / 1.574e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 3.454e-08 / 8.372e-08; 8.222e-08 / 1.555e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 2.311e-07 / 6.448e-07; 5.533e-07 / 1.535e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 7.303e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 2.605e-08 / 1.365e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.539; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.362; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.9, null_shuffle: 43.0, null_gue: 85.1, synthetic: 135.0, arithmetic: 44.7 |

Figuras: `tables/d05/spectrum_z.png`, `tables/d05/coefficients.png`, `tables/d05/synthetic_calibration.png`.

### bloco d06 (zeros 85001–88000)

Protocolo `m4-v3-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `d5c3ea03161ea5bcfe7cc09c22bcabf2cebbadfa2a434c56586fe29f3d9ed6fb` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [64804.249, 66839.778], L = 2035.5 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4374 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 7.350e-11 (máx. |F| = 84.9) |
| Quadratura: mudança ao reduzir painel pela metade | 5.300e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 6.817e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.3003 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.035 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4948 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2034, 3.3003] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.277e-04 = 0.101 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 189 |
| Detecções (nulo primário / secundário) | 26 / 16 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.000, máx. 0 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.036 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 8.388e-08 / 1.015e-07; 9.672e-08 / 5.153e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 9.154e-08 / 1.081e-07; 9.594e-08 / 5.246e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 6.381e-07 / 7.673e-07; 7.358e-07 / 3.942e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 8.754e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.793e-08 / 1.964e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.512; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.365; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.7, null_shuffle: 44.3, null_gue: 92.9, synthetic: 105.3, arithmetic: 62.9 |

Figuras: `tables/d06/spectrum_z.png`, `tables/d06/coefficients.png`, `tables/d06/synthetic_calibration.png`.

### bloco d07 (zeros 88001–91000)

Protocolo `m4-v3-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `9f520f582c4b097f48028388582aaaa4aeffcd901c542c9ef18a9755dfc34d13` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [66840.412, 68869.277], L = 2028.9 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4360 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 6.480e-11 (máx. |F| = 85.0) |
| Quadratura: mudança ao reduzir painel pela metade | 6.746e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.411e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2984 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.020 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.2878 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1844, 3.2984] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 7.410e-04 = 0.090 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 191 |
| Detecções (nulo primário / secundário) | 26 / 18 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.000, máx. 0 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.022 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 5.388e-08 / 1.021e-07; 7.933e-08 / 8.837e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 5.080e-08 / 1.191e-07; 7.980e-08 / 9.787e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 4.065e-07 / 7.798e-07; 6.267e-07 / 8.622e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 8.989e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.401e-08 / 1.920e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.496; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.371; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 1.0, null_shuffle: 42.4, null_gue: 104.3, synthetic: 124.9, arithmetic: 54.4 |

Figuras: `tables/d07/spectrum_z.png`, `tables/d07/coefficients.png`, `tables/d07/synthetic_calibration.png`.

### bloco d08 (zeros 91001–94000)

Protocolo `m4-v3-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `c26bef03425c9085500f2b48cb30cf7bb0df3e384de38be6f14325e086bb09ee` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [68870.288, 70892.743], L = 2022.5 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4346 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.746e-10 (máx. |F| = 84.4) |
| Quadratura: mudança ao reduzir painel pela metade | 3.851e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 5.762e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2525 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.043 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4294 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1528, 3.2525] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.557e-04 = 0.103 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 189 |
| Detecções (nulo primário / secundário) | 26 / 17 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.000, máx. 0 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.043 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 4.790e-08 / 1.049e-07; 6.531e-08 / 7.484e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 5.391e-08 / 1.086e-07; 6.320e-08 / 7.502e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 3.700e-07 / 8.017e-07; 4.714e-07 / 5.824e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 9.103e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 8.978e-08 / 2.003e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.509; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.363; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.8, null_shuffle: 43.0, null_gue: 84.2, synthetic: 116.8, arithmetic: 53.4 |

Figuras: `tables/d08/spectrum_z.png`, `tables/d08/coefficients.png`, `tables/d08/synthetic_calibration.png`.

### bloco d09 (zeros 94001–97000)

Protocolo `m4-v3-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `0e8b80c4740d5f92282765a3a3ccbcce17c2ff3c8c9a0e4179a750cec25def1c` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [70893.252, 72910.135], L = 2016.9 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4334 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.533e-10 (máx. |F| = 83.9) |
| Quadratura: mudança ao reduzir painel pela metade | 7.859e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 9.375e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2718 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.031 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4629 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1830, 3.2718] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 9.017e-04 = 0.109 FWHM |
| Separação de pares com ≥90% recuperado | 1.00 FWHM (medida) |
| Linhas sintéticas isoladas | 188 |
| Detecções (nulo primário / secundário) | 26 / 16 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.031 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 3.607e-08 / 6.132e-08; 6.288e-08 / 1.071e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 2.741e-08 / 4.389e-08; 4.793e-08 / 1.026e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 2.742e-07 / 4.714e-07; 4.825e-07 / 8.025e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 5.327e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 3.281e-08 / 1.135e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.531; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.324; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.8, null_shuffle: 46.3, null_gue: 90.6, synthetic: 120.1, arithmetic: 62.1 |

Figuras: `tables/d09/spectrum_z.png`, `tables/d09/coefficients.png`, `tables/d09/synthetic_calibration.png`.

### bloco d10 (zeros 97001–100000)

Protocolo `m4-v3-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `b483def168a7a625b74fd57ef4b72bf47da781bd01645b9b7cddfd15db7c5ba0` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [72910.657, 74920.827], L = 2010.2 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4320 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.960e-10 (máx. |F| = 84.4) |
| Quadratura: mudança ao reduzir painel pela metade | 6.617e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 5.289e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2571 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.052 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.2922 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1719, 3.2571] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.126e-04 = 0.097 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 202 |
| Detecções (nulo primário / secundário) | 26 / 19 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.053 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 2.817e-08 / 8.314e-08; 6.061e-08 / 1.135e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 2.254e-08 / 9.143e-08; 6.532e-08 / 1.221e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 2.089e-07 / 6.342e-07; 4.891e-07 / 9.203e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 7.256e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.739e-08 / 1.991e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.513; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.350; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 1.0, null_shuffle: 46.6, null_gue: 99.1, synthetic: 155.8, arithmetic: 60.5 |

Figuras: `tables/d10/spectrum_z.png`, `tables/d10/coefficients.png`, `tables/d10/synthetic_calibration.png`.

