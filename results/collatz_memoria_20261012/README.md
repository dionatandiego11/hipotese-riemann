# Memória finita de Collatz — 12/10/2026

Nota com provas e limites: [COLLATZ_MEMORIA_FINITA](../../hipoteses/COLLATZ_MEMORIA_FINITA_20261012.md).

O sistema finito conserva exatamente as médias de contagem em classes módulo 3^K. Não é um quociente determinístico do mapa de Collatz, nem simulação de paridades de órbitas positivas. O erro forte das densidades não foi certificado.

```bash
sha256sum -c results/collatz_memoria_20261012/DECLARACAO.sha256
.venv/bin/python -m pytest -q collatz/test_coarse_memory.py
.venv/bin/python results/collatz_memoria_20261012/verificar.py
```

`DECLARACAO.md` foi hasheada antes da implementação e do controle. `resultados.json`, `mistura.csv` e `verificacao.log` contêm a execução completa dos níveis declarados; `configuracao.json` resolve seus parâmetros; `code/` preserva cópias dos módulos e executor; `manifesto.json` registra hashes e a fonte já arquivada.

A reexecução regenera resultados e tempos; preserve uma cópia caso queira guardar a execução original. Todas as massas, cotas binomiais e probabilidades estacionárias saem como strings de frações exatas. CPU/parede usam ponto flutuante por serem medições de custo.
