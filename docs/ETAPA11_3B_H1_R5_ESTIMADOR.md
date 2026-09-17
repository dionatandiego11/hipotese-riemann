# Etapa 11.3b / H1 — alvos quantificados, variantes de somabilidade e álgebra do estimador (R5)

**Data:** 14/09/2026 (revisão 11.3b-8 no mesmo dia). **Estado de H1:** `em execução`, aberta.
- Sem dados novos e sem cálculo numérico novo.
- Complementa [ETAPA11_3B_H1_FORMULACAO.md](ETAPA11_3B_H1_FORMULACAO.md).
- A estimativa (log A)/L de R2 continua **heurística** e não orienta a escolha de rota.

**Notação:**
- f_t = w·e_t, com e_t(E) = e^{−i(E−E_c)t};
- c(n) = −Λ(n)/(π√n);
- ℓ_n(t) = ½[e^{iE_c log n}W(t − log n) + e^{−iE_c log n}W(t + log n)];
- M_{≤U} = Σ_{log n≤U} c(n)ℓ_n;
- w_ε(n) = e^{−ε²(log n)²/2} e M_ε = Σ_{n≥2} w_ε(n)c(n)ℓ_n.

**Observável ideal:** F*(t) = Σ_{A≤γ≤B} f_t(γ) − ∫_A^B f_tθ′/π dE. Vale F_w = F* + ρ_Δ + ρ_ord (11.3b §2.2a).

---

## 1. S1 quantificado

**Enunciado S1(B).** Para todo bloco da faixa A ∈ [9,9·10³; 7,3·10⁴], L ∈ [2,0·10³; 2,6·10³], e todo U ∈ 𝒰:

sup_{t∈I} |F*(t) − M_{≤U}(t)| ≤ B(A, L, U),

com B explícita e hipóteses declaradas (incondicional, ou sob hipóteses nomeadas).

**Domínio de U:** 𝒰 = [t_max + k₀·4π/L, U_max(A, L)], com k₀ fixado antes (proposta: k₀ = 10).

**Escala de comparação.**
- m(L) = θ₀ · min_{n∈𝒦_eff} |c(n)| · L/4, onde 𝒦_eff = {n : log n ∈ I, **Λ(n) > 0**} é o catálogo efetivo de potências de
  primo. Sobre todos os inteiros com log n ∈ I, o mínimo seria 0.
- O mínimo em 𝒦_eff é |c(128)| = log 2/(π√128) ≈ 0,0195, logo min·L/4 ≈ 9,8 para L = 2,0·10³.
- **S1 útil** quando B ≤ m(L) para algum U ∈ 𝒰, com θ₀ fixado antes (proposta: θ₀ = 0,1).

**Limite:** uma cota determinística em N∞(I) **não garante C1**, que depende de σ_null e de limiares calibrados por nulos.

## 2. S3: três afirmações distintas

| Variante | Enunciado | Modo |
|---|---|---|
| S3a (corte abrupto) | lim_{U→∞} M_{≤U}(t) = F*(t), pontual ou uniforme em I | convergência da série ordenada por n |
| S3b (somabilidade gaussiana) | lim_{ε→0} M_ε(t) = F*(t), com M_ε absolutamente convergente para cada ε > 0 | somabilidade de Gauss |
| S3c (distribucional, por cortes abruptos) | ∫φ(t)M_{≤U}(t)dt → ∫φF* quando U → ∞, para φ ∈ C_c^∞(I) | convergência fraca |

A divergência de Σ|c(n)ℓ_n| só impede a majoração termo a termo; não decide qual variante vale.

### 2.1 S3b: taxa O(ε²) com constantes explícitas (derivação condicional)

**Hipóteses** (as de 11.3b §2.2(b)):
- criticidade dos zeros até H₀ = 3·10¹² (F1, `bloqueado`);
- admissibilidade de h_ε ∈ 𝒜 (Teorema 6 de Connes conferido; Z1 derivada);
- cota local de contagem derivada (ETAPA11_3B_Z1_CONTAGEM §2): N(T+1) − N(T−1) ≤ 10,5 log(T+8) para T ≥ 5;
- pendências bibliográficas F5 e J1.

