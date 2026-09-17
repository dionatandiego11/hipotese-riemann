# Relatório consolidado — espectroscopia inversa dos primeiros 100.000 zeros da zeta

**Estado deste documento:** completo para as faixas m4-v1, m4-v2 e m4-v3. Os valores de m4-v3 (§5, §9) vêm das execuções
congeladas e da comparação com a reprodução independente, e foram emitidos após a investigação da regra R2.

Classificação das afirmações (AGENTS.md):
- **A** — conhecido matematicamente, com hipóteses;
- **B** — reproduzido numericamente aqui;
- **C** — achado experimental com novidade investigada;
- **D** — conjectura ou heurística.

## 1. Pergunta e desenho

O projeto mediu quanta estrutura aritmética e estatística pode ser recuperada de listas finitas de zeros não
triviais de ζ, tratadas como "níveis de energia". A pergunta subjacente é se esses níveis poderiam ser o espectro de
um operador ou de uma dinâmica caótica (Hilbert–Pólya; Berry–Keating). O projeto **não** assume a Hipótese de
Riemann e não tenta demonstrá-la.

Instrumentos, todos pré-registrados e congelados por hash:
- **Transformada F_w(t)** das ordenadas, com janela de Hann e subtração da densidade média de Riemann–von Mangoldt;
- **Detector de linhas sem catálogo de primos**, com limiar FWER calibrado por nulo de permutação de espaçamentos e
  três categorias (detectada, inconclusiva, não detectada);
- **Comparação aritmética posterior**: matching um a um com r·log p, escore global com nulo independente e medição
  direcionada dos coeficientes contra −log p/(π p^{r/2});
- **Estatística local**: CDF de espaçamentos, R₂ e form factor conectado, com envelopes GUE finitos e de Poisson
  em testes de posto simétricos;
- **Análises secundárias**: janela Blackman–Harris (robustez) e correção CUE de Bogomolny et al. (2006).

## 2. Trajetória, defeitos e correções (resumo verificável)

| Fase | Resultado principal | Defeitos encontrados e tratamento |
|---|---|---|
| M1–M3 v1 | Invalidada | Aliasing na quadratura, FWHM errada, GUE mal normalizado, ruído estimado nos zeros, relatórios com afirmações fixas (PROTOCOLO §7) |
| m3-v2/v3 | Primeiros 10.000 zeros (todos já consultados) | Assimetria entre estatística de decisão e nulos; reuso de nulos; janela não propagada; teste de envelope não simétrico (auditoria do usuário; PROTOCOLO §8) |
| m4-v1 | 10.001–40.000, protocolo pré-registrado | — |
| m4-v2 | 40.001–70.000, mesmo código e regras | — |
| Auditoria independente | 3 blocos já analisados | 4 verificações fora da tolerância mantidas como falhas: FWHM por `brentq`, condição de malha, interpolação CUE. Em m4-v3 o ensaio prévio revelou arredondamento na quadratura; ver AUDITORIA §4, §9, §10 |
| m4-v3 | 70.001–100.000, primária + reprodução | Três correções numéricas antes do acesso (FWHM, CUE, quadratura em coordenadas locais); R2 acionada por erro de desenho do plano (S4), investigada (§5.2) |

## 3. O que foi estabelecido nos primeiros 70.000 zeros (antes da faixa final)

### 3.1 Recuperação de frequências aritméticas (C1) — **B**

Nas faixas m4-v1 e m4-v2 (20 blocos de 3.000 zeros, protocolos congelados antes da análise):
- o detector, sem receber primos, encontrou 32–35 linhas por bloco, todas com correspondência r·log p;
- nenhum bloco teve detecção sem correspondência no catálogo;
- p(S) ficou no piso de 10⁻⁴ em todos os blocos;
- a recuperação entre as linhas claramente detectáveis foi 1,000;
- C1 foi replicado em 10/10 blocos nas duas faixas.

### 3.2 Concordância de coeficientes (C2) — **B**

