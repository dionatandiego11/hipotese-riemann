# Collatz: mistura L1 com custo e limites individuais — 13/10/2026

**Entrega:** derivação do alvo formulado em 12/10, aceitando a Proposição
7.3 de Tao como teorema externo. A demonstração abaixo explicita o
condicionamento, a cota de colisões e a normalização. Ainda não passou por
revisão independente; não reivindicar novidade bibliográfica.

Fonte externa: Tao, arXiv:1909.03562v5, §6, pp. 28–32 (estrutura do argumento)
e Proposição 7.3, p. 35 (estimativa profunda aceita). PDF arquivado:
`archive/fontes_etapa11/collatz_stationnaire_20261012/tao_1909.03562v5.pdf`,
SHA-256 99fa919e0e43f0c161fbdc8d9011069c92b57d2a2a09444ae2ca77ef826191dd.
Nesta sessão relida a redução de §6. A prova de renovação de §7 não foi
reconstruída. Não se assume RH nem a conjectura de Collatz.

## 1. Enunciado, sem mudança do observável

A_i são iid positivos com Pr(A_i=a)=2^{−a}. Defina

    S_j=A_1+...+A_j,
    X_n=Σ_{j=1}^n 3^{j−1}2^{−S_j} mod 3^n,
    E_{n,k}={S_n=n+k; A_i≤c_{n−i+1}, 1≤i≤n},
    c_r=2·3^{r−1}.

A probabilidade p^n_{n,k}=Law(X_n|E_{n,k}) é a dos geradores. p^m_{n,k}
é sua projeção, com o MESMO evento E, não uma distribuição independente.
Ponha

    O_{m,n}(k)=Σ_{a mod 3^n}
       |p^n_{n,k}(a)−3^{m−n}p^m_{n,k}(a mod 3^m)|.

**Proposição.** Fixados C,A>0 e ρ com

    α=log 3/(2 log 2)<ρ<1,

a derivação, dependente de Tao, dá

    sup_{|k−n|≤C√n} O_{m,n}(k) ≤ C_{A,C,ρ} n^{−A},

para todos os inteiros ceil(ρn)≤m≤n, quando n é suficientemente grande.
Constantes e início da faixa não foram numericamente avaliados. Para
ρ=0,9, isto é exatamente o regime do alvo anterior; não foi trocada a
norma ou reduzido o conjunto de custos depois de calcular uma tabela.

A proposição não diz que cada massa relativa fica próxima de 1, nem dá
minorante uniforme, densidade limitada ou confirmação numérica finita.

## 2. Medidas não normalizadas: a normalização ocorre só no fim

Se λ(Y)=Pr(X_n=Y,E_{n,k}), então sua massa é

    β_{n,k}=Pr(E_{n,k})=2^{−n−k}q_n(k).

Da razão de coeficientes da nota anterior e Stirling na janela central,
β_{n,k}≥b_C n^{−1/2}, com b_C>0, para n suficientemente grande.

Se T_m denota média nos cilindros mod 3^m,

    (T_m λ)(Y)=3^{m−n}Σ_{Y'≡Y mod3^m}λ(Y'),

então O_{m,n}(k)=β_{n,k}^{−1}||(I−T_m)λ||_1. T_m é contração em ℓ1.
Podemos descartar eventos de pequena massa antes de normalizar; cada
massa descartada η custa no máximo 2η nessa norma.

## 3. Concentração e escolha analítica do corte

Para J>0 escolhido em função do expoente final A, existe H>0 tal que

    G={|S_j−2j|≤H(√(j log n)+log n), 1≤j≤n;
       A_i≤H log n, 1≤i≤n}

satisfaz Pr(G^c)=O_J(n^{−J}). Este é um fato de concentração de geometrias,
não uma hipótese de paridades de órbitas. A função geradora de momentos
E exp(t A_i)=exp(t)/(2−exp(t)) é finita em torno de zero; a expansão
centrada tem logaritmo O(t²), dando a cota de Chernoff
2 exp(−c min(u²/j,u)) para S_j−2j. União nos j e a cauda Pr(A_i>b)≤2^{−b}
permitem escolher H grande e obter a afirmação.

Defina L0=log(4/3)>0 e

    B_H=H log2 + H²(log2)²/(2L0).

Escolha D>H+(B_H+3)/log2 ANTES de qualquer cálculo. Use o nível

    T=n log_2 3−D log n.

