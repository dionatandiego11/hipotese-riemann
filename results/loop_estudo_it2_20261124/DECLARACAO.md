# Declaração — Loop de Estudo e Verificação (Iteração 2), 24/11/2026

Desenvolvimento determinístico. Pré-registro anterior à execução da rodada.

1. **Frente Collatz — Espectro Cíclico e Gap Espectral de Altura:**
   No conjunto de estados $\mathcal{S}_{10}$ (83 racionais 2-ádicos com altura $H(x) \le 10$), construir a matriz de transferência truncada $M_{10}(\alpha)$ para $\alpha \in \{0.5, 1.0, 2.0\}$. Verificar numericamente que:
   - Os dois maiores autovalores são identicamente $1.0$ (pontos fixos $0$ e $-1$, $H=1$);
   - O par seguinte é $\pm 2^{-\alpha / 2}$ (ciclo $\{1, 2\}$, produto de alturas 2);
   - Os autovalores do 3-ciclo racional $\{1/5, 4/5, 2/5\}$ têm módulo $5^{-\alpha}$;
   - O raio espectral é $1.0$ e o gap espectral é $g(\alpha) = 1 - 2^{-\alpha / 2}$.

2. **Frente Hamiltoniano — Teste do Traço de Resolvente:**
   - Para $t \in \{0.5, 1.0\}$, calcular o traço de resolvente do controle tautológico $H_{\text{diag}}$ com os primeiros 500 zeros não triviais de Riemann:
     $$T_{\text{diag}}(t) = 2 \sum_{j=1}^{500} \frac{\cos(t\gamma_j)}{\gamma_j^2 + 1/4}$$
     e comparar com o núcleo exato de primos $K(t)$ (`prime_kernel(t)`), confirmando resíduo $< 10^{-4}$ devido unicamente à cauda finita dos zeros.
   - Para o candidato regularizado de Sierra–Rodríguez-Laguna $H_{SR}$ discretizado em reticulado conformal $N=300, L=5$, demonstrar a emergência de pelo menos 10 modos positivos espúrios abaixo de $\gamma_1 \approx 14.1347$ com espaçamento $\Delta E \approx \pi / L$, gerando um erro de traço de resolvente de ordem $\mathcal{O}(1)$ que falsifica a discretização conformal ingênua.

Teto de 30s CPU. Sem ajuste livre de parâmetros.
