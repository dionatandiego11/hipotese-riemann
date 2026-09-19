# H-004 (P-R1) — previsão do erro do estimador em outra função L — declaração (19/09/2026)

Categoria **T1-prospectivo** ([ADENDO_REGISTRO_v2_1.md](../ADENDO_REGISTRO_v2_1.md)): registrada **durante a aquisição e
antes de qualquer análise** dos zeros de Dirichlet dos blocos reservados. **Não equivale** a uma declaração anterior à
aquisição. SHA-256 em `DECLARACAO.sha256`. Preditor congelado: `preditor_pr1.py`, hash em `preditor_pr1.sha256`.

## 1. Pergunta

O mecanismo que produz os desvios do estimador do instrumento (ajuste dirigido `band_conjugate` de m4-v3) prevê, com
**sinal e tamanho**, os desvios Re Ĉ − c nos zeros de L(s, χ), sem nenhum ajuste aos desvios de teste?

**Mecanismo** (projeção de contribuições conhecidas no estimador): o ajuste dirigido aplicado ao sinal teórico
F_modelo, que tem
- todas as linhas da fórmula explícita de L(s, χ) com T ≤ 8, coeficientes c_χ(n) = −Λ(n)χ(n)/(π√n) (D1 do controle),
  inclusive as de **fora** do catálogo do ajuste (T > 5);
- os termos **conjugados**;
- o termo suave conhecido ∫w(θ′_χ/π − d̄_χ).

Isso prevê o erro de cada linha do catálogo do bloco. O que se transfere do desenvolvimento é **o mecanismo**, com as
fórmulas próprias de cada sistema, e **não** amplitudes do Maass.

## 2. Desenvolvimento (T0; já feito, não é teste)

`hipoteses/pr1_dev/`:

| Dados | Linhas | Fração explicada (corte 8) | Sinais |
|---|---|---|---|
| Maass S2 | 22 | SQ de 1,77 → 1,2·10⁻⁸ | 12/12 onde \|prev\| > 10⁻³ |
| Maass S1 | 21 | SQ de 3,7·10⁻² → 9·10⁻¹² | 7/7 |
| ζ, d01 de m4-v3, preditor congelado com ruído de tabela (3·10⁻⁹) | 11 selecionadas de 47 | **0,99998** | 11/11; resíduo mediano = 0,26 × ruído |

Com corte em 5,2 em vez de 8, o resíduo do Maass S2 fica em 1,4·10⁻²: a cauda de linhas fora do catálogo é o mecanismo
dominante onde as linhas se amontoam.

## 3. Dados e registro de acesso

**Reservados (T1-prospectivo):** blocos **e02, e03, e04** (zeros 3.001–12.000 de L(s, χ₋₄)) e **f02, f03, f04** (idem
para L(s, χ₅)), produzidos por `dirichlet_zeros.py` (script `65056bc2…`, Adendo 2) em
`results/etapa11_6_controles/dados/`.

**Fora da reserva:** e01 e f01 (zeros 1–3.000), porque contêm os 500 zeros do piloto. Ficam como exploração e controle.

**Acessos até esta declaração (agente):**
- **Piloto** (zeros 1–500 de cada caractere, `dados_piloto/`): lidos integralmente nas verificações V1–V4, na
  reavaliação de V4, na verificação de refinamento (±6·10⁻¹⁰) e no teste de regressão (25 primeiros zeros).
- **Arquivos de progresso** da aquisição completa (`dados/progresso_*.json`), que contêm a lista de zeros aceitos: lidos
  em 19/09 às ~13:48 e ~15:12 **só** para extrair fase, **número** de zeros, t corrente da varredura e data. Nenhum
  valor de zero com índice > 500 foi exibido, salvo ou usado em cálculo.
- **Nenhuma** transformada, ajuste ou métrica do instrumento foi calculado sobre zeros de Dirichlet.
- Usuário: não informado aqui; o usuário deve completar se tiver acessado algo.

