# Complementaridade: três parcelas, período aritmético e preenchimento de custos

20/10/2026. Derivações A e verificações finitas B. Estimativa uniforme de cobertura ainda D, sem novidade estabelecida ou revisão independente. T008 `em execução`.

Base: [semente completa e recorrência dos filhos](SYRACUSE_SEMENTE_COMPLETA_20261020.md). Não se usa RH, conjectura de Collatz ou fonte externa nova. N_n(S,x) conta palavras cronológicas de n expoentes positivos, custo total S, limites C_i=2*3^{i-1}, resíduo fino x mod3^n.

## 1. Regra exata de preenchimento e tamanho das testemunhas

Para pai canônico a módulo3^{n-1}, o vetor dos filhos é

    V_n(S,a)_j=N_n(S,a+j3^{n-1}), j=0,1,2.

Cada expoente final e admissível fornece uma parcela não negativa, com custo predecessor S-e. A soma das parcelas é V. Logo o conjunto de filhos ausentes é a interseção dos conjuntos ausentes de todas as parcelas.

Se os três filhos estão presentes, sempre é possível escolher no máximo três parcelas que os cubram: para cada filho, escolha uma parcela em que ele apareça; as escolhas podem coincidir. Isso é um limite para a cardinalidade de uma testemunha, NÃO para o tamanho dos expoentes escolhidos, a complexidade de encontrá-los ou o número de estados predecessores.

Uma parcela pode bastar; duas podem se completar; três também podem ser necessárias. A hipótese informal de que duas bastariam universalmente é excluída pelos exemplos finitos abaixo. Não foi usada como hipótese de teste ou de prova.

## 2. Resultado no alcance já declarado

Mesma grade das entregas anteriores: n=4,...,8, S=2n-2,...,2n+2. Examinados8.598 pais atingidos em25 perfis, com custos e resoluções repetidos; não são observações independentes.

No caso central n=8,S=16:

| Tipo de preenchimento | Pais |
|---|---:|
| Uma parcela suficiente | 457 |
| Duas parcelas necessárias e suficientes | 102 |
| Três parcelas necessárias | 1 |
| Algum filho ausente mesmo somando tudo | 690 |
| Total de pais atingidos | 1.250 |

Os560 pais completos coincidem com a contagem anterior. A classificação não altera a cobertura; descreve como as parcelas existentes a produzem.

A primeira testemunha de necessidade de três na ordem da grade é n=8,S=15,a=1196 mod2187:

    e=1: vetor(0,1,0), custo predecessor14, pai68 mod729;
    e=3: vetor(0,0,0), custo predecessor12, pai273 mod729;
    e=5: vetor(1,0,0), custo predecessor10, pai364 mod729;
    e=7: vetor(0,0,1), custo predecessor8, pai728 mod729.

A soma é(1,1,1), mas qualquer par de parcelas deixa um filho ausente. A escolha e=1,5,7 é dessa testemunha; não foi promovida a regra universal de seleção.

O exemplo n=5,S=9,pai47, já analisado, precisa de apenas duas: e=1 dá(0,1,0), e=3 dá(1,0,1). Esses dois tipos demonstram por que é preciso conservar as três componentes e os estados de custo durante o argumento.

## 3. Dinâmica aritmética dos expoentes finais

Fixe n>=2 e um pai a. Os expoentes admissíveis têm uma paridade: e=e_0+2t, com e_0 em{1,2} escolhido por2^{e_0}a=1 mod3. Antes de reduzir os estados, escreva

    c_e=(2^e a-1)/3,
    R=3^{n-2},
    b_e=c_e modR,
    k_e=floor(c_e/R) mod3.

Então

    c_{e+2}=4c_e+1,
    b_{e+2}=4b_e+1 modR,
    k_{e+2}=4k_e+floor((4b_e+1)/R) mod3,                      (1)

e o custo predecessor muda de S-e para S-e-2. A fórmula de permutação dos filhos conserva também esse deslocamento k_e; o pai b_e sozinho não determina a parcela.

A aplicação F(b)=4b+1 é um ciclo único em Z/(3^m), para todo m>=0. Com efeito,

    F^t(b)-b=((4^t-1)/3)*(3b+1).

Como3b+1 é unidade e v_3(4^t-1)=1+v_3(t), o menor t>0 que dá igualdade módulo3^m é3^m. A identidade de valoração segue por indução na potência de3 e pela soma geométrica para o fator coprimo a3, como na prova de valoração da nota de reescritas. Isso é uma prova do período, não extrapolação de uma tabela.

Assim o pai predecessor b volta após R passos de t, ou após aumento2R em e. O estado fino c mod3R só volta após3R passos de t. Mais precisamente,

    b_{e+2R}=b_e,
    k_{e+2R}=k_e+1 mod3.                                     (2)

De fato,

    (c_{e+2R}-c_e)/R
      =2^e a * (4^R-1)/(3R)=1 mod3,

pois2^e a=1 mod3 e (4^{3^m}-1)/3^{m+1}=1 mod3. A última congruência segue da expansão do cubo e indução a partir de4-1=3.

## 4. Por que a periodicidade não fornece a cobertura central

