# Adendo 1 a H-004 — execução fiel à declaração e limites de interpretação (19/09/2026)

Gravado **antes** de qualquer análise dos blocos reservados. Motivado pela revisão do usuário de 19/09/2026, que conferiu
os hashes da declaração (`82382c59…`), do adendo ao protocolo (`2afb657b…`) e do preditor v1 (`5eede5b6…`). A versão
original fica preservada; **este adendo prevalece** onde diverge. SHA-256 em `ADENDO_H004_1.sha256`.

**Os limiares de decisão não mudam** (EF ≥ 0,9, S ≥ 0,9, EF ≥ 0,5 em ≥ 5 de 6 blocos, falha se EF < 0,5 ou S < 0,7,
mínimo de 30 linhas). **A previsão não muda:** a v2 importa as funções de previsão da v1 e confere o hash dela.

## 1. A escala de arredondamento é análise de sensibilidade

As 20 perturbações U(±5·10⁻¹⁰) medem a **resposta do estimador a um modelo de arredondamento** das ordenadas a 9 casas.
Não demonstram que o erro verdadeiro das ordenadas seja independente e uniforme, nem incluem necessariamente o erro de
localização dos zeros (refinamento ≤ 10⁻¹⁰, V2 ≤ 9,3·10⁻¹¹ no piloto). Essa escala continua sendo usada **só** como
unidade operacional de seleção (\|e_prev\| > 5·ruído) e de ponderação (z = erro/ruído). Consequências:
- "resíduo do tamanho do ruído" quer dizer "do tamanho da resposta a esse modelo de arredondamento", nada mais;
- **EF alto não é significância estatística**: é a fração do erro padronizado explicada pelo modelo, na escala acima. O
  resultado de H-004 não vem acompanhado de valor-p.

## 2. Condições de inconclusão aplicadas pelo programa

`preditor_pr1_v2.py` (SHA-256 no fim) aplica, **antes** e **durante** a avaliação:

| Situação | Resultado |
|---|---|
| manifesto do cálculo com `all_checks_passed` falso (V1–V4) | **inconclusivo** |
| manifesto ou arquivo de zeros ausente; manifesto incompatível (n ≠ 12.000 ou hash do arquivo diferente) | **inconclusivo** (pré-condição) |
| saída do controle ausente num bloco; bordas A e B do controle diferentes do 1.º e do último zero do bloco (> 10⁻⁹); catálogo do controle diferente do catálogo c_χ | **inconclusivo** (pré-condição) |
| ruído ≤ 0 ou qualquer valor não finito (e_obs, e_prev, ruído) em qualquer bloco | **inconclusivo** |
| denominador de EF nulo ou não finito | **inconclusivo** |
| bloco sem linhas selecionadas | o EF do bloco fica indefinido e **conta como não atingir EF ≥ 0,5** |
| nenhuma linha selecionada no total, ou menos de 30 | **inconclusivo** |
| dependências diferentes das congeladas (§3) | **abortado**, sem veredito |

Nenhum desses casos pode produzir "sucesso" calculado parcialmente. As regras têm 8 testes com casos artificiais
(`test_preditor_v2.py`), sem dados reais.

## 3. Dependências congeladas

`dependencias_v2.json` registra o SHA-256 de **todo módulo carregado de dentro do repositório** pela avaliação:
- `preditor_pr1.py` (v1) e `preditor_pr1_v2.py`;
- `instrumento_chi.py` (`7b3ea056…`) e `dirichlet_zeros.py` (`65056bc2…`, o script do cálculo em curso);
- `riemann_spectra`: `__init__`, `arithmetic`, `controls`, `inverse_spectroscopy`, `periods`, `replication`,
  `unfolding` e `utils`.

A v2 recalcula esses hashes na execução e **aborta** se algum diferir. Uma correção posterior no controle, portanto, não
altera a previsão em silêncio: exigiria novo adendo.

## 4. Limites de interpretação (substituem a §6 da declaração nas frases indicadas)

- **"Completude verificada por V1"** passa a ler: V1 é **checagem de consistência** da contagem com N̄_χ (tolerância 3,
  sem estimar S(T, χ)), **não** certificação de completude. O modelo supõe a lista completa e os zeros na reta crítica
  na faixa dos blocos (GRH nessa faixa, não demonstrada aqui).
- **"Falha"** passa a ler: **este preditor**, com corte em T = 8, estes termos e este orçamento de precisão, não atingiu
  os critérios nos blocos reservados. Isso **não** permite concluir, isoladamente, que o mecanismo de vazamento não
  transfere: termos omitidos (linhas acima de 8, restos da fórmula explícita com janela de Hann) ou precisão
  insuficiente também explicariam o resultado. A falha é registrada como tal, e qualquer continuação é hipótese nova.
- **"Sucesso"** continua como rótulo B (previsão numérica confirmada neste estimador e nestes dados), sem afirmação de
  novidade e sem significância estatística.

## 5. Comando de avaliação (substitui o passo 3 da §5 da declaração)

```
.venv/bin/python3 results/registro_hipoteses/H-004/preditor_pr1_v2.py \
    --controle <pasta de saída do instrumento_chi com e02…f04> \
    --dados results/etapa11_6_controles/dados --saida <arquivo.json>
```

**Hashes:** `preditor_pr1_v2.py` `cc14e12f…`; `dependencias_v2.json` `9d2c749a…`; `test_preditor_v2.py` no commit.
