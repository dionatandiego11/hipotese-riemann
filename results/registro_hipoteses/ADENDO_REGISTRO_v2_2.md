# Adendo 2 ao protocolo do registro v2 — produção longa: ganho discriminante, viabilidade demonstrada e custo limitado (25/09/2026)

Protocolo: `PROTOCOLO_REGISTRO_v2.md` (`55514a35…`); adendo 1 (`2afb657b…`). SHA-256 deste adendo em
`ADENDO_REGISTRO_v2_2.sha256`. Gravado **antes** de retomar qualquer execução nova e antes do estudo de poder do
estádio.

## 1. Motivo

Proposta do usuário em 25/09/2026, aceita: parar de crescer em volume e passar a cobrar das hipóteses previsões que
justifiquem cada dia de CPU. O retorno marginal do volume está medido e é decrescente: 100.000 zeros da ζ (M2–M4) e
24.000 zeros de Dirichlet produziram reprodução (B) e resultados negativos registrados, sem nenhuma afirmação nova; as
linhas que o instrumento resolve (log p com T ≤ 5) já estão resolvidas, e mais altura acrescenta sobretudo mais do
mesmo. Em contraste, o teste da H-004 nos blocos já adquiridos custa minutos.

## 2. A regra

> **Nenhuma produção longa sem ganho científico discriminante, viabilidade demonstrada e custo limitado.**

Definições, para a regra não ficar elástica:

- **Produção:** execução cujo produto entra em critério de decisão sobre uma hipótese ou um controle.
- **Estudo de viabilidade:** execução **só com dados sintéticos ou substitutos**, cujo produto é uma probabilidade de
  detecção ou uma medida de custo. Não produz conclusão sobre o objeto, em nenhuma hipótese.
- **Custo:** medido em **horas-CPU acumuladas** — soma do tempo de CPU (usuário + sistema) de todos os processos da
  execução, somando processos simultâneos. Onde não houver medição direta, usa-se tempo de parede × número de processos
  simultâneos, com `OMP_NUM_THREADS=1` para que a conta feche. O tempo de parede é declarado à parte, só para
  planejamento; o teto é sempre em horas-CPU.
- **Longa:** acima de **4 horas-CPU**. Abaixo disso vale a declaração normal do protocolo, sem os requisitos do §3.

## 3. Requisitos de uma produção longa

Na declaração hasheada, antes de começar:

1. **Ganho discriminante:** que previsão a execução testa, o que um resultado negativo passa a estabelecer e qual
   alternativa ele elimina. "Caracterizar melhor o instrumento" e "aumentar a faixa" não são ganho discriminante.
2. **Viabilidade demonstrada:** estudo de poder prévio (v2 §9) com incerteza, pelas regras do §5 deste adendo.
3. **Custo limitado:** teto em horas-CPU, regra de parada ao atingir o teto e o que se reporta nesse caso.
4. **Regra de decisão:** limiares e vereditos fixados antes, incluindo o veredito de inconclusão.

Faltando qualquer um dos quatro, a execução não é autorizada.

## 4. Exceção explícita para o estudo de viabilidade

Exigir poder demonstrado antes do cálculo que estima o poder seria circular. Um estudo de viabilidade fica dispensado
do requisito 2 e, em troca, declara antes de rodar: **teto em horas-CPU**, **número de réplicas**, **regra de parada**,
as medidas que produz e a proibição de conclusão sobre o objeto. Teto padrão **24 horas-CPU**; acima disso o estudo
deixa de ser exceção e cai na regra geral do §3. Atingido o teto sem terminar, relata-se o que foi concluído e o
resultado é **inconclusivo por orçamento**, nunca um veredito parcial apresentado como veredito.

## 5. Poder estimado vem com incerteza

- O número de réplicas **n** é declarado antes. A frequência observada nunca decide sozinha.
- A decisão usa o **intervalo de Wilson a 95%** sobre a frequência, contra o alvo declarado (por exemplo 0,80):
  **aprovado** se o limite inferior ≥ alvo; **insuficiente** se o limite superior < alvo; **inconclusivo** se o
  intervalo cruza o alvo.
