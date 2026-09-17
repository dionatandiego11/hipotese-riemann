# Protocolo experimental pré-registrado e congelado

**Versão:** 1.0.0  
**Data:** 12/09/2026  
**Semente pseudoaleatória mestre:** `20260912`  
**Status:** Congelado antes da consulta ao conjunto de teste reservado.

---

## 1. Perguntas de pesquisa mensuráveis

1. **Estatística espectral local:** A estatística local de espaçamentos e correlação de pares dos zeros normalizados (unfolded) $\tilde\gamma_n$ é quantitativamente compatível com a previsão do Gaussian Unitary Ensemble (GUE) e estatisticamente incompatível com Poisson e controles aleatorizados?
2. **Detecção cega de períodos:** Um detector espectral estritamente cego (sem acesso a números primos, logaritmos de primos ou peneiras na entrada) é capaz de recuperar períodos correspondentes a $T_p = \log p$ e repetições $r \log p$ na densidade oscilatória $d_{\mathrm{osc}}(E)$?
3. **Resistência e estabilidade:** As frequências, amplitudes complexas e fases recuperadas resistem a variações de janelamento, tamanhos de bloco e replicação no bloco reservado (*holdout*), exibindo significância frente a espectros nulos calibrados?

---

## 2. Divisão de dados em blocos determinísticos contíguos

Para os primeiros 10.000 zeros não triviais ($\gamma_1 \approx 14.1347$ até $\gamma_{10000} \approx 9877.78$):

| Bloco | Faixa de índices | Função metodológica | Condição de acesso |
|---|---|---|---|
| **Piloto / Diagnóstico** | $1 \le n \le 1.000$ | Verificação de baixa altura, calibração do pipeline e testes de código | Aberto para depuração inicial |
| **Desenvolvimento** | $1.001 \le n \le 4.000$ | Ajuste de parâmetros de malha, janelas e limiares de detecção | Aberto para calibração de hiperparâmetros |
| **Validação** | $4.001 \le n \le 7.000$ | Confirmação de sensibilidade e estabilidade do detector | Aberto para validação cruzada prévia |
| **Teste Reservado (*Holdout*)** | $7.001 \le n \le 10.000$ | Teste confirmatório cego com protocolo estritamente congelado | Só pode ser consultado após congelamento dos hashes |
| **Expansão Futura** | $10.001 \le n \le 100.000$ | Robustez em grandes alturas e estudo de anomalias | Etapa posterior (Marco 4) |

*Nota metodológica:* Estes blocos são segmentos contíguos de um espectro determinístico único, e não amostras estatísticas i.i.d.

---

## 3. Variáveis, convenções e unfolding

### 3.1 Níveis e coordenadas
- **Estatística espectral local:** Coordenadas *unfolded* $x_n = \bar N(\gamma_n)$, com
  $$\bar N(E) = \frac{E}{2\pi}\log\frac{E}{2\pi} - \frac{E}{2\pi} + \frac{7}{8}, \qquad \bar d(E) = \frac{1}{2\pi}\log\frac{E}{2\pi}.$$
  Espaçamentos normalizados: $s_n = x_{n+1} - x_n$.
- **Períodos aritméticos:** Níveis originais em energia $E = \gamma_n$, com transformada de Fourier:
  $$F_w(t) = \sum_n w(\gamma_n) e^{-i (\gamma_n - E_c) t} - \int w(E)\bar d(E) e^{-i(E - E_c) t} dE.$$
  Relação com FFT de frequência cíclica $f$: $t = 2\pi f$. O período de uma órbita é $t = r \log p$.

---

## 4. Parâmetros operacionais congelados

- **Janela padrão de apodização:** Janela de Hann (cosseno elevado). Janela secundária de controle: Prolate Spheroidal (Slepian / DPSS) ou Blackman–Harris.
- **Faixa de períodos pesquisada:** $t \in [0.5, 5.0]$ (cobre de $\log 2 \approx 0.693$ até além de $\log 140$).
- **Amostragem no domínio do período:** Malha fina com passo $\Delta t \le \frac{2\pi}{10 (B - A)}$ garantindo sobreamostragem de pelo menos 10 pontos por lóbulo de resolução.
- **Nível de significância:** $\alpha = 0.05$ com correção para comparações múltiplas (FDR ou Bonferroni sobre a família primária de picos).
- **Número de replicações de controle nulo:**
  - Perfil `pilot`: $B = 99$ simulações.
  - Perfil `main`: $B = 999$ simulações (limite inferior de valor-p: $p_{\mathrm{MC}} \ge 0.001$).
