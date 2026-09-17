# Etapa 11.3b — fórmula explícita (L-EF1, L-EF2), integrais locais de Connes (C02) e corpos de funções (C11/C19)

**Data:** 14/09/2026 (revisão 11.3b-2 no mesmo dia). **Estado:** `em execução`. Nenhum experimento do protocolo foi reaberto e a tabela de
correspondências não foi ampliada.

**Fontes locais:**
- `archive/fontes_etapa11/` (SHA-256 em `MANIFESTO.csv`);
- verificação numérica em `results/etapa11_3b/`.

**Acesso externo nesta sessão (14/09/2026, 08:55–09:05):**
- arXiv, Numdam e jmilne.org recusaram conexão, por curl (com e sem sandbox) e por WebFetch;
- dlmf.nist.gov respondeu.

Por isso, fontes que dependiam desses servidores continuam **não obtidas**. Nenhuma afirmação abaixo se apoia nelas
como conferida.

---

## 1. L-EF1 — constantes e classe de funções-teste da forma de referência

### 1.1 Resultado

| Parte da forma §3.1 | Situação | Suporte |
|---|---|---|
| Soma sobre todos os zeros com multiplicidade, sem RH (Φ(ρ) avaliada em ρ complexo) | **conferido-secundaria** | Connes App. II, eq. (4) e Teorema 1 (p. 69–70): S(X, F) = Σ_ρ N(X, ρ)Φ(ρ), soma sobre 0 < ℜρ < 1 |
| Termos de polo h(i/2) + h(−i/2) | **derivacao** sobre fonte | Connes p. 71, eqs. (18)–(19): ⟨D, F⟩ = ĥ(0) + ĥ(1). Com a mudança de variáveis de §1.2, Φ(0) = h(i/2) e Φ(1) = h(−i/2) |
| Termo primo −2 Σ Λ(n) n^{−1/2} g(log n) (coeficiente 2, sinal −, peso n^{−1/2}) | **derivacao** sobre fonte | §1.2 (mesma conta que C02, §3) |
| Termo arquimediano −g(0) log π + (1/2π)∫h(r) Re ψ(¼ + ir/2) dr | **derivacao** (H2, 14/09/2026), para a classe 𝒢 | [ETAPA11_3B_TERMO_ARQUIMEDIANO.md](ETAPA11_3B_TERMO_ARQUIMEDIANO.md): Connes App. II, eqs. (8), (10), (11), (31), p. 78 (Haar), e DLMF 5.9.12; evidência E-LEF1-ARCH. A checagem B de §1.3 fica como verificação final |
| Termo log\|d⁻¹\| | 0 para ℚ | Connes p. 69: \|d\|⁻¹ é, a menos de sinal, o discriminante; para ℚ vale 1 |
| Classe de funções-teste | **derivacao condicional** (classe suficiente 𝒜; [ETAPA11_3B_ADMISSIBILIDADE.md](ETAPA11_3B_ADMISSIBILIDADE.md)); ponto de partida no Teorema 6 de Connes (conferido) com Z1 derivado; pendências bibliográficas F5 e J1. Registro anterior: PC | Connes (p. 68, eq. 2) registra só F(ν) = O(ν^{b}) em 0 e O(ν^{−b}) em ∞, com b > ½, isto é, g(x) = O(e^{−b\|x\|}). O enunciado original de Weil pode exigir regularidade adicional; não conferido (fonte primária não obtida) |

**Leitura:** L-EF1 fica **parcialmente resolvida**.
- Estrutura, sinais, fator 2 e termos de polo: derivados de uma fonte com página (Connes restaurando Weil; secundária).
- Termo arquimediano: **derivado analiticamente** (H2) para a classe 𝒢 com ∫|h|(1+r²) < ∞ e g ∈ L¹. A checagem B (§1.3) vira verificação final.
- Classe exata de funções-teste: PC. Classe A exigiria a fonte primária (Weil 1952) ou uma derivação arquimediana
  completa.

### 1.2 Derivação dos termos de polo e primo a partir de Weil (via Connes, App. II)

**Notação** (Connes p. 68–71, k = ℚ, caractere trivial X₀):
- N = ℝ*₊, com d*ν = dν/ν (p. 78, eq. 6);
- Φ(s) = ∫ F(ν) ν^{1/2−s} d*ν (eq. 3);
- Δ = log\|d⁻¹\| δ₁ + D − Σ_v D_v (eq. 5);
- Teorema 1: S(X, F) = Δ(F(\|w\|) X(w)).

