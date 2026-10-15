# Collatz: limite central em módulos fixos — 12/10/2026

**Conclusão:** para |k−ℓ|≤C√ℓ, C fixo, os resíduos dos geradores de
Wirsching convergem em cada módulo 3^K fixo a uma probabilidade π_K
não uniforme. As massas são positivas em todas as unidades. Nenhuma
estimativa uniforme com K=ℓ foi obtida. Derivação elementar, classificação
A no escopo indicado; diagnósticos finitos exatos separados. Sem RH,
conjectura de Collatz ou reivindicação de novidade bibliográfica.

Base: eq. (2.1) de Wirsching, preliminar pp. 7–8, fonte arquivada e
identificada em `leituras/B31_WIRSCHING_PREDECESSORES_2003.md`.
Não atribuir a prova abaixo à fonte. É uma derivação a partir de seus
geradores, sujeita a revisão matemática independente.

## 1. Teorema de custos iniciais

Escolha uniformemente uma das q_ℓ(k) tuplas de custos permitidas, com
j_1,...,j_ℓ em ordem da raiz para a folha. Para qualquer R fixo e qualquer
j_1,...,j_R fixos, com S=j_1+...+j_R,

    Pr(j_1,...,j_R | total=k)
      =q_{ℓ−R}(k−S)/q_ℓ(k) →2^{−R−S},

uniformemente nos inteiros |k−ℓ|≤C√ℓ, com C fixo. Os limites de custo
c_ℓ,...,c_{ℓ−R+1} deixam de restringir essa tupla para ℓ suficientemente
grande. O limite é o produto de R leis geométricas

    Pr(J=j)=2^{−j−1}, j≥0.

A convergência da lei conjunta ocorre também em variação total para R
fixo. Não se afirma independência das paridades de órbitas positivas:
é uma lei limite de contagens condicionadas de geradores.

### Prova por coeficientes

Ponha B_ℓ(k)=binom(k+ℓ−1,ℓ−1) e

    Q_ℓ(z)=(1−z)^{−ℓ}A_ℓ(z),
    A_ℓ(z)=∏_{i=1}^ℓ(1−z^{c_i}), c_i=2·3^{i−1}.

Para subconjunto finito E dos índices, D_E=Σ_{i∈E}c_i. A inclusão-exclusão
dá exatamente

    q_ℓ(k)/B_ℓ(k)=Σ_{E⊆{1,...,ℓ}}(−1)^{|E|}
          B_ℓ(k−D_E)/B_ℓ(k),

com B_ℓ negativo em custo interpretado como zero. Para D≤k,

    B_ℓ(k−D)/B_ℓ(k)
       =∏_{t=0}^{D−1}(k−t)/(k+ℓ−1−t)
       ≤[k/(k+ℓ−1)]^D.

Para D>k a razão é zero. Na janela declarada, para ℓ suficientemente
grande a base da majorante é ≤3/5; para cada D fixo a razão converge
uniformemente a 2^{−D}. A soma sobre todos os subconjuntos finitos é
dominada por uma série somável, pois

    Σ_E (3/5)^{D_E}=∏_{i≥1}(1+(3/5)^{c_i})<∞.

Logo, por convergência dominada uniforme (primeiro uma parte finita,
depois a cauda comum),

    q_ℓ(k)/B_ℓ(k) → A(1/2)=∏_{i≥1}(1−2^{−c_i})>0.

A positividade decorre de Σ_i2^{−c_i}<∞ e de cada fator estar em (0,1).
O mesmo limite vale para ℓ−R,k−S, que permanece em uma janela central
com constante ligeiramente maior. Por cancelamento desses dois limites,

    q_{ℓ−R}(k−S)/q_ℓ(k)
       ~ B_{ℓ−R}(k−S)/B_ℓ(k)
       = [(ℓ−1)_R (k)_S]/(k+ℓ−1)_{R+S}
       →2^{−R−S}.

Aqui (x)_r é o fatorial decrescente. Não se tomou um limite em que R
cresce. A convergência uniforme em cada tupla finita implica TV uniforme:
escolha um conjunto finito de tuplas que contenha massa limite >1−ε;
a convergência nesse conjunto limita também a massa complementar. A lei
limite soma 1, afastando perda de massa no infinito.

## 2. Teorema de resíduos em módulo fixo

O resíduo módulo 3^K depende somente dos primeiros K custos. De fato,
cada levantamento a=(3b+1)2^{−j−1} faz a dependência em b perder um
dígito 3-ádico. Iterar K vezes deixa a entrada final apenas módulo 1.
O mapa das tuplas para o resíduo é independente de ℓ, quando ℓ≥K.
Assim, a convergência TV anterior pode ser projetada e fornece

    p^K_{ℓ,k} → π_K, uniformemente em |k−ℓ|≤C√ℓ,

para K fixo. π_0 é a massa única módulo 1, e π_K é a mistura

    a=(3b+1)2^{−J−1} mod 3^K,
    b~π_{K−1},  Pr(J=j)=2^{−j−1}, independentemente.

Como a ordem de 2 módulo 3^K é d_K=2·3^{K−1}, a soma infinita pode ser
agrupada exatamente:

    Pr(J≡r mod d_K)=2^{d_K−r−1}/(2^{d_K}−1), 0≤r<d_K.

A ordem declarada é elementar: a ordem módulo 3 é 2, e
v_3(4^{3^t}−1)=t+1, por expansão binomial/indução; portanto a ordem
cresce por um fator 3 a cada nível. Não é hipótese experimental.

### Valores exatos

| Unidade a | π_1(a), módulo 3 |
|---|---|
| 1 | 1/3 |
| 2 | 2/3 |

