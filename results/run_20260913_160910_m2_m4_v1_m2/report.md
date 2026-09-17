# Relatório de execução — M2

**ID:** `run_20260913_160910_m2_m4_v1_m2`
**Data UTC:** `2026-09-13T17:19:49.547817+00:00`
**Perfil:** `m4_v1_m2`
**Zeros analisados:** `40000`

## Resumo

Execução M2 com 40000 zeros em 4238.7 s (pico de memória 218 MB).

## Afirmações sustentadas por esta execução

- B: hashes de dados conferem com o manifesto de odlyzko_zeros1_first40000; 40000 ordenadas finitas e estritamente crescentes; validação mpmath do mesmo arquivo (20 índices, máx. |erro| = 2.40e-09, critério abs_error <= declared_source_error).
- B: controles verificados — permutar a ordem dos níveis altera R2 em 0.0e+00 e K_c em 0.0e+00; inversão de Nbar com erro 3.6e-12; GUE denso e tridiagonal (N=400, 30 matrizes) com variâncias de espaçamento 0.1819 e 0.1852 e distância sup entre CDFs 0.010.
- Secundária CUE/b01 (N_eff=1.72, fora do domínio validado): distância RMS da CDF ao limite 0.0096, à predição corrigida 0.0080 (ruído amostral GUE 0.0029); Var(s) medida 0.1582, limite 0.1800, corrigida 0.1413.
- B/b01 (zeros 10001–13000): média de espaçamento 0.9997 e variância 0.1582 antes de renormalização (envelope GUE 95% da variância 0.1715–0.1903); p do envelope GUE (CDF, R2, K_c) = 0.001, 0.465, 0.001; p do envelope Poisson (CDF) = 0.001 (B=999/999).
- Secundária CUE/b02 (N_eff=1.77, fora do domínio validado): distância RMS da CDF ao limite 0.0090, à predição corrigida 0.0079 (ruído amostral GUE 0.0029); Var(s) medida 0.1587, limite 0.1800, corrigida 0.1428.
- B/b02 (zeros 13001–16000): média de espaçamento 1.0002 e variância 0.1587 antes de renormalização (envelope GUE 95% da variância 0.1705–0.1903); p do envelope GUE (CDF, R2, K_c) = 0.001, 0.001, 0.001; p do envelope Poisson (CDF) = 0.001 (B=999/999).
- Secundária CUE/b03 (N_eff=1.81, fora do domínio validado): distância RMS da CDF ao limite 0.0089, à predição corrigida 0.0072 (ruído amostral GUE 0.0029); Var(s) medida 0.1594, limite 0.1800, corrigida 0.1440.
- B/b03 (zeros 16001–19000): média de espaçamento 1.0000 e variância 0.1594 antes de renormalização (envelope GUE 95% da variância 0.1706–0.1899); p do envelope GUE (CDF, R2, K_c) = 0.001, 0.270, 0.001; p do envelope Poisson (CDF) = 0.001 (B=999/999).
- Secundária CUE/b04 (N_eff=1.84, fora do domínio validado): distância RMS da CDF ao limite 0.0082, à predição corrigida 0.0076 (ruído amostral GUE 0.0029); Var(s) medida 0.1605, limite 0.1800, corrigida 0.1449.
- B/b04 (zeros 19001–22000): média de espaçamento 0.9998 e variância 0.1605 antes de renormalização (envelope GUE 95% da variância 0.1700–0.1894); p do envelope GUE (CDF, R2, K_c) = 0.001, 0.230, 0.001; p do envelope Poisson (CDF) = 0.001 (B=999/999).
- Secundária CUE/b05 (N_eff=1.87, fora do domínio validado): distância RMS da CDF ao limite 0.0087, à predição corrigida 0.0068 (ruído amostral GUE 0.0029); Var(s) medida 0.1597, limite 0.1800, corrigida 0.1457.
- B/b05 (zeros 22001–25000): média de espaçamento 0.9999 e variância 0.1597 antes de renormalização (envelope GUE 95% da variância 0.1712–0.1899); p do envelope GUE (CDF, R2, K_c) = 0.001, 0.092, 0.001; p do envelope Poisson (CDF) = 0.001 (B=999/999).
- Secundária CUE/b06 (N_eff=1.89, fora do domínio validado): distância RMS da CDF ao limite 0.0085, à predição corrigida 0.0068 (ruído amostral GUE 0.0029); Var(s) medida 0.1595, limite 0.1800, corrigida 0.1464.
- B/b06 (zeros 25001–28000): média de espaçamento 1.0001 e variância 0.1595 antes de renormalização (envelope GUE 95% da variância 0.1707–0.1897); p do envelope GUE (CDF, R2, K_c) = 0.001, 0.042, 0.001; p do envelope Poisson (CDF) = 0.001 (B=999/999).
- Secundária CUE/b07 (N_eff=1.91, fora do domínio validado): distância RMS da CDF ao limite 0.0086, à predição corrigida 0.0067 (ruído amostral GUE 0.0029); Var(s) medida 0.1624, limite 0.1800, corrigida 0.1470.
- B/b07 (zeros 28001–31000): média de espaçamento 0.9998 e variância 0.1624 antes de renormalização (envelope GUE 95% da variância 0.1708–0.1898); p do envelope GUE (CDF, R2, K_c) = 0.001, 0.044, 0.003; p do envelope Poisson (CDF) = 0.001 (B=999/999).
- Secundária CUE/b08 (N_eff=1.93, fora do domínio validado): distância RMS da CDF ao limite 0.0085, à predição corrigida 0.0062 (ruído amostral GUE 0.0029); Var(s) medida 0.1606, limite 0.1800, corrigida 0.1475.
- B/b08 (zeros 31001–34000): média de espaçamento 0.9997 e variância 0.1606 antes de renormalização (envelope GUE 95% da variância 0.1708–0.1900); p do envelope GUE (CDF, R2, K_c) = 0.001, 0.075, 0.001; p do envelope Poisson (CDF) = 0.001 (B=999/999).
- Secundária CUE/b09 (N_eff=1.95, fora do domínio validado): distância RMS da CDF ao limite 0.0080, à predição corrigida 0.0066 (ruído amostral GUE 0.0029); Var(s) medida 0.1596, limite 0.1800, corrigida 0.1480.
- B/b09 (zeros 34001–37000): média de espaçamento 0.9999 e variância 0.1596 antes de renormalização (envelope GUE 95% da variância 0.1705–0.1898); p do envelope GUE (CDF, R2, K_c) = 0.001, 0.177, 0.001; p do envelope Poisson (CDF) = 0.001 (B=999/999).
- Secundária CUE/b10 (N_eff=1.97, fora do domínio validado): distância RMS da CDF ao limite 0.0078, à predição corrigida 0.0060 (ruído amostral GUE 0.0029); Var(s) medida 0.1616, limite 0.1800, corrigida 0.1484.
- B/b10 (zeros 37001–40000): média de espaçamento 0.9999 e variância 0.1616 antes de renormalização (envelope GUE 95% da variância 0.1703–0.1895); p do envelope GUE (CDF, R2, K_c) = 0.001, 0.106, 0.001; p do envelope Poisson (CDF) = 0.001 (B=999/999).
- C3/gue_cdf: 10 de 10 blocos rejeitados após Holm entre blocos (menor p ajustado atingível 0.010).
- C3/gue_r2: 1 de 10 blocos rejeitados após Holm entre blocos (menor p ajustado atingível 0.010).
- C3/gue_k_connected: 10 de 10 blocos rejeitados após Holm entre blocos (menor p ajustado atingível 0.010).
- C3/poisson_cdf: 10 de 10 blocos rejeitados após Holm entre blocos (menor p ajustado atingível 0.010).
- C3/poisson_r2: 10 de 10 blocos rejeitados após Holm entre blocos (menor p ajustado atingível 0.010).
- C3/poisson_k_connected: 10 de 10 blocos rejeitados após Holm entre blocos (menor p ajustado atingível 0.010).

