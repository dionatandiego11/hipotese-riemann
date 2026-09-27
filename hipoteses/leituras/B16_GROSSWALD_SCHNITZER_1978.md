# B16 — Grosswald & Schnitzer (1978), *A class of modified ζ and L-functions*

**Referência.** E. Grosswald e F. J. Schnitzer, Pacific J. Math. 74 (1978), n.º 2 — PDF p. i = revista p. 355 + i (a
p. 3 do PDF é a p. 358 da revista). 11 pp. no PDF, incluindo capa e expediente. **Cópia local:**
`archive/fontes_etapa11/hipoteses_20260925/grosswald_schnitzer.pdf`, SHA-256 `a311d5b7…`. **Lido por inteiro**;
Teoremas 1 e 2 conferidos na imagem (p. 358). As desigualdades do Lema 2 e o miolo da prova do Lema 1 foram lidos, não
auditados linha a linha.

## O que o texto afirma

| item | página (revista) | conteúdo |
|---|---|---|
| **Teor. 1** | 358 | escolha q_n com p_n ≤ q_n ≤ p_{n+1} e forme ζ\*(s) = Π(1 − q_n^{−s})^{−1}. Então ζ\*(s) ≠ 0 em σ > 1, continua meromorficamente a σ > 0, tem um único polo em s = 1 com resíduo r, 1/2 ≤ r ≤ 1, e **em σ > 0 tem exatamente os mesmos zeros, com as mesmas multiplicidades, que ζ(s)**. Vale também com p_n ≤ q_n para n ≥ n₀ e p_n/q_n → 1 |
| **Teor. 2** | 358 | para χ mod k, inteiros q_n com p_n ≤ q_n ≤ p_n + K e q_n ≡ p_n (mod k): L\*(s, χ) = Π(1 − χ(q)q^{−s})^{−1} continua a σ > 0 com **exatamente os mesmos zeros** que L(s, χ) |
| mecanismo | 359–361 | ζ\* = φ ζ, com φ(s) = Π(1 − p^{−s})/(1 − q^{−s}) absolutamente convergente e **sem zeros** em σ > 0 (Lema 1), usando a cota de lacunas entre primos p^{3/5+ε} (Montgomery, LNM 227) |
| §5 | 362 | em geral ζ\* **não** tem equação funcional, e as q_n podem ser escolhidas de modo que σ = 0 seja fronteira natural: ζ e ζ\* partilham todos os zeros complexos com caráter analítico inteiramente diferente |
| §6 | 362–363 | aplicações sugeridas (teorema de Turán sobre somas parciais; o ideal das funções holomorfas em σ > 0 com os zeros de (s − 1)ζ(s)); os autores dizem que pretendem voltar ao tema |

## Para o projeto — consequência de interpretação, sem CPU

- **O conjunto dos zeros, sozinho, não determina os primos.** Existem incontáveis "produtos de Euler" com primos
  deslocados (q_n entre p_n e p_{n+1}) que têm exatamente os mesmos zeros de ζ em σ > 0 — e, pelo Teorema 2, o mesmo
  vale para L(s, χ), que é o nosso controle de Dirichlet.
- Isso **não** contradiz o instrumento: ele recupera log p, e não log q_n, porque usa a **fórmula explícita de ζ**, que
  depende da equação funcional e do fator arquimediano (o termo suave). ζ\* não tem equação funcional nem fórmula
  explícita do mesmo tipo.
- **Qualquer frase do tipo "os zeros codificam os primos" precisa da qualificação:** dado o fator gama e a equação
  funcional da classe. É uma afirmação **A** sobre o alcance da espectroscopia inversa, útil para a redação de
  resultados e de um eventual artigo.

Rótulos: Teoremas 1 e 2, **A** (prova lida, lemas não auditados); a consequência interpretativa, **A** (leitura direta
dos enunciados).

*Leitura de 25/09/2026, Claude Opus.*