**Enunciado.** Fixe o bloco, I = [0,5; 5], δ₀ = 1 e ε₀ ∈ (0, 1/10]. Existe K = K(A, L, ε₀) tal que, para todo t ∈ I e
todo 0 < ε ≤ ε₀:

|F*(t) − M_ε(t)| ≤ K ε².

K **não depende de t nem de ε**.

**Construção de K** a partir da identidade F* = M_ε + R_zeros + R_suave + R_polos + R_longe.

1. **Zeros próximos: vizinhança fixa V = [A − δ₀, B + δ₀].**
   - Para todo real x, |f_t(x) − (f_t*φ_ε)(x)| ≤ (ε²/2)·M₂*, com M₂* = 2π²/L² + 2πt_max/L + t_max². Motivo: f_t é C¹
     com f_t′ lipschitziana e o kernel é par, com segundo momento ε².
   - O número de zeros em V é N_V ≤ N(B+1) − N(A−1), finito e limitado sem a tabela por
     N(B+1) − N(A−1) ≤ ⌈(L+2)/2⌉ · 10,5 log(B + 10).
   - Contribuição: ≤ (ε²/2)·M₂*·N_V.
2. **Zeros reais fora de V, com |t_ρ| ≤ H₀.**
   - f_t = 0 ali, e |(f_t*φ_ε)(x)| ≤ L(2πε²)^{−1/2}e^{−d(x)²/(2ε²)}, com d(x) = dist(x, [A, B]) ≥ δ₀.
   - Agrupando em faixas unitárias à distância δ₀ + k (k ≥ 0) de cada lado, cada uma com ≤ 10,5 log(B + k + 10) zeros,
     ou ≤ 31 zeros perto da origem (N(5) ≤ 31):
     ≤ L(2π)^{−1/2}ε^{−1}Σ_{k≥0} 2(10,5 log(B+k+10) + 31)e^{−(δ₀+k)²/(2ε²)} ≤ K₂(A, L)·ε^{−1}e^{−δ₀²/(2ε²)}.
   - Como sup_{0<ε≤ε₀} ε^{−3}e^{−δ₀²/(2ε²)} < ∞, o termo é ≤ K₂′ε².
3. **Parte refletida** (f_t(−·)*φ_ε nos zeros positivos): ≤ L(2πε²)^{−1/2}e^{−(x+A)²/(2ε²)}, somada do mesmo modo com
   distância ≥ A. Contribuição ≤ K₃ε².
4. **R_suave:** |∫f_t(θ′*φ_ε − θ′)/π| ≤ (ε²/2)·sup_ℝ|θ‴|/π·∫|f_t| ≤ (ε²/4)L·sup_ℝ|θ‴|/π.
   - sup_ℝ|θ‴| é finito: θ′(E) = ½Re ψ(¼ + iE/2) − ½log π (derivada de DLMF 25.10.2), logo
     θ‴(E) = −⅛Re ψ″(¼ + iE/2).
   - Por DLMF 5.9.12, derivando sob a integral (convergência dominada), |ψ″(¼ + iy)| ≤ ∫₀^∞ s²e^{−s/4}/(1 − e^{−s})ds < ∞.
5. **R_polos:** ≤ 2L(2π)^{−1/2}ε^{−1}exp(−(A² − ¼)/(2ε²)) ≤ K₅ε², pelo mesmo argumento de sup.
6. **R_longe:** ≤ 4L(2π)^{−1/2}ε^{−1}(H₀+1)²exp(−((H₀−B)² − ¼)/(2ε²)) ≤ K₆ε².

**K e escopo:**
- K = ½M₂*N_V + K₂′ + K₃ + (L/4)sup|θ‴|/π + K₅ + K₆.
- Os K_i dependem só de (A, L, ε₀, δ₀, H₀), por cotas explícitas. Os valores não foram avaliados numericamente.
- **Escopo:** blocos fixos, t no compacto I.
- S3b **não** implica S1, S3a nem S3c (que é definida por cortes abruptos).

