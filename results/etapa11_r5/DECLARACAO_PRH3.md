# Avaliação isolada do Lema 4′ — declaração prévia (15/09/2026)

Gravada **antes** do cálculo. SHA-256 em `DECLARACAO_PRH3.sha256`.

## Objeto
Medir o efeito do **Lema 4′** (§II.15.2), sozinho, sobre a cota P-RH com Lema 5′ e sobre o orçamento de S2-ratio′(U₂):

B^{RH″}_{χ,k} := (1/π)·Σ_{ν∈{A,B}} ½·[Z′_ν + 2·Pol′_ν + Arq],

com:
- Pol′_ν e Arq idênticos a PRH2 (`DECLARACAO_PRH2.md`);
- Z′_ν do Lema 4′, com J := min{j ≥ 1 : (2j − 1)² ≥ L₂/L₀}, e L₂/L₀ decidido pelo extremo superior do intervalo;
- orçamento″ := B^{RH″}/|c_k| + |Θ_k(U₂)|/|c_k|, com Θ_k de `theta_tabela.csv` (classe B).

**Sem Lema C.** Nenhuma outra constante é alterada.

## Universo (inalterado)
- Grade d₁ ∈ {1, 2, 4, 8}, Δ ∈ {0,5; 1; 2}; ε₀ = 0,1; t_max = 5; c₁ e c₂ de `prh_forca_resumo.json`.
- 30 blocos e 47 linhas.
- ‖a_k‖₁ de `prh2_forca_tabela.csv` (coluna a_l1, ponto flutuante).

## Aritmética
Intervalar (mpmath.iv, 30 dígitos), com exportação arredondada para fora. Avaliação **híbrida** (normas por SVD em ponto
flutuante; Θ_k em B).

## Conferências (tolerâncias fixadas pela granularidade das exportações)
1. **Lema 4 recalculado no script:** Z_ν recalculado com as fórmulas de PRH2. Os valores zeros_rel e B_rel recalculados
   devem ficar abaixo das colunas `zeros_rel_sup` e `B_rel_sup` de `prh2_forca_tabela.csv` por no máximo 3·10⁻¹²
   (absoluto: 12 casas decimais mais uma unidade de margem).
2. **Z′_ν ≤ Z_ν** em todos os registros (extremos superiores, ambos calculados no script).

Falha em qualquer conferência é registrada como falha e interrompe a leitura dos resultados.

## Registros por (bloco, linha, combinação)
J, zeros_rel_sup (Lema 4′), razão Z′/Z, polos_rel_sup, arq_rel_sup, B″_rel_sup, |Θ_k|/|c_k|, orçamento″, orçamento
anterior (PRH2 + Θ) e elegibilidade (descritiva).

## Resumos
- **Por combinação:** J; faixa da razão Z′/Z; max, min e mediana do orçamento″; número de pares com orçamento″ ≤ 10⁻⁶
  (todas; elegíveis), comparado ao anterior.
- **Por par:** melhor combinação da grade, descritiva.

## Regras de leitura (fixadas agora)
- Mede o efeito de uma melhoria **já derivada**. Não é escolha de parâmetros nem busca de pares abaixo da tolerância.
- Orçamento ≤ 10⁻⁶ é resultado **híbrido e condicional a RH** (F5 e J1 bibliográficas). **Não** certifica S2-ratio′:
  faltam cotas rigorosas das normas do estimador por SVD e dos cálculos finitos (Θ_k).
- Orçamento > 10⁻⁶ não refuta S2-ratio′ nem exclui compensação.
- O melhor valor da grade é o melhor entre as combinações declaradas, não um ótimo.
- A grade não é ampliada.

## Saídas
`prh3_calculo.py`, `prh3_tabela.csv`, `prh3_resumo.json`.
