# Etapa 11.3b — admissibilidade das funções-teste da fórmula explícita

**Data:** 14/09/2026. **Estado:** `em execução`.
- Nenhum cálculo numérico novo.
- F1–F7 continuam `bloqueado` por acesso; H1 (L-EF2c) continua aberta; H2 concluída para o cálculo local
  ([ETAPA11_3B_TERMO_ARQUIMEDIANO.md](ETAPA11_3B_TERMO_ARQUIMEDIANO.md)).

**Pergunta.** Para quais pares (g, h) a forma de referência (plano §3.1) vale, com cada termo bem definido e a soma
sobre zeros convergente, usando só as fontes arquivadas? E o que ainda depende de F5 e de outros fatos não conferidos?

**Fontes arquivadas:**
- Connes arXiv:math/9811068v1, Apêndice II:
  - p. 68, eq. (2);
  - p. 69–70, eqs. (4)–(11) e Teorema 1;
  - p. 70–71, eqs. (12)–(21);
  - p. 76–78, Lema 3, eq. (58) e Teorema 6;
  - p. 78, normalização de Haar.
- DLMF 25.2.12 (`dlmf_25.2.html`, versão 1.2.7).

---

## 1. O que Connes enuncia e o que fica implícito

| Enunciado | Classe declarada | Página |
|---|---|---|
| Teorema 1 (Weil) | F em N com F(ν) = O(ν^b) em 0 e O(ν^{−b}) em ∞, b > ½ | p. 68 eq. (2); p. 70 |
| Eq. (21) | "holds for finite linear combinations of functions h of the form (12)"; "This is enough to conclude when h(1) = 0" | p. 71 |
| Teorema 6 | "Let h ∈ 𝒮(C_k) have compact support", com ∫' normalizado pelos caracteres locais α_v (Teorema V.3) | p. 77–78 |

**Leitura.** A hipótese (2), sozinha, **não** garante que todos os termos façam sentido:
- Φ(ρ) é limitada na faixa. O decaimento assumido para F não garante, por si só, uma taxa de decaimento de Φ
  suficiente para somar absolutamente sobre os zeros. Ausência de uma taxa demonstrada não significa ausência de
  decaimento.
- Pfw no lugar arquimediano, eq. (11), exige ψ − c f₁⁻¹ integrável, isto é, regularidade de F em ν = 1.

Logo o Teorema 1, como transcrito, não fixa sozinho regularidade nem modo de convergência da soma sobre zeros. Por isso
a extensão (§2) parte do **Teorema 6**, que tem classe precisa. O enunciado original de Weil (F5) é pendência de
**conferência bibliográfica**, não hipótese matemática adicional da demonstração (§1a).

**O Teorema 6 tem classe precisa:** h ∈ 𝒮(C_k) de suporte compacto. Para a função radial ligada a g por
|u|^{−1/2}h(u^{−1}) = F(|u|), F(eˣ) = g(x) (eq. 12), com caractere trivial (eqs. 14–17), isso equivale a
**g ∈ C_c^∞(ℝ) par**. O compacto de C_ℚ (Ẑ*) não interfere.

**Equivalência entre ∫' e Pfw** (Lema 3, p. 76–77, com a eq. 58 e a prova do Teorema 6): ∫'_v = log|λ_v|·f(1) +
Pfw_v, e Σ_v log|d_v| = log|d| = 0 para ℚ (p. 69). O termo log|d⁻¹|δ₁ da eq. (5) desaparece, e o Teorema 6 coincide
com a forma do Teorema 1 com Pfw, usada nas derivações de §1.2, §3 e H2.

## 1a. Conferência do ponto de partida em Connes (revisão 11.3b-5)

**Conferido visualmente** nas páginas renderizadas do PDF arquivado:
- p. 70, eqs. (12)–(17) e Teorema 1;
- p. 71, eqs. (18)–(21);
- p. 76, eq. (54) e Lema 3;
- p. 77, eq. (58) e início do Teorema 6;
- p. 78, enunciado do Teorema 6 e normalização de Haar.

**Transcrição e aplicação, verificadas passo a passo:**
1. **Correspondência h ↔ F.** A eq. (12), |g|^{−1/2}h(g^{−1}) = F(|g|)X₀(g), dá h(u) = |u|^{−1/2}F(1/|u|) para h radial.
2. **Transformada.** ĥ(z) = ∫h(u)|u|^z d*u = ∫ν^{1/2−z}F(ν)d*ν = Φ(z), com ν = 1/|u|. Então ĥ(0) = Φ(0) = h_proj(i/2),
   ĥ(1) = h_proj(−i/2) e ĥ(X₀, ρ) = h_proj(γ_ρ), com F(eˣ) = g(x) (§2 de H2).
3. **Caracteres.** Para h radial (invariante por C_{ℚ,1}), ĥ(X, ρ) = 0 se X ≠ X₀ em C_{k,1} (eq. 14). A soma do Teorema 6
   sobre X reduz-se ao caractere trivial.
