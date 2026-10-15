# Geradores diagonais completos e hipótese suficiente de uniformidade

13/10/2026. R3 continua em execução. A: álgebra das diagonais e transferência condicional porCauchy. D: estimativa da média completa, formulada mas não demonstrada. B: controles da implementação. Sem dados de zeros, novidade estabelecida ou prova deC7/C8.

## 1. Objeto de média, antes de diferenciar

Fixe χ primitivo de condutorq>1, janela positiva[A,T], extremos não zeros. Suponha zeros locais críticos simples e nenhuma outra singularidade numa faixa próxima; GRH e simplicidade local são suficientes. F=L(s,χ), F#(s)=conj(F(1−conj(s))), H7=1, H8=L(2s,χ²). Para deslocamentosa,b positivos,

    Qj(s;a,b)=Hj(s+a)Hj#(s−b)/[F(s+a)F#(s−b)],
    Mj(T;u,v,a,b)=∫A^T [F(s+u)/F(s+v)] Qj(s;a,b) dt,
    s=1/2+it.

u é variável complexa; v>0. Nas faixas indicadas, o integrando é holomorfo emu. Paraa=b=ε e u=v=ν,

    ∂u Mj|u=v=ν = ∫A^T Wj,ε(t) F'/F(s+ν)dt.

É a média cuja parte real recupera a contagem ponderada da nota anterior. Nenhuma derivada foi trocada por uma fórmula assintótica sem condição de erro.

O lado aritmético da receita será denotadoGj(u,v,a,b;q), de modo que

    Rj(T;u,v,a,b)=Mj−(T−A)Gj.

Rj é definição exata de resto, não uma estimativa. Não contém implicitamente uma garantia de ausência de termos duais ou bordas: todas as contribuições que a diagonal não explica ficam nele.

## 2. Ambos os geradores locais

Para p∤q, ponha

    U=p^(−1−u−b), V=p^(−1−v−b), A_p=p^(−1−a−b).

A integração formal sobre a fase do primo dá

    G7,p=1−U+V+A_p,
    G8,p=(1+V)/[(1+U)(1−A_p)].                           (1)

Primos divisores deq não contribuem, porχ(p)=0. Inicialmente basta escolher deslocamentos que garantam convergência das séries locais; as expressões se estendem à regiãoRe(u+b),Re(v+b),Re(a+b)>0.

**Derivação7:** o fator de fase é

    [(1−V_z)/(1−U_z)] (1−A_z)(1−B_z),

onde U_z=p^(−1/2−u)z, V_z=p^(−1/2−v)z,
A_z=p^(−1/2−a)z eB_z=p^(−1/2−b)/z. O coeficiente constante envolve apenas graus0 e1 da série positiva; daí(1).

**Derivação8:** L(2s,χ²)/L(s,χ) tem fator local1/(1+χ(p)p^(−s)). Assim o fator de fase vira

    [(1−V_z)/(1−U_z)]/[(1+A_z)(1+B_z)].

Se f(z)=(1−V_z)/[(1−U_z)(1+A_z)], o termo constante da multiplicação por(1+B_z)^(−1) é f(−p^(−1/2−b)), que dá(1). A fase deχ(p) cancela nessa avaliação. Não se fez hipótese de independência entreL(s) eL(2s).

## 3. Forma global do momento ponderado

SeL0=L(s,χ0), eDj são as diagonais conhecidas, o produto local se simplifica exatamente:

    G8(u,v,a,b;q)=D8(a+b;q) D7(v+b;q)/D7(u+b;q).         (2)

Isto decorre de∏p∤q(1+p^(−1−x))=D7(x) e∏p∤q(1−p^(−1−x))^(−1)=D8(x). É uma identidade de fatores aritméticos, não uma identidade entre a média deL e o produto.

Emu=v,

    G8(v,v,a,b)=D8(a+b),
    ∂u G8|u=v=ν =−D8(a+b) D7'(ν+b)/D7(ν+b).            (3)

Logo se recuperaP8=−D7'/D7, inclusive o sinal e os fatores de condutor. A dependência de altura2t foi incorporada pela identidadeLiouville, não removida.

## 4. Forma global do momento não ponderado

Para7,

    G7=Y7 A7,
    Y7=L0(1+v+b)L0(1+a+b)/L0(1+u+b),
    A7=∏p∤q [(1−V)(1−A_p)/(1−U)](1−U+V+A_p).          (4)

O fator local deA7 é1+O(p^(−2+4r0)) uniformemente quando os quatro deslocamentos estão em discos de raior0<1/4. O cancelamento de todos os termos de primeira ordem emU,V,A_p é algébrico; assim o produto de correções converge absolutamente em uma vizinhança dos deslocamentos zero. Seu domínio não significa que a média completa tenha erro uniforme lá.

Emu=v,

    A7=∏p∤q(1−A_p²)=1/L0(2+2a+2b),
    G7(v,v,a,b)=D7(a+b),
    ∂u G7|u=v=ν =D7(a+b)Σp∤q logp p^(−1−ν−b)
                                      /(1+p^(−1−a−b)). (5)

