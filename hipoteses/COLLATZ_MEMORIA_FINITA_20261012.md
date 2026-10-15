# Collatz — memória aritmética finita na normalização de média um

Data: 12/10/2026. Continuação autorizada da [nota de fechamento](COLLATZ_FILTROS_FECHAMENTO_20261012.md). Declaração anterior à implementação: `results/collatz_memoria_20261012/DECLARACAO.md`, SHA-256 `58f14674d211cd216b3aa3876be697e2b31dda882128e080da73d52ad4adce2d`.

**Resultado:** as distribuições de contagem das raízes, projetadas módulo 3^K, evoluem num sistema finito **exato**, sem erro de fechamento. Descartar detalhes mais finos tem erro ≤3^{−αK}[f]_α nas médias de uma observável Hölder, uniforme na profundidade. O erro de densidade ponto a ponto, ou em norma de Fourier absolutamente somável, não foi fechado. A diferença entre os alvos é essencial.

Rótulos: A para derivações analíticas abaixo, sem RH nem conjectura de Collatz; B para controles pequenos em frações exatas. Antecedentes explícitos na literatura. Sem reivindicação de novidade.

## 1. Objeto normalizado e medida

T(x)=x/2 no ramo par e T(x)=(3x+1)/2 no ímpar. A contagem completa de ancestrais é H_m=L+^m1, sem poda. Da nota anterior, sua média entre classes de raízes é (4/3)^m. Fixamos

\[
A=\tfrac34\mathcal L_+,\qquad F_m=A^m1=(3/4)^mH_m.
\]

F_m tem período 3^m e, portanto, extensão localmente constante a Z3. Agora μ denota **Haar em Z3**, de massa total 1. Não é Haar em Z2, nem uma amostra de uma trajetória positiva. Definimos a probabilidade μ_m=F_m μ. Ela descreve pesos de classes das raízes na contagem de árvores inversas normalizadas.

O operador em Z3 é

\[
Af(y)=\tfrac34\big[f(2y)+\mathbf1_{y\equiv2\ (3)}f((2y-1)/3)\big].
\]

Como 2 é unidade 3-ádica, multiplicar por 2 preserva μ. A mudança y=(3x+1)/2 leva Z3 à classe y≡2 mod3 e multiplica a medida por 1/3. Assim A preserva integrais e positividade, tem norma ≤1 em L1(μ), e F_m≥0, ∫F_m dμ=1 para todo m. Não se afirma que A preserve constantes.

## 2. Dualidade exata, sem modelo de paridades

Para observáveis f,

\[
Qf(x)=\tfrac34f(x/2)+\tfrac14f((3x+1)/2).
\]

A mesma mudança de variável prova

\[
\int (Ag)f\,d\mu=\int g(Qf)\,d\mu.
\]

Logo μ_{m+1}=μ_m Q. O kernel Q é um transporte auxiliar derivado **exatamente** da média das árvores. Os pesos 3/4 e 1/4 vêm da normalização e do fator de Haar 1/3; não foram ajustados a dados e não são probabilidades assumidas para os passos de uma órbita positiva.

As duas aplicações c0(x)=x/2 e c1(x)=(3x+1)/2 estão definidas em Z3 inteiro. Suas razões métricas são 1 e 1/3, respectivamente. Isto difere dos ramos inversos em Z2, ambos contrativos por 1/2.

## 3. Fechamento exato das médias módulo 3^K

Seja E_K a média condicional nas classes módulo D=3^K. Para uma densidade g, sua probabilidade na classe a é p(a)=D^{−1}(E_Kg)(a).

Ambos os mapas c0,c1 respeitam congruências módulo D, porque 2 é invertível. Portanto induzem um kernel Q_K nos D estados:

- c0: a↦2^{-1}a mod D, peso 3/4;
- c1: a↦2^{-1}(3a+1) mod D, peso 1/4.

A projeção de qualquer medida comuta exatamente com o transporte Q. Em particular,

\[
p_{m,K}=\operatorname{proj}_K\mu_m=p_{0,K}Q_K^m,
\qquad p_{0,K}(a)=3^{-K}.
\]

