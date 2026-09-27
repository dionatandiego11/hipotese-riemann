# B12 — Kontorovich & Lagarias (2009), *Stochastic Models for the 3x+1 and 5x+1 Problems*

**Referência.** Alex V. Kontorovich e Jeffrey C. Lagarias, arXiv:0910.1944v1, 11/10/2009, 66 pp. A versão em livro
(*The Ultimate Challenge: the 3x+1 problem*, AMS, 2010) **não foi conferida**.
**Cópia local:** `archive/fontes_etapa11/koopman_20260925/kontorovich_lagarias_0910.1944.pdf`, SHA-256 `9648fd7c…`,
823.579 bytes (fora do git; `aquisicao.json` ao lado e `MANIFESTO.csv`).

**O que foi lido.** §§2.5–2.6 (pp. 14–17, com a Tabela 4 na p. 16) e §6 até o fim de §6.1 (pp. 33–36). As pp. 15 e 35
foram conferidas **na imagem da página**, porque a extração de texto perdeu as frações (mesmo problema do caso H-002).

**Por que este texto.** A leitura B11 (Leventides–Poulios) deixou uma pergunta candidata: se c_n = max_m |T^{−n}(m)|
cresce exponencialmente. Este levantamento traz o estado da literatura exatamente sobre essa quantidade. O original de
cada resultado **não** foi obtido (ver §4); o que segue é o que o levantamento, escrito por um dos autores dos
originais, afirma.

## 1. O que o texto afirma, com páginas

| item | página | conteúdo |
|---|---|---|
| Def. 2.8 | 14 | N_k(a) := \|{n : T^{(k)}(n) = a}\| — **é o \|A^k_a\| de Leventides–Poulios**; N\*_k(a) conta só n ≢ 0 (mod 3) ("árvore podada"); cadeia N\*_k ≤ N_k ≤ Σ_{j≤k} N\*_j ≤ (k+1) N\*_k |
| (2.17) | 15 | cota trivial N_k(a) ≤ 2^k |
| Def. 2.9 | 15 | constante de crescimento δ₃(a) := limsup (1/k) log N_k(a); δ₃(3a) = 0, porque N_k(3a) = 1 |
| **Teor. 2.4** | 15 | **para todo a ≢ 0 (mod 3) fixo e todo k suficientemente grande, (1,302053)^k ≤ N\*_k(a) ≤ (1,358386)^k** — atribuído a Applegate e Lagarias, *Density Bounds for the 3x+1 Problem I*, Math. Comp. 64 (1995), Teorema 1.1, "por indução simples usando a tabela" |
| Tabela 4 | 16 | N^±_k (máximo e mínimo de N\*_k(a) sobre as classes a mod 3^{k+1}) para k ≤ 30, normalizados por (4/3)^k: D⁺₃₀ ≈ 1,748, D⁻₃₀ ≈ 0,491 |
| previsão do modelo | 15 | δ₃(a) = log(4/3) para todo a ≢ 0 (mod 3) |
| Teor. 6.1 | 34–35 | N\*(k, a) depende só de a mod 3^{k+1}; a soma sobre as 2·3^k classes é 2·4^k, logo a média é exatamente (4/3)^k |
| Conj. 6.1 | 35 | δ₃(a) = log(4/3) (Lagarias–Weiss) |
| Conj. 6.2 | 35 | máximo e mínimo, N^±_k, com crescimento (4/3)^{k+o(k)} — ver o ponto de atenção 1 |

## 2. Pontos de atenção na fonte

1. **Erro tipográfico na Conjectura 6.2 (p. 35, conferido na imagem):** está impresso N^±_k = (3/4)^{k+o(k)}. Isso
   faria as contagens decaírem, o que contradiz a Tabela 4 (N⁺₃₀ = 9.788) e a Conjectura 6.1, que ela deveria
   implicar. O valor pretendido é **(4/3)^{k+o(k)}**. Conferir no original (Applegate–Lagarias, Exp. Math., Conjecture C).
