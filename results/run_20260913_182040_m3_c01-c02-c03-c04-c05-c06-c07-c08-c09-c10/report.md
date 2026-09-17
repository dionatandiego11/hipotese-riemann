# Relatório M3 — espectroscopia inversa por blocos

**ID:** `run_20260913_182040_m3_c01-c02-c03-c04-c05-c06-c07-c08-c09-c10`
**Blocos:** c01, c02, c03, c04, c05, c06, c07, c08, c09, c10
**Duração:** 1567.3 s; pico de memória 177 MB
**Comando:** `/home/dionatandiego11/Downloads/hipotese-riemann/src/riemann_spectra/__main__.py m3 --config configs/m4_v2_bh.toml --blocks c01,c02,c03,c04,c05,c06,c07,c08,c09,c10 --workers 4`

Protocolo congelado em 2026-09-13T17:30:29.894127+00:00 (config `b2f8dd1077bf89d7…`, módulos `5885b75ea98233af…`).

## Resumo por bloco

| Bloco | Índices | L | FWHM | Catálogo | Detectáveis | Detecções | S | Sem corresp. | S nulo máx | p | Recuperação | Decisões alteráveis por z refinado | mediana abs(razão−1) `band_conjugate` | mediana abs(razão−1) `band_no_conjugate` | mediana abs(razão−1) `centers_conjugate` | Δ perturbação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| c01 | 40001–43000 | 2190 | 0.008 | 47 | 27 | 27 | 27 | 0 | 1 | 0.001 | 1.000 | 0 | 3.345e-08 | 3.285e-08 | 2.530e-07 | 4.870e-08 |
| c02 | 43001–46000 | 2174 | 0.008 | 47 | 26 | 26 | 26 | 0 | 1 | 0.001 | 1.000 | 0 | 3.935e-08 | 3.835e-08 | 2.970e-07 | 4.683e-08 |
| c03 | 46001–49000 | 2160 | 0.008 | 47 | 26 | 26 | 26 | 0 | 0 | 0.001 | 1.000 | 0 | 2.421e-08 | 2.104e-08 | 1.864e-07 | 5.367e-08 |
| c04 | 49001–52000 | 2147 | 0.008 | 47 | 26 | 26 | 26 | 0 | 1 | 0.001 | 1.000 | 0 | 2.248e-08 | 2.853e-08 | 1.714e-07 | 2.710e-08 |
| c05 | 52001–55000 | 2134 | 0.008 | 47 | 26 | 25 | 25 | 0 | 1 | 0.001 | 0.962 | 1 | 3.548e-08 | 3.592e-08 | 2.714e-07 | 3.715e-08 |
| c06 | 55001–58000 | 2123 | 0.008 | 47 | 26 | 26 | 26 | 0 | 0 | 0.001 | 1.000 | 0 | 5.449e-08 | 4.445e-08 | 4.200e-07 | 6.078e-08 |
| c07 | 58001–61000 | 2111 | 0.008 | 47 | 26 | 26 | 26 | 0 | 0 | 0.001 | 1.000 | 0 | 6.527e-08 | 6.426e-08 | 4.958e-07 | 3.122e-08 |
| c08 | 61001–64000 | 2101 | 0.008 | 47 | 26 | 25 | 25 | 0 | 1 | 0.001 | 0.962 | 1 | 3.209e-08 | 3.362e-08 | 2.445e-07 | 4.227e-08 |
| c09 | 64001–67000 | 2092 | 0.008 | 47 | 26 | 26 | 26 | 0 | 1 | 0.001 | 1.000 | 0 | 5.689e-08 | 4.966e-08 | 4.271e-07 | 6.780e-08 |
| c10 | 67001–70000 | 2083 | 0.008 | 47 | 26 | 26 | 26 | 0 | 1 | 0.001 | 1.000 | 0 | 4.627e-08 | 4.242e-08 | 3.482e-07 | 4.197e-08 |

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
| c01 | 0.001 | 0.010 | 1.000 | 0 | 0 | passa | 12 | 1.000 | 1.000 | 0.010 | passa |
| c02 | 0.001 | 0.010 | 1.000 | 0 | 2 | passa | 12 | 1.000 | 1.000 | 0.010 | passa |
| c03 | 0.001 | 0.010 | 1.000 | 0 | 0 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| c04 | 0.001 | 0.010 | 1.000 | 0 | 2 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| c05 | 0.001 | 0.010 | 1.000 | 0 | 3 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| c06 | 0.001 | 0.010 | 1.000 | 0 | 0 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| c07 | 0.001 | 0.010 | 1.000 | 0 | 1 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| c08 | 0.001 | 0.010 | 1.000 | 0 | 4 | passa | 12 | 1.000 | 1.000 | 0.010 | passa |
| c09 | 0.001 | 0.010 | 1.000 | 0 | 1 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |
| c10 | 0.001 | 0.010 | 1.000 | 0 | 1 | passa | 11 | 1.000 | 1.000 | 0.010 | passa |

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

