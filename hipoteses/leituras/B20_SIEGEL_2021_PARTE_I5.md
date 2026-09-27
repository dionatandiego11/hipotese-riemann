# B20 — Siegel, *The Collatz Conjecture & Non-Archimedean Spectral Theory, Part I.5: How to write the (weak) Collatz conjecture as a contour integral*

**Referência.** M. C. Siegel, arXiv:2111.07883v2 (v1 10/11/2021; v2 15/12/2023), preprint, sem publicação
registrada no arXiv. Depende da Parte I (p-Adic Numbers Ultrametric Anal. Appl., 2024), que **não foi lida**.
**Cópia local:** `archive/fontes_etapa11/ponte_collatz_20260925/siegel_2021_arXiv_2111.07883.pdf`, SHA-256
`8dbad3f2…`, 22 pp., baixada em 26/09/2026.
**Leitura:** texto inteiro (§§0–2).
**Verificação numérica:** `hipoteses/leituras/verificacoes/siegel_2111_07883_{original,corrigida}.py` e `…_log.txt`.

## 1. O que o texto afirma

T_q(n) = n/2 ou (qn+1)/2, com q primo ímpar. A "numen" χ_q: ℕ₀ → ℚ é definida por χ(0) = 0, χ(2n) = χ(n)/2 e
χ(2n+1) = (qχ(n)+1)/2. Também M_q(0) = 1, M(2n) = M(n)/2 e M(2n+1) = qM(n)/2, ou seja,
M_q(n) = q^{#1(n)}/2^{λ₂(n)}.

| item | página | conteúdo |
|---|---|---|
| Cor. 1 (CP, da Parte I) | 3 | os pontos periódicos x ∈ ℤ∖{0} de T_q são exatamente os x = χ_q(n)/(1 − M_q(n)) inteiros; **importado, não conferido** |
| (1.13)–(1.14) | 4–5 | F_q(s, x) = Σ[(1 − M_q(n))x − χ_q(n)] n^{−s} = **ζ(s)x** − ζ_{M_q}(s)x − ζ_{χ_q}(s) |
| **Teor. 3** | 5–6 | x é ponto periódico de T_q ⟺ uma integral de Perron (PV) de F_q(s, x)·[(n+a)^s − (n+a−1)^s]/s se anula para algum n ≥ 3 e a ∈ (0, 1). É apenas Perron aplicado ao coeficiente n-ésimo; equivale a "(1 − M(n))x = χ(n) para algum n" |
| Prop. 1 | 6–8 | Σ_{n<2^N} χ_3 = N·2^N/4; Σ_{n<2^N} M_q = (q((q+1)/2)^N − 1)/(q−1) — **conferido** pela recorrência |
| Prop. 3 | 8 | abscissa de convergência absoluta σ_q = log₂((q+1)/2) |
| Prop. 4 (2.18)–(2.19) | 9–11 | equações funcionais das funções geradoras g_M e g_χ — **corretas** (rederivadas) |
| Prop. 5 (2.25) | 11–12 | equação funcional de f_q(z, x) — **errada** (ver §2) |
| Teor. 4 (2.26) | 12–14 | equação funcional de F_q e continuação meromorfa a ℂ — **coeficiente de ζ errado** (ver §2) |
| Cor. 2 | 14–20 | polos de F_3: duplo em s = 1, simples em 1 + 2πik/ln 2 e em s = −n; resíduos **com a dependência em x errada** |
| final | 20 | F_q cresce hiperexponencialmente para Re s → −∞; não é possível avaliar por resíduos deslocando o contorno |

## 2. Erro em (2.25), (2.26) e no Corolário 2 — B, reproduzido numericamente

Na prova da Prop. 5 (p. 12, 1.ª linha), f_q(z², x) é escrita com **z/(1−z)** no lugar de **x·z²/(1−z²)**. Rederivando:

  **(2.25′)** f_q(z, x) = ((qz+1)/2) f_q(z², x) + x z (2 + z − q)/(2(1 − z²)) − z/(2(1 − z²)).

Ela difere da impressa pelo termo x z/(2(1−z)). Pela transformada de Mellin, isso dá

  **(2.26′)** F_q(s, x) = { (x[(2−q)(2^s−1) + 1] − (2^s − 1)) ζ(s) + q S_q(s, x) } / (2(2^s − 2^{σ_q})),

com S_q como em (2.34). O coeficiente de ζ difere do impresso em x(2^s + q − 1).

**Verificação:** as formas impressas falham numericamente, com discrepância de −0,75x em (2.25) para z = 0,6. As
formas corrigidas conferem com diferença ≤ 10^{−14} em q = 3, 5 e ≤ 10^{−12} em q = 7 (x ∈ {1, −2, 5},
s ∈ {4; 5,5}). Somas diretas com 2^20 termos; 112 s de CPU.

**Confirmação independente:** pela Prop. 1 do próprio autor, χ_3 tem média ~ (log₂ n)/4, e M_3 tem média limitada
(3/2). Então só χ_3 contribui para o polo duplo em s = 1, e (s−1)² F_3 → −1/(4 ln 2), **independente de x**. A forma
(2.26′) dá exatamente isso. A (2.42) de Siegel dá −(4x+1)/(4 ln 2), errada para x ≠ 0, e os resíduos do Cor. 2
herdam o erro.

**O que não é afetado:** o Teor. 3 (reformulação por contorno) usa só Perron e o CP; a estrutura de polos (localização)
também não muda. O erro afeta coeficientes e resíduos.

## 3. Consequência para a ponte direta

- **ζ entra de novo como série da sequência constante:** F_q = ζ·x − …, porque o coeficiente contém o termo constante
  x. É o mesmo mecanismo trivial de Meinardus (B18 §3a). Em (2.26′), ζ aparece como transformada de Mellin de
  z/(1−z) e z/(1−z²), ou seja, como termos de fronteira das séries geradoras.
- **Os zeros de ζ não têm papel.** Os polos de F_q vêm de 1/(2^s − 2^{σ_q}), com espaçamento 2πi/ln 2 típico de
  somas digitais (Flajolet et al.), e do polo de ζ em s = 1. Os zeros de ζ entram só no numerador e não são
  singularidades nem condição do Teor. 3.
- **A reformulação do Teor. 3 não usa estrutura analítica:** detecta um coeficiente por Perron. O próprio autor
  registra que a avaliação por resíduos é inviável.
- **Rótulos:** Prop. 1, Prop. 4 e Teor. 3 (dado o CP): **A**. (2.25), (2.26) e Cor. 2 como impressos: **incorretos**;
  formas corrigidas: **B** (derivação própria + verificação numérica). Isso não é novidade matemática, é uma errata;
  antes de circular, conferir se a Parte I publicada ou a tese já a corrigem.

*Leitura de 26/09/2026, Claude Opus.*
