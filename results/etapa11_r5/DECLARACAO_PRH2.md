# P-RH com Lema 5′ — declaração prévia da reavaliação (14/09/2026)

Gravada **antes** do cálculo. SHA-256 em `DECLARACAO_PRH2.sha256`.

- **Mudança única em relação a `DECLARACAO_PRH.md`:** Pol_ν é substituído por Pol′_ν (Lema 5′,
  `docs/ETAPA11_3B_H1_CAUDA_PROJETADA.md` §II.11). Zeros e termo arquimediano não mudam.
- **Mesmos parâmetros:** corte ϕ; c₁ e c₂ dos enclosures já obtidos (c₁ ≤ 2,000982, c₂ ≤ 9,854620, lidos de
  `prh_forca_resumo.json`); grade d₁ ∈ {1, 2, 4, 8}, Δ ∈ {0,5; 1; 2}; ε₀ = 0,1; 30 blocos; 47 linhas; t_max = 5.
- **Natureza:** avaliação **híbrida**. ‖a_k‖₁ vem de SVD em ponto flutuante (não certificada) e a aritmética da cota é
  intervalar. Relatar "pares com majorante calculada abaixo de 10⁻⁶", não "certificados".
- **Regra de leitura:** acima de 10⁻⁶, "essa cota não certifica a tolerância"; não é refutação de S2-ratio′ nem de C2.
  O menor valor na grade é só o melhor entre as combinações declaradas, não um ótimo.
- **Saídas:** `prh2_forca.py`, `prh2_forca_tabela.csv` e `prh2_forca_resumo.json`, com a mesma estrutura de parcelas
  (zeros, polos′, arquimediano) normalizadas por |c_k|, todas as combinações, o mínimo sobre a grade por par e o resumo
  por grupo (todas; elegíveis, descritivo).
