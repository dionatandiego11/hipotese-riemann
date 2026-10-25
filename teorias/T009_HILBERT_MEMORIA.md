# T009 — Operadores de Collatz que guardam memória

15/10/2026. Direção **D**; primeiro alvo de estimativa `pendente`. As construções elementares abaixo têm derivação A no escopo declarado, sem revisão independente nem novidade estabelecida. Refinamento de T006.

## Um operador concreto

Fixamos T(n)=n/2 para n par e (3n+1)/2 para n ímpar, em N₊. Em H=ℓ²(N₊), defina

    P e_n=e_{T(n)},  A_s e_n=(1+n)^{−s}e_{T(n)}.

Cada inteiro tem no máximo duas pré-imagens. Por Cauchy–Schwarz em cada fibra, ||P||≤√2. Para Re s>1, A_s=P D_s é de classe traço, pois D_s é diagonal com Σ(1+n)^{−Re s}<∞. O peso é uma escolha explícita de amortecimento, não uma lei física deduzida e não foi ajustado à zeta.

Potências têm a forma exata

    A_s^m e_n = [∏_{j=0}^{m−1}(1+T^j(n))^{−s}] e_{T^m(n)}.

Logo tr A_s^m soma apenas pontos periódicos. O determinante de Fredholm é determinado por esses traços: perto de z=0,

    det(I−z A_s)=exp(−Σ_{m≥1} z^m tr(A_s^m)/m).

**Obstáculo específico:** se o único ciclo positivo for {1,2}, então, para Re s>1,

    det(I−z A_s)=1−z²6^{−s}.

De fato, os traços ímpares são zero e tr(A_s^{2r})=2·6^{−rs}; inserir na série dá a fórmula perto de zero, e a identidade se estende em z. A hipótese aqui é só a ausência de outros ciclos. Ela não exclui órbitas divergentes. Portanto esse determinante não distingue a conjectura completa de um cenário com divergência mas sem novos ciclos. Isso não exclui outros operadores ou regularizações.

## Onde procurar informação adicional

Para |z|·||A_s||<1, o elemento

    <e_m,(I−z A_s)^{-1}e_n>

é a soma sobre tempos de chegada T^j(n)=m, ponderada por z^j e pelos pesos ao longo da órbita. O traço retém retornos; esse elemento retém trajetórias entre estados diferentes.

**Primeiro alvo:** retirar explicitamente a contribuição do ciclo {1,2} e formular uma cota do funcional de primeira chegada, em média sobre n num intervalo declarado, que seja mais forte que a estimativa trivial pela norma. Não afirmar uma cota uniforme em n ou chegada de todos os inteiros. Antes de escolher pesos ou limite s→0, verificar quais estimativas já existem para esses operadores.

## Entrada honesta pela mecânica quântica

A regra T não é invertível: por exemplo, T(1)=T(4)=2. Ela não pode atuar como evolução unitária enviando cada |n> apenas a |T(n)>.

Há, entretanto, a isometria explícita

    V|n> = |T(n)> ⊗ |n mod 2>.

O par (T(n),paridade de n) determina n, então as imagens da base são ortonormais e V*V=I. A iteração usa registros de paridade sucessivos. Descartar esses registros perde informação; mantê-los dá uma descrição coerente com memória. Isso não constrói um Hamiltoniano de Riemann nem um algoritmo quântico mais rápido.

**Pergunta D:** a memória mínima necessária para preservar os funcionais aritméticos fornece uma medida útil da complexidade dos transientes? O primeiro passo seria comparar compressão de histórias com o erro em um funcional definido, não comparar gráficos de espectros.

**Fontes de partida:** Leventides–Poulios, arXiv:2010.12987v1, pp. 1–2; Béhani, arXiv:2303.03203v1, pp. 1–2. Leitura dirigida, não auditoria das provas completas: [registro](../hipoteses/leituras/TEORIAS_FONTES_20261015.md).
