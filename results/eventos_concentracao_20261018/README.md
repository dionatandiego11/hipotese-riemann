# Pares raros e colisões — 18/10/2026

Declaração anterior à implementação e aos cálculos, mas posterior ao desenvolvimento analítico em rascunho. Não é teste confirmatório de novidade.

Comando: `.venv/bin/python results/eventos_concentracao_20261018/verificar.py`.

Cinco testes novos passaram; CPU 4,701732183 s, parede 4,669306240 s. Teto 60 s de CPU no próprio processo. Quadraturas a 50 dígitos são controles B sem certificação intervalar; identidades de colisão foram verificadas em Fraction. `resultados.json` guarda os valores, `pytest.log` o relato, `manifesto.json` os hashes e a medição, `code/` as cópias consumidas.

Não há dados de zeros, simulação Monte Carlo, enumeração de órbitas, teste de RH/Collatz ou prova de novidade. As provas estão em `teorias/EVENTOS_RAROS_CUE_20261018.md` e `teorias/SYRACUSE_COLISOES_20261018.md`. Não são substituídas pelo resultado dos testes.

As verificações algébricas destes alvos estão encerradas. Próximos trabalhos: lei conjunta ponderada para uma transferência de pares; auditoria do antecedente bibliográfico de energia e eventual adaptação ao custo condicionado. Não ampliar K ou a grade ε como substituto dessas tarefas.