Em E_{n,k}, S_n=n+k>T para n grande na janela declarada. Há portanto
um primeiro R tal que S_R>T. Se os limites de G valem até R,

    T<S_R=t≤T+H log n,
    R=αn+O_H(√(n log n)),    L=n−R=(1−α)n+O_H(√(n log n)).

A restrição aos limites até R é um evento do prefixo apenas. O erro ao
remover os casos que a violam tem massa ≤Pr(G^c), pois tal violação
implica G^c. Assim não se mantém um evento de boa concentração do sufixo
que destruiria a separação dos blocos.

## 4. Injetividade e colisões no prefixo

Para uma tupla positiva do prefixo de tamanho R, considere o offset
racional exato

    x_R=Σ_{j=1}^R 3^{j−1}2^{−S_j}.

Se S_R=t, o numerador V=2^t x_R é um inteiro ímpar: o último termo é
3^{R−1}, os anteriores são pares. Logo v_2(x_R)=−t. Isso prova a
injetividade racional das tuplas por indução: igualdade de offsets implica
igualdade de t; subtrair o último termo 3^{R−1}2^{−t} recupera o offset
anterior, e por repetição recuperam-se todos os A_i.

Sob os limites de concentração do prefixo,

    x_R≤(1/3)n^{H log2}Σ_{j≥1}
       exp(−L0 j+H log2 √(j log n))
       ≤C_0 n^{B_H}.

A segunda desigualdade usa Young com metade de L0 j e soma a série
geométrica restante. Como t≤T+H log n, a escolha de D dá

    0<V=2^t x_R≤C_0 3^n n^{−D log2+H log2+B_H}<3^n

para n suficientemente grande. Para R,t fixos, dois offsets iguais mod
3^n têm numeradores inteiros congruentes no intervalo (0,3^n); logo são
iguais, e a injetividade racional dá a mesma tupla.

Se ν_{R,t} é a medida do offset do prefixo com as condições de corte,
concentração e soma t, cada átomo tem massa 2^{−t} ou zero. Portanto

    Σ_Y ν_{R,t}(Y)²≤2^{−t}Σ_Yν_{R,t}(Y)≤2^{−t},
    3^n Σ_Yν_{R,t}(Y)²≤n^{D log2},

já que t>T. Esse é o controle de colisões que impede pagar um fator
exponencial na soma de Fourier. Ele não foi inferido de gráficos.

## 5. Separação correta dos blocos, incluindo os limites

Depois de fixar R,t, vale exatamente

    X_n=x_R+3^R 2^{−t} X_L^{suffix} mod 3^n.

O custo restante é n+k−t. Os limites do sufixo são precisamente
A_{R+i}≤c_{L−i+1}; sua lei não normalizada é a de um gerador de
profundidade L, com custo k'=n+k−t−L. Se o custo for impossível, essa
medida é zero e o termo da decomposição desaparece.

Os limites do prefixo são inativos em nossos cortes: sua menor capacidade
é c_{L+1}=2·3^L, enquanto cada A_i≤t=O(n). Isso vale para n grande porque
L é uma fração positiva de n. Não foi substituído o limite original do
prefixo pelo limite de um gerador de profundidade R.

