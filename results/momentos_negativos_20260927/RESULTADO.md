# MN-1 — resultado (27/09/2026)

Ficha: `hipoteses/FICHA_MOMENTOS_NEGATIVOS.md` (`d31515d1…`), congelada às 11:07 com o código de análise, **antes**
do cálculo de qualquer derivada. Hashes conferidos antes da análise (`sha256sum -c`: todos SUCESSO).

## Veredito pelos critérios da ficha (sem alteração)

| | R medido | IC 95% (bootstrap de blocos) | PC (Conj. 7) | H0 (sem fator) | HE (fatores de Euler) | veredito | frágil? |
|---|---|---|---|---|---|---|---|
| **χ₋₄** (primária) | **0,655** | 0,592–0,715 | **2/3** ✓ | 1 ✗ | 4/3 ✗ | **Conjectura 7 favorecida** | não (sem os 5 maiores: 0,633) |
| χ₅ (secundária) | **0,827** | 0,753–0,901 | **5/6** ✓ | 1 ✗ | 25/24 ✗ | **Conjectura 7 favorecida** | não (0,794) |

R = média de v = log(qγ/2π)/|L′(ρ,χ)|² sobre os zeros 1–3.000 de L(s,χ), dividida pela média de v nos zeros de ζ
com a mesma distribuição de densidade local.

## Descritivo

- **ζ, rumo à conjectura de Gonek (6/π² para v):** razão média(v)/A₁ = 0,912 (zeros 1–3.000), 0,963 (3.001–10.000) e
  **0,992** (10.001–20.000). A convergência com a altura é visível.
- **Razão absoluta de χ:** média(v)/A_q = 0,932 (χ₋₄) e 0,937 (χ₅), na mesma faixa que ζ em alturas comparáveis.
  É consistente com um viés de altura finita comum, que o teste diferencial cancela.
- **Cauda pesada:** o 1% maior dos termos responde por 12–14% da soma em χ e por 11–23% em ζ.

## Custo

Derivadas: ζ 5.805 s, χ₋₄ 1.269 s, χ₅ 2.037 s de CPU (2,5 h no total; tetos de 3 h, 1,5 h e 1,5 h). Análise: 8 s.

## Rótulos, limites e novidade

- **B:** reprodução numérica da convergência para a constante de Gonek em ζ (zeros 1–20.000).
- **Conjectura 7 (fator aritmético ∏_{p|q} p/(p+1)):** evidência numérica favorável em dois caracteres, com
  exclusão das alternativas H0 e HE. Numa busca breve, não se encontrou teste numérico anterior (o artigo de origem,
  de 23/06/2026, não traz nenhum). **Rótulo C (novidade a investigar)**; uma busca breve não estabelece novidade.
- **Limites:**
  - alturas baixas (γ ≤ 2.900);
  - dois caracteres reais de condutor pequeno;
  - a referência ζ é a mesma para os dois testes;
  - o bootstrap pode subcobrir com cauda pesada (mitigado pela checagem de fragilidade);
  - o teste diferencial supõe que o viés de altura finita é comum a ζ e χ na mesma densidade.
- **Extensões naturais:** mais caracteres (inclusive complexos e de condutor composto, em que ∏_{p|q} tem mais
  fatores); alturas maiores; a Conjectura 8 (Σ \|L(2ρ,χ²)/L′(ρ,χ)\|²), com os mesmos dados.
- Nada aqui é evidência sobre GRH.

## Adendo 1 — busca bibliográfica ampliada (27/09/2026, depois do resultado)

- **ζ:** Hiary e Odlyzko (2011, B25) já confirmaram numericamente a conjectura de Gonek (J₋₁) em alturas de 10¹⁶ a
  10²³. A calibração ζ desta MN-1 é **B** (reprodução em alturas baixas), sem novidade.
- **L(s, χ):** nem o artigo de origem (jun/2026) nem a tese do autor (2024, B26) trazem cálculo numérico de L′(ρ,χ);
  buscas dirigidas não acharam outro teste. O rótulo **C (novidade a investigar)** do teste da Conjectura 7 se mantém.
  Ainda não é afirmação de novidade: faltam consulta a bases (MathSciNet/zbMATH), a citações do artigo e,
  idealmente, ao próprio autor.

## Adendo 2 — busca formal (27/09/2026)

Registro completo em `BUSCA_NOVIDADE.md`: zbMATH Open, arXiv, citações de Gonek 1989 (78, via OpenAlex) e do artigo.
Nenhum teste numérico anterior das Conjecturas 7 e 8 foi encontrado; MathSciNet ficou inacessível (assinatura).
Rótulo mantido: **C**, com busca documentada.
