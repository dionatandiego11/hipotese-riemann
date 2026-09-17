# Certificação da contaminação em (5, 15) e resíduo contra o catálogo 𝒦 — declaração prévia (16/09/2026)

Gravada **antes** de qualquer implementação ou cálculo. SHA-256 em `DECLARACAO_CERT_CONTAMINACAO.sha256`.

**Relação com a execução 4:**
- **Reaproveita, sem alterar:** DECLARACAO_CERT.md (b7a7980c…) e os adendos CORRECAO1 (0a693179…), CORRECAO2 (75eee940…) e
  RECONF_C1C2 (a8253e9c…).
- **Execução 4:** congelada. `cert_calculo.py` (95bec528…) **não é modificado**; os valores B_rel_sup e Sabs_rel_sup de
  `cert_tabela.csv` são **lidos**, não recalculados.
- **Corte:** o mesmo, (d₁, Δ) = (8, 2), escolhido após a avaliação exploratória.

## 0. Objeto e identidade

**Catálogo.** 𝒦 = todas as potências de primo n ≤ 148 (47 linhas; conferido por enumeração independente). Portanto:
- n ∉ 𝒦 com Λ(n) > 0 ⇔ n ≥ 149 ⇔ log n > 5;
- a_k·ℓ_n = δ_kn para n ∈ 𝒦.

**Decomposição exata** (para 0 < ε ≤ ε₀), com T_χ(ε) := Σ_n χ(log n)w_ε(n)c(n)ℓ_n e χ ≡ 0 em (−∞, 13], χ ≡ 1 em [15, ∞):

a_k·(F* − M_𝒦) = a_k·(F* − M_ε) + (w_ε(n_k) − 1)c_k + a_k·T_χ(ε) + Σ_{5<log n<15} (1 − χ(log n)) w_ε(n) c(n) Q_k(log n).

**Limite ε → 0:**
- o primeiro termo tende a 0 (S3b);
- o segundo tende a 0;
- |a_k·T_χ(ε)| ≤ B^{RH″}_{χ,k}, uniformemente em ε (P-RH com os Lemas 4′ e 5′; condicional a RH);
- a soma final é finita e converge para a soma sem w_ε.

Logo:

|a_k·(F* − M_𝒦)| ≤ B^{RH″}_{χ,k} + Σ_{5<log n≤13} |c(n)||Q_k(log n)| + Σ_{13<log n<15} (1 − χ)|c(n)||Q_k(log n)|.

**Esta decomposição não usa Θ_k.** A cota de §II.13 (P-RH-trunc) continua válida, mas não entra aqui.

**Amarração com a execução 4 (verificada no código, não só no texto):**
- `cell_sums()` de `cert_calculo.py` soma Λ(n)/√n por célula **sem peso χ**. A declaração original registra isso como
  "com χ ≤ 1".
- O valor exportado Sabs_rel_sup é, portanto, majorante de Σ_{13<log n≤15}|c(n)||Q_k(log n)|/|c_k|, sem peso. Isso
  vale porque, célula a célula, |Q_k(log n)| ≤ sup_célula|Q_k|.
- Como 0 ≤ 1 − χ ≤ 1, **o terceiro somatório é dominado por Sabs_rel_sup**, sem cálculo novo em (13, 15).

**Quantidades novas:**
- P_k := Σ_{5<log n≤6} |c(n)||Q_k(log n)| (regime I, ponto a ponto);
- C_k := Σ_{6<log n≤13} |c(n)||Q_k(log n)| (regime II, células).

**Orçamento certificado por par:**

total_k := B_rel_sup + Sabs_rel_sup + (P_k^sup + C_k^sup)/|c_k|_inf ≤ 10⁻⁶.

## 1. Conferência das premissas da proposta (registrada antes do cálculo)

