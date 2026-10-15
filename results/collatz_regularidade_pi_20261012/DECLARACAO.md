# Declaração anterior — regularidade de π e antecedente Tao, 12/10/2026

Alvo principal documental/analítico: identificar π com Syrac de Tao e
extrair consequências de sua Proposição 1.14 (aceita como teorema externo).
Sem reconstruir integralmente sua prova ou chamar esse objeto de novo.
Diagnóstico exato limitado: K=1..3, conferir recorrência do Lema 1.12
contra geometric_limit já arquivada; testar π_K(−1 mod 3^K)≥2^{−K}.
Para K=0..12 e x∈{0,1,2,−1}, comparar iteração racional de O(x)=(3x+1)/2
com O^K(x)+1=(3/2)^K(x+1); verificar divisibilidade 3^K do numerador.
Não estimar min π_K, ampliar grade ou inferir Lp de uma tabela.
RLIMIT_CPU=60 s. Inteiros/Fraction, sem aleatoriedade, dados de zeros,
CL1, commit ou mudança em resultados congelados. Registrar CPU/parede/RSS.