**Mudança de variáveis.** Tomando F(eˣ) = g(x), com g par e g(x) = (1/2π)∫h(r)e^{−irx}dr:

Φ(½ + iγ) = ∫ F(ν) ν^{−iγ} dν/ν = ∫ g(x) e^{−iγx} dx = h(γ).

Logo:
- S(X₀, F) = Σ_ρ h(γ_ρ), com ρ = ½ + iγ_ρ e γ_ρ possivelmente complexo;
- Φ(0) = h(i/2) e Φ(1) = h(−i/2).

**Termo D** (eq. 6; p. 71). O grupo C_ℚ = ℝ*₊ × Ẑ* tem parte compacta de massa 1 (p. 78, eq. 4). Então
⟨D, F⟩ = ∫₀^∞ F(ν)(ν^{1/2} + ν^{−1/2}) dν/ν = Φ(0) + Φ(1) = h(i/2) + h(−i/2).

**Termo D_p** (eq. 8; lugar finito p).
- D_p(f) = Pfw ∫_{ℚ_p*} F(\|u\|) \|u\|^{1/2} \|1−u\|⁻¹ d*u.
- Decomposição: ℚ_p* = ⊔_n pⁿ ℤ_p*.
- Pela normalização de grupos modulados (p. 79, eq. 8: α = log μ, com μ = p), cada camada \|u\| = p^{−n} tem massa
  log p.

Por camada:
- **n ≥ 1:** \|u\| = p^{−n} < 1, logo \|1−u\| = 1. Contribuição: log p · F(p^{−n}) p^{−n/2}.
- **n ≤ −1:** \|u\| = p^{\|n\|} > 1, logo \|1−u\| = \|u\|. Contribuição: log p · F(p^{\|n\|}) p^{\|n\|/2} p^{−\|n\|} =
  log p · F(p^{\|n\|}) p^{−\|n\|/2}.
- **n = 0:** F(1) · Pfw ∫_{ℤ_p*} d*u/\|1−u\| = 0, pela eq. (9), p. 69.

Portanto D_p = log p Σ_{m≥1} p^{−m/2} [F(p^m) + F(p^{−m})] = 2 log p Σ_{m≥1} p^{−m/2} g(m log p), e
−Σ_p D_p = −2 Σ_n Λ(n) n^{−1/2} g(log n).

**Conclusão:** o termo primo da forma §3.1 sai com coeficiente 2, sinal − e peso n^{−1/2}. Isso também resolve a
avaliação pendente em C02 (§3).

### 1.3 Checagem numérica de consistência (classe B; revisão 11.3b-2)

- **Script:** `results/etapa11_3b/check_explicit_formula.py`.
- **Saída:** `results/etapa11_3b/check_explicit_formula.json`.
- **Zeros:** `data/processed/zeros_100k.csv` (SHA-256 `1af728cf…`). Os primeiros 1.000 são idênticos aos de
  `zeros_10k.csv` (conferido). Os casos usam os primeiros 400 ou 1.000 zeros, índices já consultados.

**Funções-teste:** h(r) = e^{−(r/T)²}cos(ar), pares e inteiras. A soma usa Σ_ρ h(γ_ρ) = 2Σ_{γ>0} h(γ), o que supõe
esses zeros críticos e simples (citação PC, §2.2) e a tabela completa até γ₁₀₀₀. A completude foi conferida por
`mpmath.nzeros` (classe B): N(γ₁₀₀₀ + 10⁻⁶) = 1.000 e N(γ₁₀₀₀ − 10⁻⁶) = 999.

**Orçamento de erro estimado** (não certificado):
- **E_ord:** propagação do erro das ordenadas, 2·3·10⁻⁹·Σ|h′(γ_n)|, com a precisão declarada da tabela;
- **E_z1:** cauda de zeros ainda dentro da tabela, soma explícita;
- **E_z2:** cauda além da tabela, via uma cota de contagem N(T) ≤ T² para T ≥ 7·10⁴ (cota explícita de S(T) não
  citada: **PC**);
- **E_p:** cauda de primos, com a cota elementar Λ(n) ≤ log n e integral dominante (termos decrescentes conferidos);
- **E_quad:** diferença entre quadraturas tanh-sinh e Gauss–Legendre. É **estimativa de estabilidade numérica, não cota
  garantida** do erro de quadratura.

