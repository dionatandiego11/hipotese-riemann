# Registro de andamento da investigação

Estado das etapas do [plano de implementação](../PLANO_IMPLEMENTACAO.md). Última atualização: 19/09/2026.
**Ponto de retomada (resumo para quem continua o trabalho): [ESTADO_ATUAL.md](ESTADO_ATUAL.md).**
**M4 (Etapa 10):** m4-v1 ([PROTOCOLO.md §9](PROTOCOLO.md)) nos zeros 10.001–40.000 e replicação **m4-v2** (§10,
mesmo código e mesmas regras) nos zeros 40.001–70.000, ambos congelados antes da análise. **Auditoria por implementação
independente** em três blocos já analisados: [AUDITORIA_INDEPENDENTE.md](AUDITORIA_INDEPENDENTE.md). Zeros
70.001–100.000 analisados em m4-v3, com R2 acionada e investigada; conclusão conjunta com ressalva em [RELATORIO_CONSOLIDADO.md](RELATORIO_CONSOLIDADO.md) §5 e §9. Não resta faixa reservada nesta tabela.
Protocolo vigente do M3: **m3-v3** ([PROTOCOLO.md §8](PROTOCOLO.md)), congelado em `configs/m3_protocol_v3.lock.json`
(Hann) e `configs/m3_protocol_v3_bh.lock.json` (variante Blackman–Harris). O m3-v2 está preservado em
`configs/m3_protocol.toml` + lock e `archive/code_m3-v2/`. A auditoria que motivou o v3 está em
[ANALISE_RESULTADOS.md](ANALISE_RESULTADOS.md).

## Tabela de acompanhamento

| Etapa | Descrição | Marco | Estado | Última execução | Evidências | Pendências / próximo passo |
|---|---|---|---|---|---|---|
| 0 | Protocolo e pergunta mensurável | M1 | `validado` | 13/09/2026 | `docs/PROTOCOLO.md` (v1 + emendas v2 §7 e v3 §8), `docs/REFERENCIAS.md` | Nenhum dos 10.000 primeiros zeros é intocado (§7.3, §8.4) |
| 1 | Estrutura reproduzível | M1 | `validado` | 13/09/2026 | `pyproject.toml`, `requirements.txt`, CLI, manifestos com hashes; cópia dos fontes em `results/<run>/code/` | Sem Git; instalação em ambiente limpo não repetida |
| 2 | Obter e auditar os zeros | M1 | `validado` | 13/09/2026 | `data/raw/zeros1` (SHA-256 `3436c916…`); manifestos e validações `odlyzko_zeros1_first{10000,40000,70000}` (máx. \|erro\| ≤ 2,50·10⁻⁹); `data/processed/validation/odlyzko_zeros1_first10000.json` (critério \|erro\| ≤ 3·10⁻⁹, máx. 2,50·10⁻⁹, vinculado ao SHA do CSV) | Faixa final analisada em m4-v3; todos os 100.000 zeros utilizados. Registros antigos `data_manifest.json`/`data_validation.json` preservados |
| 3 | Controles | M1 | `validado` | 13/09/2026 | `controls.py`; testes; M1 em `run_20260913_135613_m2_main` | GUE corrigido em 13/09 (ver log) |
| 4 | Unfolding e espaçamentos | M2 | `validado` | 13/09/2026 | `run_20260913_135613_m2_main`: `tables/m2_*_spacing_cdf.csv`, `figures/m2_*.png` | Comparação CUE executada como análise secundária em m4; limitações no relatório consolidado |
| 5 | Correlação de pares | M2 | `validado` | 13/09/2026 | idem, `tables/m2_*_pair_correlation.csv` | — |
| 6 | Spectral form factor | M2 | `validado` | 13/09/2026 | idem, `tables/m2_*_form_factor.csv` | Termo total (sem subtração) não é salvo nas tabelas M2 |
| 7 | Densidade média e transformada | M3 | `validado` | 13/09/2026 | `periods.py`; `block_metrics.json`; Hann e Blackman–Harris executadas (m3-v3) | Densidade θ executada só como diagnóstico do termo suave, não na cadeia completa |
| 8 | Detecção sem catálogo | M3 | `validado` | 13/09/2026 | m3-v3: `blind_peaks.csv`, `freeze.json`, `nulls.npz` (conjuntos σ/limiar/escore independentes) | Inversão harmônica: `não executado`. Linhas limítrofes à resolução Monte Carlo do limiar (ver M3) |
| 9 | Comparação com primos e nulos | M3 | `validado` | 13/09/2026 | m3-v3: `arithmetic_matches.csv` com 3 variantes de estimador; `results/analysis_20260913_v3_comparacao/` | Todos os blocos já consultados: sem teste confirmatório até a Etapa 10 |
| 10 | Ampliação, anomalias, robustez | M4 | `validado` (m4-v1, m4-v2, m4-v3 concluídos; R2 de m4-v3 acionada e investigada) | 14/09/2026 | m4-v1, m4-v2, m4-v3; `results/analysis_m4_v1_v2_comparacao/`, `results/m4_v3_joint/` | Implementação por outra pessoa ou linguagem; densidade θ na cadeia completa; inversão harmônica; S4 a corrigir em versão futura do plano |
| 11 | Fórmulas de traço e classes de operadores | M4 | `em execução` | 19/09/2026 | [ETAPA11_PLANO.md](ETAPA11_PLANO.md); matriz [ETAPA11_MATRIZ_OPERADORES.md](ETAPA11_MATRIZ_OPERADORES.md) com `etapa11_matriz_operadores.csv` e `etapa11_evidencias.csv` (27 entradas sustentam decisão); fontes em [ETAPA11_PENDENCIAS_FONTES.md](ETAPA11_PENDENCIAS_FONTES.md); 11.3b encerrada ([ETAPA11_3B_ENCERRAMENTO.md](ETAPA11_3B_ENCERRAMENTO.md)); controles da 11.6 em `results/etapa11_6_controles/` | 1 pendência de conferência na matriz (K7 M4); 11.5 não iniciada; 11.6: controle Dirichlet com declaração e D1 prontas, falta código e execução; controles dinâmico e aritmético dependem de dados. Resumo em [ESTADO_ATUAL.md](ESTADO_ATUAL.md). Texto anterior desta linha preservado no log (19/09/2026) |
| 12 | Busca limitada por candidatos | M5 | `pendente` | — | — | Aguarda M4 |
| 13 | Relatório final e limites de Hilbert–Pólya | M5 | `pendente` | — | — | Aguarda Etapas 10–12 |

## Execuções válidas

| Execução | Conteúdo | Duração | Comando |
|---|---|---|---|
| `run_20260913_022651_m2_pilot` | M1 + M2, 1.000 zeros, B=19 (depuração; **antes** da correção do GUE — superada) | 9 s | `run --config configs/pilot.toml --milestone M2 --workers 4` |
| `run_20260913_023918_m3_pilot-dev-val` | M3 m3-v2 (superada: decisão assimétrica) | 6,6 min | protocolo v2 |
| `run_20260913_024706_m3_holdout-full` | M3 m3-v2 congelado (superada) | 18,2 min | protocolo v2 |
| **`run_20260913_130157_m3_pilot-dev-val`** | M3 m3-v3 Hann, blocos abertos | 5,9 min | `m3 --config configs/m3_protocol_v3.toml --blocks pilot,dev,val --workers 4` |
| **`run_20260913_130758_m3_holdout-full`** | M3 m3-v3 Hann congelado | 20,1 min | `m3 --config configs/m3_protocol_v3.toml --blocks holdout,full --workers 4` |
| **`run_20260913_132814_m3_pilot-dev-val-holdout-full`** | M3 m3-v3 Blackman–Harris (robustez) | 27,7 min | `m3 --config configs/m3_protocol_v3_bh.toml --blocks pilot,dev,val,holdout,full --workers 4` |
| **`run_20260913_135613_m2_main`** | M1 + M2, teste simétrico, B = 199 | 16,6 min | `run --config configs/main.toml --milestone M2 --workers 4` |
| `run_20260913_023024_m2_main` | M1 + M2, B = 99, teste de envelope não simétrico (superada) | 13 min | — |
| `results/analysis_20260913_v3_comparacao/` | Comparação descritiva v2 × v3 × janelas; incerteza Monte Carlo do limiar | < 1 min | `python results/analysis_20260913_v3_comparacao/compare_v2_v3_windows.py` |
| `results/audit_20260913_resultados/` | Auditoria independente (autoria do usuário) | — | ver ANALISE_RESULTADOS.md §6 |
| **`run_20260913_144429_m3_b01-…-b10`** | **M4 m4-v1 primária** (Hann, 9.999 + 9.999), zeros 10.001–40.000 | 55 min | `m3 --config configs/m4_v1.toml --blocks b01,…,b10 --workers 4` |
| **`run_20260913_154009_m3_b01-…-b10`** | M4 m4-v1 robustez Blackman–Harris (999 + 999) | 29 min | `m3 --config configs/m4_v1_bh.toml --blocks b01,…,b10 --workers 4` |
| **`run_20260913_160910_m2_m4_v1_m2`** | M4 m4-v1 C3 (B = 999) + CUE secundária | 71 min | `run --config configs/m4_v1_m2.toml --milestone M2 --workers 4` |
| **`run_20260913_173045_m3_c01-…-c10`** | **M4 m4-v2 primária** (replicação), zeros 40.001–70.000 | 50 min | `m3 --config configs/m4_v2.toml --blocks c01,…,c10 --workers 4` |
| **`run_20260913_182040_m3_c01-…-c10`** | M4 m4-v2 robustez Blackman–Harris | 26 min | `m3 --config configs/m4_v2_bh.toml --blocks c01,…,c10 --workers 4` |
| **`run_20260913_184711_m2_m4_v2_m2`** | M4 m4-v2 C3 + CUE secundária | 85 min | `run --config configs/m4_v2_m2.toml --milestone M2 --workers 4` |
| `results/analysis_m4_v1_v2_comparacao/` | Comparação m4-v1 × m4-v2 (lista fixada em §10.3) | < 1 min | `python results/analysis_m4_v1_v2_comparacao/compare_m4_v1_v2.py` |
| **`results/independent_audit_20260913/`** | Implementação independente (`independent/`) nos blocos 10.001–13.000, 22.001–25.000 e 67.001–70.000; comparação e diagnóstico | 30 min | ver AUDITORIA_INDEPENDENTE.md §8 |

Memória: processo principal ≤ 304 MB; maior processo filho ≤ 153 MB. O pico agregado dos 4 processos não foi medido.
Máquina: 4 CPUs, Python 3.12.3, NumPy 2.5.3, SciPy 1.18.1.

### Execuções invalidadas (preservadas, não usar)

`run_20260913_015541_m1_pilot`, `run_20260913_015559_m2_main`, `run_20260913_015755_m3_pilot`,
`run_20260913_015812_m3_pilot`, `run_20260913_015847_m3_pilot`, `run_20260913_015928_m3_main` (interrompida).
Motivos: GUE com normalização errada, quadratura com aliasing, FWHM errada, ruído estimado nos próprios zeros e
relatórios com afirmações fixas no template, independentes das medições (PROTOCOLO §7.1). As três execuções M3 piloto
sem `manifest.json` foram interrompidas ou parciais.

## Resultados medidos

### M2 — estatística local (`run_20260913_135613_m2_main`, teste de posto simétrico, B = 199)

| Bloco | Var(s) zeros | Envelope GUE 95% de Var(s) | p GUE: CDF / R₂ / K_c | p Poisson (CDF) |
|---|---|---|---|---|
| pilot 1–1000 | 0,1445 | 0,164–0,194 | 0,005 / 0,865 / 0,005 | 0,005 |
| dev 1001–4000 | 0,1530 | 0,171–0,189 | 0,005 / 0,405 / 0,005 | 0,005 |
| val 4001–7000 | 0,1560 | 0,169–0,188 | 0,005 / 0,255 / 0,005 | 0,005 |
| holdout 7001–10000 | 0,1569 | 0,170–0,189 | 0,005 / 0,095 / 0,005 | 0,005 |
| full 1–10000 | 0,1542 | 0,176–0,185 | 0,005 / 0,025 / 0,005 | 0,005 |

p = 0,005 é a resolução com B = 199. A calibração do teste simétrico sob permutabilidade é verificada em
`tests/test_protocol_v3.py`.

