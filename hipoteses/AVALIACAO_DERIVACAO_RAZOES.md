# Avaliação: derivar as Conjecturas 7 e 8 pela conjectura das razões (28/09/2026)

Entrega documental; nenhum cálculo. Pedido do usuário: avaliar a viabilidade antes de investir.

## 1. O que foi lido

- **Conrey–Snaith 2007** (arXiv:math/0509480; B27): §1, §7 (início e §7.1) e o sumário. A §7 usa a conjectura das
  razões para os momentos discretos **positivos** Σ|ζ′(ρ)|² e Σ|ζ′(ρ)|⁴, obtendo **todos os termos de ordem inferior**.
  - Método (7.6): Σ_ρ f(ρ) = (1/2πi)∮ (ζ′/ζ)(z) f(z) dz num retângulo; os lados horizontais são desprezados; o lado
    direito é avaliado pela conjectura das razões (derivadas em shifts de ζ(c+it+β)/ζ(c+it+γ)…); o esquerdo, pela
    equação funcional.
  - **Não trata momentos negativos.** Cita a conjectura de Hughes–Keating–O'Connell (7.2), que para k = −1 dá
    a(−1) = ∏_p(1 − 1/p)(1 + 1/p) = 6/π², isto é, a constante 3/π³ de Gonek.
- **Buscas:**
  - Bui–Gonek–Milinovich (Forum Math. 27 (2015), arXiv:1302.5032) recuperam a conjectura de HKO, **inclusive
    k = −1**, pelo produto híbrido de Euler–Hadamard. Só o resumo foi lido.
  - Há trabalhos sobre momentos **negativos contínuos** pela conjectura das razões (por exemplo, arXiv:2109.10396,
    corpos de funções). A técnica com funções L no denominador existe.
  - **Não se encontrou** derivação dos termos de ordem inferior de Σ 1/|ζ′(ρ)|² pela conjectura das razões, nem do
    análogo para L(s,χ). Busca breve; não estabelece ausência.

## 2. Primeira conta (heurística, a verificar)

Na receita CFKRS para L(s,χ), o fator aritmético é ∏_p (média local em p) × (fatores ζ-like ∏(1 − 1/p^{1+…})). Para
p | q, a média local é trivial (χ(p) = 0), mas os fatores ζ-like **permanecem**. Em k = −1 isso dá:

  ∏_{p∤q}(1 − p⁻²) · ∏_{p|q}(1 − 1/p) = (6/π²) ∏_{p|q} p/(p+1) = **A_q** (Pearce-Crump).

- A alternativa HE da MN-1/MN-3, ∏_{p|q} p²/(p²−1), corresponde a descartar também os fatores ζ-like em p | q, isto é,
  a um tratamento **incorreto** da receita. Isso explica, a posteriori, por que os dados a excluem.
- **Correção registrada:** numa mensagem ao usuário (28/09), afirmei primeiro que a generalização ingênua de HKO
  dava HE; a conta acima mostra que, com a normalização da receita, ela dá A_q.
- Rótulo: **D** (conta heurística de uma linha, sem derivação completa).

## 3. Viabilidade

| etapa | conteúdo | dificuldade | valor |
|---|---|---|---|
| A. Termo principal para χ pela receita | tornar rigorosa, no nível heurístico, a conta do §2 | baixa–média | confirma A_q por um segundo caminho independente do mollifier |
| B. Termos de ordem inferior, q = 1 | fórmula completa para Σ 1/\|ζ′(ρ)\|² via razões, no molde da §7.1 de Conrey–Snaith | **alta** | se não existir, é contribuição por si só; **testável nos nossos 27.000 zeros de ζ** (0,912 → 0,963 → 0,992) |
| C. Termos de ordem inferior, χ | estender B para caracteres | alta | teste absoluto, e não só diferencial, nos 4 caracteres |

**Dificuldade técnica principal da etapa B:** para o momento negativo, o integrando é
(ζ′/ζ)(z)/(ζ(z+α)ζ(1−z+β)), com α, β → 0 no fim, e tem **polos extras** dentro do contorno, em z = ρ′ − α e
z = 1 − ρ′ + β. É preciso tratá-los, ou escolher a região dos shifts de modo que fiquem fora, o que empurra a
conjectura das razões para a borda de sua região de validade. Conrey–Snaith não enfrentam isso no caso positivo, em
que as funções ζ estão no numerador. É o ponto em que a derivação pode travar.

**Salvaguarda:** qualquer fórmula da etapa B tem um teste decisivo e barato: reproduzir os desvios de altura finita
já medidos em ζ, com ficha congelada **antes** de comparar. Sem isso, não se usa nada da derivação.

## 4. Recomendação

1. **Etapa A primeiro** (documental, dias): derivação heurística do termo principal para χ pela receita, com cada
   passo conferido contra Conrey–Snaith e CFKRS. Se confirmar A_q, a nota ganha um parágrafo teórico forte.
2. Antes da etapa B, **ler Bui–Gonek–Milinovich 2015** e o trabalho de momentos negativos via razões para ver como o
   denominador foi tratado.
3. A etapa B só com ficha e teste pré-registrado em ζ. Tempo e risco altos; é a parte que pode virar um segundo
   artigo.
4. Se o autor responder, perguntar a opinião dele sobre as etapas A e B antes de investir na B.