Os três expoentes e,e+2R,e+4R repetem o pai predecessor e fazem rodar o índice dos filhos, mas usam TRÊS custos predecessores diferentes. Portanto mesmo que caibam nos limites dos expoentes, não se pode tratá-los como três permutações de um único vetor de contagens.

Além disso, a existência de n-1 expoentes positivos exige

    e<=S-(n-1).

Para usar o último dos três seria necessário S>=n-1+e+4R. Na faixa S=2n+O(sqrt(n)), isso falha para n suficientemente grande, já que R=3^{n-2}. A rotação completa é exponencialmente cara e não cabe no orçamento central de custo. Não é custo de CPU: é o custo aritmético da palavra.

Na grade finita desta entrega, os pais b_e de todos os expoentes permitidos são distintos; isso foi conferido exatamente. Em geral, a ausência de repetição em segmentos com menos de R passos decorre diretamente do período. A periodicidade sozinha não remove a correlação entre custo e resíduo.

Esta obstrução exclui a estratégia de preencher os filhos por voltar ao MESMO pai através do período inteiro no custo central. Não exclui complementaridade entre pais diferentes, como nos exemplos da§2.

## 5. Uma redução útil: aumentar custo por preenchimento do último expoente

Há uma simplificação independente da estimativa de mistura. Fixe n e delta>=0, com

    n<=S<=S+delta<=C_n+n-1.                                  (3)

Para toda palavra de custo S, aumente apenas o último expoente em delta. Esse expoente original é no máximo S-(n-1), portanto o novo é no máximo C_n por(3). Os outros limites não mudam. A aplicação é injetiva nas palavras.

O numerador afim final não depende do último expoente: seu aumento só multiplica o offset por2^{-delta}. Logo

    N_n(S+delta,2^{-delta}x mod3^n)>=N_n(S,x).                 (4)

A multiplicação por2^{-delta} é uma permutação das unidades. Consequências:

- o número de resíduos finos atingidos não diminui nessa faixa;
- min_{x unidade}N_n(S+delta,x)>=min_{x unidade}N_n(S,x);
- se todos os resíduos são atingidos no custo S, continuam todos atingidos nos custos seguintes que satisfazem(3).

A afirmação é sobre CONTAGENS não normalizadas e resíduos permutados, não sobre a probabilidade de uma mesma classe fixa nem sobre monotonicidade da parcela H. Não dispensa construir um custo inicial com cobertura.

Para uma janela central S em[2n-C sqrt(n),2n+C sqrt(n)] de inteiros, basta provar cobertura no menor custo inteiro da janela, desde que toda a janela satisfaça(3). Isso ocorre para n suficientemente grande com C fixo. A redução diminui o número de custos a tratar, mas não foi obtida prova de cobertura nesse custo inicial.

A§5 é uma derivação analítica por injeção; não houve nova enumeração ou implementação de uma campanha de limiares de cobertura.

## 6. Verificação realizada

Declaração em `results/complementaridade_20261020/DECLARACAO.md`, SHA-256ff0972abc9db6e1b3aebcaa5796fdb05953d22d077b5fb1c16b1da32690c0d2c, após a derivação das identidades de período, antes de implementação e cálculo.

Dois testes passaram:

1. Soma vetorial, interseção dos conjuntos ausentes e cobertura mínima em todos os8.598 pais da grade; igualdade exata com o gerador preexistente. Parcelas nulas preservadas. A classificação permite três parcelas desde a declaração.
2. Dezesseis órbitas algébricas, n em{3,4,5,6}, a em{1,2,4,5}, durante3R passos; conferidos(1), períodos e rotação(2). Essa parte ignora a disponibilidade do custo por definição e não foi usada como acesso a caminhos no custo central.

Comando `.venv/bin/python results/complementaridade_20261020/verificar.py`. Testes em0,61s, CPU total1,543455s, parede1,553696s, teto30s com RLIMIT_CPU. Inteiros exatos, sem rede, aleatoriedade, órbitas positivas, zeros reais/reservados ou nova faixa de comprimentos. Tabelas completas de pais/perfis, testemunhas, manifesto, hashes e cópias guardados. Sem commit ou push.

As tabelas validam implementação e exemplos finitos; as fórmulas gerais são as provas das§§3–5. Não foi demonstrada uniformidade assintótica ou novidade bibliográfica.

## 7. Alvo matemático após esta redução

Para um filho final fixado, seus estados predecessores percorrem F(y)=4y+1 mod3^{n-1} enquanto o custo restante cai em2 por passo. O filho estará ausente precisamente se todos os estados desse segmento aritmético, nos respectivos custos, estiverem fora dos suportes predecessores.

O próximo alvo é controlar essas sequências de ausências ao longo do par (custo,resíduo), ou encontrar uma regra aritmética que selecione até três parcelas produtivas com união dos suportes igual aos três filhos. Um limite para o número de parcelas não é, sozinho, uma regra de seleção e não fecha os estados.

Antes de mais CPU, deve-se verificar quais cotas disponíveis controlam essa correlação ao longo da órbita e não somente a distribuição média. A cobertura dos pais grossos também continua necessária. A redução por preenchimento de custo permite concentrar a prova num custo inicial por profundidade, sem presumir que o problema foi resolvido.
