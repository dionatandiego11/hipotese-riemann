# MN-3 — resultado: Conjecturas 7 e 8 em χ₈ e χ₁₂ (28/09/2026)

Ficha `hipoteses/FICHA_MOMENTOS_NEGATIVOS_MN3.md` (`57720029…`), congelada em 27/09 às 23:07, antes de qualquer
cálculo; adendos 1 (retomada com teto novo) e 2 (correção de χ₈ e conclusão de ζ), gravados antes da análise. Todos
os hashes conferidos antes de rodar `analise_mn3.py` (congelado, sem alteração).

## Dados

- **χ₁₂:** zeros 1–2.000, **V1–V4 aprovadas** na primeira passagem.
- **χ₈:** a lista principal reprovou na V2 (2.002 contra 2.000). O passe de completude recuperou **exatamente 2 zeros**,
  o par próximo 1.470,227 / 1.470,279, e a lista corrigida tem 2.002, igual à V2. Certificado D3-C1, V1, V3 e V4
  aprovados. Trabalho com os 2.000 primeiros.
- **ζ:** zeros 1–27.000 (densidade máxima 8,23, acima das de χ₈, 7,77, e de χ₁₂, 8,12).

## Veredito pelos critérios da ficha

| | medido | IC 95% | previsto | H0 (1) | outra alternativa | veredito |
|---|---|---|---|---|---|---|
| **χ₁₂, Conj. 7** (primária) | **0,501** | 0,445–0,555 | **1/2** ✓ | ✗ | HE 3/2 ✗ | **favorecida** |
| **χ₁₂, Conj. 8** (primária) | **0,340** | 0,301–0,381 | **1/3** ✓ | ✗ | H7 1/2 ✗ | **favorecida** |
| χ₈, Conj. 7 | 0,687 | 0,605–0,784 | 2/3 ✓ | ✗ | HE 4/3 ✗ | **favorecida** |
| χ₈, Conj. 8 | 0,558 | 0,450–0,684 | 1/2 ✓ | ✗ | H7 2/3 ✓ | **favorecida** (sem separar de H7) |

**Descritivo (χ₈ contra χ₋₄):** a Conj. 7 dá 0,687 [0,605; 0,784] em χ₈ e 0,655 [0,592; 0,715] em χ₋₄; a Conj. 8 dá
0,558 [0,450; 0,684] em χ₈ e 0,490 [0,430; 0,549] em χ₋₄. Os ICs se sobrepõem, como previsto (mesmo fator, paridades
opostas).

## Leitura

- **χ₁₂ era o teste mais exigente**, com o produto sobre dois primos (2 e 3). As duas previsões acertam no centro:
  0,501 contra 0,500 e 0,340 contra 0,333. As alternativas mais próximas ficam excluídas, incluindo a troca dos fatores
  entre as conjecturas (1/2 para a Conj. 8).
- Somando MN-1 a MN-3: **4 caracteres (q = 4, 5, 8, 12), 8 testes, 8 favoráveis**. Em 6 deles a segunda alternativa
  também fica excluída. Em 2 (Conj. 8 em q = 4 e q = 12) essa alternativa é o fator trocado, o da Conj. 7. *(Corrigido
  em 28/09: a versão anterior dizia "em 3 deles o fator trocado", o que estava errado.)*

## Rótulos e limites

- **C (novidade a investigar)**, com busca documentada (`BUSCA_NOVIDADE.md`).
- **Limites:**
  - alturas baixas (γ ≤ 2.650);
  - 2.000–3.000 zeros por caractere;
  - só caracteres reais;
  - referência ζ comum;
  - bootstrap com cauda pesada;
  - teste diferencial (supõe viés de altura finita comum).
- **Custo total da MN-3:** ~23 h-CPU, contra ~12 h estimadas; uma interrupção abrupta da máquina (causa não
  confirmada). Nada aqui é evidência sobre GRH.