Em a=b=ε, isto éD7(2ε)P7(ν,ε). A7 não pode ser descartado antes de diferenciar: ele participa dos coeficientes constantes já calculados.

## 5. Hipótese de erro no gerador: o que seria suficiente

Escolhaη∈(0,1), ε0 pequeno e A fixo. Para cada ε∈(0,ε0], ν∈(0,ε/2), considere o círculo complexo

    |u−ν|=ηε, v=ν, a=b=ε.

A região inteira desse disco satisfazRe(u+b)≥ν+(1−η)ε>0, portantoGj é holomorfo ali. Mj também é holomorfo emu sob as hipóteses locais. A diferenciação é justificada para funções analíticas exatas, não por uma estimativa pontual de razões.

**HipóteseUj(M), não demonstrada:** paraT suficientemente grande, com constante independente deν,ε e da posição no círculo,

    ε sup_|u−ν|=ηε |Rj(T;u,ν,ε,ε)| ≤ M(T).             (6)

M(T) ainda não foi estimada. Não presumimosO(√T), potência deT ou ausência deT/logT. (6) é uma condição suficiente, não necessária, nem um teorema citado da conjectura de razões.

Pela fórmula deCauchy,

    ε² |∂u Rj(T;u,ν,ε,ε)|u=ν ≤ M(T)/η.                 (7)

A identidade de contagem ponderada, o limiteν↓0 seguido deε↓0, e o polo da derivada deGj dão, condicionalmente a(6),

    |Sj(A,T)−κj(T−A)/(2π)| ≤ M(T)/(πη).                 (8)

O termo funcional∫ℓχWε, multiplicado porε², tende a zero em cada janela fixa. O resíduo aritmético éκj/2 e a correção de contagem tem fator1/π. Não precisamos substituir esse termo funcional por uma diagonal para obter(8).

Assim, M(T)=o(T) seria suficiente para a assíntota principal em condutor fixo; M(T) explícita daria uma cota de erro. AssumirM(T)=O(T^θ), θ<1, seria uma hipótese MAIS FORTE que excluiria desvios de escalaT/logT. Não foi adotada como premissa do projeto. Para inferiores, precisamos calcular a contribuição do resto, não só majorá-la.

A condição é sobre uma família de médias deslocadas, e não apenas sobre a soma desconhecida rebatizada como erro. Ainda assim, ela contém informação forte suficiente para as conjecturas: não foi apresentada como evidência independente de que elas sejam verdadeiras. Sua eventual validação matemática é o problema aberto nesta rota.

## 6. Por que a justificativa da fonte ainda não fecha(6)

No círculo usado paraCauchy, u e v não coincidem. Quandoν→0 comε fixo, o numerador na borda difere do denominador pareado porηε. A ressalva deConrey–Snaith para pares de deslocamentos que vão juntos a zero não fornece automaticamente essa uniformidade fora do ponto pareado.

Uma cotaO(T^θ) somente no ponto u=v não pode ser diferenciada. Uma cota numa faixa comε≥c/logT também não permite o limiteε↓0 paraT fixo. O controleCUE da nota anterior mostra que manter apenas deslocamentos da ordem1/N pode conservar um viés principal na razão discreta.

Por isso a presente entrega NÃO conclui o controle do resto, nem elimina termos duais, nem determina inferiores. Ela especifica o domínio complexo e o pesoε do erro que precisamos investigar.

## 7. Próximo alvo e critérios

1. Investigar(6) para a média real deL, começando por7 e condutor fixo: decomposição deRj e passagemν↓0 com o cancelamento correto do numerador pareado.
2. Verificar se a família emu revela contribuições do mesmo tamanho da diagonal quandoε↓0. Se sim, incorporá-las em um termo principal ampliado, preservando a derivada do gerador.
3. Para8, a parte aritmética(2) está fechada; a estimativa da média com altura2t continua separada.
4. Antes de confrontar dados, obter uma previsão concreta para o resto ou registrar uma limitação matemática da receita. Não adotar(6) por conveniência para produzir o resultado desejado.

Nenhum parâmetro foi ajustado aos dados. R3 continua `em execução`, R4/R5 pendentes. A presente álgebra não é uma nova conjectura proposta como novidade científica.

## 8. Verificações

Declaração anterior à implementação: results/razoes_geradores_20261013/DECLARACAO.md e.sha256. ControlesB: fatores locais por quadratura independente sobre a fase do primo; identidade global8 emu=v; derivada deG8 por integral deCauchy contra o fatorP8 independente; cancelamento do fatorA7 e rejeição de entradas fora do domínio. Não foi usado nenhum valor deL em zero real nem calculada uma média sobre espectros.

Execução: **26 testes passaram** (4 novos e22 anteriores pertinentes), CPU35.637s, parede38.881s, teto60s. Nenhuma falha. Aritmética mpmath não certificada; quadraturas são controles B e não prova da hipótese(6). Sem dados reservados, publicação, comunicação externa ou commit.
