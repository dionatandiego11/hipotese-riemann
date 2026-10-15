# Collatz — fechamento e complexidade dos filtros de congruência

Data da entrega: 12/10/2026. Declaração anterior à implementação: `results/collatz_filtros_20261011/DECLARACAO.md` (11/10/2026), SHA-256 `f6311b8538678202a22eb887615b7561d07ecf4c990175def1ba2bf7ca00ad8e`.

**Pergunta autorizada:** a repetição dos ramos inversos mantém os filtros numa família controlável ou sua complexidade cresce sem controle?

**Resposta demonstrada:** há fechamento numa família infinita de filtros periódicos, com módulo explícito e custo descritivo linear por palavra. Não há fechamento em um módulo fixo: até a contagem total dos ancestrais tem período mínimo 3^m. Apesar disso, o operador normalizado é uma contração na norma sup e na norma de Fourier absolutamente somável. Normas uniformes não fornecem, por si só, aproximação uniforme por um número fixo de resíduos.

Rótulos: **A — derivações elementares abaixo, sem hipótese de Collatz ou RH; B — controles exatos finitos de implementação.** Não se reivindica novidade: o crescimento da informação 3-ádica das árvores tem antecedentes explícitos. Não há conclusão sobre os zeros de ζ.

## 1. Espaços e família de filtros

Adotamos T(x)=x/2 para x par, T(x)=(3x+1)/2 para x ímpar. Nos positivos,

\[
\mathcal L_+f(y)=f(2y)+\mathbf1_{y\equiv2\ (3)}f((2y-1)/3),\qquad y\ge1.
\]

Se o ramo ímpar é inteiro, é positivo: a menor raiz admissível é y=2, produzindo 1. A mesma fórmula estende funções periódicas a Z; a restrição aos positivos coincide com o operador declarado na CL0.

Para q≥1, 0≤r<q, escrevemos F_{q,r}(x)=1_{x≡r mod q}. A família controlada considerada é o espaço de todas as combinações lineares finitas desses filtros, isto é, todas as funções periódicas de período finito. Não restringimos os resíduos aos invertíveis.

**Correção de espaço importante:** um filtro não constante de módulo ímpar não é uma função contínua de Z2. Por CRT, cada classe ímpar e seu complemento encontram toda bola 2-ádica; uma extensão contínua que concordasse nos positivos teria de assumir dois valores diferentes arbitrariamente perto de qualquer ponto. Para filtros puramente diádicos, ao contrário, há extensão localmente constante a Z2.

Logo as contas com Haar em Z2 e as contas com admissão inteira de L+ são problemas diferentes. Poderíamos realizar os filtros periódicos num espaço profinito maior, mas essa construção não é necessária para os resultados desta nota.

## 2. Um passo: duas congruências explícitas

A aplicação do ramo par equivale a

\[
F_{q,r}(2y)=\mathbf1_{2y\equiv r\ (q)}.
\]

No ramo ímpar, a condição conjunta de integridade e do filtro é

\[
\mathbf1_{y\equiv2\ (3)}F_{q,r}((2y-1)/3)
 =\mathbf1_{2y\equiv3r+1\ (3q)}.
\]

Em geral, a congruência ay≡b mod M tem solução se e somente se d=gcd(a,M) divide b. Quando tem solução, é uma única classe módulo M/d, pois a/d é invertível módulo M/d. Caso M/d=1, o filtro é constante.

Portanto cada ramo transforma um filtro em um filtro ou em zero. Para q ímpar, ambos têm solução: os novos módulos são q e 3q. Para q par, exatamente um dos ramos sobrevive para cada r: os módulos possíveis são q/2 e 3q/2. Isso evita aplicar inversos de 2 em módulos onde não existem.

## 3. Palavra de ramos: fórmula e admissibilidade completa

Uma palavra w=(ε1,…,εm) é percorrida da raiz para o ancestral, aplicando b0(y)=2y ou b1(y)=(2y−1)/3. Se k é o número de passos ímpares, sua composição racional é

\[
B_w(y)=\frac{2^my-c_w}{3^k}.
\]

A recorrência é c_empty=0; ao acrescentar um ramo par, c←2c; ao acrescentar um ramo ímpar, c←2c+3^k e depois k←k+1. Por indução, 0≤c_w≤3^m−2^m.

### Por que a condição final também verifica todos os passos

Considere um prefixo com j passos, k_j passos ímpares e numerador A_j=2^j y−c_prefix. Se a palavra restante tem m−j passos e k−k_j ímpares, o numerador final tem a forma

\[
2^{m-j}A_j-3^{k_j}d.
\]

