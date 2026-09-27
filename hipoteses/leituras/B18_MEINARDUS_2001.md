# B18 — Meinardus (2001), *Some Analytic Aspects Concerning the Collatz Problem*

**Referência.** G. Meinardus, *Some Analytic Aspects Concerning the Collatz Problem*, Mannheimer Manuskripte
Nr. 261/2001, Fakultät für Mathematik und Informatik, Universität Mannheim. Registro institucional:
https://madoc.bib.uni-mannheim.de/1608/.
**Cópia local:** `archive/fontes_etapa11/ponte_collatz_20260925/meinardus_2001_mannheim261.pdf`, SHA-256
`08ebcc73…`, 15 pp. (capa + pp. 1–14), 645.872 bytes. Escaneado (produtor "Eastman Kodak"), com camada OCR de
baixa qualidade. Obtido pelo usuário via Tor em 25/09/2026 (o acesso direto dava 403/antibot; ver
`aquisicao.json` e `tentativas_pagina_autor.json` na mesma pasta). PDF p. i = p. impressa i − 1.

**O que foi lido:** o texto inteiro pela camada OCR; **conferidas nas imagens** as pp. impressas 2, 4, 5, 6, 9, 10 e 12
(definições, Teoremas 1–5, fórmulas (5)–(8), (11), (16)–(17)). As demonstrações dos Lemas 1–2 (pp. 6–8) e a §5 (p. 13)
foram lidas apenas pelo OCR.

## 1. O que o texto afirma

τ(n) = n/2 (n par), (3n+1)/2 (n ímpar). A = sequências reais limitadas; B ⊂ A, coeficientes em {0, 1}; a_τ = (a_{τ(ν)}).

| item | página | conteúdo |
|---|---|---|
| **Teor. 1** | 2–3 | Equivalentes: (i) Collatz; (ii) as únicas soluções de a = a_τ em A são as constantes; (iii) as únicas soluções em B são 0 e 1. Prova: se Collatz vale, a_n = a_{τ^m(n)} = a_1. Se falha, M = {ν : τ^k(ν) ≠ 1 ∀k} ≠ ∅ é τ-invariante e o indicador de M resolve (3) |
| (5) | 4 | D_τ(s) = Σ a_{τ(n)} n^{−s} = 2^{−s} D(s) + (TD)(s), com **(TD)(s) = Σ_{ν≥0} a_{3ν+2} (2ν+1)^{−s}**, Re s > 1 (conferido: n = 2ν+1 ímpar ⇒ τ(n) = 3ν+2) |
| **Teor. 2** | 4–5 | Em B̂ (séries com coeficientes em {0,1}), Re s > 1: Collatz ⟺ **D(s) = (1−2^{−s})^{−1}(TD)(s)** (6) tem como única solução não trivial D = ζ. Contraexemplo ⇒ solução Σ_{ν∈M} ν^{−s} ≠ ζ |
| Teor. 3 | 5–6, 9 | Representação de Perron: (TD)(s) = (2πi)^{−1} ∫_(γ) D(v) F(v, s) dv, Re s > γ > 1, com F(v, s) = ∫_{−1/2}^{1/2} Σ_n (3n+2+ω)^{v−1}(2n+1)^{−s} dω, Re s > Re v (8). A prova toma x = 3m+5/2 e x = 3m+3/2 no Lema 2 e isola a_{3m+2} |
| Lemas 1–2 | 6–9 | Fator descontínuo de Dirichlet e fórmula de Perron com Σ\* (meio peso em x inteiro) |
| **Teor. 4** | 10–11 | F(·, s) continua meromorficamente a Re s > Re v − 1; única singularidade: polo simples em s = v com resíduo **3^{v−1}/2^v**. Recorrência (13): φ(v, s) = (2/3) φ(v−1, s−1) + (ω+1/2) φ(v−1, s) |
| Teor. 5 | 12 | φ(−v, s) = Γ(v+1)^{−1}Γ(s)^{−1} ∬ x^v y^{s−1} e^{−(2+ω)x−y}/(1 − e^{−3x−2y}) dx dy em Ĝ = {Re v > 1, Re s > 2}. O autor sugere, **sem desenvolver**, continuação e estimativas "por métodos de Riemann" |
| §5 | 13 | Para f(n) = (3n−1)/2 (ímpar) — o problema 3x−1 —, com três ciclos conhecidos, conjectura núcleo de dimensão 3. Pergunta aberta para τ(n) = (an+b)/2: quando a dimensão do núcleo é finita? |

Conferi de forma independente o resíduo do Teor. 4: a cauda ∫^∞ (3t)^{v−1}(2t)^{−s} dt = 3^{v−1}2^{−s}/(s−v) + holomorfa
dá resíduo 3^{v−1}2^{−v} em s = v; a integral em ω, de comprimento 1, não o altera.

