# Construção por núcleo de primos e peso de denominadores em Collatz

22/11/2026. Derivações A com hipóteses explícitas, controles B sob declaração anterior e propostas D. A leitura externa de RH é a documentada em `ARQUITETURA_ALPOGE_20261122.md`; não é prova verificada pelo nosso projeto. Os antecedentes de Weil/Suzuki tornam obrigatória a comparação bibliográfica; nenhuma novidade é anunciada.

## 1. Correção exata do traço suavizado

Para x>1, a inversão de Mellin de

    −ζ'(s)/[ζ(s)s(s−1)] − 1/(s−1)^2 + (1+γ)/(s−1)

tem resíduo log(2π) em0 e resíduo −1/[2k(2k+1)] em cada zero trivial −2k. A fórmula explícita suavizada da fonte, com as contribuições triviais escritas integralmente, dá

    G(x)=log(2π)−Σ_ρ x^ρ/[ρ(ρ−1)] + R(x),
    R(x)=−Σ_{k>=1} x^(−2k)/[2k(2k+1)].                    (1)

Usa-se a mesma justificativa de inversão de contorno da fórmula explícita citada na exposição; esta nota identifica os resíduos e fecha o resto trivial, mas não é uma nova demonstração completa dessa fórmula. A soma dos zeros é com multiplicidade. Para q=x^−2,

    |R(x)| <= q/[6(1−q)],
    |R(x)+Σ_{k=1}^M q^k/[2k(2k+1)]|
        <= q^(M+1)/[(2M+2)(2M+3)(1−q)].                  (2)

O resto também tem expressão fechada

    R(x)=1/2 log(1−x^−2) + x atanh(1/x) − 1.

Em x=1, seu limite é log2−1: decompor 1/[2k(2k+1)]=1/(2k)−1/(2k+1). A divergência aparente dos termos da expressão fechada se cancela; o código usa o limite explicitamente em0 e precisão controlada nos pontos declarados. O código não é uma avaliação estável certificada para todo t arbitrariamente próximo de0 ou enorme.

Defina K(t), par, usando x=e^|t|:

    K(t)=e^(−|t|/2)[G(e^|t|)−log(2π)−R(e^|t|)], t≠0,
    K(0)=2+γ−log(4π).

Sob RH, (1) implica

    K(t)=Σ_γ m_γ e^(itγ)/(γ²+1/4),                       (3)

onde γ varia agora sobre as ordenadas distintas, positivas e negativas, e m_γ é a multiplicidade. A soma é absolutamente convergente, uniforme em t, pela contagem N(T)=O(T log T); seu limite em0 coincide com a expressão anterior. Portanto K é contínua e positiva definida:

    Σ_{i,j} c_i conjugado(c_j)K(t_i−t_j)
      =Σ_γ [m_γ/(γ²+1/4)] |Σ_i c_i e^(it_iγ)|² >=0.      (4)

Essa é uma consequência global condicionada à fórmula explícita e RH, não uma conclusão inferida de uma matriz finita.

## 2. Um operador autoadjunto definido pelo núcleo

A positividade permite uma construção funcional concreta: tome os símbolos v_t e dê ao seu espaço linear a forma de Gram K(t−u). Quociente os vetores de norma zero e complete. A translação U(a)v_t=v_{t+a} preserva a norma e é fortemente contínua, pois K é contínua. Pelo teorema de Stone, existe um gerador autoadjunto H_cyc com U(a)=exp(iaH_cyc), cujo domínio são os vetores em que (U(a)v−v)/(ia) tem limite de norma quando a→0.

O espaço e a translação são definidos usando a expressão prima para K, sem consultar uma tabela de zeros. Sob (3), a representação espectral é L²(μ), onde

    μ=Σ_γ m_γ/(γ²+1/4) δ_γ,
    H_cyc f(λ)=λf(λ),
    D(H_cyc)={f:∫λ²|f(λ)|² dμ(λ)<∞}.

Os exponenciais geram todo L²(μ): um vetor ortogonal a todos eles daria uma medida finita com transformada de Fourier nula, logo seria zero. Assim o espectro de H_cyc tem como conjunto as ordenadas. Essa construção é uma realização espectral abstrata, ainda sem geometria local ou interação física.

**Multiplicidade é uma distinção essencial.** O operador cíclico tem dimensão1 por átomo distinto: m_γ aparece na massa de μ, não na multiplicidade espectral de H_cyc. Portanto não se pode identificar seu traço de resolvente com K se houver zeros múltiplos. Se todos forem simples, então K(t)=Tr[exp(itH_cyc)(H_cyc²+1/4)^−1]. Sem simplicidade, pode-se construir uma ampliação com fibra C^{m_γ}, recuperando as multiplicidades de (γ²+1/4)μ({γ}); essa ampliação usa a informação espectral da fórmula e não é dinâmica física deduzida. A frase "a positividade já encontrou o Hamiltoniano físico" seria incorreta.