### 2.2 Relação entre amortecimento e truncamento (correção)

A expressão da revisão anterior, Σ(1 − w_ε(n))c(n)ℓ_n, **não** está legitimada por S3b: é uma série sem convergência
estabelecida e não corresponde ao truncamento finito. Foi retirada.

**Decomposição válida,** para ε > 0 e U fixos:

M_ε − M_{≤U} = Σ_{log n≤U} (w_ε(n) − 1)c(n)ℓ_n + Σ_{log n>U} w_ε(n)c(n)ℓ_n.

- A primeira soma é **finita**.
- A segunda é **absolutamente convergente**, pelo amortecimento gaussiano.

**Leitura (revisão 11.3b-9).** F* − M_{≤U} = (F* − M_ε) + (M_ε − M_{≤U}), ou seja, três termos:
1. o resto de S3b, ≤ Kε²;
2. a alteração dos pesos na soma finita, Σ_{log n≤U}(w_ε(n) − 1)c(n)ℓ_n;
3. a cauda amortecida, Σ_{log n>U}w_ε(n)c(n)ℓ_n.

S1 exige controlar **os três** simultaneamente, para alguma escolha de ε (possivelmente dependente de U, A e L).
Controlar só a cauda amortecida não basta.

## 3. R5: operador do resíduo aos coeficientes

### 3.1 Sistema linear do estimador primário

O estimador primário de m4-v3 é `targeted_fit_primary = "band_conjugate"`: `sampling = "band"`,
`include_conjugate = true` (`arithmetic.py`, `targeted_joint_fit`).

**Construção do sistema:**
- **Pontos:** t₁, …, t_J, os pontos distintos de ∪_k B_k, com 9 por banda e meia largura 0,5·FWHM.
- **Matrizes complexas:** G_{jk} = ½φ_kW(t_j − T_k) e H_{jk} = ½φ̄_kW(t_j + T_k), com φ_k = e^{iE_cT_k}.
- **Matriz real:** M = [Re(G+H), Re(i(G−H)); Im(G+H), Im(i(G−H))] ∈ ℝ^{2J×2K}.
- **Dados:** f = [Re F(t_j); Im F(t_j)].
- **Parâmetros:** θ = (x, y), com C_k = x_k + iy_k.

**Estimador:** θ̂ = M⁺f, com M⁺ a pseudoinversa de Moore–Penrose. Para M de posto coluna completo,
M⁺ = (MᵀM)⁻¹Mᵀ. **Essa forma serve à derivação**, não ao cálculo (§3.5).

**Verdade de referência:** θ* = (c, 0), com coeficientes teóricos reais.

### 3.2 Erro e decomposição do resíduo

**Erro:** ρ := f − Mθ*. Então θ̂ − θ* = M⁺ρ **exatamente** (posto coluna completo).

**Decomposição de ρ** (exata por definição):

| Parte | Definição | Natureza | Cota disponível |
|---|---|---|---|
| ρ_lin(U) | M_{≤U∖𝒦}(t_j), linhas com log n ∉ I e log n ≤ U (n ≥ 149) | contaminação por outras linhas; determinística em (L, E_c, U) | calculável; não calculada |
| ρ_trunc(U) | F*(t_j) − M_{≤U}(t_j) | erro de truncamento (núcleo de H1) | aberta |
| ρ_ord | efeito dos erros de ordenada da tabela | dados | \|ρ_ord(t)\| ≤ 3·10⁻⁹·N·(π/L + t) (precisão declarada) |
| ρ_Δ | ∫f_tΔ dE | densidade média | certificada: ≤ 3,2·10⁻⁶ (máx. nos 30 blocos) |
| ρ_num | quadratura, NUFFT e ponto flutuante | numérica | B |

ρ_lin(U) + ρ_trunc(U) = F* − M_𝒦 não depende de U.

