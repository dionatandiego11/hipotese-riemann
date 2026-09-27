# Errata 1 ao adendo 2 do registro v2 — o estudo do estádio em curso é diagnóstico, não certificação de viabilidade (25/09/2026)

Adendo corrigido: `ADENDO_REGISTRO_v2_2.md` (`0b505348…`), que **não é alterado**; sua versão e seu hash ficam como
estão. SHA-256 desta errata em `ADENDO_REGISTRO_v2_2_ERRATA.sha256`. Motivo: revisão do usuário de 25/09/2026, com
quatro apontamentos sobre o §5 e o §8 do adendo e sobre o script em execução. Os quatro foram conferidos no código e no
processo e **os quatro procedem**.

## C1. O estudo em curso estima marginais, não o conjunto

`estadio/estudo_poder_estadio.py` resume E-C1, E-C1o, E-C4 e E-C2bb separadamente e gera **G, g01 e g04 como espectros
substitutos independentes**, com sementes próprias. Isso não estima a probabilidade de todos os critérios passarem no
mesmo experimento, e probabilidades marginais **não se multiplicam** sob dependência. Há ainda diferença de escopo: a
produção exige E-C2bb nos quatro blocos g01–g04, e o estudo cobre dois; interpolação qualitativa não certifica poder.

Consequências, fixadas agora:

1. A execução iniciada em 25/09 15:20 é **diagnóstico preliminar**. Não certifica viabilidade e **não autoriza
   produção**, qualquer que seja o resultado.
2. A frase do §8 do adendo — "a probabilidade do critério conjunto … é estimada e relatada separadamente" — **não é
   cumprida** por este script. Fica corrigida aqui: o script não a estima.
3. O que o diagnóstico ainda decide: como **P(conjunto) ≤ min(marginais)**, um marginal abaixo do alvo é suficiente para
   **reprovar** a viabilidade e encerrar o desenho atual do controle. Nenhum resultado dele pode aprovar.
4. Dentro do bloco G, a conjunção E-C1 ∧ E-C1o ∧ E-C4 pode ser calculada por réplica depois, porque os três campos são
   gravados réplica a réplica. Ela será relatada como **conjunção parcial do bloco G**, dito expressamente que não é a
   conjunção do controle, que exigiria E-C2bb nos quatro blocos extraídos do **mesmo** espectro.
5. Um desenho conjunto — uma réplica = um espectro completo, blocos g01–g04 extraídos dele, conjunção registrada —
   exige declaração própria, com ganho discriminante, custo e regra de decisão, pelo §3 do adendo. Não roda sem isso.

## C2. O teto era de parede; agora é de CPU

`timeout 86400` limita tempo de **parede** e `nice -n 10` só muda prioridade: nenhum dos dois é orçamento de CPU, e
`OMP_NUM_THREADS=1` não prova que toda biblioteca esteja monothread. Mecanismo realmente aplicado, registrado agora:

- `RLIMIT_CPU` imposto ao processo em execução (PID 206589) com `prlimit --pid 206589 --cpu=86400:86700`, conferido em
  `/proc/206589/limits`: 86.400 s de CPU no limite suave, 86.700 s no rígido.
- Monothread conferido pelo número de threads do processo (`NLWP = 1`), não por variável de ambiente.
- `timeout 86400` continua ativo como limite de parede redundante.
- O relatório final informa a **CPU medida** (usuário + sistema) da execução, não o tempo de parede.

## C3. A extensão sequencial fica revogada

Avaliar Wilson em 40 réplicas, estender só quando inconclusivo e reavaliar em 60 cria duas oportunidades de decisão e
**não preserva cobertura global de 95%**. Sem justificativa de cobertura, fica valendo:

- **Uma única avaliação final**, com n = 40 com sinal e 40 sem sinal, como o `ADENDO_ESTADIO_3` §2 já fixava.
- A extensão até 60 do §5 do adendo v2_2 fica **revogada** para este estudo e para qualquer outro que não apresente,
  antes de rodar, uma correção de cobertura explícita (por exemplo, dividir o nível entre as olhadas).
- Veredito **inconclusivo** não autoriza produção.

## C4. As sementes da execução em curso não são reproduzíveis

O script deriva a semente de `hash((name, cond))`. O `hash` de strings varia entre processos (conferido: três valores
distintos em três execuções do mesmo comando) e **a semente de cada réplica não é gravada** nas linhas de saída. Logo:

- A execução de 25/09 **não é reproduzível** e carrega essa limitação em qualquer relato que a cite.
- Qualquer estudo futuro usa identificadores inteiros explícitos, ou um hash estável, e grava a semente de cada
  réplica. A correção vai em **arquivo novo e versionado**; o script em execução não é editado.

## Estado

- Produção dos níveis do estádio: **bloqueada**, independentemente do resultado deste diagnóstico.
- V2′ de χ₋₄ e H-004: prioridades inalteradas.
- Decisão pendente do usuário: se completar o desenho conjunto cabe no orçamento. Enquanto não houver essa decisão,
  nada novo é iniciado nessa frente.

*Dionatan Resende & Claude Opus — 25/09/2026.*
