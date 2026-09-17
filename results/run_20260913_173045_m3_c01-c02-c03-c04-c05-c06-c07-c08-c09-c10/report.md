# Relatório M3 — espectroscopia inversa por blocos

**ID:** `run_20260913_173045_m3_c01-c02-c03-c04-c05-c06-c07-c08-c09-c10`
**Blocos:** c01, c02, c03, c04, c05, c06, c07, c08, c09, c10
**Duração:** 2971.2 s; pico de memória 189 MB
**Comando:** `/home/dionatandiego11/Downloads/hipotese-riemann/src/riemann_spectra/__main__.py m3 --config configs/m4_v2.toml --blocks c01,c02,c03,c04,c05,c06,c07,c08,c09,c10 --workers 4`

Protocolo congelado em 2026-09-13T17:30:29.591379+00:00 (config `13d0b6080f25ed2e…`, módulos `5885b75ea98233af…`).

## Resumo por bloco

| Bloco | Índices | L | FWHM | Catálogo | Detectáveis | Detecções | S | Sem corresp. | S nulo máx | p | Recuperação | Decisões alteráveis por z refinado | mediana abs(razão−1) `band_conjugate` | mediana abs(razão−1) `band_no_conjugate` | mediana abs(razão−1) `centers_conjugate` | Δ perturbação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| c01 | 40001–43000 | 2190 | 0.006 | 47 | 33 | 33 | 33 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 5.089e-10 | 5.097e-10 | 2.749e-10 | 7.285e-10 |
| c02 | 43001–46000 | 2174 | 0.006 | 47 | 32 | 32 | 32 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 2.025e-10 | 2.084e-10 | 3.853e-10 | 7.354e-10 |
| c03 | 46001–49000 | 2160 | 0.006 | 47 | 33 | 33 | 33 | 0 | 1 | 1.000e-04 | 1.000 | 1 | 2.907e-10 | 2.862e-10 | 5.877e-10 | 6.328e-10 |
| c04 | 49001–52000 | 2147 | 0.006 | 47 | 32 | 32 | 32 | 0 | 1 | 1.000e-04 | 1.000 | 1 | 3.158e-10 | 3.162e-10 | 1.010e-09 | 6.901e-10 |
| c05 | 52001–55000 | 2134 | 0.006 | 47 | 34 | 34 | 34 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 4.164e-10 | 4.123e-10 | 6.380e-10 | 6.283e-10 |
| c06 | 55001–58000 | 2123 | 0.006 | 47 | 33 | 33 | 33 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 3.580e-10 | 3.617e-10 | 7.182e-10 | 7.541e-10 |
| c07 | 58001–61000 | 2111 | 0.006 | 47 | 32 | 32 | 32 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 2.347e-10 | 2.286e-10 | 5.799e-10 | 6.273e-10 |
| c08 | 61001–64000 | 2101 | 0.006 | 47 | 33 | 33 | 33 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 2.949e-10 | 2.998e-10 | 5.346e-10 | 6.652e-10 |
| c09 | 64001–67000 | 2092 | 0.006 | 47 | 33 | 33 | 33 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 2.037e-10 | 2.342e-10 | 7.726e-10 | 6.156e-10 |
| c10 | 67001–70000 | 2083 | 0.006 | 47 | 32 | 32 | 32 | 0 | 1 | 1.000e-04 | 1.000 | 0 | 4.058e-10 | 4.013e-10 | 9.500e-10 | 7.272e-10 |

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
| c01 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| c02 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 16 | 1.000 | 1.000 | 0.010 | passa |
| c03 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| c04 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| c05 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| c06 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 16 | 1.000 | 1.000 | 0.010 | passa |
| c07 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| c08 | 1.000e-04 | 0.001 | 1.000 | 0 | 0 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| c09 | 1.000e-04 | 0.001 | 1.000 | 0 | 1 | passa | 15 | 1.000 | 1.000 | 0.010 | passa |
| c10 | 1.000e-04 | 0.001 | 1.000 | 0 | 1 | passa | 14 | 1.000 | 1.000 | 0.010 | passa |

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

