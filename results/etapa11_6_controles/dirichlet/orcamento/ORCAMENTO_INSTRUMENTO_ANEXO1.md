# Anexo 1 ao orçamento — decomposição medida da etapa aritmética e conferência da contabilidade de CPU (25/09/2026)

Complementa `ORCAMENTO_INSTRUMENTO.md` (`2e67b472…`), que **não é alterado**. SHA-256 deste anexo em
`ORCAMENTO_INSTRUMENTO_ANEXO1.sha256`. Motivo: no orçamento, o custo do controle de fase saiu **negativo** no ajuste,
isto é, não estava resolvido, e a atribuição do custo às perturbações de precisão era inferência de ajuste, não
medição. Pedido do usuário: medir a decomposição.

## 1. Método

`bench_aritmetica.py` monta o pipeline uma única vez (níveis substitutos GUE do bloco e02, transformada, nulo mínimo
só para a etapa rodar, detecção) e depois chama `arithmetic_comparison` quatro vezes, variando **uma contagem por
vez**. CPU por `getrusage` (RUSAGE_SELF + RUSAGE_CHILDREN) e número de threads lido em `/proc/self/status` a cada
ponto. Nenhum zero real.

## 2. Medições

| realizações de fase | perturbações de precisão | CPU | parede | threads |
|---|---|---|---|---|
| 10 | 2 | 8,13 s | 9,37 s | 1 |
| 999 | 2 | 8,19 s | 9,26 s | 1 |
| 10 | 20 | 43,06 s | 48,30 s | 1 |
| 999 | 20 | 43,39 s | 48,09 s | 1 |

## 3. Decomposição

| termo | valor | efeito nas contagens declaradas |
|---|---|---|
| base | 4,16 s | 4,16 s |
| por realização de controle de fase | **0,000204 s** | 999 realizações → **0,20 s** |
| por perturbação de precisão | **1,948 s** | 20 perturbações → **38,96 s** |
| **total** | rms do ajuste **0,069 s** | **43,3 s por bloco** |

**O controle de fase é irrelevante no custo**: as 999 realizações somam 0,2 s, ou 0,5% da etapa. Quem manda são as 20
perturbações de precisão, com quase 2 s cada. Isso agora está **medido**, não inferido: os dois pontos com precisão
fixa e fase variando de 10 para 999 diferem em 0,06 s e 0,34 s, dentro do ruído.

## 4. Por que 43 s aqui e 67 s no orçamento

No anexo o nulo é mínimo (8 + 40 realizações), o que muda o limiar e, com ele, **quantos picos são classificados como
detectados** — e o custo da etapa cresce com o número de picos detectados que entram no ajuste dirigido e no controle
de fase. No orçamento, os pontos vêm do pipeline completo, com nulos maiores. As duas medições não se contradizem:
medem a mesma etapa em contextos de limiar diferentes. **Para o orçamento fica valendo o valor maior, 67 s por bloco**,
que é o conservador.

## 5. Contabilidade de CPU, conferida

- **Threads = 1** em todos os pontos medidos, lido do processo, não assumido por variável de ambiente.
- **Sem processos filhos:** o benchmark roda com `workers = 1`; `RUSAGE_CHILDREN` entra na conta mesmo assim.
- **CPU e parede separadas:** a razão CPU/parede ficou entre 0,87 e 0,89, porque a máquina tinha três processos pesados
  simultâneos. A CPU é a grandeza do orçamento; a parede depende da carga.
- **Custo deste exercício de orçamento:** ≈ 640 s de CPU (≈ 0,18 hora-CPU) somando as cinco execuções do benchmark
  completo e as quatro medições deste anexo.

## 6. Orçamento final dos 8 blocos (inalterado em relação ao documento principal)

| | CPU acumulada | parede, 1 processo | parede, 4 trabalhadores |
|---|---|---|---|
| custo medido em e02 | **1,55 h** | 1,55 h | ~0,39 h |
| custo medido em f04 no shuffle (pior) | **1,8 h** | 1,8 h | ~0,45 h |
| com margem de ±30% sobre o pior | **1,3 a 2,4 h** | idem | ~0,6 h |

Abaixo do limiar de 4 horas-CPU do `ADENDO_REGISTRO_v2_2` §2. **Retomada:** por bloco (`--blocos`); não há checkpoint
dentro do bloco, e uma interrupção no meio perde no máximo ~14 min de CPU daquele bloco; as sementes vêm da posição do
bloco na lista declarada, então reexecutar um bloco isolado reproduz o mesmo resultado.

*Dionatan Resende & Claude Opus — 25/09/2026.*
