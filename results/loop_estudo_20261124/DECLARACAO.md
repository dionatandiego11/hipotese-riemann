# Declaração — Loop de Estudo e Verificação (Iteração 1), 24/11/2026

Desenvolvimento determinístico sem dados de zeros reais ou ajuste de parâmetros. Pré-registro anterior à execução.

1. **Frente Hamiltoniano — BBM (Bender, Brody & Müller):**
   A 60 dígitos com mpmath, verificar que para o primeiro zero $\gamma_1 \approx 14.1347251417$, a densidade da autofunção candidata $\psi_z(x) = -\zeta(z, x+1)$ segue assintoticamente a expansão de Euler-Maclaurin $|\psi_z(x)|^2 \sim (x+1)/|z-1|^2$ para $x \in \{10^3, 10^4, 10^5\}$, com erro relativo $< 0.01$, provando a divergência quadrática da norma $L^2(0, \infty)$ e a não-pertinência ao espaço de Hilbert padrão.

2. **Frente Hamiltoniano — Sierra & Rodríguez-Laguna:**
   A 60 dígitos, verificar que a solução exata $\psi_E(p) = (p + \ell_p^2/p)^{-1/2} (p^2 + \ell_p^2)^{-iE/2}$ satisfaz a equação diferencial de autovalores $H_{SR}\psi = E\psi$ com resíduo $< 10^{-40}$ em $p \in \{0.5, 1.0, 2.5, 10.0\}$. Documentar a prova analítica de que com fronteiras fixas $[p_{\min}, p_{\max}]$ o espectro é puramente equidistante.

3. **Frente Collatz — Transferência com Peso de Altura de Weil:**
   Com aritmética exata de Fraction, verificar que o peso $w_\alpha(x) = \max(|p|, |q|)^{-\alpha}$ decai como $k^{-\alpha}$ na sequência de inteiros $k \in \{1..10\}$, restaurando o decaimento ausente no peso de denominadores $d(x)^{-s}$. Verificar a finitude de Northcott para alturas $\le 10$ e a consistência da relação de adjunção em pré-imagens.

Teto de 30s CPU. Nenhuma aleatoriedade. Sem dados de zeros como entrada do operador.
