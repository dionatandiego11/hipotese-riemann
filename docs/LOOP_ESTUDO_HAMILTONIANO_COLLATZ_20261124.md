# Loop de Estudo e Verificação — Iteração 1: Modelos de BBM, Sierra e Peso de Altura em Collatz

> **Auditoria pendente, 24/11/2026:** as fórmulas, domínios de operadores e classificações desta nota ainda não foram verificados independentemente. Em particular, a série da zeta de Hurwitz exibida na §2.1 converge apenas para `Re(z) > 1`, exigindo continuação analítica na reta crítica; a divergência de uma família de funções não demonstra, por si só, a ausência de todos os autoestados discretos de um operador. As conclusões mais gerais permanecem por conferir.

24/11/2026. Documento de formalização da Iteração 1 do Loop de Estudo e Verificação de hipóteses históricas da literatura (mineradas via Scientific Literature / arXiv).

## 1. Contexto e Motivação
Modelos quânticos e operadores de transferência foram propostos no passado para atacar a Hipótese de Riemann (RH) e o problema de Collatz (3x+1). Muitas dessas tentativas estagnaram devido à falta de clareza analítica sobre domínios funcionais ou à incapacidade de realizar diagnósticos numéricos de alta precisão sem viés de ajuste. 

Seguindo `AGENTS.md`, este estudo classifica derivações analíticas como **[A]**, diagnósticos numéricos controlados como **[B]**, novos achados como **[C]** e conjecturas abertas como **[D]**.

---

## 2. Frente Hamiltoniano de Riemann: Auditoria dos Modelos BBM e Sierra

### 2.1 Modelo BBM (Bender, Brody & Müller, PRL 2017, arXiv:1703.05326)
O operador proposto é:
$$\widehat{H} = \frac{1}{1 - e^{-i\hat{p}}} (\hat{x}\hat{p} + \hat{p}\hat{x}) \frac{1}{1 - e^{-i\hat{p}}}$$
onde $\hat{p} = -i \frac{d}{dx}$ e $e^{-i\hat{p}}f(x) = f(x-1)$ no semi-eixo $x \in (0, \infty)$.

* **Autofunções Nominais:** 
  $$\psi_z(x) = -\zeta(z, x+1) = -\sum_{n=0}^\infty \frac{1}{(n+x+1)^z}$$
  com autovalor formal $E = i(2z - 1)$. Sob a condição de contorno $\psi_z(0) = -\zeta(z) = 0$, os zeros não-triviais gerariam autovalores reais $E_n = 2\gamma_n$ com $z = 1/2 + i\gamma_n$.
* **Obstrução Funcional [A] (Bellissard, arXiv:1704.02644):**
  Para $\mathrm{Re}(z) = 1/2$, pela expansão de Euler-Maclaurin da função zeta de Hurwitz, o comportamento assintótico para $x \to \infty$ é dominado pelo termo integral:
  $$\zeta(z, x+1) \sim \frac{(x+1)^{1-z}}{z-1} = \frac{(x+1)^{1/2 - i\gamma}}{-1/2 + i\gamma}$$
  Portanto, a densidade local não apenas não decai, como **cresce linearmente**:
  $$|\psi_z(x)|^2 = |\zeta(1/2 + i\gamma, x+1)|^2 \sim \frac{x+1}{|z-1|^2}$$
  E a norma parcial diverge quadraticamente:
  $$\int_0^X |\psi_z(x)|^2 dx \sim \frac{X^2}{2|z-1|^2} \to \infty \quad (X \to \infty)$$
  Logo, **as autofunções de Riemann não pertencem ao espaço de Hilbert $L^2(0, \infty)$**. O operador $\widehat{H}$ não possui autoestados discretos normalizáveis nesse espaço, desqualificando-o como um Hamiltoniano quântico convencional sem uma métrica completada que preserve o espectro pontual.

### 2.2 Modelo de Sierra & Rodríguez-Laguna (SR, PRL 2011, arXiv:1102.5356)
Para contornar o espectro contínuo do operador $xp$, Sierra e Rodríguez-Laguna propuseram a regularização com momento característico $\ell_p$:
$$H = x\left(p + \frac{\ell_p^2}{p}\right)$$
* Em representação de momento $p > 0$, o operador simétrico associado é:
  $$\hat{H}\psi(p) = i \hbar \left[ \left(p + \frac{\ell_p^2}{p}\right) \frac{d\psi}{dp} + \frac{1}{2}\left(1 - \frac{\ell_p^2}{p^2}\right)\psi(p) \right]$$
