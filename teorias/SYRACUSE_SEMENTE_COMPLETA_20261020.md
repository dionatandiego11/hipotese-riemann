# Semente completa, complementaridade de sufixos e bloco de cinco

20/10/2026. Derivações A e verificações finitas B; cobertura eventual e novidade não estabelecidas. Sem revisão independente. T008 `em execução`.

Base: [disponibilidade de H](SYRACUSE_DISPONIBILIDADE_20261020.md), [identidade em três expoentes](SYRACUSE_ULTIMO_DIGITO_20261019.md). As novas testemunhas foram selecionadas após o diagnóstico declarado; não são confirmação independente.

## 1. Resultado e alcance

Foi calculada a maior parcela equilibrada possível usando os quatro primeiros expoentes, com o custo desse prefixo e o sufixo fixos em cada grupo. Há casos em que a distribuição completa atinge os três filhos, mas essa parcela máxima é zero. Logo acrescentar outras identidades ao MESMO modelo local de prefixo4 não resolve esses casos.

A primeira classe encontrada na grade declarada é n=5,S=9,pai47 mod81. Seus filhos47,128,209 mod243 têm uma palavra cada, mas não formam um grupo com sufixo fixo e prefixo de quatro de mesmo custo. Os próprios caminhos fornecem uma identidade válida de cinco expoentes, que permite mudar o sufixo. Essa identidade é demonstrada na§5.

O resultado não exclui reescritas em outros blocos, cobertura para comprimentos maiores ou estratégias globais. O limite de maximalidade da parcela calculada é explicitamente o prefixo4 com sufixo fixo.

## 2. Parcela equilibrada máxima da semente

N_4(S,x) conta as palavras cronológicas com limites2,6,18,54, custo S e resíduo x mod81. Para pai a mod27, defina

    M_4(S,a)=min_{j=0,1,2} N_4(S,a+j27).                     (1)

Se uma subcontagem atribui o mesmo peso inteiro b a cada um dos três filhos, então b<=N_4(S,a+j27) para todo j, logo b<=M_4. O limite é atingido escolhendo M_4 palavras distintas em cada filho e agrupando-as em triplas. Portanto a massa equilibrada máxima é3M_4 naquele estado; a parte restante tem pelo menos um filho vazio.

Uma escolha lexicográfica constrói um catálogo de triplas disjuntas. A contagem de grupos não depende da escolha do emparelhamento. Não se enumeram todas as combinações possíveis de três palavras; calcula-se sua capacidade máxima e um emparelhamento que a realiza. Reutilizar uma palavra em vários grupos não acrescenta massa disponível e não resolve um filho ausente.

A semente de H satisfaz Z_{H,4}<=M_4 estado a estado, pois H já tem a mesma contagem em cada filho. Ao comparar catálogos, não somar novamente H à parcela máxima, o que duplicaria massa.

## 3. Transporte e maximalidade restrita

Seja T_n o kernel positivo de custo e resíduo da nota anterior. Defina

    A_n=T_n ... T_5 M_4.

Cada grupo inicial prolongado por um sufixo fixo continua equilibrado entre os três filhos finais. Para n>=4,

    Z_{H,n}(S,a)<=A_n(S,a)<=G_n(S,a),
    G_n(S,a)=min_j N_n(S,a+j3^{n-1}).                          (2)

A_n é a capacidade máxima para grupos em que apenas os primeiros quatro expoentes mudam, com o mesmo custo de prefixo e o mesmo sufixo. Para ver isso, particione as palavras por seu sufixo. O custo total fixa o custo do prefixo. Para cada sufixo, o mapa afim é injetivo nas classes de prefixo mod81 e leva as três classes de um pai mod27 aos três filhos finais, permutados. O limite(1) aplica-se independentemente a cada parte dessa partição e pode ser atingido em todas; somar dá o transporte exibido.

G_n pode ser estritamente maior: ao agrupar palavras com sufixos DIFERENTES, partes desequilibradas podem se completar. A desigualdade numérica subjacente é

    min_j sum_v x_{v,j} >= sum_v min_j x_{v,j}.                (3)

