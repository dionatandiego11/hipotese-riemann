# MN-3 — adendo 2: correção de χ₈ pelo passe de completude e conclusão de ζ (28/09/2026)

Gravado **antes** de qualquer análise da MN-3 e antes de qualquer derivada de χ₈. **Não altera** previsões nem
critérios de decisão (ficha §1 e §5). Decisão do usuário em 28/09: autorizar as duas extensões abaixo.

## 1. χ₈: lista reprovada em V2

A V2 recontou 2.002 zeros contra 2.000 na lista principal (`manifest_chi_8_2000.json`, `ed68096d…`): falta um par,
provavelmente de zeros próximos. É a mesma falha de χ₋₄/χ₅, corrigida lá pelo passe D3 (`ADENDO_DIRICHLET_3`,
`02340a5c…`).

**Procedimento** (`mn3_completude_chi8.py`): funções do `completude_d3.py` congelado (`3450b005…`), importadas sem
alteração.
- **Etapa A:** intervalos com s > 1,6 d̄, reexaminados com passo d̄/32, com checkpoint.
- **Certificado D3-C1** (janelas de 200 zeros; com 2.000 zeros há 10 janelas).
- **Etapa C** se o certificado falhar.

**Aceitação, fixada agora:**
1. a lista corrigida tem **exatamente 2.002 zeros** (igualdade de contagem com a V2; as posições da V2 não foram
   gravadas, então a comparação é só de contagem, e isso fica declarado como limitação);
2. certificado D3-C1 aprovado;
3. V1, V3 e V4 refeitas sobre a lista de trabalho, que são os 2.000 primeiros zeros da lista corrigida.

Se qualquer item falhar, χ₈ fica **não executado** na MN-3, sem nova tentativa automática.

**Derivadas:** `mn3_derivadas_d3.py`, idêntico a `mn3_derivadas.py` exceto a pasta de entrada (`mn3_zeros_d3/`) e a
exigência do manifesto da correção. Saídas com os mesmos nomes esperados pela análise congelada.

## 2. ζ

Concluir as derivadas dos zeros 26.301–27.000 e L(2ρ) dos 27.000 zeros, com os scripts já congelados.

## 3. Tetos (RLIMIT_CPU)

Correção de χ₈: 7.200 s. Derivadas de χ₈: 3.600 s. Derivadas de ζ: 1.800 s. L(2ρ) de ζ: 3.600 s.
Custo esperado ~2 h-CPU; total da MN-3 ≈ 23 h. Sem extensão automática.

## 4. Análise

`analise_mn3.py`, congelado e sem alteração, roda uma vez quando χ₁₂, χ₈ (se aceito) e ζ estiverem completos. Se χ₈
não for aceito, um adendo técnico restringe a execução a χ₁₂ sem mudar critério algum.
