# MN-2 — teste numérico da Conjectura 8 de Pearce-Crump: ficha congelada antes do cálculo (27/09/2026)

**Estado:** congelada **antes** de calcular L(2ρ,χ²). Reaproveita as derivadas da MN-1 (já medidas, cujo resultado é
conhecido). A MN-1 mostrou o comportamento de 1/|L′|², mas não o do fator |L(2ρ,χ²)|²; o fator aritmético da
Conjectura 8 (φ(q)/q) difere do da Conjectura 7 e é o que se testa aqui.

## 1. Hipótese

Pearce-Crump (arXiv:2606.25094), Conjectura 8: Σ_{0<γ≤T} |L(2ρ,χ²)/L′(ρ,χ)|² ∼ (φ(q)/q) T/2π (q = 1: conjectura de Ng,
T/2π). Mesma heurística (mollifier longo) da Conjectura 7; sem teste numérico no artigo.

## 2. Estatística

w_n = log(qγ/2π)·|L(2ρ,χ²)|²/|L′(ρ,χ)|² (média → φ(q)/q; para ζ → 1). R₈ = média(w, χ)/E_ζ[w | densidades de χ], com o
mesmo teste diferencial da MN-1 (10 bins nos quantis, bootstrap de blocos de 100, 2.000 réplicas, semente 20260928).
Para χ real, χ² é o principal mod q: L(2ρ,χ²) = ζ(1+2iγ)∏_{p|q}(1 − p^{−1−2iγ}); mpmath, dps 15.

| hipótese | χ₋₄ | χ₅ |
|---|---|---|
| **C8** (φ(q)/q) | **1/2** | **4/5** |
| H0 (sem fator) | 1 | 1 |
| H7 (mesmo fator da Conj. 7) | 2/3 | 5/6 |

## 3. Dados e código

Os mesmos γ da MN-1 (ζ 1–20.000; χ₋₄ e χ₅ 1–3.000). Scripts `results/momentos_negativos_20260927/calc_zeta2rho.py`
e `analise_c8.py`; módulo `discrete_moments.py` sem alteração.

## 4. Critérios (fixados antes do cálculo)

- **Favorecida:** C8 no IC 95% **e** H0 fora. **Contrariada:** C8 fora do IC. **Inconclusivo:** C8 e H0 dentro.
- Registrar se H7 está no IC: para χ₋₄, C8 e H7 diferem (0,5 contra 0,667); para χ₅ são quase iguais (0,8 contra
  0,833), sem poder de separação. Primária: χ₋₄.
- Descritivo ζ: média de w contra 1 (Ng) nas faixas de altura.

## 5. Custo

~26 mil avaliações de ζ(1+2iγ) a ~70 ms, ~30 min de CPU. Tetos: ζ 3.600 s; χ 900 s cada.

*Dionatan Resende & Claude Opus — 27/09/2026.*
