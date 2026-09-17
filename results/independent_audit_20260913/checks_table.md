| Código | Tolerância | baixo (b01) | intermediário (b05) | alto (c10) |
|---|---|---|---|---|
| D1 | n_t igual; dt, FWHM, W0 rel ≤ 1e-10 | **FORA** dt rel 2.50e-10 | **FORA** dt rel -1.20e-10 | ✓ dt rel -8.15e-11 |
| D2 | máx abs ≤ 1e-8 | **FORA** máx 4.09e-10 | **FORA** máx 3.20e-09 | **FORA** máx 5.48e-09 |
| D3 | máx ≤ 1e-7; mediana ≤ 1e-8 | **FORA** máx 2.88e-05; med 7.44e-09 | **FORA** máx 1.18e-05; med 3.67e-09 | **FORA** máx 6.41e-06; med 2.90e-09 |
| D4 | máx abs ≤ 1e-8 | ✓ máx 1.22e-10 | ✓ máx 3.36e-10 | ✓ máx 3.55e-09 |
| D9 | mesmas entradas; períodos ≤ 1e-14 | ✓ 47 = 47 | ✓ 47 = 47 | ✓ 47 = 47 |
| D5 | máx abs Δrazão ≤ 1e-9 (3 variantes, 47 linhas) | ✓ máx 5.67e-13 | ✓ máx 1.18e-11 | ✓ máx 3.26e-11 |
| S1 | mediana ≤ 0,03; p99 ≤ 0,08 | ✓ med 0.0109; p99 0.0474 | ✓ med 0.0107; p99 0.0510 | ✓ med 0.0124; p99 0.0445 |
| S2 | KS p ≥ 0,001 | ✓ p 0.9199 | ✓ p 0.3940 | ✓ p 0.0107 |
| S3 | ICs se sobrepõem | ✓ ref [3.307; 3.336] ind [3.283; 3.353] | ✓ ref [3.283; 3.313] ind [3.278; 3.346] | ✓ ref [3.269; 3.297] ind [3.238; 3.304] |
| S4 | faixa binomial 99,9% | ✓ 0.0345 (faixa 0.0345–0.0665) | ✓ 0.0415 (faixa 0.0345–0.0665) | ✓ 0.0420 (faixa 0.0345–0.0665) |
| S5 | linhas claramente decididas com mesmo status | ✓ 0 divergências; 7 não decididas | ✓ 0 divergências; 6 não decididas | ✓ 0 divergências; 8 não decididas |
| S6 | |z_ind/z_ref − 1| ≤ 0,05 em ≥ 95% das detectadas em ambas | ✓ 1.000 ≤5%; máx 0.032 | ✓ 0.970 ≤5%; máx 0.057 | ✓ 1.000 ≤5%; máx 0.033 |
| S7 | |ΔS| ≤ nº não claramente decididas; sem correspondência = 0 | ✓ S 34/34 | ✓ S 33/34 | ✓ S 33/32 |
| S8 | p_ind ≤ 0,01 | ✓ 0.0005 / 0.0001 | ✓ 0.0005 / 0.0001 | ✓ 0.0005 / 0.0001 |
| S9 | razão ∈ [0,5; 2]; separação igual/adjacente | ✓ razão 1.26; sep 1.25/1.25 | ✓ razão 0.91; sep 1.25/1.25 | ✓ razão 1.08; sep 1.25/1.25 |
| S10 | vereditos por bloco iguais | ✓ C1 True/True; C2 True/True | ✓ C1 True/True; C2 True/True | ✓ C1 True/True; C2 True/True |
| D6 | |ΔR|, |ΔQ| ≤ 1e-9 se o conjunto elegível for igual | ✓ ΔQ 0.0e+00; mesmo conjunto: True | ✓ ΔQ 3.9e-12; mesmo conjunto: False | ✓ ΔQ 2.5e-12; mesmo conjunto: False |
| S11 | ambos ≤ 0,01 | ✓ 0.001 / 0.001 | ✓ 0.001 / 0.001 | ✓ 0.001 / 0.001 |
| D7 | Var, CDF, R₂ rel ≤ 1e-10; K_c abs ≤ 1e-8 + rel 1e-8 | ✓ Var 0.0000; K rel 2.52e-11 | ✓ Var 0.0000; K rel 2.51e-12 | ✓ Var 0.0000; K rel 7.13e-11 |
| S12 | piso: p_ind ≤ 2/300; senão |Δp| ≤ 3·EP + 0,01 | ✓ todos dentro | ✓ todos dentro | ✓ todos dentro |
| D8 | P₀ ≤ 1e-7; P₁ ≤ 1e-4; CDF ≤ 1e-6; distâncias ≤ 1e-6 | **FORA** CDF 3.92e-05; dist 6.15e-06 | **FORA** CDF 3.23e-05; dist 5.24e-06 | **FORA** CDF 2.72e-05; dist 3.99e-06 |
| S13 | razão ∈ [0,75; 1,33] | ✓ 0.997 | ✓ 1.036 | ✓ 1.033 |