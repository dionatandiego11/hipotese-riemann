# Erro das ordenadas tabuladas ρ_ord: projeção por a_k — declaração prévia (16/09/2026)

Gravada **antes** de qualquer código ou cálculo. SHA-256 em `DECLARACAO_CERT_ORDENADAS.sha256`.

**Reaproveita, sem alterar:** DECLARACAO_CERT.md (b7a7980c…), os adendos CORRECAO1 (0a693179…), CORRECAO2 (75eee940…) e
RECONF_C1C2 (a8253e9c…), DECLARACAO_CERT_CONTAMINACAO.md (1d46bced…) e DECLARACAO_CERT_DENSIDADE.md (6a69c0d7…).

**Lidos, não recalculados:** `cert_densidade_tabela.csv` (coluna `total_densidade_sup`) e `cert_tabela.csv` (coluna
`a_l1_sup`).

**Não modificados:** `cert_calculo.py` (95bec528…), `cert_contaminacao.py` (4baff933…) e `cert_densidade.py` (598871cf…).

**Corte:** o mesmo, (d₁, Δ) = (8, 2), escolhido após a avaliação exploratória.

**Separação acordada:** esta declaração trata **só** de ρ_ord. ρ_num terá declaração própria.

## 0. Verificação prévia (16/09/2026, antes desta declaração)

- **Blocos:** cada um dos 30 usa exatamente **3.000** ordenadas da tabela.
  - As bordas A e B de `metrics.json` são ordenadas da tabela (distância 0 em `check_table_completeness.json`), mas estão
    em float binário. A tabela bruta dá decimais com 9 casas.
- **Fonte:** tabela bruta `data/raw/zeros1` (SHA-256 3436c916…); manifestos com `declared_accuracy = 3e-9`; valores
  estritamente crescentes, espaçamento mínimo 0,0147.
  - O pipeline registrado lê `data/processed/zeros_100k.csv` como **float**.
- **Validação existente (classe B):** máx. |erro| ≤ 2,50·10⁻⁹ em amostras (ANDAMENTO, etapa 2). A página da fonte está
  inacessível nesta sessão (F7).
- **Borda superior de d10:** é o zero de índice 100.000, a última entrada da tabela, que não tem vizinho tabulado acima.
- **Sensibilidade empírica a ±3·10⁻⁹** registrada em m4 (mediana 5,8–7,9·10⁻¹⁰ no estimador registrado): é dado B do
  pipeline em ponto flutuante, **não premissa** desta cota.

## 1. Hipótese nova (H-tab) e objeto

**(H-tab).** Sejam γ₁ ≤ γ₂ ≤ … as ordenadas positivas dos zeros não triviais, **listadas com multiplicidade**. Para todo
n ≤ 100.000, o valor decimal da tabela γ_n^tab satisfaz |γ_n^tab − γ_n| ≤ 3·10⁻⁹.

**H-tab reúne três coisas:**
- a precisão declarada (F7, `bloqueado` por acesso);
- a correspondência índice ↔ posto, com completude conferida só em classe B (`mpmath.nzeros`);
- a listagem com multiplicidade (a simplicidade, F2, deixa de ser necessária, mas a tabela precisaria repetir um zero
  múltiplo).

**Estado:** hipótese **não certificada**, sustentada por declaração da fonte e por validação amostral B.

**Janela e extensão:** [A*, B*] = [E_c ∓ L/2] (DECLARACAO_CERT_DENSIDADE §1). Para t fixo:
- f̃_t(E) := w(E)e_t(E) em [A*, B*] e 0 fora, com w(E) = sin²(π(E − A*)/L);
- f̃_t é **C¹ em ℝ**, porque w e w′ se anulam nas bordas;
- f̃_t′ é **lipschitziana**, mas f̃_t″ salta nas bordas, então Lagrange de 2ª ordem não se aplica diretamente.

**Conjunto de índices:** I := {n : A^tab ≤ γ_n^tab ≤ B^tab}, com A^tab e B^tab os **decimais** da tabela. São 3.000 índices
por bloco.

**Observável alvo:** F^tab(t) := Σ_{n∈I} f̃_t(γ_n^tab) − ∫ f_t d̄_rvm, com zeros tabulados exatos (decimais), densidade exata
e janela [A*, B*].

**Identidade:**