A divisibilidade do numerador final por 3^k implica divisibilidade de A_j por 3^{k_j}, porque 2 é invertível módulo potências de 3. Isso vale para todos os prefixos. Logo B_w(y) inteiro implica a integridade de todos os passos intermediários. Partindo de y≥1, a positividade segue passo a passo quando os ramos são inteiros.

Assim, o ramo w é admissível e termina no filtro F_{q,r} exatamente quando

\[
2^my\equiv c_w+3^k r\pmod{3^kq}.
\]

Com d_m=gcd(2^m,q), a saída é zero se d_m não divide c_w+3^kr; caso contrário é **uma única classe módulo**

\[
Q_w=\frac{3^kq}{d_m}.
\]

Uma palavra precisa de m bits; k e c_w têm tamanho O(m); o módulo exige O(log q+m) bits. A fórmula individual é compacta. Isso não torna barata a enumeração de todas as 2^m palavras.

## 4. Fechamento global com orçamento explícito

\[
\mathcal L_+^mF_{q,r}=\sum_{w\in\{0,1\}^m}\mathbf1_{\text{congruência de w}},
\]

omitindo filtros vazios. Palavras iguais em sua saída podem ser agregadas com coeficiente inteiro. Não se afirma que o número de filtros distintos seja sempre 2^m, nem que os módulos exibidos sejam sempre períodos mínimos.

Se q=2^d q_odd, o módulo de toda palavra divide

\[
D_m=2^{\max(d-m,0)}3^m q_{\mathrm{odd}}.
\]

Consequentemente L+^m F_{q,r} tem período que divide D_m. Há no máximo 2^m termos antes da agregação. Uma tabela completa nesse período pode exigir D_m entradas. A parte diádica diminui; a parte 3-ádica aumenta; os demais fatores primos iniciais não ganham novos expoentes.

Em particular, trabalhar apenas módulo q coprimo a 6 e usar inversos de 2 e 3 mantém uma dinâmica afim nesse módulo, mas perde a admissão inteira. É o filtro do ramo ímpar que força a resolução 3-ádica adicional.

## 5. Obstrução: nem a soma completa elimina o crescimento

Seja H_m(y)=L+^m 1(y), a quantidade de ancestrais a exatamente m passos, contando também passagens por ciclos, sem poda da árvore.

A palavra inteiramente ímpar tem

\[
b_1^m(y)=\frac{2^m(y+1)}{3^m}-1,
\]

e é admissível exatamente quando y≡−1 mod 3^m. É a única palavra com k=m. Todas as outras palavras têm filtros de módulos que dividem 3^{m−1}. Portanto

\[
H_m=H_m^{\mathrm{baixo}}+F_{3^m,-1},
\qquad H_m^{\mathrm{baixo}}\text{ tem período divisor de }3^{m-1}.
\]

Em y=3^m−1, deslocar por 3^{m−1} preserva a primeira parcela e muda a segunda de 1 para 0. H_m não tem período 3^{m−1}. Como possui período 3^m e seu período mínimo divide qualquer período, concluímos:

\[
\boxed{\text{O período mínimo de }L_+^m1\text{ é exatamente }3^m.}
\]

Isso prova a impossibilidade de representar toda a família num módulo fixo, mesmo após somar todos os ramos. Não prova que todo algoritmo exato necessite de 3^m operações: representações comprimidas e procedimentos para observáveis particulares continuam possíveis.

A média num período é também explícita. Cada palavra com k ímpares ocupa proporção 3^{−k}; existem binom(m,k) palavras assim. Logo

\[
\frac1{3^m}\sum_{y=1}^{3^m}H_m(y)=\sum_{k=0}^m\binom mk3^{-k}=(4/3)^m.
\]

É uma média entre classes da raiz, não uma previsão ponto a ponto nem uma amostra de passos independentes numa órbita positiva.

## 6. Normas uniformes: o que conseguimos preservar

Definimos R= L+/2 apenas como normalização de análise. Não é o operador de Haar P de Z2: R1=(1+F_{3,2})/2≠1.

Na norma sup, para f periódico,

\[
\|R^m f\|_\infty\le\|f\|_\infty.
\]

Sem essa normalização, a cota imediata é 2^m ||f||_∞. Essa é uma cota, não uma afirmação de crescimento exato.

Há uma melhora elementar: qualquer raiz tem no máximo três ancestrais em dois passos. Se y não é 2 módulo 3, há apenas um primeiro ramo e no máximo dois segundos ramos. Se y é 2 módulo 3, há dois primeiros ramos, mas 2y é 1 módulo 3 e só admite o ramo par no passo seguinte; o outro filho admite no máximo dois. A raiz 8 atinge três ancestrais (32, 10, 3). Pela positividade do operador,

\[
\|R^{2n}f\|_\infty\le(3/4)^n\|f\|_\infty,
\qquad \|R^{2n+1}f\|_\infty\le(3/4)^n\|f\|_\infty.
\]

