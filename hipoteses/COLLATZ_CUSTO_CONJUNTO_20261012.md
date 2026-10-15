# Collatz: custo conjunto, resolução crescente e transferência de cancelamento

12/10/2026. Duas derivações analíticas concluídas no escopo abaixo. A segunda
aceita a Proposição 7.3 de Tao como teorema externo. Não se assume RH ou a
conjectura de Collatz. Sem classificação de novidade: revisão independente
das derivações e comparação bibliográfica completa ainda não realizadas.

## 1. Objetos e alcance

g_ℓ(k,a), q_ℓ(k), p^K_{ℓ,k} e π_K são os das notas anteriores. Custos
j_i≥0 têm limites j_i<c_{ℓ−i+1}, c_r=2·3^{r−1}; A_i=j_i+1. Fixe C>0
na janela |k−ℓ|≤C√ℓ. TV aqui é metade da norma ℓ1 das probabilidades.

Resultados desta nota:

- Para K=o(√ℓ), p^K_{ℓ,k} e π_K aproximam-se em TV, uniformemente nessa
  janela. Obtém-se uma majorante assintótica, sem constantes numéricas.
- Para K≤(1/2−ε)log_3 ℓ, a aproximação é pequena também no nível relativo
  C_K=2·3^{K−1}. Para k=ℓ exatamente, o alcance suficiente aumenta para
  K≤(1−ε)log_3 ℓ.
- Aceitando Tao, há decaimento superpolinomial dos caracteres primitivos
  na resolução máxima K=ℓ, mesmo com custo e limites individuais fixados.
  A prova usa sua majorante positiva, não seu coeficiente oscilatório.

Isso não dá controle relativo em K=ℓ: há exponencialmente muitos caracteres
para reunir na inversão. Minorante uniforme e conclusão de Wirsching
permanecem `inconclusivo` neste projeto.

## 2. Fórmula conjunta de custo e resíduo

Com sinal positivo na transformada, defina o polinômio

    H_ℓ(z;K,h)=Σ_k Σ_a g_ℓ(k,a) exp(2πi h a/3^K) z^k.

Para K=0, H_ℓ=Q_ℓ(z). Para 1≤K≤ℓ, r_j=2^{−j−1} mod 3^K,

    H_ℓ(z;K,h)=Σ_{0≤j<c_ℓ} z^j exp(2πi h r_j/3^K)
       H_{ℓ−1}(z;K−1,h r_j mod 3^{K−1}).

Logo P̂^K_{ℓ,k}(h)=[z^k]H_ℓ(z;K,h)/q_ℓ(k). Por extração de coeficiente,
para qualquer r>0,

    [z^k]H_ℓ=(r^{−k}/2π)∫_{−π}^{π}H_ℓ(r e^{it};K,h)e^{−ikt}dt.

Na normalização r=1/2, Ψ_ℓ(t,h)=H_ℓ((1/2)e^{it};K,h)/Q_ℓ(1/2) é a
transformada conjunta do custo e resíduo sob geometrias independentemente
truncadas pelos limites. A probabilidade do custo k é

    p_cost(k)=q_ℓ(k)2^{−k}/Q_ℓ(1/2).

Portanto uma condição suficiente para |P̂|≤δ é

    (1/2π)∫|Ψ_ℓ(t,h)|dt ≤ δ·p_cost(k).

Na janela central p_cost(k) tem ordem ℓ^{−1/2}. Conhecer Ψ somente em
t=0 não basta para esta condição. A fórmula é exata, mas essa condição
integral não foi demonstrada; pode ser mais forte que o necessário.

## 3. Razão de coeficientes com erro uniforme

Ponha B_m(v)=binom(v+m−1,m−1), θ=v/(v+m−1),
A_m(z)=∏_{i=1}^m(1−z^{c_i}) e A(z)=∏_{i≥1}(1−z^{c_i}).
Para m≥2, v≥1, a inclusão-exclusão e uma desigualdade elementar dão

    |q_m(v)/B_m(v)−A_m(θ)|
       ≤ (1/(2v)) Σ_{E⊆{1,...,m}} θ^{D_E}D_E(D_E−1),
    D_E=Σ_{i∈E}c_i.

**Prova.** Para D≤v,

    B_m(v−D)/B_m(v)=θ^D∏_{i=0}^{D−1}
        [(1−i/v)/(1−i/(v+m−1))].

Os fatores normalizados estão em [0,1]. Sua perda é

    i(m−1)/(v(v+m−1−i))≤i/v.

