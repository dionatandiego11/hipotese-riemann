# Catálogo O1 do `ctrl-estadio-v1` — órbitas periódicas do quarto de estádio (19/09/2026)

Calculado **antes** de qualquer nível do bilhar ser usado pelo instrumento (o único nível calculado até hoje é o do
teste de funcionamento em k = 100, que não entra). Cumpre P2 de [DECLARACAO_ESTADIO.md](DECLARACAO_ESTADIO.md)
(`c7ce5d5b…`). SHA-256 deste registro em `O1_CATALOGO_ORBITAS.sha256`. Classe B: a busca é numérica, e a completude não
está demonstrada.

**Artefatos:**
- `estadio/catalogo_o1.py` (`77c19ab4…`): o procedimento está escrito na docstring antes da execução;
- `estadio/catalogo_o1.csv` (`5a3eeead…`) e `estadio/catalogo_o1.json` (`03fc5e5d…`).
- Execução oficial: 2 sementes (20260919 e 20260920), 100·n² partidas por n e por g, n ≤ 8; 2.100 s.

## Resultado

| L | Tipo | Reflexões externas / colisões no quarto | Observação |
|---|---|---|---|
| **2** | família "bouncing ball" (m = 1) | 1 / 2 | três entradas no CSV: o interior da família (hessiana degenerada) e as duas bordas. A borda x = 1 fica na junção reta–arco, onde a curvatura salta e a hessiana numérica não vê a degenerescência; a borda x = 0 corre sobre o eixo (marcada "fronteira"). **Uma única linha** |
| **4** | órbita de fronteira sobre o eixo y = 0 (ida e volta 0 → 2) | 1 / 3 | coincide com a repetição m = 2 da família (P1): **só descritiva** |
| **4,472136** (= 2√5) | isolada, pelos cantos (0,1) e (2,0) | 2 / 4 | "losango" do estádio inteiro, dobrado |
| **4,828427** (= 2 + 2√2) | isolada | 2 / 5 | |
| **4,889432** | isolada | 3 / 5 | |
| **5,000000** | isolada | 3 / 5 | na borda da janela t ≤ 5 do instrumento |
| 5,014970; 5,061467; 5,066657; 5,090170; 5,092396; 5,105829 | isoladas, "rastejando" junto ao arco | 4–6 / 6–8 | fora da janela t ∈ [0,5; 5]; sequência que se acumula perto de 2 + π ≈ 5,142 |

**Nenhuma órbita com L < 5 além das listadas**, com a busca e as ressalvas abaixo. Não há órbita isolada entre 2 e
4,47: as órbitas curtas do estádio são a família bouncing ball e as órbitas pelos eixos.

## Estabilidade da busca

- Semente 1: 14 chaves. Semente 2: 13, todas contidas na semente 1. Uma chave só apareceu na semente 1. O catálogo é a
  união, como fixado no procedimento.
- **Conferência suplementar** (feita depois da execução oficial e registrada aqui; não muda o catálogo): uma terceira
  semente (20260921) com 10 vezes mais partidas (1.000·n²) para n ≤ 3 encontrou **exatamente** os mesmos seis
  comprimentos {2; 4; 4,472136; 4,828427; 4,889432; 5}. Essas são todas as órbitas do catálogo dentro da janela t ≤ 5.
- **Ressalva:** a busca por partidas aleatórias não garante completude para n entre 4 e 8. As órbitas encontradas com
  n ≥ 4 têm todas L > 5,01, fora da janela.

## Uso no controle (conforme a declaração)

- **E-C1:** linha L = 2.
- **E-C2bb:** amplitude de L = 2, com o C̄_bb da D1-E.
- **E-C1o:** detecções claras devem corresponder a {2; 4; 4,472136; 4,828427; 4,889432; 5} com a tolerância de m4-v3.
- **E-C4:** as linhas log n do catálogo de ζ a mais de 1 FWHM desses comprimentos.
- **Catálogo do ajuste dirigido:** {2, 4, 4,472136, 4,828427, 4,889432, 5}. Os pares 4,828/4,889 (separação 0,061)
  e 4,889/5,000 (0,111) ficam **não resolvidos** em todos os blocos (FWHM de 0,15 no g01 a 0,34 no g04) e são tratados pela regra de
  elegibilidade de m4-v3. As amplitudes de Gutzwiller dessas órbitas só entram como descritivas (E-C2o).