Assim G_m converge uniformemente a zero nessa normalização. Isso também permite aproximação uniforme em sup por um conjunto finito de funções periódicas: as primeiras profundidades ficam exatas e as demais são pequenas. Não implica tal aproximação na norma A discutida a seguir, que é mais forte. E não controla a normalização natural de média um, F_m=(3/4)^m H_m: para ela, o limite triangular da norma A é (3/2)^m, e o limite sup de dois passos não fecha uma cota uniforme. A normalização por 2^m é adequada para a estimativa demonstrada, mas não resolve a dispersão relativa das árvores em sua escala (4/3)^m.

### Norma de Fourier absolutamente somável

Escreva f(y)=Σ_{t∈Q/Z} a_t e^{2πity}, com soma finita inicialmente, e ||f||_A=Σ|a_t|. Os coeficientes são únicos; mudar o período de representação apenas insere zeros. Seja A a conclusão desse espaço nessa norma.

Para o representante 0≤t<1 e e_t(y)=e^{2πity}, a identidade exata é

\[
R e_t(y)=\tfrac12 e_{2t}(y)
+\tfrac16\sum_{j=0}^2e^{-2\pi i(t+2j)/3}e_{(2t+j)/3}(y).
\]

Ela vem de expandir 1_{y≡2 mod 3} em três caracteres aditivos. A soma dos módulos dos quatro coeficientes é 1. Colisões de frequências apenas reduzem a cota triangular. Por linearidade,

\[
\boxed{\|R^m f\|_A\le\|f\|_A\quad(m\ge0).}
\]

R estende-se portanto continuamente a A. Trata-se de uma família infinita de caracteres **aditivos**, com denominadores controlados passo a passo. A operação não produz por si só um caráter multiplicativo de Dirichlet.

Essa prova dá uniformidade em m e em todo f da bola unitária de A; não há constantes ocultas dependentes do módulo. Não fornece traço, determinante, compacidade ou identidade com ζ.

### A resolução cresce, embora suas contribuições possam ficar pequenas

Para G_m=2^{−m}H_m e j não divisível por 3, o coeficiente de Fourier na frequência j/3^m vem somente da palavra inteiramente ímpar:

\[
\widehat G_m(j/3^m)=6^{-m}e^{2\pi ij/3^m}.
\]

Esses coeficientes são não nulos. A soma dos seus módulos é

\[
\varphi(3^m)6^{-m}=(2/3)2^{-m}.
\]

A escala mais fina é indispensável para representação exata, mas sua massa nessa norma decai. Isso não controla toda a cauda de frequências acima de um corte fixo: faltam as escalas intermediárias. Confundir esses dois enunciados daria um fechamento aproximado ainda não provado.

## 7. Comparação com o fechamento puramente diádico

Em Z2, f com módulo 2^d é uma função localmente constante. Os dois ramos estão sempre disponíveis. Uma composição de m ramos contrai por 2^{−m}; se m≥d, cada cilindro de paridades de comprimento m está contido numa classe módulo 2^d. Os 2^m cilindros repartem Z2 em classes de massa 2^{−m}. Por isso

\[
P^m f=\int f\,d\mu\quad(m\ge d).
\]

O filtro F_{2^d,r} torna-se exatamente a constante 2^{−d}. Essa propriedade usa Haar e admissão 2-ádica. Não vale para o operador R nos positivos, onde novas condições módulo 3 surgem a cada ramo ímpar.

## 8. Relação analítica possível com funções L

Para Re s>1, um filtro define uma série de Dirichlet

\[
D_{q,r}(s)=\sum_{n\ge1}F_{q,r}(n)n^{-s}.
\]

Escolha a∈{1,…,q} representando r e ponha d=gcd(a,q), q'=q/d, a'=a/d. Como gcd(a',q')=1, a ortogonalidade dos caracteres nas unidades dá