- **B:** CDF dos espaçamentos incompatível com Poisson e com o GUE finito usado (níveis centrais, unfolding pelo
  semicírculo) em todos os blocos. A variância dos espaçamentos dos zeros fica abaixo do envelope GUE e cresce com
  a altura. Isso estabelece menor dispersão local, mas não, sozinho, rigidez de longo alcance.
- **B:** R₂ compatível com o envelope GUE nos blocos de 3.000 zeros. `full`, com 10.000 zeros e p = 0,025, está
  próximo do limite; com B = 199, o valor tem resolução limitada.
- **Hipótese não testada:** correções de altura finita (Bogomolny et al. 2006), que usam **CUE** de dimensão efetiva
  N_eff ≈ 1,5–1,7 nesta faixa. O M2 não é refutação de conjectura assintótica: o nulo é um ensemble finito
  específico e as alturas são baixas.
- **Heurística (D):** o pico de K_c em τ = 1 coincide com a pequena variância medida de N̄(γₙ) − (n − ½)
  (0,067–0,089). A explicação via S(t) não está demonstrada (PROTOCOLO §8.5).

### M3 — espectroscopia inversa (protocolo m3-v3)

Decisão em z na malha para zeros, controles e sintéticos. σ, limiar e escore com 200, 999 e 999 realizações
independentes do nulo de permutação de espaçamentos. **Todos os blocos já tinham sido consultados.**

| Bloco | Detecções Hann v2 → **v3** | Blackman–Harris v3 | Comuns às três | Candidatos na faixa MC do limiar (Hann v3) | p global S (B_escore = 999) | Fração do conjunto-escore acima do limiar |
|---|---|---|---|---|---|---|
| pilot | 18 → **18** | 14 | 14 | 0 | 0,001 | 0,050 |
| dev | 38 → **37** (perde 139) | 29 | 29 | 2 | 0,001 | 0,054 |
| val | 36 → **35** (perde 131) | 27 | 27 | 1 | 0,001 | 0,038 |
| holdout | 36 → **35** (perde 131) | 29 | 29 | 3 | 0,001 | 0,051 |
| full | 41 → **41** | 41 | 41 | 0 | 0,001 | 0,053 |

Em todas as execuções v3 (Hann e BH): nenhuma detecção sem correspondente r log p; recuperação 1,000 entre linhas
previstas detectáveis; nenhuma detecção de linha prevista indetectável. As detecções BH são sempre um subconjunto das
detecções Hann, e as perdas são primos fracos (101–137) e 2³, 5², coerente com o ganho menor
W(0) = 0,359L e o lóbulo principal mais largo.

- **B (detecção sem catálogo):** o conjunto detectado é robusto em `full` (41 linhas iguais nas três execuções). Nos
  blocos de 3.000 zeros, a contagem depende da janela (Hann 35–37, BH 27–29) e, nas linhas limítrofes, da resolução
  Monte Carlo do limiar. Bootstrap dos 999 máximos nulos: intervalo 95% do limiar com largura ≈ 0,07–0,12 em z.
  Exemplo: `log 131` no holdout tem z = 3,295, dentro do intervalo [3,272; 3,395]. A mudança de 36 para 35 veio da
  correção da estatística (z na malha 3,2952 < z refinado 3,3008) e também de outro limiar sorteado (3,2915 em v2,
  3,3143 em v3). Com B = 999, a linha é **inconclusiva quanto à detecção significativa**.
- **B (medição direcionada, não cega):** mediana de |razão − 1| por estimador, nas linhas resolvidas e detectáveis:

  | Bloco | Hann `band_conjugate` | Hann `band_no_conjugate` | Hann `centers_conjugate` | BH `band_conjugate` | Sensibilidade ±3·10⁻⁹ Hann / BH |
  |---|---|---|---|---|---|
  | dev | 5,4·10⁻¹⁰ | 5,4·10⁻¹⁰ | 7,6·10⁻¹⁰ | 3,3·10⁻⁸ | 7,9·10⁻¹⁰ / 4,1·10⁻⁸ |
  | val | 3,9·10⁻¹⁰ | 3,8·10⁻¹⁰ | 2,5·10⁻⁹ | 3,9·10⁻⁸ | 8,4·10⁻¹⁰ / 3,7·10⁻⁸ |
  | holdout | 5,1·10⁻¹⁰ | 5,2·10⁻¹⁰ | 4,3·10⁻⁹ | 3,7·10⁻⁸ | 9,1·10⁻¹⁰ / 3,5·10⁻⁸ |
  | full | 1,9·10⁻¹⁰ | 1,9·10⁻¹⁰ | 2,5·10⁻¹⁰ | 1,6·10⁻⁸ | 4,9·10⁻¹⁰ / 9,5·10⁻⁹ |

  Entre janelas, para as mesmas 47 linhas, a diferença de razão tem mediana 2–6·10⁻⁸ e máximo 7·10⁻⁷. **Correção
  de afirmação anterior:** não se sustenta que a concordância seja "limitada pela precisão da tabela". Janela,
  amostragem e modelo do ajuste mudam a razão em até ~10⁻⁶. O que se sustenta: com cada estimador, o desvio
  mediano é da ordem da sensibilidade desse estimador a perturbações de ±3·10⁻⁹. Isso não é intervalo de confiança.
- **Fase:** R = 1,000 (alinhamento) e Q = 1,000 (sinal absoluto), com p = 0,001 contra o controle de fase em todos os
  blocos. O ajuste direcionado reproduz o sinal negativo dos coeficientes, inclusive nas repetições.
- **Classificação:** concordância com −log p/(π p^{r/2}) é **B**. A identificação exata com Guinand–Weil está
  pendente de enunciado com hipóteses (§8.5). Não houve reconstrução de dinâmica, trajetórias ou Hamiltoniano, nem
  achado classificado como **C**.

### M4 — primeira faixa nova: zeros 10.001–40.000 (protocolo m4-v1, pré-registrado e congelado)

Dez blocos de 3.000 zeros, alturas 9.879–33.190, L ≈ 2.200–2.520. As três conclusões têm critérios próprios
(PROTOCOLO §9.3); Holm entre os 10 blocos; blocos contíguos não são independentes.

**C1 — Recuperação de frequências (detecção sem catálogo). Critério pré-registrado: replicado em 10/10 blocos.**

| Bloco | Faixa inconclusiva do limiar | Detecções | Inconclusivos | Com correspondência | Sem correspondência no catálogo | p(S) (Holm) | Claramente detectáveis | Recuperação entre elas |
|---|---|---|---|---|---|---|---|---|
| b01 | [3,307; 3,336] | 34 | 0 | 34 | 0 | 1·10⁻⁴ (0,001) | 16 | 1,000 |
| b02 | [3,300; 3,324] | 34 | 0 | 34 | 0 | 1·10⁻⁴ (0,001) | 16 | 1,000 |
| b03 | [3,292; 3,316] | 34 | 1 (log 131) | 34 | 0 | 1·10⁻⁴ (0,001) | 16 | 1,000 |
| b04 | [3,276; 3,306] | 34 | 0 | 34 | 0 | 1·10⁻⁴ (0,001) | 16 | 1,000 |
| b05 | [3,283; 3,313] | 34 | 1 (log 131) | 34 | 0 | 1·10⁻⁴ (0,001) | 16 | 1,000 |
| b06 | [3,267; 3,297] | 35 | 0 | 35 | 0 | 1·10⁻⁴ (0,001) | 16 | 1,000 |
| b07 | [3,263; 3,288] | 34 | 0 | 34 | 0 | 1·10⁻⁴ (0,001) | 16 | 1,000 |
| b08 | [3,276; 3,306] | 33 | 1 (5²) | 33 | 0 | 1·10⁻⁴ (0,001) | 16 | 1,000 |
| b09 | [3,275; 3,300] | 34 | 0 | 34 | 0 | 1·10⁻⁴ (0,001) | 16 | 1,000 |
| b10 | [3,259; 3,292] | 35 | 0 | 35 | 0 | 1·10⁻⁴ (0,001) | 16 | 1,000 |

- Nenhum bloco com detecção sem correspondência no catálogo (máximo pré-registrado: 2). As mesmas 33 linhas r log p
  são detectadas nos 10 blocos. 5² é detectada em 9 blocos e inconclusiva em b08. log 131 é detectada em 2 blocos e
  inconclusiva quanto à detecção significativa em 2 (b03, b05).
- Verificação do limiar no conjunto-escore independente: a fração de máximos nulos acima do limite superior foi
  0,042–0,051 (α = 0,05). No nulo shuffle, S nulo máximo = 1 em todos os blocos.
- p(S) está no piso de resolução 1/(B+1) = 10⁻⁴. Mede incompatibilidade com o nulo de permutação de espaçamentos,
  não a probabilidade de uma interpretação física.
- Limite do critério: "claramente detectáveis" (z previsto ≥ 1,5 × limite superior) são 16 das 47 linhas por
  bloco. As outras 17–19 detecções não entram no critério de recuperação.
- Nulo GUE (secundário, 199 realizações): 23–29 detecções e 2–6 inconclusivas por bloco.

**C2 — Concordância de coeficientes (medição direcionada, não cega; Hann `band_conjugate`). Critério pré-registrado:
replicado em 10/10 blocos.**

- Em cada bloco, as 16 linhas elegíveis (resolvidas e claramente detectáveis) têm |razão − 1| ≤ 10⁻⁶: fração 1,000.
  O máximo entre elegíveis foi 4,9·10⁻¹⁰–2,6·10⁻⁹. Mediana sobre as linhas detectáveis: 1,7–3,9·10⁻¹⁰.
- Sinal e fase: Q = 1,000 e R = 1,000 em todos os blocos. p(Q) = 0,001 é o piso com 999 realizações; com Holm,
  0,010. O critério passa exatamente na resolução do controle de fase.
- Fora do critério: considerando as 47 linhas, o máximo de |razão − 1| chega a 1,63·10⁻⁶ (b08, linha fraca). As
  variantes de estimador diferem em até 1,0·10⁻⁸ nas elegíveis. Sensibilidade a ±3·10⁻⁹: mediana 5,8–7,9·10⁻¹⁰.

**Robustez Blackman–Harris (999 + 999; não seleciona resultados).** 25–28 detecções por bloco, sempre subconjunto das
detecções Hann, e nenhuma sem correspondência no catálogo. C1 e C2 também passam 10/10 com os critérios aplicados a
essa janela. Hann × BH: diferença de razão ≤ 1,4·10⁻⁷ nas linhas elegíveis; mediana 4–8·10⁻⁸ e máximo 1,7·10⁻⁶
nas 47 linhas.

**C3 — Compatibilidade estatística local (`run_20260913_160910_m2_m4_v1_m2`, 999 realizações, Holm por
estatística entre blocos; menor p ajustado atingível 0,01).**

| Referência / estatística | Blocos rejeitados (de 10) |
|---|---|
| GUE finito — CDF de espaçamentos | **10** (todos no piso 0,01) |
| GUE finito — R₂ | 1 (b02; demais p Holm 0,38–0,71) |
| GUE finito — K_c | **10** |
| Poisson — CDF, R₂, K_c | 10, 10, 10 |

- A tendência pré-registrada (CDF-GUE rejeitada em ≥ 8/10) **replica** a dos blocos 1–10.000.
- Var(s) dos zeros: 0,158–0,162, crescendo lentamente com a altura e ainda abaixo do envelope GUE (0,170–0,190).
- Nenhum veredito de "compatível" é emitido. R₂ não rejeitado em 9 blocos significa apenas ausência de rejeição com
  esse estimador e esse B.

**Secundária CUE (Bogomolny et al. 2006; descritiva, fora do domínio validado, N_eff = 1,72–1,97).**

- Em todos os blocos, a CDF corrigida fica mais próxima da empírica do que o limite. Distância RMS 0,0060–0,0080
  contra 0,0078–0,0096, mas ainda 2–3 vezes a escala de ruído amostral do ensemble GUE (0,0029).
- A correção vai na direção certa, mas **superestima** a redução de variância: predita 0,141–0,148, medida
  0,158–0,162, limite 0,180. Isso coincide com o observado antes do congelamento nos dados antigos.
- É compatível com a expansão ser inadequada em N_eff ≈ 2 (erro truncado 14–42% da correção em N = 2–3). Não é
  teste da conjectura na região de validade da fonte.

**O que sustenta e o que não sustenta.** Sustenta, como resultado numérico (B), que a transformada das ordenadas
recupera, sem catálogo, as mesmas frequências r log p em toda a faixa 10.001–40.000, com coeficientes e sinais
concordantes com −log p/(π p^{r/2}) nas linhas fortes. Sustenta também que a distribuição local difere tanto de
Poisson quanto do GUE finito de 3.000 níveis. Não sustenta reconstrução de dinâmica, trajetórias ou Hamiltoniano,
nem novidade (C). A faixa 10.001–40.000 foi analisada uma vez sob protocolo congelado; a confirmação independente
fica para 40.001–100.000.

