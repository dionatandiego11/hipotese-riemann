# Certificação computacional da condição suficiente em (d₁, Δ) = (8, 2) — declaração prévia (15/09/2026)

Gravada **antes** de implementar e executar. SHA-256 em `DECLARACAO_CERT.sha256`.

## 0. Escolha do corte e natureza do resultado
- **Corte:** (d₁, Δ) = (8, 2), isto é, U₁ = 13 e U₂ = 15, com ε₀ = 0,1 e t_max = 5.
  - **Foi escolhido depois da avaliação exploratória** (§II.12, §II.16), como o melhor entre as 12 combinações
    declaradas. Não é um ótimo e não houve ampliação da grade.
  - Nenhum outro corte é certificado aqui.
- **Resultado pretendido:** certificação computacional, **condicional a RH** (com F5 e J1 como pendências bibliográficas),
  da desigualdade

  **(B^{RH″}_{χ,k} + S^{abs}_k)/|c_k| ≤ 10⁻⁶**, com S^{abs}_k := Σ_{13<log n≤15} χ(log n)|c(n)||Q_k(log n)| ≥ |Θ_k(U₂)|,

  para os 30 blocos × 47 linhas. Por P-RH-trunc (§II.13), isso implica |a_k·(F* − M_{≤U₂})|/|c_k| ≤ 10⁻⁶.
- **Não é:** prova de RH; certificação retrospectiva de C2; tratamento de S1, S3a, S3c; tratamento da passagem ao
  estimador registrado (ordenadas tabuladas, densidade usada, código).

## 1. Objeto matemático definido (M^math)
Por bloco, a partir dos valores registrados, tomados como números exatos (racionais binários):
- A, B, E_c de `metrics.json`;
- L := fl(B − A), a subtração em ponto flutuante, como no código;
- h := 0,5·fwhm de `measure_window_response(L)`, recalculado deterministicamente e registrado em hexadecimal.

Definições:
- **Nós:** t_i são os valores em ponto flutuante de `np.unique(concat(linspace(x − h, x + h, 9)))`, com
  x = `period_theoretical` do catálogo. São recalculados, registrados por SHA-256 dos bytes e tomados como exatos.
- **Linhas:** T_j := log n_j (reais exatos, n_j do catálogo), j = 1..47.
- **Resposta:** W é a resposta exata da Hann, W(ω) = (L/2)·sinc(v)/(1 − v²), com v = ωL/(2π) e extensão contínua.
- **Matriz:** M^math = [Re; Im] de [G + H, i(G − H)], com G_ij = ½W(t_i − T_j)e^{iE_cT_j} e
  H_ij = ½W(t_i + T_j)e^{−iE_cT_j}.
- **Estimador e frequências:** a_k := linha k (k ≤ 47) de (M^mathᵀM^math)⁻¹M^mathᵀ; ν_A := E_c − L/2 e
  ν_B := E_c + L/2 (reais exatos a partir dos registrados).

O a_k do código em ponto flutuante é **outro objeto**. A diferença é reportada só como diagnóstico.

## 2. Método rigoroso
**Base de confiança (declarada):**
- (i) aritmética IEEE-754 binary64 com arredondamento ao mais próximo para +, −, ×, ÷ no numpy (x86-64), e
  `np.nextafter`;
- (ii) correção do arredondamento dirigido de `mpmath.iv` para log, exp, sin, cos, sqrt e π;
- (iii) aritmética inteira exata do Python;
- (iv) correção do crivo, conferido por uma segunda implementação independente (crivo segmentado).

**Aritmética intervalar vetorizada (numpy lo/hi):**
- Cada ×, ÷, +, − elementar é arredondado para fora com `nextafter`.
- **Somas de m termos:** s = soma calculada; o erro fica ≤ ((1 + ε)^{m−1} − 1)(1 + ε)^{m−1}·Σ|x_i| calculada, válido
  para qualquer ordem de soma, e depois é arredondado para fora.

**Passo 1 — entradas de M^math:**
- `mpmath.iv` (30 dígitos) para sin, cos e as divisões.
- Perto de v = 0 ou v = ±1 (distância < 10⁻³), usa-se sinc(x) ∈ [1 − (πx)²/6, 1] com as fatorações
  W = (L/2)sinc(v)/(1 − v²) e W = (L/2)·sinc(v ∓ 1)/(|v|(|v| + 1)), esta com v ↦ |v|.