## 4. Critérios (fixados agora)

**Informação permitida ao preditor:** caractere (q, κ, valores de χ), parâmetros do instrumento, bordas do bloco (A e B =
primeiro e último zero do bloco), a lista de ordenadas do bloco (só para o ruído de arredondamento) e o catálogo.
**Proibido:** os erros observados e qualquer saída do ajuste dos dados, exceto a leitura final de e_obs.

**Por bloco:**
- e_prev,k: pelo preditor;
- ruído_k: desvio-padrão da mudança de Re Ĉ_k sob 20 perturbações das ordenadas por U(±5·10⁻¹⁰), que é o arredondamento
  a 9 casas do arquivo de zeros;
- **seleção:** \|e_prev,k\| > 5·ruído_k. É a única seleção e não usa e_obs;
- e_obs,k = Re Ĉ_k − c_k, lido de `arithmetic_matches.csv` da execução do controle. Linhas com c = 0 entram com erro
  absoluto, sem divisão.

**Medida primária** (agregada nos 6 blocos, com z = erro/ruído):
EF = 1 − Σ(z_obs − z_prev)² / Σ z_obs² (fração explicada; o modelo de erro zero tem EF = 0), mais a concordância de
sinais S nas linhas selecionadas.

**Viabilidade** (`hipoteses/pr1_dev/viabilidade_dirichlet.py`, com níveis GUE substitutos e bordas nominais, antes dos
dados): 11 a 16 linhas selecionadas por bloco, cerca de 83 no total; ruído mediano ≈ 5·10⁻¹¹; erros previstos até
~2·10⁻⁷.

**Classificação:**
- **sucesso:** EF ≥ 0,9 **e** S ≥ 0,9 **e** EF ≥ 0,5 em pelo menos 5 dos 6 blocos;
- **falha:** EF < 0,5 **ou** S < 0,7;
- **inconclusivo:** o resto; ou menos de 30 linhas selecionadas no total; ou o controle tem V1–V4 reprovado ou a
  execução do instrumento falha.

O efeito mínimo relevante é o próprio limiar de sucesso: o modelo precisa explicar ≥ 90% do erro padronizado.

**Secundário (descritivo):** o mesmo EF para o modelo **sem** os termos conjugados, e os valores por bloco. e01 e f01 são
reportados como exploração.

**Dependência:** os 6 blocos são contíguos em dois espectros e **não** contam como 6 observações independentes. A decisão
usa o agregado, e a condição por bloco é exigência de consistência, não contagem de sucessos.

## 5. Ordem de execução (sem ajuste entre as etapas)

1. Terminar a aquisição (em curso) e as verificações V1–V4 do controle.
2. Rodar o instrumento do `ctrl-dirichlet-v1` nos 8 blocos, como declarado no controle.
3. Rodar `preditor_pr1.py` (hash congelado) sobre as saídas dos blocos e02–e04 e f02–f04 e gravar o resultado.
4. Avaliar o controle pelos critérios dele e o H-004 pelos critérios acima. Os resultados de um não mudam o procedimento
   do outro.

## 6. O que o resultado diria

- **Sucesso:** o erro sistemático do estimador é um objeto **previsível** a partir das fórmulas conhecidas, também numa
  função L em que o modelo não foi desenvolvido (rótulo **B**: previsão numérica confirmada). Não diz nada sobre RH ou
  GRH. **Não** é afirmação de novidade: a literatura de fórmulas explícitas com funções-teste (B1, B2) já trata de
  efeitos de truncamento; a comparação bibliográfica fica pendente.
- **Falha:** o mecanismo não transfere. Há algo nos dados de Dirichlet (ordenadas, densidade, termos omitidos) fora do
  modelo, e isso é registrado como resultado negativo.
- **Condição:** o modelo usa a fórmula explícita com zeros na reta crítica até a altura dos blocos (GRH nessa faixa, não
  demonstrada aqui) e a completude verificada por V1.