O código registra também um diagnóstico **B** do efeito das ordenadas: `precision_perturbations = 20` perturbações de
±`declared_table_error` = 3·10⁻⁹ na estimação primária. É dado empírico, não cota.

### 3.3 Critério implementado × alvos

**O que o código mede** (`arithmetic.py`, linhas 164–169):
- `ratio_to_theory` = **Re Ĉ_k / c_k**;
- `phase_error_rad` = arg(Ĉ_k/c_k), registrada separadamente.

**C2 por bloco** (`replication.py`; `configs/m4_v3.toml`):
- **(a)** entre as linhas **elegíveis** (resolvidas e claramente detectáveis: z previsto ≥ `clear_margin` = 1,5 vezes
  o limite superior do limiar, **definido por nulos**), a fração com |Re Ĉ_k/c_k − 1| ≤ τ = 10⁻⁶ é
  ≥ `coefficient_fraction_min` = 0,95;
- **(b)** Q = média de cos(erro de fase) ≥ `q_min` = 0,9, com p_Q (Holm entre blocos) ≤ α = 0,05;
- Q é calculado com F na grade no ponto mais próximo de T_k (`phase_coherence_test`), **não** com Ĉ_k.
- **Replicação:** C2 em todos os blocos da faixa.

**Condições por linha:**

| Alvo | Condição exata (necessária e suficiente) para a linha k | Relação com o protocolo |
|---|---|---|
| **S2-ratio** (tolerância da razão implementada) | \|e_{x_k}ᵀ M⁺ ρ\| ≤ τ\|c_k\| | é a condição por linha da parte (a) de C2; não inclui elegibilidade, agregação (fração ≥ 0,95) nem a parte (b) |
| **S2-complexo** (extensão, **não** atribuída ao protocolo) | \|(e_{x_k} + ie_{y_k})ᵀ M⁺ ρ\| ≤ τ\|c_k\| | controla o erro complexo \|Ĉ_k − c_k\|; é **mais forte** que S2-ratio |

**Observações sobre as condições:**
- **Funcionais lineares.** As duas condições são funcionais lineares de ρ. Componentes de ρ ortogonais a im M não afetam
  θ̂.
- **Condição suficiente** para S2-ratio: ‖e_{x_k}ᵀM⁺‖₁·max_j|ρ_j| ≤ τ|c_k| (ou a versão em ℓ²). Suficiente, não
  necessária.
- **C2 completo** exigiria ainda:
  - a regra de elegibilidade, que depende de nulos e de limiares;
  - a agregação por fração;
  - o critério de fase Q, que usa F na grade e é outro funcional.

  **Nenhuma condição por linha representa C2 inteiro.**
- **Escala de S2 (registro histórico; substituída em §3.6).** A cifra 10⁻⁵–10⁻⁴ (unidades de F) de
  ETAPA11_3B_H1_FORMULACAO §5 era **provisória**, porque dependia de ‖e_{x_k}ᵀM⁺‖, do condicionamento e do acoplamento
  entre linhas, então não calculados. **Não deve ser citada como exigência:** a escala calculada é 5,5·10⁻⁶ a 1,2·10⁻⁴
  (B, §3.6), e continua sendo escala de condição suficiente.
- **Erro de ordenadas.** A cota de ρ_ord em sup (≤ 4,5·10⁻⁵ no d01, t = 5) é da ordem da escala (provisória na época;
  ver a leitura atualizada em §3.6, onde ela excede a escala suficiente das linhas de menor |c_k|). A condição
  suficiente em ℓ∞ poderia falhar só por esse termo, sem implicar falha da condição exata. **Não é afirmado.**

### 3.4 Alvo projetado para o truncamento

**S2-ratio′:** |e_{x_k}ᵀ M⁺ ρ_trunc(U)| ≤ B_k(A, L, U), com B_k explícita e U finito declarado. Separa o que é analítico
(ρ_trunc) do determinístico (ρ_lin) e dos dados (ρ_ord, ρ_Δ, ρ_num).

A versão complexa (S2-complexo′) é extensão nomeada, não atribuída ao protocolo.

