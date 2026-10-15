# Declaração — primeira correção local da regularização

13/10/2026, antes de código e cálculos. Sem dados de zeros.

Alvo: C+(ε)=S+εB++O(ε²), C−(ε)=S+εB−+O(ε²), em janela fixa com zeros internos simples; B±=FP integral |H/F|² /π ±2ΣRe(a conj b). Separar simetrização e extrapolação2C(ε/2)−C(ε). Não é previsão de inferiores emT.

Controles a60 dígitos: q(s)=exp(k(s−ρ))/(s−ρ), comρ=1/2+2i, janela[1,3], k em{0;0,7}; ε em{0,02;0,01;0,005}. Integral direta por quadratura e expressão arctan independente; erro relativo≤1e−40. Viés de simetrização tem coeficiente−2/π, inclusive k=0. Extrapolação tem erro absoluto≤20ε² nesta grade. Dois polos, q=1/[(s−ρ1)(s−ρ2)], ρ1=1/2+i, ρ2=1/2+3i, janela[0,4]: comparar coeficiente analítico da parte finita por frações parciais com (C(ε)−S)/ε a ε=0,01;0,005;0,0025; erro absoluto≤20ε e erro final menor que inicial. Efeito de pares próximos: modelo de toda a reta já derivado, d={1;0,01}, ε/d={0,1;0,01}; extrapolação não acrescenta uniformidade emd. Teto60s CPU, sem Monte Carlo, sem zeros reais.
