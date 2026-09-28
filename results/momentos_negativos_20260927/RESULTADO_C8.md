# MN-2 — resultado: Conjectura 8 de Pearce-Crump (27/09/2026)

Ficha: `hipoteses/FICHA_MOMENTOS_NEGATIVOS_C8.md` (`d96f1f0d…`), congelada antes do cálculo de L(2ρ,χ²). Hashes
conferidos antes da análise (todos SUCESSO). Dados: `L2rho_*.txt`, `analise_c8.json`.

## Veredito pelos critérios da ficha

| | R₈ medido | IC 95% | C8: φ(q)/q | H0 | H7 (fator da Conj. 7) | veredito |
|---|---|---|---|---|---|---|
| **χ₋₄** (primária) | **0,490** | 0,430–0,549 | **1/2** ✓ | 1 ✗ | 2/3 ✗ | **Conjectura 8 favorecida**; H7 excluída |
| χ₅ | 0,753 | 0,673–0,835 | 4/5 ✓ | 1 ✗ | 5/6 ✓ | **favorecida**; C8 e H7 indistinguíveis (previsto na ficha) |

## Descritivo ζ (conjectura de Ng: média de w → 1)

Média de w: 0,927 (zeros 1–3.000), 0,948 (3.001–10.000), 0,934 (10.001–20.000). Na faixa estudada fica ~6% abaixo de
1, sem convergência visível; é o viés de altura finita que o teste diferencial cancela.

## Leitura conjunta com a MN-1

As duas conjecturas de Pearce-Crump passam no teste diferencial nos dois caracteres. Em χ₋₄, os dados distinguem os
**dois fatores aritméticos diferentes**: ∏ p/(p+1) = 2/3 para a Conjectura 7 e φ(q)/q = 1/2 para a Conjectura 8. Cada
momento exige o seu fator, e as alternativas trocadas ficam fora do IC.

## Rótulos e limites

- **C (novidade a investigar):** não se achou teste numérico anterior (ver adendo 1 de `RESULTADO.md`).
- Limites iguais aos da MN-1: alturas baixas, dois caracteres reais, referência ζ comum, bootstrap com cauda pesada.
- Custo: ~30 min de CPU. Nada aqui é evidência sobre GRH.
