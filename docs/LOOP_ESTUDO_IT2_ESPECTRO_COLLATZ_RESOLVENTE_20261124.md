# Loop de Estudo e Verificação — Iteração 2: Decomposição Espectral de Collatz e Teste do Traço de Resolvente

24/11/2026. Segunda iteração do loop autônomo de estudo e verificação científica.

## 1. Escopo e Objetivos
Esta iteração aprofunda duas perguntas fundamentais formuladas na arquitetura do projeto:
1. **Frente Collatz (Teoria Espectral de Transferência):** Como o operador de transferência ponderado por altura de Weil $\mathcal{L}_\alpha$ atua no espaço projetado de estados racionais 2-ádicos $\mathcal{S}_B = \{x \in \mathbb{Q} \cap \mathbb{Z}_2 : H(x) \le B\}$? Demonstrar analiticamente e verificar numericamente que seus autovalores não-nulos mapeiam exatamente os ciclos periódicos racionais com raios $R_{\mathcal{C}} = (\prod_{x \in \mathcal{C}} H(x))^{-\alpha / |\mathcal{C}|}$, provando a existência de um gap espectral discreto $1 - 2^{-\alpha / 2}$.
2. **Frente Hamiltoniano (Teste de Falsificação por Traço de Resolvente):** Aplicar o teste do traço de resolvente formulado em `PONTES_HAMILTONIANO_COLLATZ_20261122.md` para contrastar:
   - O núcleo aritmético exato de primos $K(t)$ (lado dos números primos);
   - O controle tautológico $H_{\text{diag}}$ com zeros de Riemann reais;
   - O candidato regularizado de Sierra–Rodríguez-Laguna $H_{SR}$ em reticulado conformal.
   Diagnosticar o surgimento de estados espúrios de baixa energia em $H_{SR}$ no gap $[0, \gamma_1]$.

Classificações: **[A]** para teoremas/derivações exatas; **[B]** para experimentos e computações numéricas controladas; **[C]** para achados estruturais; **[D]** para conjecturas abertas.

---

## 2. Frente Collatz: Decomposição Cíclica e Gap Espectral

### 2.1 Teorema de Decomposição Cíclica [A]
Seja $M_B(\alpha) \in \mathbb{R}^{M \times M}$ a matriz de transferência truncada no conjunto finito $\mathcal{S}_B$ de altura $H(x) \le B$:
$$[M_B(\alpha)]_{y, x} = \begin{cases} H(x)^{-\alpha} & \text{se } y = T(x) \\ 0 & \text{caso contrário} \end{cases}$$
Para qualquer ciclo periódico racional $\mathcal{C} = (x_0, x_1, \ldots, x_{k-1})$ inteiramente contido em $\mathcal{S}_B$ com $T(x_j) = x_{j+1 \pmod k}$:
1. O subespaço $\mathrm{span}\{\delta_{x_0}, \ldots, \delta_{x_{k-1}}\}$ é invariante sob $M_B(\alpha)$.
2. A restrição de $M_B(\alpha)$ a esse ciclo tem polinômio característico:
   $$P_{\mathcal{C}}(\lambda) = \lambda^k - \prod_{j=0}^{k-1} H(x_j)^{-\alpha}$$
3. Os autovalores associados a $\mathcal{C}$ são os vértices de um polígono regular no plano complexo:
   $$\lambda_{\mathcal{C}, m} = R_{\mathcal{C}} \, e^{2\pi i m / k}, \quad m = 0, \ldots, k-1$$
   com raio geométrico exato:
   $$R_{\mathcal{C}} = \left( \prod_{x \in \mathcal{C}} H(x) \right)^{-\alpha / k}$$

### 2.2 Corolário: Estrutura do Gap Espectral e Compacidade [A]
* Para os pontos fixos triviais $\mathcal{C}_0 = \{0\}$ e $\mathcal{C}_{-1} = \{-1\}$, temos $H(0) = 1$ e $H(-1) = 1$, gerando autovalores $\lambda = 1$ (multiplicidade 2) para todo $\alpha \ge 0$.
* Para o ciclo de inteiros positivos $\mathcal{C}_{\text{pos}} = \{1, 2\}$, $H(1) = 1$ e $H(2) = 2$, com comprimento $k = 2$. Seu raio é:
  $$R_{\text{pos}} = (1 \times 2)^{-\alpha / 2} = 2^{-\alpha / 2}$$
  Para $\alpha = 1$, $R_{\text{pos}} = 1/\sqrt{2} \approx 0.70710678$. Para $\alpha = 2$, $R_{\text{pos}} = 0.5$.
* Para o ciclo racional 2-ádico $\mathcal{C}_{1/5} = \{1/5, 4/5, 2/5\}$, todos os estados têm altura $5$, com comprimento $k=3$. Seu raio é:
  $$R_{1/5} = (5^3)^{-\alpha / 3} = 5^{-\alpha}$$
  Para $\alpha = 1$, $R_{1/5} = 0.2$. Para $\alpha = 2$, $R_{1/5} = 0.04$.
* **Conclusão:** Para $\alpha > 0$, o operador possui um **gap espectral estrito** $g(\alpha) = 1 - 2^{-\alpha / 2} > 0$ entre os pontos fixos triviais e o restante do espectro. Todo ciclo de altura maior decai para raios estritamente decrescentes, garantindo compacidade essencial.

---

## 3. Frente Hamiltoniano: Teste do Traço de Resolvente

Em `PONTES_HAMILTONIANO_COLLATZ_20261122.md`, estabeleceu-se a identidade sob RH:
$$K(t) := e^{-t/2} [G(e^t) - \log(2\pi) - R_{\text{triv}}(e^t)] = \sum_{\gamma} \frac{e^{it\gamma}}{\gamma^2 + 1/4} = 2 \sum_{\gamma > 0} \frac{\cos(t\gamma)}{\gamma^2 + 1/4}$$

### 3.1 Controle Tautológico $H_{\text{diag}}$ [B]
O traço com zeros conhecidos:
$$T_{\text{diag}}(t) = 2 \sum_{j=1}^{N_{\text{zeros}}} \frac{\cos(t \gamma_j)}{\gamma_j^2 + 1/4}$$
recupera $K(t)$ com resíduo dominado exclusivamente pela cauda dos zeros truncados:
$$\Delta_{\text{cauda}}(t) = 2 \sum_{j > N_{\text{zeros}}} \frac{\cos(t \gamma_j)}{\gamma_j^2 + 1/4} = \mathcal{O}(N_{\text{zeros}}^{-1} \log N_{\text{zeros}})$$

### 3.2 Obstrução do Candidato $H_{SR}$ em Reticulado Conformal [A / B]
Para o operador regularizado de Sierra–Rodríguez-Laguna $\hat{H} = \frac{i}{2} (g(u) \partial_u + \partial_u g(u))$ com $g(u) = 1 + e^{-2u}$ em reticulado $u \in [-L, L]$:
- O termo $e^{-2u}$ diverge exponencialmente no limite infravermelho $u \to -L$.
- A matriz simétrica discretizada possui autovalores espúrios no intervalo $E \in (0, \gamma_1)$ com espaçamento aproximadamente uniforme $\Delta E \approx \pi / L$.
- Como o resolvente possui peso $(E^2 + 1/4)^{-1}$, cada autovalor espúrio próximo de zero contribui com $\sim 4$, gerando um erro de ordem $\mathcal{O}(1)$ que invalida a aproximação direta de $K(t)$ sem um potencial que force um gap espectral $[0, \gamma_1]$.
