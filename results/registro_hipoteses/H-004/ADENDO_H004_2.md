# Adendo 2 à H-004 — identidade do conjunto de dados depois do passe D3 e carregador de entradas (25/09/2026)

Declaração: [DECLARACAO.md](DECLARACAO.md) (`82382c59…`); adendo 1 (`6391eb1a…`). Protocolo do registro v2
(`55514a35…`), com os adendos v2_1 (`2afb657b…`) e v2_2 (`0b505348…`) e as erratas 1 (`b56b0470…`) e 2 (`9deef4f6…`).
Passe de completude: `ADENDO_DIRICHLET_3.md` (`02340a5c…`). SHA-256 deste adendo em `ADENDO_H004_2.sha256`.
Gravado **antes** de qualquer execução do instrumento nos blocos reservados.

## 1. Motivo

As execuções originais dos zeros de L(s, χ) foram **reprovadas** em V1 e V2. O dado válido é o corrigido pelo passe D3.
O preditor congelado exige `manifest_<caractere>_12000.json` com `all_checks_passed: true`, que a execução original não
tem e não terá — o manifesto reprovado é o registro do resultado negativo e fica intacto. A pré-condição precisa
corresponder **ao arquivo efetivamente analisado e às verificações exigidas**, e não a um manifesto qualquer que diga
`true`.

## 2. Conjunto de dados declarado (χ₋₄)

| papel | arquivo | SHA-256 |
|---|---|---|
| analisado | `results/etapa11_6_controles/dirichlet/completude/zeros_chi_m4_12000_completo.txt` | `81fdfc0a37f3a9e4087eea1c2fd81ed5430b629d4edcdc2b3a08eeadc1fa81b8` |
| manifesto do passe | `.../completude/manifesto_d3_chi_m4.json` | `851a6c9584c7ea106445334176dcb4f97de2cafe645b3c5bedd912a6ddb28065` |
| zeros recuperados | `.../completude/recuperados_chi_m4.json` | `03f712b9993e00c5273040fcb7504dffab0adb82d429573501460b313b07663f` |
| código do passe | `.../completude/completude_d3.py` | `3450b005959f0a76b11677b9144a72d16fe47a1d6d635131233fc815698dc1be` |
| **execução reprovada, preservada** | `results/etapa11_6_controles/dados/zeros_chi_m4_12000.txt` | `698e7dbaabc4185d97d1bc407970740ef7e1f14eec686af4800aa4202b18d8b4` |
| manifesto reprovado | `.../dados/manifest_chi_m4_12000.json` | `all_checks_passed: false` (V1 e V2 reprovadas; V3 e V4 aprovadas) |

O manifesto D3 registra hoje certificado final, V1′, V3′ e V4′ aprovadas; **V2′ ainda não está nele** (a varredura com
passo d̄/16 está em curso). χ₅ entra pelo complemento do §6.

## 3. O que a correção mudou

- **Valores: nada.** Nenhum zero original foi alterado. A lista de trabalho é 11.986 zeros originais + 14 recuperados,
  conferido elemento a elemento.
- **Contagem: igual**, 12.000.
- **Indexação: mudou**, a partir do índice 4223 (primeiro par recuperado). Bordas dos blocos, na lista corrigida:

| borda (índice na lista corrigida) | γ | índice que esse γ tinha na lista original | recuperados abaixo |
|---|---|---|---|
| 3.000 | 2.891,346199 | 3.000 | 0 |
| 6.000 | 5.292,270171 | 5.996 | 4 |
| 9.000 | 7.560,453545 | 8.990 | 10 |
| 12.000 | 9.749,443063 | 11.986 | 14 |

- **Consequência para os blocos reservados, que são definidos por índice:** e01 (1–3000) é **idêntico** ao original;
  e02 passa a conter 4 zeros recuperados e 4 originais menos no topo; e03, 6; e04, 4, e o topo do espectro recua de
  9.758,910852 para 9.749,443063. A faixa física de e02–e04 é praticamente a mesma; o conjunto de zeros mudou em 14
  inserções e 14 exclusões no alto da lista.
- **A reserva não é reduzida:** os blocos continuam sendo e02, e03, e04, f02, f03 e f04, pelos mesmos índices
  declarados. e01 e f01 seguem exploratórios (contêm o piloto).

## 4. Acesso ocorrido aos blocos reservados, declarado

O passe D3 **tocou** os blocos reservados, e isso não é escondido: calculou larguras de intervalo, θ_χ e o certificado
de S, e reexaminou intervalos grandes. **Nenhuma observável do instrumento** (transformada, detecção cega, Ĉ_k, e_obs)
foi calculada. O agente viu as posições dos 14 zeros recuperados e os tamanhos dos maiores intervalos. Não houve
contato com os erros do estimador, que são o objeto da H-004. Fica registrado como **acesso ocorrido para completude**;
não se alega reserva intacta em sentido forte.

## 5. Carregador de entradas: `preditor_pr1_v3.py`

- `preditor_pr1_v2.py` (`cc14e12f…`) **fica preservado** e continua válido para o caso em que o manifesto do cálculo
  passa por si.
- `preditor_pr1_v3.py` difere de v2 **somente** na função de pré-condição e nos caminhos de entrada. Exige:
  1. SHA-256 do arquivo analisado igual ao campo `saida.sha256` do manifesto D3;
  2. no manifesto D3: `certificado_final.passed` e as verificações **V1, V2, V3 e V4** todas verdadeiras;
  3. bordas A e B de `block_metrics.json` iguais às do arquivo analisado, com tolerância 10⁻⁹;
  4. catálogo do controle idêntico ao do preditor, como em v2.
  Qualquer falha **aborta** com "pré-condição não satisfeita", sem produzir veredito.
- **Equivalência obrigatória antes da execução:** sobre as mesmas entradas em que v2 roda, v2 e v3 devem produzir a
  seção `blocks` **idêntica**. O teste fica em `test_preditor_v3.py` e o resultado é registrado. Sem esse teste, v3 não
  roda.
- `dependencias_v3.json` é congelado antes da execução, como em v2.
- **Nada mais muda:** previsão, ruído, seleção (|e_prev| > 5·ruído), limiares, medida primária e classificação
  continuam os da declaração e do adendo 1.

## 6. Complemento obrigatório para χ₅

Antes de executar, um complemento hasheado (`ADENDO_H004_2_COMPLEMENTO.md`) registra para χ₅: arquivo analisado e
SHA-256, manifesto D3 e SHA-256, número de zeros recuperados, a tabela de bordas equivalente à do §3 e o efeito na
indexação. Sem esse complemento, f02–f04 **não entram** na análise.

## 7. O que este adendo não faz

Não altera critérios, previsão, seleção ou medida primária; não reduz blocos reservados; não dispensa nenhuma
pré-condição declarada — inclusive a ordem do §5 da declaração (verificações do controle, instrumento nos 8 blocos,
depois o preditor) e a V2′ ainda em curso. A aprovação por custo, no orçamento de 25/09
(`ORCAMENTO_INSTRUMENTO.md`, `2e67b472…`), **não substitui** essas pré-condições.

*Dionatan Resende & Claude Opus — 25/09/2026.*