### bloco c01 (zeros 40001–43000)

Protocolo `m4-v2-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `40ecc04a9f41025cbc713f99264a87446f14ae4a3c012592662a63ad4625e0c1` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [33190.805, 35380.943], L = 2190.1 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4707 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 3.179e-10 (máx. |F| = 91.9) |
| Quadratura: mudança ao reduzir painel pela metade | 1.703e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 6.565e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2797 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.049 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4975 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1761, 3.2797] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 12; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 12; 1.000 |
| Tolerância de matching (quantil 0.99) | 0.001 = 0.156 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 177 |
| Detecções (nulo primário / secundário) | 27 / 18 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 27 |
| Escore S; nulo (conjunto independente, B=999) | 27; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.051 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.345e-08 / 8.346e-08; 5.647e-08 / 4.411e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.285e-08 / 8.357e-08; 5.957e-08 / 4.179e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 2.530e-07 / 6.456e-07; 4.385e-07 / 3.386e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 7.292e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 4.870e-08 / 1.993e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.478; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.363; p = 0.001 |
| Linhas não detectadas | 20 |
| Tempo (s) | instrument: 0.6, null_shuffle: 15.2, null_gue: 55.0, synthetic: 49.4, arithmetic: 35.3 |

Figuras: `tables/c01/spectrum_z.png`, `tables/c01/coefficients.png`, `tables/c01/synthetic_calibration.png`.

### bloco c02 (zeros 43001–46000)

Protocolo `m4-v2-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `bf42bf11d71b49827a9997f8042ef70ea623f2743f81c7e6a9890afedc00a17d` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [35381.400, 37555.829], L = 2174.4 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4673 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.027e-10 (máx. |F| = 91.0) |
| Quadratura: mudança ao reduzir painel pela metade | 2.839e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 1.000e-13 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2925 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.035 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3861 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1780, 3.2925] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 2 (dos quais com correspondência no catálogo: 2) |
| Linhas claramente detectáveis; recuperação entre elas | 12; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 12; 1.000 |
| Tolerância de matching (quantil 0.99) | 0.001 = 0.132 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 174 |
| Detecções (nulo primário / secundário) | 26 / 17 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.036 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.935e-08 / 9.554e-08; 4.984e-08 / 4.993e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.835e-08 / 8.902e-08; 5.423e-08 / 4.671e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 2.970e-07 / 7.313e-07; 3.799e-07 / 3.896e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 8.269e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 4.683e-08 / 1.882e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.491; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.336; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.6, null_shuffle: 14.2, null_gue: 54.7, synthetic: 51.4, arithmetic: 35.8 |

Figuras: `tables/c02/spectrum_z.png`, `tables/c02/coefficients.png`, `tables/c02/synthetic_calibration.png`.

### bloco c03 (zeros 46001–49000)

Protocolo `m4-v2-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `3c200ed3e2f0d17a66e9d6d110cab6541c335c5a3601cc05a069bcc4ce35b35b` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [37556.557, 39716.703], L = 2160.1 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4642 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.254e-10 (máx. |F| = 90.0) |
| Quadratura: mudança ao reduzir painel pela metade | 3.502e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 6.981e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.3392 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.022 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3503 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2066, 3.3392] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 7.595e-04 = 0.098 FWHM |
| Separação de pares com ≥90% recuperado | 1.00 FWHM (medida) |
| Linhas sintéticas isoladas | 179 |
| Detecções (nulo primário / secundário) | 26 / 20 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.000, máx. 0 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.022 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 2.421e-08 / 7.502e-08; 6.222e-08 / 3.746e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 2.104e-08 / 7.246e-08; 6.406e-08 / 3.222e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 1.864e-07 / 5.671e-07; 4.734e-07 / 3.294e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 6.421e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 5.367e-08 / 1.826e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.518; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.366; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.6, null_shuffle: 15.1, null_gue: 54.6, synthetic: 49.5, arithmetic: 35.1 |

Figuras: `tables/c03/spectrum_z.png`, `tables/c03/coefficients.png`, `tables/c03/synthetic_calibration.png`.

### bloco c04 (zeros 49001–52000)

Protocolo `m4-v2-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `a3cad3f1916cdd05b0f245b6ae8835e017bec9d72f04c801aefdd1b5ffd13d14` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [39717.125, 41863.778], L = 2146.7 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4613 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.649e-10 (máx. |F| = 90.1) |
| Quadratura: mudança ao reduzir painel pela metade | 2.478e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 6.226e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2896 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.031 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3731 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1675, 3.2896] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 2 (dos quais com correspondência no catálogo: 2) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 9.256e-04 = 0.119 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 177 |
| Detecções (nulo primário / secundário) | 26 / 19 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.002, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.031 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 2.248e-08 / 8.162e-08; 6.481e-08 / 9.574e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 2.853e-08 / 9.153e-08; 6.211e-08 / 9.531e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 1.714e-07 / 6.237e-07; 4.822e-07 / 8.936e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 7.153e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 2.710e-08 / 1.876e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.532; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.358; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.6, null_shuffle: 15.7, null_gue: 54.9, synthetic: 50.0, arithmetic: 34.7 |

