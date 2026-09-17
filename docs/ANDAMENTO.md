# Registro de andamento da investigação

Estado das etapas do [plano de implementação](../PLANO_IMPLEMENTACAO.md). Última atualização: 14/09/2026.
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
| 11 | Fórmulas de traço e classes de operadores | M4 | `em execução` | 14/09/2026 | Plano e matriz **preliminar** revisados em 11.3: [ETAPA11_PLANO.md](ETAPA11_PLANO.md), [ETAPA11_MATRIZ_OPERADORES.md](ETAPA11_MATRIZ_OPERADORES.md), `etapa11_matriz_operadores.csv`, `etapa11_evidencias.csv` | Seis pontos da auditoria e ajustes 11.3b-1 tratados (N1 de K5a/K7/K9 → PC; campos `situacao`/`conferencia`; fontes arquivadas com SHA-256 em `archive/fontes_etapa11/`); códigos não usáveis para seleção/exclusão enquanto houver PC (matriz §0.3, 11.3b); 11.4 concluída como entrega documental preliminar ([ETAPA11_CORRESPONDENCIAS.md](ETAPA11_CORRESPONDENCIAS.md), `etapa11_correspondencias.csv`, 20 relações; ajustes 11.4-1), sem liberar seleção ou congelamento de testes; 11.3b **encerrada em 17/09/2026** com itens abertos registrados ([ETAPA11_3B_ENCERRAMENTO.md](ETAPA11_3B_ENCERRAMENTO.md); estado ao encerrar: [ETAPA11_3B_FORMULA_EXPLICITA.md](ETAPA11_3B_FORMULA_EXPLICITA.md): L-EF1 parcial (termo arquimediano derivado em H2: [ETAPA11_3B_TERMO_ARQUIMEDIANO.md](ETAPA11_3B_TERMO_ARQUIMEDIANO.md); aplicabilidade a 𝒢 depende de F5; classe suficiente 𝒜 em [ETAPA11_3B_ADMISSIBILIDADE.md](ETAPA11_3B_ADMISSIBILIDADE.md) com Z1 derivado em [ETAPA11_3B_Z1_CONTAGEM.md](ETAPA11_3B_Z1_CONTAGEM.md), certificado intervalar com cauda analítica; L-EF1: fechamento documental pendente de F5 e J1; H1 formulada em [ETAPA11_3B_H1_FORMULACAO.md](ETAPA11_3B_H1_FORMULACAO.md) e [ETAPA11_3B_H1_R5_ESTIMADOR.md](ETAPA11_3B_H1_R5_ESTIMADOR.md): S1 quantificado, S3b derivada condicionalmente com taxa O(ε²) e constantes independentes de t e ε, R5 formalizado com S2-ratio (implementado) × S2-complexo (extensão) e cálculo finito B sob declaração prévia em `results/etapa11_r5/`; cruzamento exploratório com C2: contaminação > τ só em linhas não elegíveis; diagnósticos de R5 encerrados; Lema de Cauda Projetada proposto e Q_k(u) derivado ([ETAPA11_3B_H1_CAUDA_PROJETADA.md](ETAPA11_3B_H1_CAUDA_PROJETADA.md): frequências nas bordas A, B; Rota B incondicional insuficiente; cota-alvo uniforme em ε e η formulada; B_main derivada por deslocamento de contorno; representação R-EF-χ fixada, sem truncamento em altura; proposição P-RH: cota uniforme em ε condicional a RH; força avaliada sob declaração (híbrida): com Lema 5′, majorante < 1e-6 em 361/461 pares elegíveis; zeros dominam; passagem ao truncamento abrupto derivada (P-RH-trunc); termo de transição Θ_k(U₂) calculado sob declaração (B): margens todas positivas, orçamento inalterado; para reduzir a majorante, zeros são o gargalo; decomposição da parcela dos zeros: L₂ e janelas adjacentes dominam; Lema 4′ derivado e avaliado sob declaração (híbrido, sob RH): condição suficiente ≤ 1e-6 em 461/461 elegíveis com d₁ = 8; **certificada computacionalmente em (8, 2), condicional a RH, para M^math** (execução 1 inválida por enclausuramento; execução 2 substituída por lacunas de justificativa; execução 3 substituída; execução 4 vigente e congelada, com adendos 1–3, c₁ e c₂ recalculados internamente e testes T1–T9): 461/461 elegíveis, 1.178/1.410 pares; **resíduo contra o catálogo 𝒦 certificado (§II.21, `DECLARACAO_CERT_CONTAMINACAO.md`): |a_k·(F* − M_𝒦)| ≤ 10⁻⁶|c_k| sob RH, para M^math, em 461/461 elegíveis (máx 6,6091·10⁻⁷) e 1.093/1.410 pares, sem corte em U₂; testes T1–T15; termo determinístico ρ_Δ certificado (§II.22, `DECLARACAO_CERT_DENSIDADE.md`): |a_k·(F^rvm − M_𝒦)| ≤ 10⁻⁶|c_k| sob RH, para M^math, em 461/461 elegíveis (máx 6,6213·10⁻⁷) e 1.089/1.410 pares, com a cota de densidade recalculada sob a base atual (dependência herdada eliminada); testes T1–T21; erro das ordenadas ρ_ord certificado (§II.23, `DECLARACAO_CERT_ORDENADAS.md`): |a_k·(F^tab − M_𝒦)| ≤ 10⁻⁶|c_k| sob RH e H-tab (não certificada), para M^math, em 461/461 elegíveis (máx 7,313·10⁻⁷) e 1.024/1.410 pares; testes em duas rodadas (rodada 1 preservada); camada numérica ρ_num (§II.24, `DECLARACAO_CERT_NUMERICO.md`): fidelidade (N) incondicional |r̂_k − X_k/c_k| ≤ 6,3·10⁻¹¹ nos elegíveis e ligação (T) |r̂_k − 1| ≤ 10⁻⁶ sob RH e H-tab em 461/461 elegíveis (1.024/1.410 pares), sem alarmes; C2 inteiro, S1, S3a, S3c e auditoria independente pendentes; protocolo de auditoria em [PROTOCOLO_AUDITORIA_CERTIFICADO.md](PROTOCOLO_AUDITORIA_CERTIFICADO.md)**; auditoria integral independente pendente; Lema C formulado; passagem ao estimador registrado pendente); H1 aberta), L-EF2a/b revisadas em 11.3b-2/3 (completude da tabela B nos 30 blocos, fator 2, restos com prefatores, cota certificada do termo determinístico), L-EF2c aberta; fontes F1–F7 `bloqueado` por acesso de rede ([ETAPA11_PENDENCIAS_FONTES.md](ETAPA11_PENDENCIAS_FONTES.md)), C02 derivada, C11/C19 PC por fontes inacessíveis; checagens em `results/etapa11_3b/`); 11.5–11.6 pendentes; nenhum candidato implementado; `candidates.py` segue como rascunho não avaliado |
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

1. Etapa 11 (classes de operadores), com fontes primárias.
2. Verificações abertas:
   - implementação por outra pessoa ou linguagem;
   - densidade θ na cadeia completa;
   - inversão harmônica;
   - corrigir S4 numa versão futura do plano: centrar em (B+1−u)/(B+1), incluir a variabilidade do limiar estimado e calibrar a regra conjunta sem pressupor independência entre blocos sem justificativa.
3. Confirmações adicionais exigiriam dados novos (tabelas de maior altura); os 100.000 zeros já foram consumidos.
