# Declaração — blocos cronológicos de três expoentes

19/10/2026. Exploração delimitada, sem hipótese de novidade ou cobertura assintótica. Antes de implementar ou enumerar os blocos.

Alvo: localizar identidades de custo fixado que preservem o resíduo módulo3^(ell-1) e preencham os três filhos no módulo3^ell. Para um bloco de3 que começa na posição i, a diferença dos numeradores precisa ser divisível por3^(i+1), pois o sufixo tem ell-i-2 ramos.

Grade: i em{1,2,3}; limites do bloco(2*3^(i-1),2*3^i,2*3^(i+1)); soma S de3 a18. Enumerar composições positivas desses totais apenas, agrupar B3=9+3*2^a+2^(a+b) módulo3^(i+1), registrar quantos dos3 filhos aparecem módulo3^(i+2). Guardar todos os resultados e a primeira tripla lexicográfica, se existir, por i,S e classe. Também construir a tabela completa a em1..2,b em1..6 do primeiro bloco, sem restrição de S, para testar a obstrução de no máximo dois pares por classe mod9.

Não usar órbitas positivas ou zeros; não aumentar limites ou somas para encontrar testemunha. Uma testemunha será exploratória, seguida de derivação e verificação independente das identidades escolhidas. Falta de testemunha nessa grade não prova impossibilidade geral. Teto30s de CPU com RLIMIT_CPU, inteiros/Fraction, sementes não aplicáveis. Manifesto, cópias, tabelas e log próprios; nenhuma alteração em execuções anteriores.

Após a leitura da tabela declarada, será permitido selecionar identidades para a prova algébrica, com divulgação da seleção pós-exploração. Uma verificação posterior manterá a mesma grade e conferirá sua aplicação nos menores comprimentos ell=i+2 com prefixo todo1, e no mesmo comprimento acrescido de um sufixo1. Isso não será chamado de confirmação em dados novos.
