# Caracteres residuais condicionados ao custo — 12/10/2026

Estado: recorrência e critérios suficientes `validado` por álgebra finita;
estimativas de cancelamento e minorantes relativas `inconclusivo`.
Base: geradores de Wirsching, eq. (2.1), preliminar pp. 7–8, arquivado
com referência completa na nota B31. As identidades abaixo são derivadas
dessa recorrência; não são atribuídas como teoremas novos à literatura.
Nenhuma hipótese RH/Collatz ou reivindicação de novidade.

## 1. Transformada correta

Mantêm-se g_ℓ(k,a), q_ℓ(k), p_{ℓ,k} e w_{ℓ,k} da entrega anterior.
Para 0≤K≤ℓ, use a projeção da probabilidade p_{ℓ,k} em Z/3^K e defina,
com convenção de sinal positivo,

    P̂^K_{ℓ,k}(h)=Σ_a p_{ℓ,k}(a) exp(2πi h a/3^K).

A expressão só é probabilística quando q_ℓ(k)>0. Na implementação usa-se
a soma não normalizada H^K_{ℓ,k}=q_ℓ(k)P̂^K_{ℓ,k}, que é zero fora do
suporte; isso evita dividir por zero nos estados intermediários.

Haar normalizada nas unidades tem transformada

    û_K(h)=1                 se h=0 mod 3^K;
           −1/2              se h≠0 e 3^{K−1} divide h;
           0                 nos demais casos.

Prova: a soma de caracteres sobre as unidades é a soma sobre todos os
resíduos menos a soma sobre os múltiplos de 3; ambas são séries geométricas.
Assim, comparar todos os caracteres não triviais com zero é incorreto.
Para K=1, as duas frequências não triviais têm referência −1/2.

## 2. Recorrência exata e redução de condutor

Para K≥1, seja r_j o inverso de 2^{j+1} módulo 3^K. O levantamento

    a=(3b+1)r_j mod 3^K

dá exatamente

    P̂^K_{ℓ,k}(h)=Σ_{0≤j<c_ℓ} w_{ℓ,k}(j)
       exp(2πi h r_j/3^K)
       P̂^{K−1}_{ℓ−1,k−j}(h r_j mod 3^{K−1}).

Termos de peso zero são omitidos. Na forma não normalizada a mesma
identidade vale sem w, substituindo as probabilidades pelas somas H.
Em K=0, H^0_{ℓ,k}=q_ℓ(k); P̂^0=1 nos estados de massa positiva.

Se h é unidade módulo 3^K, o caráter primitivo de condutor 3^K passa a
um de condutor 3^{K−1}; em K=1 passa à constante. Mais geralmente,
um caráter de condutor 3^r, r≥1, passa a condutor 3^{r−1}. Multiplicar
por r_j não muda a valoração 3-ádica do índice. Os caracteres de condutor
menor podem ser representados diretamente no módulo menor.

A recorrência fecha no conjunto (profundidade, custo, frequência, resolução).
Uma única média residual não fecha: aparecem custos k−j e frequências
multiplicadas por r_j, além das fases do termo constante.

## 3. Por que a identidade não é ainda uma contração

A desigualdade triangular dá apenas |P̂|≤Σ_j w_j=1. Para reduzir essa
cota é necessário controlar as fases junto com os estados condicionados
k−j. Não se podem substituir esses estados por cópias independentes nem
pelos pesos 3/4 e 1/4 do operador de profundidade total.

Há um contraexemplo ao uso de uma contração estrita universal desta
recorrência: k=0 admite uma única tupla e um único resíduo em qualquer
profundidade, portanto |P̂(h)|=1. Isso não refuta um resultado na janela
central k=ℓ+O(√ℓ), mas exige declarar essa janela em qualquer estimativa.

A cota anterior de cauda de custo produz erro ≤2η em cada caráter ao
renormalizar a mistura truncada, onde η≤5(4/5)^J. É uma estimativa de um
passo, pois |f|≤1 e a distância em variação total é ≤η. Não controla os
erros já existentes nas entradas nem sua propagação entre profundidades.
Somá-la sobre 3^K frequências perde uniformidade quando K cresce.

## 4. Uma condição suficiente para a minorante por resíduo

Para ℓ≥K≥1, ponha

    D_K(ℓ,k)=Σ_{h=1}^{3^K−1}|P̂^K_{ℓ,k}(h)−û_K(h)|.

