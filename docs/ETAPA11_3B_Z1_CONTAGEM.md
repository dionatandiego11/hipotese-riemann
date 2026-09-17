# Etapa 11.3b — Z1 e cota explícita de contagem de zeros (F8; uso de F3)

**Data:** 14/09/2026. **Estado:** derivação escrita; 11.3b continua `em execução`; H1 aberta; F1, F2, F4–F7 continuam
`bloqueado`.

**Objetivo.** Estabelecer, sem RH:
- uma cota explícita N(T) = O(T log T);
- em consequência, **Z1**: Σ_ρ 1/(1 + (Im ρ)²) < ∞.

Esta rota substitui a inferência a partir da apresentação do produto de Hadamard (DLMF 25.2.12), cujo modo de
convergência não está explicitado na fonte. A mesma cota atende o uso de F3 em R_longe e E_z2 (N(T) ≤ T² para
T ≥ 7·10⁴).

**Fontes:**
- DLMF §25.2 arquivada (`dlmf_25.2.html`, versão 1.2.7, SHA-256 `0de3ae2a…`):
  - eq. 25.2.1: ζ(s) = Σ n^{−s}, para ℜs > 1;
  - eq. 25.2.10 (Euler–Maclaurin, fonte Apostol 1976):
    ζ(s) = 1/(s−1) + ½ + Σ_{k=1}^{n} C(s+2k−2, 2k−1)·B_{2k}/(2k) − C(s+2n, 2n+1)∫₁^∞ B̃_{2n+1}(x) x^{−s−2n−1} dx,
    para ℜs > −2n, onde C(·,·) é o coeficiente binomial e B̃ a função de Bernoulli periódica.
- **Fórmula de Jensen:** teorema clássico de análise complexa, **sem fonte arquivada** (pendência **bibliográfica** J1;
  por exemplo Ahlfors, *Complex Analysis*, §5.3). Forma usada: se f é holomorfa em |s − s₀| ≤ R, f(s₀) ≠ 0, e n(r)
  conta os zeros com multiplicidade em |s − s₀| ≤ r < R, então

  n(r) log(R/r) ≤ log(M_R / |f(s₀)|), com M_R = max_{|s−s₀|=R} |f(s)|.

- **Constantes:** `results/etapa11_3b/zero_count_bound.py`/`.json`, em aritmética intervalar, sem dados de zeros. Os extremos
  são exportados como intervalos em string e como decimais arredondados **para fora** (`interval_export.py`), não como
  `float`.

---

## 1. Ingredientes elementares

- **(E1)** |ζ(2 + it)| ≥ 1/4 para todo t real. Por 25.2.1, |ζ(2+it)| ≥ 1 − Σ_{n≥2} n^{−2}, e
  Σ_{n≥2} n^{−2} ≤ ¼ + Σ_{n≥3} 1/(n(n−1)) = ¼ + ½.
- **(E2)** sup |B̃₃| = √3/36. B₃(x) = x(x − ½)(x − 1); em x = ½ − 1/(2√3), o valor é (1/(2√3))(¼ − 1/12) = √3/36, e há
  simetria. Para B̃₅ usa-se só a cota grosseira pelos coeficientes: |B₅| ≤ 1 + 5/2 + 5/3 + 1/6.
- **(E3)** Por 25.2.10 com n = 1, para σ = ℜs ≥ −1 (e σ > −2):
  |ζ(s)| ≤ 1/|s−1| + ½ + |s|/12 + |s+2||s+1||s|/6 · (√3/36)/(σ + 2),
  pois |∫₁^∞ B̃₃ x^{−s−3}dx| ≤ (√3/36)∫₁^∞ x^{−σ−3}dx = (√3/36)/(σ + 2).

## 2. Contagem em janelas de altura 2, para T ≥ 5

- **Disco:** centro s₀ = 2 + iT, R = 3, r = 9/4.
  - Cobertura: o retângulo [0, 1] × [T − 1, T + 1] está em |s − s₀| ≤ r, pois a maior distância é √5 < 9/4.
  - Holomorfia: ζ é holomorfa no disco fechado, porque |s₀ − 1| = √(1 + T²) > 3.
  - Validade de (E3): o disco fica em σ ≥ −1.
- **Cota de M_R:** no círculo, |s| ≤ √(4 + T²) + 3 ≤ T + 5 e |s − 1| ≥ √(1 + T²) − 3 ≥ √26 − 3, com σ + 2 ≥ 1. Por (E3):
  4M_R ≤ 4[1/(√26 − 3) + ½ + (T+5)/12 + (√3/216)(T+7)(T+6)(T+5)] ≤ 3,91 + (T+5)/3 + 0,0321(T+8)³ ≤ (T+8)³.
  - A última desigualdade vale para todo T ≥ 5: em T = 5 o lado esquerdo é ≤ 78 e o direito é 2.197, e a diferença
    (1 − 0,0321)(T+8)³ − 3,91 − (T+5)/3 é crescente.
- **Jensen, com (E1):**
  N(T + 1) − N(T − 1) ≤ log(4M_R)/log(4/3) ≤ 3 log(T + 8)/log(4/3) ≤ **10,5 log(T + 8)**,
  contando todos os zeros não triviais com multiplicidade.

