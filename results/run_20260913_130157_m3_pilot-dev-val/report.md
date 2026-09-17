# Relatório M3 — espectroscopia inversa por blocos

**ID:** `run_20260913_130157_m3_pilot-dev-val`
**Blocos:** pilot, dev, val
**Duração:** 351.9 s; pico de memória 192 MB
**Comando:** `/home/dionatandiego11/Downloads/hipotese-riemann/src/riemann_spectra/__main__.py m3 --config configs/m3_protocol_v3.toml --blocks pilot,dev,val --workers 4`

Execução sem blocos reservados; congelamento não exigido.

## Resumo por bloco

| Bloco | Índices | L | FWHM | Catálogo | Detectáveis | Detecções | S | Sem corresp. | S nulo máx | p | Recuperação | Decisões alteráveis por z refinado | mediana abs(razão−1) `band_conjugate` | mediana abs(razão−1) `band_no_conjugate` | mediana abs(razão−1) `centers_conjugate` | Δ perturbação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pilot | 1–1000 | 1405 | 0.009 | 47 | 18 | 18 | 18 | 0 | 1 | 0.001 | 1.000 | 0 | 2.195e-10 | 1.553e-10 | 2.317e-09 | 5.542e-10 |
| dev | 1001–4000 | 3086 | 0.004 | 47 | 37 | 37 | 37 | 0 | 0 | 0.001 | 1.000 | 0 | 5.400e-10 | 5.395e-10 | 7.604e-10 | 7.883e-10 |
| val | 4001–7000 | 2757 | 0.005 | 47 | 35 | 35 | 35 | 0 | 1 | 0.001 | 1.000 | 0 | 3.850e-10 | 3.793e-10 | 2.489e-09 | 8.417e-10 |

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

Protocolo `m3-v3`. `blind_peaks.csv` SHA-256 `ba7949bc11c106a851560a27e347f5ba31f75b686b27709136927517a5b93438` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [14.135, 1419.422], L = 1405.3 |
| FWHM medida | 0.009 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 4026 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 5.132e-11 (máx. |F| = 81.6) |
| Quadratura: mudança ao reduzir painel pela metade | 1.789e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 2.093e-09 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.2135 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.050 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.2597 |
| Candidatos cuja decisão mudaria usando z refinado | 0 |
| Tolerância de matching (quantil 0.99) | 0.002 = 0.220 FWHM |
| Separação de pares com ≥90% recuperado | 2.00 FWHM (não atingiu a meta; usada a maior separação testada) |
| Linhas sintéticas isoladas | 34 |
| Detecções (nulo primário / secundário) | 18 / 18 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 42 resolvidas |
| Previstas detectáveis | 18 |
| Escore S; nulo (conjunto independente, B=999) | 18; média 0.004, máx. 1 |
| Detecções sem correspondente; detecções por realização nula | 0; 0.053 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=18); todas as 47 linhas | 2.195e-10 / 1.516e-09; 1.516e-09 / 8.060e-06 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=18); todas as 47 linhas | 1.553e-10 / 1.473e-09; 1.473e-09 / 8.059e-06 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=18); todas as 47 linhas | 2.317e-09 / 2.382e-08; 2.382e-08 / 1.299e-04 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 2.234e-08 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 5.542e-10 / 4.513e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.411; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.273; p = 0.001 |
| Linhas não detectadas | 29 |
| Tempo (s) | instrument: 0.5, null_shuffle: 6.4, null_gue: 9.3, synthetic: 2.2, arithmetic: 33.8 |

Figuras: `tables/pilot/spectrum_z.png`, `tables/pilot/coefficients.png`, `tables/pilot/synthetic_calibration.png`.

### bloco dev (zeros 1001–4000)