Usar 1−∏(1−u_i)≤Σu_i produz erro ≤θ^D D(D−1)/(2v).
Para D>v o coeficiente é zero, e D(D−1)/(2v)≥1. Aplicar a desigualdade
termo a termo na inclusão-exclusão e tomar módulos prova a fórmula.

Para θ em um compacto de (0,1), as somas de θ^{D_E}D_E² são uniformemente
finitas: são momentos derivados de ∏(1+θ^{c_i}), cujas séries convergem
uniformemente em qualquer intervalo θ≤ρ<1. Além disso, a cauda de A_m é
superexponencial em m. Assim, para v,m comparáveis e ambos grandes,

    q_m(v)/B_m(v)=A(θ)+O(1/v),

uniformemente. A é positiva e sua derivada é limitada nesses compactos.
Nenhuma constante desta notação O foi numericamente certificada.

## 4. Prefixos de comprimento crescente

Se R primeiros custos somam S, sua probabilidade exata é
q_{ℓ−R}(k−S)/q_ℓ(k), sempre que os limites desses primeiros R ramos
permitem a tupla. Para R,S=o(ℓ), as aproximações do §3 e a identidade

    B_{ℓ−R}(k−S)/B_ℓ(k)
       = (ℓ−1)_R(k)_S/(k+ℓ−1)_{R+S}

dão, na janela declarada,

    |log { [q_{ℓ−R}(k−S)/q_ℓ(k)] / 2^{−R−S} }|
       ≤ C_C[(R+S)/√ℓ+(R+S)²/ℓ+1/ℓ].

Justificativa dos erros: expandir log(x)_r=r log x+O(r²/x), com r/x
pequeno; os fatores principais diferem de 2^{−R−S} por O_C((R+S)/√ℓ).
Os argumentos θ das duas funções A diferem por O((R+S)/ℓ); sua positividade
e derivada limitada controlam a razão. Os erros do §3 são O(1/ℓ).
Para k=ℓ exatamente o primeiro termo melhora para O((R+S)/ℓ).

Isso é uma afirmação uniforme para as faixas usadas abaixo, não para
custos ou prefixos arbitrariamente próximos dos extremos do suporte.

Para transformar o controle pontual em TV, tome

    M=4R+ceil(8 log ℓ),   H=R+M.

Sob R geometrias J_i com Pr(J_i=j)=2^{−j−1}, Markov com base 4/3 dá

    Pr(Σ J_i>M)≤(3/2)^R(3/4)^M
       ≤(243/512)^R ℓ^{8 log(3/4)}≤ℓ^{−2}.

Para R=o(√ℓ), eventualmente M≪ℓ; todos os primeiros R limites c_{ℓ−i+1}
são maiores que M. No conjunto S≤M, o erro relativo é limitado por e^δ−1,
δ=O_C(H/√ℓ+H²/ℓ+1/ℓ). A massa condicional fora do conjunto é no máximo
a massa geométrica fora dele mais e^δ−1, por conservação da massa total.
A definição de TV então dá

    TV(prefixo condicionado, Geom(2)−1 em R coordenadas)
       =O_C((R+logℓ)/√ℓ+(R+logℓ)²/ℓ+ℓ^{−2}) →0.

Em k=ℓ a cota melhora para O((R+logℓ)²/ℓ+ℓ^{−2}). Esta prova não estima
a cauda condicional por independência: ela usa somente a razão exata em
um conjunto de grande massa da lei de referência e a massa total 1.

## 5. Alcance relativo em módulos logarítmicos

O resíduo mod 3^K depende apenas dos primeiros K custos. Projetar não
aumenta TV. Assim a cota anterior vale para TV(p^K_{ℓ,k},π_K), K=o(√ℓ).
Para qualquer unidade a,

    |C_K p^K_{ℓ,k}(a)−C_Kπ_K(a)|≤C_K·TV(p^K_{ℓ,k},π_K).

Se 0<ε<1/2 e 1≤K≤(1/2−ε)log_3ℓ, o lado direito é

    O_{C,ε}(ℓ^{−ε}logℓ) →0.

Para k=ℓ exatamente, com 0<ε<1 e K≤(1−ε)log_3ℓ, vale

    O_ε(ℓ^{−ε}(logℓ)²) →0.

São regimes **suficientes**, não limites ótimos demonstrados. As constantes
não são explícitas para uma decisão computacional finita. Não garantem
minorante positiva se min_a C_Kπ_K(a) também diminuir com K. Não dizem
nada relativo no caso K=ℓ.