## 3. Contagem inicial N(5)

- **Função e disco:** f(s) = (s − 1)ζ(s), inteira, com f(1) = 1 ≠ 0. Centro s₀ = 2 + 2,5i, R = 9/2, r = 13/4.
  - Cobertura: [0, 1] × [0, 5] está em |s − s₀| ≤ r (distância máxima √10,25 ≈ 3,20).
  - Validade: o disco fica em σ ≥ −2,5, dentro da validade de 25.2.10 com n = 2 (ℜs > −4).
- **Termos de 25.2.10 com n = 2:**
  (s−1)ζ(s) = 1 + (s−1)[½ + s/12 − (s+2)(s+1)s/720] − (s−1)·C(s+4, 5)·∫₁^∞ B̃₅ x^{−s−5}dx,
  com |∫| ≤ max|B₅|/(σ + 4) e σ + 4 ≥ 3/2.
- **Valores:** com |s| ≤ √10,25 + 4,5 e |s − 1| ≤ |s| + 1, o cálculo intervalar dá M_R ≤ 21.010. Por (E1),
  |f(s₀)| ≥ |1 + 2,5i|/4 ≥ 0,673.
- **Jensen:** N(5) ≤ log(M_R/|f(s₀)|)/log(18/13) ≤ 31,8, logo **N(5) ≤ 31**. A cota é grosseira; só sua finitude e
  explicitude importam.

## 4. Cota global e consequências

**Cota global.** Para T ≥ 5, cobrindo (5, T] pelos intervalos (3 + 2j, 5 + 2j], j = 1, …, J = ⌈(T − 5)/2⌉, com
centros T_j = 4 + 2j ≥ 6 e T_j + 8 ≤ T + 9:

N(T) ≤ 31 + J · 10,5 log(T + 9) ≤ **31 + 5,25·T·log(T + 9)** = O(T log T).

**(i) Uso de F3 em R_longe e E_z2.** Para T ≥ 7·10⁴, 31 + 5,25·T·log(T + 9) ≤ T² (conferido em intervalos no extremo,
e o lado direito cresce mais rápido). A hipótese "N(T) ≤ T² para T ≥ 7·10⁴", antes rotulada PC, fica **derivada**, e
a cota de R_longe (ETAPA11_3B_FORMULA_EXPLICITA §2.2b, T ≥ H₀ = 3·10¹²) passa a depender só de F1 (H₀) e de J1
(bibliográfica). F3 (Trudgian 2014) deixa de ser necessária para esses usos; continuaria útil só para constantes
finas de S(T).

**(ii) Z1** (rota diádica). Por simetria dos zeros, Σ_ρ 1/(1 + t²) = 2 Σ_{t_ρ>0} 1/(1 + t_ρ²).
- Zeros com t ≤ 4: cada termo ≤ 1, no máximo N(5) ≤ 31.
- Blocos 2^k < t ≤ 2^{k+1}, k ≥ 2: cada termo ≤ 1/(1 + 2^{2k}), e o número de zeros é ≤ N(2^{k+1}). Então

  Σ_{t>4} 1/(1 + t²) ≤ Σ_{k≥2} [31 + 5,25·2^{k+1}log(2^{k+1} + 9)] / 2^{2k} = O(Σ_k k 2^{−k}) < ∞.

- **Certificado intervalar** (revisão 11.3b-6): soma explícita para 2 ≤ k ≤ 259 e cota **analítica** da cauda k ≥ 260
  incluída no intervalo.
  - Termo a termo, termo_k ≤ 31·4^{−k} + 10,5·log 2·(k + 2)·2^{−k}, porque log(2^{k+1} + 9) ≤ (k + 2)log 2 para k ≥ 3.
  - Somas geométricas: Σ_{k≥K} 4^{−k} = (4/3)4^{−K} e Σ_{k≥K}(k + 2)2^{−k} = 2^{−K}(2K + 6), com K = 260.
  - A cauda fica ≤ 2,07·10⁻⁷⁵.
  - Resultado: Σ_ρ 1/(1 + t²) ≤ 100,578181581049 (extremo superior arredondado para cima), logo ≤ **101**.
- **Z1 fica estabelecido**, com multiplicidade e sem RH, a partir de 25.2.1, 25.2.10, (E1)–(E3) e da fórmula de
  Jensen.

## 5. Estado

| Item | Situação |
|---|---|
| Z1 (F8) | **derivada**, com J1 como pendência bibliográfica; certificado intervalar inclui a cauda infinita |
| Admissibilidade em 𝒜 | derivação concluída a partir dos enunciados conferidos em Connes (ETAPA11_3B_ADMISSIBILIDADE) |
| L-EF1 | fechamento documental pendente de F5 e J1 |
| N(T) ≤ T² para T ≥ 7·10⁴ (uso de F3) | **derivado**, com a mesma dependência |
| Constantes | grosseiras e explícitas; não usadas para nenhuma afirmação quantitativa fina |
| H1 (L-EF2c) | aberta, sem consequência automática dos fechamentos anteriores: admissibilidade para cada ε > 0 não controla o limite ε → 0 |
