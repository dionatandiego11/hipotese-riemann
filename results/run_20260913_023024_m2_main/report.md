# Relatório de execução — M2

**ID:** `run_20260913_023024_m2_main`
**Data UTC:** `2026-09-13T02:38:25.358438+00:00`
**Perfil:** `main`
**Zeros analisados:** `10000`

## Resumo

Execução M2 com 10000 zeros em 481.0 s (pico de memória 200 MB).

## Afirmações sustentadas por esta execução

- B: hashes de dados conferem com o manifesto; 10000 ordenadas finitas e estritamente crescentes; amostra de 20 índices recalculada com mpmath (máx. |erro| = 2.50e-09).
- B: controles verificados — permutar a ordem dos níveis altera R2 em 0.0e+00 e K_c em 0.0e+00; inversão de Nbar com erro 3.6e-12; GUE denso e tridiagonal (N=400, 30 matrizes) com variâncias de espaçamento 0.1803 e 0.1774 e distância sup entre CDFs 0.008.
- B/pilot (zeros 1–1000): média de espaçamento 1.0000 e variância 0.1445 antes de renormalização (envelope GUE 95% da variância 0.1639–0.1965); p do envelope GUE (CDF, R2, K_c) = 0.010, 0.900, 0.010; p do envelope Poisson (CDF) = 0.010 (B=99/99).
- B/dev (zeros 1001–4000): média de espaçamento 1.0001 e variância 0.1530 antes de renormalização (envelope GUE 95% da variância 0.1701–0.1895); p do envelope GUE (CDF, R2, K_c) = 0.010, 0.410, 0.010; p do envelope Poisson (CDF) = 0.010 (B=99/99).
- B/val (zeros 4001–7000): média de espaçamento 0.9998 e variância 0.1560 antes de renormalização (envelope GUE 95% da variância 0.1686–0.1883); p do envelope GUE (CDF, R2, K_c) = 0.010, 0.170, 0.010; p do envelope Poisson (CDF) = 0.010 (B=99/99).
- B/holdout (zeros 7001–10000): média de espaçamento 1.0000 e variância 0.1569 antes de renormalização (envelope GUE 95% da variância 0.1696–0.1891); p do envelope GUE (CDF, R2, K_c) = 0.010, 0.130, 0.010; p do envelope Poisson (CDF) = 0.010 (B=99/99).
- B/full (zeros 1–10000): média de espaçamento 1.0000 e variância 0.1542 antes de renormalização (envelope GUE 95% da variância 0.1751–0.1846); p do envelope GUE (CDF, R2, K_c) = 0.010, 0.040, 0.010; p do envelope Poisson (CDF) = 0.010 (B=99/99).

## Limitações

- A validação por amostra não certifica completude da tabela nem localização rigorosa de todos os zeros.
- Blocos contíguos de um espectro determinístico não são amostras independentes.
- Envelopes GUE usam uma matriz por realização (níveis centrais), sem concatenação de matrizes.
- Valores-p do envelope medem incompatibilidade com o ensemble finito do mesmo tamanho, não com o limite assintótico.

## Métricas

