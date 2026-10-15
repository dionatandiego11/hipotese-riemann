# B32 — Tavares, programa de densidade de predecessores

Leitura dirigida em 12/10/2026. *Wirsching's Positive-Predecessor-Density Program: Proofs of Conjectures 1 and 3*, Renato Augusto Tavares. Arquivo fornecido pelo usuário: `2608.27617v1.pdf`, movido sem alteração para `archive/fontes_etapa11/collatz_regularidade_20261012/tavares_2026_arxiv_2608.27617v1.pdf`.

SHA-256 `dc2962f0916e5cc1ebc1b3c8c0b777026572e93946711846b49f6f8b54c5a694`; 36 pp.; cabeçalho arXiv:2608.27617v1, 27/08/2026; data impressa 31/08/2026. URL bibliográfica https://arxiv.org/abs/2608.27617; o download original do usuário não foi registrado. Não substituir essa cópia por versão atual sem comparar hash.

**Escopo realmente lido:** §§1–6 (construção, cadeia, Conjectura 1, Laplace e Mellin), enunciados e argumentos de fase nas §§10–12, consultas à normalização na §9 e ao início do Apêndice A. A prova completa de ponto de sela das §§7–9, os certificados Arb e todas as dependências externas não foram auditados. P. 12, identidade (8), conferida visualmente. Páginas impressas coincidem com o PDF.

## 1. O que o preprint afirma

Afirma provar a implicação da Conjectura 1 (Teorema 4.3) por controle da convolução dos geradores com pesos de partições, e a Conjectura 3 (Teorema 10.1) por análise de φ perto de zero. Mantém sem prova a condição (⋆3) e a Conjectura 2, que é a rota de Wirsching para ela. Não afirma provar Collatz.

O autor distingue explicitamente a existência de uma constante na classe de comparação de Wirsching da comparação irrestrita. A primeira é afirmada verdadeira; a segunda é afirmada falsa devido a uma correção log-periódica. O valor e^{H(0)} é apresentado com certificado intervalar, que não foi reexecutado aqui.

Esses resultados globais são **alegações externas de demonstração, pendentes de auditoria integral neste projeto**. Não os promovemos a fatos verificados pelo projeto.

## 2. Onde o artigo é diretamente útil

§3, pp. 4–6, e §12, p. 30, localizam a diferença entre convergência de médias e uma cota inferior por resíduo em resolução crescente. Esse ponto coincide com a cautela do nosso alvo de memória finita, mas os objetos são distintos: o artigo usa geradores com custo fixado, não apenas H_m=L+^m1.

Sua φ é a densidade real de X=Σ_{j≥1}2U_j3^{−j}, U_j uniformes independentes em [0,1], conforme Prop. 3.1. Não é nossa estacionária ν em Z3. O operador W3 é o de Wirsching, sobre a coordenada real. Convergência de W3 não restaura a informação sobre a coordenada aritmética que S∞ integrou.

## 3. A presença de ζ tem mecanismo explícito

Nas pp. 9–12, define K(s)=log E[e^{−sX}] para s>0 e deriva

\[
K^*(z)=\int_0^\infty K(s)s^{z-1}ds
=\frac{(3/2)^z\Gamma(z)\zeta(1+z)}{3^z-1},
\qquad -1<\Re z<0.
\]

Conferimos a derivação **local**: o logaritmo de Laplace se decompõe em Σg(2s/3^j), com g(b)=log((1−e^{−b})/b); integração por partes dá g*(z)=−Γ(z)ζ(1+z), e a soma das dilatações é geométrica. O sinal e a faixa são essenciais. A regularização integral e o controle de convergência estão explicitados na nota de síntese desta rodada.

A extração dos polos z=2πim/log3 fornece coeficientes de uma correção periódica H:

\[
\widehat H(m)=-\frac{2^{i\omega_m}}{\log3}\Gamma(-i\omega_m)\zeta(1-i\omega_m),
\quad\omega_m=2\pi m/\log3,\quad m\ne0.
\]

A presença desse fator não foi inserida por um catálogo de primos. Contudo, deriva da distribuição uniforme e da soma de escalas; a mesma identidade de Mellin vale para outras bases. Por isso não é evidência específica de que a aritmética dos inteiros de Collatz produz os zeros de ζ.

## 4. Consequências e limites

A identidade de Mellin reproduz os zeros de ζ, deslocados por −1, dentro da faixa de convergência. É uma reformulação analítica, não uma cota nova sobre esses zeros. Não transfere automaticamente ao nosso Q, às densidades das árvores ou a uma estratégia de prova de RH.

Prioridades:

1. Auditar localmente o mecanismo Mellin/dilatação e comparar com bases alternativas como controle de especificidade — a parte elementar foi derivada nesta leitura.
2. Para informação de Collatz, definir o alvo conjunto g_ℓ(k,a)/ḡ_ℓ(k), com resolução e janela crescentes; uma cota sobre médias fixas não basta.
3. Se quisermos adotar as resoluções alegadas das Conjecturas 1 e 3, auditar separadamente as provas e o certificado computacional. Esta leitura não executou esses trabalhos.

A fonte também referencia resultados recentes e scripts públicos. Seus valores, novidades e verificações formais não foram aceitos apenas por constarem no preprint. Não houve execução de código externo.