Na linguagem das densidades, para K≥1 e v=E_Kg,

\[
(A_Kv)(a)=\tfrac34v(2a\bmod D)
+\tfrac14\mathbf1_{a\equiv2\ (3)}
\sum_{j=0}^2v(r+jD/3),\qquad
r=(2a-1)/3\bmod(D/3).
\]

Para K=0, A_0 é a identidade. Obtemos

\[
\boxed{E_KAg=A_KE_Kg,\qquad E_KF_m=A_K^m1.}
\]

A divisão por 3 pede mais um dígito para avaliar g ponto a ponto; a média sobre a classe integra esse dígito e produz a soma acima. Essa é a razão pela qual há fechamento das médias apesar da obstrução ao fechamento ponto a ponto.

Custo por passo: O(3^K) operações e memória O(3^K) para vetores; não é necessário guardar matriz densa nem conhecer filtros até período 3^m. Não é um quociente determinístico do mapa T: é um quociente exato do transporte Q.

## 4. Contração e medida estacionária

Para α>0, definimos [f]_α=sup_{x≠y}|f(x)−f(y)|/|x−y|_3^α. As razões dos mapas dão

\[
[Qf]_\alpha\le\rho_\alpha[f]_\alpha,
\qquad \rho_\alpha=\tfrac34+\tfrac14\,3^{-\alpha}<1.
\]

### Construção explícita da estacionária

Escolha ξ_j independentes, com Pr(ξ_j=1)=1/4. Ponha N_{j−1}=Σ_{i<j}ξ_i. A série aleatória

\[
X=\sum_{j\ge1}\xi_j\frac{3^{N_{j-1}}}{2^j}
\]

converge quase certamente em Z3: existem infinitos ξ_j=1 com probabilidade 1, e os termos não nulos tendem a zero na métrica 3-ádica. Em um corpo não arquimediano completo isso basta para a convergência. Separando o primeiro símbolo, a distribuição ν de X satisfaz νQ=ν.

Aqui a aleatoriedade representa o kernel auxiliar Q já derivado; a série não é uma hipótese sobre uma trajetória de T. O primeiro termo não nulo é uma unidade e todos os posteriores são múltiplos de 3; portanto ν é suportada nas unidades Z3^×.

Acople duas evoluções pelo mesmo conjunto de símbolos. Depois de m passos, a distância de seus estados foi multiplicada por 3^{−B_m}, onde B_m tem distribuição Binomial(m,1/4). Como o diâmetro inicial é ≤1,

\[
\left|\int f\,d\mu_m-\int f\,d\nu\right|
\le\rho_\alpha^m[f]_\alpha.
\]

O mesmo argumento vale para qualquer distribuição inicial e prova unicidade da estacionária: as integrais das observáveis localmente constantes/Hölder determinam a medida. Para α=1, ρ_1=5/6.

## 5. Cota para distribuições de resíduos, incluindo dependência de K

Se B_m≥K, os dois estados acoplados têm a mesma classe módulo 3^K. Assim, com variação total definida como metade da soma dos módulos das diferenças de massas,

\[
\boxed{\|p_{m,K}-\pi_K\|_{TV}
\le b_{m,K}:=\Pr[\mathrm{Binomial}(m,1/4)<K]
=(3/4)^m\sum_{j=0}^{\min(K-1,m)}\binom mj3^{-j}.}
\]

π_K é a projeção de ν. Para K=0 a cota é zero. Se m<K, a soma é 1: a fórmula não promete uma resolução arbitrariamente fina em pouco tempo.

Em densidades W_K=3^Kπ_K, a cota correspondente é

\[
\|E_KF_m-W_K\|_\infty\le3^K b_{m,K}.
\]

Para K fixo, isso tende a zero. Pode-se majorar binom(m,j) por m^j/j!, dando uma taxa explícita (3/4)^m vezes polinômio de grau K−1. O fator 3^K impede tratar essa estimativa como uniforme ao aumentar a resolução.

Caso K=1: π_1=(0,3/7,4/7), portanto W_1=(0,9/7,12/7). Não é uma previsão ajustada: decorre da equação estacionária de três estados.