F^tab − F^rvm = Σ_{n∈I} [f̃_t(γ_n^tab) − f̃_t(γ_n)] − Σ_{zeros verdadeiros em [A*, B*] com índice ∉ I} f̃_t(γ).

## 2. Derivação (a registrar em §II.23)

Seja δ_n := γ_n^tab − γ_n, com |δ_n| ≤ 3·10⁻⁹ por H-tab, e S₂(t) := 2π²/L² + 2tπ/L + t².

1. **Lipschitz de f̃_t′.**
   - f_t″ = w″e_t − 2it w′e_t − t²w e_t;
   - |w| ≤ 1, |w′| ≤ π/L, |w″| ≤ 2π²/L²;
   - logo sup|f̃_t″| ≤ S₂(t) em cada lado das bordas, e f̃_t′ é contínua;
   - daí |f̃_t(y) − f̃_t(x) − f̃_t′(x)(y − x)| ≤ ½S₂(t)(y − x)² para todos x, y reais.
2. **Expansão em torno do valor tabulado (conhecido):**
   f̃_t(γ_n^tab) − f̃_t(γ_n) = f̃_t′(γ_n^tab)δ_n − R_n(t), com |R_n(t)| ≤ ½S₂(t)δ_n².
3. **Parcela linear projetada.** Como δ_n é real, a_k·[Re, Im de Σ_n δ_n f̃′_{t_j}(γ_n^tab)] = Σ_n δ_n g_k(γ_n^tab), com

   g_k(E) := Σ_j [aR_{kj}·Re f̃′_{t_j}(E) + aI_{kj}·Im f̃′_{t_j}(E)].

   Em [A*, B*], f̃_t′ = e_t(w′ − itw), logo Re = cos φ·w′ − sin φ·t·w e Im = −(cos φ·t·w + sin φ·w′), com φ = (E − E_c)t.
   Fora da janela, f̃_t′ = 0.

   **|a_k·Lin| ≤ (3·10⁻⁹)·Σ_{n∈I} |g_k(γ_n^tab)|.**

   É cota de pior caso sobre os sinais de δ_n: nenhum cancelamento entre zeros é assumido.
4. **Resto projetado:** |a_k·Resto| ≤ ‖a_k‖₁^sup·|I|·½(3·10⁻⁹)²·S₂(t_max), com t_max = max dos nós < 5.
5. **Zeros de borda fora de I.**
   - Se um zero verdadeiro de índice m < min I está em [A*, B*], então γ_m ≤ γ_{min I} ≤ A^tab + 3·10⁻⁹. Logo ele está a
     distância ≤ η := 3·10⁻⁹ + max(|A* − A^tab|, |B* − B^tab|) da borda (idem para m > max I, na borda superior).
   - Nessa faixa, |f̃_t| = w ≤ sin²(πη/L) ≤ (πη/L)².
   - Contagem por Z1 (derivada; J1 bibliográfica): em (T − 1, T + 1], há no máximo 10,5·log(T + 8) zeros.
   - **|a_k·Borda| ≤ ‖a_k‖₁^sup·[10,5·log(A* + 8) + 10,5·log(B* + 8)]·(πη/L)².**
6. **Total:**

   total^γ_k := total^Δ_k + [(3·10⁻⁹)Σ_n|g_k|^sup + ‖a_k‖₁^sup·(|I|·½(3·10⁻⁹)²·S₂(t_max) + Borda)] / |c_k|_inf ≤ 10⁻⁶,

   que majora |a_k·(F^tab − M_𝒦)|/|c_k|.

**Hipóteses do total:** RH; F5 e J1 bibliográficas; **H-tab**; base de confiança declarada.

## 3. Método

- **Entradas da tabela:** γ_n^tab lidos como **`Fraction` dos decimais brutos** de `data/raw/zeros1` (hash conferido). Não
  se usam os floats do CSV processado; a diferença entre eles pertence a ρ_num.
  - A^tab, B^tab e I são obtidos dos decimais.
  - **Asserção:** o I dos decimais coincide com as 3.000 posições que o pipeline seleciona.
- **Reconstrução:** Arows por bloco via `cert_contaminacao.reconstruct` (primitivas de `cert_calculo.py`), com **parada
  bit a bit** de ρ e das 47 ‖a_k‖₁^sup contra a execução 4 nos 30 blocos.