4. **Integrando local.** h(u^{−1})/|1−u| = |u|^{1/2}F(|u|)/|1−u|, que é o integrando da eq. (8) usado em §1.2, §3 e H2.
5. **∫' × Pfw.** Pelo Lema 3 (p. 76), ∫'_v = log|λ_v| f(1) + Pfw_v com α_v(x) = α_{0,v}(d_v x) (eq. 58). Somando,
   Σ_v log|d_v| = log|d| (prova do Teorema 6, p. 78), e o Teorema 6 equivale à eq. (21), que contém (log|d|)h(1).
   Para ℚ, |d|⁻¹ é o discriminante a menos de sinal (p. 69), logo log|d| = 0 e (21) coincide com a forma de referência.
6. **Classe.** h ∈ 𝒮(C_ℚ) de suporte compacto e radial equivale a F ∈ C_c^∞(ℝ*₊), isto é, g ∈ C_c^∞(ℝ) par. Constante
   na parte compacta Ẑ* é localmente constante, logo de Schwartz–Bruhat.

**Conclusão:** se o Teorema 6 e o Lema 3 estão corretamente enunciados em Connes, eles fornecem o ponto de partida
matemático da extensão para g ∈ C_c^∞ par. A consulta a Weil (F5) continua **exigência bibliográfica** do projeto.

## 2. Classe admissível 𝒜 e extensão a partir de C_c^∞

**Definição de 𝒜.** g: ℝ → ℂ par, de classe C^∞, com:
- **(A1)** e^{|x|/2}|g^{(j)}(x)| ∈ L¹(ℝ) para j = 0, 1, 2, 3, 4;
- **(A2)** |g(x)| ≤ C e^{−b|x|} para algum b > ½ (hipótese (2) de Connes);
- h(r) := ∫ g(x)e^{irx}dx, tomado como função contínua. Por (A1) com j = 0, h é holomorfa na faixa aberta |Im r| < ½
  e contínua no fecho |Im r| ≤ ½. Os zeros têm |Im γ_ρ| < ½; os polos são avaliados em ±i/2 na borda.

**Consequências de (A1):**
- |h(r)| ≤ ‖g^{(4)}‖₁/r⁴, logo ∫|h|(1 + r²) < ∞: vale (G1).
- g ∈ L¹: vale (G3), com h contínua, e a igualdade Φ(½ + iγ) = h(γ) é pontual.
- 𝒜 ⊂ 𝒢 (classe de H2).

**Aproximação.** Seja χ ∈ C_c^∞(ℝ) par, 0 ≤ χ ≤ 1, com χ = 1 em [−1, 1], e g_n(x) = g(x)χ(x/n), h_n a
transformada. Então g_n ∈ C_c^∞ é par, e o Teorema 6 (via Lema 3) dá a forma de referência para (g_n, h_n):

Σ_ρ h_n(γ_ρ) = h_n(i/2) + h_n(−i/2) − g_n(0) log π + T[g_n] − 2Σ_m Λ(m)m^{−1/2}g_n(log m),

com T[g_n] como em H2 §4. (g_n, h_n) ∈ 𝒢, de modo que o cálculo de H2 se aplica.

**Passagem ao limite, termo a termo:**

| Termo | Argumento (n → ∞) | Hipótese usada |
|---|---|---|
| Primos | \|g_n(log m)\| ≤ \|g(log m)\| ≤ C m^{−b}; Σ Λ(m)m^{−1/2−b} < ∞, porque Λ(m) ≤ log m e ½ + b > 1; convergência dominada | (A2) |
| Polos h_n(±i/2) = ∫g_n e^{∓x/2}dx | dominado por \|g\|e^{\|x\|/2} ∈ L¹ | (A1), j = 0 |
| g_n(0) log π | g_n(0) = g(0) para n ≥ 1 | — |
| T[g_n] = ∫₀^∞[g(0)e^{−2x}/x − ½g_nK]dx | em [0, 1], g_n = g; em [1, ∞), \|g_nK\| ≤ \|g\|K ∈ L¹; convergência dominada, logo T[g_n] → T[g] = (1/2π)∫h Re ψ (H2 §5, pois 𝒜 ⊂ 𝒢) | (A1) |
| Zeros Σ_ρ h_n(γ_ρ) | para γ = t + iy com \|y\| < ½, duas integrações por partes dão h_n(γ) = −γ⁻²∫g_n″e^{iγx}dx e \|e^{iγx}\| ≤ e^{\|x\|/2}. Como g_n″ = g″χ_n + 2n⁻¹g′χ′(·/n) + n⁻²gχ″(·/n), ‖e^{\|x\|/2}g_n″‖₁ ≤ M uniforme em n. Com \|h_n(γ)\| ≤ ‖e^{\|x\|/2}g‖₁, vale \|h_n(γ)\| ≤ M′/(1 + t²) uniforme em n e em y. Pontualmente h_n(γ) → h(γ). Convergência dominada sobre os zeros **se** Σ_ρ 1/(1 + t_ρ²) < ∞ (com multiplicidade) | (A1), j ≤ 2; **Z1** |

