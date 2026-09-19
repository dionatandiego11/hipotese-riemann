# Catálogo G1 do `ctrl-maass-v1` — linhas previstas pela fórmula de traço (19/09/2026)

Calculado **antes** de qualquer transformada dos autovalores de Maass, pelo procedimento de P3 da declaração, corrigido
pelo [ADENDO_MAASS_1.md](ADENDO_MAASS_1.md) (`4efb9020…`) e pela [D1-M](D1M_DERIVACAO_MAASS.md) (`773a077b…`).
Aritmética inteira exata. SHA-256 deste registro em `G1_CATALOGO_GEODESICAS.sha256`.

**Artefatos (pasta `maass/`):**
- `catalogo_g1.py` (`e3b36810…`): o procedimento está na docstring;
- `catalogo_g1_classes.csv` (`2653d56e…`): uma linha por classe de conjugação de PSL(2, ℤ), com forma representante,
  conteúdo, potência, raiz e coeficiente;
- `catalogo_g1_linhas.csv` (`9f7ecadb…`): uma linha por comprimento, com o coeficiente somado;
- `catalogo_g1.json` (`6cba3e44…`): conferências dos dois algoritmos.

## Conferências

- **Dois algoritmos independentes** (ciclos de formas reduzidas de Gauss; componentes pelos geradores S e T numa caixa
  crescente) **concordam em todos os 24 discriminantes**, e cada ciclo cabe numa única componente.
- **Conferência obrigatória do adendo:** as classes com (n, δ) = (1, −1), (2, −1) e (3, +1) são únicas, com
  discriminantes 5, 8 e 5. Os coeficientes coincidem com a D1-M §3: −0,137003; −0,198379; +0,137003.
- **Contagens conhecidas de classes estreitas**, conferidas: D = 5 → 1; D = 12 → 2; D = 21 → 2; D = 32 → 3 (duas
  primitivas e uma imprimitiva, 2·(x² − 2y²)).
- **Potências**, confirmadas por multiplicação de matrizes:
  - δ = −1, traço 4: cubo da reflexão de traço 1 (traços de ρ, ρ³, ρ⁵ = 1, 4, 11);
  - δ = −1, traço 11: quinta potência da mesma reflexão;
  - δ = +1, traço 7: quadrado da classe de traço 3.
- **Quadrados de reflexões com deslizamento** aparecem como classes hiperbólicas **primitivas em PSL(2, ℤ)**, como em
  Bolte & Steiner (p. 5): traço 3 = ρ² de traço 1, e a classe (−2, 4, 2) de traço 6 = ρ² de traço 2.

## Linhas na janela t ∈ [0,5; 5] (coeficientes na convenção do instrumento)

| l | δ | traço | classes | c da linha |
|---|---|---|---|---|
| 0,962424 | −1 | 1 | 1 | −0,137003 |
| 1,762747 | −1 | 2 | 1 | −0,198379 |
| 1,924847 | +1 | 3 | 1 | +0,137003 |
| 2,389526 | −1 | 3 | 1 | −0,210955 |
| 2,633916 | +1 | 4 | 2 | +0,242026 |
| 2,887271 | −1 | 4 | 2 | −0,274007 |
| 3,133598 | +1 | 5 | 2 | +0,217663 |
| 3,294462 | −1 | 5 | 1 | −0,194731 |
| 3,525494 | +1 | 6 | 3 | +0,297568 |
| 3,636893 | −1 | 6 | 2 | −0,366084 |
| 3,849695 | +1 | 7 | 3 | +0,228339 |
| 3,931441 | −1 | 7 | 1 | −0,171895 |
| 4,126874 | +1 | 8 | 4 | +0,339176 |
| 4,189425 | −1 | 8 | 2 | −0,323430 |
| 4,369288 | +1 | 9 | 2 | +0,158495 |
| 4,418695 | −1 | 9 | 2 | −0,305116 |
| 4,584863 | +1 | 10 | 6 | +0,446850 |
| 4,624877 | −1 | 10 | 2 | −0,288711 |
| 4,779053 | +1 | 11 | 3 | +0,210955 |
| 4,812118 | −1 | 11 | 2 | −0,164404 |
| 4,955777 | +1 | 12 | 4 | +0,266642 |
| 4,983560 | −1 | 12 | 4 | −0,521578 |

Acima de t = 5 (fora da janela): 5,117958 (+, traço 13) e 5,141629 (−, traço 13).

## Leitura para o controle (informativa; os critérios são os da declaração e do adendo)

- **Linhas mais bem isoladas:** as quatro primeiras e a de 2,634. Com a FWHM do bloco H (≈ 0,072), as vizinhas estão a
  mais de 0,16.
- **A partir de ~3,5:** os pares δ = +1/δ = −1 do mesmo traço se aproximam como ≈ 4/n² e têm **sinais opostos**:
  - 3,525/3,637 (0,111) e 3,850/3,931 (0,082) ficam resolvidos no bloco H;
  - 4,127/4,189 (0,063), 4,369/4,419 (0,049), 4,585/4,625 (0,040), 4,779/4,812 (0,033) e 4,956/4,984 (0,028) **não**
    ficam resolvidos, e há cancelamento parcial entre as duas linhas de cada par.
  A regra de elegibilidade de m4-v3 e M-C2s tratam isso: M-C2s exclui coincidências de sinais opostos a menos de 1
  FWHM.
- **Ordem de grandeza:** |c| ≈ 0,14–0,52, contra a densidade média d̄ ≈ R/12 ≈ 1–15 no bloco. A razão relativa cai
  com R; o ruído efetivo só se conhece nos dados.