Protocolo `m3-v3`. `blind_peaks.csv` SHA-256 `b8e1959a259da0a8e37a60d9edc36423e8bb2ad7d158196b37d435b763541897` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [1420.417, 4506.311], L = 3085.9 |
| FWHM medida | 0.004 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 8841 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 2.811e-10 (máx. |F| = 179.1) |
| Quadratura: mudança ao reduzir painel pela metade | 5.534e-11 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 1.052e-13 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.3364 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.054 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3957 |
| Candidatos cuja decisão mudaria usando z refinado | 0 |
| Tolerância de matching (quantil 0.99) | 5.631e-04 = 0.138 FWHM |
| Separação de pares com ≥90% recuperado | 1.00 FWHM (medida) |
| Linhas sintéticas isoladas | 169 |
| Detecções (nulo primário / secundário) | 37 / 36 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 37 |
| Escore S; nulo (conjunto independente, B=999) | 37; média 0.000, máx. 0 |
| Detecções sem correspondente; detecções por realização nula | 0; 0.055 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=37); todas as 47 linhas | 5.400e-10 / 5.913e-08; 6.232e-10 / 3.854e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=37); todas as 47 linhas | 5.395e-10 / 5.912e-08; 6.222e-10 / 3.854e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=37); todas as 47 linhas | 7.604e-10 / 7.501e-07; 1.410e-09 / 4.998e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 7.946e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 7.883e-10 / 5.848e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.279; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.189; p = 0.001 |
| Linhas não detectadas | 10 |
| Tempo (s) | instrument: 1.3, null_shuffle: 20.7, null_gue: 56.4, synthetic: 23.8, arithmetic: 52.7 |

Figuras: `tables/dev/spectrum_z.png`, `tables/dev/coefficients.png`, `tables/dev/synthetic_calibration.png`.

### bloco val (zeros 4001–7000)

Protocolo `m3-v3`. `blind_peaks.csv` SHA-256 `a3bb2662f37f88f0ae249ddada5ba00c3622b8349bd183ce00631ffce4e9acc3` gravado antes do módulo aritmético.
Estatística de decisão: z na malha (idêntica para zeros, controles e sintéticos).

| Grandeza | Valor |
|---|---|
| Janela / densidade média | hann / rvm |
| Intervalo [A, B] | [4507.745, 7264.748], L = 2757.0 |
| FWHM medida | 0.005 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 7899 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 8.551e-11 (máx. |F| = 161.1) |
| Quadratura: mudança ao reduzir painel pela metade | 6.535e-10 |
| Termo suave: densidade rvm vs θ (máx. abs.) | 8.850e-14 |
| Nulo shuffle: B σ / limiar / escore | 200 / 999 / 999; limiar z = 3.3646 |
| Fração do conjunto-escore com máximo ≥ limiar (esperado ≈ α) | 0.038 |
| Nulo GUE: B σ / limiar | 100 / 199; limiar z = 3.3134 |
| Candidatos cuja decisão mudaria usando z refinado | 0 |
| Tolerância de matching (quantil 0.99) | 6.743e-04 = 0.148 FWHM |
| Separação de pares com ≥90% recuperado | 1.25 FWHM (medida) |
| Linhas sintéticas isoladas | 177 |
| Detecções (nulo primário / secundário) | 35 / 33 |
| Catálogo r log p | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Previstas detectáveis | 35 |
| Escore S; nulo (conjunto independente, B=999) | 35; média 0.002, máx. 1 |
| Detecções sem correspondente; detecções por realização nula | 0; 0.039 |
| p Monte Carlo global | 0.001 (resolução 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado `band_conjugate` (primário): mediana / máx. |razão−1| (n=35); todas as 47 linhas | 3.850e-10 / 2.572e-08; 6.313e-10 / 2.747e-07 |
| Ajuste direcionado `band_no_conjugate`: mediana / máx. |razão−1| (n=35); todas as 47 linhas | 3.793e-10 / 2.572e-08; 6.354e-10 / 2.747e-07 |
| Ajuste direcionado `centers_conjugate`: mediana / máx. |razão−1| (n=35); todas as 47 linhas | 2.489e-09 / 3.805e-07; 2.961e-09 / 3.181e-06 |
| Maior diferença entre variantes (razão, linhas selecionadas) | 3.548e-07 |
| Sensibilidade ±3e-09 (estimador primário): mediana / máx. |Δ razão| | 8.417e-10 / 5.949e-09 |
| Alinhamento de fase R (invariante a rotação comum) | 1.000; nulo q95 0.285; p = 0.001 |
| Sinal absoluto Q = média cos(erro de fase) | 1.000; nulo q95 0.200; p = 0.001 |
| Linhas não detectadas | 12 |
| Tempo (s) | instrument: 0.6, null_shuffle: 15.2, null_gue: 56.2, synthetic: 22.5, arithmetic: 49.4 |

Figuras: `tables/val/spectrum_z.png`, `tables/val/coefficients.png`, `tables/val/synthetic_calibration.png`.

