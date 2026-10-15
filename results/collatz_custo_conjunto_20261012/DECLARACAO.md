# Declaração anterior — custo conjunto e alcance mesoscópico, 12/10/2026

Objetivo analítico: fórmula conjunta custo/caractere e controle das razões
de coeficientes. Não transportar automaticamente resultados de Tao ou de
preprints. Não escolher alvos pela tabela.
Verificações exatas limitadas: ℓ=2..5, k=1..2ℓ, comparar
q_ℓ(k)/B_ℓ(k) com A_ℓ(θ), θ=k/(k+ℓ−1), e conferir majorante de erro
(1/(2k)) Σ_E θ^{D_E}D_E(D_E−1). Enumerar apenas subconjuntos desses
até cinco índices. Sem uso de ponto flutuante como cota.
Diagnóstico de prefixos: ℓ=16,32,64,128; k=ℓ−isqrt(ℓ),ℓ,ℓ+isqrt(ℓ);
R=1,2,3; somar TV entre prefixo condicionado e lei geométrica somente
sobre as tuplas com cada j_i∈{0,1,2,3}. Relatar como soma parcial, jamais
TV completa ou prova de convergência. Todas as probabilidades por inteiros
q e Fraction; sem resíduos módulo 3^ℓ ou órbitas.
Teto RLIMIT_CPU=60 s. Sem dados de zeros, aleatoriedade, CL1, ampliação de
grade, edição de protocolos anteriores ou commit. Critério técnico:
majorante finita vale em todos os casos; diagnóstico não decide teorema.