## 6. Transferência válida da majorante positiva de Tao

Fonte externa: Tao v5, §§7–7.1, pp. 33–35; em particular Lema 7.2 e
Proposição 7.3, eq. (7.10). P.35 conferida visualmente. Sua prova de
renovação não foi refeita aqui. Seja χ primitivo de condutor 3^d,
1≤d≤ℓ, e X_d=Σ_{r=0}^{d−1}3^r2^{−(A_1+...+A_{r+1})}.
Use o evento E_{ℓ,k} do custo e limites individuais da nota anterior.

### Lema de condicionamento preservando os pares

    |E[χ(X_d)1_{E_{ℓ,k}}]|≤E exp(−ε_T³ W_d),

onde ε_T é a constante pequena de Tao e W_d conta seus pontos brancos
com soma de par 3 entre as primeiras floor(d/2) coordenadas pareadas.
Não é o ε de resolução do §5.

**Prova.** Condicione as somas dos pares b_j=A_{2j−1}+A_{2j}, mais todas
as coordenadas restantes (incluindo a ímpar de fronteira). A soma total
agora é determinada, independente das orientações internas dos pares.
As orientações são independentes, uniformes em A_{2j}∈{1,...,b_j−1}.
O offset é soma de contribuições dos pares, como em Tao eq. (7.4).
Os limites individuais fatoram por pares.

Quando b_j=3, as únicas orientações são (1,2) e (2,1); ambas respeitam
qualquer limite c_i≥2. Seu fator de cancelamento é exatamente o de Tao,
limitado por exp(−ε_T³) no ponto branco. Para os demais pares, a média
com indicador do limite tem módulo ≤1, mesmo que as orientações sejam
restritas. O termo não pareado e os indicadores nas outras coordenadas
também têm módulo ≤1. Aplicar a desigualdade triangular depois de
integrar cada orientação dá a majorante indicada, e remover o indicador
de soma total só aumenta essa quantidade não negativa.

Não foi dividido um coeficiente complexo não condicionado pela massa
do evento. A divisão só ocorre após controlar o **numerador com indicador**.

### Consequência aceitando a Proposição 7.3

Para cada A>0, a majorante positiva é O_A(d^{−A}), uniforme no caráter
primitivo. Como Pr(E_{ℓ,k})=2^{−ℓ−k}q_ℓ(k) é da ordem ℓ^{−1/2} na
janela central, segue

    |P̂^d_{ℓ,k}(h)|≪_{A,C} min(1,√ℓ·d^{−A}),  3∤h.

A escrita com min significa que ambas as cotas valem, ajustando a
constante quando necessário. Particularmente em d=ℓ,

    sup_{3∤h}|P̂^ℓ_{ℓ,k}(h)|≪_{B,C}ℓ^{−B}

para todo B>0, escolhendo A>B+1/2. Mais geralmente, para δ>0 fixo e
ℓ^δ≤d≤ℓ, o sup é O_{B,C,δ}(ℓ^{−B}). Não há constantes numéricas
certificadas nesta entrega, nem alegação de reconstruir o teorema de Tao.

Essa é uma transferência analítica específica ao evento E: um indicador
arbitrário poderia destruir as orientações, e a conclusão não valeria por
essa prova. Se algum limite individual fosse 1, por exemplo, (1,2)/(2,1)
poderiam deixar de estar ambos disponíveis.

## 7. Por que ainda não há uma minorante

Há 2·3^{d−1} frequências primitivas por condutor. Decaimento em qualquer
potência de d não compensa esse número na soma absoluta da inversão.
Assim o §6 não fecha max_a|C_ℓp_{ℓ,k}(a)−1| ou a minorante por resíduo.
Controle L2/L1 com estrutura de convolução, ou cancelamento na inversão,
exigiria argumentos adicionais. O teorema de mistura fina não condicionada
de Tao também não foi transferido integralmente nesta nota.

A estrutura muda a próxima pergunta: depois de controlar caracteres
isolados sob o custo, procurar uma estimativa **agregada** que seja
suficiente para o alvo escolhido. Isso evita pedir uma propriedade de
regularidade limitada que a estacionária π não pode ter.

## 8. Revisão dirigida e prioridades

- **Tao 2020, texto do autor sobre pré-imagens:** já formula a menor massa
  c_n=min_aπ_n(a), uma desigualdade de composição e o alvo de expoente
  c_n=3^{−n+o(n)}. Esse alvo é mais fraco que inf C_n c_n>0; nem um nem
  outro foi demonstrado aqui. Não tratar nosso problema da menor massa
  como recém-identificado na literatura. Estado posterior não estabelecido
  por essa fonte de 2020. Nota B35.
