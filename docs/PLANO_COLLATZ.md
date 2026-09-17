# Plano complementar — Collatz como laboratório de dinâmica aritmética

**Adicionado:** 14/09/2026. **Estado:** pendente. Este documento é um plano de trabalho; ainda não é um protocolo experimental congelado nem um relatório de execução.

## Objetivo e escopo

Estudar o caminho regra aritmética → órbitas → estrutura espectral em sistemas cuja regra é conhecida. Usar esse laboratório para avaliar o que uma reconstrução inversa consegue identificar e o que perde. A pergunta central é: **que informação aritmética adicional distingue sistemas com a mesma dinâmica simbólica?**

A frente complementa as etapas 11–13 do [plano principal](../PLANO_IMPLEMENTACAO.md). Não condiciona a conclusão de M4/M5. Não propõe demonstrar Collatz ou Riemann, nem identifica uma dinâmica de Collatz com a dinâmica dos zeros. Nenhuma etapa requer ler ordenadas da zeta ou modificar os protocolos m3/m4.

## Convenções e referências matemáticas

Adotar o mapa com divisão por 2 também no ramo ímpar:

\[
T(x)=\begin{cases}x/2,&x\equiv0\pmod2,\\(3x+1)/2,&x\equiv1\pmod2.\end{cases}
\]

Nos inteiros positivos, o ciclo conhecido é 1 → 2 → 1. Seu período difere do período do mapa sem essa divisão; todas as tabelas devem identificar a convenção temporal.

Para contagens finitas de pontos periódicos, começar pela série formal de Artin–Mazur:

\[
\zeta_T(z)=\exp\left(\sum_{n\ge1}\frac{F_n}{n}z^n\right),
\qquad F_n=\#\operatorname{Fix}(T^n).
\]

