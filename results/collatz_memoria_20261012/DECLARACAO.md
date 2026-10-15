# Declaração — memória aritmética finita, Collatz

Data: 12/10/2026. Escopo: avançar no erro de coarsening dos filtros, priorizando a normalização natural de média um. As identidades e cotas foram formuladas antes desta verificação. Não há afirmação de novidade ou hipótese de Collatz.

Objetos: Haar μ em Z3; A=(3/4)L+; F_m=A^m1; μ_m=F_m μ. Operador dual Qf=(3/4)f(x/2)+(1/4)f((3x+1)/2). Ele é um operador auxiliar deduzido exatamente da contagem de árvores, não um modelo de paridades independentes de órbitas positivas. E_K é a média em classes módulo 3^K.

Alvos: fechamento exato das distribuições em módulo fixo; contração Hölder de Q; erro uniforme de coarsening em médias de observáveis regulares; distinguir de ||F_m−E_KF_m||∞ e da cauda de Fourier, não supostos pequenos.

Controle exato declarado, após implementação separada em collatz/coarse_memory.py:
1. K=0,1,2,3; m=0,…,6. Comparar evolução de probabilidades nos 3^K estados com E_K F_m, calculado pela expansão de filtros anterior em um período comum. Contagens em inteiros/frações; tolerância zero.
2. K=0,…,3. Resolver probabilidades estacionárias por eliminação racional; conferir massa 1, não negatividade, equação estacionária e compatibilidade por redução de K+1 para K. Nenhuma matriz maior que 27×27.
3. K=0,…,3; m=0,…,12. Conferir distância de variação total à estacionária ≤ Pr[Binomial(m,1/4)<K], incluindo m=0 e K=0.
4. K=1,…,3. Conferir seminorma Hölder α=1: [Qf]1≤(5/6)[f]1 em observáveis declaradas f(a)=a e indicadores de cada resíduo. Operação Q nas observáveis independente do transporte de probabilidades.
5. Testes rápidos para orientação de matriz, adjunção em Haar finito, nível K=0, massa, vazio e domínio de vetor.

Orçamento: 60 segundos-CPU reais via RLIMIT_CPU, sem extensão; memória prevista <128 MiB. Nenhuma aleatorização; nenhum espectro, zero, teste reservado, ciclo ou transiente. Arrays inteiros/frações e níveis pequenos. CL1 segue fora deste escopo.

Leitura bibliográfica: Applegate–Lagarias 1995, §6, pp. 204–208, fonte já arquivada. Continuidade da função limite foi conjecturada nessa fonte; não inferir seu estado atual sem revisão posterior. Esta execução não procura padrão novo nem decide a cota forte global.

Saídas: nota com provas, código independente de riemann_spectra, controles, manifesto, hashes, CPU/parede/memória e limite. Preservar falhas; não ajustar profundidade ou tolerância depois do resultado.
