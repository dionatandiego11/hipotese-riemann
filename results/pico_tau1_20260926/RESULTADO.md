# PT-1 — resultado (27/09/2026)

Ficha: `hipoteses/FICHA_PICO_TAU1.md` (`3e2b44e6…`, congelada às 10:49, antes da medição). Adendo técnico 1: correção
só de serialização JSON; nenhum valor foi visto antes dela. Dados: `medicao/medicao.json`; previsões:
`previsao/previsao.json`; diagnósticos: `diagnostico/`.

## Veredito pelos critérios da ficha (sem alteração)

| critério | resultado | exigido |
|---|---|---|
| medido na faixa B (Berry, correção 1/6, banda de τ*) | 25/30 blocos | ≥ 27 |
| medido acima do limiar das alternativas U (uniforme) e G (GUE) | 28/30 blocos | ≥ 27 |
| **primário** | **inconclusivo** | — |
| agregado: média medida 3,01 contra B 6,94 (diferença −3,93; tolerância 1,23) | **incompatível** | — |
| Spearman medido × B ao longo da altura | ρ = 0,46, p = 0,010 | descritivo |

Os valores medidos coincidem com os armazenados do C3 (diferença máxima de 2·10⁻¹⁵).

## O que isso diz

- **O pico é real e não é GUE:** K_c(1) ≈ 2–4, contra ≈ 1,1–1,3 previsto por GUE e pela amostragem uniforme.
- **O modelo acerta a origem e erra a altura:** superestima o pico por um fator de ~2,3 em todos os blocos, de modo
  sistemático (medidos sempre no terço inferior da faixa).

## Diagnóstico exploratório (depois da medição; não altera o veredito)

1. **A correção de 1/6 está confirmada diretamente nos zeros (E):** Var(x_{n+k} − x_n − k) medida coincide com
   Σ²_Berry(k) − 1/6 dentro de ~0,005 para k = 1…200, nos blocos b01, c05 e d10 (`diagnostico/log.txt`). A estrutura
   de segunda ordem prevista pelos primos mais a amostragem nos zeros está certa.
2. **A gaussianidade (G) falha:** média sobre k ∈ [30, 299] e sobre os 30 blocos de Re E[e^{2πi D_k}] = **0,0126 ±
   0,0005**, contra 0,041 da gaussiana com a variância medida e 0,033 com a variância de Berry. A razão, **0,39**,
   explica a superestimação de ~2,3 do pico (`diagnostico/log2.txt`). Os k-desvios têm variância correta, mas uma
   função característica em 2π bem menor que a de uma gaussiana: a coerência em τ = 1 depende de estrutura fina da
   distribuição, não só da variância.

## Rótulos e limites

- Existência e ordem de grandeza do pico, e sua origem (rigidez fixada pelos primos + amostragem nos zeros): **B**,
  qualitativo. A altura **não** está prevista: o modelo gaussiano foi reprovado.
- Correção de 1/6 nos k-desvios: **B**, exploratório (medido depois; confirmação direta, não pré-registrada).
- A identidade E_unif[F′(S)] = E_zeros[F(S+½) − F(S−½)] e sua aplicação ao pico: novidade **não pesquisada**.
- Pergunta aberta (D): qual é a função característica de D_k em 2π? A gaussianidade só vale para a variância.
- Observação lateral, não analisada: em b01 aparece outro pico, em τ = 1,24 (K_c = 4,77), na tabela do C3.
- Custo: previsão 132 s; controle GUE ~36 min de CPU (várias threads BLAS); medição e diagnósticos < 1 min.
- Nada aqui é evidência sobre RH.