A desigualdade estrita não significa erro na semente: é a informação perdida ao exigir que cada parcela de sufixo já esteja equilibrada isoladamente. Ela identifica uma rota analítica diferente, controlar complementaridade entre parcelas positivas.

## 4. Diagnóstico completo executado

Declaração em `results/semente_completa_20261020/DECLARACAO.md`, SHA-256ef15068bc26e8eb0f9e8a47fcba432bc7fdcc5eb6ab914c218f07daf8090b33e, antes da implementação e enumeração, após derivação do critério(1).

Enumeradas todas as11.664 palavras de quatro expoentes e custos4..80. Comparação exata com o gerador preexistente, catálogo disjunto e tabela completa de1.386 estados custo/pai, incluindo capacidades zero:

- 2.382 grupos completos;
- 7.146 palavras na parcela equilibrada máxima;
- 4.518 palavras restantes.

O transporte usou SOMENTE a grade anterior: n=4,...,8,S=2n-2,...,2n+2,25 perfis. Na linha n=8,S=16:

| Quantidade | Valor |
|---|---:|
| Palavras totais | 4.684 |
| Pais atingidos | 1.250 |
| Pais com os três filhos atingidos | 560 |
| Pais com algum filho ausente na distribuição completa | 690 |
| Pais com grupo transportado da semente máxima de4 | 139 |
| Pais completos sem esse grupo transportado | 421 |
| Pais com a antiga família H | 1 |

Logo a melhoria de1 para139 não deve ser lida como prova ou como critério perseguido: mesmo o catálogo máximo desse escopo não explica421 pais que já são completos. No pai1 mod2187, por exemplo, as contagens dos filhos são(1,2,1), mas A_8=0. Esta é a primeira classe dessa linha pela ordem numérica; não foi escolhida por maior desvio.

A primeira diferença G>A da grade aparece em n=5,S=9,pai47, com contagens(1,1,1) e A_5=0. A escolha dessas classes após ler a tabela está declarada como exploratória. Não se extrapola a n grande ou a outras reescritas.

Comando `.venv/bin/python results/semente_completa_20261020/verificar.py`: dois testes passaram em1,85s, CPU total3,152709s, parede3,276699s, teto30s. Inteiros/Fraction; conferidos catálogo, disjunção, igualdade ao gerador, inclusão de H e as desigualdades(2). Manifesto, cópias, tabelas e catálogo completos preservados.

## 5. Identidade que atravessa a fronteira do prefixo4

A classe n=5,S=9,pai47 tem as seguintes três palavras únicas nos filhos:

    u_0=(1,1,3,1,3),
    u_1=(2,2,1,1,3),
    u_2=(1,2,3,2,1).

Os offsets são331/512,493/512,655/512. Os numeradores formam uma progressão de passo162=2*81, portanto os resíduos são209,47,128 mod243, todos47 mod81.

Os dois primeiros caminhos têm último expoente3 e custo de prefixo6; o terceiro tem último expoente1 e custo de prefixo8. O custo total9 foi preservado transferindo duas unidades entre prefixo e sufixo. Isso explica por que uma regra restrita ao prefixo4 com sufixo fixo não consegue formar esse grupo.

### Extensão analítica, sem aumentar a grade

Para0<=d<=159 e qualquer sufixo válido v nas posições6,...,n, defina

    u_0(d,v)=(1,1,3,1,3+d,v),
    u_1(d,v)=(2,2,1,1,3+d,v),
    u_2(d,v)=(1,2,3,2,1+d,v).                                 (4)

Os limites cronológicos iniciais são2,6,18,54,162. O teto159 garante3+d<=162. Os custos são iguais a9+d+sum(v). O coeficiente linear dos blocos de cinco é3^5/2^{9+d}, e seus offsets têm os mesmos numeradores331,493,655, sobre2^{9+d}.

Se v tem q=n-5 ramos e custo t, cada diferença sucessiva final é

    Delta=3^q*162/2^{9+d+t}
         =2*3^{n-1}/2^{9+d+t}.                               (5)

