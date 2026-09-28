# Busca de testes numéricos anteriores das Conjecturas 7 e 8 (MN-1/MN-2) — 27/09/2026

Objetivo: verificar se já existe cálculo numérico de Σ 1/|L′(ρ,χ)|² ou Σ |L(2ρ,χ²)/L′(ρ,χ)|² sobre zeros de funções L de
Dirichlet (ou teste numérico das constantes de Pearce-Crump). Feita **depois** dos resultados (não afeta vereditos).

| fonte | consulta | resultado |
|---|---|---|
| **MathSciNet** | busca por "negative discrete moments Dirichlet" | **inacessível**: redireciona a login institucional (LibLynx). Não consultado |
| **zbMATH Open** (API) | "negative moments" & "Dirichlet L-functions" | 4 documentos (Gao 2022, 2024; Florea 2024; Ng–Toma 2024): cotas e aplicações, sem cálculo numérico |
| zbMATH Open | "discrete moments" & (Dirichlet \| L-function) | 5 documentos; relevantes: Pearce-Crump 2026 (o próprio); Garunkštis–Grahl–Steuding 2011 (momentos de L(ρ,χ₂) nos zeros de outra L, quantidade diferente, sem numérica); Tongsomporn–Steuding 2019 (torções aditivas). Nenhum teste numérico |
| zbMATH Open | derivative & zeros & "Dirichlet L-function" & (numerical \| computation) | 1 documento (Haneke 1973, zeros reais), irrelevante |
| **arXiv** (API) | abs:"discrete moments" AND abs:Dirichlet | 3: Pearce-Crump 2026; Banks–Loftus 2026 (momento torcido, teórico); Bueno 2026 (usa cotas conjecturais) |
| arXiv | abs:"negative moments" AND (numerical \| computation) | 27 entradas, nenhuma sobre ζ′(ρ) ou L′(ρ,χ) |
| **Citações** do artigo (Semantic Scholar) | arXiv:2606.25094 | 0 citações indexadas; consultas posteriores bloqueadas por limite de taxa (HTTP 429) |
| **Citações de Gonek 1989** (OpenAlex W2158180956) | 78 trabalhos que o citam, filtrados por título e resumo | único numérico: **Hiary–Odlyzko 2011 (só ζ)**; os demais que mencionam Dirichlet/L-functions são teóricos (cotas, famílias, corpos de funções) |
| Citações (OpenAlex) da entrada identificada como Milinovich–Ng | 3 trabalhos | nenhum numérico |
| Tese do autor (2024) e artigo (2026) | busca textual | sem cálculo de L′(ρ,χ) |

## Conclusão

Não foi encontrado nenhum teste numérico anterior das Conjecturas 7 e 8 (nem do análogo de Dirichlet da conjectura de
Gonek). Para ζ, a conjectura de Gonek já foi verificada numericamente (Hiary–Odlyzko 2011).

**Limitações:** MathSciNet não consultado; Google Scholar não consultado; filtros por palavra-chave em título e resumo
podem perder resultados que só aparecem no texto completo; o artigo tem três meses e trabalhos em preparação não são
visíveis. O rótulo continua **C (novidade a investigar)**, agora com busca documentada. Passo seguinte natural: consulta
direta ao autor.