| Afirmação da proposta | Conferência (16/09/2026) |
|---|---|
| π(e¹³) = π(442.413) = 37.143 | **37.128** (crivo); floor(e¹³) = 442.413, sem ambiguidade de arredondamento |
| ~37.060 primos em (e⁶, e¹³] | **37.049 primos + 161 potências r ≥ 2** |
| π(e⁶) = π(403) = 79; 45 primos em (e⁵, e⁶] | confere |
| "4 potências" em (e⁵, e⁶]: 256, 243, 169, 289, 361 | **6 potências:** 169 = 13², 243 = 3⁵, 256 = 2⁸, 289 = 17², **343 = 7³**, 361 = 19². O regime I tem **51 termos** |
| s = u − t_max ∈ (0, 1] em (5, 6], com derivadas que "invalidariam qualquer envoltória" | t_max ≤ 4,93760 nos 30 blocos (catálogo até log n = 4,9345). No primeiro n fora do catálogo (149), **s ≥ 0,0663 e v = λs ≥ 21,23** (pior bloco m4-v3/d10). A condição \|v\| ≥ √2 do Lema 1 **vale** em (5, 6]; a envoltória por células seria válida. O regime I ponto a ponto é escolhido por **precisão** (s pequeno torna a envoltória frouxa), não por validade |
| (13, 15]: peso 1 − χ exige cobertura | coberta por Sabs_rel_sup da execução 4 (§0) |
| "Fator de segurança ~350×; fechará com ampla folga em 461/461" | **Não é premissa aceita.** O valor ≤ 1·10⁻⁹|c_k| é estimativa B da contaminação **com sinal**. P_k e C_k são somas de **módulos**, que descartam o cancelamento entre fases e^{iE_c log n}. Uma quantidade com sinal não limita a soma dos módulos. **Nenhuma expectativa de fechamento é registrada** |

## 2. Método

### 2.1 Reconstrução do estimador (Passos 1–3)

- **Implementação:** novo script `cert_contaminacao.py`, que importa `cert_calculo.py` como módulo e chama as mesmas
  primitivas: `I`, `isum`, `ivf`, `W_iv`, `matmul`, `dn`, `up`, `fin`, `lo_q`, `hi_q`, `float_up`, `PI`, `PI_INF` e o
  crivo.
- **Sem monkeypatch nem edição de `cert_calculo.py`.** Os Passos 1–3 (M^math, ρ, e, Arows por componente) são repetidos
  com essas primitivas, na mesma ordem de operações.
- **Parada obrigatória:** ρ e ‖a_k‖₁^sup de cada bloco devem coincidir **bit a bit** com `cert_blocos.csv` e
  `cert_tabela.csv` da execução 4, nos 30 blocos e nos 47 valores por bloco. Qualquer divergência interrompe a leitura
  dos resultados.

### 2.2 Regime I: (5, 6], ponto a ponto (51 termos)

- **Enumeração:** n ∈ [149, 403], com floor(e⁵) = 148 e floor(e⁶) = 403 conferidos por extremos exatos. A lista de
  potências de primo é conferida por duas implementações (crivo e divisão por tentativa).
- **Avaliação, para cada n e cada bloco, sem a forma separada de §II.2(d):**
  - u := iv.log(n);
  - ℓ_u(t_j) = ½[e^{iE_c u}W(t_j − u) + e^{−iE_c u}W(t_j + u)], com `W_iv` e cos/sin(E_c u) em `mpmath.iv`;
  - Q_k(u) = Σ_j (aR_j·Re ℓ_u(t_j) + aI_j·Im ℓ_u(t_j)), com Arows intervalar e `isum`.
- **Coeficiente:** |c(n)|^sup = extremo superior exato de log p/(π√n).
- **Soma:** P_k^sup = Σ_n |c(n)|^sup·max(|lo|, |hi|) de Q_k(log n), acumulada com `up`.

### 2.3 Regime II: (6, 13], células

- **Células:** 1.792 células de largura δ = 1/256, com bordas 6 + i/256 exatas em binário.
- **Método:** idêntico ao Passo 4 de DECLARACAO_CERT (envoltórias P de §II.2(d) no centro, mais a correção pela derivada
  do Lema 1, com v⁴ por multiplicações dirigidas).
- **Margem:** verificação exata v_min > 0 e v_min² ≥ 2 **em cada célula**.
- **Somas por célula:** Σ Λ(n)/√n em `mpmath.iv`, sem peso, para n ∈ [404, 442.413], com as duas implementações do crivo.
  Um n de pertença ambígua entra nas duas células.