| T | a | diferença (esq − dir) | E_ord | E_z1 | log₁₀ E_z2 | E_p | E_quad | orçamento total | dentro? | alternativa: coef. primo 1 | alternativa: sinal de log π |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | 0 | −2,0·10⁻¹³ | 2,3·10⁻¹² | < 10⁻³⁰⁰ | −9,8·10⁷ | 2·10⁻¹⁹⁶ | 7·10⁻²⁴ | 2,3·10⁻¹² | sim | −3,5·10⁻² | −3,23 |
| 5 | log 2 | 2,3·10⁻¹³ | 2,6·10⁻¹² | < 10⁻³⁰⁰ | −9,8·10⁷ | 1·10⁻¹⁶⁵ | 7·10⁻²⁴ | 2,6·10⁻¹² | sim | −0,52 | −0,16 |
| 5 | log 3 | 1,6·10⁻¹³ | 1,9·10⁻¹² | < 10⁻³⁰⁰ | −9,8·10⁷ | 8·10⁻¹⁴⁹ | 8·10⁻²⁴ | 1,9·10⁻¹² | sim | −0,82 | −1,7·10⁻³ |
| 8 | 1 | −2,4·10⁻¹¹ | 2,7·10⁻¹⁰ | < 10⁻³⁰⁰ | −3,8·10⁷ | < 10⁻³⁰⁰ | 8·10⁻²⁴ | 2,7·10⁻¹⁰ | sim | −0,77 | −5,8·10⁻⁷ |
| 40 | 0 | −4,4·10⁻¹¹ | 1,5·10⁻⁹ | < 10⁻³⁰⁰ | −1,5·10⁶ | < 10⁻³⁰⁰ | 3·10⁻¹⁴ | 1,5·10⁻⁹ | sim | (termo ≈ 0) | −25,8 |

"< 10⁻³⁰⁰" são valores que underflow para 0 em ponto flutuante.

**Leitura (classe B):**
- O resíduo **cabe no orçamento estimado** em todos os casos. As alternativas com constante errada ficam fora dele,
  exceto onde o termo alterado é quase nulo.
- **Não é precisão certificada da identidade.**
- O orçamento depende da precisão declarada das ordenadas (validada em amostra de 20 índices), da criticidade e
  simplicidade dos zeros usados (PC), de uma cota de contagem não citada (PC, só em E_z2) e de uma estimativa de
  quadratura.
- Não demonstra a classe de funções-teste.

## 2. L-EF2 — observável com janela de Hann

### 2.1 Observável efetivamente usada (código congelado m4-v3)

`src/riemann_spectra/periods.py`, idêntico a `archive/code_m4-v3/periods.py` nas linhas 260–300 (conferido por diff):

F_w(t) = Σ_{A ≤ γ ≤ B} w(γ) e^{−i(γ−E_c)t} − ∫_A^B w(E) d̄(E) e^{−i(E−E_c)t} dE,

**Ingredientes:**
- **Janela:** w(E) = ½ − ½cos(2π(E−A)/L) = sin²(π(E−A)/L) em [A, B], zero fora. É C¹, com w(A) = w(B) = 0 e
  w'(A) = w'(B) = 0; w'' tem salto nas bordas.
- **Densidade:** d̄ = d̄_rvm = (1/2π)log(E/2π), com `density = "rvm"` em `configs/m4_v3.toml`. É o termo principal de
  BK SIAM (2.5), p. 239, com erro O(1/t²).
- **Quadratura:** Gauss–Legendre em painéis locais.
- **Alcance:** t ∈ [0,5; 5].
- **Exemplo (bloco d01):** A = 54.512,24, B = 56.585,92, L = 2.073,68, 3.000 zeros.

**Observação de código, sem impacto registrado:** o comentário das linhas 273–275 diz "termo suave por soma direta",
mas a linha 276 calcula `self.smooth` por NUFFT. A soma direta só aparece em `evaluate`. O impacto do termo suave
foi medido em PROTOCOLO §11.2 (≤ 2,0·10⁻¹⁰ contra a forma fechada). Registrado como divergência entre comentário e
código; nada foi alterado, porque o código está congelado.

### 2.2 O que está estabelecido (revisão 11.3b-2)

