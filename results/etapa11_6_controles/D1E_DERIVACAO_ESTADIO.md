# D1-E — derivação da linha "bouncing ball" para o `ctrl-estadio-v1` (19/09/2026)

Escrita **antes** de qualquer código do instrumento para bilhares e de qualquer nível calculado para o instrumento. O
único nível existente é o do teste de funcionamento de k = 100 (§14 das pendências de fontes), que não é usado aqui.
SHA-256 em `D1E_DERIVACAO_ESTADIO.sha256`. Cumpre o item D1-E da §3 de [DECLARACAO_ESTADIO.md](DECLARACAO_ESTADIO.md)
(SHA-256 `c7ce5d5b…`). Verificações numéricas (classe B) em `estadio/d1e_verificacoes.py` e `estadio/d1e_verificacoes.json`
(script `b7a4a60a…`).

**Fontes lidas:**
- Tanner, arXiv:chao-dyn/9610013v1, §2, eqs. (3)–(8), PDF pp. 3–4, que segue Sieber et al. 1993 (não lido);
- Bäcker, arXiv:nlin/0204061v1, eqs. (49)–(53), pp. 22–23;
- código congelado `riemann_spectra.arithmetic.targeted_joint_fit`, cuja docstring e código fixam o modelo "linhas de
  densidade Re[C_k e^{iET_k}]" e, "para uma linha real c cos(ET), C = c".

**Notação:** quarto de estádio com retângulo de comprimento a = 1 e raio b = 1; k = √E; setor ímpar-ímpar.

## 1. Convenção do instrumento (o que se mede)

Pelo código congelado, o ajuste com conjugado (`band`, `include_conjugate = true`) mede, para cada período T do
catálogo, o coeficiente complexo C do modelo de densidade Re[C e^{ikT}], que tem transformada

F(t) ≈ (C/2) e^{iE_cT} W(t − T) + (C̄/2) e^{−iE_cT} W(t + T).

Este é o modelo da §2.2(b) de [ETAPA11_3B_FORMULA_EXPLICITA.md](../../docs/ETAPA11_3B_FORMULA_EXPLICITA.md), com k no
lugar de E (P3 da declaração). Para ζ, C = c(n) é real. Aqui **C é complexo**, porque a linha tem fase própria.

## 2. Contribuição bouncing ball, forma exata no modelo da família

**(i) Soma de Poisson.** Seja f(x) = √(E − π²x²) para |x| < √E/π, com R = √E/π. Então
∫_{−R}^{R} √(E − π²x²) e^{2πimx} dx = (√E/2m) J₁(2m√E) para m ≠ 0, e = E/2 para m = 0 (integral clássica de
∫√(R² − x²)e^{iωx}dx = πR J₁(ωR)/ω). Pela fórmula de Poisson, Σ_{n≥1} f(n) = E/4 + (k/2)Σ_{m≥1} J₁(2mk)/m − k/2. A
eq. (52) de Bäcker, com a caixa de comprimento b = 1, fica

N_fl^bb(k) = (a/π)Σ_{n≥1} √(k² − π²n²) Θ(k − πn) − (a/4π)k² + (a/2π)k = **(ak/2π) Σ_{m≥1} J₁(2bmk)/m**,

que é a parte imaginária de Tanner, eq. (4) (N = −(1/π) Im Ig, com o termo −i(ak/2)Σ H₁⁽¹⁾(2kbn)/n). As duas fontes
**coincidem exatamente**, e não só na forma assintótica.
- **Verificação (B):** em k = 20,3; 85,47; 150; 223,53; 304,05, a diferença entre a soma finita de Bäcker e a série de
  Bessel truncada em m ≤ 2·10⁶ fica ≤ 4·10⁻¹⁰, que é a ordem da cauda truncada.

**(ii) Densidade.** Como d/dx[xJ₁(x)] = xJ₀(x), com x = 2bmk:

d_bb(k) = dN_fl^bb/dk = **(abk/π) Σ_{m≥1} J₀(2bmk)**.

A repetição m produz uma linha em t = L_m = 2bm = 2m.

**(iii) Linha m = 1 como Re[C(k)e^{ikT}], com T = 2b = 2.** Como J₀ = Re H₀⁽¹⁾ para argumento real:

d₁(k) = Re[C(k) e^{2ibk}], **C(k) = (abk/π) H₀⁽¹⁾(2bk) e^{−2ibk}**
     = (a√b/π^{3/2}) √k e^{−iπ/4} [1 − i/(16bk) + O(k⁻²)].

