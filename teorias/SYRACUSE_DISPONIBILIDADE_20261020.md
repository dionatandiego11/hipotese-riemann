# Disponibilidade da família H: recorrência e limite concreto

20/10/2026. Derivações finitas A e conferências B; cobertura eventual e novidades não estabelecidas. Resultado negativo `validado` no alcance abaixo, sem revisão independente. T008 continua `em execução`.

Base: [família do último dígito](SYRACUSE_ULTIMO_DIGITO_20261019.md), [convenção cronológica](SYRACUSE_REESCRITAS_CUSTO_20261019.md). Sem fonte externa nova ou hipótese RH/Collatz.

## 1. O resultado principal desta etapa

A família H continua produzindo uma reescrita correta do último dígito. Entretanto sua disponibilidade em toda classe atingida não vale para todos os comprimentos em que foi definida. Há um contraexemplo no custo central:

    ell=8; S=16; k=S-ell=8.

A família tem apenas um grupo completo, no pai971 módulo2187. A classe299 módulo2187 tem oito palavras válidas e nenhum grupo de H. Logo

    Pr(H | E_{8,8}, resíduo=299 mod2187)=0.

Não se pode usar uma minorante positiva dessa família em todas as classes nesse caso. Isso não refuta cobertura da lei completa, o critério abstrato de preenchimento, outras famílias, ou uma possível minorante para comprimentos suficientemente grandes. Não foi demonstrado resultado assintótico negativo.

## 2. Recorrência exata por custo e classe

Escreva C_n=2*3^{n-1}. Para n>=4, seja Z_n(S,a) o número de grupos completos de H no custo total S e no pai a módulo3^{n-1}. Um grupo corresponde a prefixo p em{1,2}, extra d em{0,...,45} e sufixo v fixados, e contém as três palavras da nota anterior. Z conta grupos, não palavras.

Depois das primeiras quatro coordenadas, o offset da versão-base é

    (27*2^{-p}+19)/2^{11+d}.

Módulo27, o primeiro termo é zero. Portanto a semente correta é

    Z_4(S,a)=sum_{p=1,2} sum_{d=0}^{45}
       1_{S=p+11+d} 1_{a=19*2^{-(11+d)} mod27}.                (1)

Adicionar um expoente e na posição n aplica Phi_e, aumenta a precisão de n-2 para n-1 dígitos e preserva a condição de grupo. Assim

    Z_n(S,a)=sum_{e=1}^{C_n}
       Z_{n-1}(S-e,(2^e*a-1)/3 mod3^{n-2}),                  (2)

incluindo somente os termos para os quais2^e*a=1 mod3. Custos fora do suporte contribuem zero. A divisão define uma classe módulo3^{n-2}, independentemente do representante de a, sob essa condição de divisibilidade.

Equivalentemente, o avanço é um transporte positivo:

    (S-e,b) -> (S,(3b+1)*2^{-e} mod3^{n-1}).

A mesma recorrência vale para P_n(S,a), a contagem de TODAS as palavras projetada no pai, começando pela semente completa de quatro coordenadas. Z e P têm sementes diferentes e o mesmo transporte. A fórmula não pressupõe que as duas distribuições sejam próximas.

Se N_n(S,x) conta todas as palavras no resíduo fino x módulo3^n, a identidade dos três filhos dá

    N_{H,n}(S,a+j3^{n-1})=Z_n(S,a),
    N_{H,n}(S,a)=3Z_n(S,a),
    lambda_n(S,a)=3Z_n(S,a)/P_n(S,a), quando P_n(S,a)>0.        (3)

O alvo de disponibilidade dessa família é, portanto, Z_n(S,a)>0 em todo pai com P_n(S,a)>0, ou uma comparação quantitativa P_n<=D_n Z_n. Ele não foi demonstrado e falha no exemplo da§1. Não dividir uma média global por uma massa de classe para presumir tal comparação.

## 3. Contagem escalar e custo mínimo

Somando (1)–(2) em a, obtém-se a função geradora do número de palavras de H:

    sum_S N_{H,n}(S) z^S
      =3 z^{12}(1+z)(1+z+...+z^{45})
         *prod_{j=5}^{n}(z+z²+...+z^{C_j}).                   (4)