### 3.5 Cálculo futuro (não executado)

- **Pseudoinversa:** calcular M⁺ por **SVD** (ou QR com pivoteamento), com posto e tolerância explícitos (por exemplo,
  valores singulares abaixo de max(2J, 2K)·σ_max·ε_mach declarados nulos e relatados). Registrar σ_min, σ_max e o
  condicionamento. **Não** usar as equações normais (MᵀM)⁻¹Mᵀ para calcular.
- **S2-ratio:** a linha relevante é e_{x_k}ᵀM⁺.
- **S2-complexo:** combinar explicitamente as linhas e_{x_k}ᵀM⁺ e e_{y_k}ᵀM⁺ no vetor complexo antes de aplicar cotas de
  norma.
- **Contaminação:** e_{x_k}ᵀM⁺ρ_lin(U) para um **U finito declarado** antes do cálculo.
- **Dados:** nenhum dado de zeros entra nesses cálculos; só (L, E_c, 𝒦, pontos de banda, U).

## 3.6 Resultado do cálculo finito (classe B; revisão 11.3b-9)

- **Declaração prévia:** `results/etapa11_r5/DECLARACAO.md`, gravada às 10:15:39 de 14/09/2026, SHA-256 `e8d681cb…`.
  O script verifica o hash antes de executar.
- **Script e saída:** `results/etapa11_r5/r5_calculo.py` e `r5_resultados.json`.
- **Entradas:** nenhum dado de zeros; A, B, L, E_c dos 30 blocos, catálogo (K = 47) e U ∈ {5,5; 6; 7; 8; 10}.
- **Ponto flutuante:** dupla precisão, SVD via LAPACK. **Nenhuma cota certificada.**

**Estimador:**

| Quantidade | Resultado (30 blocos) |
|---|---|
| Dimensão de M | 846 × 94 (J = 423 pontos) |
| Posto (tol = max(2J, 2K)·σ₁·ε_mach) | completo (94) em todos |
| Condicionamento σ₁/σ_min | 1,001 a 1,025 |
| Exatidão max\|M⁺Mθ* − θ*\| | ≤ 1,9·10⁻¹⁵ |
| ‖e_{x_k}ᵀM⁺‖₁ (S2-ratio) | 1,95·10⁻³ a 3,54·10⁻³ |
| ‖e_{x_k}ᵀM⁺‖₂ | 6,6·10⁻⁴ a 8,3·10⁻⁴ |
| ℓ₁ da linha complexa combinada (S2-complexo) | 3,9·10⁻³ a 5,1·10⁻³ |
| Escala da condição suficiente ℓ∞ de S2-ratio, τ\|c_k\|/‖e_{x_k}ᵀM⁺‖₁ | 5,5·10⁻⁶ a 1,2·10⁻⁴ (unidades de F) |

**Leitura do estimador:**
- O sistema é quase ortogonal, porque as bandas das 47 linhas não se sobrepõem em unidades de FWHM.
- A escala provisória 10⁻⁵–10⁻⁴ de ETAPA11_3B_H1_FORMULACAO §5 fica **substituída** por 5,5·10⁻⁶ a 1,2·10⁻⁴ (B),
  que continua sendo escala de condição **suficiente**, não necessária.
- A cota disponível do erro de ordenadas em sup (≤ 4,5·10⁻⁵ no d01, t = 5) excede a escala suficiente das linhas de
  menor |c_k|. A condição suficiente em ℓ∞ não pode ser verificada só com essa cota. **Não** se conclui nada sobre a
  condição exata.

**Contaminação projetada** ε_k^{lin}(U)/|c_k| (S2-ratio):