## 2. Pontos de atenção

1. **Índice em (8), p. 6:** a soma está impressa a partir de n = 1, mas (5) e a prova do Teor. 3 (p. 9, conferida)
   usam m = 0. Com n = 1, o termo a_2·1^{−s} se perderia. Tratar como **erro tipográfico por n = 0**. A prova do
   Teor. 4 (p. 10) já usa m = 0.
2. **Justificativa de Perron incompleta.** O Lema 2 troca soma e integral numa reta infinita invocando
   convergência uniforme em compactos, o que não basta: a integral é só condicionalmente convergente. O enunciado do
   Lema 2 é a fórmula de Perron clássica e vale para coeficientes limitados e γ > 1. Já a troca Σ_m ↔ ∫_(γ) no Teor. 3
   **não foi auditada**; a representação (7) fica como plausível, não conferida.
3. **"Núcleo de dimensão 1".** O resumo usa essa expressão, mas o Teor. 2 é enunciado em B̂, que não é um espaço
   vetorial. A versão linear decorre do Teor. 1(ii) e da unicidade dos coeficientes de Dirichlet: em Â, o núcleo de
   D ↦ D − D_τ é a imagem das sequências limitadas τ-invariantes. Em geral, sua dimensão é o número de componentes
   da relação "órbitas se encontram" (ciclos não triviais e órbitas divergentes contam), e a dimensão 1 equivale a
   Collatz. A leitura do resumo é correta, mas a linguagem de dimensão não aparece no Teor. 2.
