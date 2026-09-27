# Complemento ao adendo 2 da H-004 — identidade do conjunto de dados de χ₅ depois do passe D3 (26/09/2026)

Cumpre o §6 do [ADENDO_H004_2.md](ADENDO_H004_2.md) (`a5d071be…`). Declaração: [DECLARACAO.md](DECLARACAO.md)
(`82382c59…`). Passe de completude: `ADENDO_DIRICHLET_3.md` (`02340a5c…`). SHA-256 deste complemento em
`ADENDO_H004_2_COMPLEMENTO.sha256`. Gravado **antes** de qualquer execução do instrumento nos blocos reservados.
**Não altera** critérios, previsão, seleção, medida primária, blocos reservados nem o código congelado.

## 1. Conjunto de dados declarado (χ₅)

| papel | arquivo | SHA-256 |
|---|---|---|
| analisado | `results/etapa11_6_controles/dirichlet/completude/zeros_chi_5_12000_completo.txt` | `abe42070667bf90f813ea2f90acc9d0fca367071c388b09171f07314a27c84a3` |
| manifesto do passe | `.../completude/manifesto_d3_chi_5.json` | `e9ea77636273bc337ca4eb4d97c6e451dfc9262255e55489af0a3b74d124ba12` |
| zeros recuperados | `.../completude/recuperados_chi_5.json` | `a2fc84aa7d5c05db8c8da512eb28be7abb4dd49dd3e91f3f3a6daf1147adca82` |
| código do passe | `.../completude/completude_d3.py` | `3450b005959f0a76b11677b9144a72d16fe47a1d6d635131233fc815698dc1be` (o mesmo de χ₋₄) |
| **execução reprovada, preservada** | `results/etapa11_6_controles/dados/zeros_chi_5_12000.txt` | `c3727302ba8d6bd19dee30b98a575f77e9773feab6330da4f3320b33dbba52d9` |
| manifesto reprovado | `.../dados/manifest_chi_5_12000.json` | `all_checks_passed: false` (conferido em 26/09) |

O campo `saida.sha256` do manifesto D3 é igual ao SHA-256 do arquivo analisado (`abe42070…`), e `n_trabalho = 12000`.
O manifesto D3 (terminado em 26/09/2026 04:42:59, 50.223,7 s) registra **certificado final, V1, V3 e V4
aprovados**. **V2 não está no manifesto:** a V2′ de χ₅ não foi executada (ver §4).

## 2. O que a correção mudou

- **Valores: nada.** A lista de trabalho tem **11.994 zeros originais + 6 recuperados**, conferida elemento a
  elemento. Os originais são bit a bit iguais aos do arquivo reprovado. Os recuperados diferem do JSON em no máximo
  4,5·10⁻¹⁰ (arredondamento de escrita, 9 casas). Diferença máxima entre a lista de trabalho e os 12.000 primeiros
  de (originais ∪ recuperados): 4,5·10⁻¹⁰. Ordem estritamente crescente.
- **Recuperados:** a Etapa A recuperou 6 zeros em 3 intervalos (**três pares próximos**); as Etapas B e C, 0. Na lista
  corrigida, os índices são 6.336–6.337 (γ ≈ 5.404,310 e 5.404,360), 11.300–11.301 (≈ 9.012,438 e 9.012,475) e
  11.517–11.518 (≈ 9.166,155 e 9.166,187).
- **Contagem: igual**, 12.000. Lista corrigida completa: 12.006; os 6 originais mais altos saem da lista de trabalho.
- **Indexação: mudou**, a partir do índice **6.336**. Bordas dos blocos, na lista corrigida:

| borda (índice na lista corrigida) | γ | índice que esse γ tinha na lista original | recuperados abaixo |
|---|---|---|---|
| 3.000 | 2.808,091364 | 3.000 | 0 |
| 6.000 | 5.150,755239 | 6.000 | 0 |
| 9.000 | 7.366,519571 | 8.998 | 2 |
| 12.000 | 9.506,171989 | 11.994 | 6 |

