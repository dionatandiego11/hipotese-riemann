# Custo médio inverso: limites e um certificado por potencial

25/10/2026. Derivações A elementares, com hipóteses abaixo; sem nova enumeração, avaliação numérica ou novidade estabelecida. Continuação da [cobertura uniforme](SYRACUSE_COBERTURA_UNIFORME_20261025.md). T008 permanece `em execução`.

## 1. Objeto e composição de políticas

Em Z_3^×, um ramo inverso admissível é J_e(x)=(2^e x−1)/3, e>=1, exigindo J_e(x) em Z_3^×. Defina d_r(x) como o menor custo de r ramos admissíveis e mu_r=max_x d_r(x). A função d_r depende apenas de x mod3^{r+1}; mu_r é o objeto calculado anteriormente para r=1,...,4. Não há limites cronológicos C_i nesta definição auxiliar; eles são conferidos separadamente na transferência à construção de palavras.

O ramo de custo no máximo4 garante existência e mu_r<=4r. Como cada expoente de um caminho mínimo é no máximo4r, o mínimo é atingido numa família finita. Ponha mu_0=0.

**Subaditividade:** mu_{r+s}<=mu_r+mu_s. De qualquer x, aplique uma política ótima de r passos; seu ponto final é unidade, onde se pode aplicar uma política de s passos. A precisão adicional necessária é fornecida por x mod3^{r+s+1}; o argumento de levantamento da nota anterior preserva admissibilidade.

Consequentemente existe

    lambda = lim_{r→infinito} mu_r/r = inf_{r>=1} mu_r/r.

Prova sem usar um teorema externo: para r fixo, escreva n=qr+t, 0<=t<r. Então mu_n<=q mu_r+mu_t. Divida por n e tome limite superior; o termo do resto tende a0. O limite inferior é pelo menos o ínfimo das razões. Como mu_4=12 já foi certificado, lambda<=3. Uma razão finita é uma cota superior, não uma aproximação com erro conhecido ao limite.

## 2. Obstrução combinatória necessária

Uma palavra inversa fixa (e_1,...,e_r), de custo S, termina em

    (2^S x−D)/3^r,
    D_0=0, D_j=2^{e_j}D_{j−1}+3^{j−1}.

Integridade fixa uma única classe de x mod3^r, pois2^S é invertível. Ela é unidade: D não é divisível por3. Entre seus três levantamentos mod3^{r+1}, exatamente dois dão quociente final unitário. Esses dois têm todos os intermediários admissíveis: a integridade final implica a anterior; um intermediário divisível por3 impediria a divisão seguinte. Logo cada palavra cobre exatamente duas das2*3^r classes unitárias do problema de r passos.

O número de palavras positivas de comprimento r e custo no máximo m é binom(m,r), para m>=r: somar binom(S−1,r−1), S=r,...,m, conta todas as composições. Sobreposições só diminuem a união. Assim

    mu_r<=m  implica  binom(m,r)>=3^r.                      (1)

Esta é uma condição necessária, não suficiente. Não se contou apenas um conjunto escolhido de políticas: o limite usa todas as palavras desse orçamento.

Defina H(a)=a log a−(a−1)log(a−1), a>1. A estimativa log(n!)=n log n−n+O(log n), obtida comparando a soma de log j com sua integral, dá

    log binom(m,r)=r H(m/r)+O(log r)

quando m/r fica num intervalo compacto de (1,infinito). Como H é estritamente crescente, H'(a)=log(a/(a−1))>0, existe único a_* com H(a_*)=log3. Aplicando (1) e a existência de lambda,

    a_* <= lambda <= 3.                                    (2)

O caso limite lambda=1 também é excluído: binom(m,r)<=exp(m h(r/m)), com h(p)=−p log p−(1−p)log(1−p), pela expansão de (p+(1−p))^m; se m/r→1, o logaritmo dividido por r tende a0, contrariando (1).

Sem calcular uma raiz numericamente, temos 8/5<a_*<5/3. De fato H(8/5)<log3 equivale a8^8<5^5*3^8, e H(5/3)>log3 equivale a5^5>3^6*2^2. São desigualdades inteiras. Em particular a_* está estritamente abaixo de2: H(2)=log4>log3.

**Leitura:** a contagem elementar não impede uma política com custo médio menor que2. Tampouco a fornece. A distância entre (1) e cobertura é a sobreposição aritmética das palavras.

Há uma explicação exata para não termos alcançado2 nos blocos já examinados: para r=1,2,3,4, binom(2r,r) vale2,6,20,70, respectivamente, sempre abaixo de3^r=3,9,27,81. Logo mu_r>2r nesses quatro comprimentos, independentemente de qualquer algoritmo. Em r=5 a barreira de cardinalidade deixa de excluir o orçamento2r, pois binom(10,5)=252>=243; isso não afirma que haja cobertura. Não foi calculada nenhuma política de cinco passos.

