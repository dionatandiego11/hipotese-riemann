# Fechamento dos filtros — execução de 12/10/2026

A pasta conserva a data de criação da declaração (11/10); o piloto foi executado em 12/10.

Conclusão matemática e provas: [nota](../../hipoteses/COLLATZ_FILTROS_FECHAMENTO_20261012.md).

- `DECLARACAO.md` e `.sha256`: anteriores à implementação.
- `configuracao.json`: parâmetros resolvidos da declaração.
- `verificar.py`: controle exato com limite de CPU real de 60 s; verifica o hash da declaração.
- `resultados.json`, `periodos.csv`, `verificacao.log`: saídas da execução completa pequena, estado `validado`.
- `code/`: cópias do código usado.
- `manifesto.json`: hashes, fonte primária já arquivada e locks CL0 reconferidos.

Reprodução a partir da raiz do projeto:

```bash
sha256sum -c results/collatz_filtros_20261011/DECLARACAO.sha256
.venv/bin/python -m pytest -q collatz/test_congruence_filters.py
.venv/bin/python results/collatz_filtros_20261011/verificar.py
```

O último comando regenera as saídas; para preservar a execução original, copie o diretório antes. Tempos variam, identidades e contagens exatas devem coincidir. Não é experimento confirmatório, enumeração extensa, execução CL1 ou afirmação de novidade. O controle não lê dados de zeros nem requer rede.

Os resultados conhecidos foram formulados antes do piloto: implementação conferida com composição literal em frações e contagem independente por iteração direta. O período mínimo 3^m também foi provado para todas as profundidades, não apenas observado até m=7.