- **Regras de matching aritmético:**
  - Tolerância de emparelhamento: $|t_{\mathrm{obs}} - r \log p| \le \delta_t$, onde $\delta_t$ é determinado pela largura a meia altura (FWHM) do lóbulo de resolução da janela medido em testes sintéticos.
  - Associação 1-para-1 gulosa por proximidade; picos dentro da zona de fusão de duas linhas são explicitamente marcados como *mistura/não resolvido*.

---

## 5. Protocolo do detector cego (Blind Detector)

1. O módulo `periods.py` recebe unicamente as ordenadas $\{\gamma_n\}$, o intervalo $[A, B]$, e parâmetros de grade numérica.
2. O detector **NÃO** importa bibliotecas de teoria dos números, tabelas de primos, nem funções que calculem primos ou logaritmos de primos.
3. A saída do detector é persistida e congelada em `results/<run_id>/tables/blind_peaks.csv` com respectivo hash SHA-256.
4. Somente após a gravação de `blind_peaks.csv` o módulo `arithmetic.py` é invocado para confrontar os picos com $\{r \log p\}$.

---

## 6. Modelos de controle nulo

1. **Poisson uniforme:** Processo pontual com intensidade unitária ajustada ao comprimento $L = x_{\max} - x_{\min}$.
2. **GUE (Gaussian Unitary Ensemble):** Matrizes tridiagonais de Dumitriu–Edelman ($\beta = 2$) amostrando a região central de Wigner, desdobradas com o semicírculo.
3. **Permutação de espaçamentos (Shuffled Spacings):** Preserva a distribuição marginal de $s_n$, mas destrói correlações de ordem superior e coerência de fase.
4. **Randomização de fases:** Preserva amplitudes no domínio Fourier, destruindo a interferência construtiva dos níveis.

---

## 7. Emenda v2 (13/09/2026) — revisão do instrumento M3 e dos controles

Esta emenda cria a versão **m3-v2** do protocolo. A versão 1.0.0 acima permanece registrada; as análises M3
produzidas com ela ficam **invalidadas** pelos defeitos listados, não reinterpretadas.

### 7.1 Defeitos encontrados na implementação v1

1. **Quadratura do termo suave sub-resolvida.** 1000 nós de Gauss–Legendre em L≈9860 produziam aliasing: picos
   espúrios igualmente espaçados (~0,4066 em t, fase 0/π, |F|≈1374), que dominavam `blind_peaks.csv` da execução
   `run_20260913_015928_m3_main` (interrompida durante os nulos).
2. **FWHM nominal errada por fator 2.** Para Hann, a FWHM do módulo é 2·(2π/L) (medida), não 2π/L.
3. **Ruído estimado nos próprios zeros.** Nos zeros, |F| entre linhas é ~10⁻³–10⁻⁴ das flutuações dos controles,
   porque a fórmula explícita é uma identidade (o fundo é vazamento determinístico por lóbulos laterais). A escala
   MAD interna tornava lóbulos laterais "significativos".
4. **GUE com normalização errada.** Denso: raio 1/√2 em vez de 1 (unfolding pelo semicírculo distorcido).
   Tridiagonal: diagonal N(0,1)/√2 em vez de N(0,2)/√2 (Dumitriu–Edelman), gerando ensemble mais rígido
   (variância de espaçamento ≈0,145 em vez de ≈0,18). A aparente concordância dos zeros de baixa altura com o
   "envelope GUE" nas execuções v1 é artefato desse defeito.
5. **R₂ e form factor.** Normalização de R₂ sem contagem fixa; termo desconectado de Hann com argumento `sinc(2τL)`
   e sem fase do centro (efeito numérico desprezível para τL≫1, corrigido).
6. **Custo.** Soma direta (~33 s por realização) inviabilizava B=999.

### 7.2 Método m3-v2

- **Instrumento:** F_w(t) na convenção e^{-i(E−E_c)t}, janela de Hann em [γ_first, γ_last] do bloco. Termo discreto
  por NUFFT tipo 1 (kernel gaussiano, R=2, meia-largura 12), verificado a cada execução contra soma direta em 64
  pontos. Termo suave por Gauss–Legendre composto (painel 0,5, ordem 8), com verificação por redução do painel
  à metade e comparação com densidade θ′/π. Malha: 8 pontos por FWHM medida.
