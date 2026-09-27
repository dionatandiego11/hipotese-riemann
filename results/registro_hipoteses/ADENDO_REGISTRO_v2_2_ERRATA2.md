# Errata 2 ao adendo 2 do registro v2 — o que o diagnóstico do estádio não estabelece, e encerramento por prioridade (25/09/2026)

Corrige a **Errata 1** (`b56b0470…`) e uma proposta que eu havia feito na mensagem do mesmo dia. Nem o adendo
(`0b505348…`) nem a Errata 1 são alterados; os dois ficam com seus hashes. SHA-256 desta errata em
`ADENDO_REGISTRO_v2_2_ERRATA2.sha256`. Motivo: segunda revisão do usuário em 25/09/2026, com três distinções e uma
recusa. Todas aceitas.

## 1. Marginal abaixo do alvo não é reprovação

A Errata 1, C1.3, dizia que "um marginal abaixo do alvo é suficiente para reprovar a viabilidade". Está **errado pela
regra que nós mesmos fixamos**: no §5 do adendo, reprovar exige que o **limite superior** do intervalo de Wilson fique
abaixo do alvo. Uma frequência pontual abaixo de 0,80 com intervalo cruzando 0,80 é **inconclusiva**. Fica valendo:

- **insuficiência demonstrada:** limite superior < alvo;
- **inconclusivo:** intervalo cruza o alvo;
- **encerramento por orçamento ou prioridade:** decisão de pesquisa, legítima e independente do resultado
  estatístico — e que **não pode** ser relatada como insuficiência demonstrada.

## 2. A cota sobre a conjunção exige marginais do mesmo experimento

P(conjunto) ≤ min P(marginais) é correta **quando as marginais vêm do mesmo experimento**. No diagnóstico em curso, G,
g01 e g04 são espectros substitutos independentes, e **não foi demonstrado** que os sub-blocos gerados assim
representem as distribuições que teriam se fossem extraídos de G. Portanto:

- uma marginal baixa neste diagnóstico é evidência de problema **no modelo substituto examinado**;
- ela **não** estabelece cota para o desenho conjunto pretendido, e muito menos para o estádio real;
- qualquer frase de cota em relatório precisa dizer de qual experimento vêm as marginais.

## 3. "Amplitude não prevista" não é "amplitude prevista igual a zero"

Nas linhas do catálogo O1 sem previsão de amplitude (todas exceto L = 2), o coeficiente 0 é **preenchimento**, não
previsão de ausência física. Nas tabelas de relato, `ratio_to_theory` e `phase_error_rad` dessas linhas saem como
**não aplicável**, com o motivo escrito. Os arquivos brutos e os avisos de divisão por zero ficam preservados como
estão, sem limpeza.

## 4. Proposta minha, descartada

Eu havia sugerido, na mensagem de 25/09, que marginais ≥ 0,9 abririam caso para um desenho conjunto reduzido, com
E-C2bb rebaixado a descritivo. **Descartado:** seria escolher uma versão mais fácil do controle a partir do
diagnóstico. Uma pergunta científica diferente pode justificar outro desenho no futuro; não se prepara esse desenho
agora, e não se usa o diagnóstico para escolhê-lo.

## 5. Decisão registrada

- O diagnóstico em curso **termina dentro do teto de CPU já aplicado** (`RLIMIT_CPU` 86.400 s no PID 206589), é
  relatado com a classificação limitada da Errata 1 (marginais, espectros independentes, sementes não reproduzíveis) e
  tem o custo de CPU medido registrado. **Não abre rodada nova automaticamente.**
- **Produção dos níveis do estádio: bloqueada.** O desenho atual fica **encerrado por prioridade** — não por
  insuficiência demonstrada. Redesenho futuro exige pergunta científica nova.
- Nenhum desenho conjunto e nenhuma produção reduzida nesta rodada.
- Fila: fechar a V2′ de χ₋₄ e registrar; executar a H-004 quando as dependências dela estiverem satisfeitas;
  desenvolvimento seguinte em P-R1, bibliografia e CL0 — este último delegado ao outro modelo, por pedido do usuário.

*Dionatan Resende & Claude Opus — 25/09/2026.*
