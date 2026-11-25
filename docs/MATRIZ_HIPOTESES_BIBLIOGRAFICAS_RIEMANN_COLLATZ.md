# Matriz de Hipóteses Bibliográficas: Operadores Espectrais e Conexões Collatz–Riemann

24/11/2026. Documento consolidado de hipóteses históricas e recentes mineradas via Scientific Literature, arXiv e literatura primária, organizadas para teste sistemático no loop de verificação.

---

## Eixo 1: A Linha do Tempo dos Operadores Hamiltonianos para Riemann (Hilbert-Pólya)

### 1. Modelo Clássico $xp$ de Berry & Keating (1999)
- **Fonte Primária:** M. V. Berry, J. P. Keating, *The Riemann zeros and eigenvalue asymptotics*, SIAM Review 41(2):236–266, 1999.
- **Operador e Espaço:** $\hat{H} = \frac{1}{2}(\hat{x}\hat{p} + \hat{p}\hat{x}) = -i(x \partial_x + 1/2)$ em $L^2(\mathbb{R}^+)$.
- **Alegação Original:** A quantização semiclássica com corte de Planck reproduz a fórmula de Riemann-von Mangoldt $\bar{N}(E) \sim \frac{E}{2\pi}\log\frac{E}{2\pi} - \frac{E}{2\pi} + \frac{7}{8}$. As órbitas periódicas primitivas têm períodos $T_p = \log p$.
- **Obstrução Matemática:** O espectro é estritamente contínuo no semi-eixo real. As trajetórias clássicas são hipérboles abertas que escapam para o infinito. Não há autofunções discretas em $L^2$ sem condições de contorno não-locais.
- **Status:** **[A]** (Termo médio comprovado; espectro contínuo demonstrado).

### 2. Modelo de Absorção Não-Comutativo de Alain Connes (1998/1999)
- **Fonte Primária:** A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, arXiv:math/9811068, 1998; Selecta Math. 5:29–106, 1999.
- **Operador e Espaço:** Ação do grupo multiplicativo de adeles $\mathbb{A}_\mathbb{K}^\times$ sobre o espaço de classes de adeles $X = \mathbb{A}_\mathbb{K} / \mathbb{K}^\times$.
- **Alegação Original:** A fórmula explícita de Weil é reinterpretada como uma fórmula de traço geométrica. Os zeros de Riemann na linha crítica aparecem como um **espectro de absorção** (ausência de níveis no contínuo). Eventuais zeros fora da linha seriam ressonâncias.
- **Obstrução Matemática:** O traço de absorção possui sinal invertido em relação a um espectro quântico de emissão padrão; não fornece um operador diferencial de Schrödinger clássico autoadjunto com autovalores discretos positivos.
- **Status:** **[A]** (Geometria rigorosa; não produz operador de emissão física direto).

### 3. Modelo de Níveis de Landau de Sierra & Townsend (2008)
- **Fonte Primária:** G. Sierra, P. K. Townsend, *Landau Levels and Riemann Zeros*, arXiv:0805.4079, PRL 101:110202, 2008.
- **Operador e Espaço:** Partícula carregada em duas dimensões sob campo magnético uniforme $B$ perpendicular e potencial elétrico $V(x, y) = -E x y$.
- **Alegação Original:** No limite do menor nível de Landau (Lowest Landau Level - LLL), o sistema dinâmico se projeta exatamente no operador $H = xp$ de Berry-Keating e recupera a física do modelo de Connes.
- **Obstrução Matemática:** A discretização pontual dos zeros exige impor barreiras físicas artificiais nas bordas da amostra.
- **Status:** **[B]** (Mapeamento quântico 2D validado numericamente).

### 4. Modelo Regularizado $x(p + \ell_p^2/p)$ de Sierra & Rodríguez-Laguna (2011)
- **Fonte Primária:** G. Sierra, J. Rodríguez-Laguna, *The H=xp model revisited and the Riemann zeros*, arXiv:1102.5356, PRL 106:200201, 2011.
- **Operador e Espaço:** $H = x(p + \ell_p^2/p)$ em representação de momento $p > 0$.
- **Alegação Original:** O termo $\ell_p^2/p$ fecha as órbitas clássicas no espaço de fase, convertendo o espectro em discreto.
- **Obstrução Demonstrada no Projeto (Iteração 1 e 2):**
  1. Com fronteiras fixas, o espectro é puramente equidistante ($\Delta E = \text{const}$), falhando na densidade de Weyl.
  2. Em grade conformal, surgem 23 modos espúrios no gap infravermelho $[0, \gamma_1]$, gerando erro $\mathcal{O}(1)$ no traço de resolvente.
- **Status:** **[A / B]** (Falsificado como candidato autônomo sem potencial de confinamento).

### 5. Férmions de Dirac em Rindler de Germán Sierra (2014)
- **Fonte Primária:** G. Sierra, *The Riemann zeros as energy levels of a Dirac fermion in a potential built from the prime numbers in Rindler spacetime*, arXiv:1404.4252, J. Phys. A 47:325204, 2014.
- **Operador e Espaço:** Equação de Dirac 1+1D sem massa em coordenadas de Rindler com potenciais delta pontuais em $x = \log p$.
- **Alegação Original:** A matriz de espalhamento $S(E)$ tem polos que coincidem com os zeros de Riemann se a condição de contorno for ajustada.
- **Obstrução Matemática:** A condição de contorno de auto-adjunticidade necessita da fase $\theta(E) = \arg \zeta(1/2+iE)$, tornando o modelo dependente de informação prévia dos próprios zeros.
- **Status:** **[B]** (Ajuste tautológico de contorno).

