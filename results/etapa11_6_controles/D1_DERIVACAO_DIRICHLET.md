# Controle `ctrl-dirichlet-v1` — derivação D1 (19/09/2026)

Exigida pela §3 de [DECLARACAO_DIRICHLET.md](DECLARACAO_DIRICHLET.md) (SHA-256 `e6cb8ab8…`), **antes de qualquer
código**. SHA-256 deste arquivo em `D1_DERIVACAO_DIRICHLET.sha256`. Nenhum cálculo numérico. Nenhuma afirmação sobre RH
ou GRH.

**Escopo.** Justificar P1 (coeficientes), P2 (densidade suave) e o método de cálculo dos zeros (função Z_χ real). O
controle é **empírico** (classe B), como as execuções m4: esta derivação fixa o que o instrumento deve medir; ela não
certifica o instrumento nem controla os restos do modelo de linhas (o análogo de H1 fica aberto, como para ζ).

**Fonte:** Montgomery–Vaughan, *Multiplicative Number Theory I* (arquivo registrado no manifesto de fontes), lido nas
páginas citadas. Notação: χ real primitivo módulo q > 1, κ ∈ {0, 1} com χ(−1) = (−1)^κ, a := ¼ + κ/2, ρ = ½ + iγ
(γ complexo em geral).

## 1. Fator de raiz e simetria

(10.17), p. 332: ε(χ) = τ(χ)/(i^κ q^{1/2}). Teorema 9.17, p. 300: τ(χ_d) = √d se d > 0 e τ(χ_d) = i√|d| se d < 0.
- χ₋₄ (d = −4, q = 4, κ = 1): ε = 2i/(i·2) = 1.
- χ₅ (d = 5, q = 5, κ = 0): ε = √5/√5 = 1.

Como χ é real, conj L(s, χ) = L(s̄, χ): os zeros vêm em pares ρ, ρ̄, isto é, γ ↦ −γ (com multiplicidade).

## 2. Z_χ é real (item 1 do método)

Corolário 10.8, p. 333: ξ(s, χ) = (q/π)^{(s+κ)/2} Γ((s + κ)/2) L(s, χ) é inteira e ξ(s, χ) = ε(χ) ξ(1 − s, χ̄).

Para t real: conj ξ(½ + it, χ) = ξ(½ − it, χ̄), porque (q/π)^{w} e Γ(w) são reais para w real e conj L(s, χ) = L(s̄, χ̄).
Como χ̄ = χ, isso é ξ(½ − it, χ). Pela equação funcional com ε = 1, ξ(½ − it, χ) = ξ(1 − (½ − it), χ) = ξ(½ + it, χ).
Logo ξ(½ + it, χ) é **real**.

Com θ_χ(t) := arg Γ(a + it/2) + (t/2) log(q/π) (argumento contínuo, θ_χ(0) = 0), e usando
(q/π)^{(½+it+κ)/2} = (q/π)^{(½+κ)/2}(q/π)^{it/2} e Γ((½ + it + κ)/2) = Γ(a + it/2) = |Γ(a + it/2)| e^{i arg Γ(a + it/2)}:

ξ(½ + it, χ) = (q/π)^{(½+κ)/2} · |Γ(a + it/2)| · e^{iθ_χ(t)} L(½ + it, χ).

Portanto **Z_χ(t) := e^{iθ_χ(t)} L(½ + it, χ) = ξ(½ + it, χ) / [(q/π)^{(½+κ)/2}|Γ(a + it/2)|] é real**, e seus zeros
reais são exatamente os zeros de L(s, χ) na reta crítica. Uma troca de sinal de Z_χ indica zero de multiplicidade
ímpar; zeros de multiplicidade par ou fora da reta não aparecem como troca de sinal (por isso a verificação V1 de
completude).

## 3. Fórmula explícita na convenção do projeto (P1)

**Teorema 12.13 (Weil), p. 410**, para χ primitivo (E₀(χ) = 0): com Φ(s) = ∫F(x)e^{−(s−½)2πx}dx,

lim_{T→∞} Σ_{|γ|≤T} Φ(ρ) = (1/2π)(log(q/π) + ψ(a)) F(0)
  − (1/2π) Σ_n Λ(n) n^{−1/2} [χ(n)F(−log n/2π) + χ̄(n)F(log n/2π)]
  + ∫₀^∞ e^{−(1+2κ)πx}/(1 − e^{−4πx}) · (2F(0) − F(x) − F(−x)) dx,

sob as hipóteses do teorema (decaimento exponencial de F e de dF com peso e^{(½+δ₀)2π|x|}; F média dos limites laterais;
F(x) + F(−x) = 2F(0) + O(|x|)).

**Conversão.** Convenção do projeto: h(r) = ∫g(u)e^{iru}du, g par. Tomando F(x) := 2π g(2πx):
- Φ(½ + iγ) = ∫2πg(2πx)e^{−2πiγx}dx = ∫g(u)e^{−iγu}du = h(γ);
- F(±log n/2π) = 2π g(log n); com χ real, o termo de primos vira **−2 Σ_n Λ(n)χ(n) n^{−1/2} g(log n)**;
- F(0) = 2πg(0), e, com x = u/2π, a integral vira ∫₀^∞ 2e^{−2au}(g(0) − g(u))/(1 − e^{−2u}) du (note 2a = ½ + κ).