```json
{
  "data": {
    "raw_sha256_matches_manifest": true,
    "processed_sha256_matches_manifest": true,
    "strictly_increasing": true,
    "all_finite": true,
    "mpmath_sample_size": 20,
    "mpmath_max_abs_error": 2.497472451068461e-09,
    "mpmath_all_within_tolerance": true
  },
  "unfolding_inverse_max_abs_error": 3.637978807091713e-12,
  "permutation_invariance": {
    "r2_max_abs_diff": 0.0,
    "sff_max_abs_diff": 0.0
  },
  "control_poisson": {
    "fixed_count": {
      "n": 20000,
      "density": 1.0000912399744535,
      "spacing_var": 1.0014987943341276
    },
    "random_count": {
      "n": 20063,
      "density": 1.00315,
      "spacing_var": 0.9918271104690419
    },
    "convention": "comparações com zeros usam contagem fixa (mesmo n que o bloco)"
  },
  "control_gue_dense_vs_tridiagonal": {
    "matrix_dim": 400,
    "realizations": 30,
    "bulk_interval": "[-0.5, 0.5] do semicírculo",
    "dense_mean": 0.998403039868035,
    "dense_var": 0.18025712351673115,
    "tridiagonal_mean": 0.9988337832020802,
    "tridiagonal_var": 0.1774342894829203,
    "cdf_sup_distance": 0.008451893289252665,
    "n_spacings_each": 7280
  },
  "blocks": {
    "pilot": {
      "indices": [
        1,
        1000
      ],
      "gamma_range": [
        14.134725142,
        1419.422480946
      ],
      "n_levels": 1000,
      "spacing_mean_before_renormalization": 0.9999684946254795,
      "spacing_variance": 0.14449714345674547,
      "spacing_skewness": 0.46669911749137505,
      "spacing_kurtosis": -0.10472601372172363,
      "ks_distance_wigner_surmise": 0.04224553234051044,
      "wasserstein_wigner_surmise": 0.03436134922774014,
      "ks_distance_poisson": 0.3214233457170086,
      "wasserstein_poisson": 0.43513802170355065,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 0.00046929778798210364,
        "spacing_variance_theta": 0.14449705969906565,
        "max_abs_spacing_difference": 0.0001538035713353203
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.015617177755012654,
        "1-2": 0.012409513527349793,
        "2-5": 0.01394739744122155
      },
      "r2_fraction_bins_outside_gue_95_band": 0.05,
      "sff_fraction_tau_outside_gue_95_band": 0.13,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.012665513465217135,
            "distance_null_median": 0.004673487703823815,
            "p_value_mc": 0.01,
            "B": 99
          },
          "r2": {
            "distance_obs": 0.11914810501905432,
            "distance_null_median": 0.13128070434666017,
            "p_value_mc": 0.9,
            "B": 99
          },
          "k_connected": {
            "distance_obs": 0.35027474437382056,
            "distance_null_median": 0.25394444513409187,
            "p_value_mc": 0.01,
            "B": 99
          },
          "spacing_var_ensemble_q025_q975": [
            0.1638587572971714,
            0.19653301004410614
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.1216495689285366,
            "distance_null_median": 0.0063931542260161536,
            "p_value_mc": 0.01,
            "B": 99
          },
          "r2": {
            "distance_obs": 0.2997859381696756,
            "distance_null_median": 0.1429025185526205,
            "p_value_mc": 0.01,
            "B": 99
          },
          "k_connected": {
            "distance_obs": 0.5523059886854516,
            "distance_null_median": 0.30399305068118304,
            "p_value_mc": 0.01,
            "B": 99
          },
          "spacing_var_ensemble_q025_q975": [
            0.9110695274612352,
            1.1107921195045498
          ]
        }
      }
    },
    "dev": {
      "indices": [
        1001,
        4000
      ],
      "gamma_range": [
        1420.416526324,
        4506.311496729
      ],
      "n_levels": 3000,
      "spacing_mean_before_renormalization": 1.0000852162492493,
      "spacing_variance": 0.153024256609011,
      "spacing_skewness": 0.5010430285330244,
      "spacing_kurtosis": 0.08966749446995026,
      "ks_distance_wigner_surmise": 0.030837235754562764,
      "wasserstein_wigner_surmise": 0.02659830198765937,
      "ks_distance_poisson": 0.3056303441837558,
      "wasserstein_poisson": 0.43103665136917324,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 4.668670158025634e-06,
        "spacing_variance_theta": 0.15302425628549168,
        "max_abs_spacing_difference": 7.469452611985616e-09
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.006202862391915037,
        "1-2": 0.00522892068392837,
        "2-5": 0.006291134075271908
      },
      "r2_fraction_bins_outside_gue_95_band": 0.09,
      "sff_fraction_tau_outside_gue_95_band": 0.18,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.010015384385640655,
            "distance_null_median": 0.0025751028318481252,
            "p_value_mc": 0.01,
            "B": 99
          },
          "r2": {
            "distance_obs": 0.07611475798760316,
            "distance_null_median": 0.07510514424180159,
            "p_value_mc": 0.41,
            "B": 99
          },
          "k_connected": {
            "distance_obs": 0.5551467928856195,
            "distance_null_median": 0.25486442977561524,
            "p_value_mc": 0.01,
            "B": 99
          },
          "spacing_var_ensemble_q025_q975": [
            0.17007638278407777,
            0.18946339444729018
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.11896906152929869,
            "distance_null_median": 0.003726267373208659,
            "p_value_mc": 0.01,
            "B": 99
          },
          "r2": {
            "distance_obs": 0.28304132846518565,
            "distance_null_median": 0.08079114646593509,
            "p_value_mc": 0.01,
            "B": 99
          },
          "k_connected": {
            "distance_obs": 0.7026180584739214,
            "distance_null_median": 0.3129767247514112,
            "p_value_mc": 0.01,
            "B": 99
          },
          "spacing_var_ensemble_q025_q975": [
            0.9352216987775922,
            1.0719479267728904
          ]
        }
      }
    },
    "val": {
      "indices": [
        4001,
        7000
      ],
      "gamma_range": [
        4507.745182883,
        7264.74824809
      ],
      "n_levels": 3000,
      "spacing_mean_before_renormalization": 0.9997816024582927,
      "spacing_variance": 0.15595922045959465,
      "spacing_skewness": 0.4927288595254728,
      "spacing_kurtosis": 0.10238093935307857,
      "ks_distance_wigner_surmise": 0.030635658683582256,
      "wasserstein_wigner_surmise": 0.023615786323518757,
      "ks_distance_poisson": 0.31102288287701507,
      "wasserstein_poisson": 0.4293180965761887,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 1.4711249605170451e-06,
        "spacing_variance_theta": 0.15595922040160065,
        "max_abs_spacing_difference": 6.402842700481415e-10
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.0068704398323751635,
        "1-2": 0.005749848719719132,
        "2-5": 0.006234650494418912
      },
      "r2_fraction_bins_outside_gue_95_band": 0.12,
      "sff_fraction_tau_outside_gue_95_band": 0.25,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.009012817192080023,
            "distance_null_median": 0.0024486639143994834,
            "p_value_mc": 0.01,
            "B": 99
          },
          "r2": {
            "distance_obs": 0.08021522178624313,
            "distance_null_median": 0.07496714588532097,
            "p_value_mc": 0.17,
            "B": 99
          },
          "k_connected": {
            "distance_obs": 0.6996143930439491,
            "distance_null_median": 0.25540418334062565,
            "p_value_mc": 0.01,
            "B": 99
          },
          "spacing_var_ensemble_q025_q975": [
            0.16863593439219013,
            0.18829116885555502
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.11780289898515645,
            "distance_null_median": 0.0036016448860914023,
            "p_value_mc": 0.01,
            "B": 99
          },
          "r2": {
            "distance_obs": 0.28219933034352795,
            "distance_null_median": 0.08154205386010446,
            "p_value_mc": 0.01,
            "B": 99
          },
          "k_connected": {
            "distance_obs": 0.8059378577132039,
            "distance_null_median": 0.31351062706176935,
            "p_value_mc": 0.01,
            "B": 99
          },
          "spacing_var_ensemble_q025_q975": [
            0.9374044496545297,
            1.0661734554335895
          ]
        }
      }
    },
    "holdout": {
      "indices": [
        7001,
        10000
      ],
      "gamma_range": [
        7265.962856286,
        9877.782654004
      ],
      "n_levels": 3000,
      "spacing_mean_before_renormalization": 0.9999798286747086,
      "spacing_variance": 0.1568691002441484,
      "spacing_skewness": 0.495187235492297,
      "spacing_kurtosis": 0.10123584702447896,
      "ks_distance_wigner_surmise": 0.02417536106004506,
      "wasserstein_wigner_surmise": 0.021691665318721045,
      "ks_distance_poisson": 0.3048530267170649,
      "wasserstein_poisson": 0.42850327437764363,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 9.126742952503264e-07,
        "spacing_variance_theta": 0.15686910021887449,
        "max_abs_spacing_difference": 2.6193447411060333e-10
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.0036686880739494783,
        "1-2": 0.005615699561911573,
        "2-5": 0.008030126784038732
      },
      "r2_fraction_bins_outside_gue_95_band": 0.1,
      "sff_fraction_tau_outside_gue_95_band": 0.26,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.008140233359148662,
            "distance_null_median": 0.002653720459924088,
            "p_value_mc": 0.01,
            "B": 99
          },
          "r2": {
            "distance_obs": 0.08259507498618575,
            "distance_null_median": 0.07528228117095183,
            "p_value_mc": 0.13,
            "B": 99
          },
          "k_connected": {
            "distance_obs": 0.5370611404060053,
            "distance_null_median": 0.25857019830523903,
            "p_value_mc": 0.01,
            "B": 99
          },
          "spacing_var_ensemble_q025_q975": [
            0.16958302533849298,
            0.1891106339846081
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.11728394497858577,
            "distance_null_median": 0.0038918899922580266,
            "p_value_mc": 0.01,
            "B": 99
          },
          "r2": {
            "distance_obs": 0.280708049443937,
            "distance_null_median": 0.08169733371747274,
            "p_value_mc": 0.01,
            "B": 99
          },
          "k_connected": {
            "distance_obs": 0.6971935764451056,
            "distance_null_median": 0.3182161788155146,
            "p_value_mc": 0.01,
            "B": 99
          },
          "spacing_var_ensemble_q025_q975": [
            0.931053842562318,
            1.0673515453118516
          ]
        }
      }
    },
    "full": {
      "indices": [
        1,
        10000
      ],
      "gamma_range": [
        14.134725142,
        9877.782654004
      ],
      "n_levels": 10000,
      "spacing_mean_before_renormalization": 1.000023001412775,
      "spacing_variance": 0.15415454008488474,
      "spacing_skewness": 0.49351621351882824,
      "spacing_kurtosis": 0.08288856809999912,
      "ks_distance_wigner_surmise": 0.027448655032917102,
      "wasserstein_wigner_surmise": 0.024881025593120366,
      "ks_distance_poisson": 0.3066845582517176,
      "wasserstein_poisson": 0.4301691904463508,
      "theta_vs_rvm_unfolding": {
        "max_abs_x_difference": 0.00046929778798210364,
        "spacing_variance_theta": 0.1541545316073269,
        "max_abs_spacing_difference": 0.0001538035713353203
      },
      "r2_band_mse_vs_montgomery": {
        "0-1": 0.003878959011139239,
        "1-2": 0.0019782781330999573,
        "2-5": 0.001824139251213198
      },
      "r2_fraction_bins_outside_gue_95_band": 0.14,
      "sff_fraction_tau_outside_gue_95_band": 0.16,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.009202544016983873,
            "distance_null_median": 0.0013593161768905566,
            "p_value_mc": 0.01,
            "B": 99
          },
          "r2": {
            "distance_obs": 0.04756916176696844,
            "distance_null_median": 0.04098826703917276,
            "p_value_mc": 0.04,
            "B": 99
          },
          "k_connected": {
            "distance_obs": 1.5146584203105817,
            "distance_null_median": 0.262728666580273,
            "p_value_mc": 0.01,
            "B": 99
          },
          "spacing_var_ensemble_q025_q975": [
            0.17511415838307404,
            0.184590211472687
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.11840462229334106,
            "distance_null_median": 0.0019704991994438014,
            "p_value_mc": 0.01,
            "B": 99
          },
          "r2": {
            "distance_obs": 0.27473435621866465,
            "distance_null_median": 0.0446628056086232,
            "p_value_mc": 0.01,
            "B": 99
          },
          "k_connected": {
            "distance_obs": 1.5717801530650202,
            "distance_null_median": 0.31003579633731787,
            "p_value_mc": 0.01,
            "B": 99
          },
          "spacing_var_ensemble_q025_q975": [
            0.9640823238840109,
            1.0453381478847035
          ]
        }
      }
    }
  },
  "settings": {
    "B_gue": 99,
    "B_poisson": 99,
    "gue_retained_fraction": 0.6,
    "sff_blocks": 10,
    "s_bins": 100,
    "s_max": 5.0
  },
  "performance": {
    "duration_seconds": 481.0300286669999,
    "peak_memory_mb": 200.47265625
  }
}
```
