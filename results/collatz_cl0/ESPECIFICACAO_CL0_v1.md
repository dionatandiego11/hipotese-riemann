# Especificação do laboratório Collatz — CL0, versão 1 (25/09/2026)

Etapa **CL0** de [docs/PLANO_COLLATZ.md](../../docs/PLANO_COLLATZ.md). SHA-256 deste documento em
`ESPECIFICACAO_CL0_v1.sha256`. Documento **congelado**: correção vira errata ou adendo com arquivo próprio, nunca
edição deste texto. Acompanha o protocolo `PROTOCOLO_CL0_v1.md` e a configuração `collatz_cl1_v1.toml`.

## 0. O que este documento é, e o que não é

**É:** a definição dos espaços, do mapa, das medidas, dos operadores e das observáveis do laboratório, com o rótulo
A/B/C/D de cada afirmação e as hipóteses de cada teorema citado.

**Não é:** relatório de execução, declaração de hipótese testável no registro espectral, nem reivindicação de novidade.
Nenhum número deste documento foi produzido por execução do projeto: os valores das §§3 e 7 são consequências
matemáticas conhecidas ou derivadas aqui, e existem justamente para servir de resposta conhecida às verificações de
CL1–CL2. Nenhuma aproximação finita descrita aqui representa o sistema infinito.

Collatz está **fora do domínio do instrumento espectral** do projeto (protocolo do registro v2, §4). Este laboratório
não lê zeros da ζ, não lê o catálogo de primos e não alimenta nenhum critério de m3/m4.

## 1. O mapa e a convenção temporal

Convenção fixada (a mesma de Bernstein–Lagarias, p. 1, eq. (1.1), e de Monks–Yazinski):

\[
T(x)=\begin{cases}x/2,&x\equiv0\pmod 2,\\[2pt](3x+1)/2,&x\equiv1\pmod 2.\end{cases}
\]

Generalização usada em CL3: \(T_a(x)=x/2\) no ramo par e \((ax+1)/2\) no ramo ímpar, com \(a\in\{3,5\}\) declarado em
cada tabela. (A forma geral \(T_{a,b}\), com \(ab\) ímpar, aparece em Bernstein–Lagarias, p. 3; não é usada em CL0–CL2.)

**Duas convenções temporais, nunca misturadas na mesma tabela:**

| Convenção | Mapa | Ciclo dos positivos conhecido | Período desse ciclo |
|---|---|---|---|
| **T-tempo** (padrão deste laboratório) | \(T\) acima | \(1\to2\to1\) | **2** |
| C-tempo (mapa clássico) | \(C(x)=3x+1\) se ímpar, \(x/2\) se par | \(1\to4\to2\to1\) | 3 |

Conversão: \(n\) passos de \(T\) com \(k\) passos ímpares correspondem a \(n+k\) passos de \(C\). **Regra:** toda tabela,
gráfico ou arquivo de saída declara a convenção no cabeçalho; períodos de convenções diferentes nunca são comparados
diretamente nem somados.

## 2. Espaços, invariância e medidas

| Espaço | Definição | \(T\)-invariante | Medida natural | Normalização | Papel |
|---|---|---|---|---|---|
| \(\Sigma_2\) | \(\{0,1\}^{\mathbb N}\), shift unilateral \(\sigma\), \(d(x,y)=2^{-\min\{i:\,x_i\neq y_i\}}\) | sim (\(\sigma\)) | Bernoulli\((\tfrac12,\tfrac12)\) | massa total 1 | modelo simbólico; contagens de CL1 |
| \(\mathbb Z_2\) | inteiros 2-ádicos, \(|\cdot|_2\) | sim | Haar \(\mu\) | \(\mu(\mathbb Z_2)=1\) | conjugação, operadores, CL4 |
| \(\mathbb Q_{\mathrm{odd}}\) | racionais de denominador ímpar na forma reduzida; subanel de \(\mathbb Z_2\) | sim | — (contável; sem medida natural) | — | ciclos exatos de CL2 |
| \(\mathbb Z\) | inteiros | sim | contagem | — | filtro de integralidade |
| \(\mathbb N_{>0}\) | inteiros positivos | sim | contagem | — | objeto da conjectura; \(\mathcal L_+\) |