### M4 — replicação m4-v2: zeros 40.001–70.000 (mesmo código, mesmas regras; só blocos, sementes e dados alterados)

Replicação em dados não utilizados com **o mesmo instrumento e a mesma implementação**. Não é confirmação por
implementação independente. Blocos `c01`–`c10`, alturas 33.191–54.512, L ≈ 2.190, N_eff 1,98–2,08.

**Resultado dos critérios pré-registrados: C1 replicado em 10/10 blocos; C2 replicado em 10/10 blocos; C3 com
rejeição de GUE finito (CDF, K_c) em 10/10.** Não houve falhas de critério.

| Quantidade (por bloco, mín–máx, salvo indicação) | m4-v1 (10.001–40.000) | m4-v2 (40.001–70.000) |
|---|---|---|
| Detecções (nulo primário) | 33–35 | 32–34 |
| Inconclusivos (total na faixa) | 3 (131 em b03 e b05; 5² em b08) | 2 (131 em c09; 127 em c10) |
| Detecções sem correspondência no catálogo (total) | 0 | 0 |
| p(S) | 1·10⁻⁴ (piso) | 1·10⁻⁴ (piso) |
| Fração do conjunto-escore acima do limiar | 0,042–0,051 | 0,040–0,053 |
| Claramente detectáveis = elegíveis C2 | 16 | 14–16 |
| Recuperação entre claramente detectáveis (mín) | 1,000 | 1,000 |
| Fração C2 com abs(razão−1) ≤ 10⁻⁶ (mín) | 1,000 | 1,000 |
| Máx abs(razão−1) entre elegíveis | 2,6·10⁻⁹ | 1,6·10⁻⁹ |
| Mediana abs(razão−1) entre elegíveis (pior bloco) | 3,9·10⁻¹⁰ | 5,1·10⁻¹⁰ |
| Máx abs(razão−1) nas 47 linhas (fora do critério) | 1,6·10⁻⁶ | 1,8·10⁻⁶ |
| Q (mín); p(Q) Holm | 1,000; 0,010 (piso) | 1,000; 0,010 (piso) |
| Linhas detectadas nos 10 blocos | 33 | 32 |
| Detecções nulo GUE (secundário) | 23–29 | 20–26 |
| BH: detecções; subconjunto de Hann; C1/C2 | 25–28; sim; 10/10 e 10/10 | 25–27; sim; 10/10 e 10/10 |
| Hann × BH, máx Δrazão entre elegíveis | 1,4·10⁻⁷ | 1,5·10⁻⁷ |
| C3 rejeições com Holm: GUE CDF / R₂ / K_c | 10 / 1 / 10 | 10 / **0** / 10 |
| C3 rejeições com Holm: Poisson CDF / R₂ / K_c | 10 / 10 / 10 | 10 / 10 / 10 |
| Var(s) | 0,1582–0,1624 | 0,1599–0,1633 |
| Inclinação de Var(s) com log E (descritiva) | 0,0026 | 0,0044 |
| CUE: RMS da CDF ao limite / à predição corrigida | 0,0078–0,0096 / 0,0060–0,0080 | 0,0074–0,0081 / 0,0049–0,0060 |
| CUE: Var predita (medida) | 0,141–0,148 (0,158–0,162) | 0,149–0,151 (0,160–0,163) |
| CUE: ruído amostral GUE | 0,0029 | 0,0029 |

Mudanças relatadas (descritivas):

- **log 127:** detectada nos 10 blocos de m4-v1. Em m4-v2, detectada em 6, não detectada em 3 (c02, c04, c07) e
  inconclusiva em c10. O z previsto pela amplitude de referência caiu para 3,24–3,41, contra 3,30–3,47 em m4-v1,
  junto ao limiar (limite superior ≈ 3,27–3,30). A detecção acompanha o z previsto: não detectada onde o previsto
  é ≤ 3,26. É uma mudança de detectabilidade prevista pelo instrumento, não evidência de mudança nos coeficientes.
- **5²:** inconclusiva em b08 (m4-v1) e detectada nos 10 blocos de m4-v2. **log 131:** detectada em 2, inconclusiva
  em 2 e não detectada em 6 blocos de m4-v1; em m4-v2, inconclusiva em c09 e não detectada nos demais.
- **Elegibilidade:** a regra, recalculada por bloco, excluiu p = 53 em 8 blocos e p = 47 em 1 (z previsto abaixo de
  1,5 × limite superior). O número de elegíveis caiu de 16 para 14–16 com o aumento da altura.
- **C3/R₂:** a rejeição isolada em b02 (m4-v1) não se repete. Em m4-v2, nenhum bloco é rejeitado; os p Holm vão de
  0,061 a 0,912 antes do ajuste. As rejeições de CDF e K_c persistem.
- **Var(s):** continua abaixo do envelope GUE finito e aumenta lentamente com a altura.
- **CUE:** a distância à predição corrigida diminuiu (0,0049–0,0060), mas continua 1,7–2,1 vezes a escala de ruído.
  A variância predita segue abaixo da medida em 0,010–0,013. O desvio persiste, com magnitude um pouco menor, com
  N_eff ≈ 2, fora do domínio validado. A aproximação não foi ajustada.

**Limites da interpretação.** As conclusões C1 e C2 mostraram estabilidade em duas faixas disjuntas, sob o mesmo
protocolo e o mesmo código. Os p estão nos pisos de resolução. Os blocos não são independentes, e as faixas
diferem em altura. Não houve implementação independente. Não há reconstrução de dinâmica ou de operador, nem achado
classificado como C.

### Auditoria por implementação independente (três blocos já analisados)

Plano e tolerâncias congelados antes da comparação (`independent/PLAN.lock.json`). A comparação não é cega: o autor é o
mesmo e os resultados agregados já eram conhecidos. Detalhes em [AUDITORIA_INDEPENDENTE.md](AUDITORIA_INDEPENDENTE.md).

- **Dentro da tolerância, nos três blocos:**
  - D4, D5 (razões das 47 linhas: Δ ≤ 3,3·10⁻¹¹), D6, D7 (M2: Δ ≤ 7·10⁻¹¹) e D9;
  - todas as verificações estatísticas S1–S13: σ com 1,1–1,2% de diferença mediana; limiares compatíveis; nenhuma
    linha claramente decidida com status diferente; vereditos C1 e C2 iguais; p dos envelopes M2 compatíveis.
- **Fora da tolerância, investigados:**
  - D1: FWHM da referência por `brentq`, erro relativo ≤ 2,5·10⁻¹⁰;
  - D3: consequência do deslocamento de malha. Na mesma malha, ΔF ≤ 5,5·10⁻⁹;
  - D2: condição de malha idêntica; valores dentro da tolerância;
  - D8: interpolação linear de P₁ na análise CUE da referência, erro ≤ 3,9·10⁻⁵ na CDF, efeito ≤ 0,1% nas distâncias.
  Nenhum altera C1–C3.
- **Linhas junto ao limiar:** log 127, log 131, 5², 107–139 e a elegibilidade de p = 53 e p = 47 mudam de status
  entre implementações, dentro da incerteza Monte Carlo. Isso confirma o caráter inconclusivo ou variável já relatado.
- **Não verificado:** implementação por outra pessoa ou linguagem; demais blocos; Blackman–Harris; densidade θ na
  cadeia completa.

## Limitações registradas

- Os 10.000 primeiros zeros já foram consultados por v1, v2, v3 e pela auditoria; os resultados M1–M3 não são
  confirmatórios. As faixas 10.001–40.000 (m4-v1) e 40.001–70.000 (m4-v2) foram analisadas uma única vez cada,
  sob protocolos congelados. 70.001–100.000 continua não processada.
- A replicação m4-v2 usa o mesmo código de m4-v1; um erro de implementação comum às duas não seria detectado por ela.
- Pisos de resolução na faixa nova: p(S) 10⁻⁴; p(Q) e envelopes M2 10⁻³ (Holm 0,01). Rejeições no piso não informam
  a magnitude além dele.
- Linhas perto do limiar são inconclusivas quanto à detecção significativa com B = 999. Mais realizações ou um critério com margem, se
  pré-registrados, reduziriam essa indeterminação.
- A densidade θ só foi comparada no termo suave (diferença ≤ 4·10⁻¹¹), não na cadeia completa. Inversão harmônica
  não executada.
- A comparação M2 com o modelo CUE de dimensão efetiva não foi executada.
- Calibração sintética limitada pela positividade da densidade nos blocos que começam em γ₁: 33 linhas no pilot,
  63 no full.
- Sem Git: os fontes de cada execução são copiados para `results/<run>/code/`, e o m3-v2 para `archive/code_m3-v2/`.
- O pico agregado de memória com 4 processos não é medido.

## Log de atividades e decisões

- **12/09/2026:** Etapa 0 (protocolo v1). Implementação inicial M1–M3 e execuções v1 (depois invalidadas).
- **13/09/2026 — auditoria e revisão:**
  - Quadratura do termo suave com aliasing (picos espúrios a cada ~0,4066). Instrumento substituído por NUFFT
    validada contra soma direta (erro ≤ 7·10⁻¹⁰) e quadratura composta com teste de convergência. O custo por
    realização caiu de ~33 s para ~30 ms.
  - Nos zeros, a escala de ruído interna faz lóbulos laterais parecerem significativos. A escala passou a vir de
    σ_nulo(t) calculado nos controles.
  - GUE denso (raio 1/√2) e tridiagonal (diagonal com variância pela metade) corrigidos. O teste de
    concordância denso × tridiagonal passou a exigir variância 0,16–0,20 e diferença < 0,015. Medido no M1:
    0,1803 × 0,1774, distância sup entre CDFs 0,008.
  - Normalização de R₂ por contagem fixa, média de Montgomery por bin e termo desconectado de Hann corrigidos.
    Algoritmo de pares por offsets vetorizados.
  - Relatórios passaram a conter apenas afirmações derivadas das métricas medidas.
  - Testes: 25 aprovados (invariância por permutação, NUFFT × direta, resposta de Hann, recuperação de amplitude
    e fase por injeção nos níveis, detector, catálogo, matching um a um, ajuste conjunto, controles, R₂ de Poisson
    plano, rampa GUE do K_c).
  - Protocolo m3-v2 congelado após pilot/dev/val, antes de holdout/full.

- **13/09/2026 (tarde) — resposta à auditoria `docs/ANALISE_RESULTADOS.md`:**
  - Confirmadas e corrigidas todas as observações de prioridade 1 e 2 que envolvem código (PROTOCOLO §8.1):
    estatística de decisão assimétrica, reuso de nulos entre limiar e escore, janela e densidade não propagadas,
    blocos M2 fixos, manifestos sobrescrevíveis, fator 2 na validação, teste de envelope não simétrico, relato de
    memória, recuperação do código.
  - Reclassificações de interpretação registradas (§8.5): Guinand–Weil como B, τ = 1 como heurística, Bogomolny
    com CUE, R versus Q para fase.
  - m3-v2 preservado e verificado contra o lock. m3-v3 pré-registrado antes de rodar. Hann congelado após
    pilot/dev/val; BH congelado antes de sua primeira execução.
  - Testes: 35 aprovados, 10 novos. Eles cobrem: pico fora da malha com decisão igual com ou sem refinamento;
    propagação e rejeição de janela/densidade; resposta Blackman–Harris; recuperação por injeção com BH; estimador
    com conjugado exato quando o conjugado vaza; critério estrito da validação; vínculo validação/conjunto; blocos M2
    obrigatórios; calibração do teste simétrico; integração do M3 com conjuntos nulos disjuntos.
  - A contagem do holdout passou de 36 para 35, reproduzindo a auditoria. A análise mostrou que `log 131` também
    fica dentro da incerteza Monte Carlo do limiar.

- **17/09/2026 — Etapa 11 (fontes e matriz):** fontes F1, F2, F3, F4, F6, F11 e J1 lidas com página (F5 e F7 parciais);
  matriz de operadores atualizada com evidências (K2a, K3a, K4, K5a, K5b, K7, K8, K9); 27 entradas sustentam decisão,
  1 pendente (K7 M4). Análises em [ETAPA11_K5B_ANALISE.md](ETAPA11_K5B_ANALISE.md) e
  [ETAPA11_PENDENCIAS_DERIVACAO.md](ETAPA11_PENDENCIAS_DERIVACAO.md). **11.3b encerrada** com itens abertos
  ([ETAPA11_3B_ENCERRAMENTO.md](ETAPA11_3B_ENCERRAMENTO.md)). 11.6: K12 e controle Dirichlet declarados em
  `results/etapa11_6_controles/`.
