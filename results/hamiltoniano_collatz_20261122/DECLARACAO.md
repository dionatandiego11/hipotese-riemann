# Declaração antes da implementação — 22/11/2026

Escopo determinístico de desenvolvimento, sem dados de zeros. Hipóteses analíticas e resultados conhecidos registrados como controles, não novidades.

Hamiltoniano: implementar G e o resto trivial R(x)=-sum_{k>=1}x^(-2k)/(2k(2k+1)); seu limite em1 é log2-1. Construir K(t)=exp(-|t|/2)[G(exp(|t|))-log(2pi)-R(exp(|t|))]. K(0)=2+gamma-log(4pi). Conferir resto por série independente nos t=1/4,1/2,1,2,3 a60 dígitos com cauda explícita; grade de Gram nos nós0, log2/2,log2,log3,log5,log8; diagnóstico float PSD com tolerância1e-10, sem usar como prova.

Collatz: mapa T=(3x+1)/2 ímpar e x/2 par, comparação S=(x-1)/2 ímpar e x/2 par. Enumerar palavras binárias de períodos1..8 exatamente, por Fraction, verificar órbita/paridade e ponto fixo. Peso multiplicativo por passo denom(x)^(-s), s=1; relatar soma sobre Fix(T^n) com denom^(-n). Relatar filtro positivo inteiro como diagnóstico finito. Nenhum ciclo omitido, sem extrapolação à conjectura. Controle previsto: Z2_T(1)=4 e Z2_S(1)=2+2/9, enquanto ambos têm4 pontos sem peso.

Teto60s CPU, sem aleatoriedade. Testes analíticos do resto, identidades de período2, contagens2^n, órbitas por implementação direta e invariância dos denominadores. Se alguma verificação falhar, preservar saída e diagnosticar antes de aceitar resultados dependentes. Esta rodada não permite anunciar Hamiltoniano físico, ponte Riemann-Collatz ou novidade; eventual busca bibliográfica ampliada fica separada.
