# Relatório M3 — espectroscopia inversa por blocos

**ID:** `run_20260913_024706_m3_holdout-full`
**Blocos:** holdout, full
**Duração:** 1090.6 s; pico de memória 323 MB
**Comando:** `/home/dionatandiego11/Downloads/hipotese-riemann/src/riemann_spectra/__main__.py m3 --blocks holdout,full --workers 4`

Protocolo congelado em 2026-09-13T02:46:54.225011+00:00 (config `c77536530efb7d1a…`, módulos `720d907374fb9142…`).

## Resumo por bloco

| Bloco | Índices | L | FWHM | Catálogo | Detectáveis | Detecções | S | Sem corresp. | S nulo máx | p | Recuperação | mediana |razão−1| | Δ perturbação | |fase| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| holdout | 7001–10000 | 2612 | 0.005 | 47 | 36 | 36 | 36 | 0 | 0 | 0.001 | 1.000 | 5.171e-10 | 8.919e-10 | 7.569e-10 |
| full | 1–10000 | 9864 | 0.001 | 47 | 41 | 41 | 41 | 0 | 0 | 0.001 | 1.000 | 1.897e-10 | 4.778e-10 | 1.068e-10 |

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

### bloco holdout (zeros 7001–10000)

Protocolo de detecção cega: `blind_peaks.csv` SHA-256 `4c7317f1f19d51ebdd2c84d25751525c8b811f5262c4f499f467c54078fd80aa` gravado antes do módulo aritmético.

| Grandeza | Valor |
|---|---|
| Janela [A, B] | [7265.963, 9877.783], L = 2611.8 |
| FWHM medida da janela de Hann | 0.005 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 7483 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 1.543e-10 (máx. |F| = 152.7) |
| Quadratura: mudança ao reduzir painel pela metade | 7.754e-10 |
| Densidade média rvm vs θ (máx. abs.) | 8.036e-14 |
| Limiar FWER z (shuffle, B=999) | 3.291 |
| Limiar FWER z (GUE, B=199) | 3.368 |
| Mediana de |F|/σ nos zeros (toda a malha) | 4.974e-04 |
| Tolerância de matching (quantil 0.99 do erro sintético) | 6.211e-04 = 0.129 FWHM |
| Separação para recuperar ≥90% das linhas de pares | 1.25 FWHM |
| Linhas sintéticas isoladas usadas | 195 |
| Detecções cegas (nulo primário / secundário) | 36 / 32 |
| Catálogo r log p em [t_min, t_max] | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Linhas previstas detectáveis (|c| L/4 ≥ z σ) | 36 |
| Escore S (linhas com detecção correspondente) | 36; nulo: média 0.000, máx. 0 |
| Detecções sem correspondente no catálogo | 0 (detecções por realização nula: 0.050) |
| p Monte Carlo global (B=999) | 0.001 (piso 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado: mediana |razão − 1| (resolvidas e detectáveis, n=36) | 5.171e-10 |
| Ajuste direcionado: mediana |erro de fase| | 7.569e-10 rad |
| Sensibilidade: mediana |Δ razão| com zeros perturbados ±3e-09 | 8.919e-10 |
| Coerência de fase R (controle de fase, B=999) | 1.000; nulo q95 0.283; p = 0.001 |
| Linhas não detectadas | 11 |
| Tempo (s) | instrument: 0.7, null_shuffle: 11.9, null_gue: 57.7, synthetic: 23.2, arithmetic: 48.5 |

Figuras: `tables/holdout/spectrum_z.png`, `tables/holdout/coefficients.png`, `tables/holdout/synthetic_calibration.png`.

### bloco full (zeros 1–10000)

Protocolo de detecção cega: `blind_peaks.csv` SHA-256 `876996181f4af3cb4c503b657e535256f384e94512e9fa589c6e6ce90b198932` gravado antes do módulo aritmético.

| Grandeza | Valor |
|---|---|
| Janela [A, B] | [14.135, 9877.783], L = 9863.6 |
| FWHM medida da janela de Hann | 0.001 (2.000 × 2π/L); lóbulo lateral -31.5 dB |
| Malha | 28258 pontos, 8.0 por FWHM |
| NUFFT vs soma direta (máx. abs.) | 6.746e-10 (máx. |F| = 572.8) |
| Quadratura: mudança ao reduzir painel pela metade | 9.929e-10 |
| Densidade média rvm vs θ (máx. abs.) | 4.241e-11 |
| Limiar FWER z (shuffle, B=999) | 3.505 |
| Limiar FWER z (GUE, B=199) | 3.515 |
| Mediana de |F|/σ nos zeros (toda a malha) | 1.781e-05 |
| Tolerância de matching (quantil 0.99 do erro sintético) | 1.758e-04 = 0.138 FWHM |
| Separação para recuperar ≥90% das linhas de pares | 2.00 FWHM |
| Linhas sintéticas isoladas usadas | 63 |
| Detecções cegas (nulo primário / secundário) | 41 / 40 |
| Catálogo r log p em [t_min, t_max] | 47 (34 primitivas, 13 repetições); 47 resolvidas |
| Linhas previstas detectáveis (|c| L/4 ≥ z σ) | 41 |
| Escore S (linhas com detecção correspondente) | 41; nulo: média 0.000, máx. 0 |
| Detecções sem correspondente no catálogo | 0 (detecções por realização nula: 0.051) |
| p Monte Carlo global (B=999) | 0.001 (piso 0.001) |
| Recuperação entre previstas detectáveis | 1.000; detectáveis perdidas: nenhuma |
| Detectadas embora previstas indetectáveis | 0 |
| Ajuste direcionado: mediana |razão − 1| (resolvidas e detectáveis, n=41) | 1.897e-10 |
| Ajuste direcionado: mediana |erro de fase| | 1.068e-10 rad |
| Sensibilidade: mediana |Δ razão| com zeros perturbados ±3e-09 | 4.778e-10 |
| Coerência de fase R (controle de fase, B=999) | 1.000; nulo q95 0.275; p = 0.001 |
| Linhas não detectadas | 6 |
| Tempo (s) | instrument: 2.0, null_shuffle: 32.7, null_gue: 613.3, synthetic: 173.1, arithmetic: 126.5 |

Figuras: `tables/full/spectrum_z.png`, `tables/full/coefficients.png`, `tables/full/synthetic_calibration.png`.

