# Cobertura uniforme por uma política finita de custo inverso

25/10/2026. Derivação A com certificado finito exato, sem revisão independente ou formalização Lean; verificações B. Novidade não estabelecida. T008 `em execução`: há cobertura num alcance uniforme, mas não no regime central que motivou a investigação.

## 1. Teorema e convenções

Mantêm-se os mapas cronológicos Phi_a(x)=(3x+1)/2^a, expoentes1<=a_i<=C_i=2*3^{i-1}, custo total S=sum a_i e contagens N_n(S,x) dos resíduos mod3^n. S é o custo total, diferente do custo extra k=S-n das notas de Wirsching.

Defina

    b(n)=4+((n-4) mod4),
    L(n)=3n+b(n),  n>=4.

**Teorema:** para todo inteiro n>=4, toda unidade x mod3^n e todo custo inteiro

    L(n)<=S<=2*3^{n-1}+n-1,                                  (1)

há uma palavra válida de comprimento n, custo S e resíduo x. Em particular, a condição mais simples

    3n+7<=S<=2*3^{n-1}+n-1                                  (2)

é suficiente. O limite dependente de n mod4 é um pouco melhor: L(4)=16,L(5)=20,L(6)=24,L(7)=28,L(8)=28, e L(n+4)=L(n)+12.

Não se afirma que L seja o primeiro custo de cobertura nem um limite ótimo. Não houve varredura de novos limiares. O teorema é sobre palavras afins e resíduos finitos. Não é um resultado de convergência de órbitas positivas do mapa de Collatz ou uma ligação com RH.

## 2. Lema de preenchimento de custo

Usa-se a [injeção já derivada](SYRACUSE_COMPLEMENTARIDADE_20261020.md): se n<=S<=S+delta<=C_n+n-1, aumentar apenas o último expoente em delta injeta palavras e dá

    N_n(S+delta,2^{-delta}x)>=N_n(S,x).                        (3)

A potência de2 é invertida módulo3^n. Logo cobertura em um custo implica cobertura nos custos seguintes dessa faixa, com uma permutação dos resíduos. Não é monotonicidade da probabilidade de uma classe fixa.

## 3. Base finita e um limite preliminar4n

### Certificado inicial

A tabela completa de quatro expoentes, consultada na retomada, já mostrava cobertura no custo16. Isso foi divulgado antes da verificação: não é dado reservado.

Gerou-se `results/politica_inversa_20261025/certificado_base.json`, com uma palavra cronológica de custo16 para cada uma das54 unidades mod81. Cada palavra respeita os limites2,6,18,54 e sua congruência é verificada por composição racional. As contagens completas coincidem com o método preexistente `generator_counts(4,12)`. Este é um certificado finito verificável; não se depende de arredondamento ou de um valor-p.

### Um ramo inverso com custo no máximo4

Para qualquer unidade x, escolha e_0 em{1,2} tal que2^{e_0}x=1 mod3. Pelo menos um dos expoentes e_0,e_0+2 dá

    y=(2^e x-1)/3

unitário. Se os dois numeradores fossem divisíveis por9, teríamos2^{e_0}x=1 e4*2^{e_0}x=1 mod9, o que exigiria4=1 mod9. Assim existe e<=4, com ramo integral e unitário.

### Indução preliminar

A base n=4 tem cobertura em16=4n. Para n>=5 e alvo x mod3^n, escolha esse ramo e<=4. O predecessor y é unidade mod3^{n-1}, e seu custo requerido é

    U=4n-e em[4(n-1),4n-1].

Por indução e(3), todos esses custos do nível anterior estão cobertos, pois

    4n-1<=C_{n-1}+n-2, n>=5.

A desigualdade equivale a3n+1<=2*3^{n-2}, válida em5 e preservada por crescimento exponencial. Construa a palavra anterior de custo U e acrescente e ao final. O custo é4n, o resíduo é x e o limite do novo expoente é respeitado. Isso prova cobertura em4n para todo n>=4 e, por(3), nos custos seguintes até C_n+n-1.

Esta etapa fornece também as bases de comprimentos4,5,6,7 para a indução melhorada.

## 4. Política de quatro ramos: custo máximo12

Considere r aplicações inversas

    x -> (2^{e_1}x-1)/3 -> ... -> y_r,

exigindo integridade e unidade em todas as etapas. Para r passos, as classes iniciais relevantes são as unidades módulo3^{r+1}. A política elementar da§3 fornece custo<=4r. Logo uma busca de mínimos que considera e<=4r não perde um minimizador: qualquer e maior já custaria mais que o limite conhecido.

Defina d_0(x)=0 para x=1,2 mod3 e

    d_r(x)=min_e {e+d_{r-1}((2^e x-1)/3 mod3^r)},            (4)

com os ramos válidos. Desempates são lexicográficos nos caminhos. A tabela finita calculada foi:

| Passos r | Classes | Maior custo mínimo mu_r | Primeira classe de pior custo |
|---|---:|---:|---:|
| 1 | 6 | 4 | 7 mod9 |
| 2 | 18 | 7 | 25 mod27 |
| 3 | 54 | 10 | 79 mod81 |
| 4 | 162 | 12 | 79 mod243 |

Por exemplo, a classe79 mod243 usa o caminho inverso(4,6,1,1), de custo12. O arquivo `politicas.json` conserva todos os240 estados e seus caminhos, não só os piores.

Uma segunda construção examinou todas as2.072 composições positivas de comprimento r e soma<=4r, para r=1,...,4, usando a congruência afim final

    (2^{sum e_i}x-D(e_1,...,e_r))/3^r,
    D_0=0, D_j=2^{e_j}D_{j-1}+3^{j-1}.

