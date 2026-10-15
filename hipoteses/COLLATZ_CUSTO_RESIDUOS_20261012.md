# Collatz: custo condicionado e resolução residual — 12/10/2026

Estado: identidades e cota local de custo `validado` por derivação elementar,
com verificações finitas exatas. Controle relativo uniforme em resíduos
`inconclusivo`. Não se assume RH nem a conjectura de Collatz. Sem afirmação
de novidade; a recorrência e os geradores são de Wirsching.

## 1. Objeto e convenção

Mapa acelerado T(n)=n/2 para n par, (3n+1)/2 para n ímpar. Fonte:
Wirsching, cópia preliminar arquivada, pp. 7–8, eq. (2.1); identificação
completa e SHA-256 em `leituras/B31_WIRSCHING_PREDECESSORES_2003.md`.
Não confundir estes geradores com e_ℓ, com sua convolução em partições,
nem com a contagem H_m de profundidade total da entrega anterior.

Defina c_i=2·3^{i−1}, i≥1, e

    g_0(k,a)=1 se k=0 e a∈Z3, zero nos demais casos;
    g_ℓ(k,a)=Σ_{0≤j<c_ℓ} g_{ℓ−1}(k−j,(2^{j+1}a−1)/3).

Argumentos fora do domínio válido contribuem zero. Para ℓ≥1 o suporte
está em unidades a∈Z3^× e 0≤k≤3^ℓ−ℓ−1; g depende de a mod 3^ℓ.
Use Haar normalizada nas unidades. Com C_ℓ=2·3^{ℓ−1},

    q_ℓ(k)=Σ_{a∈(Z/3^ℓ)^×}g_ℓ(k,a)=C_ℓ·ḡ_ℓ(k),
    Q_ℓ(z)=Σ_k q_ℓ(k)z^k=∏_{i=1}^ℓ(1+z+...+z^{c_i−1}).

q_0(0)=1. Os custos j_t em uma tupla que vai da raiz à folha têm limites
0≤j_t<c_{ℓ−t+1} e soma k. Com d_0=0,

    d_t=2^{j_t+1}d_{t−1}+3^{t−1},
    B_{j_ℓ}∘...∘B_{j_1}(a)=(2^{k+ℓ}a−d_ℓ)/3^ℓ.

Cada tupla determina exatamente uma unidade

    a=d_ℓ·2^{−(k+ℓ)} mod 3^ℓ.

A integridade final implica a de todos os prefixos: os fatores restantes
são unidades em 3, portanto a divisibilidade final força cada divisibilidade
intermediária. A soma dos geradores conta todas as tuplas, demonstrando o
produto Q_ℓ. A escolha do representante modular não altera o levantamento.

## 2. Kernel conjunto exato

Para q_ℓ(k)>0 defina p_{ℓ,k}(a)=g_ℓ(k,a)/q_ℓ(k). Então

    w_{ℓ,k}(j)=q_{ℓ−1}(k−j)/q_ℓ(k),  0≤j<c_ℓ;
    a=(3b+1)2^{−j−1} mod 3^ℓ,
    b distribuído segundo p_{ℓ−1,k−j}.

Isso é uma mistura condicionada ao custo, não um modelo de paridades
independentes de órbitas. Na base ℓ=1 usa-se b=0 mod 1. Cada levantamento
é injetivo nos resíduos b mod 3^{ℓ−1}; portanto preserva as contagens.

Projetar a mod 3^K só exige b mod 3^{K−1}, mas conserva os estados de custo
k−j. O fechamento de médias a profundidade fixa por Q, com pesos 3/4 e 1/4,
não fornece o fechamento deste problema condicionado.

## 3. Proposição: cauda uniforme do custo de um ramo

Para ℓ≥16, 0≤k≤2ℓ e inteiro J≥0,

    Σ_{j≥J} w_{ℓ,k}(j) ≤ min(1,5(4/5)^J).

É uma cota absoluta de probabilidade, uniforme em ℓ e k nesse domínio.
A janela k=ℓ+O(√ℓ) da fonte fica dentro do domínio para ℓ suficientemente
grande, com o início dependente da constante da janela.

**Prova.** Seja L o número de índices i≤ℓ−1 com c_i≤k, e d=ℓ−1−L.
Até o grau k, Q_{ℓ−1}(z) coincide com V(z)(1−z)^{−d}, onde V tem
coeficientes não negativos (produto dos fatores cujos limites são pequenos).
Como k≤2ℓ,

    L≤1+floor(log_3 ℓ),   d−1=ℓ−2−L≥ℓ/2,  para ℓ≥16.

