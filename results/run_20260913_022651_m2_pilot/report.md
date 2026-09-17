# Relatório de execução — M2

**ID:** `run_20260913_022651_m2_pilot`
**Data UTC:** `2026-09-13T02:27:00.074243+00:00`
**Perfil:** `pilot`
**Zeros analisados:** `1000`

## Resumo

Execução M2 com 1000 zeros em 8.8 s (pico de memória 162 MB).

## Afirmações sustentadas por esta execução

- B: hashes de dados conferem com o manifesto; 1000 ordenadas finitas e estritamente crescentes; amostra de 20 índices recalculada com mpmath (máx. |erro| = 2.50e-09).
- B: controles verificados — permutar a ordem dos níveis altera R2 em 0.0e+00 e K_c em 0.0e+00; inversão de Nbar com erro 4.5e-13; GUE denso e tridiagonal (N=400, 30 matrizes) com variâncias de espaçamento 0.1003 e 0.1450 e distância sup entre CDFs 0.291.
- B/pilot (zeros 1–1000): média de espaçamento 1.0000 e variância 0.1445 antes de renormalização (envelope GUE 95% da variância 0.1317–0.1604); p do envelope GUE (CDF, R2, K_c) = 0.200, 0.300, 0.050; p do envelope Poisson (CDF) = 0.050 (B=19/19).

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
  "unfolding_inverse_max_abs_error": 4.547473508864641e-13,
  "permutation_invariance": {
    "r2_max_abs_diff": 0.0,
    "sff_max_abs_diff": 0.0
  },
  "control_poisson": {
    "fixed_count": {
      "n": 20000,
      "density": 1.0000362172834538,
      "spacing_var": 1.0145678452280524
    },
    "random_count": {
      "n": 20130,
      "density": 1.0065,
      "spacing_var": 0.9799895098157495
    },
    "convention": "comparações com zeros usam contagem fixa (mesmo n que o bloco)"
  },
  "control_gue_dense_vs_tridiagonal": {
    "matrix_dim": 400,
    "realizations": 30,
    "bulk_interval": "[-0.5, 0.5] do semicírculo",
    "dense_mean": 0.7430779995003343,
    "dense_var": 0.10027426851425182,
    "tridiagonal_mean": 0.9990198461835437,
    "tridiagonal_var": 0.1449661445611992,
    "cdf_sup_distance": 0.29054677994691336,
    "n_spacings_each": 7286
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
        "0-1": 0.012641492522972439,
        "1-2": 0.0061780466227606395,
        "2-5": 0.006506387038265778
      },
      "r2_fraction_bins_outside_gue_95_band": 0.12,
      "sff_fraction_tau_outside_gue_95_band": 0.28,
      "envelope_tests": {
        "gue": {
          "cdf": {
            "distance_obs": 0.006291828500346569,
            "distance_null_median": 0.004567655854114946,
            "p_value_mc": 0.2,
            "B": 19
          },
          "r2": {
            "distance_obs": 0.09656397067899214,
            "distance_null_median": 0.08747011608434475,
            "p_value_mc": 0.3,
            "B": 19
          },
          "k_connected": {
            "distance_obs": 0.5666148415933436,
            "distance_null_median": 0.42726157029539835,
            "p_value_mc": 0.05,
            "B": 19
          },
          "spacing_var_ensemble_q025_q975": [
            0.13170360710244458,
            0.1604231126480044
          ]
        },
        "poisson": {
          "cdf": {
            "distance_obs": 0.12235449389444455,
            "distance_null_median": 0.007242574179113112,
            "p_value_mc": 0.05,
            "B": 19
          },
          "r2": {
            "distance_obs": 0.2889852764719238,
            "distance_null_median": 0.09945529610524441,
            "p_value_mc": 0.05,
            "B": 19
          },
          "k_connected": {
            "distance_obs": 0.6871861744668764,
            "distance_null_median": 0.5216762323215052,
            "p_value_mc": 0.05,
            "B": 19
          },
          "spacing_var_ensemble_q025_q975": [
            0.9003912733835138,
            1.0899450216101578
          ]
        }
      }
    },
    "dev": {
      "status": "não executado: zeros insuficientes"
    },
    "val": {
      "status": "não executado: zeros insuficientes"
    },
    "holdout": {
      "status": "não executado: zeros insuficientes"
    },
    "full": {
      "status": "não executado: zeros insuficientes"
    }
  },
  "settings": {
    "B_gue": 19,
    "B_poisson": 19,
    "gue_retained_fraction": 0.6,
    "sff_blocks": 4,
    "s_bins": 50,
    "s_max": 5.0
  },
  "performance": {
    "duration_seconds": 8.770927946000484,
    "peak_memory_mb": 161.734375
  }
}
```
