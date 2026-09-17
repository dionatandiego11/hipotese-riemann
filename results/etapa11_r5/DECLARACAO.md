# R5 — declaração prévia do cálculo finito do estimador (14/09/2026)

Gravada **antes** de qualquer execução do script de cálculo. SHA-256 registrado em `DECLARACAO.sha256`.

## Escopo e natureza
- Cálculo **finito** de sensibilidade e contaminação do estimador direcionado primário. **Não** demonstra controle do
  truncamento (H1 aberta) e **não** altera conclusões de m4.
- **Nenhum dado de zeros** é usado. Entradas: A, B, L e E_c de cada bloco (lidos de `metrics.json`), catálogo, pontos de
  banda e U.
- Todos os resultados são **classe B** (ponto flutuante de dupla precisão; SVD LAPACK via numpy). Nenhuma cota
  certificada é produzida. Qualquer certificação futura exigiria aritmética intervalar e é declarada fora do escopo.

## Blocos
Os 30 blocos analisados em m4, com A, B, L e E_c de `metrics.json` (`instrument`):
- m4-v1 b01–b10: `results/run_20260913_144429_m3_b01*`;
- m4-v2 c01–c10: `results/run_20260913_173045_m3_c01*`;
- m4-v3 d01–d10: `results/run_20260913_220906_m3_d01*`.

Código de referência: `src/riemann_spectra` (idêntico a `archive/code_m4-v3` e a `archive/code_m4-v2` em
`window_response` e `targeted_joint_fit`, conferido por diff). A FWHM é recalculada por `measure_window_response`
(m4-v3). Para b e c, a FWHM original diferia em ≤ 2,5·10⁻¹⁰ relativo (AUDITORIA §4); a diferença é registrada e não
corrigida.

## Estimador
- Primário `band_conjugate`: 𝒦 = `prime_power_catalog(t_min = 0.5, t_max = 5.0)`, todas as potências de primo com
  log n ∈ [0,5; 5] (catálogo efetivo, Λ(n) > 0).
- Pontos: `np.unique` da concatenação de `linspace(T_k − h, T_k + h, 9)`, com h = 0,5·FWHM. É a mesma construção do
  código.
- Matriz real M = [Re(G+H), Re(i(G−H)); Im(G+H), Im(i(G−H))], com G e H como em `targeted_joint_fit`.

## Quantidades a calcular (por bloco)
1. **SVD** de M: valores singulares σ₁ ≥ … ≥ σ_{2K}.
   - Tolerância de posto: tol = max(2J, 2K)·σ₁·ε_mach.
   - Posto = #{σ_i > tol}.
   - Relatar σ₁, σ_min, σ₁/σ_min e o posto.
2. **M⁺ pela SVD truncada ao posto.** Não se usam equações normais.
3. **Normas de linha** de M⁺ para cada k:
   - ‖e_{x_k}ᵀM⁺‖₁ e ‖e_{x_k}ᵀM⁺‖₂ (S2-ratio);
   - para S2-complexo, as linhas complexas combinadas e_{x_k}ᵀM⁺ + i e_{y_k}ᵀM⁺, com normas ℓ₁ e ℓ₂ do vetor complexo.
4. **Exatidão numérica (B):** max |M⁺Mθ* − θ*| com θ* = (c, 0).
5. **Contaminação** para cada **U ∈ {5,5; 6; 7; 8; 10}** (declarado agora):
   - ρ_lin(U) nos pontos, com c(n)ℓ_n para potências de primo com 5 < log n ≤ U;
   - ε_k^{lin}(U) = e_{x_k}ᵀM⁺ρ_lin(U);
   - relatar |ε_k^{lin}(U)|/|c_k|, que é a contribuição à razão de S2-ratio, e o máximo sobre k;
   - para comparação, relatar também a versão complexa.
6. **Referência:** τ = 10⁻⁶. Só comparação descritiva; sem veredito sobre C2.

## Saídas
- `results/etapa11_r5/r5_calculo.py` e `r5_resultados.json`.
- Nenhuma alteração em configs, locks, resultados de m4 ou documentos de conclusão.
