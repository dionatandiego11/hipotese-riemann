# Adendo 4 ao `ctrl-maass-v1` — uma linha sintética isolada por realização quando só uma cabe (19/09/2026)

Gravado **antes** de qualquer resultado de linhas. A segunda execução (`maass/execucao_v2_interrompida/`, preservada)
parou no bloco S2 antes de qualquer detecção ou comparação com o catálogo; só os limiares dos nulos foram vistos. SHA-256
em `ADENDO_MAASS_4.sha256`.
- Declaração `5db97004…`;
- adendos 1 (`4efb9020…`), 2 (`3a40cf7a…`) e 3 (`0968e75b…`).

## 1. O que aconteceu

Com os blocos por segmento (adendo 3), a FWHM é 0,1853 em S2 e ≈ 0,14 em S1. Pela regra do adendo 2,
n_iso = min(12, ⌊S/(2·10·FWHM)⌋) com S = 4,4, o que dá n_iso = 1 nos dois. O adendo 2 exigia n_iso ≥ 2; com menos, o
bloco seria declarado "sem calibração", e quase todos os critérios (correspondência, resolução, elegibilidade)
dependem dela.

## 2. Mudança (única)

O limite passa a ser **n_iso ≥ 1**.
- Com uma única linha isolada por realização, o requisito de isolamento (nenhuma outra linha a menos de 10 FWHM) é
  cumprido **trivialmente**: a linha não tem vizinha.
- O número de realizações isoladas continua ⌈40 × 12 / n_iso⌉ = **480**, o que mantém o total de 480 linhas isoladas de
  m4-v3.
- **Motivo:** o limite n_iso ≥ 2 do adendo 2 era arbitrário e não tinha fundamento no desenho da calibração. Esta
  mudança não altera nenhum outro parâmetro da calibração nem os critérios.

## 3. Conferência antes de rodar nos dados

Um teste de fumaça do bloco inteiro, com níveis sintéticos em R ∈ [110, 178] (FWHM igual à de S2) e linhas de G1
injetadas, precisa rodar até o fim antes da execução real.
