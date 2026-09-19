# D1-M — derivação da previsão do `ctrl-maass-v1` a partir de Bolte & Grosche (19/09/2026)

Escrita **antes** do catálogo G1, de qualquer código do controle e de qualquer transformada dos autovalores de Maass.
SHA-256 em `D1M_DERIVACAO_MAASS.sha256`. Cumpre o item D1-M da §4 de [DECLARACAO_MAASS.md](DECLARACAO_MAASS.md)
(`5db97004…`). Onde contradiz P2 e P3 da declaração, **prevalece esta derivação**, e a correção é formalizada no
[ADENDO_MAASS_1.md](ADENDO_MAASS_1.md), antes de qualquer cálculo.

**Fontes lidas (imagem das páginas; registradas no manifesto e na §20 das pendências de fontes):**
- **[BG]** Bolte & Grosche, preprint DESY 92-118 (= CMP 163 (1994) 217–244), Theorem 2.2 [55], eq. (2.31), pp. 8–9;
- **[BS]** Bolte & Steiner, preprint DESY 90-082 (= CMP 156 (1993) 1–16), pp. 3–6, eq. (13) e a classificação das
  reflexões (p. 5).

## 1. Situação geométrica

- **Superfície dobrada:** Σ̂ = Γ̂\ℍ, com Γ̂ = PSL(2, ℤ) (domínio F̂ de área π/3).
- **Superfície com bordo:** Σ = Σ̂/I, com I(z) = −z̄, ou seja, o triângulo modular F de área π/6.
- **Autofunções de Dirichlet em F** = funções ímpares sob I = **formas de Maass ímpares** ([BS] p. 3; BLS p. 10).
- **Elementos de Γ̂I** (isometrias que invertem a orientação): z ↦ (αz̄ + β)/(γz̄ + δ), com matriz M = (α β; γ δ) ∈ GL(2, ℤ),
  **det M = −1**, módulo ±1 (BLS eq. (6.1)).
- **Classificação de ρ ∈ Γ̂I ([BS] p. 5):**
  - reflexões puras (ρ² = 1, tr ρ = 0);
  - ρ² fechando uma geodésica do bordo;
  - reflexões com deslizamento primitivas ρ_p.

  O bordo de F é formado por arcos geodésicos que vão a cantos e à cúspide, não por geodésicas fechadas. De fato, um
  elemento hiperbólico de PSL(2, ℤ) com pontos fixos {0, ∞}, {±1} ou {½, ∞} seria diagonal, simétrico ou parabólico,
  e todos esses são triviais ou parabólicos em SL(2, ℤ). **Logo a segunda classe é vazia** e os termos l(c_i) de [BG]
  não aparecem.

## 2. A fórmula ([BG] (2.31), Dirichlet, peso m = 0)

Com h par, analítica na faixa |Im p| ≤ ½ + ε e decaindo mais rápido que |p|⁻²; g(x) = ∫ h(p) e^{ipx} dp/2π; e
λ_n = ¼ + p_n²:

Σ_n h(p_n) = (A(F̂)/8π) ∫ p tanh(πp) h(p) dp
 + Σ_{{γ}_p} Σ_{k≥1} l_γ g(k l_γ) / (4 sinh(k l_γ/2))
 + Σ_{{R}_p} Σ_{k=1}^{ν−1} [8ν sin(kπ/ν)]⁻¹ ∫ h(p) cosh[π(1 − 2k/ν)p]/cosh(πp) dp
 − Σ_{{ρ}_p, tr ρ≠0} Σ_{k≥1} l_{ρ²} g[(k − ½) l_{ρ²}] / (4 cosh(½(k − ½) l_{ρ²}))
 − (κ/4π) ∫ h(p) Ψ(½ + ip) dp + (g(0)/2)[Σ_{tr ρ = 0} ln(a(ρ)/ν(ρ)) − κ ln 2].

"The summation on the right is taken over all primitive conjugacy classes {R}_p with tr(R) < 2, {γ}_p with |tr(γ)| > 2,
and {ρ}_p, tr(ρ) ≠ 0" ([BG] p. 9). As classes são **de conjugação por Γ̂** ([BS] p. 5: "{ρ}_Γ̂"). Aqui A(F̂) = π/3, há
κ = 1 cúspide e elementos elípticos de ordens ν = 2 e 3.

## 3. Conversão para o coeficiente do instrumento

Mesma conta da §2.2(b) de ETAPA11_3B_FORMULA_EXPLICITA e da D1 do Dirichlet:
- Tome h = k_t = f_t(p) + f_t(−p), com f_t suportada em p > 0. Então Σ_n h(p_n) = D_t, porque cada autovalor aparece uma
  vez, com p_n > 0; não há a divisão por 2 que existe para ζ.
- g_{k_t}(u) = G_t(u) + G_t(−u), com G_t(u) = (1/2π) e^{−iE_c u} W(t + u).
- Um termo A·g(l) do lado direito vira (A/2π)[e^{iE_c l}W(t − l) + e^{−iE_c l}W(t + l)], isto é, a linha do instrumento
  com **c = A/π** (convenção Re[C e^{iRT}] de `targeted_joint_fit`).

**Coeficientes por classe de Γ̂ = PSL(2, ℤ):**

| Classe | Comprimento da linha | Coeficiente c |
|---|---|---|
| **hiperbólica** γ = γ_p^k, com γ_p primitiva **em PSL(2, ℤ)**, \|tr γ_p\| = n ≥ 3 | l = k·l_p, com l_p = 2 arccosh(n/2) | **c = + l_p / (4π sinh(l/2))** |
| **reflexão com deslizamento** ρ = ρ_p^{2k−1}, com ρ_p primitiva, det = −1, \|tr ρ_p\| = n ≥ 1 | l = (2k − 1)·l_ρ, com l_ρ = ½ l(ρ_p²) = 2 arcsinh(n/2) | **c = − l_ρ / (2π cosh(l/2))** |