| U | linhas extra (5 < log n ≤ U) | max_k \|ε_k^{lin}\|/\|c_k\| sobre blocos | linha do máximo | blocos com alguma linha > τ | max \|ε_k\|/\|c_k\| complexo |
|---|---|---|---|---|---|
| 5,5 | 21 | 2,80·10⁻⁶ | (2, 7) | 14 | 2,99·10⁻⁶ |
| 6 | 51 | 2,78·10⁻⁶ | (2, 7) | 14 | 2,96·10⁻⁶ |
| 7 | 162 | 2,77·10⁻⁶ | (2, 7) | 14 | 2,96·10⁻⁶ |
| 8 | 418 | 2,77·10⁻⁶ | (2, 7) | 14 | 2,96·10⁻⁶ |
| 10 | 2.485 | 2,77·10⁻⁶ | (2, 7) | 14 | 2,96·10⁻⁶ |

**Distribuição por bloco (U = 6):**
- o máximo por bloco varia de 6·10⁻⁸ (b04) a 2,77·10⁻⁶ (d10);
- as linhas de máximo são sempre de T próximo de t_max = 5 ou de |c| pequeno: (2, 7) com T = 4,85, 139, 137 e, em b04,
  (5, 3);
- os blocos com alguma linha acima de τ são b08, c04, c05, c07, c08, c09, c10, d01, d02, d03, d04, d05, d09 e d10.

**Leitura da contaminação** (descritiva; sem veredito sobre C2):
1. A contaminação é dominada pelas linhas logo acima de t_max (5 < log n ≤ 5,5). Aumentar U de 5,5 para 10 muda o
   máximo em cerca de 1%.
2. **ε^{lin}(U) é só uma parte de uma divisão artificial.** Como ρ_lin(U) + ρ_trunc(U) = F* − M_𝒦 não depende de U, o
   erro de truncamento total do estimador é ε^{lin}(U) + ε^{trunc}(U), e ele não foi calculado (é o núcleo de H1). Uma
   contaminação acima de τ **não** implica erro total acima de τ. Se houver compensação entre as duas partes, ela é
   questão aberta.
3. **O cruzamento com a elegibilidade de C2 não foi declarado e não foi feito:** quais dessas linhas eram elegíveis
   (resolvidas e claramente detectáveis) em cada bloco, e qual razão foi registrada para elas. Se for feito, deve ser
   declarado antes, como análise descritiva de resultados já existentes, sem alterar conclusões de m4.
4. Nada aqui altera C1, C2 ou C3 de m4. O cálculo avalia sensibilidade e contaminação do estimador; não demonstra
   controle do truncamento.

## 3.7 Cruzamento descritivo com C2 (exploratório, classe B; revisão 11.3b-10)

**Registro:**
- **Declaração prévia:** `results/etapa11_r5/DECLARACAO_CRUZAMENTO.md`, gravada às 10:20:48 de 14/09/2026, SHA-256
  `c8580015…`. O script verifica as duas declarações.
- **Saídas:** `cruzamento.py`, `cruzamento_tabela.csv` (1.410 pares bloco × linha) e `cruzamento_resumo.json`.
- **Fontes:** `arithmetic_matches.csv` e `metrics.json` dos runs primários de m4 (somente leitura).
- **Escopo:** sem testes de significância, sem alteração de critérios, sem reclassificação de conclusões.

**Grandezas por par:**
- **elegibilidade** (resolvida e claramente detectável) e **margem** = z_previsto/(1,5·z_high);
- **erro registrado com sinal** e_rec = Re Ĉ_k/c_k − 1 (estimador primário);
- **contaminação projetada com sinal** e_lin(U) = e_{x_k}ᵀM⁺ρ_lin(U)/c_k;
- **resíduo após subtração da contaminação calculada** d(U) = e_rec − e_lin(U);
- **escala suficiente** τ|c_k|/‖e_{x_k}ᵀM⁺‖₁ e τ = 10⁻⁶.

**Linhas elegíveis** (461 pares, 30 blocos):