- **Yuan Si, preprint em GitHub:** foi obtido em commit fixado. Trata da
  soma de geometrias sem nossos limites c_i; apresenta regimes condicionados
  e intervalos não resolvidos. Leitura dirigida, sem aceitar suas provas
  avançadas ou resultados de densidade como premissas. Nota B36.
- As derivações §§3–6 usam somente a recorrência de Wirsching, a álgebra
  exposta e a Proposição 7.3 de Tao. Não dependem do preprint de Si.

Próximo alvo recomendado: controle agregado por escala no evento E,
primeiro escolhendo entre média/L1 e minorante ponto a ponto. Uma estimativa
em média pode ser um alvo intermediário legítimo, mas não pode ser
apresentada como resolução da minorante. Não ampliar enumeração para
contar novamente exemplos de fórmulas conhecidas.

## 9. Execução e evidência

Declaração anterior de verificações finitas: de6b8e1a6e81645bdd30ca931964c4c8af7bc89d3631d7399f111bf960bb1b5e.
Adendo anterior à conferência dos pares: arquivo ADENDO_PARES.md com hash
próprio. O primeiro cálculo ocorreu antes da implementação do segundo;
registros separados, sem alteração retroativa da primeira declaração.

- 28 majorantes de coeficientes verificadas em inteiros/Fraction.
- 36 diagnósticos parciais de prefixos em ℓ=16,32,64,128 e R=1,2,3.
  A tabela soma metade de ℓ1 só numa caixa {0,1,2,3}^R: **não é TV completa**.
- 39 identidades ciclotômicas de módulo ao quadrado e 351 conferências de
  admissibilidade dos pares (1,2)/(2,1): passaram exatamente.
- CPU: 0,0445 s e 0,0066 s; parede: 0,0446 s e 0,0069 s.
  RSS reportado 228.304 KiB em cada processo, não memória incremental.
  RLIMIT_CPU=60 s em cada comando.

Comandos:

    PYTHONPATH=. python3 results/collatz_custo_conjunto_20261012/verificar.py
    PYTHONPATH=. python3 results/collatz_custo_conjunto_20261012/verificar_pares.py

Resultados em arquivos separados. Essas conferências não certificam as
constantes assintóticas nem a prova profunda externa. Derivações novas
não passaram por revisão independente. Nenhum dado de zeros, CL1,
produção longa, execução de código externo, publicação ou commit.

## 10. Alvo seguinte formulado, não demonstrado

Escolhe-se como primeiro intermediário a norma L1 de oscilação condicionada,
sem pretender concluir uma minorante ponto a ponto. Para m≤ℓ,

    O_{m,ℓ}(k)=Σ_{a mod 3^ℓ}
        |p^ℓ_{ℓ,k}(a)−3^{m−ℓ}p^m_{ℓ,k}(a mod 3^m)|.

As duas probabilidades usam o mesmo evento de custo e limites, e p^m é
a projeção da primeira; não inserir π_m ou uma distribuição de outro
experimento nessa definição. A norma é ℓ1, sem o fator 1/2 de TV.

Candidato D: para m=ceil(0,9ℓ), qualquer C,A>0 fixos, demonstrar

    sup_{|k−ℓ|≤C√ℓ} O_{m,ℓ}(k) ≤ C_{A,C} ℓ^{−A}.

É apenas uma formulação matemática de trabalho, não protocolo experimental
congelado ou consequência já obtida. O fator 0,9 é um ponto de partida
para comparar com a redução de Tao §6; não foi escolhido por uma tabela
do projeto. A prova deveria explicitar qual estrutura de convolução ou
entropia sobrevive à condição. Se a cota falhar, registrar o mecanismo e
um alcance mais fraco, em vez de substituir a norma ou seus quantificadores
silenciosamente. Mesmo demonstrada, essa afirmação L1 não resolveria a
minorante de cada resíduo. Nenhum cálculo deste alvo foi executado.

## Atualização de 13/10/2026

O alvo §10 foi derivado em `COLLATZ_MISTURA_CONDICIONADA_20261013.md`, aceitando Tao Prop.7.3, com corte e soma do prefixo fixados antes de separar os blocos. Não foi usado como premissa nem decidido por uma tabela. Constantes e revisão independente permanecem pendentes; minorante por resíduo não foi demonstrada.
