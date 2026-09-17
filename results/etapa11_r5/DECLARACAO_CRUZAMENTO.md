# R5 — declaração prévia do cruzamento descritivo com C2 (14/09/2026)

Gravada **antes** do cálculo do cruzamento. SHA-256 em `DECLARACAO_CRUZAMENTO.sha256`.

## Natureza
- **Análise exploratória** de resultados já conhecidos (m4-v1, m4-v2, m4-v3).
- Sem novos testes de significância, sem alteração de critérios, sem reclassificação de C1, C2 ou C3.
- Classe B.
- Não demonstra falha de C2 nem violação de S2-ratio′, cujo alvo é a projeção do **truncamento**, não da contaminação
  finita.

## Fontes
- **Resultados de m4** (somente leitura):
  - `tables/<bloco>/arithmetic_matches.csv` dos runs primários m4-v1 (`run_20260913_144429_m3_b01*`), m4-v2
    (`run_20260913_173045_m3_c01*`) e m4-v3 (`run_20260913_220906_m3_d01*`); colunas `prime`, `repetition`,
    `coefficient_theoretical`, `fit_ratio_to_theory` (estimador primário `band_conjugate`), `z_predicted`,
    `clearly_detectable`, `resolved`;
  - `metrics.json`: `arithmetic.threshold_interval.z_high` e `arithmetic.clear_margin` (se ausente, `clear_margin = 1.5`
    de `configs/m4_v*.toml`).
- **R5 já executado:** as quantidades são recalculadas pelo mesmo código de `r5_calculo.py` (declaração
  `DECLARACAO.md`, SHA-256 e8d681cb…), mesmos U ∈ {5,5; 6; 7; 8; 10}.

## Tabela por bloco × linha (47 linhas × 30 blocos)
1. **Elegibilidade:** `eligible = resolved AND clearly_detectable` (regra do código). Mais `resolved`,
   `clearly_detectable` e a **margem do critério** `margin = z_predicted / (clear_margin · z_high)`; a linha é claramente
   detectável se `margin ≥ 1`.
2. **Erro registrado com sinal:** `e_rec = fit_ratio_to_theory − 1` = Re Ĉ_k/c_k − 1.
3. **Contaminação projetada com sinal**, para cada U: `e_lin(U) = (e_{x_k}ᵀM⁺ρ_lin(U))/c_k`, isto é, a contribuição à
   razão Re Ĉ_k/c_k − 1. c_k tem sinal negativo, e a divisão preserva o sinal da razão.
4. **Resíduo após subtração da contaminação calculada:** `d(U) = e_rec − e_lin(U)`.
   - Ele reúne truncamento acima de U e demais partes de ρ_trunc, erros das ordenadas, diferença de densidade, erros
     numéricos e diferenças de FWHM entre versões de código.
   - **Não** identifica isoladamente compensação pelo truncamento.
5. **Escala suficiente e tolerância:**
   - `escala_suficiente_F = τ|c_k|/‖e_{x_k}ᵀM⁺‖₁` (unidades de F);
   - `escala_suficiente_razao = τ` (por construção, a condição ℓ∞ equivale a ‖e_{x_k}ᵀM⁺‖₁·max|ρ| ≤ τ|c_k|);
   - `tau = 1e-6`.

## Apresentação
- Duas seções separadas: linhas **elegíveis** e **não elegíveis**.
- **Resumos por U e grupo:**
  - número de pares (bloco, linha);
  - max e mediana de |e_rec|, de |e_lin(U)| e de |d(U)|;
  - número de pares com |e_lin(U)| > τ;
  - número com |d(U)| > τ.
- Correlação descritiva sgn(e_rec) × sgn(e_lin): contagem de concordância de sinais, sem teste.
- **Leitura obrigatória:**
  - "blocos com alguma linha acima de τ" do cálculo anterior refere-se ao catálogo completo e **não** é contagem de
    falhas de C2;
  - a variação entre U = 5,5 e 10 indica estabilidade só nesse intervalo finito e não controla a cauda acima de 10.

## Saídas
- `results/etapa11_r5/cruzamento.py`
- `cruzamento_tabela.csv`
- `cruzamento_resumo.json`
