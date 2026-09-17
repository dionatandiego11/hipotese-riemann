# Relatório M3 — espectroscopia inversa por blocos

**ID:** `run_20260913_132814_m3_pilot-dev-val-holdout-full`
**Blocos:** pilot, dev, val, holdout, full
**Duração:** 1663.6 s; pico de memória 292 MB
**Comando:** `/home/dionatandiego11/Downloads/hipotese-riemann/src/riemann_spectra/__main__.py m3 --config configs/m3_protocol_v3_bh.toml --blocks pilot,dev,val,holdout,full --workers 4`

Protocolo congelado em 2026-09-13T13:28:11.440554+00:00 (config `571416ec9fec94e9…`, módulos `7e6210fb3d25dadf…`).

## Resumo por bloco

| Bloco | Índices | L | FWHM | Catálogo | Detectáveis | Detecções | S | Sem corresp. | S nulo máx | p | Recuperação | Decisões alteráveis por z refinado | mediana abs(razão−1) `band_conjugate` | mediana abs(razão−1) `band_no_conjugate` | mediana abs(razão−1) `centers_conjugate` | Δ perturbação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pilot | 1–1000 | 1405 | 0.012 | 47 | 14 | 14 | 14 | 0 | 1 | 0.001 | 1.000 | 0 | 7.462e-08 | 7.115e-08 | 5.696e-07 | 1.025e-07 |
| dev | 1001–4000 | 3086 | 0.005 | 47 | 29 | 29 | 29 | 0 | 1 | 0.001 | 1.000 | 0 | 3.287e-08 | 2.861e-08 | 2.447e-07 | 4.094e-08 |
| val | 4001–7000 | 2757 | 0.006 | 47 | 27 | 27 | 27 | 0 | 0 | 0.001 | 1.000 | 0 | 3.915e-08 | 3.376e-08 | 3.068e-07 | 3.658e-08 |
| holdout | 7001–10000 | 2612 | 0.006 | 47 | 29 | 29 | 29 | 0 | 1 | 0.001 | 1.000 | 0 | 3.696e-08 | 3.904e-08 | 2.844e-07 | 3.505e-08 |
| full | 1–10000 | 9864 | 0.002 | 47 | 41 | 41 | 41 | 0 | 0 | 0.001 | 1.000 | 0 | 1.646e-08 | 1.507e-08 | 1.265e-07 | 9.467e-09 |

Definições: *Detecções* são máximos locais de z = |F|/σ_nulo, avaliado na malha para zeros, controles e sintéticos,
acima do limiar FWER do nulo de permutação de espaçamentos, obtidos sem catálogo. O limiar e o escore global usam
conjuntos nulos independentes. *S* conta linhas r log p com uma detecção a menos da tolerância calibrada (um a um).
*p* compara S com a mesma cadeia aplicada a cada realização nula. *Recuperação* é a fração das linhas cujo
coeficiente de referência excede o limite de detecção previsto pelo nulo. As colunas de razão e fase vêm da
**medição direcionada** nos períodos conhecidos (ajuste conjunto com a resposta da janela), que não é detecção cega.

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

### bloco pilot (zeros 1–1000)

Protocolo `m3-v3-blackman-harris`. `blind_peaks.csv` SHA-256 `e137ec95a08f3f827436f2d625e516d82066b6e7c57731ca6a0ffa1b160a0b29` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [14.135, 1419.422], L = 1405.3 |
| FWHM medida | 0.012 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 3020 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 4.893e-11 (máx. |F| = 58.9) |
| Quadratura: mudança ao reduzir painel pela metade | 6.892e-12 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 3.638e-09 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.1437 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.056 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.1740 |
| Candidatos cuja decisão mudaria usando z refinado | 0 |
| Tolerância de matching (quantil 0.99) | 8.829e-04 = 0.074 FWHM |
| Separação de pares com ≥90% recuperado | 2.00 FWHM (não atingiu a meta; usada a maior separação testada) |
| Linhas sintéticas isoladas | 28 |
| Detecções (nulo primário / secundário) | 14 / 12 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 37 resolvidas |
| Previstas detectáveis | 14 |
| Escore S; nulo (conjunto independente, B=999) | 14; média 0.002, máx. 1 |
| Detecções sem correspondente; detecções por realização nula | 0; 0.058 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=14); todas as 47 linhas | 7.462e-08 / 1.661e-07; 8.302e-08 / 3.749e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=14); todas as 47 linhas | 7.115e-08 / 1.631e-07; 7.224e-08 / 3.561e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=14); todas as 47 linhas | 5.696e-07 / 1.266e-06; 5.727e-07 / 5.212e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.432e-06 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 1.025e-07 / 3.581e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.456; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.308; p = 0.001 |
| Linhas não detectadas | 33 |
| Tempo (s) | instrument: 0.6, null_shuffle: 5.3, null_gue: 7.8, synthetic: 2.6, arithmetic: 40.2 |