Protocolo `m4-v2`. `blind_peaks.csv` SHA-256 `53c8b2aa47caecdfe6d029de4d17a705e42c75a0e0395d2e4b7df272e34a2bc7` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [33190.805, 35380.943], L = 2190.1 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6275 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 4.674e-10 (máx. |F| = 128.2) |
| Quadratura: mudança ao reduzir painel pela metade | 2.386e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 6.384e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2953 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.049 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.8023 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2661, 3.2953] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 5.247e-04 = 0.091 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 201 |
| Detecções (nulo primário / secundário) | 33 / 20 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 33 |
| Escore S; nulo (conjunto independente, B=9999) | 33; média 4.000e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.050 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 5.089e-10 / 1.285e-09; 1.036e-09 / 8.314e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 5.097e-10 / 1.286e-09; 1.030e-09 / 8.314e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 2.749e-10 / 1.992e-09; 2.396e-09 / 1.026e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.475e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.285e-10 / 5.405e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.436; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.308; p = 0.001 |
| Linhas não detectadas | 14 |
| Tempo (s) | instrument: 0.7, null_shuffle: 164.2, null_gue: 57.4, synthetic: 60.0, arithmetic: 39.5 |

Figuras: `tables/c01/spectrum_z.png`, `tables/c01/coefficients.png`, `tables/c01/synthetic_calibration.png`.

### bloco c02 (zeros 43001–46000)

Protocolo `m4-v2`. `blind_peaks.csv` SHA-256 `17335c1676bd37733d3886e942311aaaf6a36efa65ceed5c2f278fffaa789999` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [35381.400, 37555.829], L = 2174.4 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6230 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.655e-10 (máx. |F| = 126.2) |
| Quadratura: mudança ao reduzir painel pela metade | 3.954e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.069e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.3068 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.042 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4810 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2753, 3.3068] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 16; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 16; 1.000 |
| Tolerância de matching (quantil 0.99) | 5.457e-04 = 0.094 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 199 |
| Detecções (nulo primário / secundário) | 32 / 25 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 32 |
| Escore S; nulo (conjunto independente, B=9999) | 32; média 5.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.043 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.025e-10 / 6.517e-10; 6.517e-10 / 8.922e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 2.084e-10 / 6.495e-10; 6.495e-10 / 8.922e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 3.853e-10 / 2.042e-09; 2.274e-09 / 1.018e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 2.370e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.354e-10 / 5.519e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.428; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.270; p = 0.001 |
| Linhas não detectadas | 15 |
| Tempo (s) | instrument: 0.5, null_shuffle: 139.9, null_gue: 54.5, synthetic: 53.6, arithmetic: 34.7 |

Figuras: `tables/c02/spectrum_z.png`, `tables/c02/coefficients.png`, `tables/c02/synthetic_calibration.png`.

### bloco c03 (zeros 46001–49000)

Protocolo `m4-v2`. `blind_peaks.csv` SHA-256 `cd80d25043c55ca199e0865a83e7d7a571161e80acc714701515826639638ce0` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [37556.557, 39716.703], L = 2160.1 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6189 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.121e-10 (máx. |F| = 125.6) |
| Quadratura: mudança ao reduzir painel pela metade | 4.857e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.646e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2996 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.044 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3820 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2703, 3.2996] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.114e-04 = 0.139 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 210 |
| Detecções (nulo primário / secundário) | 33 / 26 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 33 |
| Escore S; nulo (conjunto independente, B=9999) | 33; média 2.000e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.045 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 2.907e-10 / 1.081e-09; 1.221e-09 / 9.453e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 2.862e-10 / 1.087e-09; 1.234e-09 / 9.453e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 5.877e-10 / 5.788e-09; 5.788e-09 / 1.419e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 4.707e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.328e-10 / 5.388e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.435; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.319; p = 0.001 |
| Linhas não detectadas | 14 |
| Tempo (s) | instrument: 0.6, null_shuffle: 159.8, null_gue: 56.6, synthetic: 59.0, arithmetic: 36.8 |

