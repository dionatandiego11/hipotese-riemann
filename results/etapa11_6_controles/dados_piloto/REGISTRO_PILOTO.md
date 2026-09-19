# Piloto do `ctrl-dirichlet-v1` (500 zeros por caractere) — registro (19/09/2026)

O usuário executou os pilotos com o script original (SHA-256 `0f16b4c5…`, preservado em
`../dirichlet/versoes/dirichlet_zeros_0f16b4c5.py`). A V4 foi refeita pelo agente segundo o Adendo 1
([ADENDO_DIRICHLET_1.md](../ADENDO_DIRICHLET_1.md), SHA-256 `6ee78368…`), com o script `7b2de8e2…`, **sem recalcular os
zeros**. Os manifestos originais não foram alterados.

## Verificações

| | χ₋₄ | χ₅ |
|---|---|---|
| zeros | 500, γ₁ = 6,0209489, γ₅₀₀ = 628,8248333 | 500, γ₁ = 6,6484533, γ₅₀₀ = 606,4413632 |
| arquivo de zeros (SHA-256) | `aab50218…` | `aa201a07…` |
| V1 (\|N − θ/π\| ≤ 3) | 0,246 ✓ | 0,241 ✓ |
| V1, reamostragem de lacunas | nenhuma | nenhuma |
| V2 (passo pela metade) | mesma contagem; máx. \|Δγ\| = 9,3·10⁻¹¹ ✓ | mesma contagem; máx. \|Δγ\| = 9,3·10⁻¹¹ ✓ |
| V3 (50 zeros, 2 avaliações) | 50/50 ✓ | 50/50 ✓ |
| V4, regra original | **falhou** (ponto sobre o último zero: 8,8·10⁻²⁰) | **falhou** (ponto sobre o último zero: 1,95·10⁻¹⁹) |
| V4, Adendo 1 (`v4_adendo1_*.json`) | ✓ máx. 1,1·10⁻²⁸; mín. \|Z\| = 0,049 | ✓ máx. 4,6·10⁻²⁹; mín. \|Z\| = 0,76 |
| **V1–V4 com o Adendo 1** | **aprovado** | **aprovado** |

## Custo medido

| | χ₋₄ | χ₅ |
|---|---|---|
| 500 zeros | 796 s (12.879 avaliações; 25,8 por zero) | 1.583 s (12.803 avaliações) |
| V2 (500 zeros com passo pela metade) | 1.031 s | 2.087 s |
| custo médio por avaliação no piloto (t ≤ 630) | 0,062 s | 0,124 s |

**Tempo de uma avaliação de Z_χ em função da altura** (medido pelo agente em 19/09/2026 com 3 avaliações por ponto, na
mesma máquina, incluindo o aquecimento de cache; por isso acima da média do piloto):

| t | χ₋₄ | χ₅ |
|---|---|---|
| 600 | 0,17 s | 0,29 s |
| 2.000 | 0,38 s | 0,59 s |
| 5.000 | 0,59 s | 0,78 s |
| T₁₂₀₀₀ (9.750 / 9.507) | 0,96 s | 1,79 s |

**Estimativa para o cálculo completo** (12.000 zeros, V2 no bloco 9.001–12.000): cerca de 3,1·10⁵ avaliações na
varredura, mais cerca de 1·10⁵ na V2. A calibração pelo piloto (medido ÷ piloto ≈ 2,4–2,7 em t = 600) dá **cerca de 20 a
35 horas para χ₋₄ e 35 a 55 horas para χ₅**, com os dois rodando em paralelo em núcleos separados. É uma ordem de grandeza,
não uma medida. O script não grava pontos de retomada: uma interrupção perde o cálculo em curso.

**Nota posterior (19/09/2026):** o benchmark do Adendo 2 (`BENCHMARK.md`), medido com os dois caracteres em paralelo,
dá **~53 h para χ₋₄ e ~108 h para χ₅** e substitui a estimativa acima. A falta de retomada foi resolvida pelo Adendo 2.