Com os períodos conhecidos (medição direcionada, não cega):
- as linhas elegíveis (14–16 por bloco) têm |razão − 1| ≤ 2,6·10⁻⁹ ante a tolerância de 10⁻⁶;
- as fases concordam com o sinal negativo de referência (Q = 1,000, p no piso do controle de fase);
- a dependência de janela e estimador chega a ~10⁻⁶ nas linhas fracas.

A precisão não é limitada só pela tabela de zeros (AUDITORIA §7).

### 3.3 Estatística local (C3) — **B**

- CDF de espaçamentos e K_c: incompatíveis com Poisson e com o GUE finito de 3.000 níveis em todos os blocos.
- R₂: não rejeitado em 19 de 20 blocos.
- Variância de espaçamentos: 0,158–0,163, abaixo do envelope GUE e crescendo lentamente com a altura.

A correção CUE de altura finita reduz a distância à CDF empírica, mas com N_eff ≈ 1,7–2,1 fica fora do domínio
validado na fonte e superestima a redução de variância. Fica como **D/secundária**, sem ajuste.

### 3.4 Linhas junto ao limiar — inconclusivas

- log 127 e log 131 alternam entre detectada, inconclusiva e não detectada conforme o bloco, a realização Monte
  Carlo e a implementação. O z previsto delas fica junto ao limiar.
- O comportamento acompanha a detectabilidade prevista pelo instrumento. Não há evidência de mudança nos coeficientes.
- 5² e a elegibilidade de p = 47 e p = 53 mudam de forma análoga.

### 3.5 Auditoria por implementação independente

Em três blocos já analisados, uma implementação escrita a partir da especificação, com caminhos numéricos
diferentes, obteve:
- razões ao teórico idênticas a ≤ 3,3·10⁻¹¹;
- F idêntico a ≤ 6·10⁻⁹ na mesma malha;
- estatísticas M2 idênticas a ≤ 7·10⁻¹¹;
- controles compatíveis dentro das incertezas.

Limites: mesmo autor, especificação, dados e bibliotecas; comparação não cega.

## 4. Implementação, dados e reprodutibilidade

- **Dados:** tabela de Odlyzko `zeros1` (100.000 ordenadas, erro declarado ≤ 3·10⁻⁹), SHA-256 conferido; validação
  mpmath por amostras estratificadas em cada conjunto (máx. 2,74·10⁻⁹); manifestos por `dataset_id`.
- **Código:** hashes de pacote em cada lock; cópias integrais em `archive/` e em `results/<run>/code/`.
- **Testes:** 58 aprovados no congelamento de m4-v3.
- **Execuções e comandos:** `docs/ANDAMENTO.md`, `docs/PROTOCOLO.md` §9–§11 e `README.md`.

## 5. Faixa final 70.001–100.000 (m4-v3)

Protocolo congelado antes da análise (PROTOCOLO §11). A implementação primária é `src/riemann_spectra` m4-v3; a
reprodução é `independent/riemann_indep` v2 (`independent/M4V3_PLAN.md`). Alturas 54.512–74.921, N_eff 2,09–2,16.
Execuções e acessos: PROTOCOLO §11.6 e `results/m4_v3_data_access_log.md`.

### 5.1 Resultados da primária