- **19/09/2026 — texto anterior da linha 11 da tabela (substituído por estar desatualizado; preservado aqui):**
  > | 11 | Fórmulas de traço e classes de operadores | M4 | `em execução` | 14/09/2026 | Plano e matriz **preliminar** revisados em 11.3: [ETAPA11_PLANO.md](ETAPA11_PLANO.md), [ETAPA11_MATRIZ_OPERADORES.md](ETAPA11_MATRIZ_OPERADORES.md), `etapa11_matriz_operadores.csv`, `etapa11_evidencias.csv` | Seis pontos da auditoria e ajustes 11.3b-1 tratados (N1 de K5a/K7/K9 → PC; campos `situacao`/`conferencia`; fontes arquivadas com SHA-256 em `archive/fontes_etapa11/`); códigos não usáveis para seleção/exclusão enquanto houver PC (matriz §0.3, 11.3b); 11.4 concluída como entrega documental preliminar ([ETAPA11_CORRESPONDENCIAS.md](ETAPA11_CORRESPONDENCIAS.md), `etapa11_correspondencias.csv`, 20 relações; ajustes 11.4-1), sem liberar seleção ou congelamento de testes; 11.3b **encerrada em 17/09/2026** com itens abertos registrados ([ETAPA11_3B_ENCERRAMENTO.md](ETAPA11_3B_ENCERRAMENTO.md); estado ao encerrar: [ETAPA11_3B_FORMULA_EXPLICITA.md](ETAPA11_3B_FORMULA_EXPLICITA.md): L-EF1 parcial (termo arquimediano derivado em H2: [ETAPA11_3B_TERMO_ARQUIMEDIANO.md](ETAPA11_3B_TERMO_ARQUIMEDIANO.md); aplicabilidade a 𝒢 depende de F5; classe suficiente 𝒜 em [ETAPA11_3B_ADMISSIBILIDADE.md](ETAPA11_3B_ADMISSIBILIDADE.md) com Z1 derivado em [ETAPA11_3B_Z1_CONTAGEM.md](ETAPA11_3B_Z1_CONTAGEM.md), certificado intervalar com cauda analítica; L-EF1: fechamento documental pendente de F5 e J1; H1 formulada em [ETAPA11_3B_H1_FORMULACAO.md](ETAPA11_3B_H1_FORMULACAO.md) e [ETAPA11_3B_H1_R5_ESTIMADOR.md](ETAPA11_3B_H1_R5_ESTIMADOR.md): S1 quantificado, S3b derivada condicionalmente com taxa O(ε²) e constantes independentes de t e ε, R5 formalizado com S2-ratio (implementado) × S2-complexo (extensão) e cálculo finito B sob declaração prévia em `results/etapa11_r5/`; cruzamento exploratório com C2: contaminação > τ só em linhas não elegíveis; diagnósticos de R5 encerrados; Lema de Cauda Projetada proposto e Q_k(u) derivado ([ETAPA11_3B_H1_CAUDA_PROJETADA.md](ETAPA11_3B_H1_CAUDA_PROJETADA.md): frequências nas bordas A, B; Rota B incondicional insuficiente; cota-alvo uniforme em ε e η formulada; B_main derivada por deslocamento de contorno; representação R-EF-χ fixada, sem truncamento em altura; proposição P-RH: cota uniforme em ε condicional a RH; força avaliada sob declaração (híbrida): com Lema 5′, majorante < 1e-6 em 361/461 pares elegíveis; zeros dominam; passagem ao truncamento abrupto derivada (P-RH-trunc); termo de transição Θ_k(U₂) calculado sob declaração (B): margens todas positivas, orçamento inalterado; para reduzir a majorante, zeros são o gargalo; decomposição da parcela dos zeros: L₂ e janelas adjacentes dominam; Lema 4′ derivado e avaliado sob declaração (híbrido, sob RH): condição suficiente ≤ 1e-6 em 461/461 elegíveis com d₁ = 8; **certificada computacionalmente em (8, 2), condicional a RH, para M^math** (execução 1 inválida por enclausuramento; execução 2 substituída por lacunas de justificativa; execução 3 substituída; execução 4 vigente e congelada, com adendos 1–3, c₁ e c₂ recalculados internamente e testes T1–T9): 461/461 elegíveis, 1.178/1.410 pares; **resíduo contra o catálogo 𝒦 certificado (§II.21, `DECLARACAO_CERT_CONTAMINACAO.md`): |a_k·(F* − M_𝒦)| ≤ 10⁻⁶|c_k| sob RH, para M^math, em 461/461 elegíveis (máx 6,6091·10⁻⁷) e 1.093/1.410 pares, sem corte em U₂; testes T1–T15; termo determinístico ρ_Δ certificado (§II.22, `DECLARACAO_CERT_DENSIDADE.md`): |a_k·(F^rvm − M_𝒦)| ≤ 10⁻⁶|c_k| sob RH, para M^math, em 461/461 elegíveis (máx 6,6213·10⁻⁷) e 1.089/1.410 pares, com a cota de densidade recalculada sob a base atual (dependência herdada eliminada); testes T1–T21; erro das ordenadas ρ_ord certificado (§II.23, `DECLARACAO_CERT_ORDENADAS.md`): |a_k·(F^tab − M_𝒦)| ≤ 10⁻⁶|c_k| sob RH e H-tab (não certificada), para M^math, em 461/461 elegíveis (máx 7,313·10⁻⁷) e 1.024/1.410 pares; testes em duas rodadas (rodada 1 preservada); camada numérica ρ_num (§II.24, `DECLARACAO_CERT_NUMERICO.md`): fidelidade (N) incondicional |r̂_k − X_k/c_k| ≤ 6,3·10⁻¹¹ nos elegíveis e ligação (T) |r̂_k − 1| ≤ 10⁻⁶ sob RH e H-tab em 461/461 elegíveis (1.024/1.410 pares), sem alarmes; C2 inteiro, S1, S3a, S3c e auditoria independente pendentes; protocolo de auditoria em [PROTOCOLO_AUDITORIA_CERTIFICADO.md](PROTOCOLO_AUDITORIA_CERTIFICADO.md)**; auditoria integral independente pendente; Lema C formulado; passagem ao estimador registrado pendente); H1 aberta), L-EF2a/b revisadas em 11.3b-2/3 (completude da tabela B nos 30 blocos, fator 2, restos com prefatores, cota certificada do termo determinístico), L-EF2c aberta; fontes F1–F7 `bloqueado` por acesso de rede ([ETAPA11_PENDENCIAS_FONTES.md](ETAPA11_PENDENCIAS_FONTES.md)), C02 derivada, C11/C19 PC por fontes inacessíveis; checagens em `results/etapa11_3b/`); 11.5–11.6 pendentes; nenhum candidato implementado; `candidates.py` segue como rascunho não avaliado |
- **19/09/2026:** derivação D1 do controle Dirichlet escrita (P1 e P2 conferem, sem adendo). Ponto de retomada em
  [ESTADO_ATUAL.md](ESTADO_ATUAL.md).

### M4 — faixa final m4-v3 (70.001–100.000), primária + reprodução

Detalhes em [RELATORIO_CONSOLIDADO.md](RELATORIO_CONSOLIDADO.md) §5 e §9.

- **Primária:** C1 e C2 replicados em 10/10 blocos, sem detecção sem correspondência no catálogo. C3 rejeita GUE
  finito em CDF e K_c (10/10) e não rejeita R₂ (0/10). Blackman–Harris também replicou 10/10.
- **Reprodução:** determinísticas D1–D9 dentro da tolerância em todos os blocos; vereditos de família idênticos. As
  diferenças de status ocorrem só em linhas não claramente decididas.
- **Regras:** R2 acionada (S4 em d05, d09, d10). A causa é erro de desenho do plano: S4 centrado em α em vez de
  (B+1−u)/(B+1). Ver `results/m4_v3_joint/INVESTIGACAO_R2.md`. R2 permanece registrada; R1, R3 e R4 não foram
  acionadas.
- **Todos os 100.000 zeros foram usados.** Não resta faixa reservada nesta tabela.

## Próximo passo

**Atualizado em 19/09/2026 (detalhes em [ESTADO_ATUAL.md](ESTADO_ATUAL.md) §5–§6):**
- 11.6, controle `ctrl-dirichlet-v1`: declaração e derivação D1 prontas; próximo é o código novo (cálculo dos zeros de
  L(s, χ), verificações V1–V4, caminho novo no instrumento) e testes; depois piloto, cálculo completo e execução.
- 11.5: protocolo dos testes discriminantes (não iniciado).
- Controles dinâmico e aritmético da 11.6: dependem de dados (tabela de níveis do estádio; autovalores de Maass com
  paridade).

Registro anterior (14/09/2026):

1. Etapa 11 (classes de operadores), com fontes primárias.
2. Verificações abertas:
   - implementação por outra pessoa ou linguagem;
   - densidade θ na cadeia completa;
   - inversão harmônica;
   - corrigir S4 numa versão futura do plano: centrar em (B+1−u)/(B+1), incluir a variabilidade do limiar estimado e calibrar a regra conjunta sem pressupor independência entre blocos sem justificativa.
3. Confirmações adicionais exigiriam dados novos (tabelas de maior altura); os 100.000 zeros já foram consumidos.


### 19/09/2026 — caderno de hipóteses e revisão de escopo

- **Estado:** entrega documental `validado`; experimentos propostos `não executado`.
- Criada a pasta [hipoteses](../hipoteses/README.md): balanço do projeto, seis perguntas candidatas, bibliografia parcial, sequência de trabalho e revisão do estudo de poder recebido nesta sessão.
- Prioridades propostas: previsão transferível de erros espectrais (P-R1) e simetrias/filtros aritméticos em Collatz (P-C1, ligado a CL0–CL5). Não há achado novo reivindicado nem protocolo experimental congelado nessa pasta.
- O registro espectral v2 permanece vigente. Registradas ressalvas sobre sinal/ruído versus poder, dependência estatística e o expoente bibliográfico de H-002; nenhum protocolo existente foi alterado.
- Executado: leitura documental, busca web dirigida, aquisição de fontes, conferência de hashes e links locais. Sem novos zeros, simulações ou commits; código científico congelado preservado.
- Próximo: resolver a interpretação do poder antes da produção do estádio, concluir a triagem bibliográfica de P-R1 e preparar CL0. Ver [plano](../hipoteses/PLANO.md).

### 22–25/09/2026 — `ctrl-dirichlet-v1`: zeros calculados, V1/V2 reprovadas, passe de completude D3

- **Estado:** χ₋₄ `validado` depois do passe D3 (falta a V2′); χ₅ `em execução` (passe D3 rodando); o resultado
  original das duas execuções é `inconclusivo` por falha de completude e fica preservado como está.
- **Execuções do script congelado** `dirichlet/dirichlet_zeros.py` (`65056bc2…`), 12.000 zeros por caractere:
  χ₋₄ terminou 22/09 08:41 (142.714 s, 295.458 avaliações, 1 retomada); χ₅ terminou 24/09 13:51 (273.409 s,
  295.351 avaliações, 2 retomadas, sendo uma por reinício da máquina em 22/09 ~21:00).
  Nos dois, **V3 e V4 passaram e V1 e V2 reprovaram**: `all_checks_passed: false` nos dois manifestos.
- **Diagnóstico** (`dirichlet/completude/DIAGNOSTICO_V1V2.md`, `2fdacab5…`): a varredura com passo d̄/8 perde **pares**
  de zeros separados por menos de um passo. Em χ₋₄, sete pares (14 zeros), com separações de 0,0247 a 0,0896 contra
  passo local de 0,0914 a 0,1005; S = N − θ/π mostra platôs planos com degraus de exatamente −2. Descartados salto de
  ramo em θ (Stirling, ≤ 3·10⁻²⁰) e falha de refinamento (`bisection_fallbacks: 0`). Rótulo B.
- **Adendo:** [ADENDO_DIRICHLET_3.md](../results/etapa11_6_controles/ADENDO_DIRICHLET_3.md) (`02340a5c…`), gravado
  antes do código e da execução do passe; fixa Etapas A/B/C, o certificado D3-C1, as re-verificações V1′–V4′, o custo
  e três previsões falsificáveis (§8).
