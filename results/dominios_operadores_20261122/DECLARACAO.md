# Declaração — domínios de operadores, 22/11/2026

Desenvolvimento determinístico sem dados de zeros. Antes de implementar. Mantidos os artefatos da rodada anterior.

Collatz: T em A=Q∩Z2; preimagens2y e(2y-1)/3; peso d(x)^(-s). Implementar transferência em suportes finitos, s=1 nos controles. Conferir as duas preimagens para y=0,2,5,-1,1/5,2/7; vetores adjuntos nas8 imagens y=3k+2,k0..7, com produto Gram exatamente2I e LL*δ_y=2δ_y. Conferir x_k=1+2^k/5^k,k1..8, denominador5^k, distância2-adica2^(-k), peso5^(-k). Provas de norma sqrt2, não compacidade e descontinuidade serão analíticas; testes finitos são só controles.

Hamiltoniano: usar prime_trace_kernel anterior, sem editar. A80 dígitos conferir R'(h)=exp(h)atanh(exp(-h))-1 por derivada numérica independente para h=0.01,0.0001,0.000001,0.00000001, tolerância1e-60. Relatar2(K0-K(h))/(h log(1/h)) e correção2(K0-K(h))/h-log(1/h), que têm limites previstos1 e1-gamma-log(2pi). Não ajustar constantes aos dados nem transformar esse diagnóstico em prova.

Teto30s CPU, nenhuma aleatoriedade. Se um teste falhar, preservar saída e diagnosticar. Sem novas profundidades/períodos ou enumeração de órbitas positivas.