| Bloco | Detecções | Inconclusivas | Sem corresp. | p(S) | Claras / recuperação | Elegíveis C2 / fração ≤ 10⁻⁶ | Máx abs(razão−1) elegíveis | Q | C1 | C2 | BH detecções | Var(s) | p GUE: CDF / R₂ / K_c |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| d01 | 32 | 1 (127) | 0 | 1·10⁻⁴ | 15 / 1,000 | 15 / 1,000 | 2,2·10⁻⁹ | 1,000 | passa | passa | 25 | 0,1613 | 0,001 / 0,300 / 0,001 |
| d02 | 32 | 0 | 0 | 1·10⁻⁴ | 15 / 1,000 | 15 / 1,000 | 9,6·10⁻¹⁰ | 1,000 | passa | passa | 26 | 0,1627 | 0,001 / 0,852 / 0,001 |
| d03 | 32 | 0 | 0 | 1·10⁻⁴ | 15 / 1,000 | 15 / 1,000 | 1,9·10⁻⁹ | 1,000 | passa | passa | 26 | 0,1628 | 0,001 / 0,200 / 0,001 |
| d04 | 32 | 1 (127) | 0 | 1·10⁻⁴ | 15 / 1,000 | 15 / 1,000 | 1,5·10⁻⁹ | 1,000 | passa | passa | 25 | 0,1632 | 0,001 / 0,941 / 0,001 |
| d05 | 33 | 0 | 0 | 1·10⁻⁴ | 15 / 1,000 | 15 / 1,000 | 1,4·10⁻⁹ | 1,000 | passa | passa | 26 | 0,1621 | 0,001 / 0,390 / 0,001 |
| d06 | 32 | 1 (127) | 0 | 1·10⁻⁴ | 15 / 1,000 | 15 / 1,000 | 1,3·10⁻⁹ | 1,000 | passa | passa | 26 | 0,1634 | 0,001 / 0,715 / 0,001 |
| d07 | 33 | 1 (131) | 0 | 1·10⁻⁴ | 15 / 1,000 | 15 / 1,000 | 7,4·10⁻¹⁰ | 1,000 | passa | passa | 26 | 0,1638 | 0,001 / 0,626 / 0,001 |
| d08 | 32 | 1 (127) | 0 | 1·10⁻⁴ | 15 / 1,000 | 15 / 1,000 | 2,2·10⁻⁹ | 1,000 | passa | passa | 26 | 0,1622 | 0,002 / 0,051 / 0,043 |
| d09 | 33 | 0 | 0 | 1·10⁻⁴ | 15 / 1,000 | 15 / 1,000 | 1,4·10⁻⁹ | 1,000 | passa | passa | 26 | 0,1629 | 0,001 / 0,776 / 0,001 |
| d10 | 32 | 0 | 0 | 1·10⁻⁴ | 15 / 1,000 | 15 / 1,000 | 1,8·10⁻⁹ | 1,000 | passa | passa | 26 | 0,1638 | 0,002 / 0,775 / 0,002 |

- **C1 (recuperação de frequências): replicado em 10/10 blocos.** Nenhum bloco com detecção sem correspondência no
  catálogo. As mesmas 32 linhas são detectadas nos 10 blocos. log 127 é detectada em 3, inconclusiva em 4 e não
  detectada em 3; log 131 é inconclusiva em 1 bloco e não detectada nos demais. p(S) está no piso de resolução.
- **C2 (concordância de coeficientes): replicado em 10/10 blocos.** Máximo entre elegíveis ≤ 2,2·10⁻⁹. Fora do critério,
  nas 47 linhas, uma linha fraca chega a 2,8·10⁻⁶ (d10). Q = 1,000, com p(Q) no piso do controle de fase.
- **C3 (estatística local), Holm entre blocos:**
  - GUE finito: CDF rejeitada em 10/10, R₂ em 0/10, K_c em 10/10;
  - Poisson: rejeitado em 10/10 nas três estatísticas;
  - a rejeição de K_c em d08 é limítrofe (p = 0,043, ajustado 0,043);
  - Var(s) = 0,161–0,164, ainda abaixo do envelope GUE e crescendo lentamente com a altura.
- **Robustez Blackman–Harris:** 25–26 detecções por bloco; C1 e C2 também replicados em 10/10.
- **Secundária CUE** (N_eff ≈ 2,1–2,2, fora do domínio validado; sem ajuste):
  - a predição corrigida fica mais próxima da CDF empírica que o limite (RMS 0,0047–0,0056 contra 0,0070–0,0079);
  - ainda assim, a distância é 1,6–1,9 vezes o ruído amostral;
  - a variância predita, 0,151–0,153, continua ≈ 0,01 abaixo da medida.

### 5.2 Reprodução independente e regras de interrupção