- **Código novo:** `dirichlet/completude/completude_d3.py` e `test_completude_d3.py` (5 testes, 243 s, todos passaram).
  O script congelado é importado, nunca editado.
- **Passe D3 em χ₋₄** (23/09 04:30; 23.096 s; 47.373 avaliações): Etapa A varreu 802 intervalos acima de 1,6 d̄ com
  passo d̄/32 e recuperou **14 zeros**; Etapa C não foi necessária. Certificado D3-C1 fecha (medianas +0,498 → +0,500,
  dispersão 0,04); V1′ com diferenças −0,087, +0,335, +0,067, +0,201 (tolerância 3,0); V3′ e V4′ passaram.
  Dado de trabalho: `zeros_chi_m4_12000_completo.txt` (`81fdfc0a…`), 11.986 zeros originais + 14 recuperados,
  γ_último 9.749,443063 (era 9.758,910852). **Nenhum zero original foi alterado** (previsão §8.2 confirmada);
  previsão §8.3 confirmada.
- **χ₅:** déficit medido pelo certificado na lista original = **6 zeros** (3 pares), dentro da previsão §8.1 (5 a 30).
  Limitação registrada: a regra de localização de degraus do D3-C1 (|m_{j+1} − m_j| ≥ 1,5) só apontou 2 das 3 regiões,
  porque um degrau no meio de uma janela se divide entre duas medianas. Isso **não** produz falso positivo — a
  condição de nível continua reprovando a lista —, mas tornaria a Etapa C incompleta se ela fosse necessária.
- **Desvio operacional registrado:** o §7 do adendo previa interromper χ₅ com SIGTERM antes de a V2 do script congelado
  avançar; não havia ninguém na máquina quando a varredura terminou e a V2 rodou inteira (117.564 s), acusando 3.002
  contra 3.000 no bloco alto. Nada científico muda: a V2′ do §5 é exigida de todo modo.
- **Em execução (25/09 14:45):** passe D3 de χ₅ (790 intervalos) e V2′ de χ₋₄ (varredura com passo d̄/16 no bloco
  9001–12000, mais o passe de completude na lista recomputada).
- **Próximo:** V2′ de χ₅; depois o instrumento do controle nos 8 blocos das listas corrigidas e, só então,
  `preditor_pr1_v2.py` da H-004.

### 25/09/2026 — mudança de direção: custo de CPU passa a exigir previsão; estádio encerrado por prioridade

- **Estado:** regra `validado` (documental); estádio `encerrado por prioridade`; diagnóstico do estádio `em execução`
  com classificação limitada.
- **Regra nova:** [ADENDO_REGISTRO_v2_2.md](../results/registro_hipoteses/ADENDO_REGISTRO_v2_2.md) (`0b505348…`) —
  "nenhuma produção longa sem ganho científico discriminante, viabilidade demonstrada e custo limitado". Longa = acima
  de 4 horas-CPU acumuladas; estudo de viabilidade tem exceção com teto, réplicas e regra de parada declarados; poder
  só decide por intervalo de Wilson, nunca por frequência pontual.
- **Errata 1** (`b56b0470…`): o estudo de poder do estádio em execução estima **marginais**, com G, g01 e g04 gerados
  como espectros independentes, e não estima o critério conjunto; reclassificado como **diagnóstico preliminar**, que
  não autoriza produção. Teto real passou a ser `RLIMIT_CPU` (86.400 s no PID 206589, `NLWP = 1` conferido), porque
  `timeout` mede parede e `nice` não é orçamento. Extensão sequencial de 40 para 60 réplicas **revogada** (não preserva
  cobertura de 95%). Sementes derivadas de `hash((name, cond))` variam entre processos e não são gravadas: a execução
  **não é reproduzível** e carrega essa limitação.
- **Errata 2** (`9deef4f6…`), da segunda revisão do usuário: (i) marginal abaixo do alvo **não** reprova — reprovar
  exige o limite **superior** de Wilson abaixo do alvo, e encerrar por orçamento ou prioridade é outra coisa, que não
  se relata como insuficiência demonstrada; (ii) a cota P(conjunto) ≤ min(marginais) exige marginais do **mesmo**
  experimento, e não foi demonstrado que sub-blocos independentes representem os que seriam extraídos de G, logo o
  diagnóstico não estabelece cota para o desenho conjunto nem para o estádio real; (iii) "amplitude não prevista" ≠
  "amplitude prevista igual a zero" — `ratio_to_theory` e `phase_error_rad` dessas linhas saem como **não aplicável**,
  com motivo, e os brutos e avisos ficam preservados; (iv) descartada a minha proposta de usar marginais ≥ 0,9 para
  rebaixar E-C2bb a descritivo, que seria escolher uma versão mais fácil do controle a partir do diagnóstico.
- **Decisão:** produção do estádio bloqueada e desenho atual **encerrado por prioridade**, não por insuficiência
  demonstrada. Sem desenho conjunto e sem produção reduzida nesta rodada. O diagnóstico termina dentro do teto, é
  relatado com a classificação limitada e tem o custo de CPU medido.
- **Fila:** fechar a V2′ de χ₋₄ → H-004 quando as dependências dela estiverem satisfeitas (declaração §5: verificações
  do controle, instrumento nos 8 blocos, depois o preditor) → P-R1, bibliografia e CL0.
- **CL0 delegado** à outra sessão local (`hipotese-riemann-6c`), por pedido do usuário, com o escopo, as regras de
  rótulo e pré-registro, os limites de arquivo (nada em `src/riemann_spectra`, nada nas pastas com processos rodando) e
  o estado de F-001 a F-003.

### 25/09/2026 — CL0: especificação, protocolo e configuração do laboratório Collatz

- **Estado:** CL0 `validado` como entrega **documental**; CL1 `não executado`; CL2–CL5 `pendente`. Nenhum experimento
  foi executado e nenhuma afirmação de novidade é feita.
- **Entregues** em [results/collatz_cl0](../results/collatz_cl0/README.md), os três congelados com hash:
  `ESPECIFICACAO_CL0_v1.md` (`5556a070…`), `PROTOCOLO_CL0_v1.md` (`29ca9d5b…`) e a configuração
  `collatz_cl1_v1.toml` (`7d00d0ef…`).
- **Especificação:** separa Σ₂, ℤ₂, Q_ímpar, ℤ e ℕ_{>0}, com invariância e medida de cada um; fixa a convenção T-tempo
  (ciclo {1,2} com período 2) e a conversão para C-tempo; dá ficha de \(\mathcal L_g\), \(P\), \(U\) e \(\mathcal L_+\)
  com espaço, medida, norma e domínio antes de qualquer palavra sobre espectro; e lista nove observáveis (O1–O9) com
  mapa, espaço, medida, normalização, significado e rótulo máximo sustentável.
- **Fatos A com página:** conjugação Φ∘S∘Φ⁻¹ = T e vetor de paridades (Bernstein–Lagarias, pp. 1–2); Aut(S) = ℤ/2ℤ com
  V(x) = −1−x (p. 2); Conjectura de Periodicidade e sua equivalência com a autoconjugação (p. 3; Monks–Yazinski,
  Teorema 2.1, p. 3). Registrada a correção do usuário: Ω(3) = −4/9 (Monks–Yazinski, Exemplo 2, p. 3), logo Ω **não**
  leva positivos em negativos embora V leve.
- **Derivações próprias** (Anexo A, elementares e a reverificar como B em CL1/CL4): F_n = 2ⁿ e ζ_T = (1−2z)⁻¹; a
  fórmula exata do ciclo x = b/(2ⁿ−3ᵏ) com conferência das palavras de comprimento 1 e 2; contração de razão
  exatamente 1/2 dos dois ramos inversos em ℤ₂, com P**1** = **1** reverificando a conservação de Haar; e
  \(\|\mathcal L_+\|_{\ell^1}=1\), \(\|\mathcal L_+\|_{\ell^2}=\sqrt2\), \(\|\mathcal L_+\|_{\ell^\infty}=2\).
- **Pré-registro:** oito verificações com **resposta conhecida antes da execução** (F_n, c_n de Lyndon, Möbius nos dois
  sentidos, coeficientes da zeta, soma ponderada (a+b)ⁿ, Fix(T) = {0,−1}, Fix(T²) = {0,−1,1,2}, ciclo positivo {1,2}).
  Reproduzi-las é B e só B. **Divulgado no próprio protocolo:** esses valores foram conferidos por cálculo de rascunho
  no diretório temporário da sessão antes de serem congelados — segundos de CPU, sem artefato em `results/`, sem
  manifesto; isso não é o piloto de CL1.
- **Custo:** aplicado o adendo 2 do registro v2 (`0b505348…`, erratas `b56b0470…` e `9deef4f6…`). CL0 é texto e não é
  produção; CL1 recebe teto de segurança de 0,5 hora-CPU com `OMP_NUM_THREADS=1` e parada por orçamento; CL2 em diante
  é exponencial no período e exige configuração nova, benchmark e, acima de 4 horas-CPU, os quatro requisitos do §3.
- **Desvio registrado:** o plano propunha `src/riemann_spectra/collatz/`; como o código de m3/m4 está congelado e sob
  lock, o pacote novo será `collatz/` na raiz. Nada em `src/riemann_spectra/`, em `configs/*.lock.json` ou nas pastas
  das três execuções em andamento da 11.6 foi tocado.
- **Fonte nova:** o PDF de Bernstein & Lagarias, cujo download falhou em 19/09 (403/429), foi obtido em 25/09 —
  `archive/fontes_etapa11/collatz_cl0_20260925/bernstein_lagarias.pdf` (`476b0149…`, 16 pp., cópia do autor), com
  `aquisicao.json` próprio e linha no `MANIFESTO.csv`. O registro da falha de 19/09 foi preservado. F-003 segue
  `proposta`: a triagem não muda, só o estado da fonte.
- **Executado nesta entrega:** leitura de fontes (pp. 1–3 e 15 de Bernstein–Lagarias; pp. 2–3 de Monks–Yazinski),
  redação, conferência de hashes citados e validação sintática da configuração. Sem commit.
- **Próximo:** CL1 — criar o pacote `collatz/` com testes de invariantes e executar o piloto de períodos 1–12 sob a
  configuração congelada. Não iniciado aqui.

### 25/09/2026 (tarde) — orçamento medido do instrumento e identidade dos dados da H-004

- **Orçamento** (`dirichlet/orcamento/ORCAMENTO_INSTRUMENTO.md`, `2e67b472…`, com
  `ORCAMENTO_INSTRUMENTO_ANEXO1.md`, `54339d77…`): medido **só com níveis sintéticos** (bordas dos blocos por N̄_χ⁻¹
  nos índices, substitutos GUE, nenhum bloco reservado aberto). Custos por bloco de 3.000 zeros: nulo shuffle 341 s
  (e02) a 453 s (f04), nulo GUE 226 s, calibração sintética 58 s, aritmética 67 s (valor conservador), instrumento
  ~1 s. **Oito blocos: 1,55 a 1,8 hora-CPU**, 1,3 a 2,4 h com margem de ±30% — abaixo do limiar de 4 horas-CPU que
  define produção longa. Retomada por bloco, sem checkpoint interno (perda máxima de ~14 min de CPU).
- **Decomposição da aritmética, medida variando uma contagem por vez** (anexo 1): base 4,16 s; controle de fase
  **0,000204 s por realização** (999 realizações = 0,20 s, 0,5% da etapa); precisão **1,948 s por perturbação**
  (20 = 38,96 s); rms 0,069 s. Threads = 1 conferido no processo; CPU por `getrusage` incluindo filhos; razão
  CPU/parede 0,87–0,89 por contenção. Custo do próprio exercício: ≈ 0,18 hora-CPU.
- **Caminho dirigido mais barato descartado:** construção + aritmética nos 6 blocos reservados custaria ≈ 0,15 h-CPU
  contra 1,55–1,8 h do controle completo. A economia não paga adendo, verificação de equivalência e código novo.
  Recomendação registrada: executar o controle como declarado.
- **Identidade dos dados** (`results/registro_hipoteses/H-004/ADENDO_H004_2.md`, `a5d071be…`): conjunto de dados = lista
  corrigida pelo D3 (`zeros_chi_m4_12000_completo.txt`, `81fdfc0a…`; manifesto `851a6c95…`), com o vínculo à execução
  reprovada preservado. **Valores inalterados, contagem igual (12.000), indexação mudou a partir do índice 4223**:
  bordas 6.000, 9.000 e 12.000 correspondem aos índices originais 5.996, 8.990 e 11.986; e01 é idêntico; e02 ganha 4
  recuperados, e03 ganha 6, e04 ganha 4 e o topo recua para 9.749,443063. Reserva **não** reduzida. Registrado o acesso
  já ocorrido aos blocos reservados pelo passe D3 (larguras, θ e certificado; nenhuma observável do instrumento).