- **Consequência para os blocos reservados, definidos por índice:**
  - f01 (1–3000, fora da reserva) e **f02 (3001–6000)** são **idênticos** aos originais.
  - **f03** (6001–9000) ganha 2 recuperados e perde os 2 originais do topo, que passam para f04.
  - **f04** (9001–12000) ganha 4 recuperados e os 2 vindos de f03, e perde os 6 originais mais altos. O topo do
    espectro recua de 9.510,050470 para 9.506,171989.
  - Saem da lista de trabalho os originais 9.506,881839; 9.507,554206; 9.508,292793; 9.509,287010; 9.509,776905 e
    9.510,050470.
- **A reserva não é reduzida:** continuam f02, f03 e f04, pelos índices declarados (`preditor_pr1_v2.BLOCKS`,
  herdado por v3).

## 3. Acesso ocorrido aos blocos reservados, declarado

Como em χ₋₄ (§4 do adendo 2), o passe D3 **tocou** os blocos reservados de χ₅: larguras de intervalo, θ_χ, certificado
de S e reexame de intervalos grandes. Para redigir este complemento, o agente leu as posições dos 6 recuperados,
calculou as bordas da tabela acima, conferiu a ordem da lista e viu o menor espaçamento da lista inteira (0,0317). Viu
também as linhas de progresso do log do D3 (tempos e contagens). **Nenhuma observável do instrumento** (transformada,
detecção cega, Ĉ_k, e_obs) foi calculada, e não houve contato com os erros do estimador. Fica registrado como
**acesso ocorrido para completude e identidade**; não se alega reserva intacta em sentido forte.

## 4. Pré-condição ainda não satisfeita: V2′ de χ₅

`preditor_pr1_v3.py` (congelado, §5 do adendo 2) exige `V1`, `V2`, `V3` e `V4` aprovadas **no manifesto D3 de cada
caractere**: `CHECKS_REQUIRED = ("V1", "V2", "V3", "V4")` e o laço sobre `("chi_m4", "chi_5")` em
`preconditions_d3`. Com o manifesto de χ₅ atual, a v3 registraria "V2 ausente no manifesto D3" e **não produziria
veredito** para nenhum bloco. Pelo §5 da declaração, a H-004 ficaria **não executada por bloqueio**.

Consequências, sem alterar nada do que foi declarado:

1. Este complemento satisfaz o §6 do adendo 2, mas **não basta** para executar a H-004. Falta a **V2′ de χ₅**, pelo
   mesmo procedimento já aplicado a χ₋₄ (`completude_d3.py --carater chi_5 --v2`).
2. Não se relaxa `CHECKS_REQUIRED` nem se substitui a V2 por outra verificação. Isso mudaria uma pré-condição depois
   de conhecido o custo e exigiria adendo próprio. Não é proposto aqui.
3. A V2′ de χ₋₄ terminou em 26/09/2026 12:32 e foi aprovada: 3.000 = 3.000, diferença máxima 5,8·10⁻¹⁰, 0
   recuperados na lista recomputada. Ela **acrescentou** V2 ao manifesto D3 de χ₋₄, cujo SHA-256 passou de
   `851a6c95…` (citado no §2 do adendo 2) para `edef331b14c432145d584714a323bd477341627ae560d6d1ffae1cd24062097f`. É a
   mudança esperada e não afeta a pré-condição 1, que compara `saida.sha256` (`81fdfc0a…`, inalterado) com o arquivo
   analisado.
4. **Custo previsto da V2′ de χ₅:** a V2′ de χ₋₄ gastou ≈ 21,3 h-CPU, e o D3 de χ₅ foi ≈ 2,2× mais lento por
   intervalo. A estimativa grosseira é de 40–50 h-CPU, acima do limiar de 4 h-CPU do `ADENDO_REGISTRO_v2_2` §2.
   Precisa de declaração de custo com teto antes de iniciar. É a única produção longa no caminho da H-004 e decorre
   de uma pré-condição já declarada, não de uma escolha nova.

*Dionatan Resende & Claude Opus — 26/09/2026.*
