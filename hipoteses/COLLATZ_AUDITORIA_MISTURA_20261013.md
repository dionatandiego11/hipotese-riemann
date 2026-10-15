# Auditoria interna da mistura condicionada — 13/10/2026

**Veredito:** não foi encontrada, nesta auditoria, uma falha estrutural nas
três passagens examinadas. Foi corrigida uma cota local para limiar real.
A derivação continua dependente da Proposição 7.3 de Tao. É auditoria
pela mesma sessão/autoria, NÃO revisão independente, prova formal ou
certificação de constantes.

Objeto auditado: `COLLATZ_MISTURA_CONDICIONADA_20261013.md`. A versão anterior
à correção foi preservada com hash na pasta própria de resultados. Scripts,
declarações e saídas anteriores não foram alterados.

## 1. Dependências e quantificadores conferidos

| Passagem | Conferência / conclusão |
|---|---|
| Lei dos geradores | J_i<c_i equivale a A_i≤c_i. Cada tupla com soma n+k tem peso 2^{−n−k}; massa global β=2^{−n−k}q_n(k). |
| Fonte profunda | PDF de Tao v5 tem o SHA-256 arquivado; Proposição 7.3 controla expectativa POSITIVA, uniforme no caráter primitivo. Sua prova não foi refeita. |
| Pares cancelantes | Todos os limites c_i≥2 admitem ambas as orientações (1,2)/(2,1). Após fixar somas dos pares e coordenadas restantes, soma total e indicadores externos não distinguem essas orientações. |
| Pares não cancelantes | A média com indicador pode perder normalização, mas seu módulo é ≤1 sob a lei original; não se renormaliza o par restrito. |
| Projeção do sufixo | O caráter de condutor 3^d usa só suas primeiras d coordenadas. Fixar as demais preserva o argumento dos pares; o custo restante pode ser qualquer inteiro. |
| Corte R,t | As condições de boa concentração usadas são apenas do prefixo. O erro de descartá-las é limitado antes de dividir por β. |
| Limites do prefixo | Sua menor capacidade é c_{L+1}=2·3^L, não c_R. Para L proporcional a n, fica acima de t=O(n). |
| Convolução | Com S_R=t fixado, evento do sufixo depende apenas dele. Lei fatorada é NÃO NORMALIZADA; não pressupõe independência após o evento global sem essa separação. |
| Injetividade | Numerador ímpar recupera t por v_2. Numeradores em (0,3^n) e t fixo tornam igualdade modular uma igualdade racional. |
| Colisões | Átomos do prefixo têm massa original 2^{−t}, e não 1 sobre número de tuplas. Isso dá 3^nΣν²≤n^{D log2}. |
| Frequências excluídas | T_m mantém exatamente ξ múltiplo de 3^{n−m}. Fora desse conjunto, condutor no sufixo é d=n−R−v_3(ξ), proporcional a n se ρ>α. |
| Caso m=n | Não há frequência excluída; oscilação é zero. Argumentos de d são vacuamente válidos, não uma definição de v_3(0). |
| Constantes | H depende do expoente requerido, D depende de H; só depois se escolhe o expoente externo B. São constantes fixas quando n varia. |
| Normalização final | O único custo de normalização é β^{−1}=O_C(√n) na janela central. Não há divisão pela massa de cada sufixo. |

A validade assintótica exige n suficientemente grande, dependente das
constantes. Não se trocou essa condição por uma faixa numérica testada.

## 2. Correção encontrada

A nota usava Pr(A>b)≤2^{−b} também quando b=H log n não é inteiro.
Para b≥0 real, a fórmula correta é

    Pr(A>b)=2^{−floor(b)}≤2^{1−b}.

Por exemplo, para 0<b<1 a probabilidade é 1. O fator 2 não altera a cota
polinomial obtida por união, mas a desigualdade literal precisava ser
corrigida. Aplicado somente no documento; não mudou observável, hipótese,
janela, escolha de corte, norma, resultados de scripts ou expoente final.
Também ficou explícita a convenção: log natural, exceto log_2.

## 3. Conferência exata de normalizações

Convenção: transformada de uma medida μ no grupo de N elementos é
μ̂(h)=Σ_x μ(x)exp(2πihx/N), SEM fator 1/N. Assim

    Σ_h |μ̂(h)|²=NΣ_x |μ(x)|².