| Verificação | Resultado |
|---|---|
| Determinísticas D1–D9, mesmas coordenadas (10 blocos) | todas dentro da tolerância. Máximos: dt rel 3,3·10⁻¹⁶; termo suave 1,5·10⁻¹⁰; F 7,5·10⁻¹⁰; F em T_k 3,2·10⁻¹¹; razões 7,7·10⁻¹³; M2 2·10⁻¹⁵; CDF CUE predita 1,3·10⁻⁸ |
| Estatísticas S1–S13 | dentro da tolerância, exceto **S4 em d05, d09 e d10** |
| Vereditos de família (reprodução) | C1 10/10 replicado; C2 10/10 replicado; C3: rejeições idênticas às da primária nos seis pares |
| Diferenças de status de linha | 14 casos, **todos em linhas não claramente decididas** (127, 131, 137, 139, junto ao limiar) |
| **R1** discrepância determinística | não acionada |
| **R2** mesmo código S em ≥ 3 blocos | **acionada** (S4) |
| **R3** mudança de conclusão C1/C2 | não acionada |
| **R4** mudança em C3 | não acionada |

**Investigação de R2** (`results/m4_v3_joint/INVESTIGACAO_R2.md`, só com artefatos já gerados):
- a causa é um **erro de desenho do plano**: S4 centrava a faixa em α = 0,05, mas a regra estrita de três categorias
  implica fração esperada (B+1−u)/(B+1) = 0,0405 para a reprodução;
- as médias observadas (reprodução 0,0401; primária 0,0443, com esperado 0,0458) seguem o desenho;
- a probabilidade de ≥ 3 falhas em 10 blocos sob o desenho correto é 0,20 **supondo blocos independentes**. Blocos contíguos não têm independência garantida, então esse valor é indicativo. A simulação por bloco já reestima o limiar em cada réplica; a correção futura de S4 deve incorporar essa variabilidade na própria faixa de tolerância, e não só centrá-la em (B+1−u)/(B+1);
- não há indício de divergência entre as implementações;
- **R2 permanece registrada como acionada.** A conclusão conjunta abaixo é emitida após a investigação, com essa ressalva.

### 5.3 Conclusão conjunta (após investigação de R2)

Na faixa final, as conclusões pré-registradas da primária (C1 e C2 replicados; C3 com as mesmas rejeições das faixas
anteriores) são reproduzidas por uma segunda implementação. Grandezas determinísticas concordam a ≤ 10⁻⁹ e as
decisões divergem apenas junto ao limiar. Isso **não** é uma segunda confirmação estatística independente: são os
mesmos zeros, o mesmo autor e a mesma especificação.

## 6. Recuperar estrutura aritmética não é reconstruir uma dinâmica ou um operador

O que os dados sustentam (**B**): as ordenadas carregam, de forma recuperável sem catálogo, as frequências r·log p,
com coeficientes e sinais da forma distribucional da fórmula explícita. Carregam também uma estatística local distinta
de Poisson e próxima, mas não igual, à de matrizes GUE de tamanho finito.

O que isso **não** estabelece:

1. **Nenhuma dinâmica foi reconstruída.** Não se obtiveram espaço de fases, hamiltoniano clássico, trajetórias,
   matrizes de monodromia, expoentes de Lyapunov nem índices de Maslov. A analogia "primo ↔ órbita periódica
   primitiva, r ↔ repetição" é uma correspondência formal entre fórmulas de traço. As diferenças conhecidas (sinal
   das repetições, amplitudes log p/p^{r/2} em vez de fatores de estabilidade semiclássicos) são discutidas por
   Berry e Keating e não foram resolvidas aqui.
2. **Nenhum operador foi identificado.** Uma lista finita de autovalores é compatível com infinitos operadores
   (por exemplo, matrizes diagonais ou unitariamente equivalentes). Recuperar frequências e coeficientes restringe
   uma fórmula de traço, não seleciona domínio, condições de contorno ou auto-adjunticidade.
3. **A estrutura recuperada não é independente dos primos.** A fórmula explícita já relaciona zeros e primos (**A**,
   com hipóteses a enunciar). Recuperá-la numericamente mostra a consistência dos dados e do instrumento, não uma
   nova ponte.