- **g_k(γ_n^tab):**
  - por zero, w e w′ em `mpmath.iv`;
  - por par (n, j), cos φ e sin φ em `mpmath.iv` (cerca de 1,27·10⁶ pares por bloco);
  - soma em j com `isum` sobre Arows;
  - acumulação de |g_k|^sup com `up`.
  - **Custo estimado:** 3 a 8 min por bloco; os 30 blocos em 3 processos, de 30 a 80 min.
- **Termos analíticos:** resto, borda, η e S₂ em frações exatas, com log e π por extremos exatos de `mpmath.iv`.
- **Decisão:** total^γ_k ≤ Fraction(1, 10⁶), por frações exatas. Exportação por `sup_chk`. Execução com trava `--executar`.

## 4. Testes obrigatórios (antes da execução completa)

- **T1–T21:** reaplicação de `cert_densidade_testes.py`, com os resultados vigentes salvos, regenerados, comparados sem
  campos de tempo e restaurados.
- **T22 (entradas da tabela):**
  - hash de `data/raw/zeros1`;
  - em cada bloco, I dos decimais = seleção do pipeline (mesmos 3.000 índices);
  - A^tab e B^tab são os decimais das bordas;
  - |A* − A^tab| e |B* − B^tab| registrados.
- **T23 (diagnóstico B de H-tab, sem valor de prova):** em 30 índices, um por bloco, escolhidos por semente fixa,
  |γ_n^tab − Im ρ_n| com `mpmath.zetazero` a 30 dígitos. Registrar o máximo. Isto **não** valida H-tab.
- **T24 (Lipschitz):**
  - S₂ exato por bloco;
  - diagnóstico em 10⁴ pares (x, y) aleatórios, incluindo pares que cruzam as bordas, de |f̃(y) − f̃(x) − f̃′(x)(y − x)| ≤
    ½S₂(y − x)².
- **T25 (enclausuramento de g_k):** em 3 blocos e 50 zeros, g_k em ponto flutuante dentro do intervalo, ou a menos de
  10⁻¹⁰ relativo (diagnóstico).
- **T26 (borda):**
  - η exato por bloco;
  - vizinhos tabulados (quando existem) a mais de 3·10⁻⁹ + η das bordas;
  - valor da parcela de borda registrado.
- **T27 (decisão):** casos sintéticos 10⁻⁶ e 10⁻⁶ ± 10⁻²⁵.

**Execução de desenvolvimento:** uma, em b01, com saídas descartadas. Depois dela, método, H-tab e parcelas ficam travados.

## 5. Regras de decisão, falha e leitura (fixadas agora)

- **Par certificado** ⇔ total^γ_k ≤ 10⁻⁶ por frações exatas e todos os testes e asserções passam.
- **Nenhuma expectativa registrada.**
  - A cota grosseira ‖a_k‖₁ × 4,5·10⁻⁵ excederia o orçamento.
  - A cota de §2 é de pior caso sobre os sinais de δ_n e pode também exceder.
  - O dado B de sensibilidade não é premissa.
- **Se falhar em linhas elegíveis:** "não certifica" sob H-tab; nada é refutado. **Nesta entrega não** se supõe
  independência, distribuição ou cancelamento dos δ_n, e não se reduz 3·10⁻⁹ pela validação amostral.
- **Grade:** nenhuma ampliação.

## 6. O que fica estabelecido, se certificado

Para M^math, condicional a RH (F5, J1) **e a H-tab**, na base de confiança declarada:

|a_k·(F^tab − M_𝒦)| ≤ 10⁻⁶·|c_k|, com F^tab = observável com as ordenadas **decimais** da tabela, densidade d̄_rvm exata e
janela [A*, B*].

**Não estabelece:**
- ρ_num (floats do CSV, â_k em ponto flutuante, T_j em ponto flutuante, NUFFT/quadratura, [A, B] × [A*, B*]);
- C2;
- S1, S3a, S3c;
- H1, que continua **aberta**;
- H-tab, que **não** é certificada.

## 7. Saídas

`cert_ordenadas.py`, `cert_ordenadas_testes.py`, `cert_ordenadas_testes_resultado.json`, `cert_ordenadas_blocos.csv`,
`cert_ordenadas_tabela.csv` e `cert_ordenadas_resumo.json`. Todos entram em `MANIFESTO_CERT.csv`.