### 6. Operador $\mathcal{PT}$-Simétrico de Bender, Brody & Müller (2017)
- **Fonte Primária:** C. M. Bender, D. C. Brody, M. P. Müller, *Hamiltonian for the Zeros of the Riemann Zeta Function*, arXiv:1703.05326, PRL 118:130201, 2017.
- **Operador:** $\widehat{H} = (1 - e^{-i\hat{p}})^{-1} (2xp) (1 - e^{-i\hat{p}})^{-1}$.
- **Alegação Original:** Autofunções formais $\psi_z(x) = -\zeta(z, x+1)$ teriam autovalores reais $E = 2\gamma$ se a simetria $\mathcal{PT}$ fosse inquebrada.
- **Obstrução Demonstrada no Projeto (Iteração 1):**
  Pela expansão de Euler-Maclaurin, $|\psi_z(x)|^2 \sim \frac{x+1}{|z-1|^2}$, logo a norma $L^2(0, \infty)$ diverge quadraticamente ($X^2$). O operador não possui autoestados discretos normalizáveis.
- **Status:** **[A / B]** (Comprovadamente falsificado em $L^2$).

### 7. Núcleos Unitários de Convolução de Weil de Suzuki (1994, 2014)
- **Fonte Primária:** M. Suzuki, *Positivity of Weil's distribution and the Riemann Hypothesis*, J. Math. Soc. Japan 66:1–37, 2014.
- **Operador e Espaço:** Núcleo de convolução de tipo positivo $K(h)$ derivado da fórmula explícita. Pelo Teorema de Stone, gera grupo unitário $U(t) = e^{iHt}$.
- **Limitação Identificada:** Vetores básicos $v_t \notin D(H)$ pela singularidade $h\log(1/h)$ na origem. O gerador $H$ tem espectro assinado sem geometria física definida.
- **Status:** **[A]** (Formalizado em `DOMINIOS_OPERADORES_20261122.md` com domínio suavizado).

---

## Eixo 2: A Linha do Tempo das Conexões Collatz–Riemann e Operadores de Transferência

### 1. Teoria de Paridade de Riho Terras (1976)
- **Fonte Primária:** R. Terras, *A stopping time problem on the positive integers*, Acta Arith. 30:241–252, 1976.
- **Contribuição:** Definição da medida de paridade e demonstração de tempo de parada quase sempre finito.
- **Status:** **[A]**.

### 2. Conjugação 2-Ádica de Bernstein & Lagarias (1996)
- **Fonte Primária:** D. J. Bernstein, J. C. Lagarias, *The 3x+1 Conjugacy Map*, Can. J. Math. 48(6):1154–1169, 1996.
- **Contribuição:** Prova de que $T$ é conjugado metricamente ao shift de Bernoulli $S$ em $\mathbb{Z}_2$: $\Phi \circ S \circ \Phi^{-1} = T$. A função zeta de pontos periódicos é $\zeta_T(z) = 1/(1-2z)$.
- **Status:** **[A]** (Controle negativo do projeto: dinâmica simbólica pura não enxerga os primos).

### 3. Programa da Densidade de Predecessores de Günther Wirsching (1998, 2003)
- **Fonte Primária:** G. J. Wirsching, *The Dynamical System Generated by the 3n+1 Function*, Springer Lecture Notes in Math. 1681, 1998.
- **Contribuição:** Formulação do operador de transferência de ramos inversos e conjectura sobre a densidade invariante $\varphi$ de base 3.
- **Status:** **[A]**.

### 4. Quase Todas as Órbitas de Terence Tao (2019)
- **Fonte Primária:** T. Tao, *Almost all orbits of the Collatz map attain almost bounded values*, arXiv:1909.03562, Forum of Math. Pi, 2022.
- **Contribuição:** Quase todas as órbitas atingem valores arbitráriamente pequenos via análise de Fourier em grupos 3-ádicos.
- **Status:** **[A]**.

### 5. Descoberta Analítica Wirsching–Tavares (2026) e Verificação no Projeto
- **Fonte Primária:** R. A. Tavares, *Wirsching's Positive-Predecessor-Density Program: Proofs of Conjectures 1 and 3*, arXiv:2608.27617, 2026.
- **A Ponte Exata Demonstrada e Verificada (Iteração 3 do Projeto):**
  O produto de dilatação de predecessores $P(s) = \sum_{i=0}^\infty \log(1 - e^{-2 \cdot 3^i s})$ possui representação de Mellin cujos polos geram coeficientes de Fourier expressos exatamente pela **função zeta de Riemann**:
  $$c_n = \frac{2^{i\tau_n}}{2\pi i n} \Gamma\left( 1 - i\frac{2\pi n}{\log 3} \right) \zeta\left( 1 - i\frac{2\pi n}{\log 3} \right)$$
  - Verificação numérica a 40 dígitos: concordância de **9 dígitos significativos** ($|c_{1, \text{num}} - c_{1, \text{theo}}| / |c_{1, \text{theo}}| \approx 1.49 \times 10^{-9}$).
- **Status:** **[A / B]** (Comprovado analítica e numericamente).

### 6. Operador de Transferência por Altura de Weil (Projeto 2026)
- **Fonte:** `collatz/height_transfer.py` e `results/loop_estudo_it2_20261124/`.
- **Contribuição:** Uso da altura de Weil $H(x) = \max(|p|, q)$ restaura a compacidade e divide o espectro em círculos concêntricos correspondentes aos ciclos periódicos com gap rigoroso $g(\alpha) = 1 - 2^{-\alpha/2}$.
- **Status:** **[A / B]**.
