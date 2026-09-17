# Relatório M3 — espectroscopia inversa por blocos

**ID:** `run_20260913_220906_m3_d01-d02-d03-d04-d05-d06-d07-d08-d09-d10`
**Blocos:** d01, d02, d03, d04, d05, d06, d07, d08, d09, d10
**Duração:** 4334.6 s; pico de memória 187 MB
**Comando:** `/home/dionatandiego11/Downloads/hipotese-riemann/src/riemann_spectra/__main__.py m3 --config configs/m4_v3.toml --blocks d01,d02,d03,d04,d05,d06,d07,d08,d09,d10 --workers 4`

Protocolo congelado em 2026-09-13T22:08:46.202808+00:00 (config `6bd825dcfb4a6c0f…`, módulos `69b5744ce8f7beba…`).

## Resumo por bloco

| Bloco | Índices | L | FWHM | Catálogo | Detectáveis | Detecções | S | Sem corresp. | S nulo máx | p | Recuperação | Decisões alteráveis por z refinado | mediana abs(razão−1) `band_conjugate` | mediana abs(razão−1) `band_no_conjugate` | mediana abs(razão−1) `centers_conjugate` | Δ perturbação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| d01 | 70001–73000 | 2074 | 0.006 | 47 | 32 | 32 | 32 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 2.216e-10 | 2.630e-10 | 5.727e-10 | 7.973e-10 |
| d02 | 73001–76000 | 2065 | 0.006 | 47 | 32 | 32 | 32 | 0 | 1 | 1.000e-04 | 1.000 | 1 | 3.970e-10 | 3.994e-10 | 1.148e-09 | 6.712e-10 |
| d03 | 76001–79000 | 2058 | 0.006 | 47 | 32 | 32 | 32 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 4.160e-10 | 4.182e-10 | 8.358e-10 | 6.947e-10 |
| d04 | 79001–82000 | 2049 | 0.006 | 47 | 33 | 32 | 32 | 0 | 1 | 1.000e-04 | 0.970 | 1 | 3.401e-10 | 3.831e-10 | 8.580e-10 | 6.574e-10 |
| d05 | 82001–85000 | 2042 | 0.006 | 47 | 33 | 33 | 33 | 0 | 1 | 1.000e-04 | 1.000 | 1 | 3.558e-10 | 3.780e-10 | 7.869e-10 | 7.259e-10 |
| d06 | 85001–88000 | 2036 | 0.006 | 47 | 33 | 32 | 32 | 0 | 1 | 1.000e-04 | 0.970 | 2 | 3.000e-10 | 2.807e-10 | 1.142e-09 | 7.693e-10 |
| d07 | 88001–91000 | 2029 | 0.006 | 47 | 33 | 33 | 33 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 1.311e-10 | 9.712e-11 | 6.077e-10 | 7.437e-10 |
| d08 | 91001–94000 | 2022 | 0.006 | 47 | 33 | 32 | 32 | 0 | 1 | 1.000e-04 | 0.970 | 1 | 3.951e-10 | 3.912e-10 | 6.140e-10 | 6.974e-10 |
| d09 | 94001–97000 | 2017 | 0.006 | 47 | 33 | 33 | 33 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 3.308e-10 | 4.323e-10 | 4.391e-10 | 7.644e-10 |
| d10 | 97001–100000 | 2010 | 0.006 | 47 | 32 | 32 | 32 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 3.303e-10 | 4.097e-10 | 7.479e-10 | 6.715e-10 |

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
| d01 | 1.000e-04 | 0.001 | 1.000 | 0 | 1 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| d02 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| d03 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| d04 | 1.000e-04 | 0.001 | 1.000 | 0 | 1 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| d05 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| d06 | 1.000e-04 | 0.001 | 1.000 | 0 | 1 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| d07 | 1.000e-04 | 0.001 | 1.000 | 0 | 1 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| d08 | 1.000e-04 | 0.001 | 1.000 | 0 | 1 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| d09 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| d10 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |

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

Protocolo `m4-v3`. `blind_peaks.csv` SHA-256 `95580bc56b28e7e3eab302e9a9f50f9088b0ecc778988dba8e2cb16fa3fa5273` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [54512.241, 56585.923], L = 2073.7 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 5941 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.495e-10 (máx. |F| = 121.2) |
| Quadratura: mudança ao reduzir painel pela metade | 2.294e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 1.107e-13 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2965 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.043 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.5114 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2642, 3.2965] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.280e-04 = 0.137 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 221 |
| Detecções (nulo primário / secundário) | 32 / 24 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 32 |
| Escore S; nulo (conjunto independente, B=9999) | 32; média 6.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.044 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 2.216e-10 / 2.185e-09; 1.595e-09 / 1.497e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 2.630e-10 / 2.177e-09; 1.592e-09 / 1.497e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 5.727e-10 / 1.465e-08; 1.324e-08 / 2.914e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.415e-08 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.973e-10 / 4.869e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.434; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.294; p = 0.001 |
| Linhas não detectadas | 15 |
| Tempo (s) | instrument: 0.6, null_shuffle: 164.3, null_gue: 86.6, synthetic: 76.0, arithmetic: 38.1 |