4. Na p. 12, a região G de (15) (Re v > 0, Re s > 0) difere de Ĝ no Teor. 5 (Re v > 1, Re s > 2); vale Ĝ.
5. A OCR troca τ por r, ζ por ((, ∈ por E. Não usar a camada de texto como fonte de fórmulas.

## 3. Diagnóstico para a ponte direta (P1 do plano)

É exatamente o cenário previsto na "Decisão" da rota 1 de `PLANO_PONTE_DIRETA_COLLATZ_RIEMANN.md`.

**(a) ζ entra como série da sequência constante, para qualquer mapa.** Para todo τ: ℕ → ℕ, a sequência constante 1
satisfaz a = a_τ. Logo ζ pertence ao núcleo de D ↦ D − D_τ **qualquer que seja τ**. Para Collatz, isso se reduz à
identidade Tζ(s) = Σ_{ν≥0}(2ν+1)^{−s} = (1 − 2^{−s})ζ(s), que vale sem hipótese. A escolha da base n^{−s} é
convencional: o próprio autor (p. 3) cita versões anteriores com séries de potências ([1], [2], [7]); nelas o
gerador seria 1/(1 − z), não ζ.

**(b) Os zeros de ζ não carregam informação sobre Collatz nesta construção.** Ambos os lados de (6) se anulam
identicamente nos zeros de ζ, independentemente da dinâmica; a identidade Tζ = (1−2^{−s})ζ se estende a todo ℂ por
continuação. O conteúdo de Collatz está só no **complemento**: a existência ou não de séries Σ_{ν∈M} ν^{−s}
τ-invariantes além de ζ. Os zeros de uma tal D_M hipotética não têm relação estabelecida com os de ζ.

**(c) Obstrução estrutural (heurística, rótulo D).** A informação sobre zeros de ζ vem do produto de Euler, isto é, da
multiplicatividade, somada à continuação e à equação funcional. O operador a ↦ a∘τ não respeita a convolução de
Dirichlet, pois τ não é multiplicativo: τ(3) = 5, τ(1) = 2 e τ(3·1) ≠ τ(3)τ(1). Portanto T não age no produto de
Euler. Para atingir o nível 2 do plano, seria preciso um ingrediente que ligue τ à estrutura multiplicativa; nada
em Meinardus faz isso. É um argumento de plausibilidade, não um teorema de impossibilidade.

**Rótulos.**
- (a) e (b): **A** — verificação elementar, sem hipóteses além de Re s > 1 para as séries e da continuação de ζ para
  a identidade estendida.
- Teor. 1–2 de Meinardus: **A** (prova conferida, curta e correta).
- Teor. 3: **A-parcial** (enunciado plausível, justificativa com lacuna).
- Teor. 4: **A** (resíduo reconferido; a continuação não foi reauditada linha a linha).
- (c): **D**.

**O que Meinardus deixa de genuinamente analítico:** o núcleo F(v, s), sua continuação (Teors. 4–5) e a pergunta da
§5 sobre dimensão do núcleo para τ(n) = (an+b)/2. Não há afirmação sobre zeros de ζ nem sobre RH.

## 4. Consequência para o plano

- **Nível 1 (relação funcional): conferido e conhecido desde 2001** (e, em forma de séries de potências, desde
  Berg–Meinardus 1994/1995). Reproduzi-lo não é novidade.
- **Nível 2 (zeros): esta construção não fornece caminho.** Pelo mecanismo (a)–(b), o que ela contém sobre ζ é
  independente de Collatz. Qualquer passo não tautológico (P2) precisa de uma propriedade que **mude ao trocar a
  regra** τ, como pede o controle de conteúdo da rota 2, e que interaja com a estrutura multiplicativa, conforme (c).
- **Convergência de rotas:** o objeto não trivial é o operador de composição a ↦ a∘τ, isto é, o operador de Koopman
  de Collatz — o mesmo de Leventides–Poulios (B11). A rota 1 desemboca na rota 3; não é uma via independente.
- **Candidata a P2 (pergunta, não conjectura):** existe um espaço de Hilbert de séries de Dirichlet (por exemplo, o
  H² de Hedenmalm–Lindqvist–Seip) em que D ↦ D_τ seja limitado, e cujo espectro, fora do autovalor trivial 1,
  dependa de τ de modo mensurável? Primeiro teste: a limitação. Não há nenhuma expectativa de que o espectro envolva
  zeros de ζ.
- **Citações posteriores — não lidas:** a busca de 25/09/2026 encontrou Berg–Meinardus, Results Math. 25 (1994) 1–12,
  e, como possíveis descendentes, "Functional Analysis Approach to the Collatz Conjecture" (Results Math., 2024,
  doi 10.1007/s00025-024-02167-7) e arXiv:2111.07882 (equações funcionais para mapas do tipo Collatz em corpos de
  números). Uma busca breve não estabelece ausência de trabalhos que usem ζ além do gerador trivial; permanece
  **pendente**.

*Leitura de 25/09/2026, Claude Opus.*

## 5. Varredura bibliográfica Collatz–Riemann (25/09/2026, segunda rodada)

Pergunta: há na literatura alguma ligação entre Collatz e ζ, ou os zeros de ζ, além do gerador trivial de Meinardus?
**Resultado: nenhuma encontrada.** É um resultado negativo de busca, não uma prova de ausência.

- **Bibliografias anotadas de Lagarias** (arXiv:math/0309224, 1963–1999, SHA-256 `99fd33f3…`; arXiv:math/0608208,
  2000–2009, `5bf53a2c…`; texto integral pesquisado): 0 ocorrências de "zeta" e "Riemann"; "Dirichlet" aparece uma
  vez, sobre teoremas tauberianos na tese de Fredman. Berg–Meinardus 1994/1995 constam; **Meinardus 2001 não
  consta** da parte II.
- **Mesma família, sem ζ:** Berg–Meinardus 1994/1995 (disco unitário; o gerador trivial é racional); Opfer
  (tentativa de prova pelo núcleo de Berg–Meinardus; versão para valores negativos na CMFT 2013); Neklyudov
  (arXiv:2106.11859; o índice de Id − 𝒯 em H²(D) limita o número de ciclos); Efrem (arXiv:2510.06736, equações
  funcionais por resíduos). Todos usam séries de potências ou operadores em H²(D), sem ζ.
- **Siegel** (arXiv:2111.07883, Parte I.5): aplica Perron a uma série de Dirichlet construída com a numen χ_q e
  obtém continuação meromorfa e equações funcionais. É o paralelo analítico mais próximo de Meinardus, mas o resumo
  não menciona ζ. O próprio autor diz que o crescimento hipergeométrico impede avaliar as integrais por resíduos.
  **Lida em 26/09/2026 → B20:** ζ entra como série da constante x; os zeros não têm papel; (2.25), (2.26) e os
  resíduos do Cor. 2 estão errados como impressos (corrigidos e verificados numericamente).
- **Obstrução relevante:** Bell–Lagarias, Acta Arith. 170 (2015). As funções geradoras das órbitas inversas de 3x+k
  têm o círculo unitário como fronteira natural para quase todo m; para 3x+1, Collatz equivale à racionalidade de
  f_{1,m} para m = 1, 2, 4, 8. ~~Isso bloqueia a continuação analítica que uma ponte com zeros exigiria nesse tipo de
  série.~~ **Retificado em 26/09/2026 (B19 §3):** a fronteira natural em z não obstrui a série de Dirichlet
  correspondente. Contraexemplo: m ≡ 0 (mod 3) dá fronteira natural (Fabry), mas D_m(s) = m^{−s}/(1−2^{−s}) é
  meromorfa em ℂ. O que importa para a rota 2 é a distribuição de O⁻(m) nos inteiros grandes (t → 0⁺ na
  transformada de Mellin).
- **Descartados, sem revisão ou fora do tema:** arXiv:2202.01064 (RH "quase certamente verdadeira", math.GM, não
  trata de Collatz); ResearchGate "Proof of the Riemann Hypothesis and the Modified Collatz Conjecture…"; páginas
  temáticas agregadas. Não entram como fonte.