Em \(\mathbb Z_2\), a codificação pelo itinerário de paridades conjuga esse mapa ao shift binário unilateral. Consequentemente, \(F_n=2^n\) e \(\zeta_T(z)=(1-2z)^{-1}\), como série formal e inicialmente para \(|z|<1/2\). Este é um caso conhecido (**A**), com espaço de estados explicitado; reproduzi-lo computacionalmente será **B**. Fonte: [Bernstein e Lagarias, The 3x+1 Conjugacy Map](https://websites.umich.edu/~lagarias/doc/bernstein.pdf).

Nos positivos, **se** o único ciclo for 1 ↔ 2, a zeta periódica será \((1-z^2)^{-1}\). Essa hipótese sobre ciclos não exclui trajetórias divergentes: uma zeta de pontos periódicos não registra todos os transientes.

As duas pré-imagens em \(\mathbb Z_2\) são \(b_0(y)=2y\) e \(b_1(y)=(2y-1)/3\). Distinguir:

- operador ponderado \(\mathcal L_g f(y)=\sum_{i=0}^1g(b_i(y))f(b_i(y))\);
- operador de Perron–Frobenius para Haar, \(Pf(y)=\tfrac12[f(2y)+f((2y-1)/3)]\);
- operador de contagem nos positivos, \(\mathcal L_+f(m)=f(2m)+\mathbf1_{m\equiv2\ (3)}f((2m-1)/3)\).

O último mantém a restrição aritmética de integridade. Não aplicar automaticamente a ele a normalização de Haar. Especificar espaço de funções, medida, norma e domínio antes de falar de espectro. Zeta periódica e determinante de um operador infinito exigem uma identidade demonstrada sob hipóteses apropriadas. Referência para esse enquadramento: [Ruelle, Dynamical Zeta Functions and Transfer Operators](https://www.ihes.fr/~ruelle/PUBLICATIONS/137zeta.pdf).

## Etapas, entregáveis e critérios

### CL0 — Especificação e protocolo do laboratório

**Dependência:** nenhuma. Escrever uma especificação com os espaços \(\mathbb N_{>0}\), \(\mathbb Z_2\) e modelos simbólicos separados; convenção de tempo; pesos; observáveis; limites de recursos; tratamento de truncamento e classificações A/B/C/D. Registrar quais afirmações são teoremas, derivações, hipóteses ou alvos numéricos.

Preparar configuração versionada para o piloto, testes e manifesto. Congelar regras, tolerâncias e hashes antes das comparações experimentais; registrar que os casos de validação já têm resposta conhecida. Uma ampliação posterior exige configuração própria.

**Entregáveis:** especificação, protocolo inicial e configuração. **Critério:** cada observável identifica mapa, espaço, medida quando necessária, normalização e significado; nenhuma aproximação finita é apresentada como o sistema infinito.

### CL1 — Zeta exata e controle simbólico

**Dependência:** CL0. Implementar contagens do shift binário e coeficientes da zeta com aritmética exata. Para pesos constantes por ramo, \(a\) e \(b\), verificar a soma periódica ponderada \((a+b)^n\) e a zeta \([1-(a+b)z]^{-1}\).

Recuperar contagens de órbitas primitivas por inversão de Möbius e verificar a identidade \(F_n=\sum_{d\mid n}d\,c_d\), onde \(c_d\) conta órbitas de período mínimo \(d\). Comparar enumeração de palavras/ciclos e expansão formal, usando caminhos computacionais distintos.

**Piloto:** períodos 1–12. **Entregáveis:** tabela de pontos fixos, órbitas primitivas, coeficientes e testes. **Critério:** igualdade exata nos casos previstos, contagens primitivas inteiras não negativas e distinção correta entre período mínimo e período divisor de \(n\). Não interpretar a zeta simples como evidência sobre convergência dos inteiros positivos.

### CL2 — Ciclos e filtro aritmético

**Dependência:** CL1. Para cada palavra de paridades \(\varepsilon_0,\ldots,\varepsilon_{n-1}\), calcular exatamente

\[
k=\sum_j\varepsilon_j,\quad
b=\sum_{j=0}^{n-1}\varepsilon_j2^j3^{\sum_{i=j+1}^{n-1}\varepsilon_i},\quad
x=\frac{b}{2^n-3^k}.
\]

Verificar por iteração racional o itinerário e \(T^n(x)=x\); definir paridade racional por denominador ímpar. Classificar candidatos em inteiro positivo, inteiro negativo, zero e racional não inteiro, com sinal registrado. Canonicalizar ciclos por rotações e verificar período mínimo. Comparar a contagem total à previsão de CL1, antes e depois do filtro positivo.

**Piloto:** períodos 1–12, incluindo \(\operatorname{Fix}(T)=\{0,-1\}\) e \(\operatorname{Fix}(T^2)=\{0,-1,1,2\}\). Processar palavras em fluxo; registrar custo exponencial e benchmark antes de ampliar.

**Entregáveis:** catálogo exato com proveniência das palavras, contagens filtradas e tempo/memória. **Critério:** reconstrução e classificação verificadas sem tolerância de ponto flutuante. Ausência de outros ciclos até o limite examinado é um resultado finito, nunca prova de ausência global.

### CL3 — Regras alternativas e transientes

**Dependência:** CL2. Comparar \(T_a(x)=x/2\) no ramo par e \((ax+1)/2\) no ímpar, inicialmente \(a=3,5\). Derivar o caso simbólico para cada mapa e comparar filtros de integridade/positividade. A coincidência das zetas simbólicas é um controle de perda de informação, não uma identificação das dinâmicas nos positivos.

Em experimento separado, estudar transientes de valores iniciais positivos. Pré-fixar amostragem, conjunto de chegada, orçamento de passos e limite de altura. Registrar tempo de chegada, máximo atingido e censura; distinguir saída do domínio computacional de chegada a um ciclo. Estimar custo em piloto de até 1.000 valores iniciais e 1.000 passos por valor, com teto de altura definido na configuração antes da execução.

**Entregáveis:** comparação de ciclos e relatório separado de transientes. **Critério:** a zeta não incorpora trajetórias censuradas como ciclos; esgotar orçamento não conta como divergência. Interpretar distribuições relativamente à amostragem escolhida, sem pressupor independência temporal.

### CL4 — Operadores e aproximações finitas

**Dependência:** CL1–CL2. Documentar primeiro o operador em funções Hölder sobre \(\mathbb Z_2\), com expoente explícito, e o operador de Haar em \(L^2\). Para \(\mathcal L_+\), analisar separadamente um espaço de sequências escolhido e justificar que a ação está bem definida e é limitada, ou restringir a afirmação ao modelo finito.

Implementar modelos simbólicos finitos com matriz de adjacência ponderada \(A\). Verificar exatamente \(\zeta_A(z)=\det(I-zA)^{-1}\) pela contagem de caminhos fechados e pelos coeficientes de \(\operatorname{tr}(A^n)\). Declarar a projeção, a orientação da matriz e as condições de fronteira.

Não tratar a aplicação de T aos menores representantes módulo \(2^m\) como uma dinâmica quociente bem definida: a divisão por 2 perde um bit. Não fechar artificialmente saídas de um grafo truncado. Testar dependência da resolução e da fronteira antes de atribuir significado a autovalores numéricos. Uma identidade matricial não prova um determinante de Fredholm para o operador infinito.

**Entregáveis:** ficha matemática dos operadores, modelos finitos e testes de traço/determinante. **Critério:** identidade exata nos modelos declarados; qualquer espectro aproximado acompanha definição da aproximação e estudo de estabilidade. Não exigir auto-adjunticidade ou estatística GUE de um operador de transferência.

### CL5 — Reconstrução inversa e comparação com Riemann

**Dependência:** CL2–CL4. Construir experiências com resposta conhecida: fornecer apenas coeficientes finitos da zeta ou traços de modelos finitos e recuperar contagens de ciclos até a ordem disponível. Separar isso de recuperar uma regra dinâmica. Documentar exemplos de regras distintas que compartilham a zeta simbólica, mas têm filtros aritméticos distintos.

Produzir uma tabela de correspondências com hipóteses explícitas:

| Comparação | O que pode ser estudado | Limite |
|---|---|---|
| Órbitas primitivas e repetições | Estrutura de produtos e contagens | Não identifica órbitas de Collatz com primos |
| Pesos e fórmulas de traço | Identidades demonstradas e informação recuperável | Não transferir uma identidade entre operadores diferentes |
| Período e frequência | Efeito da coordenada temporal na transformação | Tempo inteiro de Collatz não é automaticamente \(\log p\) |
| Problema inverso | Identificabilidade e perda de informação | Dados espectrais finitos não selecionam um Hamiltoniano |

Não escolher tempos ou pesos usando os primos para fabricar concordância. Não usar aparência de picos ou GUE como critério de ponte matemática. Qualquer ponte proposta exige mapa, espaços, observáveis e identidade verificável, com hipóteses e condições de refutação.

**Entregáveis:** relatório de reconstrução, tabela de correspondências e atualização das limitações nas etapas 11–13. **Critério:** recuperar corretamente o que os dados permitem e exibir explicitamente o que não identificam. Um resultado negativo sobre identificabilidade pode ser validado.

## Organização e execução futura

- Lógica proposta em `src/riemann_spectra/collatz/`, testes rápidos sem rede, configurações próprias e nenhuma dependência do catálogo de primos ou dos zeros.
- Cada execução futura terá pasta exclusiva em `results/`, configuração resolvida, manifesto, hashes, versões, tabelas, logs, duração e memória. Nenhum caminho proposto aqui representa artefato já produzido.
- Resultados e estados CL0–CL5 serão registrados em [ANDAMENTO.md](ANDAMENTO.md), separadamente dos critérios C1–C3 de m4.
- Preservar arquivos e cópias congelados de m3/m4. Antes de integrar código novo ao pacote, verificar o alcance dos locks para preservar a reprodutibilidade de m4-v3, agora concluído com a ressalva de R2; usar uma árvore de trabalho separada se necessário.
- A primeira entrega de implementação deve cobrir **CL0–CL1**, com o piloto exato até período 12. CL2–CL5 são etapas seguintes, não executadas por esta atualização documental.

Prompt sugerido para essa primeira entrega:

```text
Leia AGENTS.md, PLANO_IMPLEMENTACAO.md, prompt.txt, docs/ANDAMENTO.md
e docs/PLANO_COLLATZ.md. Implemente CL0 e CL1, incluindo o protocolo,
os testes de invariantes e o piloto de períodos 1–12. Preserve os locks
e artefatos de m3/m4. Não reexecute m4-v3 nem leia dados dos zeros.
Registre o que foi implementado, executado e validado, com comandos,
custos e limitações. Encerre a entrega após CL1.
```
