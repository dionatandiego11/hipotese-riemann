# Relatório M3 — espectroscopia inversa por blocos

**ID:** `run_20260913_023918_m3_pilot-dev-val`
**Blocos:** pilot, dev, val
**Duração:** 397.5 s; pico de memória 212 MB
**Comando:** `/home/dionatandiego11/Downloads/hipotese-riemann/src/riemann_spectra/__main__.py m3 --blocks pilot,dev,val --workers 4`

Execução sem blocos reservados; congelamento não exigido.

## Resumo por bloco

| Bloco | Índices | L | FWHM | Catálogo | Detectáveis | Detecções | S | Sem corresp. | S nulo máx | p | Recuperação | mediana |razão−1| | Δ perturbação | |fase| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pilot | 1–1000 | 1405 | 0.009 | 47 | 18 | 18 | 18 | 0 | 1 | 0.001 | 1.000 | 1.553e-10 | 7.025e-10 | 2.741e-10 |
| dev | 1001–4000 | 3086 | 0.004 | 47 | 38 | 38 | 38 | 0 | 0 | 0.001 | 1.000 | 5.508e-10 | 7.670e-10 | 5.052e-10 |
| val | 4001–7000 | 2757 | 0.005 | 47 | 36 | 36 | 36 | 0 | 1 | 0.001 | 1.000 | 3.866e-10 | 8.835e-10 | 5.487e-10 |

Definições: *Detecções* são máximos locais de |F|/σ_nulo acima do limiar FWER do nulo de permutação de espaçamentos,
obtidos sem catálogo. *S* conta linhas r log p com uma detecção a menos da tolerância calibrada (um a um).
*p* compara S com a mesma cadeia aplicada a cada realização nula. *Recuperação* é a fração das linhas cujo
coeficiente de referência excede o limite de detecção previsto pelo nulo. As colunas de razão e fase vêm da
**medição direcionada** nos períodos conhecidos (ajuste conjunto com a resposta da janela), que não é detecção cega.

## Interpretação e limites

- A análise mede a transformada de uma janela finita de zeros; a comparação usa a forma distribucional da fórmula
  explícita, válida para zeros na janela sobre a linha crítica, fato verificado numericamente nesta faixa de alturas.
  A concordância numérica não demonstra RH nem acrescenta zeros além dos tabelados.
- O "fundo" entre linhas nos zeros não é ruído estatístico: é vazamento determinístico de outras linhas pelos lóbulos
  laterais da janela. A escala de ruído usada para decidir detecções vem, portanto, dos controles nulos.
- Linhas abaixo do limite de detecção do nulo não são evidência de ausência; ver colunas de detectabilidade prevista.
- Os valores-p são limitados inferiormente por 1/(B+1) e medem incompatibilidade com o nulo declarado.

## Detalhes por bloco

### bloco pilot (zeros 1–1000)

Protocolo de detecção cega: `blind_peaks.csv` SHA-256 `c138ed7d573be039a48e708355b4e38cf8a464c64baff39a43655a008051113e` gravado antes do módulo aritmético.

