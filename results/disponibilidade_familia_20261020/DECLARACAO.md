# Declaração — disponibilidade da família H por custo/resíduo

20/10/2026. Após formulação analítica da recorrência e do contraexemplo ell8/S16; antes de implementação e enumeração. Verificação de identidades, sem teste confirmatório de novidade.

Objeto H: família das posições2–4 definida em19/10, extra d em0..45. Contar grupos completos por resíduo módulo3^(ell-1), conservando custo total; o número de palavras de H no pai é3 vezes o número de grupos.

Grade fixa: ell=4,...,8, S=2ell-2,...,2ell+2. Comparar recorrência com enumeração direta de H e comparar os pais com a contagem total já existente generator_counts. Verificar balanço exato entre os3 filhos; gravar também os casos sem H, sem alterar o alvo. Para a semente ell4, conferir S57 e58 como limites do parâmetro d, sem usar esses casos para ampliar a grade de disponibilidade.

Testemunha fixada antes do cálculo: ell8/S16. H tem um grupo somente (prefixo1,extra0,sufixo de4 expoentes1), cujo pai previsto é971 mod2187. A palavra(1,1,1,1,1,1,1,9) tem o mesmo custo e pai previsto299 mod2187, portanto a disponibilidade de H nesse pai é0. Comparar contra método de contagem existente e composição afim exata.

Teto30 segundos de CPU, RLIMIT_CPU, uma execução; inteiros/Fraction, sem Monte Carlo, órbitas positivas, dados de zeros ou rede. Manifesto, cópias do código, log, tabela completa e resumo. A falha de disponibilidade neste caso não será generalizada a comprimentos arbitrariamente grandes, a outras famílias ou à cobertura global.
