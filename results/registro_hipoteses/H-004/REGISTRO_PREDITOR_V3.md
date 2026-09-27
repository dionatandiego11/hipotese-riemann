# Registro do avaliador v3 — testes de equivalência e congelamento de dependências (25/09/2026)

Cumpre o §5 do [ADENDO_H004_2.md](ADENDO_H004_2.md) (`a5d071be…`), com os reforços pedidos na revisão do usuário de
25/09/2026: congelar as dependências **transitivas** e registrar que a equivalência foi medida com as duas versões
chegando à análise. SHA-256 deste registro em `REGISTRO_PREDITOR_V3.sha256`. **Nenhum dado real foi usado.**

## 1. Arquivos

| arquivo | SHA-256 |
|---|---|
| `preditor_pr1_v3.py` | `8fa78457551d9d1d267a43266b1a2bf8145103785249041fec232bc84e7a38a5` |
| `test_preditor_v3.py` | `0d2abfb82ddfbbf10a6a7edf05ccdf63658fa6ebe8483be68a1625cc191a5efa` |
| `dependencias_v3.json` | `235140a0e39a039186c1b4213d32a0f4404147514f6a59916a59d2818d1979f9` |

v1 (`5eede5b6…`) e v2 (`cc14e12f…`) ficam intactos.

## 2. O que a v3 muda, e o que não muda

A v3 **importa** a v2 com hash conferido e reaproveita os próprios objetos de análise (`classify`, `BLOCKS`, `SEEDS` e a
cadeia de previsão da v1). As únicas funções definidas nela são `_import_v2`, `extra_hashes`,
`current_dependencies`, `dependency_diff`, `dataset_files`, `preconditions_d3` e `main` — o teste verifica esse
conjunto exato. Previsão, ruído, seleção, limiares, medida primária e classificação continuam os da declaração
(`82382c59…`) e do adendo 1 (`6391eb1a…`).

## 3. Dependências congeladas

`dependencias_v3.json` tem duas seções, e a execução confere as duas, abortando com a lista de diferenças:

- **`modules` (13):** `preditor_pr1.py`, `preditor_pr1_v2.py`, `preditor_pr1_v3.py`,
  `dirichlet/dirichlet_zeros.py`, `dirichlet/instrumento_chi.py` e `src/riemann_spectra/` (`__init__`, `arithmetic`,
  `controls`, `inverse_spectroscopy`, `periods`, `replication`, `unfolding`, `utils`).
- **`arquivos` (5):** `ctrl_dirichlet_v1.toml` (`b51f78a1…`), `completude/completude_d3.py` (`3450b005…`) e os três
  avaliadores. Esta seção existe porque a varredura de módulos carregados não vê a configuração (não é `.py`) nem o
  código que **produziu** o conjunto de dados (não é importado pelo preditor). Conferir o hash da v2 sozinho não
  congelaria nada disso.

## 4. Testes

`8 passed, 2 warnings in 101,24 s` (os dois avisos são a divisão por zero conhecida em `ratio_to_theory` e
`phase_error_rad` das linhas sem amplitude prevista; ver a errata 2 do adendo v2_2, `9deef4f6…`).

1. **Identidade da análise:** v3 aponta para os objetos da v2 e define exatamente as sete funções do §2.
2. **Equivalência das seções `blocks`:** com zeros substitutos de conteúdo idêntico nos dois formatos de entrada
   (manifesto antigo com `all_checks_passed: true` e manifesto D3), as duas versões produzem a seção `blocks`
   idêntica na serialização ordenada. **A equivalência não é entre saídas bloqueadas:** o teste exige, nas duas
   versões, `preconditions_ok` verdadeiro **e** `notes` vazio, 12.000 zeros carregados, os quatro blocos de teste
   avaliados, `e_obs`, `e_prev` e `noise` não vazios e finitos com ruído positivo, `metrics` presente, e ao menos um
   bloco com linha selecionada — sem isso o teste falha com "equivalência sem análise efetiva".
   Os blocos são reduzidos por monkeypatch (2 de 300 níveis por caractere) só para o teste caber em segundos; os
   blocos declarados da H-004 seguem os da declaração.
3. **Rejeições da pré-condição:** SHA-256 que não corresponde ao manifesto; V2 reprovada; V2 ausente; certificado
   falso; bordas A/B diferentes das do arquivo analisado. Em todos, `preconditions_ok` falso com nota, sem veredito.
4. **Congelamento:** `arquivos` cobre os cinco caminhos com hash de 64 hexadecimais, a varredura inclui v1, v2 e o
   instrumento, `dependency_diff(dep, dep)` é vazio, e adulterar o hash do `.toml` produz exatamente uma diferença
   apontando esse arquivo.

## 5. Situação

A v3 está pronta e **não foi executada sobre dado algum do controle**. A execução depende, pela ordem autorizada:
validação dos dados corrigidos (V2′ de χ₋₄ e passe D3 de χ₅, em curso), complemento de identidade de χ₅
(`ADENDO_H004_2` §6), instrumento nos 8 blocos, e só então o preditor. Se qualquer pré-condição falhar, a H-004 fica
**não executada por bloqueio** — o que não é falha da hipótese.

*Dionatan Resende & Claude Opus — 25/09/2026.*