- **Módulo:** cresce como √k.
- **Fase:** −π/4. Vem da fase −3π/4 de Tanner (5) mais π/2 da derivada.
- **Verificação (B):** |C_exato/C_assint − 1| = 7,3·10⁻⁴ (k = 85,5); 4,9·10⁻⁴ (127,4); 2,1·10⁻⁴ (304,1).
- **A repetição m = 2 (T = 4)** tem C₂(k) = C(k)/√2 na ordem dominante (J₀(4k)). Ela coincide com a órbita de fronteira
  de comprimento 4 e fica só descritiva, pela declaração (P1).

**(iv) Condições de contorno (inferência registrada).** O termo −2ak/4π de Tanner (8) e a fase −3π/4 correspondem a
Dirichlet nas duas paredes paralelas do retângulo (y = 0, que é o eixo de simetria, e y = b). É o setor ímpar-ímpar. O
texto de Tanner não escreve as condições; isso fica como **inferência**, não como citação.

**(v) Escopo.** A fórmula vale só para a família e é **assintótica** em relação ao espectro exato. Tanner, §2: "The
bouncing ball part does, however, not contribute to individual eigenvalues"; §§3–4 tratam das órbitas instáveis
próximas da família, que Gutzwiller não descreve. Por isso a tolerância de E-C2bb (10%) continua sendo **convenção a
priori** (declaração, §5), e esta derivação não a transforma em cota.

## 3. O valor que o instrumento deve medir (C̄_bb)

C(k) varia no bloco, e o estimador ajusta um C constante. **Definição operacional, fixada agora:**

**C̄_bb(bloco) := o coeficiente da linha T = 2 que o próprio estimador congelado** (`targeted_joint_fit`, Hann,
`band`, `include_conjugate = true`, `half_width = ½·FWHM`, 9 pontos por linha, **mesmo catálogo** da execução real)
**devolve quando aplicado ao sinal analítico**

F_bb(t) = ∫_A^B w(k) e^{−i(k−E_c)t} d_bb(k) dk,

com A, B e E_c do bloco real, obtidos dos níveis na hora da avaliação, e d_bb com m ≤ 10.

Nesta definição, a variação de C(k) no bloco e o efeito do ajuste conjunto entram exatamente como entram nos dados, sem
aproximação adicional.

**Valores nos blocos nominais da declaração** (bordas de N̄₀; catálogo provisório {2, 4}; os valores oficiais são
recalculados com o catálogo O1 ∪ {2m} e as bordas reais):

| Bloco | A | B | FWHM | C̄_bb | \|C̄_bb\| | arg/π | média de C(k) ponderada pela janela | diferença relativa |
|---|---|---|---|---|---|---|---|---|
| g01 | 85,47 | 169,36 | 0,150 | 1,4308 − 1,4323i | 2,0245 | −0,25016 | 1,4301 − 1,4315i | 5,0·10⁻⁴ |
| g02 | 169,36 | 223,53 | 0,232 | 1,7789 − 1,7800i | 2,5165 | −0,25010 | 1,7787 − 1,7798i | 8,6·10⁻⁵ |
| g03 | 223,53 | 266,86 | 0,290 | 1,9878 − 1,9888i | 2,8119 | −0,25008 | 1,9877 − 1,9887i | 3,6·10⁻⁵ |
| g04 | 266,86 | 304,05 | 0,338 | 2,1449 − 2,1459i | 3,0341 | −0,25007 | 2,1449 − 2,1458i | 1,9·10⁻⁵ |

**Leitura:**
- O estimador recupera a média de C(k) ponderada pela janela com erro ≤ 5·10⁻⁴, desprezível diante da tolerância de 10%.
- A fase é −π/4 em todos os blocos.
- **Consequência para E-C2bb:** a razão complexa Ĉ/C̄_bb deve ficar a até 0,10 de 1, com o módulo e a fase de C̄_bb acima
  (ordem de 2,0 a 3,0, fase −π/4), recalculados pela definição desta seção.

**Ordem de grandeza (informativa, não é critério).** A densidade média no bloco é d̄ ≈ A_q k/2π ≈ 36 (g01) a 81 (g04),
com A_q = 1 + π/4. A linha tem |C| ≈ 2–3, ou 3,5–5,5% da densidade. Para ζ em m4-v3 (E ≈ 6–7,5·10⁴), |c(2)| ≈ 0,156 contra
d̄ ≈ 1,46 (≈ 11%).

## 4. Conclusão

- **P1 da declaração confirmada**, com a forma exata (Bessel) no lugar da assintótica. A divergência "2an√E" do texto
  extraído da eq. (53) de Bäcker não afeta nada: com a = b = 1 a fase é 2k nos dois casos, e a forma geral correta usa b.
- **P3 inalterada:** o termo médio de Tanner (8) está contido no termo de Weyl, sem dupla contagem.
- **Nenhum adendo à declaração é necessário.** O que esta derivação acrescenta é a **definição operacional de C̄_bb**
  (§3), que completa o critério E-C2bb.