Cauchy–Schwarz na norma ℓ1 e Plancherel dão

    ||(I−T_m)μ||_1²
       ≤Σ_{h∉3^{n−m}Z}|μ̂(h)|².

Esse fator é consistente mesmo quando a massa de μ não é 1. No push do
sufixo por 3^R2^{−t}, a fase torna-se uma fase módulo 3^{n−R}; não aparece
fator de massa 3^R, pois é push de medidas e não transformação de densidades.

Declaração anterior: SHA-256
0c318bcb44f13f4a3fdaa98dfb2ca967b4624455355a3373891605b91718b9cd.
Módulos 9 e 27, medidas racionais não normalizadas, todos os modos:

- 126 produtos de transformadas da convolução: passaram.
- 28 identidades de Parseval/projeção: passaram.
- 6 conservações de massa de convolução: passaram.
- 33 cotas para cauda em limiar real: passaram exatamente após cubar,
  evitando avaliar potências fracionárias em ponto flutuante.

CPU 0,924 s; parede 0,928 s; RSS informado 244.616 KiB, não medição da
memória incremental. Teto RLIMIT_CPU=60 s respeitado. Não houve execução
de oscilação dos geradores, zeros, aleatoriedade, CL1 ou campanha extensa.

Essas identidades não certificam o passo assintótico ou a estimativa externa.
Conferências finitas anteriores são compatíveis, mas também não substituem
uma auditoria independente do argumento completo.

## 4. Consequência permitida: exceções em massa, não no pior resíduo

Se p é a lei fina e q=T_m p sua média dentro dos cilindros, com
ε=||p−q||_1, para δ>0 defina

    B_δ={a:q(a)>0 e |p(a)/q(a)−1|>δ}.

Então, diretamente pela desigualdade de Markov,

    q(B_δ)≤ε/δ,
    p(B_δ)≤(1+1/δ)ε.

Onde q(a)=0, a projetividade e não negatividade implicam p(a)=0; não há
razão a calcular. As massas pequenas acima são medidas por p e q, NÃO
por Haar nem pela fração uniforme dos resíduos. Não se conclui que todas
as classes ficam próximas ou que o mínimo é positivo.

### Contraexemplo geral à inferência de minorante

Considere as unidades mod 3^n e qualquer m<n. Seja a projeção grossa
uniforme nas unidades mod 3^m. Em cada cilindro, que contém F=3^{n−m}
classes, escolha uma classe de massa zero e distribua a massa grossa
uniformemente nas F−1 restantes. A projeção permanece a mesma.

A lei q obtida por levantar uniformemente a projeção é Haar nas unidades.
Por conta direta, em cada cilindro a perda na classe zerada é sua massa
original, compensada pelas outras classes. Portanto

    ||p−q||_1=2/F=2·3^{m−n},
    min_{a unidade}p(a)=0.

Para m=ceil(ρn), ρ<1 fixo, a oscilação cai exponencialmente, satisfazendo
qualquer cota polinomial, mas o mínimo continua zero. Isso não é um
contraexemplo de Collatz nem da lei real dos geradores: mostra que uma
conclusão de minorante NÃO segue apenas do controle L1. Qualquer avanço
nesse sentido precisará usar estrutura adicional da dinâmica aritmética.

## 5. Estado e próximo alvo

- Mistura L1 em escalas finais: derivação internamente revisada, dependente
  de Tao, sem falha estrutural encontrada neste escopo.
- Revisão independente, reconstrução de Tao e constantes finitas: pendentes.
- Minorante uniforme/piores classes: `inconclusivo`, não provados pelo L1.

Próximo alvo recomendado: formular a estrutura que distingue a lei real
p_{n,k} de exemplos com buracos — por exemplo um controle de multiplicidade
ou um mecanismo de preenchimento por resíduo e custo. Primeiro comparar
esse alvo com c_n de Tao e com os requisitos de Wirsching. Não iniciar
uma enumeração extensa de mínimos para decidir uma afirmação assintótica.

Comando executado:

    PYTHONPATH=. python3 results/collatz_auditoria_mistura_20261013/verificar.py

Sem commit, publicação ou alteração das conclusões de Riemann.
