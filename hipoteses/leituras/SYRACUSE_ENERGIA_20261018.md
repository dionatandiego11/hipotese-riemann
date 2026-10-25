# Leitura dirigida — energia quadrática de Syracuse

18/10/2026. Fonte primária: Lucas Valbuena, *Quadratic cylinder energy and integrability of the Syracuse law*, fonte TeX no repositório do autor.

- Commit consultado: `a7275d5a73814d3d9a400c6fe6577de9542b03a3`.
- URL: https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/quadratic-cylinder-energy.tex
- Cópia: `archive/fontes_etapa11/syracuse_energia_20261018/quadratic-cylinder-energy.tex`.
- SHA-256: `d8bc1905bdc833ce01fcfe21984096d5c8cf75bef10ebd93e4ec3e8804392df0`.
- Escopo efetivo: contexto/enunciado, linhas 60–115, e equação estacionária/obstrução L², linhas 409–493. Documento fonte, sem paginação renderizada nesta sessão.

O texto contém a mesma obstrução quadrática por sobreposição positiva dos ramos. Seu argumento usa igualdade dos suportes em medida, dispensando positividade em todas as unidades. Isso é antecedente direto; a derivação do projeto não será classificada como novidade. O enunciado também anuncia uma majorante quadrática da energia e integrabilidade abaixo de 2, que não foram auditadas aqui nem usadas como premissas. As verificações Lean anunciadas no repositório não foram executadas.

A cópia e o commit permitem conferir a comparação. A primeira consulta da API `commits/main` falhou por `IncompleteRead`; a consulta posterior de `git/ref/heads/main` e o download de `raw` funcionaram. Metadados completos em `fonte.json` junto à cópia. Não se tratou o rótulo de formalização como prova verificada por esta sessão.

**Decisão:** o alvo canônico L² tem antecedente identificado. Antes de tentar nova majorante, conferir a prova publicada pelo autor e só então definir uma extensão ao condicionamento de custos do projeto. Não declarar essa extensão inédita sem comparar as hipóteses e trabalhos pertinentes.

## Ampliação da leitura — 19/10/2026

Fonte arquivada reconferida pelo mesmo SHA, sem novo download ou mudança do original. Lidas as linhas 117–381 da cópia TeX: decodificação e contagem de fibras; energia por Cauchy–Schwarz; normalização da lei inclinada; momentos; interpolação L1/L2. Não foi encontrado erro nesses passos. A prova de energia sustenta E_K<=24K+8K². O pertencimento a Lp, 1<=p<2, usa a Proposição1.14 de Tao como entrada externa. Releitura da cópia v5 de Tao, pp.10–12: na p.11 a numeração é (1.23)–(1.24), distinta da versão citada por Valbuena. A normalização de oscilação coincide com a norma L1 de densidades de cilindros.

Esta é auditoria interna de manuscrito, sem certificação Lean ou alegação de revisão por pares. As declarações anteriores sobre trechos ainda não lidos descrevem a sessão de18/10. Agora a cota e a interpolação foram conferidas, não apenas seus enunciados.

A aplicação ao custo fixado foi escrita em [energia condicionada](../../teorias/SYRACUSE_ENERGIA_CONDICIONADA_20261019.md). Reutiliza a contagem de quocientes, conserva o indicador de custo no momento inclinado e obtém energia<=4/beta². A autoria/novidade dessa consequência não foi estabelecida por uma busca exaustiva. Não atribuir a extensão ao teorema de Tao nem à formalização anunciada pelo autor.
