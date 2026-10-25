# Declaração — perfil polar do gerador real e do erro

14/10/2026. Antes de implementação/verificações. Sem dados de zeros.

Alvo analítico: para janela fixa, ν=λε, u=ν+εz, λ∈(0,1/2) fixo e z em compacto, provar εMj→πSj[1+z/(1+λ)] e εGj→κj/2[1+z/(1+λ)]. Identificar a consequência para a norma do resto. Isso não demonstra Sj~κjT/(2π).

Controles B a50 dígitos: um polo artificialρ=1/2+2i, janela[1,3], λ={0,25;0,4}, ε={0,04;0,02;0,01}, z={0;0,5;0,5i;−0,5;−0,5i}. Quadratura contra fórmula fechada, erro relativo≤1e−35; aproximação do perfil, erro absoluto≤20ε. Dois polosρ=1/2+i,1/2+3i, janela[0,4], λ=0,25, z={0;0,5;0,5i}, ε={0,02;0,01}; erro absoluto≤30ε e desvio final menor que inicial. Perfil aritmético G8, q={4,5}, ε={0,001;0,0001}, λ=0,25, z={0,5;0,5i}: erro relativo≤0,02 contraκ8/2 vezes o perfil. Nenhuma média real deL.

Teto60s CPU. Rodar apenas testes novos e testes pertinentes de fatores aritméticos; não repetir toda a cadeia já aprovada. O limite comλ fixo é suficiente para uma condição necessária da hipóteseU; uniformidade emλ↓0 não será presumida nem alegada com estes controles.