- **Carregador:** `preditor_pr1_v2.py` preservado; `preditor_pr1_v3.py` difere só na pré-condição e nos caminhos, exige
  as cinco verificações do manifesto D3 e o SHA-256 do arquivo analisado, e só roda depois de um teste de equivalência
  que mostre `blocks` idêntico ao de v2 nas entradas em que v2 roda. χ₅ entra por complemento hasheado.
- **CL0** encerrada como entrega documental (outra sessão), com a divulgação do rascunho preservada; **CL1 não
  executada** nesta rodada.
- **Sequência acordada:** orçamento fechado → validação dos dados corrigidos (V2′ em curso; passe de χ₅ em curso) →
  complemento de identidade de χ₅ → controle completo nos 8 blocos → H-004, sem ajuste entre as duas análises.

### 25/09/2026 — pesquisa bibliográfica e perguntas além da calibração

- Entrega documental em `hipoteses/RODADA_BIBLIOGRAFICA_20260925.md` e `PERGUNTAS_20260925.md`: quatro fontes primárias obtidas e parcialmente lidas, com hashes e proveniência. Propostas P-R5/P-R6/P-C2a **pendentes**, sem alegação de novidade.
- `results/collatz_cl0/ERRATA_CL0_1.md` separa Q_odd como pontos eventualmente periódicos do shift da inclusão Φ(Q_odd)⊆Q_odd para Collatz; a igualdade não é assumida. Textos congelados preservados.
- Verificações desta entrega: hashes dos PDFs, manifesto e congelamento CL0; links locais dos documentos novos. Sem simulação, CL1, leitura de dados reservados ou interferência nas validações. H-004 mantém a sequência autorizada. Sem commit.
- Próximo trabalho documental: especificar P-R5, aprofundar antecedentes e formular limites de identificabilidade; Collatz requer confronto com literatura de operadores antes de promover proposta a teste.

### 25/09/2026 — plano complementar de dependências e transientes de Collatz

- Criado `hipoteses/PLANO_COLLATZ_DEPENDENCIAS_TRANSIENTES.md`, a pedido do usuário: alvo principal sobre variância normalizada das árvores inversas e dependências entre palavras; alvo secundário sobre sobrevivência finita antes de chegada/saída. São formulações propostas, não teoremas demonstrados nem lacunas estabelecidas.
- C-D0 **validado** como entrega documental; C-D1–C-D3 **pendentes**; C-D4–C-D5 **não executados**. A leitura de fontes próximas deve anteceder qualquer piloto. Atualizados os vínculos no plano Collatz e no índice de hipóteses.
- Nenhuma enumeração, experimento, acesso a dados reservados ou mudança na CL0 congelada. Próximo: revisão dos momentos/dependências nas fontes primárias e do estado posterior em Wirsching/citações. H-004 e as validações mantêm a sequência própria. Sem commit.

### 25/09/2026 — ampliação para investigar ponte direta Collatz–Riemann

- A pedido do usuário, criado `hipoteses/PLANO_PONTE_DIRETA_COLLATZ_RIEMANN.md`. Prioridade: conferir Meinardus (2001), cujo resumo institucional relaciona Collatz a um núcleo de séries de Dirichlet gerado por ζ. Fonte completa **não conferida**: acesso ao PDF bloqueado por 403/antibot; falha arquivada. Isso não é evidência sobre zeros ou RH.
- Separados os alvos de relação funcional, relação com zeros e consequência para localização. Rotas alternativas: séries de órbitas e operador/traço/determinante; todas **pendentes** de derivação. Documentos de planejamento anteriores vinculados ao novo escopo.
- Nenhum cálculo científico, enumeração, acesso reservado ou alteração de protocolo congelado. Próximo: obtenção/leitura do antecedente e ficha de um primeiro passo não tautológico. Sem commit.

### 25/09/2026 — P1 da ponte direta: leitura de Meinardus (2001)

- PDF obtido pelo usuário via Tor (pasta de downloads do Tor Browser), copiado somente-leitura para `archive/fontes_etapa11/ponte_collatz_20260925/meinardus_2001_mannheim261.pdf` (SHA-256 `08ebcc73…`, 15 pp.). Proveniência em `aquisicao_tor_usuario.json` (a falha 403 anterior foi preservada); linha nova no `MANIFESTO.csv`; B18 em `hipoteses/BIBLIOGRAFIA.md`.
- Nota `hipoteses/leituras/B18_MEINARDUS_2001.md`: texto inteiro lido; Teors. 1–5 conferidos nas imagens. **P1 (Meinardus): validado.** Resultado negativo para o nível 2: ζ é o gerador trivial (a sequência constante é invariante sob qualquer τ, e Tζ = (1−2^{−s})ζ é identidade). Os zeros de ζ não codificam Collatz nessa construção (A). A obstrução multiplicativa (τ não respeita o produto de Euler) fica como heurística (D).
- Pontos de atenção registrados: índice n=1 em (8) é erro tipográfico por n=0; a troca soma–integral de Perron não foi auditada.
- Citações posteriores: busca breve com três candidatas **não lidas**; pendente. Sem cálculo, enumeração ou alteração de protocolo congelado. Sem commit.
- Próximo: ficha P2, com uma propriedade que mude ao trocar τ e interaja com a estrutura multiplicativa; primeira pergunta concreta: a limitação de D ↦ D_τ no H² de séries de Dirichlet.
- Varredura bibliográfica Collatz–Riemann registrada em B18 §5: **nenhuma ligação com ζ ou com seus zeros além do gerador trivial**. As bibliografias anotadas de Lagarias não mencionam zeta; a série de Siegel usa Perron sem ζ; Bell–Lagarias (2015) mostram fronteiras naturais, o que restringe a rota 2. Siegel I.5 e Bell–Lagarias ficam **pendentes** de leitura integral.

### 26/09/2026 — leitura de Bell–Lagarias (2015) e Siegel (Parte I.5)

- PDFs do arXiv arquivados somente leitura em `archive/fontes_etapa11/ponte_collatz_20260925/`, com duas linhas novas no `MANIFESTO.csv`. Notas `hipoteses/leituras/B19_BELL_LAGARIAS_2015.md` e `B20_SIEGEL_2021_PARTE_I5.md`; entradas B19/B20 na bibliografia.
- **Retificação de B18 §5:** a fronteira natural de Bell–Lagarias **não** obstrui a rota 2 em séries de Dirichlet. Contraexemplo (A): m ≡ 0 (mod 3). A continuação depende da distribuição de O⁻(m), via Mellin em t → 0⁺.
- **Siegel:** ζ entra como série da constante x; seus zeros não têm papel. Erro encontrado: (2.25), (2.26) e os resíduos do Cor. 2 estão errados como impressos. Derivei formas corrigidas e as conferi numericamente: impressas falham; corrigidas batem a ≤1e-12 em q=3,5,7. A confirmação independente vem da Prop. 1 do autor (polo duplo em s=1 independente de x). Comandos: `python3 hipoteses/leituras/verificacoes/siegel_2111_07883_original.py` (31 s) e `…_corrigida.py` (112 s); log ao lado. O Teor. 3 não é afetado.
- Conclusão: nenhuma das três fontes com série de Dirichlet de Collatz (Meinardus, Siegel e a leitura de Mellin de Bell–Lagarias) liga Collatz aos zeros de ζ. Em todas, ζ aparece como série da constante. Candidata a P2 (D): densidade e termo de erro de O⁻(5)/O⁻(16), ainda sem mecanismo para os zeros. Sem commit.

### 26/09/2026 08:00 — situação das execuções (consulta do usuário)

- **V2′ de χ₋₄** (PID 201421, `completude_d3.py --carater chi_m4 --v2`): `em execução` há 17 h 12 min (16 h 51 min de CPU, sem `RLIMIT_CPU`). A varredura com passo d̄/16 está em t ≈ 9.524 do bloco alto [≈7.561, ≈9.749], com 2.688 zeros recomputados, 86.436 avaliações e 0 re-varreduras de lacuna, ou seja, ≈ 90% do bloco. Estimativa de término: ~2 h. O log de stdout está vazio; o progresso sai só pelo checkpoint `progresso_d3_v2_chi_m4.json`. Autorizada pela fila de 25/09, depois da regra de custo (acima de 4 h-CPU, portanto execução longa).
- **Passe D3 de χ₅:** **terminou 26/09 04:42** (Etapa A: 790 intervalos, 50.018 s; 6 zeros recuperados em 3 intervalos; Etapa C: 0; lista corrigida com 12.006 zeros; certificado B `passed=True`, medianas +0,492 → +0,495). χ₅ passa a `validado` após D3, e falta a V2′. Registro anterior "χ₅ em execução" desatualizado.
- **Diagnóstico de poder do estádio:** **terminou com erro** em 25/09 22:01, depois de 24.069 s. Completou G (com e sem sinal) e g01/com_sinal (40/40 réplicas); abortou em g04 com `ValueError: FWHM 0.3381 grande demais para a calibração sintética` (`instrumento_estadio.py:419`). JSON parcial preservado em `estadio/estudo_poder_estadio.json`. Estado: `inconclusivo` (execução parcial). O estádio já estava encerrado por prioridade; não se propõe nova execução.

### 26/09/2026 — recebimento do PDF de Meinardus

- Localizado `261_2001.pdf` no download interno do Tor do usuário e copiado ao acervo como `ponte_collatz_20260925/meinardus_2001.pdf`. Original preservado; nenhuma permissão alterada. PDF de 15 páginas, não criptografado; capa confere título, autor e Nr.261/2001. SHA-256 de origem e cópia coincidem (`08ebcc736ad2…`). Recebimento e manifesto registrados; tentativas anteriores preservadas.
- Obtenção concluída; leitura matemática **pendente**. Nenhum processo científico ou dado reservado consultado nesta entrega.

### 26/09/2026 — propostas baseadas no acervo e nos resultados disponíveis

- Criado `hipoteses/DIRECAO_EXPERIMENTAL_20260926.md`: EXP26-1 (inversão do vazamento), EXP26-2 (assinaturas de perda seletiva), EXP26-3 (identificação aritmética), EXP26-4 (contagem dos ramos de Collatz) e EXP26-5 (condições para um teste direto com zeros). Todos **pendentes**, sem piloto ou novidade estabelecida. Não substituem H-004.
- Consultados o estado, a declaração H-004 e as notas B14/B18–B20 de outras sessões; não realizada nova auditoria integral dessas leituras. A indicação anterior de leitura de Meinardus pendente referia-se à entrega local de recebimento, não invalida a leitura já registrada pela outra sessão.
- Nenhum dado reservado aberto, cálculo científico executado ou processo alterado. Próxima entrega proposta: identificabilidade e ficha prévia para EXP26-1, com controle de complexidade e orçamento antes de simulação. Sem commit.

### 26/09/2026 — prioridade revista e ficha prévia EXP26-2

- Incorporadas as ressalvas do usuário: H-004 inalterada; EXP26-2 principal; EXP26-1 condicionada a estudo de condicionamento e referência de ajuste conjunto direto; EXP26-4 com bibliografia/modelos/benchmark antes de execução; EXP26-3 posterior.
- Criada `hipoteses/FICHA_EXP26_2_PREVIA.md`: retirada aleatória, pares próximos, pares adjacentes aleatórios e lacuna contígua; referências simples e com informação espectral; dados T0 divididos por espectro pai; decisão e itens necessários ao congelamento. É ficha de desenvolvimento, não pré-registro completo.
- Incorporada identidade A₅(x)+A₁₆(x)=⌊x⌋−4 no mapa acelerado, para 8≤x na faixa em que a convergência de todos os iniciais é estabelecida. Barina consultado em fonte primária; convergência externa não dá automaticamente a classificação local dos ramos nem seu custo.
- Nenhuma simulação/enumeração, acesso a resultados reservados ou intervenção nos processos. Estado dos testes: **não executado**. Sem commit.

### 26/09/2026 — correções da conta de viabilidade de EXP26-2

