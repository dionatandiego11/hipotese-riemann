# Controles de Hamiltoniano e Collatz — 22/11/2026

Declaração e SHA anteriores à implementação. Comando usado: `.venv/bin/python results/hamiltoniano_collatz_20261122/executar.py`. Código científico em `src/riemann_spectra/prime_trace_kernel.py` e `collatz/periodic_denominator.py`; cópias em `code/`, hashes em `manifesto.json`.

Três testes passaram: resto trivial contra série com cauda, pontos racionais contra iteração/paridades, e separação aritmética no período2. Grade fixa1–8;1.020 pontos dos dois mapas. CPU0,982002s e parede1,108816s. `resultados.json` preserva soma ponderada exata, filtro positivo inteiro e matriz de Gram float por seus autovalores. O filtro não estabelece a conjectura de Collatz; o diagnóstico PSD não é prova nem certificação global.

Primeira chamada falhou no import do pacote collatz, antes de qualquer cálculo; corrigido caminho do runner, sem mudar método ou declaração. Nenhum zero foi lido, nem experimento de ajuste feito. Interpretação e limitações em `docs/ATAQUE_OPERADOR_PESO_ARITMETICO_20261122.md`. Reexecutar código modificado requer outra pasta, preservando esta rodada.