**Termo arquimediano.** Pela representação DLMF 5.9.12, ψ(z) = ∫₀^∞ (e^{−t}/t − e^{−zt}/(1 − e^{−t})) dt (ℜz > 0), a
mesma conta do lema arquimediano do projeto ([ETAPA11_3B_TERMO_ARQUIMEDIANO.md](../../docs/ETAPA11_3B_TERMO_ARQUIMEDIANO.md)
§5), agora com z = a + ir/2, dá

(1/2π)∫h(r) Re ψ(a + ir/2) dr = ψ(a) g(0) − ∫₀^∞ 2e^{−2au}(g(u) − g(0))/(1 − e^{−2u}) du

(Fubini sob ∫|h|(1 + |r|) < ∞, como no lema citado; o integrando em u é limitado perto de 0 porque g(u) − g(0) = O(u²)
para g par e suave). Comparando termo a termo:

**Σ_ρ h(γ_ρ) = (1/2π)∫h(r)[log(q/π) + Re ψ(a + ir/2)] dr − 2 Σ_{n≥2} Λ(n)χ(n) n^{−1/2} g(log n)**,

com a soma sobre zeros no sentido simétrico do teorema. Diferenças em relação à forma de referência de ζ:
(i) **não há** termos h(±i/2) (L(s, χ) é inteira); (ii) Λ(n) → Λ(n)χ(n); (iii) o termo suave troca ¼ por a e ganha
log q. Como θ_χ′(r) = ½ Re ψ(a + ir/2) + ½ log(q/π), o termo suave é **(1/π)∫h(r)θ_χ′(r) dr**.

**Modelo de linhas.** Repetindo a §2.2(b) de [ETAPA11_3B_FORMULA_EXPLICITA.md](../../docs/ETAPA11_3B_FORMULA_EXPLICITA.md)
(k_t(E) = f_t(E) + f_t(−E), h_ε = k_t ∗ φ_ε, divisão por 2 usando a simetria γ ↦ −γ do §1), com f_t suportada em
[A, B] ⊂ (0, ∞) (um eventual zero em γ = 0 contribui (k_t ∗ φ_ε)(0) → 0):

D_t − ∫_A^B f_t(E) θ_χ′(E)/π dE = Σ_n (c_χ(n)/2) e^{−ε²(log n)²/2}[e^{iE_c log n}W(t − log n) + e^{−iE_c log n}W(t + log n)] + R_ε,

com **c_χ(n) = −Λ(n)χ(n)/(π√n)**, pois −Λ(n)χ(n)n^{−1/2}[G_t(log n) + G_t(−log n)] = (c_χ(n)/2)[⋯] exatamente como no caso
de ζ (G_t(u) = (1/2π)e^{−iE_c u}W(t + u)). O resto R_ε tem as parcelas de troca f_t → h_ε e de suavização do termo suave;
**não** há parcela de polos. **P1 confirmada.**

## 4. Densidade suave (P2)

θ_χ′(E)/π = (1/2π)[Re ψ(a + iE/2) + log(q/π)]. Por DLMF 5.11.2 com o resto de §5.11(ii) (mesma conta da §II.22.2 de
[ETAPA11_3B_H1_CAUDA_PROJETADA.md](../../docs/ETAPA11_3B_H1_CAUDA_PROJETADA.md), trocando ¼ por a):
- ln|a + iE/2| − ln(E/2) = ½ ln(1 + 4a²/E²) ∈ [0, 2a²/E²];
- Re(1/(2z)) = a/(2|z|²) ∈ (0, 2a/E²];
- |Re R| ≤ 2√2/(3E²) (½ ph z < π/4, |z|² ≥ E²/4).

Logo |θ_χ′(E)/π − (1/2π) log(qE/2π)| ≤ C_a/E², com **C_a = (2a² + 2a + 2√2/3)/(2π)** (para a = ¼ recupera o C do
projeto). **P2 confirmada:** d̄_χ(E) = (1/2π) log(qE/2π), com erro O(E⁻²) explícito.

## 5. Contagem para V1

Teorema 14.5, p. 454: N(T, χ) = (1/π) arg Γ(a + iT/2) + (T/2π) log(q/π) + S(T, χ) − S(0, χ), contando zeros com
0 < β < 1 e 0 ≤ γ ≤ T (bordas com peso ½). Como θ_χ(T)/π = (1/π) arg Γ(a + iT/2) + (T/2π) log(q/π),
**N(T, χ) = θ_χ(T)/π + S(T, χ) − S(0, χ)**, que é a forma usada em V1 (sem estimar S).

## 6. Conclusão

- P1 e P2 da declaração **conferem** com a derivação; **não há adendo**.
- O método do §4 da declaração (troca de sinal de Z_χ real) está justificado pelo §2.
- Limites: o Teorema 12.13 exige decaimento exponencial de F; a janela de Hann do instrumento não é admissível sem
  suavização (mesma situação de ζ, H1 aberta). O controle usa o instrumento em modo empírico e não depende de
  controlar R_ε.
- A multiplicidade dos zeros de L(s, χ) e sua criticidade **não** são supostas: V1 detecta falta de trocas de sinal
  (zeros múltiplos ou fora da reta apareceriam como déficit de contagem).
