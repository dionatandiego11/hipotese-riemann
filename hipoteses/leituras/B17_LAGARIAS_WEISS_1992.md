# B17 — Lagarias & Weiss (1992), *The 3x+1 problem: two stochastic models*

**Referência.** J. C. Lagarias e A. Weiss, Ann. Appl. Probab. 2 (1992), n.º 1, 229–261.
**Cópia local:** `archive/fontes_etapa11/Lagarias&Weiss.pdf`, SHA-256 `dd83bfa9…`, 33 pp. É o escaneado do JSTOR, **só
imagem**, sem camada de texto; PDF p. i = revista p. 228 + i, completo (229–261). Obtido pelo usuário em 25/09/2026;
registro em `koopman_20260925/aquisicao.json` e no `MANIFESTO.csv`.

**Arquivo ao lado que não é fonte:** `archive/fontes_etapa11/Lagarias&Weiss.tex` (SHA-256 `78826206…`) é uma
**transcrição LaTeX de origem não registrada**, criada dez minutos depois do PDF. Já no resumo ela troca σ_∞ por σ_α.
Foi usada apenas como índice para localizar seções; **toda afirmação abaixo foi conferida na imagem da página**. Esse
`.tex` não está coberto pelo `.gitignore`.

**O que foi lido, nas imagens:** pp. 229–234, 242–248, 250, 253 e 255. A p. 243 foi ampliada a 140 e 300 dpi. As
demais páginas (235–241, 249, 251–252, 254, 256–261: provas da §2, parte da §4, §6 e referências) **não** foram lidas.

## 1. O que o texto afirma

| item | página | conteúdo |
|---|---|---|
| definições | 229–230 | tempo total de parada σ_∞(n); excursão máxima t(n); constantes γ (1.2), δ = limsup (log N_k)/k com N_k = #{n : σ_∞(n) = k} (1.3), e ρ; cotas triviais γ ≥ 3,72931 (1.4), ρ ≥ 1,58496 (1.5), δ ≤ log 2 |
| (1.6) | 230 | **0,17328 ≐ ¼ log 2 ≤ δ ≤ ½ log 3 ≐ 0,54931**, demonstrado na §3 |
| modelos | 231 | passeio aleatório imitando T mod 2^j; passeios aleatórios ramificados B[3^j] imitando T⁻¹ mod 3^j; (1.7) γ_RW = γ_BP ≐ 41,677647 |
| Conjecturas 1–3 | 231–232 | 1: γ = γ_RW = γ_BP. **2: lim (log N_k)/k existe e vale log(4/3)**. 3: ρ = 2 (o modelo dá ρ_RW = 2, Teor. 2.3) |
| Teor. 2.1 | 234 | no processo de passeios independentes, limsup σ_∞(ω_n)/log n = γ_RW q.c., com γ_RW solução de γ g(1/γ) = 1 |
| Lema 3.1 | 242 | (1/k) N(k) ≤ N\*(k) ≤ N(k): perder os nós ≡ 0 (mod 3) custa no máximo um fator k |
| **cota inferior** | **243** | **para todo m ≢ 0 (mod 3) e todo k: N\*(k, m) ≥ 2^{⌊k/4⌋}**, porque todo caminho na árvore podada encontra um ramo ao menos uma vez a cada quatro níveis: se n ≢ 0 (mod 3), algum de {n, 2n, 4n, 8n} é ≡ 2 ou 8 (mod 9). Daí (3.6): N(k) ≥ N\*(k) = N\*(k−2, 4) ≥ 2^{⌊(k−2)/4⌋} |
| cota superior | 243 | ver o ponto de atenção 1; com ela, (3.7): ¼ log 2 ≤ δ ≤ ½ log 3 |
| **Teor. 3.1** | 243–244 | Σ_{m mod 3^{k+1}, m ≢ 0 (mod 3)} N\*(k, m) = 2·4^k: a média é exatamente (4/3)^k — é o resultado que Applegate–Lagarias (B13, p. 197) citam como "Lagarias–Weiss, Teorema 3.1" |
| afirmação da matriz média | 247–248 | a matriz média E_j de B[3^j] tem autovalor máximo **4/3**, simples, com autovetor à esquerda e = (1, …, 1); o processo é supercrítico, positivamente regular e não singular |
| Cor. 3.1 | 248 | em B[3^j], lim (log N_k(ω))/k = δ_BP = log(4/3) q.c. |
| Teor. 3.3 | 248 | em B[1]: E[N_k] = (4/3)^k |
| variabilidade | 250 | árvores de 3x+1 de profundidade d têm no máximo 2·3^d estruturas distintas; as do modelo, pelo menos exp(exp(c_j d)) — **os modelos têm mais variabilidade que as árvores reais** (semente do achado de Applegate–Lagarias 1995, B13) |
| §5, Tabela 4 | 253–255 | dados até 10^11: γ(n) = σ_∞(n)/log n chega a ~32, abaixo dos 41,68 previstos; os autores ainda julgam os dados compatíveis com a Conjectura 1 |

