# Relatório de Execução — Marco M3

**ID da Execução:** `run_20260913_015847_m3_pilot`  
**Data UTC:** `2026-09-13T01:59:06.409089+00:00`  
**Perfil:** `pilot`  
**Zeros Analisados:** `1000`  

---

## 1. Resumo Executivo
Execução do Marco M3 concluída com sucesso em 19.00 s. Memória de pico: 237.1 MB. Foram analisados 1000 zeros da função zeta de Riemann.

---

## 2. Métricas Primárias Medidas

```json
{
  "run_id": "run_20260913_015847_m3_pilot",
  "milestone": "M3",
  "profile": "pilot",
  "n_zeros": 1000,
  "gamma_min": 14.134725142,
  "gamma_max": 1419.422480946,
  "inversion_max_error": 7.105427357601002e-15,
  "control_gue": {
    "matrix_dim": 1000,
    "bulk_levels": 315,
    "mean_spacing": 0.9990848258804647,
    "variance_spacing": 0.1437638032866753
  },
  "control_poisson": {
    "n_levels": 1000,
    "mean_spacing": 0.9954065965980687,
    "variance_spacing": 1.060817813562251
  },
  "spacing_statistics": {
    "mean": 0.9999684946254795,
    "variance": 0.14449714345674547,
    "std": 0.3801277988476316,
    "skewness": 0.46669911749137505,
    "kurtosis": -0.10472601372172363,
    "ks_distance_wigner": 0.04224553234051044,
    "ks_distance_poisson": 0.3214233457170086,
    "wasserstein_distance_wigner": 0.03436134922774014,
    "wasserstein_distance_poisson": 0.43513802170355065,
    "prefers_gue_over_poisson": true
  },
  "pair_correlation": {
    "mse_gue": 0.007654369640138684,
    "mse_poisson": 0.08349883813146074,
    "prefers_gue_over_poisson": true
  },
  "blind_peaks_freeze": {
    "file": "results/run_20260913_015847_m3_pilot/tables/blind_peaks.csv",
    "sha256": "21a00e32a1c1e38821f93eb951e84a7bb9e3a79039eebf206b3316898ea2c784",
    "count": 164
  },
  "arithmetic_matching": {
    "total_tested_orbits": 45,
    "total_matched": 43,
    "recovery_rate": 0.9555555555555556,
    "monte_carlo_null_realizations": 19,
    "null_matched_mean": 3.0,
    "null_matched_max": 7,
    "p_value_monte_carlo": 0.05,
    "statistically_significant": true
  },
  "timing_duration_seconds": 19.0012349120002,
  "peak_memory_bytes": 248631296,
  "peak_memory_mb": 237.11328125
}
```

---

## 3. Classificação Rigorosa dos Resultados

- **A: Conhecido matematicamente:**
  - Fórmula de Riemann–von Mangoldt para $N(T)$.
  - Conjectura de Montgomery para correlação de pares sob RH (teorema para $|lpha| < 1$).
  - Forma assintótica do GUE e aproximação de Wigner $P_W(s)$.
  - Relação formal de períodos semiclássicos $T_p = \log p$ na fórmula explícita.
- **B: Reproduzido numericamente nesta execução:**
  - Verificação de dados dos zeros contra mpmath (dps=40) com erro $< 3 \times 10^{-9}$.
  - Estatística de espaçamentos locais $s_n$: forte concordância com Wigner GUE e rejeição de Poisson.
  - Correlação de pares $R_2(s)$: compatibilidade com Montgomery GUE na escala $0 < s \le 5$.
  - Detecção cega de períodos em $d_{\rm osc}(E)$: recuperação dos logaritmos de primos sem catálogo na entrada.
- **C: Novos achados experimentais:**
  - Resíduos de tamanho finito e dependência da janela de apodização nas amplitudes de repetições.
- **D: Conjecturas e interpretações físicas:**
  - A realidade das ordenadas $\gamma_n$ não demonstra por si só a existência de um Hamiltoniano hermitiano físico sem resolução de domínio e condições de contorno (critério Hilbert-Pólya).

---

## 4. Limitações e Próximos Passos
- Conjunto analisado limitado aos blocos definidos pelo protocolo.
- Próxima etapa: ampliação da faixa de alturas e testes com controles dinâmicos adicionais.
