# Declaração — identidade de cinco expoentes após o diagnóstico da semente

20/10/2026. Seleção exploratória após consultar a primeira classe da execução semente_completa_20261020: n5/S9/pai47, contagens(1,1,1), sem grupo transportado de prefixo4. Os caminhos abaixo foram derivados algebricamente a partir dessa classe antes da implementação deste teste; não é confirmação independente.

Família: (1,1,3,1,3+d), (2,2,1,1,3+d), (1,2,3,2,1+d). Numeradores esperados331,493,655, custo9+d, limites cronológicos2,6,18,54,162. Proposta válida para0<=d<=159 e qualquer sufixo válido. Diferenças dos numeradores162=2*81 dão três filhos no último dígito.

Verificação fixa: d em{0,1,159}; sufixos(),(1,),(1,1). Inteiros/Fraction, verificar limites, custo, coeficiente linear, diferença exata entre offsets e três filhos. No caso base n5/S9, comparar os três resíduos com as contagens completas existentes e a capacidade transportada da semente4, que deve ser0 nesse pai. Preservar dados e hipótese original se algum teste falhar; nenhuma ampliação de d/sufixos.

Teto30s de CPU via RLIMIT_CPU; manifesto, hashes/cópias e log. Sem Monte Carlo, órbitas positivas, zeros reais/reservados, produção longa ou inferência sobre cobertura assintótica. A extração de uma nova identidade é desenvolvimento pós-exploração, não novidade estabelecida.