Figuras: `tables/d01/spectrum_z.png`, `tables/d01/coefficients.png`, `tables/d01/synthetic_calibration.png`.

### bloco d02 (zeros 73001–76000)

Protocolo `m4-v3`. `blind_peaks.csv` SHA-256 `94ff2a4ce7873a8587ec181d6ef83a69dc90b608b5f0ba95fdab51f60d528d70` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [56586.415, 58651.793], L = 2065.4 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 5917 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 6.090e-10 (máx. |F| = 120.7) |
| Quadratura: mudança ao reduzir painel pela metade | 8.362e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.165e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2998 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.044 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4553 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2692, 3.2998] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 7.488e-04 = 0.123 FWHM |
| Separação de pares com ≥90% recuperado | 1.50 FWHM (medida) |
| Linhas sintéticas isoladas | 210 |
| Detecções (nulo primário / secundário) | 32 / 25 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 32 |
| Escore S; nulo (conjunto independente, B=9999) | 32; média 7.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.045 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 3.970e-10 / 9.575e-10; 9.311e-10 / 1.782e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 3.994e-10 / 9.621e-10; 9.235e-10 / 1.782e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 1.148e-09 / 1.055e-08; 1.055e-08 / 1.736e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.031e-08 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.712e-10 / 4.631e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.441; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.303; p = 0.001 |
| Linhas não detectadas | 15 |
| Tempo (s) | instrument: 0.5, null_shuffle: 217.8, null_gue: 68.6, synthetic: 78.5, arithmetic: 45.2 |

Figuras: `tables/d02/spectrum_z.png`, `tables/d02/coefficients.png`, `tables/d02/synthetic_calibration.png`.

### bloco d03 (zeros 76001–79000)

Protocolo `m4-v3`. `blind_peaks.csv` SHA-256 `fb10cf04ceeb41b368d5c49696ca3a1f02373ef58fdf8b21c68e922552656b41` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [58652.565, 60710.110], L = 2057.5 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 5895 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.260e-10 (máx. |F| = 120.4) |
| Quadratura: mudança ao reduzir painel pela metade | 1.039e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.558e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2918 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.046 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.5835 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2634, 3.2918] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 6.562e-04 = 0.107 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 198 |
| Detecções (nulo primário / secundário) | 32 / 22 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 32 |
| Escore S; nulo (conjunto independente, B=9999) | 32; média 9.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.048 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 4.160e-10 / 1.883e-09; 1.410e-09 / 1.666e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 4.182e-10 / 1.879e-09; 1.409e-09 / 1.666e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 8.358e-10 / 1.380e-08; 1.380e-08 / 2.279e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.316e-08 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.947e-10 / 4.110e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.448; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.285; p = 0.001 |
| Linhas não detectadas | 15 |
| Tempo (s) | instrument: 0.9, null_shuffle: 244.1, null_gue: 75.2, synthetic: 194.9, arithmetic: 70.3 |

Figuras: `tables/d03/spectrum_z.png`, `tables/d03/coefficients.png`, `tables/d03/synthetic_calibration.png`.

### bloco d04 (zeros 79001–82000)

Protocolo `m4-v3`. `blind_peaks.csv` SHA-256 `4be89e96d0754576b914cce1595b69590822a6ae2487a8d7ab114c7c6cddce07` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [60710.853, 62760.177], L = 2049.3 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 5871 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 7.574e-11 (máx. |F| = 119.2) |
| Quadratura: mudança ao reduzir painel pela metade | 2.007e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 9.766e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2870 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.043 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.5484 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2601, 3.2870] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 6.732e-04 = 0.110 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 219 |
| Detecções (nulo primário / secundário) | 32 / 24 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 33 |
| Escore S; nulo (conjunto independente, B=9999) | 32; média 6.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.044 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 0.970; detectáveis perdidas: 127 |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 3.401e-10 / 1.543e-09; 8.699e-10 / 1.935e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 3.831e-10 / 1.543e-09; 8.645e-10 / 1.935e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 8.580e-10 / 5.757e-09; 5.757e-09 / 2.130e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 5.130e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.574e-10 / 5.486e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.426; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.300; p = 0.001 |
| Linhas não detectadas | 15 |
| Tempo (s) | instrument: 0.9, null_shuffle: 424.0, null_gue: 93.7, synthetic: 76.1, arithmetic: 37.2 |

