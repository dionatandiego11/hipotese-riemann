# Etapa 11.3b / H2 — derivação analítica do termo arquimediano da fórmula explícita

**Data:** 14/09/2026. **Estado de H2:** derivação concluída, condicionada à aplicabilidade do Teorema 1 de Weil à
classe indicada (F5). A 11.3b continua `em execução`, L-EF1 não fica encerrada e H1 (L-EF2c) continua aberta.
F1–F7 continuam `bloqueado` por acesso.

**Fontes (todas arquivadas, SHA-256 em `archive/fontes_etapa11/MANIFESTO.csv`):**
- **Connes 1999, arXiv:math/9811068v1, Apêndice II:**
  - p. 68, eqs. (1)–(3);
  - p. 69, eqs. (4)–(10);
  - p. 70, eq. (11) e Teorema 1 (Weil);
  - p. 73, eq. (31) e cálculo da média de fibra;
  - p. 78, eqs. (1)–(6), normalização de Haar em grupos modulados.
  - As eqs. (8)–(11) e (31) foram conferidas visualmente nas páginas renderizadas.
- **DLMF §5.9, eq. 5.9.12** (`dlmf_5.9.html`, baixado em 14/09/2026 09:33:49, SHA-256 `778124f0…`):
  ψ(z) = ∫₀^∞ (e^{−t}/t − e^{−zt}/(1 − e^{−t})) dt, para ℜz > 0.

**Alvo** (plano §3.1, com g(u) = (1/2π)∫h(r)e^{−iru}dr):

−D_∞ = −g(0) log π + (1/2π) ∫_ℝ h(r) Re ψ(¼ + ir/2) dr.

---

## 1. Classe de funções-teste usada (suficiente, não ótima)

𝒢 é o conjunto dos pares (g, h) com:
- **(G1)** h: ℝ → ℂ par, mensurável, com ∫|h(r)|(1 + r²) dr < ∞. Como classe de L¹, h é tomado no seu **representante
  contínuo** quando este existe (ver G3);
- **(G2)** g(u) = (1/2π)∫h(r)e^{−iru}dr. Por (G1), g é par, de classe C², limitada, com g' e g'' limitadas; em
  particular g é lipschitziana;
- **(G3)** g ∈ L¹(ℝ). Então ∫g(x)e^{irx}dx é contínua em r e, pela inversão de Fourier, coincide com h **quase em toda
  parte**. Escolhe-se explicitamente h como esse representante contínuo; só assim vale a igualdade **pontual**
  Φ(½ + iγ) = h(γ). A continuidade não decorre da mera mensurabilidade de h;
- **(G4)** para o Teorema 1 (Weil, via Connes p. 68, eq. 2): |g(x)| = O(e^{−b|x|}) com b > ½.

**Funções fora do cálculo:** (G4) não é usada no cálculo de D_∞ (§3–§5), que só precisa de (G1)–(G3). Ela entra ao
aplicar o Teorema 1.

**Membros e não membros de 𝒢:**
- as gaussianas da checagem numérica pertencem a 𝒢;
- h_ε = k_t * φ_ε de L-EF2b pertence a 𝒢: h_ε é de Schwartz na reta, e g_{h_ε} tem decaimento gaussiano;
- a janela de Hann sem suavização satisfaz (G1)–(G3), mas **não** (G4): g_k decai só como |u|⁻³. É coerente com a
  necessidade de suavização em L-EF2.

**Dependência de F5:** Connes registra como hipótese de Weil só o decaimento (2). Se o enunciado original de Weil
exigir regularidade adicional, falta conferir que 𝒢 a satisfaz. O **cálculo** de D_∞ abaixo não depende de F5; a
**aplicabilidade** da fórmula explícita a 𝒢 depende.

## 2. Distribuição local real e mudança de variáveis

**(i) Dicionário** (Connes p. 68–70; k = ℚ, caractere trivial):
- Φ(s) = ∫_{ℝ*₊} F(ν)ν^{1/2−s}d*ν (eq. 3);
- S(X₀, F) = Σ_ρ N(ρ)Φ(ρ) (eq. 4);
- Teorema 1: S = Δ(F(|w|)), com Δ = log|d⁻¹|δ₁ + D − Σ_v D_v (eq. 5).
- Para ℚ, log|d⁻¹| = 0 (p. 69: |d|⁻¹ é o discriminante, a menos de sinal).