- Criada `hipoteses/EXP26_2_REVISAO_VIABILIDADE.md`: ΔK_c inclui interferência; experimento bayesiano de uma lacuna não é teto do B0 completo; MA=MJ em k=2 sob igual seleção; M0 mede falso diagnóstico seletivo. V1 conferida no código: contagem suave com tolerância 3 e S não estimado, não Turing certificado.
- Ficha atualizada para conta sintética prévia, teto proposto 600 s-CPU, com regra de decisão ainda a declarar. Nenhum cálculo iniciado. GUE e K_c não encerram automaticamente hipóteses sobre resíduos aritméticos complexos. Ranking de intervalos por recuperação/custo registrado como possível objetivo, sem alegação de otimalidade.
- Apenas leitura de código-fonte e revisão documental; nenhum processo ativo ou dado reservado acessado. Sem commit.
- **Atualização 26/09 10:40 — V2′ de χ₋₄:** a varredura com passo d̄/16 terminou às 10:14 com **3.000 zeros** no bloco alto, a mesma contagem da lista corrigida pelo D3. O processo segue no passe de completude sobre a lista recomputada (Etapa A: 210 intervalos acima de 1,6 d̄, passo d̄/32). Pelo ritmo do D3 de χ₋₄ na mesma faixa (~36 s/intervalo), a estimativa é de ~2 h, com término por volta de 12:30 e cerca de 21,5 h-CPU no total. Esse passe **não grava checkpoint** (`v2_prime` chama `stage_a` sem `state`): se for interrompido, a varredura é preservada, mas a Etapa A recomeça. A comparação V2 (contagem e posições) só sai no fim.

### 26/09/2026 12:32 — V2′ de χ₋₄ concluída: χ₋₄ `validado`

- `completude_d3.py --carater chi_m4 --v2` (PID 201421) terminou 26/09 12:32:06 (início 25/09 14:45). Parede ≈ 21 h 47 min; CPU ≈ 21,3 h; a varredura V2′ sozinha levou 70.146 s e 96.469 avaliações.
- **Resultado V2′ (bloco 9001–12000):** recomputação com passo d̄/16 → 3.000 zeros; lista corrigida → 3.000; **mesma contagem**, diferença máxima de posição **5,8·10⁻¹⁰**. O passe de completude na lista recomputada (210 intervalos, passo d̄/32) recuperou **0** zeros. O certificado ficou nivelado (15 janelas, spread 0,040, sem degraus nem janelas fora do nível).
- **Manifesto** `manifesto_d3_chi_m4.json` (SHA-256 `edef331b…`): V1, V2, V3, V4 e certificado final `passed=True`; `passou=True`. Lista de trabalho `zeros_chi_m4_12000_completo.txt` (`81fdfc0a…`) inalterada desde 23/09.
- **Estado:** χ₋₄ passa a `validado` (D3 + V2′). χ₅: `validado` após D3, com a V2′ pendente.
- **Próximo na fila** (confirmado em 26/09 pelo código congelado, ver entrada seguinte): V2′ de χ₅. Pelo custo desta execução, deve ficar acima de 20 h-CPU, possivelmente o dobro, já que o passe D3 de χ₅ foi ~2,2× mais lento que o de χ₋₄. Pela regra de 25/09, deve ter teto (`RLIMIT_CPU`) declarado antes de iniciar. Sugestão: gravar checkpoint também na Etapa A da V2′, que hoje não grava.

### 26/09/2026 — complemento de identidade de χ₅ (ADENDO_H004_2 §6)

- Gravado `results/registro_hipoteses/H-004/ADENDO_H004_2_COMPLEMENTO.md` (SHA-256 `f61ecb49…`, em `.sha256`); o adendo 2 foi reconferido intacto (`a5d071be…`). **§6 satisfeito.**
- Identidade de χ₅ conferida elemento a elemento: 11.994 originais + 6 recuperados (três pares próximos), diferença ≤ 4,5·10⁻¹⁰. Indexação muda a partir de 6.336. f02 fica idêntico; f03 recebe 2 recuperados; f04 recebe 4, e o topo recua de 9.510,050 para 9.506,172. O acesso para identidade foi declarado.
- **Correção de rumo:** na resposta ao usuário desta manhã afirmei que a V2′ de χ₅ não era pré-condição da H-004. **Estava errado.** `preditor_pr1_v3.py` exige V1–V4 no manifesto D3 dos **dois** caracteres (`CHECKS_REQUIRED`), e o de χ₅ não tem V2. Sem a V2′ de χ₅, a H-004 fica não executada por bloqueio. Nada foi relaxado.
- **Caminho da H-004:** declaração de custo com teto para a V2′ de χ₅ (≈ 40–50 h-CPU estimadas; sugestão: checkpoint também na Etapa A da V2′, verificado por teste antes) → V2′ de χ₅ → controle nos 8 blocos (1,55–1,8 h-CPU) → preditor v3.

### 26/09/2026 — mudança de norte: H-004 adiada; VN-1 (variância numérica e órbitas curtas) executada

- **H-004 adiada por prioridade** (decisão do usuário): `results/registro_hipoteses/H-004/ADENDO_H004_3.md` (`85e5ebee…`). O ganho esperado é baixo (projeção linear de um teorema; desenvolvimento com 0,99998) diante de 40–50 h-CPU para a V2′ de χ₅. A reserva e02–e04/f02–f04 fica mantida. **V2′ de χ₅ não será executada** por ora.
- **Novo norte:** voltar à pergunta original de espectroscopia inversa. Onde os dados se afastam do GUE, verificar se as órbitas periódicas curtas (primos) explicam o desvio.
- **VN-1:** ficha `hipoteses/FICHA_VARIANCIA_NUMERICA.md` (`bbbcb7b9…`) congelada às 13:38:51, com previsões calculadas só com primos (`previsao.json`, 242 s CPU) e o script de medição congelado antes de rodar. Código novo: `src/riemann_spectra/number_variance.py`, 8 testes passando. Fonte: Lugar–Milinovich–Quesada-Herrera, arXiv:2211.14918 (transcrição da eq. 19 de Berry 1988; original IOP não obtido).
- **Resultado** (`results/variancia_numerica_20260926/RESULTADO.md`; medição em 3,5 s):
  - Q1 (ζ): **sucesso** em 9/9 blocos. Σ² fica muito abaixo do GUE e segue Berry a ~0,001–0,005, inclusive nas ressurgências previstas (b05, L = 20: 0,458 previsto, 0,457 medido).
  - Q3 (χ₋₄, sem órbita log 2): **conjunto correto preferido**, Δχ² = 164.
  - χ₅: inconclusivo (Δχ² = 6,9 < 9), na direção prevista.
  - Rótulos B. Q3 depende de uma extensão a χ não conferida em fonte; novidade não estabelecida.
- **Próximo:** conferir a extensão a L(s, χ) na literatura (Bogomolny–Keating; famílias de L); ficha da estimativa inversa, isto é, recuperar os períodos das órbitas curtas a partir de Σ²(L) sem catálogo; gráficos pendentes.

### 26/09/2026 — conta sintética EXP26-2 concluída

- Execução técnica `validado`; avanço ao piloto `inconclusivo` em k=2/12. Resultado negativo registrado em k=6/30: pela regra declarada, parar esta versão de B1 no ensemble examinado. Nenhum caso autorizou avançar.
- 120 espectros pais GUE de 3.000 níveis; 40/40/40 desenvolvimento/calibração/avaliação; máscaras agrupadas por pai na incerteza. Custo da execução concluída 113,25 s-CPU. Primeira tentativa falhou por importação ausente antes de gerar espectros, preservada; correção técnica declarada e reserva de 10 s dentro do teto original 600 s.
- Código novo loss_viability.py; declaração, lock e artefatos em results/exp26_2_viabilidade_20260926/. Oito ajustes convergentes; atualização linear conferida contra recomputação, erro máximo 5,11e-15; hashes conferidos.
- Relatório RELATORIO.md: ganhos não são comparações a FPR efetiva idêntica; nenhum teto bayesiano estimado. Ranking por custo segue proposta, sem piloto nem economia demonstrada. Nenhum dado real/reservado lido ou processo externo alterado; sem commit. Preservadas decisões mais recentes sobre H-004 e VN-1.
- **26/09 (tarde), sequência da VN-1:**
  - **Extensão a χ conferida em fonte:** Bogomolny–Keating 2013 (B22), eqs. (26), (30)–(33), (55). Adendo `results/variancia_numerica_20260926/RESULTADO_ADENDO_1.md`. Q3 segue **B**; **novidade excluída**, porque o efeito dos primos que dividem q já está no artigo. B21/B22 na bibliografia; PDF de BK arquivado (`bed4651d…`).
  - **Estimativa inversa por Σ²: não executada, por redundância verificada.** Σ²(L) é uma integral do fator de forma K(τ), que o projeto já mede (`form_factor.py`, K_c no C3), e os períodos log p já foram recuperados sem catálogo (C1). Inverter Σ² seria um caminho mais ruidoso até o mesmo resultado.
  - **Candidata para o próximo passo:** o pico de K_c em τ = 1 (C3), hoje com explicação apenas heurística (D) e com crítica registrada em `docs/ANALISE_RESULTADOS.md`. A altura do pico depende da distribuição de x_n − (n − ½), ou seja, de S nos zeros, cuja variância de longo alcance é justamente o que a VN-1 validou (saturação de Σ²). Falta derivação e ficha própria.

### 27/09/2026 — PT-1: pico de K_c em τ = 1

- Ficha `hipoteses/FICHA_PICO_TAU1.md` (`3e2b44e6…`) congelada antes da medição. Módulo `src/riemann_spectra/bragg_peak.py` com 4 testes; previsões só com primos (132 s). Controle GUE: valida a parte incoerente (viés de ~7%), mas não a correção de 1/6. Adendo técnico 1: correção de serialização JSON antes de ver qualquer valor.
- **Resultado** (`results/pico_tau1_20260926/RESULTADO.md`): primário **inconclusivo** (25/30 na faixa B, com 27 exigidos; 28/30 acima das alternativas GUE e uniforme); agregado **incompatível** (média medida 3,01 contra 6,94 prevista). O pico é real e não é GUE, mas o modelo superestima sua altura por um fator de ~2,3. Valores idênticos aos armazenados do C3.
- **Diagnóstico exploratório:** a variância dos k-desvios bate com Σ²_Berry − 1/6 a ~0,005, confirmando a correção de amostragem nos zeros. A coerência de fase medida é 0,39 da gaussiana (0,0126 ± 0,0005 contra 0,033). **A falha está na gaussianidade**, não na estrutura de segunda ordem.
- Pergunta aberta (D): a função característica de D_k em 2π. Novidade da identidade de 1/12 aplicada ao pico não pesquisada. Sem commit.

### 27/09/2026 — busca de um norte na literatura: momentos negativos discretos

- A pedido do usuário (foco em ciência), foram triadas candidatas na literatura: momentos negativos de ζ′/L′ nos zeros, lei de Gram e correções de tamanho finito. Escolhida como norte proposto: **Conjectura 7 de Pearce-Crump (arXiv:2606.25094, jun/2026)**, Σ 1/|L′(ρ,χ)|² ∼ (A_q/2π)T. Nota `hipoteses/leituras/B23_PEARCE_CRUMP_2026.md`; B23/B24 na bibliografia; PDFs arquivados.
- A conjectura vem de heurística; o artigo não traz teste numérico. Inclinações previstas: ζ 3/π³; χ₋₄ 2/π³; χ₅ 5/(2π³).
- **Custo medido:** |Z′(γ)| para ζ via mpmath: média de 288 ms/zero (mediana 120, máximo 876), ou ~8 h-CPU para 100 mil zeros. L(s,χ) nos zeros 1–3.000: 0,08–0,6 s/zero (χ₋₄) e 0,16–1,1 s/zero (χ₅), ~1 h-CPU no total.
- Nenhuma ficha congelada; nenhum cálculo de L′ feito além do benchmark. Próximo: ficha com previsão, alternativas e análise de ruído (cauda pesada).

### 27/09/2026 — MN-1: teste numérico da Conjectura 7 de Pearce-Crump

- Ficha `hipoteses/FICHA_MOMENTOS_NEGATIVOS.md` (`d31515d1…`) e código de análise congelados antes de qualquer derivada. Uma correção na regra de fragilidade foi feita antes de rodar e registrada na ficha. Módulo `src/riemann_spectra/discrete_moments.py`, 4 testes.
- Derivadas |L′(ρ)| em ζ (zeros 1–20.000) e em χ₋₄ e χ₅ (zeros 1–3.000, fora da reserva da H-004): 2,5 h-CPU, dentro dos tetos.
- **Resultado** (`results/momentos_negativos_20260927/RESULTADO.md`):
  - χ₋₄: R = 0,655 [0,592; 0,715], previsto 2/3 → **Conjectura 7 favorecida**;
  - χ₅: R = 0,827 [0,753; 0,901], previsto 5/6 → **favorecida**;
  - as alternativas sem fator e com só os fatores de Euler ficam excluídas; decisões não frágeis;
  - ζ converge para a constante de Gonek (0,912 → 0,963 → 0,992 da constante, com a altura).