\[
D_{q,r}(s)=\frac{d^{-s}}{\varphi(q')}\sum_{\chi\bmod q'}\overline{\chi(a')}L(s,\chi).
\]

Para q'=1, a fórmula reduz a d^{−s}ζ(s). Logo os filtros transformados admitem decomposição finita em funções L, com módulos no máximo D_m. Em geral aparecem combinações lineares com fatores d^{−s}, não uma função L individual nem seu produto de Euler.

Para G_m, a série D_m(s)=Σ G_m(n)n^{−s} satisfaz |D_m(s)|≤ζ(Re s), uniformemente em m, por ||G_m||∞≤1. Em Re s≥1+δ, δ>0, isso dá uma constante independente de m. O crescimento do conjunto de condutores reaparece se tentarmos estimar a decomposição em funções L termo a termo perto da linha crítica.

Esta é uma relação exata entre filtros e funções L no semiplano absolutamente convergente. Não identifica seus zeros: zeros de combinações lineares não são automaticamente zeros dos termos. Uma continuação uniforme dessa família ainda requer argumento próprio.

## 9. Antecedentes e alcance bibliográfico

Fonte primária já arquivada: Applegate–Lagarias, *The Distribution of 3x+1 Trees*, Experimental Mathematics 4 (1995), 193–209, PDF `archive/fontes_etapa11/koopman_20260925/applegate_lagarias_1995_trees.pdf`, SHA-256 `cc3df1accda2bf5aa335f31c08215283f3354b4b490c1bfca19baeb98be02390`.

Nesta entrega foi relido o trecho de p. 195 (PDF p. 3) que define as pré-imagens e o papel das classes módulo 3^{k+1} nas **árvores podadas**. Isso é antecedente explícito da necessidade de resolução 3-ádica. Nossas contagens H_m são **não podadas**, sem excluir múltiplos de 3, e não substituem N*_m daquela fonte. Não se compara diretamente a fórmula de período ou a média sem ajustar as definições. A leitura anterior é registrada em `hipoteses/leituras/B13_APPLEGATE_LAGARIAS_1995_TREES.md`.

Consulta dirigida adicional: Monks et al., arXiv:1204.3904, resumo e metadados sobre grupos afins em módulos coprimos a 6. O PDF não foi usado como evidência nesta nota; a ligação com suas provas específicas fica pendente. A busca não foi uma revisão exaustiva de novidade. Nenhum resultado aqui recebe C por ausência de referência.

## 10. Verificações executadas

Código isolado em `collatz/`, conforme desvio registrado na CL0. Sem imports do instrumento espectral. Comandos:

```bash
.venv/bin/python -m pytest -q collatz/test_congruence_filters.py
.venv/bin/python results/collatz_filtros_20261011/verificar.py
```

- 7 testes passaram, em 0,13 s de parede reportados pelo pytest.
- 235.872 comparações exatas entre composição literal em frações, com integridade em cada prefixo, e congruência final.
- 26.208 comparações com contagem por **iteração direta** de T, independente da fórmula dos ramos inversos.
- Período mínimo e média verificados para m=1,…,7.
- 1.344 controles da média diádica para m≥d.
- Todos passaram. CPU do piloto 5,5215 s; parede 5,7305 s; pico do processo 18.508 KiB, conforme getrusage em Linux. Limite real de CPU 60 s via RLIMIT_CPU. Duração de obtenção/leitura/documentação não está incluída nessa medição.

As provas das §§2–8 são analíticas; testes finitos apenas conferem sua implementação. Norma de Fourier e decomposição em funções L não foram avaliadas numericamente. A declaração não autoriza enumerações extensas, e não houve ampliação.

## 11. Decisão e próximo alvo

O primeiro alvo fica **validado**, com resposta distinta para cada medida de complexidade:

| Medida | Resultado |
|---|---|
| Fórmula por palavra | Uma congruência; O(log q+m) bits nos parâmetros |
| Número de palavras antes de agregação | No máximo 2^m; a nota não elimina esse custo |
| Módulo comum | Divisor de D_m; crescimento 3-ádico exponencial possível |
| Módulo mínimo para H_m | Exatamente 3^m, demonstrado |
| Norma de R^m | ≤1 em Fourier A; em sup, ≤(3/4)^{floor(m/2)} |
| Aproximação por módulo fixo | Exata impossível; para G_m, aproximada uniforme em sup possível, mas cauda na norma A ainda não controlada |

**Próximo alvo matemático sugerido, não executado:** limitar, ou demonstrar uma obstrução a limitar,

\[
\sup_{m\ge0}\sum_{\operatorname{den}(t)>3^K}|\widehat G_m(t)|
\]

por uma função que tenda a zero quando K→∞. No caso G_m, todos os denominadores são potências de 3. A norma A≤1 e a massa da última escala não resolvem esse problema. É necessário tratar conjuntamente as escalas intermediárias e as fases dos resíduos das palavras.

Uma cota assim daria aproximação uniforme por memória aritmética finita. Sua negação também seria informativa. Antes de atribuir novidade ou executar campanha, confrontar o alvo com os resultados de árvores e funções 3-ádicas de Applegate–Lagarias e Wirsching. A ponte com zeros de funções L continua uma etapa adicional.

Para estudar heterogeneidade relativa das árvores, a família de média um F_m é mais pertinente que G_m. Transportar a eventual cota acima de G_m para F_m introduz o fator (3/2)^m e exige uma taxa adicional. Não fazer esse transporte sem prova; a prioridade científica entre esses dois alvos depende do confronto com a literatura.
