# Collatz: regularidade da estacionária e limites pontuais — 12/10/2026

**Resultado:** a estacionária π identificada no limite central é exatamente
a lei de Syracuse de Tao. Aceitando sua Proposição 1.14, ela tem densidade
L1. Por derivação local, essa densidade é positiva quase em toda parte nas
unidades, mas não é limitada. Uma minorante uniforme continua sem decisão
neste projeto. Não houve campanha numérica nem alegação de novidade.

## 1. Correção bibliográfica e base matemática

Fonte: Tao, arXiv:1909.03562v5, pp. 9–12. Referência, cópia, hash e escopo
de leitura em `leituras/B34_TAO_SYRACUSE_ESTACIONARIA_20261012.md`.
O Lema 1.12/Remark 1.13 definem a mesma lei que a nossa, com a=j+1:

    X = Σ_{r≥0} 3^r 2^{−(A_1+...+A_{r+1})},
    Pr(A_i=a)=2^{−a}, a≥1, iid.

A expressão converge em Z3. As projeções em 3^K são π_K. O artigo já
apresenta os mesmos números em módulos 3 e 9. A identificação do objeto
e esses números devem ser registrados como reprodução/confronto de fonte
conhecida, não descoberta do projeto. A prova anterior de limite central
dos geradores permanece uma derivação própria; sua novidade não foi
estabelecida pela comparação bibliográfica desta entrega.

## 2. Densidade L1: consequência da mistura fina

Seja μ Haar de probabilidade em Z3 e

    f_n(x)=3^n π_n(x mod 3^n).

A projetividade dá E_m f_n=f_m para n≥m. Pela definição de oscilação
na Proposição 1.14, eqs. (1.23)–(1.24), exatamente

    ||f_n−f_m||_{L1(μ)} ≤ C_A m^{−A}, 1≤m≤n,

para cada A>0, com C_A independente de m,n. Aqui a norma é L1,
não supremo. Tao define dTV sem o fator 1/2 usado nos diagnósticos do
projeto; não misturar essas convenções.

Portanto (f_n) é Cauchy em L1. Sua completude dá f≥0, ∫f dμ=1,
e ||f−f_m||_1≤C_A m^{−A}. Em cada cilindro fixo, o limite preserva sua
massa π_K; logo dπ=f dμ. f é zero nos múltiplos de 3.

Em Haar normalizada nas unidades μ_u=(3/2)μ|_{Z3^×}, a densidade é
F=(2/3)f e as aproximações são F_K=C_Kπ_K, C_K=2·3^{K−1}. A identidade
L1 mantém a mesma constante após esta troca de normalização.

Classificação A, **dependente da Proposição 1.14 de Tao**, cujo enunciado
foi conferido, mas cuja prova profunda não foi refeita aqui. Não é
certificação numérica de constantes; C_A não foi avaliada.

## 3. Um obstáculo demonstrado à densidade limitada

Use O(x)=(3x+1)/2 e D(x)=x/2. A lei estacionária satisfaz

    π=(1/2)O_*π+(1/2)D_*π.

O ponto −1 é fixo de O e

    O^K(x)+1=(3/2)^K(x+1).

Assim O^K(Z3) está no cilindro B_K=−1+3^K Z3. O evento em que os
últimos K mapas são O tem probabilidade 2^{−K}, independentemente da
entrada. Pela estacionariedade,

    π(B_K)≥2^{−K},  μ(B_K)=3^{−K}.

A média da densidade f em B_K é pelo menos (3/2)^K. Logo f não admite
representante essencialmente limitado. Equivalentemente,

    C_Kπ_K(−1 mod 3^K)≥(2/3)(3/2)^K →∞.

Não há densidade contínua finita em todo o compacto Z3^×. Isso não
demonstra singularidade: a densidade L1 acima existe. Tampouco impede
uma minorante positiva, pois limita superior e inferior são problemas
independentes. −1 é um ponto do espaço 3-ádico; este argumento não afirma
nada sobre órbitas de inteiros positivos nem sobre um novo ciclo positivo.