- No inconclusivo é permitida **uma única extensão**, até um n máximo também declarado antes, e a regra é aplicada mais
  uma vez. Não há parada opcional: nenhuma decisão é tomada olhando o resultado de réplicas em andamento.
- Falso positivo: mesma construção, com **limite superior** de Wilson ≤ 0,10.
- **Poder de um critério não é poder do conjunto.** A declaração diz a qual critério a probabilidade se refere. Se o
  critério serve de filtro inicial de viabilidade, isso fica escrito; o critério conjunto tem poder próprio, estimado e
  relatado separadamente, e é ele que autoriza a produção.

## 6. Verificação declarada e em andamento

Uma verificação **já declarada** que está rodando não é produção nova e não precisa ser re-autorizada. Ela continua se,
e só se: (a) responde à causa identificada; (b) tem término estimado; (c) preserva o registro da falha original. Seu
objetivo **não** é converter reprovação em aprovação — a execução reprovada continua reprovada, com o manifesto
original intacto, e o que o passe produz é um dado novo, com histórico próprio. Interromper não torna o dado
matematicamente irrecuperável; deixa a validação incompleta, e é assim que se registra.

Aplicação imediata, com os términos estimados medidos hoje (25/09, 15:18):

| execução | estado | término estimado |
|---|---|---|
| passe D3 de χ₅ (Etapa A) | 108/790 intervalos, 17,4 s/intervalo | hoje, ~18:40 |
| V2′ de χ₋₄ (passo d̄/16 no bloco alto + completude na lista recomputada) | 74/3.000 zeros, ~139 zeros/h | 26/09, ~20:00 |

## 7. Fila fixada

1. Concluir a V2′ e registrar o resultado, preservando o histórico.
2. Executar a H-004 assim que as dependências dela estiverem satisfeitas — custo de minutos, não espera o estádio.
3. Estudo limitado de poder do estádio (pelo §4), em paralelo se houver recurso; decidir a produção pela regra
   congelada.
4. Bibliografia e CL0, já.

Bibliografia e CL0 não são gratuitas: custam trabalho intelectual. Não caem no teto de horas-CPU e, nesta fase,
rendem mais informação por recurso investido.

## 8. Aplicação ao `ctrl-estadio-v1`

- O estudo de poder entra pela exceção do §4, com **teto de 24 horas-CPU**, as **40 réplicas com sinal e 40 sem sinal**
  já fixadas no `ADENDO_ESTADIO_3` §2, `OMP_NUM_THREADS=1`, e parada por teto com relato de inconclusivo por orçamento.
  Extensão única permitida até **60 réplicas**, se o intervalo cruzar o alvo e o teto permitir.
- A regra de decisão do `ADENDO_ESTADIO_3` §3 passa a ser lida com o intervalo de Wilson do §5 deste adendo, em vez da
  frequência pontual. A mudança é **declarada agora, antes de rodar**: a execução de 22/09 morreu com a sessão e não
  gerou `estudo_poder_estadio.json`; não há resultado de poder visto por ninguém.
- **Divulgação, para que a mudança não passe por ajuste pós-dados:** um teste de fumaça do instrumento, em 22/09, com
  pouquíssimas réplicas, mostrou |Ĉ/C̄_bb − 1| entre 0,042 e 0,093 no bloco g01. Isso é informação sobre **E-C2bb**,
  cujo critério **não** muda aqui, e nenhuma informação sobre E-C1, que é o critério cuja regra de leitura mudou.
- **E-C1 é filtro de viabilidade**, não o critério do controle. A probabilidade do critério conjunto
  (E-C1 ∧ E-C1o ∧ E-C4, com E-C2bb em g01 e g04) é estimada e relatada separadamente, e é ela que autoriza a produção
  dos níveis.
- Se o estudo der **insuficiente**, o desenho atual do controle do estádio é **encerrado**. Um redesenho futuro precisa
  de justificativa científica nova — outra pergunta, outro ganho discriminante —, nunca da vontade de obter aprovação.

## 9. O que este adendo não faz

Não proíbe verificação necessária; não altera nenhum critério científico já declarado (E-C*, D-C*, M-C*, H-004); não
transforma resultado negativo em pendência; não autoriza reduzir escopo de verificação já em curso para economizar
tempo.

*Dionatan Resende & Claude Opus — 25/09/2026.*