**Antecedentes:** [Suzuki, Aspects of the screw function](https://arxiv.org/abs/2206.03682), [screw line](https://arxiv.org/abs/2209.04658) e [Hilbert space from Weil distribution](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/on-the-hilbert-space-derived-from-the-weil-distribution/FD33EBD117A6B448053450DD8D62ADB6). Busca identificou essas construções; seus enunciados específicos precisam de leitura integral antes de reivindicar relação exata com este núcleo, que tem peso 1/(γ²+1/4), diferente de 1/γ². Positividade, reconstrução cíclica e Stone são ferramentas conhecidas, não novidade atribuída ao projeto.

**Novo alvo H2 (D):** realizar H_cyc, ou uma ampliação justificada, como operador em espaço aritmético/geometricamente especificado sem reconstruí-lo apenas pelo núcleo. Conferir a fórmula de traço e multiplicidades, antes de atribuir uma interpretação física. O ganho desta etapa é ter espaço, domínio e translação definidos e saber exatamente o que ainda falta.

## 3. Peso aritmético para Collatz

Para a palavra de paridades ε_0,...,ε_{n−1}, o mapa com ramo ímpar (ax+b)/2 e par x/2 tem composição (Ax+B)/2^n, com

    A_0=1, B_0=0,
    A_{j+1}=a^{ε_j}A_j,
    B_{j+1}=a^{ε_j}B_j+ε_j b2^j.

O ponto fixo racional é x=B/(2^n−A). Para os dois mapas usados, T=(a,b)=(3,1) e S=(1,−1), esse denominador é ímpar e não nulo. A codificação por paridade dá2^n pontos distintos em Z₂; a implementação confere ainda todas as paridades por iteração racional independente da fórmula de composição.

Se d(x) é o denominador reduzido positivo de x, ele é constante ao longo de cada órbita racional periódica. Para T, o denominador inicial é coprimo com3, pois divide2^n−3^k (k>=1; no caso k=0, x=0); os passos dividem por2 ou multiplicam numerador por3 e somam o denominador, preservando a forma reduzida. Para S, multiplicar por1 e subtrair o denominador também preserva. Isso fundamenta o peso multiplicativo por passo d(x)^{−s}.

Defina, para s>=0,

    Z_n(s)=Σ_{T^n x=x} d(x)^(−sn),
    ζ_den(z,s)=exp(Σ_{n>=1} Z_n(s) z^n/n).

É uma zeta periódica ponderada, bem definida ao menos para |z|<1/2, já que 0<Z_n(s)<=2^n. Formalmente ela tem produto sobre órbitas primitivas de comprimento ℓ e denominador d:

    ζ_den(z,s)=Π_orbitas [1−z^ℓ d^(−sℓ)]^−1.

Não se identificou um determinante de Fredholm nem um operador ilimitado para essa expressão; isso exige espaço funcional e hipóteses próprias.

**Separação exata no período2:**

    Fix(T²)={0,−1,1,2},    Z_2^T(1)=4;
    Fix(S²)={0,−1,−1/3,−2/3},    Z_2^S(1)=20/9.

Ambos têm4 pontos sem peso. O peso detecta a aritmética dos pontos racionais na mesma coordenada x; se fosse transportado pela conjugação, os dados seriam iguais. A diferença não é uma quebra de invariância: compara observáveis distintas sob a conjugação. Não é evidência de relação com a zeta de Riemann.

À medida que s→∞, os coeficientes Z_n(s) selecionam os pontos periódicos inteiros. Pode-se ainda inserir a indicação x>0, invariante nas órbitas periódicas, para selecionar os ciclos inteiros positivos. Se o único ciclo positivo for{1,2}, a zeta assim filtrada seria1/(1−z²). Mesmo provar isso excluiria apenas outros ciclos; trajetórias divergentes dos inteiros positivos não são detectadas por essa contagem periódica. Aqui se calcula somente até n=8.

**Novo alvo C2 (D):** investigar se a série ponderada admite operador natural e estimativas uniformes que controlem a seleção de inteiros. Ler antecedentes de zetas de altura e dinâmica aritmética antes de atribuir novidade; não escolher fatores locais para forçar um produto sobre primos.

## 4. Controles executados e leitura

Declaração anterior à implementação: `results/hamiltoniano_collatz_20261122/DECLARACAO.md`, SHA-256 `00a66149edf2aeb2636f477e2aa61db287e0418fc6c2198ecf735a8cb531853a`. Grade fixa: períodos1–8; resto trivial em t=1/4,1/2,1,2,3; Gram de6 nós; teto60s CPU. A execução fornece testes, tabelas e manifesto no mesmo diretório. A matriz de Gram é diagnóstico de ponto flutuante, não certificado.

A primeira chamada do runner falhou no import do pacote local `collatz`, antes de calcular ou gerar manifestos. Corrigiu-se apenas o caminho de importação do runner e repetiu-se; escopo e método científico não foram modificados. Os artefatos registram a execução que chegou às verificações; a ocorrência inicial fica documentada aqui.

**Resultado efetivo:**3 testes passaram em0,40s. CPU acumulada do runner e filho:0,982002s; parede1,108816s. Foram conferidos1.020 pontos dos dois mapas, incluindo paridades, fechamento da órbita e invariância do denominador; o período2 teve a separação prevista. O filtro positivo inteiro deu2 pontos nos períodos pares de T até8 e0 nos ímpares, sem inferência para períodos maiores. A matriz de Gram6×6 teve menor autovalor float0,01722477; K(0)=0,04619141793224..., diagnóstico compatível com a positividade teórica. A expressão fechada do resto concordou com a série independente dentro da tolerância de desenvolvimento1e-55 e da cauda analítica nos cinco t declarados; isso não é certificação intervalar. Nenhum zero da zeta foi usado como entrada.

Próximo trabalho: revisão de R(x)/núcleo e antecedentes; para H, estrutura geométrica e multiplicidades; para Collatz, espaço de transferência para o peso de denominadores e um enunciado que controle inteiros, antes de ampliar períodos. Cálculos novos sobre zeros, matrizes ajustadas a zeros e inferências de convergência da conjectura não fazem parte desta etapa.
