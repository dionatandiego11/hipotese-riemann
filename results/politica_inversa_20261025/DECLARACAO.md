# Declaração — custo uniforme por blocos inversos

25/10/2026. Após derivação preliminar do limite4n e da recorrência de custo mínimo, antes de implementar ou calcular a política abaixo. Não é teste de novidade.

Parte1: gerar certificado da base n4/S16 usando somente palavras positivas com limites(2,6,18,54), custo16; guardar uma palavra lexicográfica por unidade mod81. Comparar suporte e contagens com o gerador existente. Esta base já tinha cobertura na tabela completa consultada, fato divulgado: não é amostra reservada.

Parte2: para r=1,2,3,4, todas as unidades x mod3^(r+1), calcular o menor custo de r ramos inversos (2^e*x-1)/3 que preservem unidade em cada etapa e no final. A política elementar e<=4 dá custo<=4r; portanto buscar e<=4r inclui todo possível mínimo. Recorrência exata de Bellman por redução de profundidade, desempate lexicográfico. Guardar cada custo/caminho e o máximo mu_r. Comparar os mínimos com uma segunda busca exaustiva das composições positivas de comprimento r e soma<=4r, testando a condição afim final de unidade. Uma melhora sobre4r poderá ser usada num lema uniforme, mas não se promoverá um valor escolhido após a tabela a confirmação independente.

Parte3: verificar a injeção de aumentar o último expoente e o novo limite uniforme SOMENTE na grade já usada n4..8,S=2n-2..2n+2, se aplicável. Além disso, gerar para n4..8 todas as unidades no custo4n pelo algoritmo construtivo ancorado no certificado n4/S16, conferindo limites, custo e resíduo exatos. Não criar varredura de limiares de cobertura nem ampliar n para procurar sucesso.

Teto30s CPU com RLIMIT_CPU, inteiros exatos, sem rede, Monte Carlo, órbitas positivas ou dados de zeros. Caso o teto não baste, relatar execução parcial e não ampliar orçamento. Artefatos: declaração, manifesto, código/cópias, certificado base, políticas por r, tabelas, log e resumo. A inferência assintótica será por prova, não extrapolação dos n testados. Novidade e revisão independente permanecem pendentes.
