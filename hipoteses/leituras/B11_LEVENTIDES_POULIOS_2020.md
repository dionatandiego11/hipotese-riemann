# B11 — Leventides & Poulios (2020), *Koopman operators and the 3x+1-dynamical system*

**Referência.** John Leventides e Costas Poulios, arXiv:2010.12987v1 [math.DS], 24/10/2020 — única versão listada no
arXiv na consulta de 25/09/2026. 37 pp. Publicação em periódico **não conferida**.
**Cópia local:** `archive/fontes_etapa11/koopman_20260925/leventides_2010.12987.pdf`, SHA-256 `4754a246…`,
554.824 bytes (fora do git; registro em `aquisicao.json` ao lado e no `MANIFESTO.csv`).

**O que foi lido.** Enunciados de todas as seções (pp. 1–37). Provas lidas nas §§2, 4 e 5 e na §6 até o Teorema 6.7
(pp. 3–18), e na §7 até o Teorema 7.7 (pp. 18–25). §§8–10 (pp. 25–36): definições e enunciados, provas **não
auditadas**. Texto extraído com `pdftotext`; as fórmulas foram conferidas no texto extraído, não na imagem da página.

## 1. O que o artigo faz

| seção | páginas | conteúdo |
|---|---|---|
| §1 | 1–3 | mapa T(n) = n/2 ou (3n+1)/2 em ℕ* — **mesma convenção da CL0**; Koopman K(g) = g∘S (p. 2) |
| §2 | 3–7 | Teor. 2.1 (p. 3): T^k(n) pelo vetor de paridades (é o A6 da CL0). Prop. 2.2 (p. 3): a k-ésima paridade é periódica em n com período 2^k (atribuído a Everett). Teor. 2.4 (p. 4): as paridades de comprimento k de n mod 2^k percorrem ℤ₂^k. Teor. 2.5 (p. 5): Σₙ T^k(n) xⁿ é racional, com polos nas raízes 2^k-ésimas da unidade |
| §3 | 7–8 | revisão de resultados de densidade (Terras, Everett, Allouche, Korec, Tao) |
| §4 | 8–11 | operadores em ℓ^p, 1 ≤ p ≤ ∞: "forward" L_{T,p} e "backward" B_{T,p}. **Teor. 4.2 (p. 9): ‖L_{T,p}‖ = 2^{1−1/p}**. **Teor. 4.3 (p. 10): L\*_{T,p} = B_{T,q}**, com ‖B_{T,p}‖ = 2^{1/p} |
| §5 | 11–13 | c_n = max_m \|T^{−n}(m)\|. Prop. 5.3 (p. 12): n ≤ c_n ≤ F_n (Fibonacci, F₀ = 1, F₁ = 2). Teor. 5.4 (p. 12): ‖L^n_{T,p}‖ = c_n^{1−1/p}. **Cor. 5.5 (p. 13): 1 ≤ ρ(L_{T,p}) ≤ φ^{1−1/p}**, com ρ(L_{T,1}) = 1. Obs. 5.6 (p. 13): cota inferior só polinomial, c_n ≥ (n+1)(n+2)/4 |
| §6 | 14–18 | média de Cesàro K em ℓ¹; Lema 6.1 e Teor. 6.2 (pp. 15–16) **sob a hipótese de não haver trajetória divergente** — o próprio texto nota (p. 15) que a média ignora trajetórias divergentes. Teor. 6.7 (p. 17): autoespaço de λ = 1 de L_{T,1} = fecho do span dos indicadores de ciclos. Teor. 6.9 e Cor. 6.10 (p. 18): λ = −1 ↔ ciclos de comprimento par |
| §7 | 18–25 | Prop. 7.1 (pp. 18–19): a sequência de sinais (−1)^{T^k(n)} em k é eventualmente periódica ⟺ a órbita atinge um ciclo. Cor. 7.3 (p. 20): Collatz ⟺ todas eventualmente de período 2. Lema 7.4 (p. 20; prova na ref. [12]) e Teors. 7.5–7.6 (pp. 20–23): **DFT na variável n**, para profundidade k fixa, sobre um antiperíodo de comprimento 2^k, nas raízes de z^{2^k} = −1, com norma ℓ² igual a 1 |
| §§8–9 | 25–31 | operadores A_k: V_k → V_{k+1}; Teor. 8.8 (p. 28): M_k M_k\* = I; isometria S de tipo deslocamento em V∞ ≅ ℓ² (Teor. 8.11, p. 30). Prop. 9.1 (p. 30): **parte unitária da decomposição de Wold é nula**; Obs. 9.2 (p. 31): os autores dizem que isso é "infeliz" e que outro operador talvez tivesse parte unitária não nula |
| §10 | 31–36 | funcionais na C\*-álgebra da isometria, comparando correlações das sequências de sinais com as de um "deslocamento ideal"; Teor. 10.3 (p. 36): Collatz ⟺ existe f ∈ Inc com φ_f = 0. São **reformulações equivalentes**; os autores não afirmam ter resolvido a conjectura |

## 2. Rótulos e pontos a conferir

Os resultados do artigo entram como **A** (preprint; enunciados lidos; provas das §§2, 4 e 5 conferidas na leitura),
com o estatuto de revisão por pares não conferido. Três pontos a conferir — **não são afirmações de erro**:

1. **Notação na definição (p. 8).** A linha de definição escreve L_{T,p}(x) = x∘T, mas as fórmulas explícitas que se
   seguem (a_{3k+2} = x_{6k+4} + x_{2k+1}; L(e_n) = e_{T(n)}, pp. 8–9) são a soma sobre pré-imagens, isto é, o
   operador de transferência. A composição x∘T é B_{T,p} (p. 10). Os teoremas usam as fórmulas explícitas.
