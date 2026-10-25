# Reescritas de mesmo custo e preenchimento de dígitos

19/10/2026. Derivações elementares A, conferências finitas B; hipóteses sobre presença de palavras com folga continuam D. Sem revisão independente ou alegação de novidade. T008 `em execução`.

## 1. Correção de ordem descoberta nesta etapa

As notas de energia condicionada e cobertura desta data usavam limites decrescentes na ordem cronológica de composição. Isso não coincide com a lei dos geradores do projeto. A distinção correta é:

- na ordem da raiz para a folha dos ramos inversos, os expoentes a_i satisfazem a_i<=2*3^{ell-i};
- a composição direta cronológica de Phi_b(x)=(3x+1)/2^b usa b_i=a_{ell-i+1}, portanto b_i<=2*3^{i-1}.

Na ordem inversa, d_0=0 e d_i=2^{a_i}d_{i-1}+3^{i-1}; o resíduo é d_ell/2^{sum a_i} mod3^ell. Na ordem cronológica, B_0=0 e B_i=3B_{i-1}+2^{b_1+...+b_{i-1}}. Então

    B_ell(b_1,...,b_ell)=d_ell(b_ell,...,b_1).

O denominador é o mesmo nas duas fórmulas. Não basta reverter o resíduo e manter os limites na ordem antiga.

**Testemunha:** ell=2, custo total4. A ordem cronológica correta permite (1,3),(2,2), com resíduos2,1 mod9. Limites decrescentes permitem (3,1),(2,2), com resíduos8,1. O número de palavras e o custo coincidem, mas as distribuições não. A palavra inversa (3,1) corresponde à cronológica (1,3).

A cota de energia<=4/beta² é válida para qualquer subconjunto de custo fixado, e a prova analítica permanece válida sob a correção. beta e q_ell(k) não mudam com a reversão conjunta das coordenadas/limites. Os testes de energia anteriores verificavam uma família de eventos válida, mas não identificavam por si sós sua distribuição com os geradores. Nenhum arquivo de execução anterior ou declaração foi alterado. Cópias pré-correção das duas notas e do estado estão em `results/reescritas_custo_20261019/antes/`, com hashes. Os exemplos históricos são preservados nesse arquivo; as notas de entrada receberam correção explícita.

## 2. Identidade afim de transferência

Daqui em diante b=(b_1,...,b_ell) é cronológica, com limites C_i=2*3^{i-1}. Considere o par em posições i,i+1 (índices a partir de1), com valores a,b, e q=ell-i-1 expoentes no sufixo posterior, cuja soma é t. Troque

    (a,b) -> (a+h,b-h).

O custo e o coeficiente linear do mapa não mudam. A diferença dos offsets finais é exatamente

    Delta_h=3^q * 2^{-(t+b)} * (2^h-1).                        (1)

Vale também para h negativo, com potências racionais de2; denominadores continuam unidades em3. A identidade vem do bloco

    Phi_b(Phi_a(x))=(9x+3+2^a)/2^{a+b}

seguido pelo sufixo, que multiplica diferenças por3^q*2^{-t}. É independente do prefixo e do valor de entrada.

## 3. Três versões que preenchem os três filhos

Se ambos os expoentes têm folga bilateral,

    3<=a<=C_i-2; 3<=b<=C_{i+1}-2,                             (F)

as versões h=-2,0,+2 são válidas e preservam o evento de custo e limites. Escreva r=q+1=ell-i. Então

    Delta_{+2}=3^r * 2^{-(t+b)},
    Delta_{-2}=-3^r * 2^{-(t+b+2)}.

As diferenças são zero módulo3^r, e seus quocientes por3^r são opostos e não nulos módulo3, pois4=1 mod3. Assim as três versões ocupam os três filhos da mesma classe módulo3^r.

**Exemplo:** b=(1,3,3,1), com par nas posições2,3, respeita limites2,6,18,54 e custo total8. As versões (1,1,5,1), (1,3,3,1), (1,5,1,1) têm offsets185/256,221/256,365/256. Seus resíduos módulo27 são8,17,26, todos iguais a8 módulo9. Este é um mecanismo concreto, não apenas uma condição postulada.

## 4. Da folga a uma minorante quantitativa

Fixe ell,k e i. Dentro da classe a módulo3^r, seja W_r(a) o conjunto de palavras do evento e G_r(a) o subconjunto que satisfaz (F) no par fixado. A letra G também denota sua cardinalidade no que segue.

Para um filho desejado, cada palavra de G tem exatamente uma das três versões naquele filho. Dada a imagem, a origem só pode ser uma das três transferências inversas h=-2,0,+2. Portanto a multiplicidade é no máximo3 e

    N_{r+1}(a+j3^r) >= G_r(a)/3,
    p^{r+1}(a+j3^r) >= [lambda_r(a)/3] p^r(a),                (2)
    lambda_r(a)=G_r(a)/N_r(a), quando N_r(a)>0.