Antes do condicionamento global, as coordenadas são independentes; com
t fixado, o indicador do custo restante depende somente do sufixo. A
medida da peça é assim

    λ_{R,t}=ν_{R,t} * (3^R2^{−t})_*η_{L,k'},

onde η é a medida NÃO NORMALIZADA do sufixo com custo e limites. A
notação de push multiplica um resíduo mod 3^L pelo fator 3^R2^{−t}
para colocá-lo mod 3^n. Não se está afirmando que prefixo e sufixo sejam
independentes depois de impor E sem fixar t.

## 6. Cota do sufixo sem segunda divisão por probabilidade

Da derivação de pares da nota `COLLATZ_CUSTO_CONJUNTO_20261012.md`, para
qualquer custo do sufixo e caráter primitivo de condutor 3^d, d≤L,

    |η̂_{L,k'}(h)|≤E exp(−ε_T³ W_d)≪_B d^{−B}.

A afirmação é sobre o numerador não normalizado com indicador. Os pares
com soma 3 usam somente (1,2),(2,1), que respeitam TODOS os limites c_i≥2;
a soma total é fixada pelas somas dos pares e pelas coordenadas restantes.
As outras orientações têm módulo de média com indicador ≤1. A majorante
positiva não precisa ser dividida pela massa do sufixo.

A última desigualdade aceita a Proposição 7.3 de Tao; sua constante é
uniforme na frequência primitiva e no tamanho d. Essa é a única estimativa
profunda externa importada. Não se usou apenas a Proposição 1.17 nem a
mistura L1 não condicionada como conclusão pronta.

Para frequência ξ mod 3^n não pertencente a 3^{n−m}Z/3^nZ,

    v_3(ξ)<n−m,
    d=n−R−v_3(ξ)≥m−R+1≥(ρ−α)n−O_H(√(n log n)).

Logo d é uma fração positiva de n. Multiplicação por 2^{−t} não muda sua
valoração 3-ádica. A transformada do sufixo nesta frequência é O_B(n^{−B}),
uniformemente em R,t,k' e no caráter, sem condição adicional de centralidade
sobre o custo restante.

## 7. Plancherel, soma das peças e normalização

Usando Cauchy–Schwarz e Plancherel no grupo de 3^n elementos,

    ||(I−T_m)λ_{R,t}||_1
       ≤[Σ_{ξ∉3^{n−m}Z}|λ̂_{R,t}(ξ)|²]^{1/2}
       ≤C_B n^{−B}[Σ_ξ |ν̂_{R,t}(ξ)|²]^{1/2}
       =C_B n^{−B}[3^n Σ_Yν_{R,t}(Y)²]^{1/2}
       ≤C_B n^{−B+(D log2)/2}.

Há no máximo O_H(n²) peças R,t para n grande. O operador é linear, de
modo que a desigualdade triangular permite somá-las. Depois de dividir
somente pela massa global β_{n,k}≥b_C n^{−1/2},

    O_{m,n}(k)≤C n^{5/2−B+(D log2)/2}
                +C n^{1/2}Pr(G^c).

Escolha J>A+2, obtenha H e D, e então escolha
B>A+4+(D log2)/2 na estimativa externa. A expressão é O_{A,C,ρ}(n^{−A}).
As escolhas dependem do expoente e janela declarados, não dos resultados
numéricos. Isso conclui a derivação do enunciado.

## 8. Conclusão sustentada e limites

O alvo de oscilação L1 em m=ceil(0,9n) está fechado **como derivação
matemática dependente do teorema externo**. A estimativa também vale para
m≥ρn com ρ>α fixo. Não se estabeleceram constantes computáveis nesta
entrega, portanto não se certifica uma tolerância em um n finito.

Este resultado não resolve:

- min_a C_n p^n_{n,k}(a), ou sua minorante uniforme;
- distribuição das piores classes residuais e seu expoente;
- oscilação para m=o(n) por esta demonstração (a redução telescópica de
  Tao não pode ser copiada sem conferir a família condicionada);
- identificação espectral com ζ ou RH, ou a conjectura de Collatz.

A norma L1 permite exceções pequenas em massa total, incluindo classes
com probabilidade zero. A fórmula não garante aproximação uniforme por
resíduo. Os resultados anteriores de estacionária não limitada e módulos
logarítmicos permanecem compatíveis.

Próximo trabalho recomendado: auditoria desta derivação, principalmente
preservação dos pares, corte/injetividade e fatores de Plancherel. Só depois
formular um alvo para as piores classes ou para escalas sublineares.
Não usar a derivação como motivo automático para uma campanha extensa.

## 9. Verificações realmente executadas

Declaração anterior à implementação:
`results/collatz_mistura_condicionada_20261013/DECLARACAO.md`, SHA-256
e15f44f4818598622260e0909102ab021aa6c82d8e1ddea2d83810d65b3c8a99.

- 150 identidades integrais de decomposição em blocos: passaram.
  Prefixo usa os limites originais de n; sufixo usa os de n−R; fator
  3^R2^{−t} e custo restante são explícitos.
- 714 offsets racionais de composições positivas: distintos em seus grupos
  de R,t. 712 offsets no intervalo declarado também passaram na conferência
  modular. Dois ficaram fora do intervalo, não foram falhas de injetividade.
- CPU 0,2231 s; parede 0,2439 s; RSS reportado 265.244 KiB, não memória
  incremental do algoritmo. RLIMIT_CPU=60 s respeitado.
- Nenhuma tabela de oscilação foi calculada; o diagnóstico não verifica
  um limite assintótico nem substitui a prova de Tao ou revisão independente.

Comando:

    PYTHONPATH=. python3 results/collatz_mistura_condicionada_20261013/verificar.py

Sem dados de zeros, aleatoriedade, CL1, enumeração extensa, publicação ou
commit. Código externo não executado; módulos anteriores não modificados.
