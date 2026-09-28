# MN-3 — Conjecturas 7 e 8 em caracteres novos (χ₈, χ₁₂): ficha congelada antes do cálculo (27/09/2026)

**Estado:** congelada antes de calcular zeros, derivadas ou valores de L. Estende MN-1/MN-2 com caracteres escolhidos
para tentar **derrubar** as conjecturas. Autorizada pelo usuário com orçamento de ~10 h-CPU.

## 1. Caracteres e previsões (fixadas agora)

χ₈ = (8/·) e χ₁₂ = (12/·): reais, primitivos, pares. R = razão diferencial contra ζ (mesmo desenho da MN-1/MN-2).

| | C7: ∏ p/(p+1) | alternativas C7 | C8: φ(q)/q | alternativas C8 |
|---|---|---|---|---|
| **χ₈** | **2/3** (igual a q = 4) | H0 = 1; HE = 4/3 | **1/2** (igual a q = 4) | H0 = 1; H7 = 2/3 |
| **χ₁₂** | **1/2** | H0 = 1; HE = 3/2 | **1/3** | H0 = 1; H7 = 1/2 |

- **χ₁₂ é a primária:** condutor composto, com produto sobre dois primos.
- **χ₈ testa a estrutura:** as conjecturas preveem os mesmos fatores de q = 4, embora χ₈ seja par e χ₋₄ ímpar.

## 2. Dados

- **Zeros 1–2.000** de cada L(s,χ) pelo `dirichlet_zeros.run` congelado (`65056bc2…`), sem editar o arquivo: mesmo
  passo, refinamento e verificações V1–V4, com V2 reexaminando 1–2.000 com passo pela metade. Pelo benchmark, 60
  zeros de cada foram aprovados em V1–V4.
- **Redução de 3.000 para 2.000 zeros:** custo medido (0,06–0,47 s por avaliação, crescendo com a altura), para caber
  no orçamento.
- **Referência ζ estendida** para os zeros 1–27.000, retomando o checkpoint da MN-1, para cobrir as densidades
  log(12γ/2π) até ~8,15.
- **Se uma lista não for aprovada em V1–V4, as derivadas não são calculadas** (o script aborta). Um passe de
  completude D3 exigiria decisão nova. Não é automático.

## 3. Derivadas e L(2ρ,χ²)

Como na MN-1/MN-2: |L′| por diferença central (h = 10⁻⁶, dps 20); L(2ρ,χ²) = ζ(1+2iγ)∏_{p|q}(1−p^{−1−2iγ}) (χ² é o
caractere principal).

## 4. Código

`results/momentos_negativos_20260927/mn3_caracteres.py`, `mn3_zeros.py`, `mn3_derivadas.py` e `analise_mn3.py`;
`calc_derivadas.py` e `calc_zeta2rho.py` (MN-1/MN-2, sem alteração) para estender ζ; `discrete_moments.py` sem
alteração. Semente do bootstrap: 20260929.

## 5. Critérios (para cada caractere e conjectura)

- **Favorecida:** previsto no IC 95% **e** H0 fora. **Contrariada:** previsto fora. **Inconclusivo:** o resto.
- Registrar as alternativas no IC.
- **Primária:** χ₁₂ nas duas conjecturas.
- **Descritivo:** comparação dos R de χ₈ com os de χ₋₄ (MN-1/MN-2); sobreposição dos ICs.

## 6. Teto de CPU

Zeros: 28.800 s por caractere (RLIMIT_CPU), em paralelo. Derivadas e L(2ρ): 3.600 s por caractere. Extensão de ζ:
3.600 s para derivadas e 1.800 s para L(2ρ). **Teto total: ~21 h nominais; custo esperado ~12 h.** Sem extensão
automática.

## 7. O que se pode concluir

Evidência numérica (B/C) a favor ou contra os fatores aritméticos em mais dois caracteres. **Não é prova**; nada
sobre GRH.

*Dionatan Resende & Claude Opus — 27/09/2026.*
