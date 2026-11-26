# Núcleo da versão condensada GRH Lean

Data: 26/11/2026. Fonte primária: [lsernau/grh-lean](https://github.com/lsernau/grh-lean), revisão `72fead102f663d5c7a407964a13dc0cf9d977207`, igual à ponta de `main` consultada nesta data. Esta é uma leitura dirigida dos arquivos indicados abaixo; não executamos Lean nem auditamos a cadeia completa de dependências.

## Enunciados

[`grh-compact/src/Statements.lean`](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/Statements.lean) importa Mathlib e define, entre outros, que para cada módulo natural não nulo e cada caráter de Dirichlet complexo, a função L não se anula em Re(s) > 1/2, com exceção de s = 1 para o caráter principal; e que seus zeros com 0 < Re(s) < 1 estão na linha crítica. A leitura matemática depende das definições de Mathlib, não apenas dos nomes das declarações.

[`src/Main.lean`](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/Main.lean) deriva os cinco resultados expostos de `New.grh` e de lemas de simetria. O caso de ζ decorre de `New.zeta_zeros_on_line New.grh`. Esta é a dependência no código final; não demonstra que nenhuma prova alternativa possa começar apenas por ζ.

O [README da edição compacta](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/README.md) relata verificações pelo kernel, Comparator e apenas três axiomas padrão. Relata também que nenhum matemático leu toda a prova. Essas afirmações pertencem aos autores e não foram reproduzidas aqui. O projeto usa Lean v4.35.0 e Mathlib `56a005855ea17e0b0958f73ec801ae140b0a1679`; os autores estimam 1–2 h em 12 núcleos e 24 GB para compilar. Não iniciamos compilação.

## Peça escolhida: `star_inequality`

Em [`New/Main.lean`, linhas 23–130](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Main.lean#L23), o enunciado para dados admissíveis `D : Data P` é

`D.m * D.remainder ≤ D.logB ^ 2 * D.budget`.

O comentário descreve `remainder` como uma combinação de somas de primos menos seus termos esperados, `m` como número de passos da cadeia e `budget` como uma unidade de erro. A desigualdade resulta da comparação de estimativas para um mesmo covolume. Em termos esquemáticos, para dimensão positiva `d`, as entradas dão uma estimativa inferior e uma superior, respectivamente com os termos principais `d·h_main` e `d·(h_main − m·remainder)`, mais erros. A comparação cancela `d·h_main`; depois divide-se pela dimensão positiva. A prova também contabiliza as dimensões que não foram preenchidas e o custo do índice. O limite final usa as desigualdades de escala agrupadas em `D.le_of_hasLogBound`.

Esse resumo algébrico explica a montagem, não prova as entradas profundas. O arquivo cita `exists_family_covolumeSq_le`, `integral_forms_long`, as condições de posto e cotas de escala; a interpretação e a prova dessas entradas precisam ser conferidas nos respectivos módulos. Em particular, uma estimativa média de Gram sozinha não fornece a cota inferior de covolume usada aqui.

O passo seguinte, `eventually_primeError_le_rpow` (linhas 131–151), escolhe uma escala auxiliar em uma janela e combina a desigualdade com outras entradas. A afirmação é eventual: uma cota para todos os x suficientemente grandes, não uma verificação numa lista finita. `New.grh` (linhas 152–172) usa esse resultado e um critério de não anulação; os detalhes e quantificadores pertencem aos arquivos importados.

## Aplicação possível ao projeto

**Proposta, não resultado do repositório:** procurar, para uma família explícita de operadores de ramos de Collatz, um mesmo funcional com cota superior e inferior, que permita cancelar um termo dominante e deixar um erro controlável uniformemente no número de composições. Antes de reivindicar qualquer aplicação, definir o espaço, o operador, o funcional, as hipóteses e a dependência nas palavras de ramos. Um contraexemplo finito ou uma perda de controle é um resultado informativo.

Isto não constrói função L, Hamiltoniano ou equivalência com ζ. A revisão da viabilidade desse programa ainda está pendente. A seleção deste trecho é motivada pela arquitetura, sem afirmação de novidade bibliográfica.
