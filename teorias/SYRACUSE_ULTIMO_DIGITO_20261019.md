# Uma reescrita de três expoentes para o último dígito

19/10/2026. Identidade e consequências finitas A; testes exatos B; disponibilidade em todas as classes ainda D. T008 `em execução`. Novidade não estabelecida; sem revisão independente. Seleção da identidade feita DEPOIS da exploração declarada, não teste confirmatório.

Base: [convenções e obstrução para pares](SYRACUSE_REESCRITAS_CUSTO_20261019.md), [critério de cobertura](SYRACUSE_COBERTURA_CRITERIO_20261019.md). Não foi usada fonte externa nova.

## 1. Identidade encontrada e domínio

Na ordem cronológica de Phi_a(x)=(3x+1)/2^a, os limites são C_i=2*3^{i-1}. Para ell>=4, fixe primeiro expoente p em{1,2}, qualquer sufixo válido v nas posições5,...,ell e um inteiro0<=d<=45. Considere as três palavras

    w_0=(p,1,1,9+d,v),
    w_1=(p,3,5,3+d,v),
    w_2=(p,2,8,1+d,v).                                        (1)

Os blocos nas posições2–4 têm limites6,18,54. Todas as palavras são válidas e têm custo total

    S=p+11+d+sum(v).

O limite45 para d vem de9+d<=54 e torna as três versões simultaneamente válidas. Não é um parâmetro ajustado aos zeros ou a uma contagem de sucesso.

**Proposição:** as palavras de(1) têm o mesmo resíduo módulo3^{ell-1} e atingem os três filhos distintos módulo3^ell.

## 2. Prova pelo numerador do bloco

Para um bloco(a,b,c),

    Phi_c(Phi_b(Phi_a(x)))=(27x+B(a,b))/2^{a+b+c},
    B(a,b)=9+3*2^a+2^{a+b}.

Os três numeradores de(1) são

    B_0=19,
    B_1=289=19+27*10,
    B_2=1045=19+27*38.

O coeficiente linear é igual nas três versões, e o denominador do bloco é2^{11+d}. Se o sufixo tem q=ell-4 ramos e custo t, suas diferenças de offset finais são

    Phi_{w_1}(0)-Phi_{w_0}(0)=3^{ell-1}*10/2^{11+d+t},
    Phi_{w_2}(0)-Phi_{w_0}(0)=3^{ell-1}*38/2^{11+d+t}.          (2)

O primeiro expoente p não aparece nas diferenças porque a entrada do bloco é comum e seu coeficiente linear também. O denominador é uma unidade em3; os coeficientes10 e38 são1 e2 módulo3. Portanto as diferenças divididas por3^{ell-1}, junto com0, percorrem todos os dígitos ternários. Isso prova a proposição para qualquer sufixo válido, não só para os casos enumerados.

**Exemplo:** p=1,d=0,sufixo vazio, ell=4. Os offsets são65/4096,605/4096 e2117/4096. Os resíduos módulo81 são56,29 e2, todos iguais a2 módulo27. A identidade muda o último dígito mantendo os anteriores e o custo total12.

## 3. Uma parcela exatamente equilibrada da distribuição

Fixe o evento de custo E_{ell,k} do projeto. Seja H o subconjunto das palavras de E que têm uma das três formas(1), com os limites indicados. Para cada p,d,v, as três versões formam um grupo. Esses grupos são disjuntos: as duas primeiras coordenadas do bloco distinguem suas versões e a terceira determina d.

Dentro de E, todas as palavras têm o mesmo peso. Cada grupo tem uma versão em cada filho e todos os seus membros pertencem a E ou nenhum pertence, pois seus custos são iguais. Assim, para qualquer classe a módulo3^{ell-1} e j em{0,1,2},

    Pr(resíduo=a+j3^{ell-1}, H | E)
       =(1/3) Pr(resíduo=a mod3^{ell-1}, H | E).               (3)

Isto é igualdade para a parcela H, não uma hipótese de independência. Como a distribuição completa inclui outras palavras,

    p^ell(a+j3^{ell-1}) >= [lambda(a)/3] p^{ell-1}(a),         (4)
    lambda(a)=Pr(H | E, resíduo=a mod3^{ell-1}),

quando p^{ell-1}(a)>0. A mesma consequência pode ser vista pela seleção de um filho: cada imagem tem exatamente3 origens dentro do grupo.

