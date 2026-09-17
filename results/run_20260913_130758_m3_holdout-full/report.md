# Relatório M3 — espectroscopia inversa por blocos

**ID:** `run_20260913_130758_m3_holdout-full`
**Blocos:** holdout, full
**Duração:** 1205.8 s; pico de memória 304 MB
**Comando:** `/home/dionatandiego11/Downloads/hipotese-riemann/src/riemann_spectra/__main__.py m3 --config configs/m3_protocol_v3.toml --blocks holdout,full --workers 4`

Protocolo congelado em 2026-09-13T13:07:56.578028+00:00 (config `029e453d897d3c3e…`, módulos `7e6210fb3d25dadf…`).

## Resumo por bloco

| Bloco | Índices | L | FWHM | Catálogo | Detectáveis | Detecções | S | Sem corresp. | S nulo máx | p | Recuperação | Decisões alteráveis por z refinado | mediana abs(razão−1) `band_conjugate` | mediana abs(razão−1) `band_no_conjugate` | mediana abs(razão−1) `centers_conjugate` | Δ perturbação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| holdout | 7001–10000 | 2612 | 0.005 | 47 | 35 | 35 | 35 | 0 | 1 | 0.001 | 1.000 | 0 | 5.078e-10 | 5.155e-10 | 4.305e-09 | 9.063e-10 |
| full | 1–10000 | 9864 | 0.001 | 47 | 41 | 41 | 41 | 0 | 0 | 0.001 | 1.000 | 0 | 1.898e-10 | 1.897e-10 | 2.519e-10 | 4.919e-10 |

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

### bloco holdout (zeros 7001–10000)

Protocolo `m3-v3`. `blind_peaks.csv` SHA-256 `02968eaca95d4086cf4078607bbade4b71a195e8868fdf75bfb322f82b7d7444` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [7265.963, 9877.783], L = 2611.8 |
| FWHM medida | 0.005 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 7483 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.504e-10 (máx. |F| = 152.7) |
| Quadratura: mudança ao reduzir painel pela metade | 7.754e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.036e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.3143 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.051 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3088 |
| Candidatos cuja decisão mudaria usando z refinado | 0 |
| Tolerância de matching (quantil 0.99) | 6.911e-04 = 0.144 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 188 |
| Detecções (nulo primário / secundário) | 35 / 32 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 35 |
| Escore S; nulo (conjunto independente, B=999) | 35; média 0.001, máx. 1 |
| Detecções sem correspondente; detecções por realização nula | 0; 0.051 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=35); todas as 47 linhas | 5.078e-10 / 7.841e-08; 1.068e-09 / 6.391e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=35); todas as 47 linhas | 5.155e-10 / 7.841e-08; 1.064e-09 / 6.391e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=35); todas as 47 linhas | 4.305e-09 / 1.226e-06; 6.637e-09 / 9.095e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.147e-06 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 9.063e-10 / 6.794e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.295; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.202; p = 0.001 |
| Linhas não detectadas | 12 |
| Tempo (s) | instrument: 0.7, null_shuffle: 22.4, null_gue: 56.2, synthetic: 24.8, arithmetic: 53.0 |

Figuras: `tables/holdout/spectrum_z.png`, `tables/holdout/coefficients.png`, `tables/holdout/synthetic_calibration.png`.

### bloco full (zeros 1–10000)

Protocolo `m3-v3`. `blind_peaks.csv` SHA-256 `ffbed5dc061d53bdee9fc532703acf5f503eab48f9c48fcd2d2fbb4ed8027dd0` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [14.135, 9877.783], L = 9863.6 |
| FWHM medida | 0.001 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 28258 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 3.966e-10 (máx. |F| = 572.8) |
| Quadratura: mudança ao reduzir painel pela metade | 9.929e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 4.241e-11 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.5123 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.053 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.5014 |
| Candidatos cuja decisão mudaria usando z refinado | 0 |
| Tolerância de matching (quantil 0.99) | 1.539e-04 = 0.121 FWHM |
| Separação de pares com ≥90% recuperado | 2.00 FWHM (não atingiu a meta; usada a maior separação testada) |
| Linhas sintéticas isoladas | 68 |
| Detecções (nulo primário / secundário) | 41 / 40 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 41 |
| Escore S; nulo (conjunto independente, B=999) | 41; média 0.000, máx. 0 |
| Detecções sem correspondente; detecções por realização nula | 0; 0.056 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=41); todas as 47 linhas | 1.898e-10 / 8.189e-09; 2.235e-10 / 1.703e-08 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=41); todas as 47 linhas | 1.897e-10 / 8.189e-09; 2.235e-10 / 1.703e-08 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=41); todas as 47 linhas | 2.519e-10 / 1.086e-07; 2.935e-10 / 2.130e-07 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 1.004e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 4.919e-10 / 3.902e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.272; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.185; p = 0.001 |
| Linhas não detectadas | 6 |
| Tempo (s) | instrument: 2.0, null_shuffle: 62.5, null_gue: 653.5, synthetic: 191.1, arithmetic: 138.2 |

Figuras: `tables/full/spectrum_z.png`, `tables/full/coefficients.png`, `tables/full/synthetic_calibration.png`.