### Limite de integrabilidade

A mesma concentração exclui f∈Lp para

    p≥p_* = log 3 / log(3/2).

Se f∈Lp, p>1, Hölder no cilindro daria

    2^{−K}≤π(B_K)≤[∫_{B_K}|f|^p dμ]^{1/p} 3^{−K(1−1/p)}.

Para p>p_* isso contradiz até uma norma Lp global finita. No ponto
p=p_*, o fator exponencial à direita é exatamente 2^{−K}, enquanto
[∫_{B_K}|f|^p]^{1/p}→0 pela continuidade absoluta da integral, pois
μ(B_K)→0. Também há contradição. Não foi demonstrada pertinência a Lp
para 1<p<p_*; este é somente um limite superior da possibilidade.
É uma derivação analítica local, não ajuste experimental de expoente.

## 4. Positividade quase em toda parte, sem minorante uniforme

A equação de densidades, válida quase em toda parte, é

    f(a)=(1/2)f(2a)+(3/2)1_{a≡2 mod3} f((2a−1)/3).

O fator 3 vem do módulo da mudança de variável do ramo O. Considere
Z={a unidade: f(a)=0}. A não negatividade implica que a∈Z força 2a∈Z,
fora de um conjunto nulo. Multiplicação por 2 preserva μ_u, portanto a
inclusão tem medidas iguais e Z é invariante quase em toda parte.

Essa multiplicação é ergódica em Z3^×: módulo 3^K ela permuta todas
as unidades em um ciclo, pois 2 gera o grupo de unidades. Se um conjunto
é invariante, suas médias condicionais em cada cilindro de unidades são
iguais; convergência dessas médias implica que seu indicador é constante
quase em toda parte. A medida de Z é 0 ou 1. O segundo caso contradiz
∫F dμ_u=1. Portanto F>0 quase em toda parte.

Isso não dá ess inf F>0 nem a cota uniforme inf_K min_a C_Kπ_K(a)>0.
Valores arbitrariamente pequenos podem existir em conjuntos de medidas
positivas decrescentes. Essa lacuna não é fechada por suporte pleno,
positividade em todos os cilindros ou pelo resultado L1 de Tao.

## 5. Limite do critério por soma de módulos de Fourier

A Proposição 1.17 de Tao fornece decaimento superpolinomial em K nos
caracteres primitivos de condutor 3^K. Há 2·3^{K−1} deles. Logo essa cota,
sozinha, não torna somável a soma de seus módulos através de todos os
condutores. Não inferir norma de Wiener finita, convergência uniforme das
densidades ou o critério D_ℓ<3/2 da nota anterior.

O obstáculo do §3 também mostra que uma estratégia que exigisse densidade
contínua limitada desta estacionária não seria adequada. Não afeta a
conjectura de continuidade do outro operador 3/4,1/4: ele é distinto.

## 6. Relação exata com o custo condicionado

Se A_1,...,A_ℓ são iid Geom(2), na ordem da raiz para a folha, defina

    E_{ℓ,k}={Σ_i A_i=ℓ+k,
             A_i≤c_{ℓ−i+1} para todo i}.

Cada tupla nesse evento tem peso 2^{−(ℓ+k)}, de modo que

    Pr(E_{ℓ,k})=2^{−(ℓ+k)}q_ℓ(k).

O resíduo do gerador é o offset de Tao com ordem reversa:

    p_{ℓ,k}=Law(F_ℓ(A_ℓ,...,A_1) mod 3^ℓ | E_{ℓ,k}).

Os limites individuais não são simétricos em i, portanto a reversão deve
ser mantida na fórmula; não permutar silenciosamente o evento.

Usando a razão de coeficientes da entrega anterior e as estimativas
elementares de Stirling para a binomial, Pr(E_{ℓ,k}) é da ordem de
ℓ^{−1/2} na janela |k−ℓ|≤C√ℓ (constantes dependem de C). Não foi
avaliada constante explícita nesta entrega.

