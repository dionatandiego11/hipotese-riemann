# Análise de poder dos controles da 11.6 com níveis sintéticos (19/09/2026)

Feita **antes** de existirem os zeros completos de L(s, χ) (o cálculo está em andamento e nenhum zero foi lido) e antes de
qualquer nível do estádio. Motivo: no `ctrl-maass-v1`, os critérios herdados de m4-v3 ficaram inalcançáveis, com nenhuma
linha "claramente detectável", e isso só apareceu depois de rodar nos dados (RELATORIO_MAASS_v1.md). SHA-256 em
`ANALISE_PODER_11_6.sha256`.

**Artefatos:** `poder/analise_poder.py` (`04b9afaf…`) e `poder/analise_poder.json` (`bfabcd9a…`).

## 1. Método

O critério "claramente detectável" de m4-v3 compara |c| com o ruído σ(t) do **nulo shuffle**. Esse ruído depende da
distribuição dos espaçamentos, da densidade e da faixa do bloco, e tudo isso se conhece antes dos dados. Para cada bloco:
1. gerar níveis substitutos: GUE (Dirichlet), GOE (estádio, β-Hermite tridiagonal de Dumitriu–Edelman com β = 1) ou
   Poisson (Maass), com a densidade do controle;
2. aplicar o nulo shuffle: 200 realizações para σ(t) e 999 para o limiar;
3. calcular z_prev = |c|·W(0)/(2σ(T)) para cada linha do catálogo;
4. contar como "clara" a linha com z ≥ 1,5 × limiar, e como "resolvida" a que tem a vizinha a ≥ 2 FWHM (aproximação da
   separação calibrada, que foi 2,00 FWHM em S1 e S2 do Maass).

## 2. Validação em casos já conhecidos

| Caso | Previsto | Observado |
|---|---|---|
| ζ, bloco d01 de m4-v3 (Hann; `run_20260913_220906`) | 13 linhas claras; z máx 7,88; limiar 3,34 | 15 linhas claras; z máx 8,40 |
| Maass S2 (`execucao_v3`) | z máx 0,57; 0 claras | z máx 0,66; 0 claras |
| Maass S1 | z máx 1,09; 0 claras | z máx 1,27; 0 claras |

O método reproduz a ordem de grandeza e a contagem, com diferenças de ~10–15% no z. **Serve para desenho de protocolo**,
não para cálculo exato.

## 3. Previsões

**`ctrl-dirichlet-v1`** (blocos de 3.000 zeros; GUE):

| Bloco | FWHM | Limiar | Linhas claras e resolvidas | com χ = −1 (D-C2s) | χ = 0 resolvidas (D-C2z) | z máx |
|---|---|---|---|---|---|---|
| e01 | 0,0044 | 3,37 | 14 | 8 | 6 | 10,4 |
| e02 | 0,0052 | 3,28 | 14 | 8 | 6 | 9,1 |
| e03 | 0,0055 | 3,33 | 13 | 7 | 6 | 8,7 |
| e04 | 0,0057 | 3,30 | 13 | 7 | 6 | 8,4 |
| f01 | 0,0045 | 3,37 | 16 | 10 | 3 | 10,0 |
| f02 | 0,0054 | 3,29 | 14 | 9 | 3 | 8,8 |
| f03 | 0,0057 | 3,33 | 13 | 8 | 3 | 8,4 |
| f04 | 0,0059 | 3,30 | 13 | 8 | 3 | 8,2 |

**Conclusão:** todos os critérios D-C* têm conjuntos elegíveis não vazios e poder comparável ao de m4-v3. **Nenhuma
mudança** no `ctrl-dirichlet-v1`.

**`ctrl-estadio-v1`** (GOE; |C̄_bb| da D1-E):

| Bloco | FWHM | Limiar | z previsto da linha L = 2 | Clara? |
|---|---|---|---|---|
| g01 | 0,150 | 2,72 | 2,17 | não (abaixo até do limiar) |
| g02 | 0,232 | 2,64 | 1,80 | não |
| g03 | 0,290 | 2,64 | 1,57 | não |
| g04 | 0,338 | 2,60 | 1,55 | não |
| g01+g02 (7.000 níveis) | 0,091 | 2,91 | 3,14 | não |
| **bloco único (12.000 níveis)** | 0,0575 | 2,97 | **3,84** | não (acima do limiar, abaixo de 1,5 × limiar) |

**Conclusões para o estádio:**
1. **E-C1** (detecção cega de L = 2 em **todos** os 4 blocos) é **praticamente inalcançável** como declarado: z previsto
   de 1,55 a 2,17, contra limiar ≈ 2,65. No bloco único, z ≈ 3,84 > 2,97, e a detecção é provável, mas sem folga.
2. **E-C2bb** (|Ĉ/C̄_bb − 1| ≤ 0,10): pelo modelo de ruído do nulo, o erro relativo por bloco é 1/z ≈ 46–64% (26% no bloco
   único), e o critério passaria só se o resíduo real fosse muito menor que o do nulo. No Maass, onde a fórmula de traço é
   exata, foi ~10⁵ vezes menor. No estádio a fórmula é assintótica, e **não se sabe**. O resultado de E-C2bb é, portanto,
   informativo **nos dois sentidos**, e o critério fica como declarado.
3. A correção de E-C1 vai no ADENDO_ESTADIO_1, antes de qualquer nível.