**Notação:**
- f_t(E) = w(E)e_t(E), com e_t(E) = e^{−i(E−E_c)t}. f_t é C¹ em ℝ, porque w e w′ se anulam nas bordas, e
  M₂ = sup|f_t″| ≤ 2π²/L² + 2πt/L + t².
- D_t = Σ_{A≤γ≤B, tabela} f_t(γ), a soma discreta do instrumento.
- W(ω) = ∫ w(E)e^{−i(E−E_c)ω}dE, real e par, com W(0) = L/2.

#### (a) Identidade de Stieltjes: contagem completa × tabela utilizada

**(a1) Contagem completa** (`derivacao`; fórmula de contagem **conferido-secundaria com ressalva**).

Seja N(E) a contagem de **todos** os zeros não triviais com 0 < Im ρ ≤ E, com multiplicidade. Admite-se
N(E) = θ(E)/π + 1 + S(E):
- fonte: BK SIAM p. 239, eqs. 2.1–2.4, escrita "for the t_n (assumed real)";
- versão incondicional clássica (Titchmarsh, cap. 9): não conferida, **PC**;
- a DLMF §25.10 arquivada **não** contém a fórmula (citação do plano corrigida).

Como w(A) = w(B) = 0:

Σ_{A ≤ Im ρ ≤ B} f_t(Im ρ) = ∫_{[A,B]} f_t dN = ∫_A^B f_t θ′/π dE − ∫_A^B S(E) f_t′(E) dE.

A identidade é exata para a soma sobre **todas** as ordenadas com multiplicidade. Os saltos de N em A e B, que são
zeros (§2.1), têm peso f_t(A) = f_t(B) = 0.

**(a2) Identificação com a tabela.** D_t é igual à soma de (a1) se a tabela contém exatamente as ordenadas em
[A, B], com multiplicidade, e se essas ordenadas são reais e exatas.

- **Completude** (`results/etapa11_3b/check_table_completeness.py`/`.json`, classe B). Nos 30 blocos de m4-v1, m4-v2 e
  m4-v3:
  - o número de ordenadas da tabela em [A, B] é igual a N(B + 10⁻⁶) − N(A − 10⁻⁶) calculado por `mpmath.nzeros`;
  - N(A − 10⁻⁶) é igual ao índice da tabela abaixo de A;
  - as duas condições valem nos 30 blocos (3.000 zeros por bloco);
  - A e B são o primeiro e o último zero de cada bloco;
  - `nzeros` é ponto flutuante, não certificado.
- **Criticidade e multiplicidade:** a igualdade das contagens é **compatível** com zeros simples, mas não a demonstra.
  - Criticidade até 3·10¹²: Platt & Trudgian (2021), *Bull. London Math. Soc.*, doi:10.1112/blms.12460, indicada pela
    auditoria.
  - A página editorial respondeu 403 e o arXiv recusou conexão nesta sessão: texto **não lido**, **PC**.
- **Exatidão das ordenadas:** com |δγ| ≤ 3·10⁻⁹ (precisão declarada, validada em amostra),
  |ΔD_t| ≤ 3·10⁻⁹ · Σ_γ |f_t′(γ)| ≤ 3·10⁻⁹ · N_janela · (π/L + t). No d01 com t = 5: ≤ 4,5·10⁻⁵.

**(a3) Termo determinístico integrado.** O instrumento subtrai d̄_rvm, não θ′/π. Seja Δ = θ′/π − d̄_rvm =
(1/2π)[Re ψ(¼ + iE/2) − ln(E/2)], e |∫_A^B f_t Δ dE| ≤ ∫_A^B w|Δ| dE.

- **Estimativa (classe B)** (`density_error_bound.py`/`.json`): sup|Δ|·L/2, com o supremo tomado nas bordas e Δ
  calculado em mpmath. Vai de 8,6·10⁻⁸ (b01) a 1,25·10⁻⁹ (d10); a integral numérica ∫w|Δ| fica entre 6,8·10⁻⁸ e
  1,22·10⁻⁹. **Não é certificada:** não há controle rigoroso do erro de avaliação nem da maximização.