Figuras: `tables/d04/spectrum_z.png`, `tables/d04/coefficients.png`, `tables/d04/synthetic_calibration.png`.

### bloco d05 (zeros 82001–85000)

Protocolo `m4-v3`. `blind_peaks.csv` SHA-256 `65855a92891aa7af9459d6c0e303d25a1d8c0b09c7708765cf11dbc1bff689bb` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [62761.148, 64803.459], L = 2042.3 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 5851 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.881e-10 (máx. |F| = 119.5) |
| Quadratura: mudança ao reduzir painel pela metade | 1.328e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 9.766e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.3045 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.044 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4243 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2742, 3.3045] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.930e-04 = 0.145 FWHM |
| Separação de pares com ≥90% recuperado | 1.00 FWHM (medida) |
| Linhas sintéticas isoladas | 222 |
| Detecções (nulo primário / secundário) | 33 / 24 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 33 |
| Escore S; nulo (conjunto independente, B=9999) | 33; média 9.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.046 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 3.558e-10 / 1.382e-09; 1.151e-09 / 1.341e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 3.780e-10 / 1.389e-09; 1.150e-09 / 1.341e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 7.869e-10 / 6.365e-09; 8.453e-09 / 1.258e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 4.983e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.259e-10 / 4.012e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.432; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.299; p = 0.001 |
| Linhas não detectadas | 14 |
| Tempo (s) | instrument: 0.5, null_shuffle: 168.9, null_gue: 61.7, synthetic: 72.5, arithmetic: 45.2 |

Figuras: `tables/d05/spectrum_z.png`, `tables/d05/coefficients.png`, `tables/d05/synthetic_calibration.png`.

### bloco d06 (zeros 85001–88000)

Protocolo `m4-v3`. `blind_peaks.csv` SHA-256 `37cd40254729da704f4416a2cd2bbf890a363b2ef85ceaf73003d8f6f5543e75` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [64804.249, 66839.778], L = 2035.5 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 5832 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 5.853e-11 (máx. |F| = 118.7) |
| Quadratura: mudança ao reduzir painel pela metade | 7.857e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.450e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2985 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.041 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.6414 |
| Candidatos cuja classificação mudaria usando z refinado | 2 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2695, 3.2985] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 7.171e-04 = 0.116 FWHM |
| Separação de pares com ≥90% recuperado | 1.00 FWHM (medida) |
| Linhas sintéticas isoladas | 222 |
| Detecções (nulo primário / secundário) | 32 / 20 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 33 |
| Escore S; nulo (conjunto independente, B=9999) | 32; média 8.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.042 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 0.970; detectáveis perdidas: 127 |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 3.000e-10 / 1.307e-09; 1.775e-09 / 9.543e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 2.807e-10 / 1.298e-09; 1.780e-09 / 9.543e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 1.142e-09 / 4.576e-09; 1.710e-08 / 5.644e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 5.036e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.693e-10 / 4.626e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.450; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.299; p = 0.001 |
| Linhas não detectadas | 15 |
| Tempo (s) | instrument: 0.5, null_shuffle: 196.4, null_gue: 64.2, synthetic: 67.8, arithmetic: 63.3 |

Figuras: `tables/d06/spectrum_z.png`, `tables/d06/coefficients.png`, `tables/d06/synthetic_calibration.png`.

### bloco d07 (zeros 88001–91000)

Protocolo `m4-v3`. `blind_peaks.csv` SHA-256 `9d2408c00d781c09c1ca8d07e9eef7223063e79861d92f45d2630e2185b2236b` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [66840.412, 68869.277], L = 2028.9 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 5813 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 9.810e-11 (máx. |F| = 117.8) |
| Quadratura: mudança ao reduzir painel pela metade | 9.515e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.694e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2958 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.043 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.6118 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2685, 3.2958] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.192e-04 = 0.132 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 224 |
| Detecções (nulo primário / secundário) | 33 / 23 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 33 |
| Escore S; nulo (conjunto independente, B=9999) | 33; média 9.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.043 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 1.311e-10 / 7.381e-10; 7.381e-10 / 4.705e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 9.712e-11 / 7.393e-10; 7.393e-10 / 4.705e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 6.077e-10 / 1.835e-09; 3.265e-09 / 1.427e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.801e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.437e-10 / 6.434e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.452; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.302; p = 0.001 |
| Linhas não detectadas | 14 |
| Tempo (s) | instrument: 0.5, null_shuffle: 219.9, null_gue: 56.6, synthetic: 79.5, arithmetic: 45.1 |

