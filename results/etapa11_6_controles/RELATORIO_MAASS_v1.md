# Relatório do `ctrl-maass-v1` (19/09/2026)

Execução válida: `maass/execucao_v3/`. Os manifestos têm os hashes de dados, catálogo, configuração e scripts:
`instrumento_maass.py` `fb8ac9f1…` e `ctrl_maass_v1.toml` `3d93e7b6…`. Houve duas execuções interrompidas antes, sem
nenhum resultado de linhas aberto: `execucao_v1_interrompida` e `execucao_v2_interrompida`, tratadas pelos adendos 3
e 4.

**Documentos do protocolo:**
- declaração `5db97004…`;
- D1-M `773a077b…`;
- adendos 1 (`4efb9020…`), 2 (`3a40cf7a…`), 3 (`0968e75b…`) e 4 (`5ac738d2…`);
- G1 `8705bd7f…`.

SHA-256 deste relatório em `RELATORIO_MAASS_v1.sha256`.

## 1. Resultado pelos critérios declarados: **NÃO PASSA**

| Bloco | M-C1 | M-C2s | M-C2a+ | M-C2a− | M-C4 | M-C4s |
|---|---|---|---|---|---|---|
| **S2 (primário, 751 formas)** | falha | falha | falha | falha | passa | passa |
| S1 (descritivo, 341 formas) | falha | falha | falha | falha | passa | passa |

**Por quê.**
- **Nenhuma linha de G1 é "claramente detectável"** pelo critério herdado de m4-v3. O z previsto vai de 0,17 a 0,66
  em S2 e de 0,39 a 1,27 em S1, contra 1,5 × (limiar ≈ 2,67).
- O **detector sem catálogo não detectou nenhum pico** em nenhum bloco.
- Sem linhas claramente detectáveis, o conjunto elegível de M-C2s e M-C2a± é **vazio**, e esses critérios falham por
  construção.
- M-C4 e M-C4s "passam", mas de forma **vazia**: não há detecção nenhuma.

**Pela regra de leitura 2 da declaração, o resultado é negativo e fica registrado.** Nenhum parâmetro será reajustado
para este protocolo.

## 2. O que a medição dirigida mostrou (observação **exploratória**, rótulo C; não decide o controle)

O estimador primário (`band_conjugate`, ajuste conjunto com o catálogo G1) foi calculado em todas as linhas, como sempre.
A razão Re Ĉ/c, com c da D1-M e do adendo 1:

| T | δ | c previsto | S1: razão | S2: razão | razão se fosse H_sinh (S1) |
|---|---|---|---|---|---|
| 0,9624 | −1 | −0,13700 | 1,000001 | 1,000000 | 0,447 |
| 1,7627 | −1 | −0,19838 | 0,999999 | 0,999993 | 0,707 |
| 1,9248 | +1 | +0,13700 | 1,000003 | 1,000001 | — |
| 2,3895 | −1 | −0,21096 | 0,999999 | 1,000009 | 0,832 |
| 2,6339 | +1 | +0,24203 | 1,000002 | 0,999976 | — |
| 2,8873 | −1 | −0,27401 | 0,999999 | 0,999990 | 0,894 |
| 3,1336 | +1 | +0,21766 | 1,000004 | 1,000100 | — |
| 3,2945 | −1 | −0,19473 | 1,000001 | 1,000006 | 0,928 |
| 3,5255 | +1 | +0,29757 | 0,999993 | 1,001303 | — |
| 3,6369 | −1 | −0,36608 | 1,000003 | 0,998832 | 0,949 |
| 3,8497 | +1 | +0,22834 | 0,999986 | 0,980599 | — |
| 3,9314 | −1 | −0,17190 | 1,000076 | 0,991032 | 0,962 |
| 4,1269 | +1 | +0,33918 | 1,000121 | 1,010356 | — |
| 4,1894 | −1 | −0,32343 | 0,999886 | 1,028944 | 0,970 |