**Estimativa que continua faltando:** para o alcance declarado de ell,k, provar que toda classe atingida módulo3^{ell-1} contém algum grupo de H; para uma minorante quantitativa, provar

    inf_{a:p^{ell-1}(a)>0} lambda(a)>=lambda_{ell,k}>0.         (D)

(D) não foi demonstrada. A positividade de Pr(H|E) sem condicionar pelo resíduo, ou uma proporção positiva em média, não basta. O resultado resolve a construção de uma reescrita possível para o último dígito, não sua disponibilidade em todas as classes. Também não preenche classes que já estejam vazias na projeção grossa.

## 4. Por que três expoentes iniciais não bastam

A exploração não encontrou uma família com três filhos no bloco que começa na posição1. Há uma prova simples, que dispensa extrapolar a grade.

Para esse bloco, o primeiro expoente está em{1,2}, o segundo em{1,...,6}. Fixados o custo do bloco e o sufixo, preservar módulo3^{ell-1} equivale a manter B(a,b) módulo9. Para cada a fixado, b de1 a6 percorre as seis potências distintas de2 módulo9. A expressão9+3*2^a+2^{a+b} percorre as seis unidades módulo9 uma vez.

Logo cada classe de B mod9 recebe exatamente dois pares(a,b) antes de impor o custo e o limite do terceiro expoente, um para cada valor de a. Depois dessas restrições recebe no máximo dois blocos, portanto no máximo dois filhos. Isso exclui o preenchimento dos três filhos com esse bloco inicial e sufixo fixo, para qualquer custo. Não é impossibilidade de reescritas maiores ou de outras posições; a identidade(1) usa as posições2–4.

## 5. Exploração e verificação efetivamente executadas

Declaração em `results/blocos_tres_20261019/DECLARACAO.md`, SHA-2569aa0de14fa6d18f2eae5c63a514e1a324e700212f2236899cf605996d40a3a65, antes da implementação e enumeração. Ela informa que uma identidade poderia ser escolhida após ler os resultados, para derivação algébrica, sem chamá-la de confirmação independente.

**Exploração delimitada:** posições iniciais i=1,2,3; somas de bloco S=3,...,18; limites corretos dos três expoentes; agrupamento de B módulo3^{i+1} e de seus filhos módulo3^{i+2}. São48 perfis, com82 fibras que ocupam os três filhos. Nenhuma na posição1. Primeira na posição2: S=11, classe19 e os blocos(1,1,9),(3,5,3),(2,8,1). Na posição3 a primeira ocorre emS=15. Isso é apenas resultado da grade; não estabelece custo mínimo fora dela nem uma lei assintótica.

Comando `.venv/bin/python results/blocos_tres_20261019/explorar.py`: CPU0,013794s, parede0,013604s, teto30s. Tabela completa, todas as testemunhas e tabela do primeiro bloco foram preservadas.

**Verificação posterior à exploração:** `.venv/bin/python results/blocos_tres_20261019/verificar.py`. Dois testes passaram em0,16s; CPU total0,520697s, parede0,522836s, teto30s. Todas as82 testemunhas foram aplicadas por composição racional independente nos menores comprimentos e com mais um sufixo1:164 aplicações. Conferidos custo, coeficiente linear, igualdade grossa e três filhos distintos. A família escolhida foi também conferida contra os offsets e resíduos explícitos acima e na seleção com três origens. Tabela inicial de12 pares conferida contra composição racional.

A verificação numérica é finita e exata, em inteiros/Fraction. A extensão aos parâmetros p,d e sufixos gerais é a prova da§2, não extrapolação dos testes. Manifestos guardam hashes do código, cópias e entradas. Não foram usados dados reais/reservados, órbitas positivas, aleatoriedade ou execução longa. Nenhuma ampliação da grade. Sem commit ou push.

## 6. Próxima pergunta

O alvo local foi alcançado: existe uma reescrita válida para o último dígito. O próximo alvo é estimar a disponibilidade de H por classe, ou demonstrar que uma classe-alvo a exclui e construir uma família complementar. Antes de novas enumerações, escrever a contagem de H por custo e resíduo usando a recorrência já existente; comparar essa contagem com a mistura condicionada e seus limites. Não substituir uma estimativa por classe por sua média global.

A presença de famílias locais e a cota de energia não demonstram sozinhas cobertura, Collatz ou uma ponte direta com Riemann. As metas de pares raros e termos inferiores na frente Riemann permanecem independentes desse mecanismo.
