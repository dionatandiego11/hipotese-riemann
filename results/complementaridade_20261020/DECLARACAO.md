# Declaração — complementaridade e órbita dos expoentes finais

20/10/2026. Após derivação analítica da recorrência e do período, antes de implementação/verificação. Diagnóstico exato, sem inferência assintótica ou reivindicação de novidade.

Parte1: mesma grade n=4,...,8,S=2n-2,...,2n+2. Em cada pai atingido, decompor o vetor dos3 filhos por expoente final e, guardando o custo S-e, comparar a soma com o gerador existente. Calcular suporte de cada parcela e o menor número de parcelas cuja união cobre os3 filhos:1,2 ou3; incompleto se impossível. Seleção por ordem crescente dos expoentes, sem mudar o critério após ler os resultados. Guardar todas as classes e a primeira testemunha de cada caso, além do caso n5/S9/pai47 já conhecido. Conferir interseção dos filhos ausentes e ausência de pais predecessores repetidos nessa faixa.

Parte2: n em{3,4,5,6}, pais a em{1,2,4,5}, e0 menor expoente positivo tal que2^e0*a=1 mod3. Com R=3^(n-2), verificar durante3R passos a identidade c_{e+2}=4c_e+1, períodoR do pai b=c modR, período3R do estado fino c mod3R, e rotação k->k+1 em e->e+2R. Esta parte é álgebra sem um orçamento físico de custo, e não será confundida com acessibilidade no custo central.

Teto30s CPU via RLIMIT_CPU, inteiros exatos, sem rede, Monte Carlo, órbitas positivas, zeros reais/reservados ou aumento de comprimentos. Manifesto, hashes/cópias, log, tabelas completas e resumo. Não concluir que duas parcelas bastem se aparecer necessidade de3; não extrapolar a grade a n grande. Os dados anteriores ficam intactos.