**Passo 2 — posto e inversa:**
- G := M^mathᵀM^math em intervalos; R := inversa em ponto flutuante do ponto médio.
- ρ := sup ‖I − R·G‖_∞ (intervalar). **Exige ρ < 1**, o que certifica G invertível e, portanto, **posto 94 = 2K**.

**Passo 3 — linhas:**
- Y := R·M^mathᵀ em intervalos; e := ρ/(1 − ρ).
- ‖a_k‖₁ ≤ ‖y_k‖₁^sup + e·max_i‖y_i‖₁^sup.
- Entrada a entrada: a_kj ∈ y_kj ± e·max_i|y_ij|^sup.

**Passo 4 — S^abs_k:**
- Para u ∈ (13, 15], por desigualdade triangular sobre a expansão de §II.2(d):
  |Q_k(u)| ≤ (L/8π)·Σ_{s∈{A,B}, ±}|P_s^±(u)|, com P_{A}^∓(u) = Σ_j ᾱ_je^{it_jL/2}R(v_j^∓(u)),
  P_{B}^∓(u) = Σ_j ᾱ_je^{−it_jL/2}R(v_j^∓(u)), R(v) = 1/(v(v² − 1)), v_j^∓ = (t_j ∓ u)L/(2π) e α_j = a^R_j + i·a^I_j.
  Vale porque |v_j^∓| ≥ λ(13 − max t_j) ≥ √2.
- **Malha:** células de largura δ = 0,005 em u. Em cada célula, sup|P| ≤ |P(u_c)|^sup + (δ/2)·λ·‖a_k‖₁^sup·12·|v_min|⁻⁴,
  com v_min := λ(u_c − δ/2 − max t_j), pois |R′(v)| ≤ 12|v|⁻⁴ para |v| ≥ √2 (Lema 1).
- **Aritmética:** P(u_c) em intervalos, com as fases e^{±it_jL/2} enclausuradas por `mpmath.iv` e α_j pelo Passo 3.
- **Soma sobre n:** S^abs_k ≤ Σ_células [sup_célula|Q_k|]·(1/π)·Σ_{n∈célula}Λ(n)n^{−1/2}, com χ ≤ 1. As somas por
  célula usam `mpmath.iv` termo a termo. Um n cuja pertença a uma célula é ambígua entra nas duas.

**Passo 5 — orçamento:**
- B^{RH″}_{χ,k} com as fórmulas de PRH3 (Lema 4′ + Lema 5′ + Arq) em `mpmath.iv`, usando a = ‖a_k‖₁^sup, ν_A, ν_B, L,
  c₁^sup e c₂^sup;
- |c_k| = Λ(n_k)/(π√n_k) com extremo inferior em `mpmath.iv`;
- total_k := (B^{RH″} + S^{abs,sup}_k)/|c_k|^inf, **exportado com arredondamento para fora**;
- **par certificado** ⇔ total_k^sup ≤ 10⁻⁶ e todos os passos do bloco aceitos (ρ < 1, |v| ≥ √2, conferência do crivo).

## 3. Diagnósticos (não entram na decisão)
- ‖a_k‖₁^sup contra a_l1 em ponto flutuante (PRH2);
- S^{abs,sup} contra S_abs em ponto flutuante (THETA);
- total_k contra orcamento2 (PRH3).

## 4. Registros
- **Por bloco:** h (hex), SHA-256 dos nós, ρ, e, max_i‖y_i‖₁ e min_j|v_j|.
- **Por par:** ‖a_k‖₁^sup, B^{RH″}/|c_k| (sup), S^{abs}/|c_k| (sup), total_k (sup) e certificado (sim/não), mais os
  diagnósticos.
- **Resumo:** número de pares certificados (todos; elegíveis, descritivo), máximo de total_k nos elegíveis e lista dos
  não certificados.

## 5. Regras de leitura
- Par certificado significa que a desigualdade vale para M^math, sob RH e a base de confiança (i)–(iv). Não certifica
  C2 retrospectivamente nem o estimador em ponto flutuante.
- Par não certificado **não** refuta a desigualdade nem S2-ratio′.
- Correções de implementação que não mudem o método são registradas como tais. Mudanças de método exigem nova declaração.

## Saídas
`cert_calculo.py`, `cert_blocos.csv`, `cert_tabela.csv`, `cert_resumo.json`.