- **Escala de ruído:** σ_nulo(t) = RMS de |F| em 200 realizações do nulo primário (permutação de espaçamentos
  unfolded reconstruída em energia), média móvel de largura 0,05 em t. Nulo secundário: GUE (uma matriz
  tridiagonal por realização, 60% dos níveis centrais, reescala linear para a mesma contagem e extensão unfolded).
- **Detecção (sem catálogo):** máximos locais de z = |F|/σ_nulo separados por ≥1 FWHM; limiar FWER = quantil
  1−α da distribuição do máximo de z em 999 realizações nulas independentes das usadas para σ; p ajustado por
  pico = (1+#{max nulo ≥ z})/(B+1). α=0,05.
- **Calibração sintética (sem catálogo):** linhas em períodos uniformes aleatórios injetadas na densidade de níveis
  GUE (resolvendo N̄(E) + Σ Re[C e^{iET}/(iT)] = x, i.e. densidade d̄ + Σ Re[C e^{iET}]), com z verdadeiro em [0,5; 4]×limiar; tolerância de matching =
  quantil 0,99 do erro de localização das linhas recuperadas (limitada a 0,5 FWHM); separação de resolução = menor
  separação de pares com ≥90% das linhas recuperadas. Orçamento de positividade da densidade registrado.
- **Congelamento:** `blind_peaks.csv` e `nulls.npz` gravados e com SHA-256 antes de importar `arithmetic.py`.
- **Comparação aritmética:** catálogo de todos (p, r) com r log p ∈ [0,5; 5]; matching um a um guloso por distância;
  escore S = linhas com detecção correspondente; p Monte Carlo de S com a mesma cadeia nos 999 nulos. Detectabilidade
  prevista: |c| L/4 ≥ limiar·σ_nulo(T). Medição **direcionada** separada: ajuste linear conjunto
  F(t) ≈ Σ a_k W(t−T_k) em ±0,5 FWHM de cada linha, C_k = 2 a_k e^{−iE_c T_k}. Coerência de fase comparada com
  controle de fase que preserva |F| (999 realizações). Sensibilidade: 20 perturbações uniformes de ±3·10⁻⁹ nos zeros.
- **Blocos:** piloto 1–1000, dev 1001–4000, val 4001–7000, holdout 7001–10000, e `full` 1–10000 (descritivo,
  aninhado, contém o holdout).

### 7.3 Estado do teste reservado

O bloco 7001–10000 **não é intocado**: as execuções v1 `run_20260913_015559_m2_main` e
`run_20260913_015928_m3_main` já processaram os 10.000 zeros. Nenhum parâmetro v2 foi escolhido observando saídas
desses índices após a revisão, mas os resultados do bloco reservado devem ser lidos como validação com protocolo
congelado, não como teste pré-registrado intocado. Para uma afirmação confirmatória estrita, reservar os zeros
10.001–100.000 (Etapa 10).

### 7.4 Congelamento

`python -m riemann_spectra protocol freeze --config configs/m3_protocol.toml` grava
`configs/m3_protocol.lock.json` com o SHA-256 da configuração e dos módulos `periods.py`, `arithmetic.py`,
`inverse_spectroscopy.py`, `controls.py`, `unfolding.py`. O subcomando `m3` recusa os blocos `holdout` e `full` sem
um lock idêntico ao estado atual.

---

## 8. Emenda v3 (13/09/2026) — correções da auditoria `docs/ANALISE_RESULTADOS.md`

Registrada **antes** de executar qualquer análise m3-v3. A versão m3-v2 permanece preservada:
`configs/m3_protocol.toml`, `configs/m3_protocol.lock.json`, cópia integral dos fontes em `archive/code_m3-v2/`
(hashes conferidos contra o lock) e execuções `run_20260913_023918_*` e `run_20260913_024706_*`.

### 8.1 Defeitos corrigidos

1. **Assimetria da estatística de decisão (prioridade 1).** Em v2, z dos zeros usava amplitude recalculada por soma
   direta na posição refinada, enquanto máximos nulos e sintéticos usavam a malha. Isso alterou a decisão de
   `log 131` no holdout, que passaria de 36 para 35 detecções. Em v3, z = |F(t_k)|/σ(t_k) é tomado no ponto da
   malha para zeros, nulos e sintéticos. `z_refined` e a posição refinada são apenas descritivos. `freeze.json`
   registra quantas decisões mudariam se o z refinado fosse usado.
2. **Reuso de nulos entre limiar e escore global.** Em v3 há três conjuntos independentes de sementes: σ(t) (200),
   limiar e p ajustado por pico (999), distribuição nula de S com o limiar já fixado (999).
3. **Janela e densidade não propagadas.** `window` (`hann`, `blackman_harris`) e `density` (`rvm`, `theta`) são
   obrigatórios na configuração e chegam ao instrumento, à resposta analítica, ao ajuste direcionado e ao limite
   de detecção. Opções não implementadas geram erro.
4. **Blocos M2 fixos e manifestos sobrescrevíveis.** Os blocos M2 são declarados em `[[m2_blocks]]`. Manifesto e
   validação passaram a `data/raw/manifests/<dataset_id>.json` e `data/processed/validation/<dataset_id>.json`, sem
   sobrescrita. A validação guarda o SHA-256 e a contagem do arquivo validado, e M1/M3 recusam validação de outro
   conjunto. Os arquivos antigos foram preservados. A validação dos 10.000 zeros foi refeita nesse formato
   (máx. |erro| 2,50·10⁻⁹).
5. **Critério de validação com fator 2.** O critério passou a ser |erro| ≤ erro declarado (3·10⁻⁹).
6. **Teste de envelope M2 não simétrico.** Agora é um teste de posto sobre observação e nulos, cada membro comparado
   à média dos outros B. A calibração sob permutabilidade é verificada em teste. B passou de 99 para 199.
7. **Memória e recuperação do código.** O manifesto registra o RSS do processo principal e do maior filho, e declara
   que o pico agregado não é medido. Cada execução copia os fontes para `results/<run>/code/`.

### 8.2 Estimadores direcionados (declarados antes da execução)

- Primário `band_conjugate`: 9 pontos em ±0,5 FWHM por linha e modelo com lóbulo conjugado W(t + T), resolvido como
  sistema linear real em (Re C, Im C).
- Variantes de sensibilidade: `band_no_conjugate` (estimador de v2) e `centers_conjugate` (só t = T_k).
- O relatório mostra as três variantes e a maior diferença entre elas. Resíduo de ajuste ≠ incerteza total.

### 8.3 Fase

R = |média exp(i·erro)| mede alinhamento e é invariante a rotação comum. Q = média cos(erro) testa também o sinal
absoluto. As duas estatísticas são comparadas com o mesmo controle de fase, que preserva |F|.

### 8.4 Execuções planejadas e estado dos dados

- `configs/m3_protocol_v3.toml` (Hann): pilot, dev, val. Depois, congelamento. Depois, holdout e full.
- `configs/m3_protocol_v3_bh.toml` (Blackman–Harris): variante de robustez exploratória, com lock próprio, nos mesmos
  blocos.
- M2 principal repetido com o teste simétrico e B = 199.
- **Todos os 10.000 primeiros zeros já foram consultados** (v1, v2 e auditoria). As execuções v3 medem o impacto das
  correções e a robustez. Não são confirmatórias.
- A faixa 10.001–100.000 **não** será analisada nesta etapa. Suas regras (blocos, B, estimador primário e critérios)
  serão congeladas numa versão própria antes de qualquer consulta.

### 8.5 Reclassificação de afirmações anteriores

- Concordância dos coeficientes com −log p/(π p^{r/2}): **B** (numérica). Identificação exata da observável
  finita com a fórmula explícita de Guinand–Weil: **pendente** de enunciado com classe de funções-teste, termos e
  erros.
- Pico de K_c em τ = 1 associado à pequena variância de N̄(γₙ) − (n − ½): **heurística** (D), não consequência
  demonstrada do teorema de Selberg. A variância não determina a função característica numa frequência fixa, e o
  resultado usual não se transfere automaticamente para amostragem nos zeros.
- Correções de altura finita de Bogomolny et al. (2006): a comparação usa **CUE** de dimensão efetiva, não GUE de
  dimensão N_eff. A dimensão efetiva nos centros das janelas atuais é ~1,5–1,7, fora de um regime claramente
  assintótico. Nenhuma comparação quantitativa foi feita.

---

## 9. Protocolo m4-v1 (13/09/2026) — primeira faixa nova: zeros 10.001–40.000

Registrado **antes** de qualquer análise de zeros com índice > 10.000. Até o congelamento, os dados novos só
passaram por aquisição e auditoria:
- leitura de `data/raw/zeros1` até o índice 40.000 (finitude, ordenação estrita, espaçamentos mínimo e máximo);
- CSV `data/processed/zeros_40k.csv`, cujo prefixo coincide com o de 10k;
- validação mpmath de 20 índices estratificados, com máx. |erro| 2,40·10⁻⁹ ≤ 3·10⁻⁹;
- γ₁₀₀₀₁ e γ₄₀₀₀₀ lidos para calcular alturas e N_eff.

Os zeros **40.001–100.000 não foram processados** e ficam reservados para confirmação posterior. O código m3-v3
está preservado em `archive/code_m3-v3/`, conferido contra os locks.

### 9.1 Dados e blocos

Dez blocos contíguos e disjuntos de 3.000 zeros (`b01` = 10.001–13.000, …, `b10` = 37.001–40.000), comparáveis aos
blocos de 3.000 do M3. Não há bloco agregado. Blocos contíguos de um espectro determinístico não são amostras
independentes; toda correção entre blocos usa Holm, válido sob dependência arbitrária.

### 9.2 Análise primária (C1 e C2): `configs/m4_v1.toml`

- Instrumento: janela **Hann**, densidade Riemann–von Mangoldt, t ∈ [0,5; 5], 8 pontos por FWHM, quadratura com painel
  0,5 e ordem 8.
- Estatística de decisão: z = |F|/σ_nulo na malha, idêntica para zeros, controles e sintéticos.
- Nulo primário (permutação de espaçamentos), com conjuntos de sementes independentes:
  - σ(t): 200 realizações;
  - limiar: **9.999**;
  - escore global: **9.999**.
- Nulo secundário GUE: 100 + 199.
- **Orçamento fixado antes de ver a faixa**, pelo benchmark no bloco já consultado 7.001–10.000: 300 s por bloco com
  9.999 + 9.999 e 4 processos, projeção ≈ 50 min para 10 blocos. **O orçamento não será aumentado depois de ver
  resultados.**
- **Regra de três categorias:** IC exato de 95% por estatísticas de ordem para o quantil 0,95 do máximo nulo.
  - z > limite superior: *detectada*;
  - z dentro do IC: *inconclusiva quanto à detecção significativa*;
  - z < limite inferior: *não detectada*.
  Cobertura verificada por simulação (0,963 com B = 9.999). Candidatos inconclusivos não contam como detecções nem são
  reclassificados.
- Escore S: linhas do catálogo com detecção correspondente (um a um, tolerância calibrada nos sintéticos do bloco).
  O nulo de S usa a mesma regra estrita no conjunto-escore. S incluindo inconclusivos é só sensibilidade.
- Estimador direcionado primário: `band_conjugate`. As variantes `band_no_conjugate` e `centers_conjugate` são só
  robustez.

### 9.3 Critérios pré-registrados (α familiar = 0,05, Holm entre os 10 blocos)

**C1 — Recuperação de frequências (sem catálogo na detecção).** Um bloco passa se:
- (a) p(S) com Holm ≤ 0,05;
- (b) recuperação ≥ 0,95 entre as linhas *claramente detectáveis*, isto é, com z previsto = |c|·W(0)/(2σ) ≥ **1,5** ×
  limite superior do limiar. A margem 1,5 veio dos sintéticos dos blocos já consultados: recuperação 100% acima de
  1,5 e 0,82–1,0 entre 1,25 e 1,5.

Critério de família: no máximo **2** blocos com alguma detecção sem correspondência no catálogo. Sob FWER 0,05 por
bloco, P(≥ 3 de 10) ≈ 0,012 se os blocos fossem independentes.

C1 é *replicado* na faixa se todos os blocos passam e o critério de família vale. Caso contrário, é relatado como
parcial, com os blocos e motivos.

**C2 — Concordância de coeficientes (medição direcionada, não cega).** Linhas elegíveis são as resolvidas e
claramente detectáveis. Um bloco passa se:
- a fração de elegíveis com |razão − 1| ≤ **1·10⁻⁶** é ≥ **0,95**; a tolerância cobre a dependência de janela e
  estimador observada em dados antigos (máx. 7·10⁻⁷);
- Q ≥ **0,9**, com p(Q) Holm ≤ 0,05 (controle de fase com 999 realizações).

C2 é replicado se todos os blocos passam.

**C3 — Compatibilidade estatística local (`configs/m4_v1_m2.toml`).**
- Testes de posto simétricos contra GUE finito e Poisson, para CDF de espaçamentos, R₂ e K_c, com **999**
  realizações cada. O menor p com Holm atingível entre 10 blocos é 0,01.
- Uma família Holm por par (referência, estatística).
- Resultado por bloco: "rejeitado" ou "não rejeitado". Não existe veredito de compatibilidade confirmada.
- Referência dos dados antigos: CDF-GUE rejeitada em todos os blocos de 1–10.000. A tendência "replica" se a
  rejeição ocorrer em ≥ 8 dos 10 blocos novos.

As três conclusões são relatadas separadamente; nenhuma é condição para outra.

### 9.4 Robustez (não seleciona resultados)

- `configs/m4_v1_bh.toml`: mesma cadeia com Blackman–Harris e orçamento 999/999, pré-registrado por custo. Os
  critérios são calculados e relatados como robustez. Um resultado mais favorável com BH não substitui o primário.
- Variantes de estimador e sensibilidade a ±3·10⁻⁹: relatadas.

### 9.5 Análise secundária CUE (C3, descritiva)

- Implementação de Bogomolny et al. (2006), eqs. 18–24: p₀ por Fredholm do núcleo seno (Bornemann), p₁ por
  Richardson (N = 32, 64) sobre E_N exato (eq. 22), N_eff e α na mediana de altura do bloco.
- Validações antes do congelamento: caso analítico N = 2 (erro 1·10⁻¹⁰); Var p₀ = 0,17999; ∫p₁ ≈ 0; Haar CUE com
  N = 2, 4, 10 dentro do limite DKW; convergência N⁻⁴ da expansão truncada.
- **Domínio:** nos blocos novos, N_eff ≈ 1,7–2,0. O erro da expansão truncada na CDF é 42% da correção em N = 2 e 14%
  em N = 3; a fonte valida em N_eff ≈ 7,7 e 11,3. Resultados são indicativos. **Nenhuma decisão de C1–C3 depende
  desta análise**, e ela não será ajustada depois de ver os dados.
- Observação feita em dados já consultados, antes do congelamento e sem uso para ajuste: a correção superestima a
  redução de variância (predita 0,129–0,139; medida 0,153–0,157 em 1.001–10.000).

### 9.6 Congelamento e ordem de execução

1. `protocol freeze` para `m4_v1.toml`, `m4_v1_bh.toml` e `m4_v1_m2.toml`, com `lock_scope = "package"`: todos os
   módulos entram no hash, inclusive critérios e relatórios.
2. Primária Hann nos 10 blocos; depois robustez BH; depois M2 + CUE.
3. Se algo falhar por defeito de código, o protocolo não é editado: cria-se m4-v2, registrando o que já foi visto.

### 9.7 Registro de execução (sem alteração das regras acima)

- Congelamento em 13/09/2026 11:44, combinado de código `5885b75ea98233af…` (19 módulos), idêntico nos três locks.
  Cópia integral dos fontes e locks em `archive/code_m4-v1/`.
- Execuções, todas com o lock conferido pelo CLI e sem desvios de protocolo:
  - primária Hann: `run_20260913_144429_m3_b01-…-b10`, 55 min;
  - robustez BH: `run_20260913_154009_m3_b01-…-b10`, 29 min;
  - C3 + CUE: `run_20260913_160910_m2_m4_v1_m2`, 71 min. O custo previsto era ~30 min; a diferença veio das
    estatísticas R₂ e K_c por realização e não alterou nenhum parâmetro.
- Nenhum orçamento foi alterado. Os zeros 40.001–100.000 continuam não processados.

---

## 10. Protocolo m4-v2 (13/09/2026) — replicação de m4-v1 nos zeros 40.001–70.000

Registrado **antes** de qualquer análise de zeros com índice > 40.000. Até o congelamento, os dados novos só
passaram por aquisição e auditoria:
- leitura até o índice 70.000 (finitude, ordenação, espaçamentos mínimo e máximo);
- `zeros_70k.csv`, cujo prefixo coincide com `zeros_40k.csv`;
- validação mpmath de 20 índices estratificados até 70.000, com máx. |erro| 2,27·10⁻⁹ ≤ 3·10⁻⁹;
- γ₄₀₀₀₁ ≈ 33.190 e γ₇₀₀₀₀ ≈ 54.512 lidos para calcular alturas e N_eff ≈ 1,97–2,10.

Os zeros **70.001–100.000 continuam reservados** e não processados.

### 10.1 Natureza da verificação

- **Replicação em dados não utilizados, com o mesmo instrumento e a mesma implementação.** O código é idêntico ao
  congelado em m4-v1 (hash combinado `5885b75ea98233af…`, cópia em `archive/code_m4-v1/`).
- Não é confirmação por implementação independente; essa verificação continua pendente.
- Blocos contíguos não são tratados como independentes. Holm é mantido por ser válido sob dependência arbitrária.
- A comparação m4-v1 × m4-v2 é descritiva, sem teste estatístico entre faixas: as faixas diferem em altura e as
  estatísticas não são independentes.

### 10.2 O que muda e o que não muda

- Alterados **apenas**:
  - blocos: `c01` = 40.001–43.000, …, `c10` = 67.001–70.000, dez blocos contíguos de 3.000;
  - sementes: 20260916 para as análises M3 e 20260917 para M2;
  - identificação dos dados: `odlyzko_zeros1_first70000`, `zeros_70k.csv`, `max_zeros`;
  - rótulos de versão.
- **Inalterados**, conferido por comparação semântica das configurações:
  - critérios C1–C3, tolerâncias, `clear_margin`, `ratio_tolerance`, frações mínimas, `q_min`, α familiar;
  - janela primária Hann e estimador `band_conjugate`, com as mesmas variantes;
  - orçamentos: 200/9.999/9.999 (primária), 999/999 (BH), 999 (M2), 999 (controle de fase);
  - regra de três categorias e confiança 0,95;
  - famílias de hipóteses (Holm entre os 10 blocos da faixa, por critério e por par referência/estatística);
  - **regra** de elegibilidade de linhas: resolvida e com z previsto ≥ 1,5 × limite superior, recalculada em cada
    bloco. Nenhuma lista de linhas herdada de m4-v1 é usada.
- Blackman–Harris e CUE continuam secundários, com a mesma implementação. **A aproximação CUE não é ajustada.**

### 10.3 Comparações com m4-v1 a relatar (lista fixada agora)

1. Por bloco: detecções, inconclusivos, sem correspondência, p(S), faixa inconclusiva, claramente detectáveis,
   recuperação, elegíveis C2, fração ≤ tolerância, máximo e mediana de |razão − 1|, Q, p(Q), veredito C1/C2.
2. Família: blocos que passam C1/C2, blocos com detecção sem correspondência, replicação sim/não. Falhas e
   inconclusivos são relatados sem reclassificação.
3. Linhas detectadas: as que aparecem em todos os blocos da faixa, as variáveis e as mudanças em relação a m4-v1
   (descritivo; sem usar as listas de m4-v1 como critério).
4. C3: número de rejeições por par referência/estatística; Var(s) por bloco e tendência com a altura.
5. Secundárias: detecções BH e diferença de coeficientes Hann × BH; CUE, com distâncias RMS ao limite e à predição
   corrigida, ruído amostral e variância predita versus medida.
6. Custos de tempo e memória e qualquer desvio operacional.

### 10.4 Congelamento e execução

`protocol freeze` para `m4_v2.toml`, `m4_v2_bh.toml` e `m4_v2_m2.toml` (`lock_scope = "package"`). Depois, executar
na ordem primária → BH → M2 + CUE. Se houver defeito de código, nenhuma regra é editada: cria-se nova versão e se
registra o que já foi visto.

### 10.5 Registro de execução (sem alteração das regras acima)

- Congelamento em 13/09/2026 14:30. Hash combinado de código `5885b75ea98233af…`, idêntico ao de m4-v1. Cópia em
  `archive/code_m4-v2/`.
- Execuções, com os locks conferidos pelo CLI e sem desvios de protocolo:
  - primária: `run_20260913_173045_m3_c01-…-c10` (50 min);
  - BH: `run_20260913_182040_m3_c01-…-c10` (26 min);
  - C3 + CUE: `run_20260913_184711_m2_m4_v2_m2` (85 min).
- Comparação da lista §10.3: `results/analysis_m4_v1_v2_comparacao/`, script escrito durante a execução primária e
  antes de qualquer saída arithmetic/M2 de m4-v2 ser lida. Uma correção de busca de diretório foi feita no script
  antes da primeira execução.
- Zeros 70.001–100.000 continuam não processados.

---

## 11. Protocolo m4-v3 (13/09/2026) — faixa final 70.001–100.000, duas implementações

Registrado **antes** de qualquer análise dos zeros 70.001–100.000. Acesso anterior limitado à aquisição e à auditoria
(`results/m4_v3_data_access_log.md`): leitura até 100.000, validação mpmath de 20 índices (máx. 2,74·10⁻⁹ ≤ 3·10⁻⁹),
γ₇₀₀₀₁ ≈ 54.512 e γ₁₀₀₀₀₀ ≈ 74.921.

### 11.1 Fechamento anterior

As quatro verificações fora da tolerância da auditoria independente continuam registradas como **falhas do critério
pré-registrado**, com diagnóstico ([AUDITORIA_INDEPENDENTE.md](AUDITORIA_INDEPENDENTE.md) §4, §9;
`results/independent_audit_20260913/closure.json`). Não houve reclassificação.

### 11.2 Versão do código (única alteração além de blocos, sementes e dados)

`src/riemann_spectra` m4-v3, com três correções **numéricas**, sem alteração de regra científica: FWHM com tolerância
de máquina, CUE sem interpolação linear, quadratura do termo suave em coordenadas locais.

Impacto medido só nos 20 blocos já analisados (`results/m4_v3_impact/`): nenhuma mudança de classificação; z relativo
≤ 6,4·10⁻⁸; termo suave ≤ 2,0·10⁻¹⁰ contra a forma fechada.

As fontes de m4-v1 e m4-v2 continuam em `archive/code_m4-v2/` (= m4-v1); as configurações e os resultados anteriores
não mudam. As configurações `configs/m4_v3*.toml` diferem de m4-v2 **apenas** em blocos (`d01`–`d10` = 70.001–100.000),
sementes (20260918 e 20260919), identificação dos dados e rótulo de versão (verificação semântica registrada).

### 11.3 Papéis das implementações

- **Primária:** `src/riemann_spectra` m4-v3. As conclusões C1–C3 de m4-v3 são as dela, com os critérios e as famílias de
  §9.3 inalterados.
- **Reprodução:** `independent/riemann_indep` v2, que difere de v1 só pelo limite explícito de acesso. Plano, orçamentos,
  tolerâncias e regras de interrupção R1–R4 estão em `independent/M4V3_PLAN.md`.
- A escolha é fixa: nenhum resultado é trocado depois de ver os dados.
- A concordância entre as duas implementações **não** constitui duas confirmações estatísticas independentes.
- Blackman–Harris continua como robustez e CUE como análise secundária, ambos só na primária. A reprodução recalcula
  CUE apenas para a verificação determinística.

### 11.4 Interrupção

Qualquer regra R1–R4 acionada suspende a conclusão **conjunta**. A conclusão da primária é relatada como
"reprodução com discrepância aberta" até investigação, e todo acesso adicional aos dados é registrado.

### 11.5 Congelamento e ordem

- Locks de pacote para `m4_v3.toml`, `m4_v3_bh.toml` e `m4_v3_m2.toml`.
- Lock do plano de reprodução, cobrindo o plano, os scripts de execução e de comparação e os fontes da reprodução.
- Ordem de execução: primária Hann → BH → M2 + CUE → reprodução → comparação.

### 11.6 Registro de execução

- Primária Hann `run_20260913_220906_m3_d01-…-d10`; BH `run_20260913_232151_m3_d01-…-d10`; M2 + CUE
  `run_20260914_012016_m2_m4_v3_m2`. Uma execução M2 anterior, interrompida por pausa a pedido do usuário, está em
  `…_m2_m4_v3_m2_INTERROMPIDA` e não foi usada.
- Reprodução `results/m4_v3_independent/`; comparação `results/m4_v3_joint/comparison_m4v3.json`.
- Todas as execuções conferiram os locks (código `69b5744c…`). Nenhuma regra, limiar ou orçamento foi alterado.
- **Regras de interrupção:** R1 não; **R2 sim** (S4 em d05, d09, d10); R3 não; R4 não. Investigação em
  `results/m4_v3_joint/INVESTIGACAO_R2.md`: erro de desenho do plano (S4 centrado em α em vez de (B+1−u)/(B+1)).
  R2 permanece registrada como acionada.
- Acessos aos dados: `results/m4_v3_data_access_log.md`.