| Unidade a | π_2(a), módulo 9 |
|---|---|
| 1 | 8/63 |
| 2 | 16/63 |
| 4 | 11/63 |
| 5 | 4/63 |
| 7 | 2/63 |
| 8 | 22/63 |

Massas em múltiplos de 3 são zero. A projeção de π_2 coincide com π_1.
Os valores resultam de contas racionais de uma mistura de seis ramos,
não de ajuste aos dados.

## 3. Operador limite e distinção dos operadores anteriores

No módulo 3^K defina D(x)=x/2 e O(x)=(3x+1)/2. A mistura geométrica
pode ser escrita, usando projetividade,

    π_K=Σ_{j≥0}2^{−j−1}D_*^j O_*π_K.

Separar j=0 e reindexar o restante dá

    π_K=(1/2)O_*π_K+(1/2)D_*π_K.

Logo π_K é a estacionária da mistura com pesos 1/2,1/2. É diferente do
operador com pesos 3/4,1/4 da contagem a profundidade total apresentada
em `COLLATZ_MEMORIA_FINITA_20261012.md`. As normalizações e condicionamentos
são diferentes; não reutilizar suas estacionárias 3/7 e 4/7 aqui.

A estacionária deste novo kernel é única em cada módulo: acople dois
estados usando a mesma sequência de mapas. D preserva distância 3-ádica,
O a reduz por fator 3; após K ocorrências de O os estados coincidem
mod 3^K. O erro de acoplamento é majorado por Pr[Binomial(m,1/2)<K].
Isso prova a unicidade e convergência do kernel **limite**. Não é uma taxa
para a cadeia finita condicionada por custo, cuja aproximação ao kernel
limite precisaria ser controlada separadamente.

Os π_K são projetivos e determinam uma probabilidade em Z3, suportada
nas unidades. Não se demonstrou que tenha densidade contínua, limitada
ou uniformemente positiva em Haar.

Cada π_K dá massa positiva a todas as unidades: escolha qualquer b de
massa positiva; conforme r percorre 0..d_K−1, o fator 2^{−r−1} percorre
todas as unidades e 3b+1 é unidade. A menor massa nesse argumento depende
de K; não fornece uma minorante positiva uniforme em K.

## 4. Consequências para a direção de pesquisa

Haar não é o limite central, já em módulo 3. Portanto a hipótese de
convergência uniforme a Haar seria falsa nesse domínio. Isso **não**
refuta a condição suficiente anterior D_ℓ<3/2: pequena discrepância a
Haar e minorante positiva não exigem convergência a Haar.

O alvo mais adequado é separar dois problemas:

1. Regularidade da família π_K: existe inf_K min_{a unidade} C_Kπ_K(a)>0?
   Ou existe outra referência/mecanismo que dê a minorante necessária?
2. Aproximação de p^K_{ℓ,k} por π_K quando K cresce com ℓ, no nível relativo
   exigido pelo programa de Wirsching.

Para K=1 a menor densidade relativa é 2/3; para K=2 é 4/21. Esses dois
valores não provam decadência ao longo de K nem impossibilidade de uma
minorante uniforme. Não se propõe enumeração extensa para decidir isso.
A prova entregue fixa K antes do limite ℓ→∞ e não permite trocar os limites.

Esta formulação é uma ponte interna entre geradores e um operador limite.
Não identifica uma dinâmica espectral de ζ, não recupera logaritmos
discretos e não implica RH ou a conjectura de Collatz. Antecedentes
bibliográficos da lei estacionária específica ainda devem ser comparados
antes de qualquer classificação de novidade.

## 5. Verificações e custo

Declaração anterior à implementação:
`results/collatz_centro_20261012/DECLARACAO.md`, SHA-256
74f781b329d22446694ea482defbb93a74326564a9f0f40b5ac56278bf7d51fa.

- Leis dos módulos 3/9 conferidas por mistura geométrica e solução racional
  independente do sistema estacionário de 3/9 estados: passaram.
- Projeção 9→3: passou.
- 24 testes rápidos: passaram; 3 novos e 21 anteriores.
- Diagnóstico finito de 24 pares (ℓ,k,K) com ℓ=16,32,64,128, K=1,2:
  contagens projetadas exatas, sem construir resíduos módulo 3^ℓ.
- Para k=ℓ, TV no módulo 9 foi aproximadamente 0,02968; 0,01449;
  0,00716; 0,00356. É diagnóstico, não prova ou estimativa certificada
  da taxa assintótica. Frações exatas estão em resultados.json;
  floats servem exclusivamente à apresentação.
- CPU 0,044 s; parede 0,045 s; pico RSS 16.684 KiB; RLIMIT_CPU=60 s.

Comandos:

    PYTHONPATH=. python3 results/collatz_centro_20261012/verificar.py
    .venv/bin/python -m pytest -q collatz/test_central_residues.py collatz/test_residue_characters.py collatz/test_cost_residues.py collatz/test_congruence_filters.py collatz/test_coarse_memory.py

Código independente: `collatz/central_residues.py`. Nenhum dado reservado,
zero, CL1, campanha de órbitas, publicação ou commit. Próximo alvo
analítico: regularidade/minorante da estacionária π, com revisão dirigida
dos antecedentes antes de ampliar K.

## Atualização bibliográfica e de regularidade posterior

π_K coincide exatamente com Syrac de Tao (v5, Lema 1.12 e Remark 1.13); os números acima já aparecem na fonte. A nota `COLLATZ_REGULARIDADE_PI_20261012.md` deriva densidade L1 aceitando sua Proposição 1.14, mas exclui densidade limitada pelo ramo fixo em −1. Minorante uniforme e estimativas em custo condicionado continuam sem decisão. Esta atualização não modifica a prova anterior de limite em módulo fixo.