| U | max\|e_rec\| | mediana \|e_rec\| | max\|e_lin(U)\| | mediana \|e_lin(U)\| | max\|d(U)\| | pares com \|e_lin\| > τ | pares com \|d\| > τ |
|---|---|---|---|---|---|---|---|
| 5,5 | 2,60·10⁻⁹ | 2,9·10⁻¹⁰ | 7,3·10⁻¹⁰ | 3,5·10⁻¹¹ | 2,41·10⁻⁹ | 0 | 0 |
| 6 | idem | idem | 9,4·10⁻¹⁰ | 4,2·10⁻¹¹ | 2,51·10⁻⁹ | 0 | 0 |
| 7 | idem | idem | 1,00·10⁻⁹ | 4,0·10⁻¹¹ | 2,55·10⁻⁹ | 0 | 0 |
| 8 | idem | idem | 9,8·10⁻¹⁰ | 4,0·10⁻¹¹ | 2,57·10⁻⁹ | 0 | 0 |
| 10 | idem | idem | 9,8·10⁻¹⁰ | 4,2·10⁻¹¹ | 2,56·10⁻⁹ | 0 | 0 |

**Linhas não elegíveis** (949 pares, 30 blocos; \|e_rec\| > τ em 20 pares):

| U | max\|e_lin(U)\| | mediana \|e_lin(U)\| | pares com \|e_lin\| > τ | max\|d(U)\| | mediana \|d(U)\| | pares com \|d\| > τ | sinais iguais de e_rec e e_lin (\|e_lin\| > 10⁻⁹) |
|---|---|---|---|---|---|---|---|
| 5,5 | 2,80·10⁻⁶ | 1,7·10⁻⁹ | 20 | 5,3·10⁻⁸ | 1,0·10⁻⁹ | 0 | 524/542 |
| 6 | 2,77·10⁻⁶ | 1,7·10⁻⁹ | 20 | 3,1·10⁻⁸ | 9,3·10⁻¹⁰ | 0 | 535/550 |
| 7 | 2,77·10⁻⁶ | 1,7·10⁻⁹ | 20 | 3,0·10⁻⁸ | 9,3·10⁻¹⁰ | 0 | 532/548 |
| 8 | 2,77·10⁻⁶ | 1,8·10⁻⁹ | 20 | 3,0·10⁻⁸ | 9,5·10⁻¹⁰ | 0 | 534/548 |
| 10 | 2,77·10⁻⁶ | 1,7·10⁻⁹ | 20 | 2,9·10⁻⁸ | 9,3·10⁻¹⁰ | 0 | 531/545 |

**Os 20 pares com \|e_lin(6)\| > τ:**
- todos são **não elegíveis**: 2⁷ com margem 0,093–0,096 e 137/139 com margem 0,63–0,65;
- estão nos mesmos 14 blocos do cálculo anterior (b08, c04, c05, c07, c08, c09, c10, d01, d02, d03, d04, d05, d09, d10);
- em todos, e_rec também excede τ, com o mesmo sinal de e_lin;
- |d(6)| fica entre 5·10⁻¹⁰ e 1,3·10⁻⁸;
- a lista completa está em `cruzamento_resumo.json`.

**Leitura** (descritiva; limites obrigatórios):
1. **Linhas usadas em C2.** A contaminação calculada **não** atinge a escala τ nas linhas elegíveis (máx. ≈ 1·10⁻⁹), e
   o erro registrado delas fica ≤ 2,6·10⁻⁹, como já registrado em C2. Os pares com contaminação > τ são todos
   **excluídos pelo critério de elegibilidade**.
2. **Os "14 blocos acima de τ"** do cálculo anterior (§3.6) referem-se ao catálogo completo. Não são falhas de C2: C2
   avalia só as elegíveis.
3. **Nas linhas não elegíveis afetadas,** o erro registrado acompanha a contaminação calculada, com sinais iguais em
   cerca de 97% dos pares com |e_lin| > 10⁻⁹ e resíduo após subtração ≤ 1,3·10⁻⁸. Essa é uma **associação descritiva**,
   sem teste.
4. **O resíduo após subtração não é erro de truncamento.** d(U) reúne o truncamento acima de U e demais partes de
   ρ_trunc, erros das ordenadas, diferença de densidade, erros numéricos e diferenças de FWHM entre versões de código.
   Não identifica isoladamente compensação pelo truncamento nem valida S2-ratio′.