Figuras: `tables/c03/spectrum_z.png`, `tables/c03/coefficients.png`, `tables/c03/synthetic_calibration.png`.

### bloco c04 (zeros 49001–52000)

Protocolo `m4-v2`. `blind_peaks.csv` SHA-256 `8973043932d4d19bacf67a38cd2e32623ce3901993ac6afe1c68085711e3a386` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [39717.125, 41863.778], L = 2146.7 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6150 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.347e-10 (máx. |F| = 125.6) |
| Quadratura: mudança ao reduzir painel pela metade | 3.453e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 9.569e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2779 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.053 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3738 |
| Candidatos cuja classificação mudaria usando z refinado | 1 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2518, 3.2779] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 8.766e-04 = 0.150 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 203 |
| Detecções (nulo primário / secundário) | 32 / 26 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 32 |
| Escore S; nulo (conjunto independente, B=9999) | 32; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.054 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 3.158e-10 / 9.557e-10; 9.399e-10 / 1.844e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 3.162e-10 / 9.529e-10; 9.490e-10 / 1.844e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 1.010e-09 / 6.946e-09; 4.319e-09 / 2.210e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 5.993e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.901e-10 / 5.283e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.455; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.302; p = 0.001 |
| Linhas não detectadas | 15 |
| Tempo (s) | instrument: 0.5, null_shuffle: 142.5, null_gue: 55.6, synthetic: 59.7, arithmetic: 36.4 |

Figuras: `tables/c04/spectrum_z.png`, `tables/c04/coefficients.png`, `tables/c04/synthetic_calibration.png`.

### bloco c05 (zeros 52001–55000)

Protocolo `m4-v2`. `blind_peaks.csv` SHA-256 `3e6648096eea13ac10f6328b6fc8f3b0c24b5f873c99e70b5515898168e75542` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [41864.552, 43998.539], L = 2134.0 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6114 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 6.016e-10 (máx. |F| = 124.4) |
| Quadratura: mudança ao reduzir painel pela metade | 3.036e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.356e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.3023 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.040 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.6542 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2757, 3.3023] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 7.078e-04 = 0.120 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 212 |
| Detecções (nulo primário / secundário) | 34 / 23 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 34 |
| Escore S; nulo (conjunto independente, B=9999) | 34; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.041 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 4.164e-10 / 1.201e-09; 1.088e-09 / 1.283e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 4.123e-10 / 1.202e-09; 1.089e-09 / 1.283e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 6.380e-10 / 4.339e-09; 3.718e-09 / 1.102e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 3.772e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.283e-10 / 6.296e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.450; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.302; p = 0.001 |
| Linhas não detectadas | 13 |
| Tempo (s) | instrument: 0.5, null_shuffle: 156.8, null_gue: 56.3, synthetic: 59.8, arithmetic: 36.3 |

Figuras: `tables/c05/spectrum_z.png`, `tables/c05/coefficients.png`, `tables/c05/synthetic_calibration.png`.

### bloco c06 (zeros 55001–58000)