Tomando F(eˣ) = g(x) e d*ν = dν/ν (p. 78, eq. 6):
- Φ(½ + iγ) = ∫g(x)e^{−iγx}dx = h(γ), por paridade;
- os termos D e D_p já foram tratados em ETAPA11_3B_FORMULA_EXPLICITA §1.2 e §3.

Logo Σ_ρ h(γ_ρ) = h(i/2) + h(−i/2) − D_∞(F) − Σ_p D_p(F).

**(ii) Distribuição local real** (eq. 8, v = ∞, k_∞ = ℝ):

D_∞(F) = Pfw ∫_{ℝ*} φ(u) d*u, com φ(u) = F(|u|)|u|^{1/2}/|1 − u|.

A integral é divergente em u = 1 (singularidade 1/|1 − u| não integrável). A prescrição Pfw é a regularização.

**(iii) Medida de Haar em ℝ*** (p. 78, eqs. 2–4):
- ℝ* é grupo modulado com núcleo compacto G₀ = {±1} e imagem N = ℝ*₊;
- d*u se decompõe como d*ν = dν/ν em N vezes a medida de massa total 1 em {±1}, isto é, peso ½ em cada sinal.

**(iv) Integração nas fibras** (p. 70, logo abaixo de (10)):

ψ(ν) = ∫_{|u|=ν} φ(u) d_ν u = ½[φ(ν) + φ(−ν)] = ½F(ν)ν^{1/2}[1/|1 − ν| + 1/(1 + ν)].

*Confirmação da normalização ½ na própria fonte:* na p. 73, para F = f₀³, Connes escreve "integrating over the fibers
gives f₀⁴ × (1 − f₀⁴)⁻¹". Com a fórmula acima:
- para ν < 1: ½·ν^{3/2}·ν^{1/2}·2/(1 − ν²) = ν²/(1 − ν²);
- para ν > 1: ½·ν^{−1}·2ν/(ν² − 1) = ν^{−2}/(1 − ν^{−2});
- ambos são f₀⁴/(1 − f₀⁴), com f₀⁴ = min(ν², ν⁻²). ✓

**(v) Regularização** (eqs. 10–11):

Pfw ∫ φ d*u = PF₀ ∫ ψ d*ν = 2 log(2π)·c + lim_{t→∞}[ ∫(1 − f₀^{2t})ψ d*ν − 2c log t ],

- f₀(ν) = min(ν^{1/2}, ν^{−1/2}) e f₁ = f₀⁻¹ − f₀;
- a hipótese é que ψ − c f₁⁻¹ seja integrável em ℝ*₊.

**(vi) Coordenada logarítmica** ν = eˣ, d*ν = dx:
- e^{x/2}/|1 − eˣ| = 1/(2|sinh(x/2)|) e e^{x/2}/(1 + eˣ) = 1/(2cosh(x/2));
- ψ(eˣ) = (g(x)/4)·K(x), com K(x) = 1/|sinh(x/2)| + 1/cosh(x/2);
- f₁⁻¹(eˣ) = e^{x/2}/|1 − eˣ| = 1/(2|sinh(x/2)|) e f₀^{2t}(eˣ) = e^{−t|x|}.

## 3. Determinação de c e verificação da hipótese de (11)

- **Valor de c.** Perto de x = 0, ψ(eˣ) = g(x)/(4|sinh(x/2)|) + O(1). A parte singular de ψ é (g(0)/2)·f₁⁻¹, logo
  **c = g(0)/2**.
- **Integrabilidade de ψ − c f₁⁻¹** = (g(x) − g(0))/(4|sinh(x/2)|) + g(x)/(4cosh(x/2)):
  - perto de 0: |g(x) − g(0)| ≤ ‖g'‖_∞|x| (G2) e |sinh(x/2)| ≥ |x|/2, logo o primeiro termo é limitado;
  - no infinito: os dois termos são O(e^{−|x|/2}), pois g é limitada;
  - logo ψ − c f₁⁻¹ ∈ L¹(dx). ✓

**Resultado de (v):**

