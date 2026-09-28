# B23 — Pearce-Crump (2026), *Negative discrete second moments of Dirichlet L-functions*

**Referência.** A. Pearce-Crump, arXiv:2606.25094v1 (23/06/2026), preprint.
**Cópia local:** `archive/fontes_etapa11/momentos_negativos_20260927/pearce_crump_2026_arXiv_2606.25094.pdf` (25 pp.).
**Lido:** §1 inteiro (pp. 1–5), §6.2 e início do §8. Provas (§§2–5, 7) **não** lidas.

## O que o texto afirma

| item | conteúdo |
|---|---|
| Conj. 1 (Gonek) | sob RH e zeros simples: Σ_{0<γ≤T} 1/\|ζ′(ρ)\|² ∼ (3/π³) T |
| Teor. 2 (Milinovich–Ng) | a mesma soma ≥ (3/(2π³) − ε) T: metade do conjecturado |
| Conj. 3 (Ng) e Teor. 4 (Sinha) | Σ \|ζ(2ρ)/ζ′(ρ)\|² ∼ T/2π, com cota inferior da metade |
| **Teor. 5** | sob GRH e zeros simples, χ primitivo mod q, 3 ≤ q ≤ T^A: Σ 1/\|L′(ρ,χ)\|² ≥ (1−ε) (A_q/2π) β/(1+β) T, com β = log T/log qT e **A_q = (6/π²) ∏_{p\|q} p/(p+1)** (1.4) |
| Teor. 6 | análogo para Σ \|L(2ρ,χ²)/L′(ρ,χ)\|², com fator φ(q)/q |
| **Conj. 7** | **Σ_{0<γ≤T} 1/\|L′(ρ,χ)\|² ∼ (A_q/2π) T**, uniforme para q ≤ T^A |
| Conj. 8 | Σ \|L(2ρ,χ²)/L′(ρ,χ)\|² ∼ (φ(q)/q) T/2π |
| Conj. 9–10 (§8) | médias sobre a família de caracteres primitivos mod q |

## Proveniência das conjecturas (§6.2) — o ponto que importa

As conjecturas 7 e 8 vêm da **heurística do mollifier longo de Farmer** (limite u → ∞ na fórmula (6.1)). O autor escreve
que a heurística "não é uma prova" e foi aplicada a uma soma discreta sobre zeros, e não às médias contínuas para as
quais foi formulada. O único apoio externo citado é o caso q = 1, que coincide com Gonek e Ng. Ele deixa em aberto
derivá-las pela receita CFKRS ou pela conjectura das razões. **Não há nenhum teste numérico no artigo**
(busca por "numeric", "comput", "data", "Odlyzko": nada).

## Para o projeto

- Inclinações previstas: ζ, 3/π³ ≈ 0,0968; **χ₋₄ (q = 4): A₄/2π = 2/π³ ≈ 0,0645**; **χ₅ (q = 5): 5/(2π³) ≈ 0,0806**.
- O fator aritmético ∏_{p|q} p/(p+1) é a parte menos segura da conjectura, e é justamente o que nossos dados de χ₋₄
  e χ₅ podem discriminar: para χ₋₄, sem o fator a previsão seria 50% maior.
- Candidata a **norte**: teste numérico da Conjectura 7 (rótulo D → evidência B), com calibração em ζ.

*Leitura de 27/09/2026, Claude Opus.*