Logo, se demonstrarmos por argumento adicional

    inf_{a:N_r(a)>0} lambda_r(a) >= lambda_{ell,k,r}>0,         (RF)

obtemos o critério de preenchimento (P) da [nota de cobertura](SYRACUSE_COBERTURA_CRITERIO_20261019.md), naquela resolução, com eta=lambda. A estimativa faltante para este mecanismo passou a ser uma proporção de caminhos com folga, condicionada simultaneamente ao custo e ao resíduo grosso. Não se presume independência desses eventos; uma estimativa da proporção média de palavras com folga não prova (RF).

Nesta etapa não foi demonstrada positividade uniforme dessa fração. Ela pode ser zero em classes da grade pequena. Isso limita a aplicação desta regra, sem refutar cobertura por outras regras.

## 5. O último dígito exige mais do que uma transferência adjacente

Na regra dos três filhos, o último dígito corresponde a r=ell-1, logo i=1. O primeiro limite é C_1=2, incompatível com a folga exigida. Há uma obstrução mais geral: nenhuma transferência adjacente não trivial de mesmo custo, em qualquer posição, preserva o resíduo módulo3^{ell-1}.

De fato, para h diferente de0, a validade dos expoentes em um par que começa na posição i implica

    |h|<=C_i-1=2*3^{i-1}-1.

Se h é ímpar, v_3(2^h-1)=0. Se h é par,

    v_3(2^h-1)=1+v_3(h).                                     (3)

Para h positivo par, escreva h=2*3^u*m com3 não dividindo m. A identidade4^{3^u}-1 tem valoração u+1, por indução usando X²+X+1 de valoração1 quando X=1 mod3; o fator geométrico restante tem valor m mod3. Para h negativo, dividir por uma potência de2 não muda a valoração. Isso prova (3) sem nova premissa externa.

Por (1), preservar módulo3^{ell-1} exigiria

    q+v_3(2^h-1)>=ell-1, isto é, v_3(2^h-1)>=i.

No caso par, h teria de ser múltiplo de2*3^{i-1}=C_i; no caso ímpar, a condição é impossível. Ambos contradizem o intervalo de h. Assim uma única transferência adjacente não produz um novo último dígito mantendo os anteriores.

Essa obstrução não exclui reescritas maiores, transferências coordenadas que alterem temporariamente os dígitos anteriores, nem a cobertura da distribuição completa. Também não contradiz o ganho de mistura obtido com trocas de pares, cujo alvo era cancelamento e não preenchimento ponto a ponto.

Outra limitação de uma regra local universal é um bloco de expoentes todos1: não existe outra composição positiva do mesmo comprimento e custo. Para uma janela fixa de primeiras coordenadas, palavras centrais com esse bloco podem concentrar o custo extra em uma coordenada posterior de capacidade grande. Logo uma regra de bloco fixo não pode contar com folga em toda palavra; deve trabalhar com subconjuntos adequados ou permitir empréstimo de custo fora do bloco.

## 6. O que foi executado

Declaração anterior à implementação/enumeração, posterior à derivação preliminar e à identificação da troca de ordem. SHA-256497d2f9a67b19fa587e245cf83dc58fa39398fea0748ac3878390c4d0e1928c3. Diretório `results/reescritas_custo_20261019/`.

Comando:

    .venv/bin/python results/reescritas_custo_20261019/verificar.py

Dois testes passaram em3,67s. CPU total3,996489s, parede4,194812s, teto30s. Inteiros e Fraction, sem tolerância de ponto flutuante. Escopo declarado: ell=1,...,5, s=ell,...,3ell, todos os pares adjacentes.

- 34 distribuições não vazias coincidem exatamente com `generator_counts` e `tuple_oracle`; um evento vazio foi preservado;
- 1.005 palavras/par com folga verificam identidade afim, três filhos, validade dos limites e conservação do custo;
- conferida a multiplicidade máxima3 e a desigualdade (2);
- 150 classes/par têm algum caminho com folga;676 não têm, incluindo todas as classes dos pares que começam na primeira posição.

Essas contagens são diagnósticos finitos com repetições de comprimentos/custos/resoluções; não são observações independentes, estimativas assintóticas ou critérios ajustados após resultados. A prova geral é a álgebra acima. Nenhuma enumeração extensa, órbita positiva, zero real ou reservado foi usada. Declaração, log, hashes e cópias do código preservados. As verificações anteriores não foram repetidas.

## 7. Próximo alvo delimitado

1. Para resoluções r<=ell-2, procurar um argumento sobre a massa de caminhos com folga em cada classe, como (RF), ou uma regra alternativa quando ela falha. A cota agregada de energia não implica essa condição.
2. Para o último dígito, derivar uma família de reescritas coordenadas em blocos maiores, preservando o custo e a classe módulo3^{ell-1}. Uma única transferência adjacente está excluída.

A próxima entrega deve começar pelas identidades dessas reescritas e por seus domínios de validade, antes de novas contagens. Nenhum dos dois alvos foi demonstrado nesta etapa. Sem commit ou push.
