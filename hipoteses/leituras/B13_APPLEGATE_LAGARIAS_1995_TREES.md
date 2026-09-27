# B13 — Applegate & Lagarias (1995), *The Distribution of 3x+1 Trees*

**Referência.** David Applegate e Jeffrey C. Lagarias, *Experimental Mathematics* 4 (1995), n.º 3, pp. 193–209.
**Cópia local:** `archive/fontes_etapa11/koopman_20260925/applegate_lagarias_1995_trees.pdf`, SHA-256 `cc3df1ac…`,
316.651 bytes, 17 pp., layout da revista. **Obtida pelo usuário** em 25/09/2026; origem web não registrada. O arquivo
chegou como `archive/fontes_etapa11/Applegate–Lagariaspdf`, sem extensão, o que o deixava **fora do `.gitignore`**; o
agente o moveu para o caminho acima, sem alterar o conteúdo (registro em `aquisicao.json`).
**Paginação:** PDF p. i = revista p. 192 + i. Isso confirma 193–209; a lista de referências do levantamento
Kontorovich–Lagarias (B12), que dá 101–117, está errada.

**O que foi lido.** Pp. 193–198 integrais (introdução, §2, Conjecturas C e C#, Tabela 1). Enunciados dos Teoremas 5.1 e
5.2 (p. 203), 6.1 (p. 204) e 6.3 (p. 207), e as conjecturas finais (pp. 207–208). **Pp. 197, 198 e 203 conferidas na
imagem da página.** As provas das §§4–6 não foram auditadas.

## 1. O que o artigo afirma

| item | página | conteúdo |
|---|---|---|
| T⁻¹ | 195 | T⁻¹(n) = {2n} se n ≡ 0, 1 (mod 3); {2n, (2n−1)/3} se n ≡ 2 (mod 3) — o mesmo que o Lema 4.1 de Leventides–Poulios (B11) e o 𝓛₊ da CL0 |
| estrutura | 195 | a árvore podada T\*_k(a) é determinada por a mod 3^{k+1}; há no máximo 2·3^k estruturas distintas, e o número real R(k) cresce exponencialmente |
| ramificação estrita | 196 | toda árvore podada ramifica em no máximo quatro passos a partir de qualquer nó |
| (2.1) | 197 | E[N\*_k(a)] = (4/3)^k sobre as classes a mod 3^{k+1} (atribuído a Lagarias–Weiss 1992, Teor. 3.1) |
| **Conjectura C** | 197 | **N⁺(k) e N⁻(k) se comportam como (4/3)^{k(1+o(1))}** quando k → ∞ — conferido na imagem |
| Tabela 1 | 197 | N^±(k) e D^±(k) = (4/3)^{−k} N^±(k) para k ≤ 30, com os mesmos números da Tabela 4 de B12 |
| **Conjectura C#** | 198 | existem C^± > 0 com C⁻ ≤ D⁻(k) < 1 < D⁺(k) < C⁺ para k grande — conferido na imagem |
| **Teor. 5.1** | 203 | no modelo de ramificação repetida (⌊τ^k⌋ sorteios i.i.d. do processo B[9], τ > 1 fixo), com probabilidade 1, lim (Ñ^±_τ(k))^{1/k} = 4/3: **o análogo da Conjectura C vale no modelo** |
| **Teor. 5.2** | 203 | no mesmo modelo, (4/3)^{−k} Ñ⁻_τ(k) → 0 e (4/3)^{−k} Ñ⁺_τ(k) → +∞: **o análogo da Conjectura C# é falso no modelo** |
| interpretação | 196 | os extremos reais (Tabela 1) têm faixa bem mais estreita que a do modelo — "a primeira evidência" de que as iterações de 3x+1 não se comportam tão aleatoriamente quanto possível, dadas as restrições óbvias |
| Teor. 6.1 | 204 | E_k[l mod 3^j] = (W[l mod 3^j] + o(1)) (4/3)^k |
| Teor. 6.3 | 207 | para quase todo α nos inteiros 3-ádicos invertíveis ℤ₃^×, o limite W_∞(α) = lim_j W[α mod 3^j] existe (argumento de martingal) |
| Conj. da função limite | 207 | W_∞ é contínua e não nula em todo ℤ₃^×; junto com uma "conjectura do limite extremal", implica C# (p. 208) |

**Não está neste artigo:** a cota (1,302053)^k ≤ N\*_k(a) ≤ (1,358386)^k do Teorema 2.4 de B12. Ela é de
[Applegate e Lagarias 1995a], *Density bounds for the 3x+1 problem, I: Tree-search method*, Math. Comp. 64 (1995),
411–426, como confirma a lista de referências daqui. Continua **não obtida**.

## 2. Rótulos

- Teoremas 5.1, 5.2, 6.1 e 6.3: **A**, com a ressalva de que as provas não foram auditadas.
- Conjecturas C, C# e a da função limite: **D**.
- Os fatos de estrutura (p. 195) e (2.1): **A**.

## 3. O que esta leitura muda nas anteriores

- **B12, ponto de atenção 1, resolvido contra o original:** a Conjectura 6.2 do levantamento, impressa com
  (3/4)^{k+o(k)}, corresponde à Conjectura C daqui, que diz **(4/3)^{k(1+o(1))}**. Era erro tipográfico do
  levantamento.
- **B12, ponto de atenção 3, resolvido:** a paginação é 193–209.
- **B11/B12, raio espectral de Leventides–Poulios:** a cota rigorosa continua a de B12,
  ρ(L_{T,p}) ≥ (1,302053)^{1−1/p}, que depende do artigo da Math. Comp. ainda não obtido. **Sob a Conjectura C**, o
  máximo c_n de Leventides–Poulios cresce como (4/3)^{n(1+o(1))}, porque c_n fica entre N⁺ da profundidade n e (n+1)
  vezes o maior N⁺ até n, e então ρ(L_{T,p}) = (4/3)^{1−1/p}. Rótulo **D**, porque depende de uma conjectura.

## 4. Para o projeto

- **Instrumento espectral: nada.** Não há previsão mensurável pela régua.
- **Frente Collatz:** o crescimento das árvores inversas, a comparação com modelos de ramificação e até uma função
  limite 3-ádica W_∞ em ℤ₃^× já estão aqui, desde 1995. O próprio artigo (p. 196) aponta funções em ℤ₃ ligadas à
  iteração inversa introduzidas por G. Wirsching (1994–1995), sem saber a relação com W_∞. Se a frente Collatz seguir
  pelo lado p-ádico, a busca seguinte é: **a Conjectura da função limite foi resolvida depois de 1995?** A ordem de
  leitura seria Wirsching e trabalhos posteriores de Lagarias. Não afirmo nada sobre o estado dessa questão.
- **Não há candidata nova nesta leitura.** O resultado com cara de achado — os extremos reais mais estreitos que os do
  modelo — é dos próprios autores, de 1995.

*Leitura de 25/09/2026, Claude Opus, para o caderno de hipóteses.*