- **Cota certificada** (`density_error_certified.py`/`.json`; módulo a cota de resto da DLMF §5.11(ii), arquivada):
  - pela DLMF 5.11.2 truncada em n = 1, com resto ≤ sec³(½ ph z)/(12|z|²) e |½ ph z| < π/4 (logo sec³ < 2√2), para
    z = ¼ + iE/2:
    |Δ(E)| ≤ C/E², com C = (1/8 + 1/2 + 2√2/3)/(2π) ≤ 0,24953;
  - daí ∫w|Δ| ≤ C·(L/2)/A², avaliado em aritmética intervalar e **sem maximização numérica**;
  - **resultado:** ≤ 3,2·10⁻⁶ (b01) a ≤ 4,7·10⁻⁸ (d10). Os extremos são exportados como decimais arredondados para cima
    (revisão 11.3b-6; antes `float`, que podia arredondar para baixo);
  - as estimativas B ficam abaixo dessas cotas em todos os blocos (conferido).
- Isso substitui a formulação anterior, que citava só a ordem O(E⁻²) da diferença de densidades.

**Resultado de (a):**

F_w(t) = −∫_A^B S(E) f_t′(E) dE + ∫_A^B f_t Δ dE + (erro de ordenadas),

nas condições de (a2): completude (B), criticidade e simplicidade (PC), precisão declarada.

#### (b) Identidade suavizada, com o fator 2 da simetrização explicitado (`derivacao`, condicionada a L-EF1)

**Construção:**
- Seja k_t(E) = f_t(E) + f_t(−E), par, e h_ε = k_t * φ_ε, com φ_ε(z) = (2πε²)^{−1/2}e^{−z²/(2ε²)}.
- h_ε é inteira, e g_{h_ε}(u) = g_{k_t}(u)e^{−ε²u²/2} decai como gaussiana, o que satisfaz a hipótese de §1.1.
- A forma §3.1 vale exatamente para h_ε, somando **todos** os zeros.

**Fator 2.** Os zeros são simétricos por γ ↦ −γ (equação funcional com conjugação). Se todos os zeros com
|Re γ| ≤ H₀ são críticos:
- Σ_{|γ|≤H₀} k_t(γ) = 2 Σ_{0<γ≤H₀} f_t(γ) = 2D_t, porque f_t só é não nula em [A, B] ⊂ (0, H₀).
- A soma unilateral do instrumento é **metade** da soma simetrizada.
- Aplicando §3.1 a h_ε e **dividindo por 2**:

  ½Σ_ρ h_ε(γ_ρ) = ½[h_ε(i/2) + h_ε(−i/2)] + ½∫ h_ε(r) θ′(r)/π dr − Σ_n Λ(n)n^{−1/2} g_{h_ε}(log n),

  usando (1/2π)[Re ψ(¼ + ir/2) − log π] = θ′(r)/π, que é par.

**Termo de primos:**
- g_{k_t}(u) = G_t(u) + G_t(−u), com G_t(u) = (1/2π)∫f_t(E)e^{−iEu}dE = (1/2π)e^{−iE_cu}W(t + u).
- Com T = log n e c(n) = −Λ(n)/(π√n):

  −Λ(n)n^{−1/2}[G_t(T) + G_t(−T)] = (c(n)/2)[e^{iE_cT}W(t − T) + e^{−iE_cT}W(t + T)].

- Isso é **exatamente** o modelo de linha do instrumento (plano §3.2, com o fator ½ e o termo conjugado). A
  normalização do coeficiente fica confirmada por derivação, não só por ajuste.

**Termo suave:** ½∫ k_t θ′/π dr = ∫_A^B f_t θ′/π dE. A suavização altera esse termo em
|∫ f_t (θ′*φ_ε − θ′)/π| ≤ (ε²/2)·(L/2)·sup|θ‴|/π, mais caudas gaussianas desprezíveis.

**Identidade resultante:**

D_t − ∫_A^B f_t θ′/π dE = Σ_n (c(n)/2)e^{−ε²(log n)²/2}[e^{iE_c log n}W(t − log n) + e^{−iE_c log n}W(t + log n)] + R_ε,

com R_ε = R_zeros + R_suave + R_polos + R_longe. Todas as cotas abaixo são **derivações condicionais** às hipóteses indicadas; nenhuma foi avaliada como resultado certificado.