O produto vazio é1. Cada grupo tem três palavras com o mesmo custo. Como os fatores têm coeficientes positivos em intervalos inteiros, H tem alguma palavra exatamente nos custos

    n+8 <= S <= 3^n-23.                                     (5)

O limite inferior vem de p=1, d=0 e sufixo todo1. O superior é2+11+45+sum_{j=5}^n C_j=3^n-23. Não é um critério de disponibilidade por resíduo.

Em S=2n, H é vazia para4<=n<8. Em n=8, S=16, só há a escolha mínima p=1,d=0,v=(1,1,1,1), logo um único grupo. Essa conclusão é analítica e precedeu a enumeração desta entrega.

## 4. Contraexemplo por composição racional

No caso n=8,S=16, a versão-base do único grupo é

    (1,1,1,9,1,1,1,1).

Seu offset é271505/65536 e seu pai é971 mod2187. As três versões do grupo têm o mesmo pai pela identidade já demonstrada.

Considere a palavra válida

    w=(1,1,1,1,1,1,1,9).

Seu custo também é16, todos os limites individuais são respeitados e seu offset é6305/65536. Módulo2187, o denominador é-74 e sua inversa é-266; o resíduo é299, diferente de971. Portanto essa classe é atingida pelo evento completo e não recebe H. Não é preciso assumir que ela seja típica nem estimar sua frequência.

A contagem independente por `generator_counts` acrescenta o dado finito: há4.684 palavras no evento,1.250 pais atingidos e8 palavras no pai299. H tem3 palavras em um único pai; os outros1.249 pais atingidos não contêm H. Não são amostras independentes ou estimativas de uma proporção assintótica.

## 5. Verificações executadas

Declaração prévia em `results/disponibilidade_familia_20261020/DECLARACAO.md`, SHA-25690d565f5a1f99d53364af0419fc95163b04e289676d7e1a2977e9eb794b1a874. Escrita após a derivação da recorrência e do contraexemplo, antes da implementação/enumeração. Não é confirmação independente nem teste de novidade.

Grade: n=4,...,8, S=2n-2,...,2n+2;25 perfis. Conferidas também as bordas S=57,58 da semente n=4. Os casos vazios de H foram preservados. A tabela não foi ampliada para procurar sucesso.

Comando:

    .venv/bin/python results/disponibilidade_familia_20261020/verificar.py

Dois testes passaram em0,17s. CPU total0,573708s, parede0,583651s, teto30s com RLIMIT_CPU. Comparações exatas em inteiros/Fraction:

- recorrência Z versus enumeração direta das palavras de H;
- balanço exato dos grupos entre filhos;
- inclusão de H no evento completo calculado pelo método preexistente;
- pai971 do único grupo e pai299 da palavra-testemunha;
- positividade da contagem completa no pai299 e ausência de H ali.

Módulo `collatz/family_availability.py`; teste próprio; declaração, manifesto, tabela, resumo, log e cópias do código no diretório de execução. Não houve Monte Carlo, órbitas positivas, dados de zeros ou reservados, cálculo extenso, commit ou push. Os artefatos anteriores foram preservados.

## 6. Consequência para o plano

A próxima etapa não deve presumir que H aparece em toda classe nem gastar CPU tentando certificar essa presunção. Há dois caminhos matemáticos distintos:

1. **Combinar famílias complementares:** derivar sementes adicionais de grupos completos, contabilizar sobreposições e verificar se sua união tem um mecanismo de preenchimento que sobreviva ao custo. A família atual pode continuar como uma parcela válida.
2. **Provar disponibilidade eventual:** demonstrar uma comparação de transportes que use estrutura adicional e tenha um início n_0 explicitado. O contraexemplo n=8 não elimina essa possibilidade; a mistura L1 já disponível não a estabelece.

O alvo recomendado é primeiro examinar a semente completa de quatro coordenadas por custo/resíduo e identificar onde ela não pode ser decomposta em grupos equilibrados dos três filhos. Essa é uma pergunta algébrica finita, antes de novos comprimentos ou novas tabelas grandes. Se a semente não permitir uma dominação uniforme, documentar quais estados exigem empréstimo de custo ou blocos mais longos. Uma conclusão positiva teria de especificar o alcance, não apenas acrescentar famílias até melhorar uma contagem.

A cota de energia permanece válida. Cobertura global, Collatz, ligação direta com Riemann e novidade continuam abertas.