Protocolo `m4-v2`. `blind_peaks.csv` SHA-256 `eb06d521fc998e40b35acd2f8166ec90c7f7b89f89f865beb893d0f04a3d31c7` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [43999.278, 46122.216], L = 2122.9 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6082 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 8.173e-11 (máx. |F| = 124.1) |
| Quadratura: mudança ao reduzir painel pela metade | 1.393e-08 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.359e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2793 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.044 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4246 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2518, 3.2793] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 16; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 16; 1.000 |
| Tolerância de matching (quantil 0.99) | 7.993e-04 = 0.135 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 195 |
| Detecções (nulo primário / secundário) | 33 / 26 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 33 |
| Escore S; nulo (conjunto independente, B=9999) | 33; média 6.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.045 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=16); todas as 47 linhas | 3.580e-10 / 1.628e-09; 9.003e-10 / 5.268e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 3.617e-10 / 1.627e-09; 8.905e-10 / 5.268e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=16); todas as 47 linhas | 7.182e-10 / 7.886e-09; 7.886e-09 / 1.393e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 6.259e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.541e-10 / 4.381e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.433; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.288; p = 0.001 |
| Linhas não detectadas | 14 |
| Tempo (s) | instrument: 0.5, null_shuffle: 158.3, null_gue: 55.0, synthetic: 65.9, arithmetic: 40.3 |

Figuras: `tables/c06/spectrum_z.png`, `tables/c06/coefficients.png`, `tables/c06/synthetic_calibration.png`.

### bloco c07 (zeros 58001–61000)

Protocolo `m4-v2`. `blind_peaks.csv` SHA-256 `3c4c5de1eb1cfa87becefd0c476fe5a74935de2fa68a2b408b23a170e02634d1` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [46122.878, 48234.310], L = 2111.4 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6049 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 3.695e-10 (máx. |F| = 122.6) |
| Quadratura: mudança ao reduzir painel pela metade | 3.346e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 9.703e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2971 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.044 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.5117 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2689, 3.2971] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 6.979e-04 = 0.117 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 204 |
| Detecções (nulo primário / secundário) | 32 / 23 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 32 |
| Escore S; nulo (conjunto independente, B=9999) | 32; média 6.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.045 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 2.347e-10 / 1.020e-09; 1.020e-09 / 1.250e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 2.286e-10 / 1.010e-09; 1.010e-09 / 1.250e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 5.799e-10 / 1.042e-08; 1.088e-08 / 1.472e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 9.580e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.273e-10 / 4.078e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.440; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.277; p = 0.001 |
| Linhas não detectadas | 15 |
| Tempo (s) | instrument: 0.5, null_shuffle: 143.9, null_gue: 55.0, synthetic: 52.8, arithmetic: 34.9 |

Figuras: `tables/c07/spectrum_z.png`, `tables/c07/coefficients.png`, `tables/c07/synthetic_calibration.png`.

### bloco c08 (zeros 61001–64000)

Protocolo `m4-v2`. `blind_peaks.csv` SHA-256 `ea05ab26085a3cfb0afad60da507410653d1f3751826e7daa8ddcfd0053fe4ef` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [48234.981, 50336.353], L = 2101.4 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 6020 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 3.339e-10 (máx. |F| = 122.5) |
| Quadratura: mudança ao reduzir painel pela metade | 1.029e-08 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.726e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.3088 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.044 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3628 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2760, 3.3088] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 0 (dos quais com correspondência no catálogo: 0) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 9.937e-04 = 0.166 FWHM |
| Separação de pares com ≥90% recuperado | 1.00 FWHM (medida) |
| Linhas sintéticas isoladas | 215 |
| Detecções (nulo primário / secundário) | 33 / 25 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 33 |
| Escore S; nulo (conjunto independente, B=9999) | 33; média 5.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.045 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 2.949e-10 / 6.990e-10; 7.642e-10 / 1.102e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 2.998e-10 / 6.952e-10; 7.625e-10 / 1.102e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 5.346e-10 / 6.438e-09; 7.399e-09 / 3.539e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 6.975e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.652e-10 / 4.792e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.450; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.306; p = 0.001 |
| Linhas não detectadas | 14 |
| Tempo (s) | instrument: 0.5, null_shuffle: 131.7, null_gue: 54.3, synthetic: 53.2, arithmetic: 34.4 |

Figuras: `tables/c08/spectrum_z.png`, `tables/c08/coefficients.png`, `tables/c08/synthetic_calibration.png`.