- **R_zeros (troca f_t → h_ε nos zeros críticos):**
  - para real x, |f_t(x) − (f_t*φ_ε)(x)| ≤ (ε²/2)M₂, já que f_t é C¹ com f_t′ lipschitziana e o kernel é par;
  - a parte refletida (f_t(−·)*φ_ε)(x) em x > 0 é ≤ L(2πε²)^{−1/2}e^{−(x+A)²/(2ε²)};
  - somando: |R_zeros| ≤ (ε²/2)M₂·N_K + L(2πε²)^{−1/2}Σ_{d(γ)>Kε}e^{−d(γ)²/(2ε²)} + (reflexo), onde
    N_K = #{γ ∈ [A − Kε, B + Kε]} (tabela completa, (a2)) e d(γ) é a distância de γ a [A, B];
  - d01, t = 5, K = 10, ε ≤ 0,01: N_K = 3.000, porque os vizinhos de A e B distam 0,583 e 0,492, mais que 10ε = 0,1.
    O primeiro termo é
    ≤ 37.500ε² e os demais são desprezíveis.
- **R_suave:** ≤ (ε²/4)L·sup|θ‴|/π, mais caudas; desprezível.
- **R_polos:** |h_ε(±i/2)| ≤ 2L(2πε²)^{−1/2}e^{1/(8ε²)}e^{−A²/(2ε²)}; desprezível para A ≥ 10⁴.
- **R_longe (zeros com |Re γ_ρ| > H₀, possivelmente não críticos):** γ_ρ = t_ρ + iy com |y| < ½.
  - |h_ε(t + iy)| ≤ 2L(2πε²)^{−1/2}e^{y²/(2ε²)}e^{−(|t|−B)²/(2ε²)}.
  - Com a cota de contagem N(T) ≤ T² para T ≥ H₀ (**derivada** em ETAPA11_3B_Z1_CONTAGEM §4), agrupando os zeros em intervalos unitários, e com termos
    consecutivos decrescendo por um fator ≤ e^{−(H₀−B)/ε²}:

    |½Σ_{|t_ρ|>H₀} h_ε(γ_ρ)| ≤ 4L(2πε²)^{−1/2}(H₀ + 1)² exp(1/(8ε²) − (H₀ − B)²/(2ε²)).

  - Com H₀ = 3·10¹², B ≤ 7,5·10⁴ e 10⁻³ ≤ ε ≤ 1, o expoente é ≤ −4,5·10²⁴ (≤ −4,5·10³⁰ para ε = 10⁻³).
  - **A verificação até H₀ separa esta cauda e a torna quantificável; ela não a elimina.**
  - A cota depende de (i) criticidade até H₀ (Platt–Trudgian, PC). A cota de contagem (ii) está derivada (ETAPA11_3B_Z1_CONTAGEM; dependência bibliográfica J1).

**Juntando com (a2) e (a3):** para cada ε > 0 fixo, com série de primos absolutamente convergente,

F_w(t) = Σ_n (c(n)/2)e^{−ε²(log n)²/2}[e^{iE_c log n}W(t − log n) + e^{−iE_c log n}W(t + log n)] + R_ε + ∫_A^B f_t Δ dE + (erro de ordenadas).

### 2.3 O que continua aberto (L-EF2c)

> **Leitura atual (revisão 11.3b-26, 16/09/2026).** A formulação "passagem ε → 0 com erro controlado" foi refinada em H1:
> - **O limite gaussiano existe condicionalmente:** S3b, |F* − M_ε| ≤ Kε² com K independente de t e de ε, sob F1 (F5 e
>   J1 bibliográficas), em [ETAPA11_3B_H1_R5_ESTIMADOR.md](ETAPA11_3B_H1_R5_ESTIMADOR.md) §2.1. A passagem ε → 0, em
>   si, deixou de ser o ponto aberto.
> - **O aberto é o truncamento finito:** S1 (quantificado e aberto), S3a (aberto) e S2-ratio′ (projeção do truncamento
>   com U declarado), com a decomposição em três termos F* − M_{≤U} = (F* − M_ε) + Σ_{log n≤U}(w_ε − 1)c(n)ℓ_n +
>   Σ_{log n>U}w_εc(n)ℓ_n (R5 §2, "Leitura"). S1 exige controlar os três simultaneamente.
> - **Para S2-ratio′ há uma condição suficiente certificada, só condicional e só num corte:**
>   - condicional a RH, com F5 e J1 bibliográficas;
>   - para a matriz matemática M^math, com U = U₂ = 15 no corte (d₁, Δ) = (8, 2), escolhido após avaliação
>     exploratória;
>   - vale em 461/461 linhas elegíveis
>     ([ETAPA11_3B_H1_CAUDA_PROJETADA.md](ETAPA11_3B_H1_CAUDA_PROJETADA.md) §II.20, execução 4).
>
>   Não vale para outros U, não trata S1, S3a, S3c nem a passagem ao estimador registrado, e não fecha H1.
>
> O texto abaixo registra a análise original da cota absoluta, que continua correta no que afirma.

