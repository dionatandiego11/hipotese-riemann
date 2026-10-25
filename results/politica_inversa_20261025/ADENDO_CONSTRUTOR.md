# Adendo anterior à implementação do construtor melhorado

25/10/2026. A exploração declarada produziu mu_1=4,mu_2=7,mu_3=10,mu_4=12. A escolha do bloco4 é pós-exploratória e não novidade confirmada. A prova combina o certificado finito com indução e preenchimento de custo.

Antes de implementar/testar o construtor melhorado, acrescenta-se às verificações a construção para todas as unidades mod3^n, n4..8, no custo L(n)=3n+b, b=4+((n-4) mod4). Mantêm-se as construções no custo4n, a busca independente por composições e a grade anterior de preenchimento. Não são acrescentados novos comprimentos ou uma varredura de limiares; L(n) vem da prova, não de otimização dos resultados do teste. Teto30s CPU para a verificação completa; os mesmos limites de ausência de dados reais/reservados e de inferência da declaração original permanecem.