## Limitações

- A validação por amostra não certifica completude da tabela nem localização rigorosa de todos os zeros.
- Blocos contíguos de um espectro determinístico não são amostras independentes.
- Envelopes GUE usam uma matriz por realização (níveis centrais), sem concatenação de matrizes.
- Valores-p do envelope medem incompatibilidade com o ensemble finito do mesmo tamanho, não com o limite assintótico.

## Métricas

```json
{
  "data": {
    "dataset_id": "odlyzko_zeros1_first40000",
    "raw_sha256_matches_manifest": true,
    "processed_sha256_matches_manifest": true,
    "validation_matches_processed_file": true,
    "zeros_used": 40000,
    "zeros_in_validated_file": 40000,
    "strictly_increasing": true,
    "all_finite": true,
    "mpmath_sample_size": 20,
    "mpmath_max_abs_error": 2.4010660126805305e-09,
    "mpmath_tolerance_rule": "abs_error <= declared_source_error",
    "mpmath_all_within_tolerance": true
  },
  "m1_checks_index_range": [
    1,
    10000
  ],
  "unfolding_inverse_max_abs_error": 3.637978807091713e-12,
  "permutation_invariance": {
    "r2_max_abs_diff": 0.0,
    "sff_max_abs_diff": 0.0
  },
  "control_poisson": {
    "fixed_count": {
      "n": 20000,
      "density": 0.9999667575116871,
      "spacing_var": 1.0039248777848593
    },
    "random_count": {
      "n": 19990,
      "density": 0.9995,
      "spacing_var": 0.9910026838228196
    },
    "convention": "comparações com zeros usam contagem fixa (mesmo n que o bloco)"
  },
  "control_gue_dense_vs_tridiagonal": {
    "matrix_dim": 400,
    "realizations": 30,
    "bulk_interval": "[-0.5, 0.5] do semicírculo",
    "dense_mean": 0.9998468016113619,
    "dense_var": 0.1818665179049772,
    "tridiagonal_mean": 0.9992720553888845,
    "tridiagonal_var": 0.185168739936159,
    "cdf_sup_distance": 0.010018254704863394,
    "n_spacings_each": 7274
  },
  "blocks": {
    "b01": {
      "indices": [
        10001,
        13000
      ],
      "gamma_range": [
        9878.654772383,
        12397.778202687
      ],
      "n_levels": 3000,
      "spacing_mean_before_renormalization": 0.9997365881645528,
      "spacing_variance": 0.15819823822833126,
      "spacing_skewness": 0.48345718910747243,
      "spacing_kurtosis": 0.13577674076740065,
      "ks_distance_wigner_surmise": 0.026590925709870372,
      "wasserstein_wigner_surmise": 0.02273654589535933,
      "ks_distance_poisson": 0.30071280684318236,
      "wasserstein_poisson": 0.4279878098703671,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 6.712889444315806e-07,
        "spacing_variance_theta": 0.15819823821388984,
        "max_abs_spacing_difference": 1.3096723705530167e-10
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.002171645193479096,
        "1-2": 0.003680926287999115,
        "2-5": 0.0025523665055099507
      },
      "r2_fraction_bins_outside_gue_95_band": 0.08,
      "sff_fraction_tau_outside_gue_95_band": 0.25,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.00861466923670495,
            "distance_null_median": 0.0025789773881590193,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.051571886785952994,
            "distance_null_median": 0.050964985628546726,
            "p_value_mc": 0.465,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.5369881487524112,
            "distance_null_median": 0.2559143549057731,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.17145603011197708,
            0.19031308984256756
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.11747747685839405,
            "distance_null_median": 0.0037023600291181415,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.27380329682520854,
            "distance_null_median": 0.05740463724330116,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.6764388954075499,
            "distance_null_median": 0.31263314469230175,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.9302225605900554,
            1.0716296657495252
          ]
        }
      },
      "cue_secondary": {
        "E_median": 11147.851328275,
        "N_eff_range_in_block": [
          1.69401996687108,
          1.7462982234991185
        ],
        "N_eff": 1.7218392380620149,
        "alpha": 1.196761851027691,
        "rms_cdf_distance_to_limit": 0.00956353558961102,
        "rms_cdf_distance_to_cue_corrected": 0.008014649671567599,
        "ratio_cue_over_limit": 0.8380425415339079,
        "sampling_noise_rms_gue_ensemble": 0.0028629090942798195,
        "sup_cdf_distance_to_limit": 0.02551776464764302,
        "sup_cdf_distance_to_cue_corrected": 0.021047737992621385,
        "spacing_variance_measured": 0.15819823822833126,
        "spacing_variance_limit": 0.17999376244101595,
        "spacing_variance_cue_corrected": 0.14129551531285156,
        "domain_warning": "N_eff fora do domínio validado na fonte (7,7 e 11,3); O(N_eff^-4) não desprezível."
      }
    },
    "b02": {
      "indices": [
        13001,
        16000
      ],
      "gamma_range": [
        12398.691913962,
        14852.514122194
      ],
      "n_levels": 3000,
      "spacing_mean_before_renormalization": 1.0001722292183446,
      "spacing_variance": 0.158672811038495,
      "spacing_skewness": 0.4933340529120594,
      "spacing_kurtosis": 0.13853651910914744,
      "ks_distance_wigner_surmise": 0.025519715445328023,
      "wasserstein_wigner_surmise": 0.02101044733288778,
      "ks_distance_poisson": 0.30293940564111416,
      "wasserstein_poisson": 0.4270820498186804,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 5.34850187250413e-07,
        "spacing_variance_theta": 0.15867281102916792,
        "max_abs_spacing_difference": 8.549250196665525e-11
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.006085195527952489,
        "1-2": 0.004337234753252063,
        "2-5": 0.004876278244304231
      },
      "r2_fraction_bins_outside_gue_95_band": 0.14,
      "sff_fraction_tau_outside_gue_95_band": 0.25,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.00801855992752348,
            "distance_null_median": 0.002564866852762642,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.070356831088601,
            "distance_null_median": 0.0509715902221392,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.42287765502792557,
            "distance_null_median": 0.2548908763119704,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.1704714195572994,
            0.1902733400460226
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.1173809868287311,
            "distance_null_median": 0.00365680794892662,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.2780963237519518,
            "distance_null_median": 0.05751134260311231,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.6215413033219045,
            "distance_null_median": 0.31417752813751604,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.9301074865287325,
            1.072192767039436
          ]
        }
      },
      "cue_secondary": {
        "E_median": 13632.840227638499,
        "N_eff_range_in_block": [
          1.7463151854112215,
          1.7878766603609961
        ],
        "N_eff": 1.768155003293602,
        "alpha": 1.1916077917502206,
        "rms_cdf_distance_to_limit": 0.009020813290985549,
        "rms_cdf_distance_to_cue_corrected": 0.00794312309678573,
        "ratio_cue_over_limit": 0.8805329232036374,
        "sampling_noise_rms_gue_ensemble": 0.002851928293007153,
        "sup_cdf_distance_to_limit": 0.02589217315548986,
        "sup_cdf_distance_to_cue_corrected": 0.022894864848284457,
        "spacing_variance_measured": 0.158672811038495,
        "spacing_variance_limit": 0.17999376244101595,
        "spacing_variance_cue_corrected": 0.14281749882417305,
        "domain_warning": "N_eff fora do domínio validado na fonte (7,7 e 11,3); O(N_eff^-4) não desprezível."
      }
    },
    "b03": {
      "indices": [
        16001,
        19000
      ],
      "gamma_range": [
        14853.311400585,
        17255.317628137
      ],
      "n_levels": 3000,
      "spacing_mean_before_renormalization": 1.000014736153394,
      "spacing_variance": 0.1594454248038019,
      "spacing_skewness": 0.4839784658441538,
      "spacing_kurtosis": 0.16414355980526585,
      "ks_distance_wigner_surmise": 0.023937208863016604,
      "wasserstein_wigner_surmise": 0.020394300544311485,
      "ks_distance_poisson": 0.3037490972278367,
      "wasserstein_poisson": 0.4267524089837701,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 4.464636731427163e-07,
        "spacing_variance_theta": 0.15944542479725476,
        "max_abs_spacing_difference": 6.184563972055912e-11
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.0026979511700142788,
        "1-2": 0.0028343732459125987,
        "2-5": 0.0030558120544248685
      },
      "r2_fraction_bins_outside_gue_95_band": 0.12,
      "sff_fraction_tau_outside_gue_95_band": 0.23,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.008017182229510096,
            "distance_null_median": 0.0025954639098973126,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.053970998027890606,
            "distance_null_median": 0.050588592200234525,
            "p_value_mc": 0.27,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.47463624711681696,
            "distance_null_median": 0.2573887258793384,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.17056869230371985,
            0.18987524378745682
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.11717058117732196,
            "distance_null_median": 0.003648162482285329,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.2725869137515516,
            "distance_null_median": 0.057328277978407796,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.6231292139145991,
            "distance_null_median": 0.3129111219098446,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.9327618988733795,
            1.0670104968563663
          ]
        }
      },
      "cue_secondary": {
        "E_median": 16059.811257815,
        "N_eff_range_in_block": [
          1.7878890148291218,
          1.8223891008609958
        ],
        "N_eff": 1.8058636771753638,
        "alpha": 1.1876067833553816,
        "rms_cdf_distance_to_limit": 0.008875532459500821,
        "rms_cdf_distance_to_cue_corrected": 0.0071606073903764484,
        "ratio_cue_over_limit": 0.8067805985782149,
        "sampling_noise_rms_gue_ensemble": 0.0028946935881198504,
        "sup_cdf_distance_to_limit": 0.024633532740851546,
        "sup_cdf_distance_to_cue_corrected": 0.01961791916776856,
        "spacing_variance_measured": 0.1594454248038019,
        "spacing_variance_limit": 0.17999376244101595,
        "spacing_variance_cue_corrected": 0.14399252030015686,
        "domain_warning": "N_eff fora do domínio validado na fonte (7,7 e 11,3); O(N_eff^-4) não desprezível."
      }
    },
    "b04": {
      "indices": [
        19001,
        22000
      ],
      "gamma_range": [
        17256.387732148,
        19616.305076708
      ],
      "n_levels": 3000,
      "spacing_mean_before_renormalization": 0.9998498981507143,
      "spacing_variance": 0.1605282223062201,
      "spacing_skewness": 0.4716705348478709,
      "spacing_kurtosis": 0.12876396523935796,
      "ks_distance_wigner_surmise": 0.02395954090026528,
      "wasserstein_wigner_surmise": 0.018807493353082762,
      "ks_distance_poisson": 0.3049553329453078,
      "wasserstein_poisson": 0.42485007132464064,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 3.842869773507118e-07,
        "spacing_variance_theta": 0.16052822230126138,
        "max_abs_spacing_difference": 4.729372449219227e-11
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.003056476910130922,
        "1-2": 0.0014859073122865459,
        "2-5": 0.003436264084885155
      },
      "r2_fraction_bins_outside_gue_95_band": 0.1,
      "sff_fraction_tau_outside_gue_95_band": 0.3,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.007285241223246645,
            "distance_null_median": 0.0026154083944336056,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.054870603567715226,
            "distance_null_median": 0.05072682713357562,
            "p_value_mc": 0.23,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.38041478511260235,
            "distance_null_median": 0.25702216038704534,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.16996260506721614,
            0.18939859189693883
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.11684598186041249,
            "distance_null_median": 0.0037122011614853442,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.2731278631472832,
            "distance_null_median": 0.0573616823664904,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.5485494834539357,
            "distance_null_median": 0.31390053622969205,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.9317182166004427,
            1.075032037451414
          ]
        }
      },
      "cue_secondary": {
        "E_median": 18441.004065621,
        "N_eff_range_in_block": [
          1.822403373860729,
          1.8519047087280396
        ],
        "N_eff": 1.8376845370385906,
        "alpha": 1.1843582338670333,
        "rms_cdf_distance_to_limit": 0.008222458978138657,
        "rms_cdf_distance_to_cue_corrected": 0.007625638964503785,
        "ratio_cue_over_limit": 0.9274158721592094,
        "sampling_noise_rms_gue_ensemble": 0.002914418889161613,
        "sup_cdf_distance_to_limit": 0.02369226591140154,
        "sup_cdf_distance_to_cue_corrected": 0.019967911416855166,
        "spacing_variance_measured": 0.1605282223062201,
        "spacing_variance_limit": 0.17999376244101595,
        "spacing_variance_cue_corrected": 0.14494115391000828,
        "domain_warning": "N_eff fora do domínio validado na fonte (7,7 e 11,3); O(N_eff^-4) não desprezível."
      }
    },
    "b05": {
      "indices": [
        22001,
        25000
      ],
      "gamma_range": [
        19617.381963594,
        21942.592430134
      ],
      "n_levels": 3000,
      "spacing_mean_before_renormalization": 0.999931705169786,
      "spacing_variance": 0.1597202578373907,
      "spacing_skewness": 0.48644626406433267,
      "spacing_kurtosis": 0.1181203419966379,
      "ks_distance_wigner_surmise": 0.02931864507675236,
      "wasserstein_wigner_surmise": 0.019602702498383095,
      "ks_distance_poisson": 0.30094566771489917,
      "wasserstein_poisson": 0.42637777769060037,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 3.380373527761549e-07,
        "spacing_variance_theta": 0.15972025783354282,
        "max_abs_spacing_difference": 4.001776687800884e-11
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.0021605114036504927,
        "1-2": 0.0037087539522057565,
        "2-5": 0.0037788515573781937
      },
      "r2_fraction_bins_outside_gue_95_band": 0.08,
      "sff_fraction_tau_outside_gue_95_band": 0.24,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.00783375902595803,
            "distance_null_median": 0.0026182346599780155,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.05872128504596294,
            "distance_null_median": 0.05094725545885519,
            "p_value_mc": 0.092,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.5275396240425461,
            "distance_null_median": 0.2567256470408736,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.17121908029689556,
            0.18989027855857102
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.11706502218264338,
            "distance_null_median": 0.0037216896067522676,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.27450991055820306,
            "distance_null_median": 0.05742281509553753,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.662454863504728,
            "distance_null_median": 0.3124921805895283,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.9320000992363805,
            1.0679979660057741
          ]
        }
      },
      "cue_secondary": {
        "E_median": 20783.4379232215,
        "N_eff_range_in_block": [
          1.8519173434779672,
          1.877698146713199
        ],
        "N_eff": 1.8652067484588564,
        "alpha": 1.1816379208005339,
        "rms_cdf_distance_to_limit": 0.008708516514268617,
        "rms_cdf_distance_to_cue_corrected": 0.006756510495100214,
        "ratio_cue_over_limit": 0.7758509137612467,
        "sampling_noise_rms_gue_ensemble": 0.002925451842203559,
        "sup_cdf_distance_to_limit": 0.028178411348770804,
        "sup_cdf_distance_to_cue_corrected": 0.020361328107649346,
        "spacing_variance_measured": 0.1597202578373907,
        "spacing_variance_limit": 0.17999376244101595,
        "spacing_variance_cue_corrected": 0.14573277054703615,
        "domain_warning": "N_eff fora do domínio validado na fonte (7,7 e 11,3); O(N_eff^-4) não desprezível."
      }
    },
    "b06": {
      "indices": [
        25001,
        28000
      ],
      "gamma_range": [
        21942.661101298,
        24238.383657457
      ],
      "n_levels": 3000,
      "spacing_mean_before_renormalization": 1.000109177301114,
      "spacing_variance": 0.15947599930529233,
      "spacing_skewness": 0.47878434512569,
      "spacing_kurtosis": 0.10035387561523157,
      "ks_distance_wigner_surmise": 0.02273471508756919,
      "wasserstein_wigner_surmise": 0.01951912586260393,
      "ks_distance_poisson": 0.3024129014934581,
      "wasserstein_poisson": 0.42761208642410153,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 3.0221781344152987e-07,
        "spacing_variance_theta": 0.1594759993024124,
        "max_abs_spacing_difference": 3.637978807091713e-11
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.002383320187330096,
        "1-2": 0.003939039050925288,
        "2-5": 0.004273848383436761
      },
      "r2_fraction_bins_outside_gue_95_band": 0.12,
      "sff_fraction_tau_outside_gue_95_band": 0.29,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.0076908115839531875,
            "distance_null_median": 0.0026329018954631494,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.06149254418227209,
            "distance_null_median": 0.05097561814456089,
            "p_value_mc": 0.042,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.4972623151130084,
            "distance_null_median": 0.2558945656512855,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.170746888898776,
            0.18970803964221922
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.11713488844170634,
            "distance_null_median": 0.0037066291592048194,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.2750933446816229,
            "distance_null_median": 0.05730581595371561,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.6502128125499582,
            "distance_null_median": 0.3140676057827778,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.9295718785595073,
            1.0717444578472157
          ]
        }
      },
      "cue_secondary": {
        "E_median": 23094.260640611,
        "N_eff_range_in_block": [
          1.877698867009995,
          1.9006006588279374
        ],
        "N_eff": 1.8894717586778715,
        "alpha": 1.179305286833319,
        "rms_cdf_distance_to_limit": 0.008499984550887851,
        "rms_cdf_distance_to_cue_corrected": 0.006816726742088855,
        "ratio_cue_over_limit": 0.8019693096238423,
        "sampling_noise_rms_gue_ensemble": 0.002945463670421025,
        "sup_cdf_distance_to_limit": 0.021982280666862142,
        "sup_cdf_distance_to_cue_corrected": 0.021245389491982625,
        "spacing_variance_measured": 0.15947599930529233,
        "spacing_variance_limit": 0.17999376244101595,
        "spacing_variance_cue_corrected": 0.1464084740247844,
        "domain_warning": "N_eff fora do domínio validado na fonte (7,7 e 11,3); O(N_eff^-4) não desprezível."
      }
    },
    "b07": {
      "indices": [
        28001,
        31000
      ],
      "gamma_range": [
        24239.881615681,
        26508.693400476
      ],
      "n_levels": 3000,
      "spacing_mean_before_renormalization": 0.9997510848262258,
      "spacing_variance": 0.16241869301023099,
      "spacing_skewness": 0.4657529000276968,
      "spacing_kurtosis": 0.1941031330063181,
      "ks_distance_wigner_surmise": 0.027239139441125604,
      "wasserstein_wigner_surmise": 0.019253005741912257,
      "ks_distance_poisson": 0.29914097947317503,
      "wasserstein_poisson": 0.42375360974135007,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 2.735760062932968e-07,
        "spacing_variance_theta": 0.16241869300764727,
        "max_abs_spacing_difference": 3.2741809263825417e-11
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.005051176826290115,
        "1-2": 0.004644683152743116,
        "2-5": 0.003071473722847349
      },
      "r2_fraction_bins_outside_gue_95_band": 0.14,
      "sff_fraction_tau_outside_gue_95_band": 0.3,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.007692482255056371,
            "distance_null_median": 0.002613139926848031,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.061123963281444045,
            "distance_null_median": 0.050811207006002154,
            "p_value_mc": 0.044,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.3359151682846412,
            "distance_null_median": 0.25764003462012436,
            "p_value_mc": 0.003,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.17077590712848467,
            0.1897815426344945
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.11653287613534237,
            "distance_null_median": 0.0037019660058011275,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.2735425220852806,
            "distance_null_median": 0.05743876539164507,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.5691505370326154,
            "distance_null_median": 0.3136228200067761,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.9245061630774741,
            1.0760309238785595
          ]
        }
      },
      "cue_secondary": {
        "E_median": 25377.392509243502,
        "N_eff_range_in_block": [
          1.9006148823881845,
          1.9212078955177427
        ],
        "N_eff": 1.9111697904018963,
        "alpha": 1.17726958502308,
        "rms_cdf_distance_to_limit": 0.008637156998983259,
        "rms_cdf_distance_to_cue_corrected": 0.006700795710483795,
        "ratio_cue_over_limit": 0.7758103402858826,
        "sampling_noise_rms_gue_ensemble": 0.0029064959958502966,
        "sup_cdf_distance_to_limit": 0.027119756844204368,
        "sup_cdf_distance_to_cue_corrected": 0.015966731130321765,
        "spacing_variance_measured": 0.16241869301023099,
        "spacing_variance_limit": 0.17999376244101595,
        "spacing_variance_cue_corrected": 0.1469965342340609,
        "domain_warning": "N_eff fora do domínio validado na fonte (7,7 e 11,3); O(N_eff^-4) não desprezível."
      }
    },
    "b08": {
      "indices": [
        31001,
        34000
      ],
      "gamma_range": [
        26509.94995712,
        28755.618891189
      ],
      "n_levels": 3000,
      "spacing_mean_before_renormalization": 0.9997218477408123,
      "spacing_variance": 0.16055425141640176,
      "spacing_skewness": 0.4846175610281327,
      "spacing_kurtosis": 0.15580771956963613,
      "ks_distance_wigner_surmise": 0.021900982227817167,
      "wasserstein_wigner_surmise": 0.020021877815626067,
      "ks_distance_poisson": 0.2993330598620789,
      "wasserstein_poisson": 0.42518718736699174,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 2.501510607544333e-07,
        "spacing_variance_theta": 0.16055425141421822,
        "max_abs_spacing_difference": 3.637978807091713e-11
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.002696882650838509,
        "1-2": 0.0028124336814717215,
        "2-5": 0.003925597950412197
      },
      "r2_fraction_bins_outside_gue_95_band": 0.16,
      "sff_fraction_tau_outside_gue_95_band": 0.28,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.007591081261787449,
            "distance_null_median": 0.002602613210885661,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.05907132275437905,
            "distance_null_median": 0.05062417202119478,
            "p_value_mc": 0.075,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.40301755897225205,
            "distance_null_median": 0.2563154477606251,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.17081370973797477,
            0.1899944828210558
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.11676084768957158,
            "distance_null_median": 0.003728732959055749,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.2732388059941447,
            "distance_null_median": 0.05753062938804225,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.6021140105685848,
            "distance_null_median": 0.3149081948382483,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.9295359643220285,
            1.0740097533983708
          ]
        }
      },
      "cue_secondary": {
        "E_median": 27635.2618050655,
        "N_eff_range_in_block": [
          1.921218805125738,
          1.9399336387025805
        ],
        "N_eff": 1.9307870231394513,
        "alpha": 1.1754684859556992,
        "rms_cdf_distance_to_limit": 0.008485374396702959,
        "rms_cdf_distance_to_cue_corrected": 0.006179821322097472,
        "ratio_cue_over_limit": 0.7282909431195725,
        "sampling_noise_rms_gue_ensemble": 0.0029148397245410533,
        "sup_cdf_distance_to_limit": 0.021176077237400337,
        "sup_cdf_distance_to_cue_corrected": 0.01560159817892931,
        "spacing_variance_measured": 0.16055425141640176,
        "spacing_variance_limit": 0.17999376244101595,
        "spacing_variance_cue_corrected": 0.14751453908699785,
        "domain_warning": "N_eff fora do domínio validado na fonte (7,7 e 11,3); O(N_eff^-4) não desprezível."
      }
    },
    "b09": {
      "indices": [
        34001,
        37000
      ],
      "gamma_range": [
        28757.060109636,
        30982.39614278
      ],
      "n_levels": 3000,
      "spacing_mean_before_renormalization": 0.9998682726601407,
      "spacing_variance": 0.15958136216123095,
      "spacing_skewness": 0.49103379217800686,
      "spacing_kurtosis": 0.12660998972803839,
      "ks_distance_wigner_surmise": 0.022993148869756064,
      "wasserstein_wigner_surmise": 0.019261360448373826,
      "ks_distance_poisson": 0.30449236927313766,
      "wasserstein_poisson": 0.42553665647602135,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 2.306042006239295e-07,
        "spacing_variance_theta": 0.1595813621593601,
        "max_abs_spacing_difference": 3.637978807091713e-11
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.004760848732337018,
        "1-2": 0.0031237379599356034,
        "2-5": 0.002650428035090432
      },
      "r2_fraction_bins_outside_gue_95_band": 0.14,
      "sff_fraction_tau_outside_gue_95_band": 0.24,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.007208434347238598,
            "distance_null_median": 0.0026068230549112655,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.05608519931518036,
            "distance_null_median": 0.05053383097042789,
            "p_value_mc": 0.177,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.5354569248504504,
            "distance_null_median": 0.25722427090607014,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.17053910350667414,
            0.18976043556318753
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.11686283070802303,
            "distance_null_median": 0.0037031941619727437,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.27314196160868875,
            "distance_null_median": 0.05744318008298113,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.6824832429553002,
            "distance_null_median": 0.3140161069393199,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.9301814811674005,
            1.0710614861006962
          ]
        }
      },
      "cue_secondary": {
        "E_median": 29872.0730523465,
        "N_eff_range_in_block": [
          1.939945173816823,
          1.9571001855368688
        ],
        "N_eff": 1.948700543511532,
        "alpha": 1.1738554837382515,
        "rms_cdf_distance_to_limit": 0.008041793416147837,
        "rms_cdf_distance_to_cue_corrected": 0.006596074596246455,
        "ratio_cue_over_limit": 0.8202243274493481,
        "sampling_noise_rms_gue_ensemble": 0.0029186520936505833,
        "sup_cdf_distance_to_limit": 0.022358487985426223,
        "sup_cdf_distance_to_cue_corrected": 0.020577368178153144,
        "spacing_variance_measured": 0.15958136216123095,
        "spacing_variance_limit": 0.17999376244101595,
        "spacing_variance_cue_corrected": 0.14797742907342037,
        "domain_warning": "N_eff fora do domínio validado na fonte (7,7 e 11,3); O(N_eff^-4) não desprezível."
      }
    },
    "b10": {
      "indices": [
        37001,
        40000
      ],
      "gamma_range": [
        30983.18800561,
        33190.012145055
      ],
      "n_levels": 3000,
      "spacing_mean_before_renormalization": 0.9999392666731828,
      "spacing_variance": 0.161563204591243,
      "spacing_skewness": 0.4690029002485513,
      "spacing_kurtosis": 0.11985802919118305,
      "ks_distance_wigner_surmise": 0.023108343852897534,
      "wasserstein_wigner_surmise": 0.017648127391511857,
      "ks_distance_poisson": 0.2966563228788637,
      "wasserstein_poisson": 0.4259482000164604,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 2.1402956917881966e-07,
        "spacing_variance_theta": 0.1615632045895079,
        "max_abs_spacing_difference": 4.3655745685100555e-11
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.0027784204093664836,
        "1-2": 0.0022069222073929436,
        "2-5": 0.003998640532028401
      },
      "r2_fraction_bins_outside_gue_95_band": 0.12,
      "sff_fraction_tau_outside_gue_95_band": 0.25,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.007048732774816941,
            "distance_null_median": 0.002595947545598408,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.05820594068993417,
            "distance_null_median": 0.0505906672217521,
            "p_value_mc": 0.106,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.5714343492627572,
            "distance_null_median": 0.25671062212118184,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.1702992483478837,
            0.18950111409627104
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.11637428249902979,
            "distance_null_median": 0.0037439954593520815,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "r2": {
            "distance_obs": 0.27167367930803527,
            "distance_null_median": 0.057274427622093484,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "k_connected": {
            "distance_obs": 0.6939804152500433,
            "distance_null_median": 0.31406759869346096,
            "p_value_mc": 0.001,
            "B": 999,
            "method": "posto simétrico leave-one-out sobre observação + nulos"
          },
          "spacing_var_ensemble_q025_q975": [
            0.9324047873881073,
            1.070993208739156
          ]
        }
      },
      "cue_secondary": {
        "E_median": 32088.5835218135,
        "N_eff_range_in_block": [
          1.957106067944214,
          1.9729419040146876
        ],
        "N_eff": 1.965174382599042,
        "alpha": 1.1723980724830747,
        "rms_cdf_distance_to_limit": 0.0078117958105381555,
        "rms_cdf_distance_to_cue_corrected": 0.005961630065803526,
        "ratio_cue_over_limit": 0.7631574365731953,
        "sampling_noise_rms_gue_ensemble": 0.002913704246374178,
        "sup_cdf_distance_to_limit": 0.02351018860785717,
        "sup_cdf_distance_to_cue_corrected": 0.017260087623296172,
        "spacing_variance_measured": 0.161563204591243,
        "spacing_variance_limit": 0.17999376244101595,
        "spacing_variance_cue_corrected": 0.14839442536258662,
        "domain_warning": "N_eff fora do domínio validado na fonte (7,7 e 11,3); O(N_eff^-4) não desprezível."
      }
    }
  },
  "cue_secondary_domain": {
    "reference": "Bogomolny, Bohigas, Leboeuf & Monastra (2006), eqs. 18-24",
    "richardson_change_pdf_max": 0.0004068597311288613,
    "expansion_error_by_N": [
      {
        "N": 2,
        "sup_abs_error_pdf_truncated": 0.06364207354358943,
        "sup_abs_error_cdf_truncated": 0.015238792152018066,
        "sup_abs_correction_cdf": 0.035958075467978766,
        "sup_abs_error_pdf_limit_only": 0.16505548860983277
      },
      {
        "N": 3,
        "sup_abs_error_pdf_truncated": 0.00808462887949124,
        "sup_abs_error_cdf_truncated": 0.002243026858985475,
        "sup_abs_correction_cdf": 0.01598136687465723,
        "sup_abs_error_pdf_limit_only": 0.05863628149433553
      },
      {
        "N": 4,
        "sup_abs_error_pdf_truncated": 0.0023674586369302197,
        "sup_abs_error_cdf_truncated": 0.0006514880345617202,
        "sup_abs_correction_cdf": 0.008989518866994691,
        "sup_abs_error_pdf_limit_only": 0.03098418686984372
      },
      {
        "N": 6,
        "sup_abs_error_pdf_truncated": 0.00044422121936416037,
        "sup_abs_error_cdf_truncated": 0.00012153472069076354,
        "sup_abs_correction_cdf": 0.003995341718664307,
        "sup_abs_error_pdf_limit_only": 0.013205729068136773
      },
      {
        "N": 8,
        "sup_abs_error_pdf_truncated": 0.00013814956480229235,
        "sup_abs_error_cdf_truncated": 3.771938387686635e-05,
        "sup_abs_correction_cdf": 0.002247379716748673,
        "sup_abs_error_pdf_limit_only": 0.007323671475112814
      },
      {
        "N": 12,
        "sup_abs_error_pdf_truncated": 2.6963377047883874e-05,
        "sup_abs_error_cdf_truncated": 7.350497515989929e-06,
        "sup_abs_correction_cdf": 0.0009988354296660768,
        "sup_abs_error_pdf_limit_only": 0.0032226469597629315
      },
      {
        "N": 16,
        "sup_abs_error_pdf_truncated": 8.497529165873985e-06,
        "sup_abs_error_cdf_truncated": 2.31491142921314e-06,
        "sup_abs_correction_cdf": 0.0005618449291871682,
        "sup_abs_error_pdf_limit_only": 0.001806469755033513
      }
    ],
    "validated_in_source_at_N_eff": [
      7.74,
      11.3
    ],
    "note": "Análise secundária; não altera decisões. Para N_eff ~ 2 o termo O(N^-4) é comparável à correção."
  },
  "family_holm": {
    "gue_cdf": {
      "b01": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b02": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b03": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b04": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b05": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b06": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b07": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b08": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b09": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b10": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "n_rejected": 10,
      "min_attainable_p_holm": 0.01
    },
    "gue_r2": {
      "b01": {
        "p": 0.465,
        "p_holm": 0.708,
        "verdict": "não rejeitado"
      },
      "b02": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b03": {
        "p": 0.27,
        "p_holm": 0.708,
        "verdict": "não rejeitado"
      },
      "b04": {
        "p": 0.23,
        "p_holm": 0.708,
        "verdict": "não rejeitado"
      },
      "b05": {
        "p": 0.092,
        "p_holm": 0.552,
        "verdict": "não rejeitado"
      },
      "b06": {
        "p": 0.042,
        "p_holm": 0.378,
        "verdict": "não rejeitado"
      },
      "b07": {
        "p": 0.044,
        "p_holm": 0.378,
        "verdict": "não rejeitado"
      },
      "b08": {
        "p": 0.075,
        "p_holm": 0.525,
        "verdict": "não rejeitado"
      },
      "b09": {
        "p": 0.177,
        "p_holm": 0.708,
        "verdict": "não rejeitado"
      },
      "b10": {
        "p": 0.106,
        "p_holm": 0.552,
        "verdict": "não rejeitado"
      },
      "n_rejected": 1,
      "min_attainable_p_holm": 0.01
    },
    "gue_k_connected": {
      "b01": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b02": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b03": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b04": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b05": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b06": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b07": {
        "p": 0.003,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b08": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b09": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b10": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "n_rejected": 10,
      "min_attainable_p_holm": 0.01
    },
    "poisson_cdf": {
      "b01": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b02": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b03": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b04": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b05": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b06": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b07": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b08": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b09": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b10": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "n_rejected": 10,
      "min_attainable_p_holm": 0.01
    },
    "poisson_r2": {
      "b01": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b02": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b03": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b04": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b05": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b06": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b07": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b08": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b09": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b10": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "n_rejected": 10,
      "min_attainable_p_holm": 0.01
    },
    "poisson_k_connected": {
      "b01": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b02": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b03": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b04": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b05": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b06": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b07": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b08": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b09": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "b10": {
        "p": 0.001,
        "p_holm": 0.01,
        "verdict": "rejeitado"
      },
      "n_rejected": 10,
      "min_attainable_p_holm": 0.01
    }
  },
  "settings": {
    "B_gue": 999,
    "B_poisson": 999,
    "gue_retained_fraction": 0.6,
    "sff_blocks": 10,
    "s_bins": 50,
    "s_max": 5.0
  },
  "performance": {
    "duration_seconds": 4238.680998266998,
    "peak_memory_mb": 218.234375,
    "peak_memory_largest_child_mb": 99.70703125,
    "memory_note": "RSS máximo do processo principal e do maior processo filho; o pico agregado dos processos simultâneos não é medido."
  }
}
```