A observável numérica corresponde a ε = 0: soma de linhas sem amortecimento, com todos os n. Falta controlar ao mesmo
tempo R_ε (pequeno exige ε pequeno), a diferença entre as séries com e sem amortecimento e a cauda de linhas longe de t.

**A cota absoluta utilizada não fecha:**
- R_zeros ≤ 37.500ε² no d01 (t = 5); para ficar ≤ 1, é preciso ε ≲ 0,005. Para comparação, (c/2)W(0) ≈ 81 para p = 2
  e ≈ 70 para p = 131.
- Majorando |W(t ± log n)| pela queda lateral O(L⁻²|ω|⁻³) e usando Σ_{log n≤U} Λ(n)n^{−1/2} ~ 2e^{U/2}, a soma dos
  módulos com amortecimento é da ordem de e^{1/(8ε²)}: 10²² para ε = 0,05 e 10²¹⁷¹ para ε = 0,005.

**Conclusão moderada:**
- Com **essa** cota absoluta não se obtém um enunciado "linhas + erro controlado" para a observável sem suavização.
- Isso **não** demonstra que toda abordagem rigorosa precise de estimativas de cancelamento do tipo usado para S(t).
  Outras rotas (mollifiers diferentes, janelas adaptadas, estimativas médias em t) não foram examinadas.
- N3 continua classe **B**.

### 2.4 Estado de L-EF2

| Subitem | Conteúdo | Situação |
|---|---|---|
| L-EF2a | identidade com a contagem completa; identificação com a tabela; termo determinístico integrado | (a1) derivação, com fórmula de contagem secundária e ressalva; (a2) completude B nos 30 blocos, criticidade e simplicidade PC; (a3) cota ≤ 8,6·10⁻⁸ |
| L-EF2b | versão suavizada com fator 2, termo de linha, restos R_ε com prefatores e soma sobre zeros distantes | derivação; condicionada a L-EF1 (classe de funções-teste PC), a H₀ (Platt–Trudgian, PC) e a uma cota explícita de contagem (PC) |
| L-EF2c | originalmente "passagem ε → 0 com erro controlado"; hoje decomposto em H1: limite gaussiano (S3b) × truncamento finito (S1, S3a, S2-ratio′) | limite gaussiano **derivado condicionalmente** (S3b); truncamento finito **aberto** (S1, S3a); S2-ratio′ com condição suficiente **certificada só sob RH, para M^math, em U₂ = 15** (§II.20 da Cauda Projetada); a cota absoluta de §2.3 não fecha; **H1 aberta** |

## 3. C02 — integrais locais de Connes

**Avaliação** (`derivacao` sobre Connes App. II, p. 69, eqs. 8–9; p. 78–79, normalização): para F dependente só de
\|u\| e lugar finito p,

Pfw ∫_{ℚ_p*} F(\|u\|) \|u\|^{1/2} \|1−u\|⁻¹ d*u = log p Σ_{m≥1} p^{−m/2} [F(p^m) + F(p^{−m})].

**Consequências:**
- Com F(eˣ) = g(x): contribuição −2 log p Σ_m p^{−m/2} g(m log p) na fórmula de Weil (§1.2).
- Na linguagem de C02, a órbita H_p (isotropia ℚ_p*) contribui com "período primitivo" log p (massa da camada de
  Haar) e amplitude p^{−m/2} na m-ésima camada. O fator 1/\|1−u\| vale 1 ou \|u\|⁻¹ fora da camada unitária, e a
  camada unitária é anulada pela prescrição Pfw.

**Escopo:**
- Vale para o Teorema 1 de Weil na forma de Connes (distribuição Δ com Pfw).
- A igualdade com a prescrição ∫' do Teorema V.3 é o Lema 2 (p. 72–73, caso não arquimediano), com o caractere
  normalizado (22).
- Teorema 6 (p. 77–78): h com suporte compacto em C_k.
- O caso global "como traço" continua condicional (C02 inalterada quanto a isso).

## 4. C11/C19 — corpos de funções e convenção de Frobenius