Figuras: `tables/c04/spectrum_z.png`, `tables/c04/coefficients.png`, `tables/c04/synthetic_calibration.png`.

### bloco c05 (zeros 52001–55000)

Protocolo `m4-v2-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `8200a1068c501a9b7ecde0321b23b22b099a7a6ba2ad341946cf40b23a31589e` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [41864.552, 43998.539], L = 2134.0 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4586 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 3.148e-10 (máx. |F| = 89.1) |
| Quadratura: mudança ao reduzir painel pela metade | 2.191e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 5.926e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.3049 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.034 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.5407 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1983, 3.3049] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 3 (dos quais com correspondência no catálogo: 3) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.623e-04 = 0.110 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 185 |
| Detecções (nulo primário / secundário) | 25 / 16 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 25; média 0.003, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.035 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 0.962; detectáveis perdidas: 89 |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 3.548e-08 / 8.217e-08; 5.261e-08 / 1.183e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 3.592e-08 / 8.818e-08; 6.878e-08 / 1.201e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 2.714e-07 / 6.306e-07; 4.005e-07 / 1.146e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 7.184e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 3.715e-08 / 1.740e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.516; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.346; p = 0.001 |
| Linhas não detectadas | 22 |
| Tempo (s) | instrument: 0.6, null_shuffle: 17.1, null_gue: 54.5, synthetic: 49.5, arithmetic: 34.3 |

Figuras: `tables/c05/spectrum_z.png`, `tables/c05/coefficients.png`, `tables/c05/synthetic_calibration.png`.

### bloco c06 (zeros 55001–58000)

Protocolo `m4-v2-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `bb9475dc77915a3b3febbf7dd6e1a65202f2a31992a5609ea5c8ddc1c97799fc` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [43999.278, 46122.216], L = 2122.9 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4562 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 5.928e-11 (máx. |F| = 88.9) |
| Quadratura: mudança ao reduzir painel pela metade | 1.002e-08 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.359e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2667 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.029 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3281 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1815, 3.2667] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.272e-04 = 0.105 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 175 |
| Detecções (nulo primário / secundário) | 26 / 17 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.000, máx. 0 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.029 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 5.449e-08 / 1.182e-07; 1.135e-07 / 2.011e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 4.445e-08 / 1.055e-07; 1.055e-07 / 1.958e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 4.200e-07 / 9.001e-07; 8.725e-07 / 6.064e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.018e-06 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.078e-08 / 2.162e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.507; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.383; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.6, null_shuffle: 15.7, null_gue: 54.7, synthetic: 49.6, arithmetic: 34.9 |

Figuras: `tables/c06/spectrum_z.png`, `tables/c06/coefficients.png`, `tables/c06/synthetic_calibration.png`.

### bloco c07 (zeros 58001–61000)