Figuras: `tables/pilot/spectrum_z.png`, `tables/pilot/coefficients.png`, `tables/pilot/synthetic_calibration.png`.

### bloco dev (zeros 1001–4000)

Protocolo `m3-v3-blackman-harris`. `blind_peaks.csv` SHA-256 `6c0868a19e3266e5bd4e38ff4abd916a76bece845a4d3a85ce3153bd1bd2f724` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [1420.417, 4506.311], L = 3085.9 |
| FWHM medida | 0.005 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 6631 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.719e-10 (máx. |F| = 128.7) |
| Quadratura: mudança ao reduzir painel pela metade | 7.494e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 4.833e-13 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2784 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.053 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3098 |
| Candidatos cuja decisão mudaria usando z refinado | 0 |
| Tolerância de matching (quantil 0.99) | 5.939e-04 = 0.109 FWHM |
| Separação de pares com ≥90% recuperado | 1.00 FWHM (medida) |
| Linhas sintéticas isoladas | 155 |
| Detecções (nulo primário / secundário) | 29 / 28 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 29 |
| Escore S; nulo (conjunto independente, B=999) | 29; média 0.001, máx. 1 |
| Detecções sem correspondente; detecções por realização nula | 0; 0.056 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=29); todas as 47 linhas | 3.287e-08 / 9.573e-08; 5.495e-08 / 7.756e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=29); todas as 47 linhas | 2.861e-08 / 9.051e-08; 5.333e-08 / 7.871e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=29); todas as 47 linhas | 2.447e-07 / 7.368e-07; 4.205e-07 / 6.500e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 8.325e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 4.094e-08 / 1.620e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.330; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.222; p = 0.001 |
| Linhas não detectadas | 18 |
| Tempo (s) | instrument: 0.8, null_shuffle: 20.5, null_gue: 62.3, synthetic: 28.5, arithmetic: 66.5 |

Figuras: `tables/dev/spectrum_z.png`, `tables/dev/coefficients.png`, `tables/dev/synthetic_calibration.png`.

### bloco val (zeros 4001–7000)

Protocolo `m3-v3-blackman-harris`. `blind_peaks.csv` SHA-256 `8ec9dacf2db6c68f54db0682f4aa7b7adb414ab2841084728b20971ad3a77300` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [4507.745, 7264.748], L = 2757.0 |
| FWHM medida | 0.006 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 5925 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 9.512e-11 (máx. |F| = 114.7) |
| Quadratura: mudança ao reduzir painel pela metade | 6.924e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.540e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.3190 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.039 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.1934 |
| Candidatos cuja decisão mudaria usando z refinado | 0 |
| Tolerância de matching (quantil 0.99) | 5.968e-04 = 0.098 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 162 |
| Detecções (nulo primário / secundário) | 27 / 27 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 27 |
| Escore S; nulo (conjunto independente, B=999) | 27; média 0.000, máx. 0 |
| Detecções sem correspondente; detecções por realização nula | 0; 0.040 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=27); todas as 47 linhas | 3.915e-08 / 1.127e-07; 4.545e-08 / 3.846e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=27); todas as 47 linhas | 3.376e-08 / 1.144e-07; 5.162e-08 / 4.974e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=27); todas as 47 linhas | 3.068e-07 / 8.580e-07; 3.464e-07 / 5.303e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 9.706e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 3.658e-08 / 2.202e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.323; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.209; p = 0.001 |
| Linhas não detectadas | 20 |
| Tempo (s) | instrument: 0.8, null_shuffle: 22.0, null_gue: 64.0, synthetic: 25.3, arithmetic: 55.5 |