2. A p. 35 diz que o cálculo foi feito "para k ≥ 30"; a p. 15 diz "k ≤ 30", que é o que a Tabela 4 mostra.
3. A paginação do artigo sobre árvores diverge: 101–117 na lista de referências do levantamento, 193–209 no resultado
   de busca. A conferir.

## 3. Consequência para a pergunta deixada pela leitura B11

A pergunta **já está respondida na literatura**, desde 1995, e Leventides–Poulios (2020) não citam esse resultado.

- **Cota inferior, rigorosa.** Pelo Teorema 5.4 de Leventides–Poulios (p. 12), ‖L^n_{T,p}‖ = c_n^{1−1/p}. Como
  c_n ≥ N_n(1) ≥ N\*_n(1) e, pelo Teorema 2.4 com a = 1, N\*_n(1) ≥ (1,302053)^n para n grande, a fórmula de Gelfand dá
  **ρ(L_{T,p}) ≥ (1,302053)^{1−1/p} para 1 < p ≤ ∞**, contra a cota inferior 1 da Cor. 5.5 deles. Pela dualidade
  (Teor. 4.3 e Cor. 5.7 deles), ρ(B_{T,p}) ≥ (1,302053)^{1/p} para 1 ≤ p < ∞.
- **Cota superior.** Continua φ^{1−1/p} (Leventides–Poulios). Melhoraria para (1,358386)^{1−1/p} **se** a cota
  superior de Applegate–Lagarias valer uniformemente em a — o que é plausível, porque N\*_k(a) só depende de a mod
  3^{k+1}, mas o enunciado relatado é "para a fixo, k grande", e sem o original não afirmo a uniformidade.
- **Condicional à Conjectura 6.2** (com 4/3): ρ(L_{T,p}) = (4/3)^{1−1/p}.

**Rótulos.** Teoremas 2.4 e 6.1: **A**, via o levantamento de um dos autores (original não lido). Conjecturas 6.1 e
6.2: **D**. A cota ρ(L_{T,p}) ≥ (1,302053)^{1−1/p}: **A** — combinação imediata de dois resultados publicados, feita
aqui. **Não é novidade que justifique publicação**; é uma observação que fecha a candidata.

## 4. Não obtido

- Applegate e Lagarias, *Density Bounds for the 3x+1 Problem I. Tree-Search Method*, Math. Comp. 64 (1995), 411–426 —
  fonte do Teorema 2.4. `ams.org` respondeu 403 daqui em 25/09/2026. O acervo antigo da Math. Comp. costuma ser aberto
  no navegador; se o usuário baixar, confiro o enunciado exato e a uniformidade.
- Applegate e Lagarias, *(On) the distribution of 3x+1 trees*, Experimental Math. 4 (1995) — fonte da Conjectura 6.2.
  `websites.umich.edu` respondeu 403 (inclusive para o PDF de Bernstein–Lagarias baixado mais cedo no mesmo dia),
  Project Euclid devolveu página anti-robô e Taylor & Francis é pago.

*Leitura de 25/09/2026, Claude Opus, para o caderno de hipóteses.*

## Atualização (25/09/2026) — pontos de atenção conferidos no original

Com o artigo de Applegate e Lagarias sobre árvores, obtido pelo usuário (leitura `B13_APPLEGATE_LAGARIAS_1995_TREES.md`):

- **Ponto 1, confirmado:** a Conjectura 6.2 daqui é a Conjectura C do original (p. 197, conferida na imagem), que diz
  **(4/3)^{k(1+o(1))}**. O (3/4) impresso aqui é erro tipográfico.
- **Ponto 3, resolvido:** a paginação correta é Exp. Math. 4 (1995), n.º 3, **193–209**.
- **Continua aberto:** o Teorema 2.4 (as cotas 1,302053 e 1,358386) **não** está no artigo das árvores; é do artigo da
  Math. Comp. (Density bounds I), ainda não obtido. A cota inferior do raio espectral continua dependendo dele.