Protocolo `m4-v2-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `d3e332cc528afd6f9136b304d6c2349848615a3403249e2edc5cce181429bbd5` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [46122.878, 48234.310], L = 2111.4 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4538 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 3.234e-10 (máx. |F| = 88.5) |
| Quadratura: mudança ao reduzir painel pela metade | 2.394e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 6.692e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2759 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.034 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3324 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1933, 3.2759] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.456e-04 = 0.107 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 180 |
| Detecções (nulo primário / secundário) | 26 / 19 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.000, máx. 0 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.035 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 6.527e-08 / 1.185e-07; 1.066e-07 / 1.378e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 6.426e-08 / 1.192e-07; 1.020e-07 / 1.362e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 4.958e-07 / 9.067e-07; 8.122e-07 / 2.132e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.026e-06 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 3.122e-08 / 1.731e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.500; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.349; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.5, null_shuffle: 15.7, null_gue: 54.5, synthetic: 49.3, arithmetic: 33.8 |

Figuras: `tables/c07/spectrum_z.png`, `tables/c07/coefficients.png`, `tables/c07/synthetic_calibration.png`.

### bloco c08 (zeros 61001–64000)

Protocolo `m4-v2-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `fe0b52a8196a6ecaafa2fe3b78850380087cf537fbc54dfcc5347656e5ac6d62` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [48234.981, 50336.353], L = 2101.4 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4516 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.937e-10 (máx. |F| = 88.2) |
| Quadratura: mudança ao reduzir painel pela metade | 7.378e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.383e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2677 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.049 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4041 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1699, 3.2677] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 4 (dos quais com correspondência no catálogo: 4) |
| Linhas claramente detectáveis; recuperação entre elas | 12; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 12; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.336e-04 = 0.105 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 189 |
| Detecções (nulo primário / secundário) | 25 / 17 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 25; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.050 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 0.962; detectáveis perdidas: 89 |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.209e-08 / 9.733e-08; 4.724e-08 / 5.665e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 3.362e-08 / 8.025e-08; 4.171e-08 / 5.312e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=12); todas as 47 linhas | 2.445e-07 / 7.384e-07; 3.571e-07 / 4.358e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 8.358e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 4.227e-08 / 1.932e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.469; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.356; p = 0.001 |
| Linhas não detectadas | 22 |
| Tempo (s) | instrument: 0.5, null_shuffle: 15.4, null_gue: 55.4, synthetic: 50.9, arithmetic: 34.8 |

Figuras: `tables/c08/spectrum_z.png`, `tables/c08/coefficients.png`, `tables/c08/synthetic_calibration.png`.

### bloco c09 (zeros 64001–67000)

Protocolo `m4-v2-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `d86d42bff40015090e4194d6d2f25c95231fbea2e3eff50ddd8f79e0c9d73088` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [50336.772, 52428.443], L = 2091.7 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4495 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 8.576e-11 (máx. |F| = 87.7) |
| Quadratura: mudança ao reduzir painel pela metade | 6.985e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 6.748e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2855 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.030 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3869 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1787, 3.2855] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 7.555e-04 = 0.094 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 178 |
| Detecções (nulo primário / secundário) | 26 / 17 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.031 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 5.689e-08 / 9.270e-08; 6.277e-08 / 5.446e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 4.966e-08 / 8.554e-08; 6.354e-08 / 5.143e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 4.271e-07 / 7.005e-07; 4.751e-07 / 3.625e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 7.932e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.780e-08 / 1.964e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.499; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.351; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.5, null_shuffle: 15.3, null_gue: 54.4, synthetic: 50.2, arithmetic: 33.7 |

Figuras: `tables/c09/spectrum_z.png`, `tables/c09/coefficients.png`, `tables/c09/synthetic_calibration.png`.

### bloco c10 (zeros 67001–70000)

Protocolo `m4-v2-robustez-blackman-harris`. `blind_peaks.csv` SHA-256 `46c2d64395477e6f8cc04344c24f482836e2605814e928a1cc1d5727cda9f79c` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | blackman_harris / rvm |
| Intervalo [A, B] | [52428.975, 54511.658], L = 2082.7 |
| FWHM medida | 0.008 (2.666 × 2π/L); lóbulo lateral -92.0 dB |
| Malha | 4476 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.775e-10 (máx. |F| = 87.5) |
| Quadratura: mudança ao reduzir painel pela metade | 3.893e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 5.467e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2792 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.030 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4140 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.1885, 3.2792] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 11; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 11; 1.000 |
| Tolerância de matching (quantil 0.99) | 9.548e-04 = 0.119 FWHM |
| Separação de pares com ≥90% recuperado | 1.00 FWHM (medida) |
| Linhas sintéticas isoladas | 187 |
| Detecções (nulo primário / secundário) | 26 / 18 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 45 resolvidas |
| Previstas detectáveis | 26 |
| Escore S; nulo (conjunto independente, B=999) | 26; média 0.002, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.030 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=11); todas as 47 linhas | 4.627e-08 / 9.092e-08; 8.963e-08 / 8.630e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 4.242e-08 / 8.389e-08; 8.034e-08 / 8.163e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=11); todas as 47 linhas | 3.482e-07 / 6.866e-07; 6.866e-07 / 5.361e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 7.775e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 4.197e-08 / 1.585e-07 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.509; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.351; p = 0.001 |
| Linhas não detectadas | 21 |
| Tempo (s) | instrument: 0.5, null_shuffle: 16.6, null_gue: 54.4, synthetic: 55.8, arithmetic: 38.9 |

Figuras: `tables/c10/spectrum_z.png`, `tables/c10/coefficients.png`, `tables/c10/synthetic_calibration.png`.

