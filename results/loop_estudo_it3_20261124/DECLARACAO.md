# Declaração — Loop de Estudo e Verificação (Iteração 3), 24/11/2026

Desenvolvimento determinístico. Pré-registro anterior à execução da rodada.

1. **Equação Funcional e Fundo Suave de Duas Escalas:**
   A 40 dígitos de precisão com mpmath, verificar que o produto de dilatação de Collatz $P(s) = \sum_{i=0}^\infty \log(1 - e^{-2 \cdot 3^i s})$ satisfaz a equação funcional $P(s) - P(3s) = \log(1 - e^{-2s})$ com erro absoluto $< 10^{-35}$ para $s \in \{0.05, 0.01, 0.001, 0.0001\}$.
   Verificar que o termo suave $P_0(s) = - \frac{(\log s)^2}{2 \log 3} + (1/2 - \frac{\log 2}{\log 3})\log s$ satisfaz $P_0(s) - P_0(3s) = \log s + \log 2$ com resíduo $< 10^{-35}$.

2. **Coeficientes de Fourier da Função Zeta de Riemann:**
   Calcular exatamente os coeficientes de Fourier teóricos gerados pelos polos de Mellin:
   $$c_n = - \frac{2^{i\tau_n}}{\log 3} \Gamma(-i\tau_n) \zeta(1 - i\tau_n), \quad \tau_n = \frac{2\pi n}{\log 3}$$
   para $n = 1, \ldots, 5$. Registrar módulo e fase a 40 dígitos, demonstrando o decaimento super-exponencial $|c_{n+1}| / |c_n| \approx \exp(-\pi^2 / \log 3) \approx 1.25 \times 10^{-4}$.

3. **Verificação de Concordância Numérica Collatz–Zeta:**
   Amostrando 100 pontos no intervalo de um período logarítmico $s \in [10^{-12}, 3 \times 10^{-12}]$, calcular a projeção numérica de Fourier de $P(s) - P_0(s)$ e verificar que o coeficiente numérico $c_{1, \text{num}}$ converge para o valor teórico $c_{1, \text{theo}}$ previsto pela função zeta de Riemann com erro relativo $< 10^{-6}$.

Teto de 30s CPU. Determinismo estrito.