- **Acima de T ≈ 4,3**, as razões degradam: até 1% em S1, e desvios grandes em S2, com sinal trocado em 4,81 e 4,98.
  Ali há pares δ = ±1 separados por 0,03 a 0,05, menos que a FWHM, e o catálogo corta em t = 5, com linhas logo acima
  (5,118 e 5,142) fora do ajuste.
- **Parte imaginária:** |Im Ĉ/c| ≲ 2·10⁻⁵ nas linhas da tabela, até T ≈ 3,7.
- **Escala do ruído dos nulos:** σ_c ≈ 0,35 (S1) e 0,8 (S2) por linha, cerca de **10⁵ vezes** o desvio observado. O
  nulo shuffle destrói a estrutura exata do espectro e superestima o resíduo real. É o mesmo fenômeno registrado no
  código congelado para os zeros de ζ ("|F_w| entre linhas é ordens de grandeza menor que as flutuações dos
  controles"). Os critérios baseados em detectabilidade, calibrados por esse nulo, ficam **cegos** para um sinal que o
  ajuste dirigido mede com 5 a 6 casas decimais.

**Leitura exploratória (rótulo C; não é conclusão do controle):**
- Nas linhas resolvidas pelo ajuste conjunto (T ≲ 4,2), os autovalores ímpares do LMFDB reproduzem, com erro relativo
  de 10⁻⁶ a 10⁻⁴, os coeficientes da fórmula de traço de Bolte–Grosche (2.31) na normalização da D1-M: classes de
  PSL(2, ℤ), peso ¼, sinal − e **cosh** para as reflexões com deslizamento, potências e quadrados de reflexões tratados
  como na D1-M.
- **H_sinh é incompatível** com as medidas: razões de 0,45 a 0,97, contra 1,000001.
- O resultado é coerente com a fórmula ser **exata**, como Bolte & Grosche afirmam, e com o instrumento medir o que a
  fórmula prevê.
- Isso **não** vira afirmação confirmada: a observação veio de dados que o protocolo não usava para decidir, e os
  critérios que decidiam falharam.

## 3. O que este resultado diz e não diz

- **Diz:** o desenho de critérios herdado de m4-v3 (detecção cega e elegibilidade por "clareza" medida contra o nulo
  shuffle) é **inadequado** para espectros que obedecem a uma fórmula de traço exata, quando o número de níveis é
  pequeno (341 a 751). O instrumento em si, o ajuste dirigido, não falhou.
- **Não diz:** nada sobre RH. Não confirma, pelo protocolo, que o instrumento mede corretamente sinais e amplitudes;
  a observação é exploratória. Não muda K5b M4.
- **Sobre m4-v3 (ζ):** lá havia linhas claramente detectáveis, porque os blocos tinham 3.000 zeros, com resolução e
  relação sinal/ruído muito maiores. O problema aparece aqui por causa do tamanho do espectro. Mas o mesmo fenômeno do
  nulo que superestima o ruído existe lá, e já estava registrado.

## 4. Caminhos para uma confirmação (a decidir; nenhum foi executado)

Uma versão confirmatória precisaria de:
1. critério de concordância do ajuste dirigido com **elegibilidade definida só pela geometria do catálogo** (linha
   resolvida pelo ajuste conjunto, com separação mínima fixada antes, sem depender da detecção cega), e tolerância
   fixada antes;
2. **dados que ainda não foram usados** (T1). Os autovalores ímpares deste arquivo agora são T0. Opções:
   - setor **par** do mesmo arquivo, ainda não transformado, mas que exige derivar os termos de espalhamento e
     Eisenstein (K5b, fato 2);
   - formas de Maass de outros grupos Γ₀(N) do LMFDB, que exigem um catálogo G1 próprio para cada grupo;
   - as faixas ímpares hoje ausentes do LMFDB, se forem completadas.