2. **Teorema 6.7 (p. 17)** é enunciado sem hipótese, mas a prova (p. 18) usa K(v) = v e o Lema 6.1, que supõe
   ausência de trajetória divergente.
3. **Corolário 6.8(1) (p. 18)** diz que o problema 3x+1 equivale a dim E₁ = 1. dim E₁ = 1 significa um único ciclo; a
   direção "dim E₁ = 1 ⇒ Collatz" precisaria excluir trajetórias divergentes, que o texto (p. 15) diz serem invisíveis
   à média. Na minha leitura, a equivalência vale para "o único ciclo é o trivial", não para a conjectura inteira.
   **A confirmar** antes de citar o corolário em qualquer sentido.

## 3. Sobreposição com a CL0

- O operador de contagem 𝓛₊ da CL0 (`results/collatz_cl0/ESPECIFICACAO_CL0_v1.md`, l. 98) **é** o L_{T,p} de LP
  (p. 8). O Koopman U da CL0 (l. 97) é o B_{T,2}. A relação 𝓛₊ = U\* (CL0, l. 102) é o **Teorema 4.3** (p. 10).
- O fato **A8** da CL0 (l. 81; Anexo A, ll. 242–246) — ‖𝓛₊‖_{ℓ¹} = 1, ‖𝓛₊‖_{ℓ²} = √2, ‖𝓛₊‖_{ℓ^∞} = 2, e
  ≤ 2^{1−1/p} por Riesz–Thorin — **é o Teorema 4.2** (p. 9), que dá a **igualdade** ‖L_{T,p}‖ = 2^{1−1/p} para todo p.
  A CL0 apresenta isso como "derivação própria" e **não cita LP**. A derivação da CL0 vale como reprodução
  independente (B); o fato é conhecido (A, LP 2020) e precisa da citação. Isso entra junto da correção da CL0 que o
  usuário vai registrar.
- O que a CL0 tem e LP não têm: todo o lado 2-ádico — ℤ₂, medida de Haar, a conjugação Φ de Bernstein–Lagarias e a
  involução Ω de Monks–Yazinski. LP trabalham só em ℕ e não citam nenhum dos dois.

## 4. Triagem

- **Instrumento espectral (zeros): fora do domínio.** A "análise de Fourier" de LP é uma DFT na variável do ponto
  inicial n, para profundidade k fixa — não é o espectro de uma sequência de níveis. Não há previsão mensurável pela
  nossa régua. Proposta de registro: **F-004, fora do domínio**, como F-001 e F-002.
- **Frente Collatz: "Koopman/Fourier em Collatz" não é contribuição por si**, o que confirma a observação do usuário
  de 25/09/2026. Qualquer pergunta nova precisa ser distinta das de LP.
- **Pergunta que LP deixam aberta, registrável como candidata — não como achado.** Pelo Teorema 5.4,
  ρ(L_{T,p}) = (lim c_n^{1/n})^{1−1/p}, e LP só provam 1 ≤ lim c_n^{1/n} ≤ φ, com cota inferior para c_n apenas
  polinomial (Obs. 5.6). Decidir se c_n cresce exponencialmente — se existe m com número exponencial de pré-imagens em
  profundidade n — fixaria ρ(L_{T,p}) > 1 para p > 1. **Antes de qualquer declaração:** busca registrada sobre o
  tamanho das árvores inversas de 3x+1. Há trabalhos de Applegate e Lagarias sobre isso, **não lidos**; não afirmo o
  que dizem. A resposta pode já estar na literatura, e nesse caso a pergunta entra como reprodução. Custo: zero de CPU
  na parte bibliográfica.

## 5. Não obtido

- *An operator theoretic approach to the 3x + 1 dynamical system*, IFAC-PapersOnLine (2021), ScienceDirect
  S2405896321005371 — não baixado, não lido; autoria a confirmar.
- J. Leventides, *A new embedding of the 3x+1 dynamical system* (ref. [12], onde está a prova do Lema 7.4) — não obtido.

*Leitura de 25/09/2026, Claude Opus, para o caderno de hipóteses.*

## Atualização (25/09/2026, mesma data) — a pergunta candidata do §4 já está respondida

A leitura B12 (Kontorovich–Lagarias 2009, `B12_KONTOROVICH_LAGARIAS_2009.md`) mostra que o crescimento exponencial de
c_n já é conhecido desde 1995: N\*_k(a) ≥ (1,302053)^k para a ≢ 0 (mod 3) fixo e k grande (Teor. 2.4, p. 15,
atribuído a Applegate–Lagarias, Math. Comp. 1995). Combinado com o Teorema 5.4 daqui, dá
ρ(L_{T,p}) ≥ (1,302053)^{1−1/p} para p > 1 — melhora imediata da Cor. 5.5, sem novidade publicável. A candidata fica
**descartada como já respondida**. O texto acima fica como estava, para registro do que a leitura B11 concluiu antes
desta.

## Atualização 2 (25/09/2026) — cota rigorosa com fonte lida

Lagarias–Weiss (1992, p. 243; leitura B17) provam, de forma elementar, N\*(k, m) ≥ 2^{⌊k/4⌋} para todo m ≢ 0 (mod 3).
Com o Teorema 5.4 daqui, ρ(L_{T,p}) ≥ 2^{(1−1/p)/4} para p > 1, com toda a cadeia em textos lidos. A cota melhor,
(1,302053)^{1−1/p}, continua dependendo do artigo da Math. Comp. (1995), não obtido.