## 2. Pontos de atenção

1. **Erro tipográfico no original (p. 243, conferido a 300 dpi):** a cota superior está impressa como
   **N\*(2k, m) ≤ 2^{k/2}**. A justificativa do próprio texto — toda árvore podada de profundidade 2 tem no máximo três
   ramos — dá **3^k**. A linha seguinte (N(k) ≤ k N\*(k) ≤ k·3^{(k+1)/2}) e a cota ½ log 3 de (3.7) também exigem 3^k.
   A versão impressa é ainda **refutada pelos dados** de Applegate–Lagarias (B13, Tabela 1): N⁺(30) = 9.788 > 2^{7,5} ≈ 181.
2. O σ_∞ do original aparece como σ_α na transcrição `.tex` — mais um motivo para ela não servir de fonte.

## 3. Consequência para a pergunta de B11 — agora com prova em mãos

A cota inferior da p. 243 é **uniforme em m** e vale para **todo k**, com prova elementar. Conferi o argumento de
forma independente: 2 é raiz primitiva mod 9 (ciclo 1, 2, 4, 8, 7, 5); os nós que ramificam na árvore podada são
exatamente os de resíduo 2 ou 8 (mod 9); e toda janela de quatro duplicações contém um desses resíduos. Então:

- c_n (Leventides–Poulios) ≥ N_n(1) ≥ N\*_n(1) ≥ 2^{⌊(n−2)/4⌋}, logo lim inf c_n^{1/n} ≥ 2^{1/4} ≐ 1,189;
- com o Teorema 5.4 deles, **ρ(L_{T,p}) ≥ 2^{(1−1/p)/4} para 1 < p ≤ ∞**, e, por dualidade, ρ(B_{T,p}) ≥ 2^{1/(4p)}.

É mais fraca que a cota (1,302053)^{1−1/p} de B12, mas **toda a cadeia agora está em textos lidos e conferidos**: a de
B12 dependia do artigo da Math. Comp., que continua não obtido. As cotas superiores de Lagarias–Weiss (√3 por nível)
são piores que o φ de Leventides–Poulios, que continua sendo a melhor.

**Rótulo:** A — combinação imediata de dois resultados publicados, com o argumento conferido. Não é novidade
publicável; fecha a pergunta de B11 com fonte lida.

## 4. Para o projeto

- **Instrumento espectral: nada.**
- **Frente Collatz:** o crescimento das árvores inversas tem **cota inferior rigorosa desde 1992** (2^{k/4}), cota
  melhor desde 1995 (1,302^k) e conjectura (4/3)^k com evidência forte. A pergunta deixada por Leventides–Poulios não
  tem espaço.
- **Nenhuma candidata nova.**

*Leitura de 25/09/2026, Claude Opus.*
