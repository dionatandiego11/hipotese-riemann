# Adendo 3 ao `ctrl-estadio-v1` — E-C1o no bloco único e desenho do estudo de poder (21/09/2026)

Gravado **antes** de qualquer nível do bilhar ser calculado para o instrumento e antes de rodar o estudo de poder.
SHA-256 em `ADENDO_ESTADIO_3.sha256`. Declaração `c7ce5d5b…`; adendos 1 (`a1496aca…`) e 2 (`ea251f00…`).

## 1. E-C1o no bloco G (regra explícita)

A declaração escrevia E-C1o como "no máximo 2 blocos com alguma detecção clara sem correspondência", contando blocos.
O adendo 1 passou E-C1o para o bloco único G, onde contar blocos não faz sentido. Fica fixado:

**E-C1o passa** se a fração dos picos "detected" do bloco G que **não** correspondem a nenhum comprimento de
O1 ∪ {2m}, pela tolerância calibrada, for **≤ 0,10** (mesma regra do M-C1 do controle de Maass). Em g01–g04 a
avaliação é descritiva.

E-C4 continua como declarado (fração ≤ 0,05), avaliado em G.

## 2. Desenho do estudo de poder (exigido pelo adendo 2 §2)

Fixado antes de rodar:

- **Réplicas:** 40 com sinal e 40 sem sinal, por configuração de bloco. Incerteza relatada por intervalo de Wilson a
  95%; com 40 réplicas, uma probabilidade próxima de 0,8 tem meia-largura ≈ 0,12.
- **Espectros substitutos:** níveis GOE (β-Hermite com β = 1) com a densidade de Weyl do quarto de estádio, no mesmo
  intervalo de k do bloco.
- **Sinal injetado (alternativa):** a **densidade exata da família** da D1-E, d_bb(k) = (abk/π)Σ_{m≤10} J₀(2bmk),
  resolvendo N̄₀(k) + N_fl^bb(k) = x. Não é uma linha de amplitude constante: a amplitude cresce como √k e a fase é a
  da derivação. **Efeito mínimo relevante = a própria previsão**, sem fator de escala.
- **Réplicas sem sinal:** só o fundo GOE, para estimar a taxa de falso positivo de E-C1.
- **Cadeia por réplica:** a mesma do instrumento (nulos shuffle e GOE, detector sem catálogo, calibração sintética,
  correspondência, ajuste dirigido e critérios), com **realizações reduzidas**, fixadas agora: shuffle 60 para σ e 300
  para o limiar; GOE 4 e 8; calibração sintética com 3 realizações; controle de fase 100; perturbações de precisão 2.
  **Nota de redação (antes de rodar, sem nenhum dado):** a primeira versão fixava GOE 40 e 120 e 8 realizações
  sintéticas. Cada espectro GOE de dimensão ~20.000 custa segundos (diagonalização O(n²)), e o nulo GOE **não entra
  em nenhum critério** (E-C1, E-C1o, E-C4 e E-C2bb usam o nulo primário shuffle); ele só alimenta campos
  descritivos. Os números foram reduzidos para caber no orçamento de tempo, sem mudar nenhum critério.
  A redução afeta a precisão do limiar, não o mecanismo; o relatório informa o limiar médio obtido.
- **Blocos estudados:** G (12.000 níveis) para E-C1, E-C1o e E-C4; g01 e g04 para E-C2bb. g02 e g03 não entram, por
  custo; ficam cobertos por interpolação qualitativa.
- **Medidas:** P(E-C1 | sinal), P(E-C1 | sem sinal), P(E-C1o | sinal), P(E-C4 | sinal) e P(E-C2bb | sinal) em g01 e g04;
  além da distribuição de \|Ĉ/C̄_bb − 1\|.

## 3. Regra de decisão, fixada agora

- Se **P(E-C1 | sinal) ≥ 0,80** e **P(E-C1 | sem sinal) ≤ 0,10**, o critério E-C1 fica como está e a produção dos níveis
  pode começar.
- Se P(E-C1 | sinal) < 0,80, E-C1 é redesenhado por novo adendo **antes** de qualquer nível: as opções, também fixadas
  agora, são (a) ampliar a faixa de k, com o custo recalculado, ou (b) trocar a detecção cega por um critério de
  amplitude com elegibilidade geométrica, como no aprendizado do Maass.
- **E-C2bb:** o estudo **não** decide o critério; ele só registra a probabilidade prevista. Um P(E-C2bb) baixo já está
  antecipado na análise de poder (o ruído do nulo é grande diante da tolerância de 10%), e o resultado real continua
  informativo nos dois sentidos, porque o resíduo verdadeiro pode ser muito menor que o do nulo.