- **Conferência de l(ρ²) = 2 l_ρ:** se det M = −1 e tr M = n, então tr M² = n² + 2, e 2 cosh(l_ρ) = 2 + n² = 2 + 4
  sinh²(l_ρ/2). Numericamente, 2 arccosh(3/2) = 1,924847 = 2 × 2 arcsinh(½).
- **H_cosh vale** ([BG], [BS]): a amplitude das reflexões com deslizamento tem **cosh** no denominador, com sinal − para
  Dirichlet. A hipótese H_sinh da declaração fica **refutada por fonte**. A comparação descritiva M-C2a− continua, mas
  agora como previsão com fonte.
- **As potências pares** de ρ_p estão em Γ̂ e entram no primeiro somatório como classes hiperbólicas de PSL(2, ℤ). ρ_p²
  é **primitiva em Γ̂**, porque ρ_p ∉ Γ̂.

**Primeiros valores (a confirmar pela contagem G1):**
- δ = −1, n = 1: l = 0,962424. Se houver uma única classe (forma de discriminante 5), c = **−0,137003**. Sob H_sinh
  seria −0,306349.
- δ = −1, n = 2: l = 1,762747. Com uma única classe (discriminante 8), c = −0,198379.
- δ = +1, n = 3: l = 1,924847. Com uma classe de PSL(2, ℤ) (discriminante 5), c = +0,137003.

## 4. Termos que não são linhas

- **Área:** (π/3)/(8π)·∫ p tanh(πp) h dp. Com h = k_t, dá densidade p/12 para p > 0 e N ~ p²/24, que é o coeficiente
  fixo da §5 da declaração.
- **Elípticos (cantos):** densidade proporcional a cosh[π(1 − 2k/ν)p]/cosh(πp) ≤ 2e^{−2πkp/ν}. Para p ≥ 9,53 e ν ≤ 3,
  fica ≤ 2e^{−19,97} ≈ 4·10⁻⁹ **por unidade de p**, desprezível (ordem 10⁻¹⁰ da densidade média).
- **Parabólico (cúspide):** −(1/4π)·2 Re Ψ(½ + ip) ≈ −(1/2π) log p + O(p⁻²). É termo suave, absorvido pelo ajuste
  βR log R + γR + δ₀ da declaração.
- **Termos em g(0):** densidade constante, absorvida por γR.
- **Conclusão:** só as classes hiperbólicas e as reflexões com deslizamento produzem linhas em t > 0. Isso confirma a
  suposição de P1 da declaração, agora com fonte ([BG] (2.31)).

## 5. Contagem de classes (método para G1)

- Para M ∈ GL(2, ℤ), a forma Q_M(x, y) := det(v, Mv), com v = (x, y), vale c x² + (d − a)xy − b y². Ela tem
  discriminante (tr M)² − 4 det M, e (A, B, C) = (c, d − a, −b) é uma **bijeção** entre as matrizes com (tr, det)
  fixos e as formas desse discriminante (B ≡ tr M mod 2 é automático).
- Para P ∈ GL(2, ℤ): Q_{PMP⁻¹}(v) = det(P)·Q_M(P⁻¹v). Logo **conjugação por Γ̂ = SL(2, ℤ)/±1 corresponde a equivalência
  própria de formas**, sem a involução ι da declaração.
- **Classes hiperbólicas de PSL(2, ℤ) com |tr| = n ≥ 3:** classes próprias de **todas** as formas (primitivas ou não)
  de discriminante n² − 4.
- **Classes de Γ̂ das reflexões com deslizamento com |tr| = n ≥ 1:** classes próprias de todas as formas de
  discriminante n² + 4.
- M e −M dão a mesma isometria e traços opostos, então basta tr = n > 0.
- **Potências:** M^k = U_{k−1}M − (det M)U_{k−2}I, com U₀ = 1, U₁ = tr M e U_{j+1} = (tr M)U_j − (det M)U_{j−1}. Logo
  Q_{M^k} = U_{k−1}·Q_M. Uma classe é potência k-ésima de uma classe com (n₀, δ₀) se o conteúdo da forma for divisível
  por U_{k−1}(n₀, δ₀) e se Q/U_{k−1} tiver discriminante n₀² − 4δ₀. Para reflexões com deslizamento, só potências
  ímpares ficam em Γ̂I.

## 6. O que muda na declaração (e vai para o ADENDO_MAASS_1)

1. **P2:** trocar "classes de PGL(2, ℤ) com peso L_p/(2π S(l/2))" pelos coeficientes da §3, **por classe de Γ̂**, e
   declarar **H_cosh** como previsão, com fonte.
2. **P3:** trocar "formas de discriminante n² − 4δ identificadas por ι" por **classes próprias sem ι**, com
   discriminante n² − 4 para δ = +1 e n² + 4 para δ = −1. Continuam os dois algoritmos independentes e a gravação com
   hash antes de qualquer transformada.
3. **Critérios:** a amplitude das reflexões com deslizamento pode passar de descritiva para critério. O ADENDO decide,
   antes de qualquer cálculo, com a mesma forma de M-C2a+ (\|Re Ĉ − c\| ≤ 3σ_c em ≥ 90% das linhas elegíveis).
4. **Nada mais muda:** setor, faixa, blocos, densidade, nulos, semente e os outros critérios.
