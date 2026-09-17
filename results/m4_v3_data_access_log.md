# Registro de acesso aos zeros 70.001–100.000 (m4-v3)

| Data/hora (local) | Ação | Dados tocados | Finalidade |
|---|---|---|---|
| 13/09/2026 18:31 | `data fetch --config configs/data_first100000.toml` | leitura de `data/raw/zeros1` até 100.000; finitude, ordenação, espaçamentos mín/máx; `zeros_100k.csv` | auditoria de dados, antes do congelamento |
| 13/09/2026 18:31 | `data validate` | 20 índices estratificados até 100.000 recalculados com mpmath | auditoria de precisão, antes do congelamento |
| 13/09/2026 18:31 | leitura de γ₇₀₀₀₁ e γ₁₀₀₀₀₀ | 2 valores | altura e N_eff para o pré-registro |
| 13/09/2026 19:08 | congelamento m4-v3 (locks de pacote e do plano) | nenhum dado novo | — |
| 13/09/2026 19:09 | primária Hann: m3 --config configs/m4_v3.toml | zeros 70.001–100.000 | análise pré-registrada (C1, C2) |
| 13/09/2026 20:21 | primária BH: m3 --config configs/m4_v3_bh.toml | zeros 70.001–100.000 | robustez pré-registrada |
| 13/09/2026 21:08 | primária M2+CUE: run --config configs/m4_v3_m2.toml | zeros 70.001–100.000 | C3 e análise secundária CUE |
| 13/09/2026 22:07 | **pausa a pedido do usuário**: M2+CUE interrompido após 4 de 10 blocos (d01–d04; métricas parciais apenas no log); reprodução independente e comparação não iniciadas | zeros 70.001–100.000 (blocos d01–d04 no M2) | execução pausada; nenhum resultado M2 gravado; pasta renomeada para `results/run_20260914_000844_m2_m4_v3_m2_INTERROMPIDA` |
| 13/09/2026 22:20 | execução pelo usuário (retomada): M2+CUE `run_20260914_012016_m2_m4_v3_m2`, reprodução independente (d01–d10), `compare_m4v3.py` | zeros 70.001–100.000 | etapas congeladas; resultado da comparação: R2 acionada (S4 fora em d05, d09, d10) |
| 14/09/2026 | investigação de R2: leitura de `results/m4_v3_independent/*/arrays.npz`, `summary.json`, `nulls.npz` e `block_metrics.json` da primária | somente artefatos já gerados; nenhuma nova computação sobre os zeros | diagnóstico pré-conclusão (M4V3_PLAN §5) |