Para o modelo cronológico a custo exato S, há no máximo binom(S−1,n−1) palavras antes dos limites C_i. Cobrir as2*3^{n−1} unidades exige pelo menos esse número de palavras. A mesma barreira assintótica a_* se aplica; os limites individuais podem tornar a contagem ainda menor. Nada aqui prova cobertura em2n.

## 3. Alvo alternativo: certificado de amortização

Em vez de aumentar r sucessivamente, procurar um potencial limitado V:Z_3^×→R, um teto finito E e eta>0 tais que

    para todo x existe e em{1,...,E}, J_e(x) unitário, com
    e + V(J_e(x)) − V(x) <= 2−eta.                         (3)

Escolhendo o ramo de (3) a cada passo e telescopando,

    soma e_j <= (2−eta)r + osc(V),
    osc(V)=sup V−inf V.

Para r>osc(V)/eta, isso implica mu_r<2r. Um certificado assim seria suficiente para ultrapassar o fator2 pela estratégia de blocos da nota anterior, depois de verificar bases e limites cronológicos. eta=0 daria mu_r<=2r+osc(V), mas não, por si só, algum bloco com mu_r<=2r ou cobertura cronológica em2n+O(1) por aquela indução; essa transferência precisaria de argumento adicional.

**Como torná-lo finito:** se V depende apenas de x mod3^h, a admissibilidade do ramo e o valor de V(J_e(x)) dependem de x mod3^{h+1}. Basta conferir todas as2*3^h classes unitárias desse módulo, com expoentes1,...,E. A escolha do ramo pode depender da classe mais fina; não se deve substituir essas classes apenas por x mod3^h, perdendo um dígito. Os valores de V, eta e os ramos podem formar um certificado racional, verificável exatamente.

Isto é um alvo matemático formulado, não uma função V já encontrada nem uma equivalência necessária. A escolha de h/E, qualquer busca por otimização e sua regra de parada exigem declaração antes da execução. Falhar num h/E finito não refuta (3) em geral, muito menos a cobertura central por outros mecanismos. Nesta entrega não se executou tal busca.

## 4. Confronto dirigido com a fonte arquivada

Fonte efetivamente relida: G. J. Wirsching, *On positive predecessor density in 3n+1 dynamics*, versão preliminar arquivada em `archive/fontes_etapa11/collatz_regularidade_20261012/wirsching_positive_predecessor_prelim_bielefeld.pdf`. SHA-256 conferido contra o manifesto: c1fef3ffaa08fdea949ba927664f3b5fc2c0b146c515cceed465a395b2234bc5. Não confundir esta cópia com a versão publicada.

- Páginas impressas4–5: Elka e_ell(k,a), equações(1.2)–(1.4), média binomial e periodicidade mod3^ell. São precedentes claros para contagens por custo e classe, não resultados novos do projeto.
- Página5, Teorema1 e condição (?1): uma minorante uniforme positiva da razão e_ell(k_ell,a)/média, na faixa |ell−k_ell|<=delta sqrt(ell), implica a conclusão de densidade de predecessores, sob as hipóteses do enunciado. É um critério suficiente, não uma equivalência nem um teorema de Collatz.
- Nossa convenção acelerada usa S=n+k e limites cronológicos; a igualdade entre cada contagem particular e a Elka não é assumida nesta nota. Exige a tradução precisa dos percursos T_0/T_1, com eventuais passos iniciais/finais. A média binomial de Elka não pode ser transplantada silenciosamente para o modelo limitado.

Mesmo após essa tradução, positividade de uma contagem inteira não fornece uma fração uniforme de sua média, que pode crescer exponencialmente. O resultado anterior em S da ordem de3n está fora da faixa S da ordem de2n correspondente ao custo central. Portanto há duas dificuldades distintas: alcançar todas as classes na faixa relevante e controlar quantitativamente sua menor multiplicidade. O potencial(3) trata a primeira pelo método de políticas; sozinho não fecha a segunda nem a condição de Wirsching.

Uma tentativa de busca externa nesta sessão devolveu erro sem conteúdo. Não houve revisão bibliográfica abrangente nem inferência de ausência de antecedente. A prioridade das derivações continua por conferir, particularmente na literatura de árvores inversas e controle de custo.

## 5. Direção de trabalho e limites desta entrega

1. Preservar a prova de cobertura3n+O(1) e seu certificado; não a promover a minorante central.
2. Antes de nova enumeração, examinar (3): procurar construção analítica ou obstrução para potenciais simples e conferir a tradução Elka/custo limitado. São tarefas separadas.
3. Se uma busca finita for justificada, declarar h, E, objetivo, teto e leitura de resultado negativo; verificar o eventual certificado com aritmética racional independente da otimização.
4. Só depois investigar multiplicidades/razão com a média, indispensáveis para o alvo de densidade.

Não houve novo cálculo científico, testes de código, ampliação dos blocos, dados de zeros ou trajetórias positivas. Foram lidos documentos, conferido o hash da fonte e escritas derivações. RH e convergência de Collatz não são hipóteses dessas derivações. A frente Riemann e suas estimativas de erros de médias de funções L permanecem como estavam.