D_∞(F) = g(0) log(2π) + lim_{t→∞} [ ½∫₀^∞ (1 − e^{−tx}) g(x)K(x) dx − g(0) log t ],   (★)

usando a paridade de g para ∫_ℝ = 2∫₀^∞. Para t fixo, a integral converge: (1 − e^{−tx}) ≤ tx cancela o 1/x de K, e
g(x)K(x) = O(e^{−x/2}) no infinito.

## 4. Separação da singularidade e limite t → ∞

**Decomposição.** Para t fixo:

½∫₀^∞(1 − e^{−tx})gK dx = ½∫₀^∞(1 − e^{−tx})[gK − 2g(0)e^{−2x}/x] dx + g(0)∫₀^∞(1 − e^{−tx})e^{−2x}/x dx.

Os dois integrais são finitos para t fixo.

**Integral de Frullani** (elementar). Para 0 < a < b:
∫_ε^∞ (e^{−ax} − e^{−bx})/x dx = ∫_{aε}^{bε} e^{−y}/y dy → log(b/a) quando ε → 0. Logo:

∫₀^∞ (1 − e^{−tx})e^{−2x}/x dx = ∫₀^∞ (e^{−2x} − e^{−(t+2)x})/x dx = log((t + 2)/2).

**Convergência dominada** no primeiro integral. Seja R(x) = gK − 2g(0)e^{−2x}/x.
- **Perto de 0:** K(x) = 2/x + 1 + O(x) e (1 − e^{−2x})/x = O(1), logo
  R(x) = 2(g(x) − g(0))/x + g(x)(K(x) − 2/x) + 2g(0)(1 − e^{−2x})/x é limitado (G2).
- **No infinito:** |R(x)| ≤ C‖g‖_∞e^{−x/2} + 2|g(0)|e^{−2x}/x.
- Então R ∈ L¹(0, ∞), |(1 − e^{−tx})R| ≤ |R| e (1 − e^{−tx}) → 1 pontualmente. Por convergência dominada:

  ½∫₀^∞(1 − e^{−tx})R dx → ½∫₀^∞ R dx =: −T[g], com T[g] = ∫₀^∞ [g(0)e^{−2x}/x − ½g(x)K(x)] dx.

**Substituindo em (★):**

D_∞(F) = g(0) log(2π) + lim_{t→∞}[−T[g] + g(0) log((t + 2)/2) − g(0) log t]
       = g(0) log(2π) − T[g] − g(0) log 2
       = **g(0) log π − T[g]**.

## 5. Identificação de T[g] com a integral de ψ

**Passo 1 (DLMF 5.9.12, z = ¼ + ir/2, ℜz = ¼ > 0).** Tomando parte real:

Re ψ(¼ + ir/2) = ∫₀^∞ B(r, s) ds, com B(r, s) = e^{−s}/s − e^{−s/4}cos(rs/2)/(1 − e^{−s}).

**Passo 2 (Fubini).** Majorante de |B|:
- **para 0 < s ≤ 1:** B = [e^{−s}/s − e^{−s/4}/(1 − e^{−s})] + e^{−s/4}(1 − cos(rs/2))/(1 − e^{−s});
  - o primeiro colchete é contínuo em [0, 1], com limite −5/4 em s → 0, logo limitado;
  - no segundo, 1 − cos(rs/2) ≤ r²s²/8 e 1 − e^{−s} ≥ s/2, logo ele é ≤ r²s/4 ≤ r²/4;
- **para s > 1:** |B| ≤ e^{−s} + e^{−s/4}/(1 − e^{−1}).

Portanto ∫∫|h(r)||B(r, s)| ds dr ≤ C∫|h|(1 + r²) dr < ∞ por (G1), e a ordem de integração pode ser trocada:

(1/2π)∫h(r) Re ψ(¼ + ir/2) dr = ∫₀^∞ [ e^{−s}/s · (1/2π)∫h dr − e^{−s/4}/(1 − e^{−s}) · (1/2π)∫h(r)cos(rs/2) dr ] ds.

**Passo 3 (inversão).** Por (G2) e paridade de h: (1/2π)∫h dr = g(0) e (1/2π)∫h(r)cos(rs/2) dr = g(s/2). Logo:

(1/2π)∫h Re ψ dr = ∫₀^∞ [ g(0)e^{−s}/s − g(s/2)e^{−s/4}/(1 − e^{−s}) ] ds.

**Passo 4 (s = 2x).**
- e^{−s}/s ds = e^{−2x}/x dx.
- e^{−s/4}/(1 − e^{−s}) ds = 2e^{−x/2}/(1 − e^{−2x}) dx.
- 2e^{−x/2}/(1 − e^{−2x}) = e^{x/2}/sinh x = (cosh(x/2) + sinh(x/2))/(2 sinh(x/2) cosh(x/2)) = ½K(x), para x > 0.

Portanto (1/2π)∫h(r) Re ψ(¼ + ir/2) dr = ∫₀^∞ [g(0)e^{−2x}/x − ½g(x)K(x)] dx = **T[g]**.

## 6. Resultado

Para (g, h) ∈ 𝒢 com (G1)–(G3):

−D_∞(F) = −g(0) log π + (1/2π) ∫_ℝ h(r) Re ψ(¼ + ir/2) dr,

que é exatamente o termo arquimediano da forma de referência (plano §3.1).

**Com os resultados anteriores** (termos D e D_p), e sob o Teorema 1 aplicado a F(eˣ) = g(x), o que exige (G4) e o que
F5 vier a exigir:

Σ_ρ h(γ_ρ) = h(i/2) + h(−i/2) − g(0) log π + (1/2π)∫h(r) Re ψ(¼ + ir/2) dr − 2Σ_n Λ(n)n^{−1/2}g(log n).

## 7. Checagens numéricas dos passos (classe B; não substituem a derivação)

- **Script:** `results/etapa11_3b/check_archimedean_derivation.py`.
- **Saída:** `results/etapa11_3b/check_archimedean_derivation.json`.
- **Precisão:** mpmath, 30 dígitos.

| Passo | Conteúdo | Resultado |
|---|---|---|
| P1 | Connes (31): D_∞(f₀³) = log π + γ. Pelas §§3–4, com g = e^{−3\|x\|/2}, exige T[g] = −γ, com T[g] definido pela integral em x de §4 | T[g] = −0,5772156649015329 = −γ (diferença 0 em 30 dígitos). **Escopo:** g = e^{−3\|x\|/2} **não** pertence a 𝒢 (não é diferenciável em 0 e sua transformada h(r) = 3/(9/4 + r²) não tem segundo momento absoluto finito). P1 é controle da **regularização das §§3–4**, cujas hipóteses são mais fracas (g par, limitada, lipschitziana em 0), e confirma o fator ½ da fibra e a constante 2 log(2π) contra um valor calculado por Connes. **Não** é aplicação do argumento de Fubini da §5 |
| P2 | (10)–(11) avaliadas diretamente, com t = 10³, 10⁴, 10⁵ e extrapolação em 1/t, contra g(0) log π − T[g] (gaussiana, T₀ = 5) | extrapolado 1,94982762; derivado 1,94982763; diferença −8,9·10⁻⁹, limitada pela extrapolação |
| P3 | T[g] contra (1/2π)∫h Re ψ, com a mesma gaussiana (em 𝒢; testa também §5) | −0,3352159347118184 nos dois lados (diferença 0) |

A checagem gaussiana anterior (ETAPA11_3B_FORMULA_EXPLICITA §1.3), que usa o termo arquimediano na fórmula completa,
fica como verificação final. Não foi ampliada.

## 8. Efeito e limites

- **H2 fechada como derivação:** o termo arquimediano deixa de ser só "checagem B" e passa a `derivacao` sobre fontes
  arquivadas (Connes App. II; DLMF 5.9.12), para a classe 𝒢.
- **L-EF1 não fica encerrada.** A aplicabilidade do Teorema 1 de Weil a 𝒢 depende de F5, e a fonte de Connes é
  secundária em relação a Weil.
- **L-EF2c (H1) continua aberta:** a janela sem suavização não satisfaz (G4).
- Os passos usam a normalização de Haar e a média de fibra lidas em Connes. A consistência com o valor (31) de Connes
  (P1) é evidência B dessa leitura, não uma prova independente.