### bloco c09 (zeros 64001–67000)

Protocolo `m4-v2`. `blind_peaks.csv` SHA-256 `27e7cdc69239d3e934db93c322a5a0909b602d0f2fec8f9fcfe0f396708e805b` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [50336.772, 52428.443], L = 2091.7 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 5993 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 8.857e-11 (máx. |F| = 121.7) |
| Quadratura: mudança ao reduzir painel pela metade | 9.768e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.923e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2987 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.042 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4612 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2690, 3.2987] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 15; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 15; 1.000 |
| Tolerância de matching (quantil 0.99) | 6.763e-04 = 0.113 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 196 |
| Detecções (nulo primário / secundário) | 33 / 23 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 33 |
| Escore S; nulo (conjunto independente, B=9999) | 33; média 6.001e-04, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.043 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=15); todas as 47 linhas | 2.037e-10 / 1.254e-09; 1.156e-09 / 1.310e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 2.342e-10 / 1.253e-09; 1.158e-09 / 1.310e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=15); todas as 47 linhas | 7.726e-10 / 4.792e-09; 7.143e-09 / 1.209e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 3.636e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 6.156e-10 / 5.462e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.449; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.307; p = 0.001 |
| Linhas não detectadas | 14 |
| Tempo (s) | instrument: 0.5, null_shuffle: 131.6, null_gue: 54.3, synthetic: 52.3, arithmetic: 34.3 |

Figuras: `tables/c09/spectrum_z.png`, `tables/c09/coefficients.png`, `tables/c09/synthetic_calibration.png`.

### bloco c10 (zeros 67001–70000)

Protocolo `m4-v2`. `blind_peaks.csv` SHA-256 `2a6f8455b41a6b1e3cb644cd56b96734b06ae2cdcce21e0a32319c9c27c94bdb` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [52428.975, 54511.658], L = 2082.7 |
| FWHM medida | 0.006 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 5967 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 4.638e-10 (máx. |F| = 121.8) |
| Quadratura: mudança ao reduzir painel pela metade | 5.479e-09 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 7.803e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 9999 / 9999; limiar z = 3.2973 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.042 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.4357 |
| Candidatos cuja classificação mudaria usando z refinado | 0 |
| Faixa inconclusiva do limiar (IC 0.95) | [3.2690, 3.2973] |
| Candidatos inconclusivos quanto à detecção significativa (nulo primário) | 1 (dos quais com correspondência no catálogo: 1) |
| Linhas claramente detectáveis; recuperação entre elas | 14; 1.000 |
| Concordância de coeficientes (critério C2): elegíveis; fração com abs(razão−1) ≤ tolerância | 14; 1.000 |
| Tolerância de matching (quantil 0.99) | 7.881e-04 = 0.131 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 208 |
| Detecções (nulo primário / secundário) | 32 / 24 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 32 |
| Escore S; nulo (conjunto independente, B=9999) | 32; média 0.001, máx. 1 |
| Detecções sem correspondência no catálogo; detecções por realização nula | 0; 0.043 |
| p Monte Carlo global | 1.000e-04 (resolução 1.000e-04) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=14); todas as 47 linhas | 4.058e-10 / 9.912e-10; 1.268e-09 / 1.117e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=14); todas as 47 linhas | 4.013e-10 / 9.843e-10; 1.255e-09 / 1.117e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=14); todas as 47 linhas | 9.500e-10 / 3.161e-09; 6.972e-09 / 1.450e-05 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 3.277e-09 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.272e-10 / 3.904e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.458; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.311; p = 0.001 |
| Linhas não detectadas | 15 |
| Tempo (s) | instrument: 0.5, null_shuffle: 152.2, null_gue: 54.5, synthetic: 51.3, arithmetic: 34.4 |

Figuras: `tables/c10/spectrum_z.png`, `tables/c10/coefficients.png`, `tables/c10/synthetic_calibration.png`.