Um pequeno coeficiente de Fourier **não condicionado** não limita o
coeficiente condicionado por E: pode haver cancelamento entre os custos
antes da condição. A mera divisão pela probabilidade de E não é um
argumento válido a partir da cota não condicionada. Seria necessário
controlar o numerador com indicador de E ou a transformada conjunta
(resíduo, custo).

A oportunidade de pesquisa deve ser formulada aqui: adaptação das
estimativas ao custo total e aos limites dos geradores, ou controle em
média suficiente para o alvo declarado. Antes de chamar isso de lacuna da
literatura, revisar trabalhos posteriores de condicionamento; a busca
identificou candidatos ainda não lidos. Nenhuma produção nova autorizada
pela existência desses candidatos.

## 7. Verificações e decisão

Declaração prévia: `results/collatz_regularidade_pi_20261012/DECLARACAO.md`,
SHA-256 a03d082e51f2b9ba0bee200978fa112cae16675d756f1ff226f2c3c8b0de2fb9.

- 39 componentes do Lema 1.12 nos módulos 3,9,27 coincidem exatamente
  com geometric_limit anterior; identidade da fonte e normalização conferidas.
- 52 identidades racionais do ramo O e suas divisibilidades: passaram.
- Cota π_K(−1)≥2^{−K} nos três módulos: passou. Não foi calculado mínimo.
- CPU 0,0047 s; parede 0,0052 s; RSS reportado 228.304 KiB. RSS é o
  campo retornado pelo sistema, não memória incremental do algoritmo.
  RLIMIT_CPU=60 s respeitado. Código do diagnóstico isolado na pasta.
- Não se testou numericamente integrabilidade, minorante ou a prova de Tao.

Comando: `PYTHONPATH=. python3 results/collatz_regularidade_pi_20261012/verificar.py`.

Direção escolhida: abandonar a exigência de regularidade contínua limitada
para este π; usar o resultado L1 conhecido e procurar controle adequado ao
custo condicionado. Minorante uniforme continua `inconclusivo` no projeto.
Sem simulações extensas, zeros, CL1, publicação ou commit.

## Atualização posterior — transferência por majorante positiva

A nota `COLLATZ_CUSTO_CONJUNTO_20261012.md` deriva uma transferência específica para caracteres condicionados, usando Tao Prop.7.3 e preservação dos pares cancelantes. Não usa divisão do coeficiente não condicionado. A mistura fina L1 integral e a minorante por resíduo continuam sem transferência demonstrada. Foram obtidas também aproximações em resoluções crescentes limitadas, sem trocar irrestritamente os limites.

## Atualização 18/10/2026 — obstrução quadrática mais forte

A nota `../teorias/SYRACUSE_COLISOES_20261018.md` deriva f∉L² pela sobreposição dos dois ramos, fortalecendo o limite anterior p≥log3/log(3/2), que permanece correto. Também deriva a recorrência finita de energia e um crescimento pelo menos linear sem constantes avaliadas. O argumento L² tem antecedente direto no texto de Valbuena, registrado em `leituras/SYRACUSE_ENERGIA_20261018.md`; não há alegação de novidade. Pertencimento para 1<p<2 e a majorante anunciada nessa fonte não foram auditados nesta entrega. Não se transfere a obstrução automaticamente à lei condicionada ao custo.

## Atualização de19/10 — energia sob condicionamento

A [nota de energia condicionada](../teorias/SYRACUSE_ENERGIA_CONDICIONADA_20261019.md) confere os trechos bibliográficos antes pendentes e deriva Energia(E)<=4/beta² para qualquer subconjunto de custo fixado. Para E_{ell,k} da§6, beta=q_ell(k)2^{-(ell+k)}; a estimativa central anterior dá O_C(ell). É uma majorante positiva de colisões, não divisão de coeficiente de Fourier: a advertência da§6 continua válida. Sem minorante por resíduo, novidade demonstrada ou conclusão de Collatz.