| Grandeza | Valor |
|---|---|
| Janela [A, B] | [14.135, 1419.422], L = 1405.3 |
| FWHM medida da janela de Hann | 0.009 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 4026 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.749e-10 (máx. |F| = 81.6) |
| Quadratura: mudança ao reduzir painel pela metade | 1.789e-11 |
| Densidade média rvm vs θ (máx. abs.) | 2.093e-09 |
| Limiar FWER z (shuffle, B=999) | 3.259 |
| Limiar FWER z (GUE, B=199) | 3.293 |
| Mediana de |F|/σ nos zeros (toda a malha) | 0.002 |
| Tolerância de matching (quantil 0.99 do erro sintético) | 0.001 = 0.159 FWHM |
| Separação para recuperar ≥90% das linhas de pares | 2.00 FWHM |
| Linhas sintéticas isoladas usadas | 33 |
| Detecções cegas (nulo primário / secundário) | 18 / 17 |
| Catálogo r log p em [t_min, t_max] | 47 (34 primitivas, 13 repetições); 42 resolvidas |
| Linhas previstas detectáveis (|c| L/4 ≥ z σ) | 18 |
| Escore S (linhas com detecção correspondente) | 18; nulo: média 0.002, máx. 1 |
| Detecções sem correspondente no catálogo | 0 (detecções por realização nula: 0.049) |
| p Monte Carlo global (B=999) | 0.001 (piso 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado: mediana |razão − 1| (resolvidas e detectáveis, n=18) | 1.553e-10 |
| Ajuste direcionado: mediana |erro de fase| | 2.741e-10 rad |
| Sensibilidade: mediana |Δ razão| com zeros perturbados ±3e-09 | 7.025e-10 |
| Coerência de fase R (controle de fase, B=999) | 1.000; nulo q95 0.392; p = 0.001 |
| Linhas não detectadas | 29 |
| Tempo (s) | instrument: 0.5, null_shuffle: 2.8, null_gue: 9.7, synthetic: 2.5, arithmetic: 44.0 |

Figuras: `tables/pilot/spectrum_z.png`, `tables/pilot/coefficients.png`, `tables/pilot/synthetic_calibration.png`.

### bloco dev (zeros 1001–4000)

Protocolo de detecção cega: `blind_peaks.csv` SHA-256 `e7337234209ed31d09d19450bfb222521b10b7f1589608d86a9f3d95bfea02b6` gravado antes do módulo aritmético.

| Grandeza | Valor |
|---|---|
| Janela [A, B] | [1420.417, 4506.311], L = 3085.9 |
| FWHM medida da janela de Hann | 0.004 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 8841 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.064e-10 (máx. |F| = 179.1) |
| Quadratura: mudança ao reduzir painel pela metade | 5.534e-11 |
| Densidade média rvm vs θ (máx. abs.) | 1.052e-13 |
| Limiar FWER z (shuffle, B=999) | 3.311 |
| Limiar FWER z (GUE, B=199) | 3.351 |
| Mediana de |F|/σ nos zeros (toda a malha) | 3.198e-04 |
| Tolerância de matching (quantil 0.99 do erro sintético) | 4.539e-04 = 0.111 FWHM |
| Separação para recuperar ≥90% das linhas de pares | 1.00 FWHM |
| Linhas sintéticas isoladas usadas | 169 |
| Detecções cegas (nulo primário / secundário) | 38 / 36 |
| Catálogo r log p em [t_min, t_max] | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Linhas previstas detectáveis (|c| L/4 ≥ z σ) | 38 |
| Escore S (linhas com detecção correspondente) | 38; nulo: média 0.000, máx. 0 |
| Detecções sem correspondente no catálogo | 0 (detecções por realização nula: 0.050) |
| p Monte Carlo global (B=999) | 0.001 (piso 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado: mediana |razão − 1| (resolvidas e detectáveis, n=38) | 5.508e-10 |
| Ajuste direcionado: mediana |erro de fase| | 5.052e-10 rad |
| Sensibilidade: mediana |Δ razão| com zeros perturbados ±3e-09 | 7.670e-10 |
| Coerência de fase R (controle de fase, B=999) | 1.000; nulo q95 0.286; p = 0.001 |
| Linhas não detectadas | 9 |
| Tempo (s) | instrument: 0.8, null_shuffle: 15.5, null_gue: 78.1, synthetic: 26.6, arithmetic: 69.8 |

Figuras: `tables/dev/spectrum_z.png`, `tables/dev/coefficients.png`, `tables/dev/synthetic_calibration.png`.

### bloco val (zeros 4001–7000)

Protocolo de detecção cega: `blind_peaks.csv` SHA-256 `7fe9f48c266a66b04921e8494a801abb7a90f9ef1c3eb1c586188eae60918cd5` gravado antes do módulo aritmético.

| Grandeza | Valor |
|---|---|
| Janela [A, B] | [4507.745, 7264.748], L = 2757.0 |
| FWHM medida da janela de Hann | 0.005 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 7899 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.038e-10 (máx. |F| = 161.1) |
| Quadratura: mudança ao reduzir painel pela metade | 6.535e-10 |
| Densidade média rvm vs θ (máx. abs.) | 8.850e-14 |
| Limiar FWER z (shuffle, B=999) | 3.342 |
| Limiar FWER z (GUE, B=199) | 3.351 |
| Mediana de |F|/σ nos zeros (toda a malha) | 4.284e-04 |
| Tolerância de matching (quantil 0.99 do erro sintético) | 6.076e-04 = 0.133 FWHM |
| Separação para recuperar ≥90% das linhas de pares | 1.25 FWHM |
| Linhas sintéticas isoladas usadas | 188 |
| Detecções cegas (nulo primário / secundário) | 36 / 33 |
| Catálogo r log p em [t_min, t_max] | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Linhas previstas detectáveis (|c| L/4 ≥ z σ) | 36 |
| Escore S (linhas com detecção correspondente) | 36; nulo: média 0.001, máx. 1 |
| Detecções sem correspondente no catálogo | 0 (detecções por realização nula: 0.050) |
| p Monte Carlo global (B=999) | 0.001 (piso 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado: mediana |razão − 1| (resolvidas e detectáveis, n=36) | 3.866e-10 |
| Ajuste direcionado: mediana |erro de fase| | 5.487e-10 rad |
| Sensibilidade: mediana |Δ razão| com zeros perturbados ±3e-09 | 8.835e-10 |
| Coerência de fase R (controle de fase, B=999) | 1.000; nulo q95 0.284; p = 0.001 |
| Linhas não detectadas | 11 |
| Tempo (s) | instrument: 0.7, null_shuffle: 13.0, null_gue: 59.5, synthetic: 25.1, arithmetic: 48.2 |

Figuras: `tables/val/spectrum_z.png`, `tables/val/coefficients.png`, `tables/val/synthetic_calibration.png`.