5. **Estabilidade em U.** A variação entre U = 5,5 e 10 indica estabilidade **só nesse intervalo finito**. Não controla
   a cauda acima de 10.
6. **Nada muda em m4.** C1, C2 e C3 não são alterados, e nenhum critério foi recalculado ou reinterpretado.

## 3.8 Encerramento da sequência de diagnósticos de R5 (revisão 11.3b-11)

A sequência de diagnósticos numéricos de R5 (§3.6–§3.7) fica **encerrada** com o resultado registrado. Não serão ampliados
cortes em U nem cruzamentos.

**Conclusões registradas** (classe B, descritivas):
1. O estimador primário está numericamente bem condicionado nos 30 blocos examinados (posto completo, cond ≤ 1,025).
2. A contaminação finita calculada acima de 10⁻⁶ ocorre **apenas em linhas não elegíveis**. Nas linhas de C2, ela fica
   muito abaixo da tolerância (≤ 1·10⁻⁹).
3. **Interpretação descritiva:** nas condições examinadas (U ∈ [5,5; 10]), o vazamento das linhas adicionais reproduz
   grande parte dos desvios observados nas linhas fracas (sinais iguais em ~97%; resíduo após subtração ≤ 1,3·10⁻⁸
   nos 20 pares).

**O que isso não faz:**
- não controla a cauda infinita;
- não demonstra S2-ratio′ nem S1;
- não altera C1, C2 ou C3 de m4.

**Próximo avanço relevante:** analítico. Uma cota para a projeção do truncamento (S2-ratio′) ou para S1, mantendo a
separação entre resultados empíricos (B) e demonstração.

**Ponto de partida registrado** (sem execução). Para a linha k, a projeção é o funcional a_k := e_{x_k}ᵀM⁺ aplicado
aos valores nos pontos de banda. Pela decomposição de §2.2:

a_k·(F* − M_{≤U}) = a_k·(F* − M_ε) + Σ_{log n≤U}(w_ε(n) − 1)c(n)·a_k·ℓ_n + Σ_{log n>U}w_ε(n)c(n)·a_k·ℓ_n,

com |a_k·(F* − M_ε)| ≤ ‖a_k‖₁Kε² por S3b. O segundo termo é finito e explícito. O terceiro concentra o obstáculo já
identificado: tornar Kε² pequeno exige ε pequeno, e isso torna inútil a cota absoluta da cauda amortecida. Uma
estratégia analítica precisa explorar **cancelamento** em a_k·ℓ_n ao longo de n, ou uma fonte (F9 ou F10), e não
majoração termo a termo.

## 4. Estado

| Item | Situação |
|---|---|
| S1 | quantificado (§1), com mínimo sobre 𝒦_eff (Λ(n) > 0); **aberto**; não implica C1 |
| S2-ratio | condição exata por linha = \|e_{x_k}ᵀM⁺ρ\| ≤ τ\|c_k\|; parte (a) de C2 por linha; **aberto** |
| S2-complexo | extensão nomeada, mais forte; **não** atribuída ao protocolo; **aberto** |
| S2-ratio′ | projeção do truncamento com U finito declarado; **aberto** |
| S3a, S3c | abertos (S3c definido por cortes abruptos) |
| S3b | **derivada condicionalmente** (F1; F5 e J1 bibliográficas): \|F* − M_ε\| ≤ Kε² para 0 < ε ≤ ε₀, K independente de t ∈ I e de ε; blocos fixos |
| R5 | formalizado; **cálculo finito B executado** sob declaração prévia (§3.6): posto completo, cond ≤ 1,025, normas de linha e contaminação projetada; a contaminação por linhas logo acima de t_max supera τ em 20 pares (14 blocos), **todos não elegíveis**; nas elegíveis ≤ 1·10⁻⁹ (§3.7). Não é erro total de truncamento nem falha de C2 |
| Diagnósticos numéricos de R5 | **encerrados** (§3.8) |
| H1 | **aberta**; próximo avanço analítico: cota para a projeção do truncamento (S2-ratio′) ou para S1 |