A integridade final força a das etapas anteriores porque2 é unidade em3. Exigir o quociente final unitário exclui também etapas intermediárias não unitárias que impediriam a próxima divisão. Os mínimos e desempates coincidiram exatamente com(4).

Para usar a tabela em uma classe de maior precisão, reduza x mod243. Dois representantes que diferem por3^5h, depois de j passos, diferem por2^{e_1+...+e_j}3^{5-j}h. Para j<=4 isso preserva integridade e unidade. Portanto a tabela serve para qualquer levantamento da classe, não apenas para seu representante numérico.

## 5. Prova do limiteL(n)

As bases n=b em{4,5,6,7} têm L(b)=4b, pela§3. Suponha n=m+4 com m>=4 e o teorema conhecido no nível m. A identidade b(n)=b(m) implica

    L(n)=L(m)+12.

Dado x mod3^n, a política de quatro ramos dá um predecessor unitário y mod3^m com custo t entre4 e12. O custo restante requerido é

    U=L(n)-t em[L(m),L(m)+8].

Esse intervalo está na faixa coberta pela indução: L(m)<=4m e

    L(m)+8<=4m+8<=C_m+m-1, m>=4.

A última desigualdade equivale a3m+9<=2*3^{m-1}, verdadeira em4 e daí em diante. Construa a palavra anterior com custo U. Acrescente os quatro expoentes inversos em ordem reversa, porque a palavra resultante é cronológica. Cada novo expoente é<=12 e o menor limite novo é C_{m+1}>=162, portanto os limites individuais são respeitados. Isso produz custo L(n) e resíduo x.

A injeção(3) estende de L(n) a todos os custos de(1). Como b(n)<=7, segue(2). O argumento é uma indução para todo n, não extrapolação dos casos testados.

## 6. O que isso deixa em aberto

A janela do projeto é S=2n+O(sqrt(n)), equivalente a k=n+O(sqrt(n)). O limite provado é da ordem de3n, equivalente a k da ordem de2n. Para n grande, essas faixas permanecem separadas. O teorema não certifica a minorante central, nem reclassifica a mistura e os diagnósticos anteriores.

A escolha do bloco4 ocorreu depois da comparação dos quatro blocos declarados. Ela é desenvolvimento exploratório seguido de uma prova com certificado, não validação independente de uma previsão. Nenhuma busca bibliográfica nova estabeleceu prioridade; o argumento pode ter antecedente na literatura de ramos inversos. Não anunciar novidade antes da comparação com essa literatura.

## 7. Verificações efetivamente executadas

Diretório `results/politica_inversa_20261025/`.

- Declaração original SHA-256ef921f04194d19fb603ddab1d5f924e024c6b8ce05d4fac4ea81e21c385d16a7 antes de implementar/calcular as políticas; informa que a base n4/S16 já era conhecida.
- Adendo SHA-256a9247893c83fdf6a0f8226856c5d78e54df27ef34c29cbe2d1044a9b487c4081 depois de obter mu_4=12 e antes de implementar/testar o construtor melhorado; acrescenta os custos L(n), mantendo n=4,...,8.

Comandos:

    .venv/bin/python results/politica_inversa_20261025/explorar.py
    .venv/bin/python results/politica_inversa_20261025/verificar.py

Exploração: CPU0,038849s, parede0,044588s, teto30s.

Verificação: três testes passaram em1,85s; CPU total2,218014s, parede2,323142s, teto30s. Foram conferidos:

1. Certificado de54 classes e240 políticas contra a busca afim independente de2.072 caminhos.
2. Construtores em TODAS as unidades dos comprimentos4,...,8:6.534 construções no custo4n e6.534 no custoL(n), com integridade, limites, custo e resíduo exatos.
3. A injeção de preenchimento na grade anterior de custos:13.703 desigualdades inteiras, sem mudar os comprimentos.

Os testes são em inteiros/Fraction, sem tolerância de ponto flutuante. O construtor geral e a política estão em `collatz/uniform_coverage.py` e `collatz/inverse_cost_policy.py`. Manifestos guardam declarações, hashes de entradas, versões e cópias do código. Não houve aquisição de zeros, consulta de dados reservados, Monte Carlo, enumeração de trajetórias de T, produção longa, commit ou push.

Não foram testados numericamente comprimentos maiores que8. A afirmação uniforme vem da prova e de seus certificados finitos; a revisão independente desse conjunto continua pendente.

## 8. Próximo alvo com critério matemático

A quantidade útil agora é mu_r, o pior custo mínimo de um bloco inverso que termina em unidade. Uma política finita certificada com razão mu_r/r menor que3 melhoraria o coeficiente do limite, com bases e limites individuais novamente conferidos. Isso ainda não deve ser confundido com o fator2 da janela central.

Mais precisamente, a mesma estrutura de indução mostra, se houver um bloco fixo de r passos e custo máximo mu_r, com bases suficientemente grandes, um limite de cobertura

    S >= (mu_r/r)n + O_r(1).

As bases podem ser escolhidas grandes o bastante para acomodar os expoentes do bloco e os pequenos preenchimentos de custo; para r=4 a escolha explícita está na§5. Uma política com mu_r<=2r seria suficiente para um limite2n+O_r(1). Para cobrir toda janela2n+-C sqrt(n) pelo mesmo argumento, uma desigualdade estrita mu_r<2r seria suficiente, pois a folga linear venceria a largura sublinear. São condições SUFICIENTES, não necessárias, e nenhuma foi obtida nesta etapa.

Antes de ampliar blocos, comparar esse problema de controle finito com a literatura e procurar obstruções analíticas à razão2. A falha de uma política finita ou a ausência de mu_r<2r em uma busca limitada não refutaria a cobertura central por um mecanismo mais global. A próxima execução deve ter esse alvo explícito e orçamento, em vez de repetir tabelas de cobertura sem uma previsão.