**Conclusão de §2** (revisão 11.3b-5). Para g ∈ 𝒜, a forma de referência vale com a soma sobre zeros **absolutamente
convergente**.

**Ponto de partida matemático:**
- Teorema 6 e Lema 3 de Connes, conferidos em §1a;
- normalização de Haar e média de fibra (H2);
- **Z1**, agora **derivado** em [ETAPA11_3B_Z1_CONTAGEM.md](ETAPA11_3B_Z1_CONTAGEM.md) por N(T) ≤ 31 + 5,25·T·log(T + 9),
  via DLMF 25.2.1 e 25.2.10 e a fórmula de Jensen.

**Pendências só bibliográficas:**
- F5: conferir o enunciado original de Weil;
- J1: fonte arquivada para a fórmula de Jensen.

**Registro anterior (substituído):** Z1 não se infere só da apresentação do produto:
- A DLMF 25.2.12 (arquivada) escreve ζ(s) como produto sobre os zeros Π_ρ(1 − s/ρ)e^{s/ρ}, com fonte Titchmarsh
  (2.12.6), (2.12.8), p. 30–31, sem explicitar o modo de convergência.
- A passagem do produto canônico de gênero 1 para Σ|ρ|⁻² < ∞ é teoria clássica de funções inteiras. A passagem daí
  para Z1 é elementar: para ρ = β + it com 0 < β < 1, |ρ|² = β² + t² < 1 + t², logo 1/(1 + t²) < 1/|ρ|².
- A rota foi abandonada em favor da derivação por contagem (F8 resolvida em ETAPA11_3B_Z1_CONTAGEM).

## 3. Funções-teste concretas do projeto

| Função | Pertence a 𝒜? | Justificativa (derivação) |
|---|---|---|
| Gaussianas h(r) = e^{−(r/T)²}cos(ar) da checagem de L-EF1 | **sim** | g(x) = (T/4√π)[e^{−T²(x−a)²/4} + e^{−T²(x+a)²/4}] é inteira, e g^{(j)} = polinômio × gaussiana; (A1) e (A2) valem para todo b |
| h_ε = k_t * φ_ε de L-EF2b, com ε > 0 fixo | **sim** | g_{h_ε}(u) = g_{k_t}(u)e^{−ε²u²/2}; g_{k_t} = G_t(u) + G_t(−u), com G_t(u) = (1/2π)∫f_t(E)e^{−iEu}dE inteira e \|G_t^{(j)}\| ≤ (1/2π)∫_{A}^{B}\|E\|^j dE ≤ B^jL/(2π) (f_t tem suporte em [A, B] e \|f_t\| ≤ 1). Pela regra de Leibniz, g^{(j)} é limitada por polinômio × gaussiana; (A1) e (A2) valem |
| Janela de Hann sem suavização (ε = 0) | **não** | g_{k_t} decai só como \|u\|⁻³: (A2) falha, e e^{\|x\|/2}g ∉ L¹. Φ(s) nem é definida fora da reta crítica. Coerente com H1 (L-EF2c) aberta |
| e^{−3\|x\|/2} (controle P1 de H2) | **não** | não é C¹ em 0. Serve só como controle da regularização local (H2 §§3–4) |

**Consequência para L-EF2b.** A identidade suavizada de ETAPA11_3B_FORMULA_EXPLICITA §2.2(b) usa a forma de referência
para h_ε. Com §1a, §2 e §3, isso passa a ter ponto de partida matemático no Teorema 6 de Connes, com Z1 derivado.
Restam: F1 (H₀, criticidade), pendência bibliográfica F5 e J1. A cota de contagem usada em R_longe agora é derivada.

## 4. Estado e dependências

| Item | Situação |
|---|---|
| Classe de funções-teste de L-EF1 | **especificada**: 𝒜, suficiente; admissibilidade derivada do Teorema 6 de Connes (conferido, §1a) por aproximação, com Z1 derivado |
| Dependências matemáticas remanescentes | nenhuma além das fontes lidas (Connes Teorema 6, Lema 3, normalização; DLMF 25.2.1, 25.2.10, 5.9.12) e da fórmula de Jensen |
| Pendências bibliográficas | F5 (enunciado original de Weil); J1 (fonte arquivada para Jensen) |
| Funções do projeto | gaussianas e h_ε (ε > 0) ∈ 𝒜; janela de Hann sem suavização ∉ 𝒜 |
| Admissibilidade em 𝒜 | derivação concluída a partir dos enunciados conferidos em Connes |
| Z1 | derivada (ETAPA11_3B_Z1_CONTAGEM), com J1 como pendência bibliográfica |
| L-EF1 | fechamento documental pendente de F5 e J1 |
| L-EF2c (H1) | aberta, sem consequência automática dos fechamentos anteriores |
| F1–F7 | `bloqueado` por acesso, sem alteração |
