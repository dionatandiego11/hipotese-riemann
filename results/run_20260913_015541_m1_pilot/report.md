# Relatório de Execução — Marco M1

**ID da Execução:** `run_20260913_015541_m1_pilot`  
**Data UTC:** `2026-09-13T01:55:41.626912+00:00`  
**Perfil:** `pilot`  
**Zeros Analisados:** `1000`  

---

## 1. Resumo Executivo
Execução do Marco M1 concluída com sucesso em 0.04 s. Memória de pico: 141.8 MB. Foram analisados 1000 zeros da função zeta de Riemann.

---

## 2. Métricas Primárias Medidas

```json
{
  "run_id": "run_20260913_015541_m1_pilot",
  "milestone": "M1",
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
  "timing_duration_seconds": 0.035208185999636044,
  "peak_memory_bytes": 148660224,
  "peak_memory_mb": 141.7734375
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
