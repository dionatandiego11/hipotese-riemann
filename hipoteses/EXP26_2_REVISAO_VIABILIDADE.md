# EXP26-2 — revisão da conta de viabilidade

26/09/2026. Revisão documental antes de qualquer cálculo. Nenhum resultado numérico ou poder foi medido. Esta nota corrige a formulação da conta proposta; a declaração de simulação ainda deve fixar suas escolhas.

## 1. A ordem k/N não é a variação universal do fator de forma

No estimador do projeto, para janela, coordenadas, bordas e partição fixas, escreva A=Z−μ, Q=∫w² e D=Σ_{removidos}w_j exp(−2πiτx_j). Então, por álgebra,

    ΔK_c = [−2 Re(A conjugado(D)) + |D|²]/Q.

Para vários sub-blocos, somar numeradores e usar a soma dos Q. Se o procedimento redimensionar janelas, recalcular unfolding, μ ou partições, esses efeitos precisam entrar separadamente; o código atual reparte por índice, portanto não reutilizar a fórmula fixa sem preservar a partição.

Com Q de ordem N, a parcela quadrática pode ter média de ordem k/N sob hipóteses de fases, mas a interferência não pode ser descartada numa realização. Sob estimativas heurísticas |A|~√N e |D|~√k, sua escala é √(k/N); fases coerentes de pares próximos modificam essas estimativas. Isto não prova detectabilidade: sinal pareado e flutuação entre espectros são objetos diferentes.

A hipótese de flutuações relativas de ordem um é plausível em regimes não auto-mediantes, não uma lei uniforme em frequência, janela e suavização. Bins correlacionados não reduzem variância como amostras independentes; estimar covariância ou número efetivo. Referência primária localizada: Prange, *The Spectral Form Factor Is Not Self-Averaging*, https://arxiv.org/abs/chao-dyn/9606010 (resumo consultado, prova não relida nesta rodada).

**Escopo:** B1 inclui resíduo complexo, não somente K_c. Uma simulação GUE sem sinal aritmético pode decidir viabilidade para esse ensemble e essas features, mas não limitar universalmente um resíduo relativo a uma fórmula explícita conhecida. Não encerrar toda a hipótese aritmética com esse único controle.

## 2. Experimento bayesiano local, não teto do B0 inteiro

Se o par perdido e sua posição forem informados por um oráculo, a lacuna observada tem G=s_−+s+s_+. Definir as leis p_MP(G) e p_MA(G) com a seleção correta do par. Em MP, condicionar pelo critério de proximidade e pela maneira de amostrar candidatos; não tratar três espaçamentos GUE consecutivos como independentes nem substituir sua lei por três Wigner surmises sem rotular a aproximação.

Para classes equiprováveis, a acurácia ótima **desse experimento escalar** é (1+TV(p_MP,p_MA))/2. Para falso positivo fixado, usar a curva de Neyman–Pearson; acurácia equiprovável não é sensibilidade a 5% de falso positivo. Priors de classes tampouco são a prevalência de um intervalo defeituoso entre milhares.

Isso não é teto do B0 descrito na ficha: ele pode usar posição, lacunas vizinhas, contagem e dependências globais. Uma alteração física gera uma lacuna nova, mas o observador recebe todas as lacunas e não sabe qual foi alterada. Para uma cota do experimento completo seria necessária a verossimilhança da lista observada, marginalizando posições e níveis omitidos, ou um experimento comprovadamente mais informativo. Um classificador aprendido sobre amostras finitas fornece desempenho atingido, não limite superior de todos os métodos.

A conta local continua útil como diagnóstico idealizado explicitamente rotulado. Mesmo uma baixa acurácia escalar não prova impossibilidade no experimento completo.

## 3. Igualdade de mecanismos e contagem

- Em k=2, MA e MJ são idênticos **se** usam a mesma distribuição do índice inicial e as mesmas exclusões de borda. Unificar as etiquetas nessa severidade; MJ fica separado a partir de k≥6.
- M0 mede falso alarme de “perda seletiva”. Se existe contagem certificada dos zeros no intervalo, a incompletude é conhecida; localizar e escolher o mecanismo são tarefas distintas. A referência certificada deve existir no experimento real, não vir de N escondido pelo gerador.
- Riemann–von Mangoldt com seu termo de argumento não é apenas a densidade suave. A V1 local (`dirichlet_zeros.py`, função `v1_completeness`) compara N_encontrado com `smooth_count`, tolerância 3, e declara que S não é estimado. Não a descrever como Turing ou detecção sem erro. A disponibilidade de métodos certificados de completude é questão separada; referência: https://arxiv.org/abs/1308.6704 .

## 4. Conta curta que faz sentido executar depois de declarada

Teto proposto: 600 segundos-CPU acumulados (dentro do teto de 0,5 h do piloto), sem extensão automática; somente espectros sintéticos, nenhuma leitura Dirichlet. Fixar antes: ensemble/dimensão/unfolding; seleção MP/MA; bordas; frequência/janela; réplicas; sementes; resumos B0/B1; divisão por espectro pai; incerteza; ganho mínimo de interesse.

Separar duas saídas:

1. Distribuições do efeito de remoção sobre K_c e sobre as features B1, com covariâncias, distinguindo médias, RMS pareado e dispersão entre espectros. A diferença em relação ao espectro completo serve à avaliação; não entra como informação que o classificador real não possui.
2. Experimento local da lacuna G e curva ROC de um discriminador especificado, com avaliação fora do ajuste. Só chamar de curva ótima se as verossimilhanças e o erro de sua aproximação forem controlados.

**Seguir/parar:** definir um ganho mínimo antes. Um limite superior abaixo desse ganho pode encerrar o ganho pretendido do método avaliado no modelo substituto; ausência de significância não equivale a ausência de ganho. Intervalo que cruza o alvo ou teto atingido: inconclusivo. Resultado favorável também não valida o diagnóstico em zeros reais. Não transferir para B1 inteiro um resultado que só avaliou K_c.

## 5. Possível mudança de objetivo: priorizar reexames

A proposta é comparar regras que ranqueiam intervalos observados e medir recuperação de pares por custo acumulado. Referências obrigatórias: regra D3 s>1,6 d̄ na ordem vigente; ordenação por largura normalizada; escore de verossimilhança local; eventual escore aumentado B1.

**Métrica primária a declarar:** fração de pares recuperados em um orçamento de reexame fixo, incluindo o custo do diagnóstico. Secundárias: curva recuperação×custo, intervalos reexaminados, avaliações da função L, CPU, pares ainda faltantes. Medir custo com o mesmo procedimento de reexame e com dependência de altura e largura; número de intervalos não é CPU.

p_j/c_j (probabilidade de recuperar um par por custo previsto) é uma candidata heurística de ranking, não política universalmente ótima para buscas adaptativas. Estimar probabilidades, custos e limiares no desenvolvimento, sem usar os acertos reais do D3 como conjunto de teste.

No GUE, pode-se estudar ranking e proxies de custo, mas não medir diretamente segundos de avaliação de uma função L. Usar os 50.018 s/790 intervalos fornecidos pelo usuário como motivação, não orçamento medido para o novo método nem promessa de economia. Uma busca ranqueada também não substitui certificado de completude se parar antes de revisar o necessário.
