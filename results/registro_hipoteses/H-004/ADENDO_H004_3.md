# Adendo 3 à H-004 — adiamento por prioridade (26/09/2026)

Declaração: [DECLARACAO.md](DECLARACAO.md) (`82382c59…`); adendos 1 (`6391eb1a…`) e 2 (`a5d071be…`); complemento do
adendo 2 (`f61ecb49…`). SHA-256 deste adendo em `ADENDO_H004_3.sha256`. Gravado **antes** de qualquer execução do
instrumento nos blocos reservados e sem nenhum contato com os erros do estimador.

## 1. Decisão

A H-004 fica **adiada por prioridade**, por decisão do usuário em 26/09/2026. Não é falha, não é resultado negativo e
não é abandono.

## 2. Motivo, declarado com a avaliação que o fundamenta

- A execução exige a V2′ de χ₅, pré-condição do `preditor_pr1_v3.py` congelado (complemento §4), estimada em 40–50
  h-CPU. Isso está acima do limiar de produção longa do `ADENDO_REGISTRO_v2_2`.
- **Avaliação do ganho, feita sem ver resultado algum:** o mecanismo testado é a projeção linear, no estimador, de uma
  fórmula explícita que é teorema. No desenvolvimento (§2 da declaração), a fração explicada foi de 0,99998 em ζ e o
  resíduo ficou em ~10⁻⁸ no Maass. O desfecho esperado é sucesso, salvo erro de código ou de dados; a informação
  nova esperada é pequena. É uma verificação de calibração do instrumento, não uma pergunta nova sobre os zeros.
- Essa avaliação é um juízo de prioridade, **não** uma previsão registrada nem um resultado da H-004.

## 3. O que fica preservado

- Declaração, adendos, preditores v1–v3, `dependencias_v3.json` e testes: inalterados.
- **Reserva mantida:** e02–e04 e f02–f04 continuam reservados para a H-004 e não podem ser usados por outras
  análises sem declaração própria, que deve registrar o efeito sobre a H-004. e01 e f01 seguem exploratórios.
- Para retomar: V2′ de χ₅ com declaração de custo e teto → controle nos 8 blocos → preditor v3, na ordem do §5.

*Dionatan Resende & Claude Opus — 26/09/2026.*