Figuras: `tables/val/spectrum_z.png`, `tables/val/coefficients.png`, `tables/val/synthetic_calibration.png`.

### bloco holdout (zeros 7001–10000)

Protocolo `m3-v3-blackman-harris`. `blind_peaks.csv` SHA-256 `8a2806457edd04224bbfe7d9b7e94c2ceff9469ca6572f59ced632576b5a398c` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [7265.963, 9877.783], L = 2611.8 |
| FWHM medida | 0.006 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 5613 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.647e-10 (máx. |F| = 109.3) |
| Quadratura: mudança ao reduzir painel pela metade | 6.331e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 6.493e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2494 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.053 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.2191 |
| Candidatos cuja decisão mudaria usando z refinado | 0 |
| Tolerância de matching (quantil 0.99) | 8.650e-04 = 0.135 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 174 |
| Detecções (nulo primário / secundário) | 29 / 25 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 29 |
| Escore S; nulo (conjunto independente, B=999) | 29; média 0.001, máx. 1 |
| Detecções sem correspondente; detecções por realização nula | 0; 0.054 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=29); todas as 47 linhas | 3.696e-08 / 2.509e-07; 6.113e-08 / 1.002e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=29); todas as 47 linhas | 3.904e-08 / 2.470e-07; 6.320e-08 / 1.005e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=29); todas as 47 linhas | 2.844e-07 / 1.919e-06; 4.684e-07 / 1.132e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 2.170e-06 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 3.505e-08 / 1.751e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.326; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.233; p = 0.001 |
| Linhas não detectadas | 18 |
| Tempo (s) | instrument: 1.0, null_shuffle: 23.7, null_gue: 68.2, synthetic: 25.5, arithmetic: 62.2 |

Figuras: `tables/holdout/spectrum_z.png`, `tables/holdout/coefficients.png`, `tables/holdout/synthetic_calibration.png`.

### bloco full (zeros 1–10000)

Protocolo `m3-v3-blackman-harris`. `blind_peaks.csv` SHA-256 `6fd3a9640f7644ac5f279fab088449da5c5c1d3833416f37ead23913722fb6c7` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [14.135, 9877.783], L = 9863.6 |
| FWHM medida | 0.002 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 21195 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 3.125e-10 (máx. |F| = 413.6) |
| Quadratura: mudança ao reduzir painel pela metade | 7.978e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 3.742e-09 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.4658 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.056 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4413 |
| Candidatos cuja decisão mudaria usando z refinado | 0 |
| Tolerância de matching (quantil 0.99) | 1.894e-04 = 0.112 FWHM |
| Separação de pares com ≥90% recuperado | 2.00 FWHM (não atingiu a meta; usada a maior separação testada) |
| Linhas sintéticas isoladas | 59 |
| Detecções (nulo primário / secundário) | 41 / 39 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 41 |
| Escore S; nulo (conjunto independente, B=999) | 41; média 0.000, máx. 0 |
| Detecções sem correspondente; detecções por realização nula | 0; 0.059 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=41); todas as 47 linhas | 1.646e-08 / 7.960e-08; 1.804e-08 / 5.463e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=41); todas as 47 linhas | 1.507e-08 / 7.921e-08; 1.802e-08 / 5.480e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=41); todas as 47 linhas | 1.265e-07 / 6.097e-07; 1.427e-07 / 4.148e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 6.893e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 9.467e-09 / 1.059e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.272; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.185; p = 0.001 |
| Linhas não detectadas | 6 |
| Tempo (s) | instrument: 2.4, null_shuffle: 91.8, null_gue: 603.1, synthetic: 171.6, arithmetic: 209.5 |

Figuras: `tables/full/spectrum_z.png`, `tables/full/coefficients.png`, `tables/full/synthetic_calibration.png`.