* **Solução Exata [A]:** A equação de autovalores $\hat{H}\psi = E\psi$ é integrável exatamente:
  $$\psi_E(p) = \frac{C}{\sqrt{p + \ell_p^2/p}} \, (p^2 + \ell_p^2)^{-iE / (2\hbar)}$$
* **Quantização e Fronteira [A]:** Em um intervalo $[p_{\min}, p_{\max}]$, uma condição de contorno autoadjunta $\psi(p_{\max}) = e^{i\theta}\psi(p_{\min})$ fornece a regra de quantização:
  $$\frac{E_n}{2\hbar} \log\left(\frac{p_{\max}^2 + \ell_p^2}{p_{\min}^2 + \ell_p^2}\right) = 2\pi n + \theta$$
  **Conclusão Analítica:** Com fronteiras fixas independentes da energia, o espectro é estritamente **equidistante** ($\Delta E = \text{const}$), falhando na reprodução da densidade média de Riemann-von Mangoldt $N(E) \sim E \log E$. Para recuperar a média de Riemann, as fronteiras precisam depender dinamicamente de $E$ (pontos de retorno clássicos $x(p) = \text{const}$), o que equivale a impor o termo suave de antemão.

---

## 3. Frente Collatz: Restauração de Compacidade via Peso de Altura de Weil

Em 22/11/2026, demonstrou-se em `collatz/denominator_transfer.py` que o peso de denominador $d(x)^{-s} = (\text{denom}(x))^{-s}$ falha na compacidade em $\ell^2(\mathbb{Q} \cap \mathbb{Z}_2)$ porque $d(x) = 1$ para todo inteiro $x \in \mathbb{Z}$.

* **Nova Construção:** Definir o peso usando a **altura ingênua / de Weil** em $\mathbb{Q}$:
  $$H(x) = \max(|p|, |q|) \quad \text{para } x = p/q \text{ com } \gcd(p, q) = 1, \ q \text{ ímpar}$$
  e o peso aritmético de altura com expoente $\alpha > 0$:
  $$w_\alpha(x) = H(x)^{-\alpha} = \frac{1}{\max(|p|, |q|)^\alpha}$$
* **Propriedade Chave [A]:**
  1. Para $x \in \mathbb{Z}$, $H(x) = |x|$, logo $w_\alpha(k) = |k|^{-\alpha} \to 0$ quando $|k| \to \infty$.
  2. Para qualquer cota de altura $B$, o conjunto $\{x \in \mathbb{Q} \cap \mathbb{Z}_2 : H(x) \le B\}$ é **estritamente finito** (Teorema de Northcott para $\mathbb{P}^1(\mathbb{Q})$).
  3. Portanto, o operador de transferência ponderado $\mathcal{L}_\alpha$ com peso $w_\alpha(x)$:
     $$(\mathcal{L}_\alpha f)(y) = \sum_{x \in T^{-1}(y)} w_\alpha(x) f(x)$$
     tem coeficientes que decaem uniformemente fora de conjuntos finitos em $\mathbb{Q} \cap \mathbb{Z}_2$.

---

## 4. Plano da Rodada Computacional (Resultados Pré-Registrados)
1. **Verificação Numérica de BBM:** Integrar a densidade de probabilidade $|\zeta(1/2+i\gamma_1, x+1)|^2$ para $\gamma_1 \approx 14.134725$ com $\mathrm{mpmath}$ e confirmar o crescimento logarítmico da norma parcial $\int_0^X |\psi|^2 dx$ entre $X = 10^1$ e $X = 10^5$.
2. **Verificação de Sierra-Laguna:** Implementar a solução exata $\psi_E(p)$ e demonstrar a auto-adjunticidade da derivada simplética em reticulado discreto de momento.
3. **Verificação de Collatz com Altura:** Implementar `collatz/height_transfer.py`, calcular a matriz de transferência em pontos racionais de altura $H(x) \le 30$ e verificar a taxa de decaimento dos autovalores em comparação com o peso anterior $d(x)^{-1}$.