Cadeia de inclusões: \(\mathbb N_{>0}\subset\mathbb Z\subset\mathbb Q_{\mathrm{odd}}\subset\mathbb Z_2\).
\(\mathbb Q_{\mathrm{odd}}\) é exatamente a imagem, sob a codificação de paridades, dos pontos **eventualmente
periódicos** do shift (Monks–Yazinski, p. 2).

**Regra de transporte.** Nenhuma afirmação vale automaticamente de um espaço para outro. Um enunciado só passa de
\(\mathbb Z_2\) para \(\mathbb Z\) ou \(\mathbb N_{>0}\) com argumento próprio, registrado. Contraexemplo de referência,
registrado em §3 (A3): a involução \(\Omega\) tem \(\Omega(3)=-4/9\), que não é inteiro — a simetria 2-ádica **não**
leva os positivos nos negativos, embora \(V(x)=-1-x\) leve.

**Quando a medida é necessária.** Contagens de pontos periódicos, coeficientes da zeta e classificação de ciclos
(O1–O6) **não** usam medida alguma. Medida só entra em: o operador de Perron–Frobenius para Haar (§4), afirmações
ergódicas sobre \(\mathbb Z_2\) (A1), e a amostragem declarada dos transientes (O8), onde a medida é a da amostra, não
uma medida invariante.

## 3. Fatos de referência, com hipóteses e páginas

Estado da fonte: **L** = lido nesta entrega, com página; **L-parcial** = trechos lidos, prova não auditada.
Fontes com hash em `archive/fontes_etapa11/collatz_cl0_20260925/aquisicao.json` e
`archive/fontes_etapa11/hipoteses_20260919/aquisicao.json`.