## 6. Descartar detalhes finos: o erro fraco fecha uniformemente

Como os pontos de uma classe módulo 3^K estão a distância ≤3^{−K},

\[
\|f-E_Kf\|_\infty\le3^{-\alpha K}[f]_\alpha.
\]

Usando E_K auto-adjunto em Haar, F_m≥0 e ∫F_m=1,

\[
\boxed{\left|\int f(F_m-E_KF_m)\,d\mu\right|
\le3^{-\alpha K}[f]_\alpha\quad\text{para todo }m.}
\]

A constante é independente de m. A desigualdade vale em geral para uma densidade de probabilidade; o avanço dinâmico é combiná-la com o fechamento **exato** de E_KF_m e a cota explícita de convergência desse sistema. A parte de coarsening isolada não é descoberta.

Se ν_K^{lift} tem densidade W_K em Haar, a mesma cota se aplica ao transporte ν→ν_K^{lift}. Combinando com a evolução:

\[
\left|\int fF_m\,d\mu-\int fW_K\,d\mu\right|
\le(\rho_\alpha^m+3^{-\alpha K})[f]_\alpha.
\]

Para f indicador de um resíduo fino, sua seminorma cresce com o nível. Por isso estas cotas não são um controle uniforme sobre observáveis de regularidade arbitrária.

## 7. O alvo forte continua aberto — redução precisa

Defina

\[
\delta_K=\sup_{m\ge0}\|F_m-E_KF_m\|_\infty.
\]

Nesta entrega não foi demonstrado que δ_K seja finito ou tenda a zero. A versão de cauda em norma de Fourier da nota anterior é ainda mais forte que essa norma sup.

**Proposição de redução:** δ_K→0 se e somente se F_m converge uniformemente para uma função contínua W em Z3.

- Se δ_K→0, para cada K fixo temos E_KF_m→W_K uniformemente pela §5. Isso torna W_K uma sequência uniformemente de Cauchy: a diferença entre dois níveis é limitada, ao passar m→∞, por δ_K+δ_L. Seu limite W é contínuo. A desigualdade ||F_m−W||∞≤δ_K+||E_KF_m−W_K||∞+||W_K−W||∞ prova convergência uniforme de F_m. Então ν=Wμ.
- Reciprocamente, se F_m→W uniformemente com W contínua, E_K é uma contração em sup e E_KW→W uniformemente. Para as profundidades grandes, ||F_m−E_KF_m||∞≤2||F_m−W||∞+||W−E_KW||∞. As poucas profundidades restantes têm períodos finitos e ficam exatas para K suficientemente grande.

A continuidade de uma densidade estacionária, sozinha, não foi provada suficiente para a convergência uniforme de F_m. Não trocar essa condição pela conclusão mais forte sem argumento.

Isso localiza o obstáculo: aproximação fraca é controlada; aproximação forte requer regularidade e convergência da família de densidades, não apenas massas em cada resolução fixa.

## 8. Confronto com Applegate–Lagarias

Fonte já arquivada: *The Distribution of 3x+1 Trees*, Experimental Mathematics 4 (1995), 193–209; SHA-256 `cc3df1accda2bf5aa335f31c08215283f3354b4b490c1bfca19baeb98be02390`. Relidos §6, Teorema 6.1 e recorrências (6.3)–(6.7), pp. 204–206, e Teorema 6.3/Limit Function Conjecture, pp. 207–208. P. 208 também conferida renderizada. A renderização produziu avisos de bounding boxes de fontes Type 3, mas o conteúdo visual é legível.

O artigo trata de árvores **podadas**, excluindo nós múltiplos de 3. Ele já prova limites de médias em classes fixas e formula regularidade global da função limite como conjectura. Não atribuímos novidade ao surgimento de uma função 3-ádica, a médias de resíduos ou a uma cadeia auxiliar.

### Correspondência entre normalizações

Nos ramos inversos, depois de entrar em um múltiplo de 3 só se pode continuar por duplicações, permanecendo múltiplo de 3. Para uma raiz unidade, terminar numa unidade é portanto equivalente a permanecer na árvore podada. Logo sua contagem é L+^m 1_{Z3^×}.