Figuras: `tables/d07/spectrum_z.png`, `tables/d07/coefficients.png`, `tables/d07/synthetic_calibration.png`.

### bloco d08 (zeros 91001–94000)

Protocolo `m4-v3`. `blind_peaks.csv` SHA-256 `cd6fc83f0ff1f1d7ea8a336ea9143faae3eb7d7296b4807bcafcbe7143497edb` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [68870.288, 70892.743], L = 2022.5 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 5794 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 3.503e-10 (máx. |F| = 117.8) |
| Quadratura: mudança ao reduzir painel pela metade | 1.047e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.990e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2884 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.046 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.5873 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2560, 3.2884] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.149e-04 = 0.131 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 215 |
| Detecções (nulo primário / secundário) | 32 / 21 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 33 |
| Escore S; nulo (conjunto independente, B=9999) | 32; média 6.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.047 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 0.970; detectáveis perdidas: 127 |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 3.951e-10 / 2.184e-09; 1.170e-09 / 8.974e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 3.912e-10 / 2.189e-09; 1.182e-09 / 8.974e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 6.140e-10 / 8.040e-09; 7.444e-09 / 8.809e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 5.856e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.974e-10 / 4.920e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.447; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.287; p = 0.001 |
| Linhas não detectadas | 15 |
| Tempo (s) | instrument: 0.5, null_shuffle: 195.3, null_gue: 65.2, synthetic: 96.5, arithmetic: 37.7 |

Figuras: `tables/d08/spectrum_z.png`, `tables/d08/coefficients.png`, `tables/d08/synthetic_calibration.png`.

### bloco d09 (zeros 94001–97000)

Protocolo `m4-v3`. `blind_peaks.csv` SHA-256 `3d5560c52c779b7b77bedf127f86f0546d1cb9727e3e03d77a1d76620b537d1c` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [70893.252, 72910.135], L = 2016.9 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 5778 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.374e-10 (máx. |F| = 117.0) |
| Quadratura: mudança ao reduzir painel pela metade | 2.220e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 9.520e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2947 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.046 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.5765 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2695, 3.2947] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 7.889e-04 = 0.127 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 208 |
| Detecções (nulo primário / secundário) | 33 / 20 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 33 |
| Escore S; nulo (conjunto independente, B=9999) | 33; média 7.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.047 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 3.308e-10 / 1.442e-09; 1.037e-09 / 1.689e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 4.323e-10 / 1.452e-09; 1.036e-09 / 1.689e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 4.391e-10 / 3.735e-09; 4.012e-09 / 2.100e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 2.293e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.644e-10 / 6.058e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.448; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.304; p = 0.001 |
| Linhas não detectadas | 14 |
| Tempo (s) | instrument: 0.6, null_shuffle: 256.0, null_gue: 68.3, synthetic: 94.5, arithmetic: 42.8 |

Figuras: `tables/d09/spectrum_z.png`, `tables/d09/coefficients.png`, `tables/d09/synthetic_calibration.png`.

### bloco d10 (zeros 97001–100000)

Protocolo `m4-v3`. `blind_peaks.csv` SHA-256 `1784ede4bcd06754850cf17ec8d445b74f5d9eeed190c67b1989c58af136068b` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [72910.657, 74920.827], L = 2010.2 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 5759 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 8.789e-11 (máx. |F| = 117.1) |
| Quadratura: mudança ao reduzir painel pela metade | 9.349e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 9.064e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2905 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.048 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4138 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2604, 3.2905] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 7.162e-04 = 0.115 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 218 |
| Detecções (nulo primário / secundário) | 32 / 24 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 32 |
| Escore S; nulo (conjunto independente, B=9999) | 32; média 7.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.049 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 3.303e-10 / 1.756e-09; 1.258e-09 / 2.771e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 4.097e-10 / 1.739e-09; 1.267e-09 / 2.771e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 7.479e-10 / 3.125e-09; 5.488e-09 / 2.441e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 2.599e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.715e-10 / 4.397e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.427; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.299; p = 0.001 |
| Linhas não detectadas | 15 |
| Tempo (s) | instrument: 0.5, null_shuffle: 173.2, null_gue: 58.9, synthetic: 64.6, arithmetic: 41.0 |

Figuras: `tables/d10/spectrum_z.png`, `tables/d10/coefficients.png`, `tables/d10/synthetic_calibration.png`.