- **Resultado:** C_k^sup = Σ_células sup|Q_k|·S_célula/π_inf.
- **Fronteira entre regimes:** n ≤ 403 fica no regime I e n ≥ 404 no regime II. Nenhum n fica fora ou em ambos (asserção).

### 2.4 Decisão

- **Leitura da execução 4:** B_rel_sup e Sabs_rel_sup lidos como `Fraction` das strings exportadas, já verificadas por
  asserção ≥ extremo superior.
- **Normalização:** |c_k|_inf = extremo inferior exato.
- **Critério:** total_k ≤ Fraction(1, 10⁶), por frações exatas.
- **Exportação:** com `sup_chk`.

## 3. Testes obrigatórios (antes da execução completa)

- **T1–T9:** `cert_testes.py`, reaplicados sem alteração; o script importado continua com hash 95bec528….
- **T10 (enumeração):**
  - os 51 n do regime I, iguais nas duas implementações;
  - crivo de [404, 442.413], igual nas duas implementações;
  - floor(e⁵), floor(e⁶) e floor(e¹³) sem ambiguidade.
- **T11 (cobertura):** bordas das células exatas; primeira = 6, última = 13, sem lacunas; todo n em [404, 442.413]
  atribuído a pelo menos uma célula; total de termos = 37.049 + 161 no regime II.
- **T12 (consistência entre regimes):** em pelo menos 20 valores de n em (6, 7] e em (12, 13], em 3 blocos, o extremo
  superior de |Q_k(log n)| ponto a ponto (método do regime I) é ≤ ao sup da célula correspondente (regime II).
- **T13 (diagnóstico B, sem valor de prova):** em 3 blocos e nos 51 n do regime I, o Q_k em ponto flutuante do estimador
  fica dentro do intervalo, ou a menos de 10⁻¹⁰ relativo.
- **T14 (decisão):** casos sintéticos com total = 10⁻⁶ ± 10⁻²⁵ decididos corretamente.
- **T15 (margem):** v_min² ≥ 2 exato em todas as células de todos os blocos, antes de somar.

**Execução de desenvolvimento permitida:** uma, no bloco b01, com o mesmo método, para depuração. Suas saídas são
descartadas, e nenhuma escolha de método (regimes, δ, fronteira) pode mudar depois dela. Correções de implementação são
registradas como tais.

## 4. Regras de decisão, falha e leitura (fixadas agora)

- **Par certificado** ⇔ total_k ≤ 10⁻⁶ por frações exatas e todos os testes e asserções do bloco passam.
- **Se falhar em linhas elegíveis:**
  - registra-se "não certifica" para elas; isso **não** refuta S2-ratio nem exclui compensação no resíduo real;
  - **nesta entrega não** se tenta a soma com sinal, não se muda a fronteira entre regimes, não se refina δ e não se
    subdivide célula;
  - a alternativa (cota com sinal, explorando cancelamento em e^{iE_c log n}) fica listada como trabalho futuro, com
    declaração própria.
- **Se passar:** a leitura é a de §5, sem extrapolação a outros cortes ou ao estimador registrado.
- **Grade:** nenhuma ampliação.

## 5. O que fica estabelecido, se certificado

Para M^math, condicional a RH (F5 e J1 bibliográficas), na base de confiança declarada (DECLARACAO_CERT §2, lema de
somação de §II.19.2):

|a_k·(F* − M_𝒦)| ≤ 10⁻⁶·|c_k| nos pares certificados.

É a condição por linha **no observável ideal F\***, contra o catálogo real, **sem corte em U₂**.

**Não estabelece:**
- C2 (elegibilidade, agregação por fração, critério de fase Q);
- a camada do estimador registrado (ordenadas tabuladas, densidade usada, código em ponto flutuante);
- S1, S3a, S3c;
- H1, que continua **aberta**.

## 6. Saídas

`cert_contaminacao.py`, `cert_contaminacao_testes.py`, `cert_contaminacao_testes_resultado.json`,
`cert_contaminacao_blocos.csv`, `cert_contaminacao_tabela.csv` e `cert_contaminacao_resumo.json`. Todas entram em
`MANIFESTO_CERT.csv`, e os arquivos da execução 4 não mudam.
