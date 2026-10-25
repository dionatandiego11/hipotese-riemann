# Declaração — parcela equilibrada máxima da semente completa

20/10/2026. Após derivação do critério min(N0,N1,N2), antes de implementar ou enumerar a semente. Exploração finita determinística; sem alegação de novidade ou confirmação assintótica.

Enumerar TODAS as11664 palavras cronológicas de quatro expoentes com limites(2,6,18,54), custos totais4..80 e resíduos mod81. Comparar por inteiro com generator_counts(4,76). Em cada custo/pai mod27, definir capacidade M=min das3 contagens de filhos. Construir catálogo lexicográfico de M triplas disjuntas e guardar a tabela completa, incluindo M=0. Conferir custo, limites, disjunção e balanço.

Provar e conferir que a capacidade domina a semente da família H em cada estado. Propagar essa capacidade pelo mesmo kernel positivo de custo/resíduo grosso. Grade fixa n=4,...,8, S=2n-2,...,2n+2, como na execução anterior, sem expandi-la para procurar cobertura. Comparar com H e com min das3 contagens finas da distribuição completa em n. Relatar pais sem último filho, pais completos sem grupo transportado e pais com grupo transportado. Se houver pais completos sem grupo transportado, guardar a primeira classe lexicográfica como testemunha exploratória dessa limitação; não escolhê-la por outra medida. Falta de tal testemunha não prova propriedade assintótica.

A maior parcela EQUILIBRADA transportada de prefixos4 tem escopo restrito: mesmo custo do prefixo e mesmo sufixo em cada grupo. Seu fracasso não exclui grupos com prefixos de custos diferentes compensados pelo sufixo, blocos maiores ou reescritas globais.

Teto30s de CPU via RLIMIT_CPU, inteiros/Fraction, sem rede, aleatoriedade, órbitas positivas, zeros reais/reservados ou produção extensa. Uma execução; manifesto, hashes/cópias, catálogo, tabela, resumo e log. Falhas preservadas; alterar método ou ampliar grade exige novo registro.