| ID | Afirmação | Hipóteses / ressalvas | Rótulo | Fonte e página | Estado |
|---|---|---|---|---|---|
| A1 | \(T\) está bem definido em \(\mathbb Z_2\), preserva a medida de Haar e é fortemente mixing, logo ergódico | O próprio texto atribui a afirmação a sua referência [8] (Lagarias 1985); a prova **não** está em Bernstein–Lagarias e não foi auditada aqui. A conservação de Haar é reverificada de forma independente em A7b | A | Bernstein–Lagarias, p. 1 | L-parcial |
| A2 | Existe homeomorfismo \(\Phi:\mathbb Z_2\to\mathbb Z_2\) com \(\Phi\circ S\circ\Phi^{-1}=T\), onde \(S\) é o shift 2-ádico; \(\Phi\) é único sob \(\Phi(0)=0\) e solenoidal; \(\Phi^{-1}(x)=\sum_{i\ge0}\bigl(T^i(x)\bmod2\bigr)2^i\) (vetor de paridades) | Enunciado em \(\mathbb Z_2\), **não** em \(\mathbb Z\) nem em \(\mathbb N_{>0}\); a versão métrica (preserva a medida 2-ádica) é afirmada no mesmo trecho | A | Bernstein–Lagarias, p. 1, eqs. (1.2)–(1.3); p. 2, eqs. (1.4)–(1.5) | L-parcial (prova de unicidade lida, p. 2) |
| A3 | O grupo de automorfismos de \(S\) é \(\mathbb Z/2\mathbb Z\), com elemento não trivial \(V(x)=-1-x\); \(\Omega=\Phi\circ V\circ\Phi^{-1}\) comuta com \(T\) e satisfaz \(\Omega^2=\mathrm{id}\) | O texto de Bernstein–Lagarias atribui o cálculo do grupo a suas referências [6, Teorema 6.9] e [3]; não auditado. **\(\Omega\) não preserva \(\mathbb Z\):** \(\Omega(3)=\Phi\circ V\circ\Phi^{-1}(3)=-4/9\) | A | Bernstein–Lagarias, p. 2; Monks–Yazinski, Teorema 2.1 (p. 3) e Exemplo 2 (p. 3) | L |
| A4 | **Conjectura de Periodicidade:** \(\Phi(\mathbb Q\cap\mathbb Z_2)=\mathbb Q\cap\mathbb Z_2\). É equivalente à Conjectura de Autoconjugação \(\Omega(\mathbb Q_{\mathrm{odd}})\subseteq\mathbb Q_{\mathrm{odd}}\) e a "nenhum 2-ádico racional tem \(T\)-órbita divergente"; \(\Omega(\mathbb Z_+)\subseteq\mathbb Q_{\mathrm{odd}}\) equivale à Conjectura das Órbitas Divergentes | **Aberta:** é conjectura (D), não teorema. A equivalência (essa sim, teorema) é o que está demonstrado. Bernstein–Lagarias registram na p. 3 que seus resultados **não** se relacionam de modo imediato com a Conjectura 3x+1, pois \(\Phi\circ S^k\circ\Phi^{-1}=T^k\) não carrega informação nova para \(k\ge2\) | A (a equivalência) / D (a conjectura) | Bernstein–Lagarias, p. 3; Monks–Yazinski, Teorema 2.1, p. 3 | L |
| A5 | \(\#\operatorname{Fix}(\sigma^n)=2^n\) em \(\Sigma_2\) e \(\#\operatorname{Fix}(S^n)=\#\operatorname{Fix}(T^n)=2^n\) em \(\mathbb Z_2\); logo \(\zeta_T(z)=(1-2z)^{-1}\) como série formal, convergente para \(|z|<1/2\) | Depende de A2. Derivação elementar no Anexo A.1 | A (derivação própria) | — | — |
| A6 | Para a palavra de paridades \(\varepsilon\in\{0,1\}^n\): \(T^n(x)=\bigl(3^kx+b\bigr)/2^n\) com \(k=\sum_j\varepsilon_j\) e \(b=\sum_j\varepsilon_j2^j3^{\sum_{i>j}\varepsilon_i}\); o único ponto com essa palavra e \(T^n(x)=x\) é \(x=b/(2^n-3^k)\), e \(2^n\neq3^k\) para \(n\ge1\) | Vale em \(\mathbb Q_{\mathrm{odd}}\) (e em \(\mathbb Z_2\)). A palavra é a de \(x\), a verificar por iteração; a fórmula sozinha não garante que o itinerário realizado seja \(\varepsilon\). Derivação e conferências no Anexo A.2 | A (derivação própria) | — | — |
| A7 | Os dois ramos inversos \(b_0(y)=2y\) e \(b_1(y)=(2y-1)/3\) são contrações de razão **exatamente** \(1/2\) na métrica 2-ádica, com imagens disjuntas que cobrem \(\mathbb Z_2\); logo \(\mathcal L_g\) preserva \(\mathrm{Lip}_\alpha(\mathbb Z_2)\) para todo \(\alpha>0\), e \(P\) é o operador de transferência de \(T\) para Haar, com \(P\mathbf 1=\mathbf 1\) | \(3\) é unidade em \(\mathbb Z_2\); nada aqui afirma quase-compacidade, determinante de Fredholm ou lacuna espectral — isso é objeto de CL4 e exige derivação própria. Anexo A.3 | A (derivação própria) | — | — |
| A8 | \(\mathcal L_+\) é limitado em \(\ell^p(\mathbb N_{>0})\), com \(\|\mathcal L_+\|_{\ell^1}=1\), \(\|\mathcal L_+\|_{\ell^2}=\sqrt2\), \(\|\mathcal L_+\|_{\ell^\infty}=2\) | Vale para \(\mathcal L_+\) sem peso, como definido em §4; um peso não constante muda a conta e exige derivação nova. Anexo A.4 | A (derivação própria) | — | — |

**Não são fatos de referência deste laboratório:** a Conjectura 3x+1; a inexistência de ciclos além de \(\{1,2\}\) nos
positivos; qualquer afirmação de que resultados simbólicos informem sobre convergência de órbitas. O resultado de Tao
(F-001 do registro) é sobre densidade logarítmica e quase todas as órbitas em sentido preciso; **não** prova que toda
órbita chega a 1 e não é usado aqui.

## 4. Operadores: ficha matemática

Nenhuma linha desta tabela afirma existência de espectro discreto, auto-adjunticidade ou identidade de determinante.
Espaço, medida, norma e domínio vêm **antes** de qualquer palavra sobre espectro.

| Operador | Fórmula | Espaço de funções | Medida | Norma | Limitação | O que **não** se afirma |
|---|---|---|---|---|---|---|
| \(\mathcal L_g\) (ponderado) | \(\mathcal L_gf(y)=\sum_{i=0}^{1}g(b_i(y))f(b_i(y))\) | \(\mathrm{Lip}_\alpha(\mathbb Z_2)\), \(\alpha>0\) declarado; ou \(C(\mathbb Z_2)\) | não requer | \(\|f\|_\infty+\mathrm{Lip}_\alpha(f)\) | limitado se \(g\in\mathrm{Lip}_\alpha\) (A7) | quase-compacidade, traço, determinante de Fredholm |
| \(P\) (Perron–Frobenius, Haar) | \(Pf(y)=\tfrac12\bigl[f(2y)+f((2y-1)/3)\bigr]\) | \(L^2(\mathbb Z_2,\mu)\) ou \(C(\mathbb Z_2)\) | Haar \(\mu\), \(\mu(\mathbb Z_2)=1\) | \(\|\cdot\|_{L^2}\) | \(\|P\|\le1\), \(P\mathbf1=\mathbf1\) (A7) | que seu espectro descreva os inteiros positivos |
| \(U\) (Koopman) | \(Uf=f\circ T\) | \(\ell^2(\mathbb N_{>0})\) | contagem | \(\|\cdot\|_{\ell^2}\) | \(\|U\|=\sqrt2\) (A8) | — |
| \(\mathcal L_+\) (contagem nos positivos) | \(\mathcal L_+f(m)=f(2m)+\mathbf 1_{m\equiv2\,(3)}f\bigl((2m-1)/3\bigr)\) | \(\ell^p(\mathbb N_{>0})\), \(p\) declarado | contagem | \(\|\cdot\|_{\ell^p}\) | A8 | **nada de Haar**: o fator \(\tfrac12\) não se aplica aqui |

Observações que fazem parte da especificação:

1. \(\mathcal L_+=U^{*}\) na dualidade \(\ell^2\): \(\langle\mathcal L_+f,g\rangle=\langle f,Ug\rangle\). O segundo ramo
   existe só quando \(m\equiv2\pmod 3\); nesse caso \((2m-1)/3\) é automaticamente **ímpar** e \(\ge1\). Essa indicatriz
   é o filtro aritmético do laboratório: é ela, e não a dinâmica simbólica, que distingue \(\mathbb N_{>0}\) de
   \(\mathbb Z_2\).
2. **Proibição explícita** (plano, §Convenções): não transportar a normalização \(\tfrac12\) de Haar para
   \(\mathcal L_+\), e não transportar identidade demonstrada para um operador a outro operador.
3. Um modelo finito (§5, O6–O7) tem espectro próprio, do modelo. Ele nunca é apresentado como espectro de
   \(\mathcal L_g\), \(P\) ou \(\mathcal L_+\).

## 5. Observáveis

Cada observável declara mapa, espaço, medida (ou a ausência dela), normalização e significado. A coluna "rótulo
esperado" diz o máximo que a observável pode sustentar quando medida corretamente — não o que se espera encontrar.

| ID | Observável | Mapa | Espaço | Medida | Normalização | Significado | Rótulo esperado | Etapa |
|---|---|---|---|---|---|---|---|---|
| O1 | \(F_n^X=\#\operatorname{Fix}(T^n)\cap X\) | \(T\) (ou \(T_a\)) | \(X\in\{\Sigma_2,\mathbb Z_2,\mathbb Q_{\mathrm{odd}},\mathbb Z,\mathbb N_{>0}\}\) | não requer | nenhuma | pontos de período **divisor** de \(n\), em T-tempo | B | CL1, CL2 |
| O2 | \(c_d^X\), órbitas de período **mínimo** \(d\) | idem | idem | não requer | nenhuma | contagem de órbitas primitivas; \(F_n=\sum_{d\mid n}d\,c_d\) | B | CL1, CL2 |
| O3 | coeficientes de \(\zeta_T(z)=\exp\sum_n F_nz^n/n\) | idem | idem | não requer | série **formal**; raio declarado quando houver | função geradora de contagens periódicas; **não** registra transientes | B | CL1 |
| O4 | \(Z_n(g)=\sum_{x\in\operatorname{Fix}(T^n)}\prod_{j<n}g(T^jx)\) | idem | \(\Sigma_2\), \(\mathbb Z_2\) | não requer | pesos \(a,b\) constantes por ramo, declarados na configuração | soma periódica ponderada; caso conhecido \((a+b)^n\) | B | CL1 |
| O5 | candidato \(x_\varepsilon=b/(2^n-3^k)\) e sua classe | \(T\), \(T_a\) | \(\mathbb Q_{\mathrm{odd}}\) | não requer | fração reduzida, sinal registrado | ciclo exato; classes: inteiro positivo, inteiro negativo, zero, racional não inteiro | B | CL2 |
| O6 | \(\operatorname{tr}(A^n)\) e \(\det(I-zA)\) de modelo finito | modelo declarado | grafo finito declarado | não requer | orientação de \(A\) e fronteira declaradas | contagem de caminhos fechados **do modelo** | B (do modelo) | CL4 |
| O7 | autovalores de modelo finito | idem | idem | não requer | idem, mais estudo de estabilidade | propriedade **do modelo**, com dependência de resolução e fronteira medida | B (do modelo) | CL4 |
| O8 | tempo de chegada, altura máxima, censura | \(T\), \(T_a\) | \(\mathbb N_{>0}\) | medida **da amostra**, declarada antes | por tamanho de amostra; orçamento de passos e teto de altura fixos | comportamento transiente **relativo à amostragem**; esgotar orçamento **não** é divergência | B, e C só com controle | CL3 |
| O9 | assinatura aritmética que distingue \(T_3\) de \(T_5\) | \(T_a\) | declarado em CL3–CL5 | conforme a assinatura | declarada antes dos dados | informação que a zeta simbólica perde | C no máximo, com colisões exibidas | CL5 |

Para O1–O5 a exigência é **igualdade exata**, sem tolerância de ponto flutuante (§6 do protocolo).

## 6. Truncamento e aproximações finitas

1. Toda tabela de saída carrega: convenção temporal, espaço, período máximo examinado e se houve censura.
2. "Não há ciclo além dos listados até período \(n_{\max}\)" é resultado finito. Nunca é escrito como ausência global,
   nem como evidência sobre convergência de órbitas.
3. Um grafo truncado **não** tem suas saídas fechadas artificialmente; a condição de fronteira é declarada e a
   dependência dela é medida antes de qualquer interpretação.
4. Aplicar \(T\) aos menores representantes módulo \(2^m\) **não** define dinâmica quociente: a divisão por 2 perde um
   bit. Qualquer modelo desse tipo é rotulado como aproximação, com a perda declarada.
5. Uma identidade matricial em modelo finito não é um determinante de Fredholm do operador infinito.
6. Zeta de pontos periódicos não registra transientes; toda leitura de O3 que sugira o contrário é erro de
   interpretação, não achado.

## 7. Rótulos, fontes e o que já tem resposta conhecida

- **A:** teorema, com hipóteses registradas (§3). **B:** reprodução numérica. **C:** achado experimental com novidade a
  investigar. **D:** conjectura.
- Fonte só conta se foi lida, com página. Resumo de busca e texto gerado por IA não são fonte.
- **Registro explícito:** os valores da §3 (A5, A6) e a tabela de validação do protocolo (§2 de
  `PROTOCOLO_CL0_v1.md`) **já têm resposta conhecida antes de qualquer execução**. Reproduzi-los é B e apenas B;
  nenhum deles pode ser apresentado como achado, nem contar para novidade.
- Novidade exige busca bibliográfica registrada. A busca de 19/09 ([hipoteses/BIBLIOGRAFIA.md](../../hipoteses/BIBLIOGRAFIA.md))
  é varredura dirigida, não revisão sistemática concluída.

## 8. Fora do escopo do CL0

Não foram executados, e não são autorizados por este documento: piloto de CL1, enumeração de palavras, cálculo de
ciclos, modelos finitos, simulação de transientes, qualquer leitura de zeros ou de primos, qualquer comparação com a
ζ. CL0 entrega texto e configuração.

*Dionatan Resende & Claude Opus — 25/09/2026.*

---

# Anexo A — derivações próprias

Elementares e verificáveis; incluídas para que A5–A8 não dependam de fonte não auditada. Cada uma será reverificada
numericamente na etapa indicada (rótulo B), o que **não** as transforma em achado.

## A.1 Contagem de pontos periódicos (A5)

Em \(\Sigma_2\), \(\sigma^n(x)=x\) significa \(x_{i+n}=x_i\) para todo \(i\): a sequência é determinada pelos \(n\)
primeiros símbolos e qualquer escolha deles produz um ponto fixo de \(\sigma^n\). Logo
\(\#\operatorname{Fix}(\sigma^n)=2^n\).

Em \(\mathbb Z_2\) com o shift \(S\), o mesmo argumento nos dígitos binários dá
\(x=c\,(1+2^n+2^{2n}+\cdots)=c/(1-2^n)\) com \(c\in\{0,\dots,2^n-1\}\): também \(2^n\) pontos, todos em
\(\mathbb Q_{\mathrm{odd}}\) (o denominador \(2^n-1\) é ímpar). Por A2, \(\Phi\) é bijeção e
\(\Phi\circ S^n\circ\Phi^{-1}=T^n\), logo \(\Phi\) leva \(\operatorname{Fix}(S^n)\) bijetivamente em
\(\operatorname{Fix}(T^n)\) e \(F_n^{\mathbb Z_2}=2^n\).

Daí \(\sum_{n\ge1}F_nz^n/n=\sum_n(2z)^n/n=-\log(1-2z)\) e \(\zeta_T(z)=(1-2z)^{-1}\), como série formal e como função
analítica em \(|z|<1/2\).

Inversão de Möbius: de \(F_n=\sum_{d\mid n}d\,c_d\) vem \(c_n=\frac1n\sum_{d\mid n}\mu(d)\,2^{n/d}\) (contagem de
palavras de Lyndon binárias).

## A.2 Fórmula do ciclo (A6)

Indução em \(n\). Para \(n=1\): \(\varepsilon_0=0\) dá \(k=0,b=0\) e \(T(x)=x/2\); \(\varepsilon_0=1\) dá \(k=1,b=1\) e
\(T(x)=(3x+1)/2\). Supondo \(T^n(x)=(3^kx+b)/2^n\) para a palavra \(\varepsilon_0\ldots\varepsilon_{n-1}\), um passo
par mantém o numerador e dobra o denominador; um passo ímpar leva \((3^kx+b)/2^n\) a
\((3^{k+1}x+3b+2^n)/2^{n+1}\) — que é a fórmula com \(\varepsilon_n=1\), pois cada \(b\)-termo anterior ganha um fator
3 e o novo termo é \(2^n3^0\).

Conferências (T-tempo):

| \(\varepsilon\) | \(k\) | \(b\) | \(2^n-3^k\) | \(x=b/(2^n-3^k)\) | itinerário verificado |
|---|---|---|---|---|---|
| \((0)\) | 0 | 0 | 1 | 0 | \(0\to0\), par ✓ |
| \((1)\) | 1 | 1 | \(-1\) | \(-1\) | \(-1\to-1\), ímpar ✓ |
| \((0,0)\) | 0 | 0 | 3 | 0 | ✓ |
| \((1,0)\) | 1 | 1 | 1 | 1 | \(1\to2\to1\) ✓ |
| \((0,1)\) | 1 | 2 | 1 | 2 | \(2\to1\to2\) ✓ |
| \((1,1)\) | 2 | 5 | \(-5\) | \(-1\) | \(-1\to-1\) ✓ (palavra não primitiva) |

Logo \(\operatorname{Fix}(T)=\{0,-1\}\) e \(\operatorname{Fix}(T^2)=\{0,-1,1,2\}\), com \(2^1\) e \(2^2\) elementos,
coerente com A.1. \(2^n=3^k\) com \(n\ge1\) é impossível (paridade), então o denominador nunca se anula.

**Ressalva que o protocolo transforma em verificação obrigatória:** a fórmula produz um candidato por palavra; que o
itinerário de \(x_\varepsilon\) seja de fato \(\varepsilon\) é conferido por iteração exata, com paridade definida por
denominador ímpar.

## A.3 Ramos inversos, \(\mathcal L_g\) e \(P\) (A7)

\(b_0(y)=2y\) e \(b_1(y)=(2y-1)/3\) satisfazem \(T\circ b_i=\mathrm{id}\); \(b_0\) tem imagem \(2\mathbb Z_2\) (pares) e
\(b_1\) tem imagem \(1+2\mathbb Z_2\) (ímpares, pois \(3b_1(y)=2y-1\) é ímpar), imagens disjuntas cuja união é
\(\mathbb Z_2\). Como \(|3|_2=1\),
\[
|b_0(y)-b_0(y')|_2=\tfrac12|y-y'|_2,\qquad |b_1(y)-b_1(y')|_2=\bigl|\tfrac23\bigr|_2|y-y'|_2=\tfrac12|y-y'|_2 .
\]
Contração uniforme de razão exatamente \(1/2\): se \(f\in\mathrm{Lip}_\alpha\), então \(f\circ b_i\in\mathrm{Lip}_\alpha\)
com constante multiplicada por \(2^{-\alpha}\), e \(\mathcal L_g\) é limitado em \(\mathrm{Lip}_\alpha\) quando
\(g\in\mathrm{Lip}_\alpha\). Isso situa \(\mathcal L_g\) no quadro usual de sistemas de funções iteradas uniformemente
contrativos; **nada além disso está afirmado aqui**.

\(P\) é o operador de transferência de \(T\) para Haar: como \(y\mapsto2y\) leva \(\mu\) na uniforme de
\(2\mathbb Z_2\), vale \(\int_{2\mathbb Z_2}F\,d\mu=\tfrac12\int F(2y)\,d\mu(y)\), e o análogo para os ímpares via
\(b_1\). Com \(T(b_i(y))=y\),
\[
\int f\,(g\circ T)\,d\mu=\tfrac12\int f(2y)g(y)\,d\mu+\tfrac12\int f\bigl(\tfrac{2y-1}3\bigr)g(y)\,d\mu=\int (Pf)\,g\,d\mu .
\]
Em particular \(P\mathbf1=\mathbf1\), o que reverifica, de forma independente da fonte, que \(T\) preserva \(\mu\)
(parte de A1).

## A.4 Limitação de \(\mathcal L_+\) (A8)

Seja \(M[m,x]=1\) se \(T(x)=m\) e 0 caso contrário, \(m,x\in\mathbb N_{>0}\); então
\(\mathcal L_+f(m)=\sum_xM[m,x]f(x)\), e o segundo ramo aparece exatamente quando \(m\equiv2\pmod3\) (aí
\(3\cdot\frac{2m-1}{3}=2m-1\) é ímpar, logo o pré-imagem é ímpar, e \(\ge1\) para todo \(m\ge2\)).

Cada coluna tem soma 1 (cada \(x\) tem um único \(T(x)\)); cada linha tem soma \(\le2\). Daí:
\(\|\mathcal L_+f\|_1\le\sum_x|f(x)|\sum_mM[m,x]=\|f\|_1\), com igualdade em \(f=\delta_x\), logo
\(\|\mathcal L_+\|_{\ell^1}=1\); \(\|\mathcal L_+\|_{\ell^\infty}=2\), atingido em \(f\equiv1\) e \(m\equiv2\pmod3\);
e pelo teste de Schur \(\|\mathcal L_+\|_{\ell^2}\le\sqrt{2\cdot1}=\sqrt2\). O valor é exato: \(\mathcal L_+=U^*\) e
\(\|U\delta_2\|_2^2=\#T^{-1}(2)=\#\{1,4\}=2\), logo \(\|U\|=\|\mathcal L_+\|_{\ell^2}=\sqrt2\). Por Riesz–Thorin,
\(\|\mathcal L_+\|_{\ell^p}\le2^{1-1/p}\).

Um peso não constante altera essas contas; nenhum enunciado acima se transfere a \(\mathcal L_g\) com peso arbitrário,
nem ao caso \(T_a\) com \(a\neq3\) sem refazer a indicatriz (\(a=5\): o ramo existe quando \(2m\equiv1\pmod5\)).