Por inversão finita (sinal negativo na inversão), para toda unidade a,

    |C_K p^K_{ℓ,k}(a)−1|≤(2/3)D_K(ℓ,k),
    C_K=2·3^{K−1}.

O termo h=0 cancela pela massa 1, e C_K/3^K=2/3. Para K=ℓ,
C_ℓ p_{ℓ,k}(a)=g_ℓ(k,a)/ḡ_ℓ(k). Assim uma cota uniforme

    D_ℓ(ℓ,k)≤d<3/2

na janela e nos quantificadores escolhidos implica a minorante positiva

    g_ℓ(k,a)/ḡ_ℓ(k)≥1−2d/3>0

para todas as unidades. É uma condição suficiente, possivelmente mais
forte que o necessário; não foi provada. Não identificar automaticamente
essa formulação uniforme em a com os quantificadores livres da fonte.

A soma pode ser organizada por condutor:

    D_K=Σ_{r=1}^K Σ_{v∈(Z/3^r)^×}
          |P̂^r_{ℓ,k}(v)−û_r(v)|.

Cada frequência de módulo 3^K tem representação única h=3^{K−r}v.
São 2·3^{r−1} termos em cada escala. A identidade deixa explícito o que
falta: controlar a soma das discrepâncias em escalas r crescentes, e não
apenas a convergência em cada módulo fixo.

Cotas por norma de Fourier são suficientes, mas podem ser folgadas porque
ignoram cancelamento na inversão. Uma abordagem alternativa pode limitar
a inversão por resíduo diretamente. Não se conclui que falhar no critério
D_ℓ<3/2 refute a minorante ou a conjectura de densidade positiva.

## 5. Verificação exata sem aproximação de fases

Nova declaração anterior: `results/collatz_caracteres_20261012/DECLARACAO.md`,
SHA-256 f05dd9b405a12c94608d2e170aebf74ef431f518dae68228193571dfebe2aec9.
Grade fixada: ℓ=1..4, k=0..2ℓ, K=1..ℓ, todos os h mod 3^K.
Não foram calculados mínimos de densidade ou tendências para escolher alvo.

As fases foram representadas em Z[ζ_{3^K}], pela redução exata

    Φ_{3^K}(x)=x^{2·3^{K−1}}+x^{3^{K−1}}+1.

O polinômio ciclotômico é mínimo, portanto igualdade dos vetores reduzidos
certifica igualdade dos caracteres. Uma construção usa a recorrência de
frequências; a referência usa a composição afim independente das tuplas
(tuple_oracle). Não há exp/sin/cos em ponto flutuante nesta conferência.

- 1.422 identidades da recorrência: passaram exatamente.
- 120 identidades de Haar nas unidades: passaram exatamente.
- 21 testes rápidos: passaram (3 novos, 18 anteriores).
- CPU 0,095 s; parede 0,096 s; pico RSS reportado 17.032 KiB.
- Teto RLIMIT_CPU=60 s; sem filhos, aleatoriedade ou dados de zeros.

Comandos:

    PYTHONPATH=. python3 results/collatz_caracteres_20261012/verificar.py
    .venv/bin/python -m pytest -q collatz/test_residue_characters.py collatz/test_cost_residues.py collatz/test_congruence_filters.py collatz/test_coarse_memory.py

Código separado: `collatz/residue_characters.py`. Os módulos anteriores
não foram alterados. A implementação com vetores ciclotômicos densos é
somente para esta grade pequena, não um algoritmo escalável para K=ℓ
em profundidade extensa. CL1 e dados reservados permanecem intocados.

## 6. Direção de pesquisa resultante

O alvo seguinte é analítico: desenvolver a discrepância por condutor na
janela central, começando pelos caracteres de condutor 3 e 9 para procurar
uma identidade ou estimativa com dependência explícita em ℓ e k. Antes
de escalar, verificar se o centro de comparação Haar é adequado nessa
janela: uma minorante positiva não exige convergência a Haar.

Só depois escolher entre controlar D_ℓ, uma referência não uniforme ou
a inversão direta por resíduo. A mera recorrência não estabelece que uma
dessas abordagens seja viável. Nenhuma ligação com zeros de ζ foi obtida.

## Atualização posterior — limite central

A nota `COLLATZ_LIMITE_CENTRAL_20261012.md` deriva que Haar não é o limite em módulo fixo na janela central. O critério de discrepância desta nota permanece uma condição suficiente, não uma conjectura de convergência a Haar. A referência candidata é agora π_K; regularidade e controle em K crescente continuam abertos.
