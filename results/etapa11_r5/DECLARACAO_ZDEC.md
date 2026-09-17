# Decomposição da parcela dos zeros de B^{RH′} — declaração prévia (14/09/2026)

Gravada **antes** do cálculo. SHA-256 em `DECLARACAO_ZDEC.sha256`.

## Objeto
Decompor, **sem alterar nenhuma constante**, a majorante Z_ν do Lema 4 (§II.9.5), com os mesmos parâmetros de
`DECLARACAO_PRH2.md`: grade d₁ ∈ {1, 2, 4, 8}, Δ ∈ {0,5; 1; 2}, ε₀ = 0,1, t_max = 5, c₁ e c₂ de
`prh_forca_resumo.json`, 30 blocos, 47 linhas e ν ∈ {A, B}.

Z_ν/2 = P0 + P1a + P1b + P2 + P3, com:
- **P0** = n(ν)·L₀: janela central |γ − ν| ≤ 1 (j = 0);
- **P1a** = 21·(log(ν + 8) + log 3)·L₂: janelas adjacentes j = ±1 (1 < |γ − ν| ≤ 3);
- **P1b** = 21·(0,5·log(ν + 8) + 2√2 − log 3)·L₂: janelas |j| ≥ 2 com centro ≥ 5;
- **P2** = 3N₆/(ν − 6)²·L₂: centros em (−1, 5);
- **P3** = (2N₆/ν² + 5,25·(log(ν + 2) + 1)/(ν + 2))·L₂: parcela espelhada φ(γ + ν).

Soma: P1a + P1b = 21(1,5·log(ν + 8) + 2√2), idêntica ao Lema 4. É só repartição da mesma cota.

**Agrupamentos:**
- **próximos de ±ν** = P0 + P1a (|γ − ν| ≤ 3);
- **distantes** = P1b + P2 + P3;
- **por constante:** parte L₀ = P0; parte L₂ = P1a + P1b + P2 + P3.

## Aritmética
- Intervalar (mpmath.iv), com ‖a_k‖₁ em ponto flutuante (híbrida), como em PRH2.
- **Conferência:** a soma das partes, levada à escala (1/π)Σ_ν/|c_k|, deve reproduzir `zeros_rel_sup` de
  `prh2_forca_tabela.csv` dentro de 10⁻⁹ relativo.

## Registros
- **Por (bloco, linha, combinação):** cada parte relativa a |c_k| (sup) e sua fração na parcela dos zeros.
- **Resumo por combinação:** frações min/máx, com destaque para (8, 2) e para os pares elegíveis cujo orçamento excede 10⁻⁶.

## Regras de leitura
- As frações descrevem a **majorante**, não as somas reais sobre zeros.
- Nenhuma constante é escolhida, nem nenhum parâmetro é ajustado a partir desta decomposição ou dos erros observados de C2.
  A decomposição orienta **qual lema** refinar analiticamente.
- Grade, cortes e alvos inalterados. Nenhuma avaliação com zeros ou com dados de C2.

## Saídas
`zdec_calculo.py`, `zdec_tabela.csv`, `zdec_resumo.json`.
