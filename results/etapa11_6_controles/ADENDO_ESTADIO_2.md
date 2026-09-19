# Adendo 2 ao `ctrl-estadio-v1` — regra explícita de E-C1 e estudo de poder antes da produção (19/09/2026)

Gravado **antes** de qualquer nível do bilhar ser calculado para o instrumento. SHA-256 em `ADENDO_ESTADIO_2.sha256`.
Declaração `c7ce5d5b…`; adendo 1 `a1496aca…`; errata da análise de poder `ANALISE_PODER_11_6_ERRATA.md`.

## 1. Regra de E-C1, sem ambiguidade

A declaração e o adendo 1 dizem "detecção clara … pela regra de m4-v3". Fica fixado que isso significa:

**E-C1 passa** se, no bloco G, existe um pico do detector sem catálogo com classificação primária **"detected"** (z
acima do limite superior `z_high` do intervalo do limiar, nulo shuffle, regra de `classify_detection` de m4-v3) e se
esse pico é correspondido à linha L = 2 pela correspondência um-a-um de m4-v3, com a tolerância calibrada.

**Não** se exige a regra de elegibilidade "claramente detectável" (z_prev ≥ 1,5 × limiar), que é outra coisa: ela
seleciona as linhas elegíveis para os critérios de coeficiente. Essa distinção não muda depois de ver níveis.

## 2. Estudo de poder antes da produção longa

A produção dos ~12.000 níveis com o `vergini` (horas) **só começa** depois de um estudo de poder por simulação, conforme
a §9 do protocolo v2 do registro e a revisão do usuário, com:
- réplicas de espectros substitutos GOE com a densidade do controle e a linha L = 2 **injetada** com a amplitude e a fase
  de C̄_bb (D1-E), e a linha L = 4 com C̄_bb/√2;
- a **cadeia completa** em cada réplica: nulos (com número reduzido de realizações, fixado no estudo), detector,
  correspondência, ajuste, elegibilidade e critérios E-C1, E-C1o, E-C4 (bloco G) e E-C2bb (blocos g01–g04);
- número de réplicas, efeito mínimo e intervalo de incerteza fixados **antes** de rodar;
- também réplicas **sem** a linha, para estimar a taxa de falso positivo de E-C1.

**Se o poder estimado de E-C1 for baixo** (limite a fixar no estudo), o critério é redesenhado por novo adendo, ainda
sem níveis. O código do instrumento e o piloto de convergência do `vergini` (minutos) podem avançar antes.

## 3. O que não muda

Todo o resto do adendo 1 e da declaração.