A última desigualdade segue de 1+log_3 ℓ≤ℓ/2−2: vale em 16 e a diferença
é crescente daí em diante. Para r≥t≥0,

    binom(r−t+d−1,d−1)/binom(r+d−1,d−1)
      =∏_{i=0}^{t−1}(r−i)/(r+d−1−i)
      ≤(k/(k+d−1))^t ≤(4/5)^t,   r≤k.

Quando t>r o coeficiente do numerador é zero. Aplicando a desigualdade
termo a termo na convolução com V,

    q_{ℓ−1}(k−t)≤(4/5)^t q_{ℓ−1}(k).

O termo j=0 dá q_ℓ(k)≥q_{ℓ−1}(k)>0. Somar a série geométrica prova a
cota; k=0 é imediato. A restrição j<c_ℓ só reduz a soma.

Esta prova não usa a contagem experimental de resíduos ou a hipótese
conjectural de Wirsching. A cauda aqui é do ramo j condicionado por k;
não é a cauda de partições da Conjectura 1/Lema 4.2 de Tavares.

## 4. O que o truncamento preserva — e o que ainda falta

Omitir j≥J perde massa η≤5(4/5)^J. Renormalizar a mistura restante, quando
não vazia, muda sua lei conjunta (j,b) em variação total exatamente η;
após projetar para a, a distância é no máximo η. Logo J independente de ℓ
basta para uma precisão **absoluta** fixa na distribuição de um passo.
Não foi demonstrado controle acumulado dessa aproximação ao longo de ℓ
passos; tal controle exigiria propagar erros entre os estados de custo.

Entretanto o alvo relativo de Wirsching é

    g_ℓ(k,a)/ḡ_ℓ(k)=C_ℓ p_{ℓ,k}(a).

Uma cota absoluta η dá apenas erro relativo aditivo ≤C_ℓη por resíduo.
Para garantir erro ≤ε por esta rota é suficiente exigir

    5C_ℓ(4/5)^J≤ε,
    J≥log(5C_ℓ/ε)/log(5/4).

Essa condição suficiente cresce linearmente com ℓ. Não prova que J fixo
seja impossível: mostra que a cota absoluta obtida não basta para o alvo
relativo. Nem estabilidade em variação total fixa garante massa positiva
em todas as classes, cuja massa Haar é 1/C_ℓ.

**Resposta ao alvo:** a família conjunta tem evolução exata e o custo local
é controlável na janela central. A resolução residual exata ainda cresce
como 3^ℓ. Não foi obtida uma redução uniforme que preserve as estimativas
relativas da Conjectura 2. O obstáculo agora está definido por uma fórmula,
em vez de uma analogia espectral.

## 5. Execução limitada e reprodutibilidade

Declaração anterior à implementação: `results/collatz_custo_residuos_20261012/DECLARACAO.md`,
SHA-256 ed3b3e302f2905f1c2ebf76f6af95be6b0768c894dae5b61a7439bf7da960fb3.
Inteiros Python e Fraction; nenhum dado de zeros ou órbitas extensas.

- 48 identidades g versus composição afim e produto Q: passaram.
- 181 conferências de projeção e conservação de massa: passaram.
- 60 desigualdades de cauda nos níveis 16,24,32,64: passaram.
- 18 testes rápidos (5 novos e 13 anteriores): passaram.
- CPU 0,156 s; parede 0,156 s; ru_maxrss informado pelo processo: 261.412 KiB.
  Esse campo é relatado como retornado pelo sistema, não como medição de
  memória incremental do algoritmo. Teto RLIMIT_CPU=60 s respeitado.

Comandos:

    PYTHONPATH=. python3 results/collatz_custo_residuos_20261012/verificar.py
    .venv/bin/python -m pytest -q collatz/test_cost_residues.py collatz/test_congruence_filters.py collatz/test_coarse_memory.py

O Python do sistema não tem pytest; a primeira tentativa de testes não
executou testes. O ambiente .venv executou os 18 acima. Artefatos anteriores
não foram reexecutados nem modificados. Sem commit ou campanha extensa.

## 6. Próximo alvo matemático

Estimar discrepância residual condicionada ao custo, por exemplo

    max_a |C_ℓ p_{ℓ,k}(a)−1|,

ou obter uma minorante positiva suficiente no domínio e quantificadores
de Wirsching. Não presumir que a distribuição tende à uniforme: o alvo
acima é um diagnóstico matemático possível, mais forte que uma minorante.
Uma abordagem a investigar é acompanhar os caracteres aditivos de módulo
3^K no kernel condicionado, com dependência explícita em K e ℓ, e separar
as escalas K fixo e K=ℓ. Antes de calcular uma grade maior, derivar a
recorrência dessas observáveis e decidir qual estimativa seria suficiente.
Não constitui ligação nova com zeros de ζ nem estratégia estabelecida de RH.