A densidade normalizada F*_m=A^m1_{Z3^×} tem massa 2/3. A medida (3/2)F*_m μ é uma probabilidade inicial uniforme nas unidades, evoluída pelo mesmo Q. Por unicidade da estacionária, E_KF*_m→(2/3)W_K. Assim o limite de médias da árvore podada corresponde a

\[
W^{AL}[a\bmod3^K]=(2/3)W_K(a)\quad(a\not\equiv0\ (3)).
\]

Em K=1, isso recupera 6/7 e 8/7, os valores de (6.5), p. 205. Essa correspondência foi derivada usando o objeto exato; não se transportou uma conjectura sobre máximos para a árvore completa.

A redução forte da §7 exigiria regularidade compatível com temas daquela conjectura, além do controle de convergência das contagens. A fonte de 1995 não basta para afirmar que o alvo continua aberto hoje. A revisão posterior de Wirsching e citações permanece pendente.

## 9. Consequência para a ligação com funções L

A decomposição em funções L dos filtros periódicos, na nota anterior, permanece válida. Mas a estimativa fraca 3-ádica não se aplica automaticamente ao peso n^{−s} da série de Dirichlet.

Para Re s>0, não existe função contínua em Z3 cuja restrição aos positivos seja n^{−s}: os inteiros n_j=n0+3^j convergem a n0 em Z3, enquanto n_j^{−s}→0 em módulo e n0^{−s}≠0. Portanto uma passagem desse controle às séries aritméticas exige estimativas que também tratem a altura real dos inteiros.

Esse é um obstáculo demonstrado ao uso **direto** da cota fraca na ponte. Não exclui uma abordagem com truncamentos, pesos e erros adicionais. Nenhuma identidade de zeros ou continuação uniforme perto da linha crítica foi estabelecida.

## 10. Verificações e artefatos

Código novo `collatz/coarse_memory.py`; código anterior preservado e hash conferido. Nenhum import de riemann_spectra. Comandos:

```bash
.venv/bin/python -m pytest -q collatz/test_coarse_memory.py
.venv/bin/python results/collatz_memoria_20261012/verificar.py
```

- 6 testes passaram, 0,09 s de parede reportados pelo pytest.
- 280 componentes de vetores: cadeia exata versus expansão completa de filtros, K=0,…,3 e m=0,…,6.
- 4 estacionárias, incluindo massa, equação e compatibilidade entre níveis.
- 52 verificações da cota de variação total, m=0,…,12.
- 42 verificações de contração Hölder em observáveis fixadas previamente.
- Todos passaram, em aritmética racional exata. CPU 0,2968 s; parede 0,2976 s; pico do processo 18.760 KiB em Linux. RLIMIT_CPU=60 s, sem extensão. Leituras, documentação e testes pytest não entram na CPU medida do piloto.

K≤3 limita a matriz densa estacionária a 27×27. Não houve enumeração de ciclos ou transientes, dados de zeros, campanha estatística ou ampliação de grade. Os controles conhecidos foram declarados antes da implementação. Provas analíticas das cotas para todo m/K não dependem do piloto.

## 11. Estado e próximo trabalho

| Alvo | Estado |
|---|---|
| Fechamento das distribuições módulo 3^K | validado por identidade exata |
| Contração Hölder e convergência fraca | validado por derivação |
| Coarsening em médias regulares, uniforme em m | validado por derivação |
| Erro de densidade em sup, uniforme em m | inconclusivo; redução matemática estabelecida |
| Cauda uniforme em norma de Fourier | não executado nesta entrega; o controle fraco não a implica |
| Continuação/zeros de séries ligadas às árvores | não executado; incompatibilidade direta do peso com continuidade 3-ádica localizada |

Próximo trabalho indicado: conferir os resultados posteriores sobre regularidade das funções 3-ádicas de árvores podadas e localizar o enunciado mais próximo da redução forte acima. Depois escolher entre um alvo de regularidade ou uma estimativa conjunta de resíduos e altura real para as séries aritméticas. Não ampliar profundidades para substituir essa decisão analítica.