- **Rótulo C** (novidade a investigar): nenhum teste numérico anterior foi achado numa busca breve. Próximos passos: busca bibliográfica adequada; extensão a mais caracteres e à Conjectura 8.

### 27/09/2026 — MN-2 (Conjectura 8) e busca ampliada

- Busca ampliada: Hiary–Odlyzko 2011 (B25) já confirmaram a conjectura de Gonek para ζ (a calibração da MN-1 é B). A tese do autor (B26) e o artigo não calculam L′(ρ,χ): o teste para χ continua C.
- **MN-2:** ficha `hipoteses/FICHA_MOMENTOS_NEGATIVOS_C8.md` (`d96f1f0d…`) congelada antes do cálculo.
  - χ₋₄: R₈ = 0,490 [0,430; 0,549], previsto 1/2 → **favorecida**, excluindo H0 (1) e o fator da Conj. 7 (2/3);
  - χ₅: 0,753 [0,673; 0,835], previsto 4/5 → **favorecida**, sem separação de 5/6, como previsto na ficha;
  - resultado em `results/momentos_negativos_20260927/RESULTADO_C8.md`.
- Em χ₋₄, cada momento exige o seu fator aritmético (2/3 e 1/2).
- Próximo: consulta bibliográfica formal e ao autor; mais caracteres (condutor composto, complexos), o que exige calcular zeros novos com declaração de custo.

### 27/09/2026 — busca formal de novidade (MN-1/MN-2)

- `results/momentos_negativos_20260927/BUSCA_NOVIDADE.md`: zbMATH Open (3 consultas), arXiv (2), citações do artigo (0 indexadas) e de Gonek 1989 (78, OpenAlex). **Nenhum teste numérico anterior** das Conjecturas 7 e 8; o único trabalho numérico, Hiary–Odlyzko 2011, trata só de ζ. MathSciNet inacessível (assinatura); Semantic Scholar limitado por taxa.
- Rótulo C mantido, agora com busca documentada. Próximo: consulta ao autor (decisão do usuário).

### 27–28/09/2026 — MN-3 (χ₈, χ₁₂): interrompida nos tetos de CPU

- Ficha `hipoteses/FICHA_MOMENTOS_NEGATIVOS_MN3.md` (`57720029…`) congelada às 23:07; pipeline das 23:08 às 07:16.
- **As três frentes pararam no teto declarado (RLIMIT_CPU), sem extensão automática:**
  - zeros de χ₈ e χ₁₂: varredura de 2.000 zeros concluída e **V1 aprovada**; parou na **V2** (reexame com passo pela metade) em 1.689/2.000 (χ₈) e 1.760/2.000 (χ₁₂), com ~8 h-CPU cada;
  - extensão de ζ: 23.200/27.000 derivadas (teto de 1 h).
- Nenhuma derivada de χ₈/χ₁₂ foi calculada; nenhum resultado do teste existe.
- **Erro de estimativa:** previsto ~12 h-CPU, gasto ~17 h até aqui. A V2 sobre toda a faixa custa quase tanto quanto a varredura, o que não pesei direito. Falta estimada para concluir como declarado: ~4 h-CPU (V2 restante, V3, V4, derivadas, ζ). Tudo retomável pelos checkpoints.
- Aguarda decisão do usuário.

### 28/09/2026 — MN-3: retomada (ADENDO_MN3_1) concluída às 10:06

- **χ₁₂:** V1–V4 **aprovadas**; derivadas e L(2ρ) calculadas (`derivadas_chi_12_2000.txt`, `L2rho_chi_12_2000.txt`).
- **χ₈:** **V2 reprovada.** O reexame com passo pela metade achou 2.002 zeros contra 2.000 da lista principal (`manifest_chi_8_2000.json`, `ed68096d…`). V1, V3 e V4 aprovadas; a V1 passou com diferença −1,76, dentro da tolerância de 3, compatível com um par perdido. **Derivadas não calculadas**, como declarado na ficha §2. É a mesma falha de pares próximos de χ₋₄/χ₅. A correção pelo passe D3 exige decisão nova.
- **ζ:** parou de novo no teto, em 26.300/27.000 derivadas; L(2ρ) de ζ não rodou.
- Nenhuma análise executada; nenhum resultado do teste visto. Aguarda decisão do usuário.

### 28/09/2026 — MN-3: adendo 2 e desligamento abrupto da máquina

- Usuário autorizou o `ADENDO_MN3_2` (correção de χ₈ pelo passe D3; conclusão de ζ). Hashes registrados.
- Derivadas de ζ 1–27.000 **concluídas** (571 s na sessão).
- **Desligamento abrupto às 10:39:** o journal termina sem mensagem de shutdown. A causa não pôde ser confirmada (falta de energia ou proteção térmica). A máquina tem 2 núcleos físicos e rodou 3 processos pesados em paralelo por mais de 12 h.
  - Perdido: o cálculo de L(2ρ) de ζ, que não tem checkpoint e será refeito.
  - Preservado: o checkpoint da correção de χ₈ (88/133 intervalos da Etapa A, 0 zeros recuperados até ali; JSON íntegro).
- Retomada às 10:44 **em série** (χ₈ D3 → derivadas de χ₈ → L(2ρ) de ζ), com um processo por vez para reduzir a carga térmica. Tetos do adendo 2 mantidos por sessão.
- **12:23 — série concluída.** Correção de χ₈: 2 zeros recuperados (par 1.470,227/1.470,279), lista com 2.002 = contagem da V2, verificações aprovadas. L(2ρ) de ζ refeito.

### 28/09/2026 — MN-3: resultado

- `analise_mn3.py` rodou com todos os hashes conferidos. **χ₁₂:** Conj. 7 R = 0,501 [0,445; 0,555] (previsto 1/2); Conj. 8 R = 0,340 [0,301; 0,381] (previsto 1/3), com H7 excluída. **χ₈:** Conj. 7 0,687 [0,605; 0,784] (2/3); Conj. 8 0,558 [0,450; 0,684] (1/2). **Todas favorecidas.**
- Somando MN-1 a MN-3: 4 caracteres, 8 testes, 8 favoráveis. Resultado em `results/momentos_negativos_20260927/RESULTADO_MN3.md`.

### 28/09/2026 — nota enviada ao autor

- Rascunho v0 da nota (`nota_momentos_negativos/nota.pdf`, 4 pp., commit `7793f74`) enviado pelo usuário por e-mail a A. Pearce-Crump (andrew.pearce-crump@bristol.ac.uk). Pedidos: saber de outro trabalho numérico e de problemas no método. Uso de IA declarado. Sem pedido de endosso nem de colaboração.
- Enquanto se aguarda a resposta: não publicar o preprint; preparar o depósito no Zenodo (dados, código, fichas); ler Conrey–Snaith 2007 para avaliar a derivação pela conjectura das razões.

### 28/09/2026 — avaliação da derivação pela conjectura das razões

- Lido Conrey–Snaith 2007 (B27), §7: momentos discretos positivos de ζ′(ρ) com todos os termos de ordem inferior via razões; não trata momentos negativos. Bui–Gonek–Milinovich 2015 recuperam HKO (inclusive k = −1) pelo produto híbrido.
- Conta heurística (D): na receita CFKRS, os fatores ζ-like em p | q permanecem, e isso dá exatamente A_q = (6/π²)∏ p/(p+1). HE corresponde a um tratamento incorreto, o que explica sua exclusão pelos dados. Registrada a correção de uma afirmação anterior minha ao usuário.
- Avaliação em `hipoteses/AVALIACAO_DERIVACAO_RAZOES.md`:
  - etapa A (termo principal para χ): viável;
  - etapa B (termos de ordem inferior, q = 1): difícil, com polos extras no contorno do momento negativo, mas testável nos 27.000 zeros de ζ;
  - etapa C (χ): depois da B.

### 28/09/2026 — Etapa A: fatores aritméticos pelo modelo HKO

- `hipoteses/DERIVACAO_ETAPA_A.md` (D, heurístico). O modelo de Hughes–Keating–O'Connell estendido a L(s,χ), mantendo (1 − 1/p)^{k²} em todos os primos e com média local 1 em p | q, reproduz **exatamente** A_q (Conj. 7) e φ(q)/q (Conj. 8). Conferido numericamente para q = 1, 4, 5, 8, 12 (`results/derivacao_etapa_a_20260928/verifica_fatores_locais.py`).
- Âncora k = 1 (média quadrática: fator φ(q)/q), verificada numericamente de forma exploratória (`ancora_k1.py`, 474 s CPU). Inclinações de 0,447 [0,142; 0,746] (χ₋₄, previsto 0,5) e 0,243 [0,014; 0,467] (χ₁₂, previsto 1/3); a alternativa 1 fica excluída.
- As alternativas excluídas pelos dados (HE, fator trocado) ganham interpretação no modelo. Sem reivindicação de novidade.
- Nota v1: nova §5 com a verificação heurística; PDF com 5 pp. A v0 enviada ao autor fica preservada em `7793f74`.

### 28/09/2026 — pacote do depósito Zenodo (não publicado)

- `deposito_zenodo_mn/` (montagem, README em inglês, `.zenodo.json`, licença MIT para código e CC BY 4.0 para dados) gera `dist/mn_negative_moments_v1/` (54 arquivos, `SHA256SUMS`) e o `.zip` (1,05 MB, `6ac89c00…`). `dist/` fica fora do git.
- **Reprodução conferida:** `reproduce_table.py`, rodando do pacote com a `zeros1` de Odlyzko (não redistribuída; hash conferido), reproduz **exatamente** os 16 números da Tabela 1.
- Só os zeros usados na nota (os blocos reservados da H-004 ficam de fora). Nenhum caminho pessoal nos arquivos.
- **Publicação: decisão e ação do usuário.** Nada foi enviado.
- **DOI reservado pelo usuário: 10.5281/zenodo.23020957.** Inserido na nota ("Data and code"), no README e no `.zenodo.json`; nota recompilada; pacote remontado (`.zip` `c853ed96…`, 1,06 MB). Depósito ainda **não publicado**.
- **Zenodo (28/09):** arquivo enviado pelo usuário conferido: MD5 `38f56e7b…`, idêntico ao pacote final (`.zip` SHA-256 `bd85056d…`). Situação de publicação não confirmada: API do Zenodo bloqueou o acesso (403) e o DOI ainda não resolve (404). ORCID do usuário (0009-0009-8217-1623, dígito verificador conferido) acrescentado à nota, ao README e ao `.zenodo.json` do repositório; o `.zip` enviado **não** foi alterado.

### 28/09/2026 — Etapa B: derivação pela conjectura das razões

- Busca: nenhum trabalho encontrado com termos de ordem inferior (Durkan–Hughes–Pearce-Crump 2026, Pearce-Crump sobre Ng 2026 e Bui–Gonek–Milinovich 2015 tratam de outras coisas ou só do termo principal).
- `hipoteses/DERIVACAO_ETAPA_B_RAZOES.md` (D). O contorno de Conrey–Snaith com peso ζ′/ζ falha: os resíduos extras cancelam os resíduos em ρ. O contorno com o resíduo de 1/ζ(s) e um único deslocamento funciona. A receita dá:
  - Σ 1/|ζ′(ρ)|² = (3/π³)T + O(T^{1/2+ε});
  - Σ 1/|L′(ρ,χ)|² = (A_q/2π)T + O(T^{1/2+ε});
  - Σ |L(2ρ,χ²)/L′(ρ,χ)|² = (φ(q)/q)T/2π + O(T^{1/2+ε}).
  **Sem termos de ordem T/log T.** Conferido na fonte o passo central: CS (2.10), com o numerador levado a 1.
- **Correção de interpretação:** os desvios de altura finita não seriam termos de ordem inferior, mas flutuação de soma de cauda pesada (variância infinita). Conferência exploratória em ζ 1–27.000: janelas de 3.000 com razão entre 0,907 e 1,088, sem tendência; (J − CT)/√T estável.
- Pendente: revisar a nota (§2.2, §6, nova seção); teste em zeros novos com referência CUE (proposta).