O quociente por3^{n-1} é uma unidade mod3. As três versões ocupam os três filhos finais, preservando os dígitos anteriores para qualquer sufixo válido. Isso prova a identidade geral. Não prova que as formas(4) ocorram em todo pai/custo. O menor custo dessa família é n+4, contra n+8 da família H; isso é alcance de uma construção, não uma afirmação de cobertura ou superioridade estatística.

### Verificação posterior à seleção da identidade

Declaração separada em `results/cinco_expoentes_20261020/DECLARACAO.md`, SHA-25668e419a415993a3d099755890b6b3fbf0c5650a708938e759786fa78c3442696. A declaração informa a seleção depois do diagnóstico da semente4 e precede a implementação dos testes.

Testados d em{0,1,159} e sufixos(),(1,),(1,1), nove aplicações exatas; conferidos limites, custo, coeficiente linear, diferenças e filhos. O caso base coincide com a contagem completa(1,1,1) e com A_5=0. Dois testes passaram em1,67s; CPU1,626740s, parede2,175537s, teto30s. A prova para todos os parâmetros é(5), não extrapolação desses testes.

Nenhuma execução usou dados de zeros ou reservados, órbitas positivas, aleatoriedade ou produção longa. Artefatos anteriores intactos. Sem commit ou push.

## 6. Uma formulação melhor do próximo alvo: interseção dos filhos ausentes

A ideia de exigir equilíbrio em cada parcela separada é mais forte que o necessário. Podemos trabalhar diretamente com o vetor de contagens dos três filhos:

    V_n(S,a)_j=N_n(S,a+j3^{n-1}), j=0,1,2.

Tomando o representante canônico0<=a<3^{n-1}, para cada expoente final e com2^e*a=1 mod3, ponha

    c_e=(2^e*a-1)/3,
    b_e=c_e mod3^{n-2},
    k_e=(c_e-b_e)/3^{n-2} mod3.

A recorrência exata do gerador se torna

    V_n(S,a)_j=sum_e V_{n-1}(S-e,b_e)_{k_e+2^e*j mod3}.       (6)

Expoentes fora dos limites, custos fora do suporte e estados predecessores impossíveis têm contribuição zero. Os índices dos filhos são permutados; os pesos são contagens não negativas. Se Z_e é o conjunto dos j cuja contribuição daquele expoente é zero, o conjunto de filhos ausentes é EXATAMENTE

    Z_n(S,a)=intersection_e Z_e.                              (7)

Nenhuma parcela precisa preencher todos os filhos. Basta que os conjuntos de ausências não tenham uma interseção comum.

### Exemplo já contido nas tabelas

Para n=5,S=9,a=47, os expoentes finais possíveis são1,3,5. As parcelas são:

- e=1: predecessor S=8,pai4 mod27, vetor bruto(1,0,0); a permutação dá(0,1,0);
- e=3: predecessor S=6,pai17 mod27, vetor bruto(0,1,1); a permutação dá(1,0,1);
- e=5: o pai predecessor é15 mod27, não unidade; a contribuição é zero.

A soma é(1,1,1). Os vetores predecessores estão na tabela completa da semente; não houve nova busca ou enumeração para este exemplo. Ele ilustra exatamente a desigualdade estrita em(3).

**Alvo D recomendado:** demonstrar, num alcance de n,k declarado, que em cada pai atingido existem parcelas admissíveis cujos conjuntos de filhos ausentes têm interseção vazia. Antes de mais CPU, estudar as permutações k_e e a compatibilidade dos estados de custo S-e. A mistura agregada não estabelece essa condição, e a recorrência(7) sozinha é uma reformulação exata, não uma prova assintótica. Cobrir os filhos de cada pai atingido ainda exige garantir a cobertura dos pais grossos, ou aplicar um critério correspondente em todas as resoluções sob o mesmo evento. Os estados de custo S-e não permanecem automaticamente na janela central; isso deve entrar no argumento, sem assumir uma indução que a janela não fecha.

Essa direção evita exigir que uma família fixa de palavras esteja em todas as classes. Também evita acrescentar catálogos até obter uma contagem desejada. Sua vantagem potencial depende de encontrar um argumento uniforme para a complementaridade, que ainda não existe no projeto. Novidade bibliográfica permanece por investigar.