| Tentativa | Resultado |
|---|---|
| Milne, *Lectures on Étale Cohomology* (jmilne.org) | conexão recusada (curl e WebFetch), 14/09/2026 08:55 e ~09:00 |
| Deligne, *La conjecture de Weil I* (Numdam) | conexão recusada, ~09:00 |
| alternativas no arXiv | conexão recusada, ~09:00 |

**Situação:** continua **PC**. A transformação algébrica registrada em C19 (P₁(T) = det(I − TF | H¹), zeros em T =
α_j⁻¹, T = q^{−s}) permanece como está. A convenção de Frobenius (geométrico × aritmético) **não** foi conferida.

**Próxima tentativa:** repetir o download quando os servidores estiverem acessíveis e arquivar com SHA-256.

## 5. Efeitos nos documentos

- **Plano:**
  - §3.1: estado de L-EF1 (parcial: estrutura derivada; termo arquimediano B; classe de funções-teste PC).
  - §3.2: L-EF2 dividida em a/b/c, com c aberta.
  - §2.1 M3: citação da fórmula de contagem corrigida.
- **Correspondências:**
  - C02: avaliação p-ádica deixa de ser PC e passa a `derivacao`.
  - C09: fator 2 e sinal do termo primo derivados; o termo arquimediano não entra em C09. A comparação com Selberg
    continua analogia; `conferencia` passa de PC para `derivacao`.
- **Matriz:**
  - K5a M4/N3 continuam PC. A derivação de incompatibilidade de sinal fica desbloqueada quanto às constantes, mas não
    foi feita nesta entrega.
  - §0.3 atualizada.
- **Evidências:** E-LEF1-W, E-LEF1-NUM, E-C02, E-NT.

## 6. Revisão 11.3b-2 (auditoria de 14/09/2026)

| # | Ponto | Tratamento |
|---|---|---|
| 1 | Stieltjes: contagem completa × tabela; erro integrado do termo determinístico | (a1) identidade para todas as ordenadas com multiplicidade; (a2) completude da tabela conferida nos 30 blocos (classe B, `check_table_completeness`), com criticidade e simplicidade PC; (a3) cota integrada sup\|Δ\|·L/2 ≤ 8,6·10⁻⁸ (`density_error_bound`) |
| 2 | Fator 2 da simetrização | Σ k_t = 2D_t sob criticidade até H₀; divisão por 2 explícita nos termos de polo, suave e de primos; termo de linha derivado com o fator ½ e o conjugado; comparação f_t × h_ε feita no lado unilateral, com a parte refletida limitada separadamente |
| 3 | Zeros distantes | Cota da soma com prefatores da convolução (2L(2πε²)^{−1/2}), fator e^{y²/(2ε²)}, contagem N(T) ≤ T² (PC) e agrupamento. H₀ separa a cauda e não a elimina. Platt–Trudgian registrado pela referência editorial, texto não lido (403) |
| 4 | Checagem gaussiana sem orçamento | Orçamento estimado (ordenadas, caudas de zeros e de primos, quadratura) acrescentado. O resíduo cabe no orçamento; interpretação restrita a consistência (B), não precisão certificada |
| — | Conclusão de L-EF2c | Moderada: a cota absoluta utilizada não fecha; não se afirma necessidade de estimativas de cancelamento para toda abordagem. **Atualização 11.3b-26:** o limite ε → 0 existe condicionalmente (S3b); o aberto é o truncamento finito (S1, S3a, S2-ratio′), com a decomposição em três termos; ver §2.3 |

## 7. Revisão 11.3b-3: qualificações e registro de fontes pendentes

- **E_quad** passa a ser descrita como estimativa de estabilidade numérica, não cota garantida.
- O **supremo numérico de Δ** fica como estimativa B. Foi acrescentada uma cota certificada (módulo DLMF §5.11(ii)),
  sem maximização numérica.
- **Três níveis distinguidos no texto:**
  - derivação condicional: identidades (a1) e (b), restos R_ε;
  - verificação numérica B: completude da tabela, checagem gaussiana, estimativa de Δ;
  - cota certificada: só (a3), módulo a cota de resto da DLMF.
- **Fontes e hipóteses pendentes:** consolidadas em [ETAPA11_PENDENCIAS_FONTES.md](ETAPA11_PENDENCIAS_FONTES.md),
  com o registro das tentativas de acesso. Nenhum cálculo gaussiano adicional foi feito.
