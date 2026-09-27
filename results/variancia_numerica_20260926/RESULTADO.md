# VN-1 — resultado (26/09/2026 13:39)

Ficha congelada: `hipoteses/FICHA_VARIANCIA_NUMERICA.md` (`bbbcb7b9…`, congelada às 13:38:51, antes da medição).
Manifesto: `MANIFESTO.json`. Dados brutos: `medicao/medicao.json`; previsões: `previsao/previsao.json`.

## Vereditos pelos critérios da ficha (sem alteração)

| pergunta | resultado | veredito |
|---|---|---|
| **Q1** — ζ, blocos b02–b10 | RMS_Berry 0,26–0,62; RMS_GUE 13,3–15,2; 9/9 blocos no critério | **sucesso** |
| **Q3 primária** — χ₋₄ (sem órbita log 2), zeros 1–3.000 | Δχ² = **164,1**; RMS correto 0,48; todos os primos 3,60; GUE 15,2 | **conjunto correto preferido**, com concordância quantitativa |
| Q3 secundária — χ₅ (sem órbita log 5) | Δχ² = 6,9 (limiar 9); RMS correto 0,39; todos 1,16; GUE 12,3 | **inconclusivo** (direção prevista, abaixo do limiar) |
| b01 (descritivo) | RMS_Berry 0,25; RMS_GUE 16,7 | — |

## O que os números mostram

- Σ²(L) dos zeros de ζ fica **muito abaixo do GUE** a partir de L ≈ 1 (por exemplo, em b05, L = 6: 0,400 medido,
  0,527 GUE) e coincide com a fórmula semiclássica de Berry, calculada **só com primos**, dentro de ~0,001–0,005.
- As **ressurgências** previstas aparecem nos dados, na posição e na altura dependentes da altura E: em b05,
  L = 20, previsto 0,458 e medido 0,457 (vizinhos 0,322 e 0,305); em b10, L = 20, previsto 0,442 e medido 0,441.
- χ₋₄: sem a órbita de período log 2, a curva é mais baixa e a previsão correta acerta (L = 4: medido 0,276,
  correto 0,281, todos os primos 0,378). A alternativa com o primo 2 fica ~9 σ fora em L = 3–5.
- **Observação descritiva:** os resíduos em relação a Berry são ~3 vezes **menores** que a incerteza declarada
  (RMS ≈ 0,3). O σ conservador (substitutos GUE mais a banda de τ*) superestima a dispersão real dos zeros, cujas
  flutuações de longo alcance são fixadas pelos primos, e não aleatórias como no GUE. Isso torna os vereditos
  robustos, mas o RMS não deve ser lido como qualidade de ajuste calibrada.
- O viés de unfolding (média de n − L) ficou ≤ 2·10⁻⁴ em todos os blocos de ζ.

## Rótulos e limites

- **Q1: B** — reprodução numérica de resultado conhecido (Berry 1988; dados de Odlyzko). Explica, no projeto, por que
  as estatísticas de longo alcance se afastam do GUE: as órbitas curtas (primos) fixam essa parte do espectro.
- **Q3 (χ₋₄): B** — a remoção de uma órbita altera Σ² como previsto. Depende da extensão da fórmula a χ real,
  que é derivação própria **não conferida em fonte**. **Novidade não estabelecida:** o arcabouço de
  Bogomolny–Keating cobre o caso geral; rótulo C só depois de uma busca adequada.
- Dados de ζ são T0 (já consultados para outras observáveis); χ usou só e01/f01, fora da reserva da H-004. Não é
  teste prospectivo.
- Não se relaciona ainda, quantitativamente, com o C3 (Var(s) de espaçamentos vizinhos); Σ² é uma observável de longo
  alcance e Var(s), de curto alcance.
- Nada aqui é evidência sobre RH.