4. **Nada disso diz respeito à Hipótese de Riemann.** Os zeros analisados já estavam na linha crítica por verificação
   numérica. A realidade de ordenadas finitas não exclui zeros fora da linha em outras alturas, e uma construção de
   Hilbert–Pólya exigiria operador auto-adjunto definido de forma não circular, com espectro igual a todos os zeros.
5. **Réplicas não são independentes.** Blocos contíguos compartilham o mesmo espectro determinístico, e duas
   implementações sobre os mesmos dados não são duas confirmações estatísticas.

## 7. Limitações gerais

- Faixa de alturas baixa (E ≲ 7,5·10⁴) comparada aos estudos clássicos (E ~ 10²⁰–10²³).
- Pisos de resolução Monte Carlo: p(S) 10⁻⁴; controle de fase e envelopes 10⁻³.
- Primeiros 10.000 zeros consultados várias vezes; confirmação estrita só nas faixas m4.
- Não executados:
  - implementação por outra pessoa ou linguagem;
  - densidade θ na cadeia completa;
  - inversão harmônica;
  - verificação completa dos zeros;
  - Etapas 11–12 (classes de operadores e busca de candidatos).

## 8. Próximos passos possíveis

1. Etapa 11: matriz de classes de operadores com fontes primárias, tratando cada lacuna como "não especificado".
2. Implementação independente por outra pessoa ou linguagem.
3. Alturas maiores (tabelas de Odlyzko em ~10¹²–10²²), onde a correção CUE entra no domínio validado.
4. Enunciado rigoroso da forma distribucional da fórmula explícita para a observável com janela (**A**).

## 9. Quadro-síntese

| Tema | m4-v1 (10.001–40.000) | m4-v2 (40.001–70.000) | m4-v3 (70.001–100.000) | Classe | Situação |
|---|---|---|---|---|---|
| C1: frequências r·log p sem catálogo | 10/10 | 10/10 | 10/10, reproduzido | B | **Sucesso** replicado em 30 blocos; detecções sem correspondência: 0 |
| C2: coeficientes −log p/(π p^{r/2}) e sinal (linhas claras) | 10/10 | 10/10 | 10/10, reproduzido | B | **Sucesso**; abs(razão−1) ≤ 2,6·10⁻⁹ entre elegíveis |
| Linhas junto ao limiar (log 127, log 131, 5², 137, 139) | variáveis/inconclusivas | variáveis/inconclusivas | variáveis/inconclusivas; divergem entre implementações | — | **Inconclusivo** quanto à detecção significativa; limitado pela detectabilidade do instrumento |
| C3: CDF de espaçamentos × GUE finito / Poisson | rejeitados 10/10 | rejeitados 10/10 | rejeitados 10/10 | B | Distinto de ambos |
| C3: R₂ × GUE finito | 1/10 rejeitado | 0/10 | 0/10 | B | Não rejeitado (não equivale a compatibilidade demonstrada) |
| C3: K_c × GUE finito | 10/10 | 10/10 | 10/10 (d08 limítrofe) | B | Distinto; pico em τ = 1 com explicação heurística (D) |
| Var(s) | 0,158–0,162 | 0,160–0,163 | 0,161–0,164 | B | Abaixo do GUE finito, crescendo com a altura |
| CUE de altura finita (Bogomolny et al.) | reduz a distância; superestima a redução de variância | idem | idem; distância 1,6–1,9× o ruído | D/secundária | Fora do domínio validado; sem ajuste |
| Blackman–Harris | C1/C2 10/10 | 10/10 | 10/10 | B | Robusto |
| Implementação independente | — | — | D1–D9 dentro; S4 fora em 3 blocos | — | **Discrepância de plano** (R2), investigada; sem divergência entre implementações |
| Auditoria anterior (3 blocos) | D1, D2, D3 e D8 fora | — | — | — | Falhas explicadas e mantidas; corrigidas numericamente em m4-v3 |
| Dinâmica, trajetórias, operador | não reconstruídos | não reconstruídos | não reconstruídos | — | **Fora do alcance** destes dados (§6) |
| Hipótese de Riemann | sem implicação | sem implicação | sem implicação | — | §6, item 4 |
