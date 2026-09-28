# PT-1 — pico do fator de forma em τ = 1: ficha congelada antes da medição (27/09/2026)

**Estado:** congelada; medição **não executada** no congelamento. SHA-256 em `FICHA_PICO_TAU1.sha256`.
Categoria: previsão declarada antes da medição, em dados já consultados (T0). O projeto já calculou K_c nesses blocos
(C3), mas **os valores em τ = 1 não foram consultados** para montar esta previsão. Não é teste prospectivo.

## 1. Pergunta

O pico de K_c em τ = 1, observado no C3 e até agora explicado só heuristicamente (D), é previsto quantitativamente,
sem parâmetros livres, pelas órbitas curtas (Σ² de Berry, validada na VN-1) mais a correção de amostragem nos zeros?

## 2. Derivação (resumo)

- Unfolding x_n = N̄(γ_n) = n − ½ − S_n (convenção do ponto médio). Em τ = 1, Z(1) = Σ w_n e^{−2πi x_n} ∝ Σ w_n e^{2πi S_n}:
  o pico mede a coerência de fase de S **nos zeros**.
- **Amostragem uniforme dá zero exatamente:** e^{2πiS(t)} = e^{−2πi(N̄(t)+c)} só gira de fase. O argumento de Selberg
  (amostragem uniforme) não se transfere; era a objeção registrada em `docs/ANALISE_RESULTADOS.md`.
- **Identidade:** para S com saltos unitários nos zeros e declive −d̄ entre eles, E_unif[F′(S)] = E_zeros[F(S+½) − F(S−½)].
  Com F = s³/3: Var_unif(S) = Var_zeros(S) + 1/12. Por extremidade, amostrar nos zeros tira 1/12.
- **Modelo:** D_k = x_{n+k} − x_n − k gaussiano, com V_k = Var(D_k) ≈ Σ²_Berry(k) − 1/6. Substituto gaussiano
  estacionário com essa estrutura, medido com o **mesmo estimador** do C3.
- **Aproximações declaradas:** (G) gaussianidade; (E) V_k = Σ² − 1/6; sub-blocos sorteados de modo independente;
  altura fixa no meio do bloco. A estrutura de Berry não é exatamente realizável: autovalores negativos pequenos são
  zerados, com erro máximo em V_k de 0,0012 no modelo principal (0,7%) e 0,023 na banda τ* = 0,75 (bloco mais baixo).
- **Controle em GUE** (sem zeros; `results/pico_tau1_20260926/rascunho/`): o modelo prevê K_c(1) = 1,06 (95%:
  0,54–1,77) e o GUE real dá 0,99 (0,52–1,60). Valida a parte incoerente com viés de ~7%. **Não testa a correção 1/6**,
  porque no GUE não há pico.

## 3. Código e previsões congeladas

- `src/riemann_spectra/bragg_peak.py`; testes `tests/test_bragg_peak.py` (4: correção de estrutura, substituto
  reproduz V_k, igualdade com o estimador do C3, limite rígido e^{−2π²ε}·2N/3).
- `results/pico_tau1_20260926/previsao/previsao.py` → `previsao.json` (132 s de CPU, semente 20260927), com só primos e
  alturas. 30 blocos do C3: zeros 10.001–100.000 (b01–b10, c01–c10, d01–d10), 3.000 por bloco, 10 sub-blocos Hann de 300.
- Modelos: **B** (Berry, τ* = 0,5, correção 1/6; 300 réplicas), **B25/B75** (banda de τ*), **U** (sem correção,
  amostragem uniforme), **G** (GUE com correção); 200 réplicas cada.
- Previsões centrais: B 5,8–8,9, decrescente com a altura; banda 5,6–8,3; U ≈ 1,2; G ≈ 1,1.

## 4. Medição

`results/pico_tau1_20260926/medicao/medicao.py`: `data/processed/zeros_100k.csv`, unfolding `n_bar_rvm` (o mesmo do
C3), K_c(1) por `kc_tau1` (estimador `compute_spectral_form_factor`, 10 sub-blocos, Hann).

## 5. Critérios (fixados antes de medir)

Por bloco: faixa B = [mínimo dos q2,5% de B, B25, B75; máximo dos q97,5%]; limiar alternativo = máximo dos q97,5% de U
e G.

- **Sucesso:** medido na faixa B em ≥ 27/30 blocos **e** acima do limiar alternativo em ≥ 27/30.
- **Falha do modelo B:** medido fora da faixa B em ≥ 6/30 blocos.
- **Inconclusivo:** o resto.
- **Secundário (agregado):** média dos 30 medidos contra média prevista por B. Compatível se
  |diferença| ≤ 2·dp_média + metade da amplitude da banda de τ* entre as médias de B25, B, B75, com
  dp_média = √(Σ dp_b²)/30 e dp_b ≈ (q97,5 − q2,5)/3,92 (aproximação declarada; blocos tratados como independentes).
- **Descritivo:** correlação de Spearman entre medido e B ao longo da altura; consistência com os valores
  armazenados do C3 (conferida **depois** da medição).

## 6. O que se pode concluir

- Sucesso: o pico em τ = 1 passa de heurístico (D) a **previsto quantitativamente (B)**: é uma assinatura de
  "rigidez" dos zeros, fixada pelos primos (saturação de Σ²) e amplificada pela amostragem nos próprios zeros. A
  novidade da identidade de 1/12 aplicada ao pico **não foi pesquisada**; nenhum C antes de busca.
- Falha: registrada como está, com diagnóstico (gaussianidade, independência, banda de τ*).
- Nada aqui é evidência sobre RH.

*Dionatan Resende & Claude Opus — 27/09/2026.*
