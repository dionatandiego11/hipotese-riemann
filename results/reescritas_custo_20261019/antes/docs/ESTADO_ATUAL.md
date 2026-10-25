# Estado atual do projeto — ponto de retomada (19/10/2026)

Documento de entrada para quem retoma o trabalho (pessoa ou agente). Resume onde o projeto está, o que está congelado,
quais regras seguir e qual é a próxima tarefa. Os detalhes ficam nos documentos citados; em conflito, eles prevalecem.
Versão anterior (19/09/2026) no histórico do git.

## Alvo de cobertura formulado — 19/10/2026

A cota agregada será complementada por um alvo local, ainda não demonstrado: cada classe atingida módulo3^r deve enviar uma fração positiva de suas palavras para cada um dos três filhos módulo3^{r+1}, sob o mesmo custo e limites. A base das duas unidades módulo3 foi explicitada. Nota `teorias/SYRACUSE_COBERTURA_CRITERIO_20261019.md`. Variações apenas do prefixo com sufixo fixo não bastam: alcançam no máximo dois filhos. Próximo passo analítico: procurar reescritas de sufixos de mesmo custo, com controle das fibras. Sem cálculo novo; Riemann mantém os alvos já registrados.

## Concentração condicionada — 19/10/2026

Auditada a prova da majorante de Valbuena e a interpolação Lp (com mistura de Tao como entrada externa). A contagem por fibras permite uma consequência para o evento do projeto: para qualquer subconjunto E de palavras com custo total fixado e probabilidade beta>0, Energia(E)<=4/beta². A massa central beta>=b_C/sqrt(ell), já derivada anteriormente, dá energia O_C(ell), inclusive com os limites individuais. Não fornece minorante por resíduo nem conclusão sobre órbitas positivas. Novidade não estabelecida; sem revisão independente.

Nota: `teorias/SYRACUSE_ENERGIA_CONDICIONADA_20261019.md`. Dois testes exatos passaram:35 momentos e69 eventos não vazios, 0,417s CPU, sem dados reais/reservados. Próximo alvo de Collatz: explicitar a estimativa adicional necessária para cobertura, partindo desta cota agregada e da mistura condicionada já existente. Riemann mantém a prioridade da intensidade ponderada de pares; os termos inferiores e R3 seguem abertos. O registro de18/10 abaixo é histórico quanto à majorante e à extensão ao custo então pendentes.

## Execução das prioridades — 18/10/2026

T001: a contribuição de pares próximos no controle CUE(2) foi isolada por regiões e recupera o defeito conhecido de −1/2. Um lema condicional explicita a intensidade conjunta de gap/amplitude necessária para transferir o mecanismo; essa hipótese não foi provada para L. Nota: `teorias/EVENTOS_RAROS_CUE_20261018.md`.

T008: derivada a recorrência exata E_K−E_(K−1)=2·3^(K−1)H_K. Sob a densidade L¹/positividade já usadas, a sobreposição dos ramos dá f∉L² e crescimento pelo menos linear de E_K, sem constantes avaliadas. Antecedente direto da obstrução L² encontrado em fonte de Valbuena; demais resultados anunciados não auditados. Nota: `teorias/SYRACUSE_COLISOES_20261018.md`. Cinco testes novos passaram, 4,702s CPU, sem zeros reais ou reservados. R3 e termos inferiores de L seguem abertos. Próximos alvos: intensidade ponderada independente para pares; conferir a majorante bibliográfica antes de adaptar energia ao custo condicionado.

## Atualização prioritária — 14/10/2026

A frente principal é a derivação por razões dos momentos negativos (Conjecturas7/8 dePearce-Crump), seguida de termos inferiores. A antiga conclusão analítica daEtapaB foi retirada por falta de uniformidade nos deslocamentos; tabelas numéricas preservadas. Plano: `hipoteses/PLANO_RAZOES_MOMENTOS_NEGATIVOS.md`; errata: `hipoteses/ERRATA_ETAPA_B_20261013.md`.

**R3 em execução:** geradores aritméticos fechados e duas constantes principais recuperadas formalmente. A tentativa de estimar o erro identificou que seu perfil polar contém o próprio desvio do momento. Não foi obtida cota sublinear. Há uma representação exata fora da diagonal na região de convergência absoluta; o alvo atual é justificá-la por truncamento/continuação com erro controlado na faixa crítica. Nota: `hipoteses/RAZOES_ERRO_PERFIL_POLAR_20261014.md`. Termos inferiores emT continuam abertos.

O controleCUE mostra que a primeira correção pode não comutar com a média: `hipoteses/RAZOES_DISCRETAS_MOMENTOS_NEGATIVOS_20261013.md`.Última verificação:8 testes pertinentes passaram, sem consultar zeros reais ou dadosMN/H-004 reservados. Os26 testes da entrega anterior não foram repetidos nesta. Collatz permanece complementar. Histórico abaixo deve ser lido com esta atualização.

**Exploração complementar — 15/10:** `teorias/DIRECOES_20261015.md` organiza cinco apostas, com dez fichas no registro. Novas frentes: concentração/colisões de Syracuse, Hilbert/memória/primeira passagem e comparação modular. Busca dirigida com quatro fontes primárias arquivadas; novidade não estabelecida. Derivações elementares delimitam perda de transientes pelo determinante e a ausência de uma conjugação projetiva simples com Gauss; controle CUE(2) explicita média finita/variância infinita. Não transferem resultados a RH/Collatz. Sem simulação ou dados de zeros nesta entrega; R3 permanece como acima.

## 1. O que é o projeto

Espectroscopia inversa dos zeros da função zeta: medir, com protocolos pré-registrados e controles, que informação
aritmética e dinâmica é recuperável de listas finitas de zeros, e avaliar classes de operadores candidatos (programa de
Hilbert–Pólya). **O projeto não tenta provar RH e não afirma nada a favor dela.**

## 2. Regras de trabalho (obrigatórias)

- **Declaração prévia antes de cálculo que decide algo**, com SHA-256 em `.sha256` ao lado. Protocolos não mudam
  depois de ver dados; mudanças só por adendo com causa.
- **Custo de CPU** (`results/registro_hipoteses/ADENDO_REGISTRO_v2_2.md`, `0b505348…`, e erratas): execução **longa**
  (> 4 h-CPU acumuladas) só com previsão discriminante, viabilidade demonstrada e teto declarado (`RLIMIT_CPU`, não
  `timeout`). Antes de gastar CPU, perguntar: **o resultado pode surpreender?** Se a teoria já determina a resposta,
  não é experimento.
- **Resultados negativos e falhas são registrados**, nunca apagados.
- **Rótulos:** A (matemática conhecida, com hipóteses), B (reprodução numérica), C (achado com novidade a investigar),
  D (conjectura). Separar sempre o condicional (RH, H-tab, conjecturas) do incondicional.
- **Sem afirmação de novidade** sem busca bibliográfica adequada.
- **Fontes:** só vale o que foi lido na fonte, com página. Cada fonte vai para `archive/fontes_etapa11/` e é registrada
  em `archive/fontes_etapa11/MANIFESTO.csv` (URL, versão, data, páginas, SHA-256). PDFs/HTML/TeX de terceiros **não**
  entram no git. Notas de leitura em `hipoteses/leituras/`.
- **Código e artefatos congelados** (m3/m4, certificado, fichas com `.sha256`) não são editados; código novo vai em
  módulo novo.
- **Um agente por vez no repositório.** Sessões paralelas já editaram os mesmos documentos; evitar.
- **Formato:** `* -text` (`.gitattributes`); vários CSVs usam **CRLF** (por exemplo `archive/fontes_etapa11/MANIFESTO.csv`).
  Preservar os bytes de fim de linha.
- **Documentação em português.** Commits em branch, nunca direto na `main`; o usuário integra e faz o push.
- Instruções adicionais de agente: `AGENTS.md` local (fora do repositório público).

## 3. Onde cada coisa está

| Assunto | Documento |
|---|---|
| Plano geral (etapas 0–13, marcos M1–M5) | [../PLANO_IMPLEMENTACAO.md](../PLANO_IMPLEMENTACAO.md) |
| Log detalhado | [ANDAMENTO.md](ANDAMENTO.md) |
| Protocolos m3/m4 e resultados M1–M4 | [PROTOCOLO.md](PROTOCOLO.md), [RELATORIO_CONSOLIDADO.md](RELATORIO_CONSOLIDADO.md) |
| Etapa 11 (matriz de operadores, certificado, controles) | [ETAPA11_PLANO.md](ETAPA11_PLANO.md), [ETAPA11_MATRIZ_OPERADORES.md](ETAPA11_MATRIZ_OPERADORES.md), `results/etapa11_r5/`, `results/etapa11_6_controles/` |
| Registro de hipóteses (H-*) | [REGISTRO_HIPOTESES.md](REGISTRO_HIPOTESES.md), `results/registro_hipoteses/` |
| Caderno de hipóteses, planos, bibliografia (B1–B22) | `../hipoteses/` ([README](../hipoteses/README.md), [BIBLIOGRAFIA](../hipoteses/BIBLIOGRAFIA.md)) |
| Variância numérica e órbitas curtas (VN-1) | [../hipoteses/FICHA_VARIANCIA_NUMERICA.md](../hipoteses/FICHA_VARIANCIA_NUMERICA.md), `results/variancia_numerica_20260926/` |
| Collatz | [PLANO_COLLATZ.md](PLANO_COLLATZ.md), `results/collatz_cl0/`, `../hipoteses/PLANO_PONTE_DIRETA_COLLATZ_RIEMANN.md` |

## 4. Resultados centrais (não refazer)

| Resultado | Rótulo | Onde |
|---|---|---|
| **C1/C2:** linhas em log p recuperadas sem catálogo; coeficientes concordam (máx. entre elegíveis ≤ 2,6·10⁻⁹) nos 30 blocos (zeros 10.001–100.000) | B | RELATORIO_CONSOLIDADO |
| **C3:** CDF de espaçamentos e K_c rejeitam Poisson e o GUE finito de 3.000 níveis em todos os blocos; Var(s) abaixo do GUE. Restrição ao procedimento de comparação, **não** refutação da universalidade assintótica. K_c tem um pico em τ = 1 ainda sem explicação quantitativa (D) | B | RELATORIO_CONSOLIDADO §3.3 |
| **Certificado 11.3b:** fidelidade numérica (N) incondicional; ligação (T) \|r̂ − 1\| ≤ 10⁻⁶ sob RH e H-tab, 461 linhas elegíveis. Publicado no Zenodo (doi:10.5281/zenodo.22811040). **Sem auditoria independente** | B | ETAPA11_3B_* |
| **Matriz de operadores:** K1, K5a, K5b, K7, K8, K9 incompatíveis (demonstrado/derivado no escopo registrado); K3a e K4 condicionais; K12 é controle de ajuste | A/B | ETAPA11_MATRIZ_OPERADORES |
| **Zeros de Dirichlet** (12.000 por caractere): execuções originais **reprovadas** em V1/V2 (preservadas); corrigidas pelo passe D3. χ₋₄ **validado** (D3 + V2′, 26/09); χ₅ validado no D3, **V2′ não executada** | B | `results/etapa11_6_controles/dirichlet/completude/` |
| **Controle Maass `ctrl-maass-v1`:** não passa pelos critérios declarados (nulo superestima o ruído ~10⁵); observação exploratória de coeficientes com razão 1 ± 10⁻⁶–10⁻⁴ | B/C | RELATORIO_MAASS_v1 |
| **VN-1 (26/09):** Σ²(L) dos zeros de ζ segue a fórmula semiclássica de Berry (só primos) e não o GUE, em 9/9 blocos, inclusive nas ressurgências previstas; em L(s, χ₋₄), a curva com a órbita log 2 removida vence a alternativa (Δχ² = 164); χ₅ inconclusivo. Extensão a χ confirmada em Bogomolny–Keating 2013; **sem novidade** | B | `results/variancia_numerica_20260926/RESULTADO.md` e adendo 1 |
| **EXP26-2, viabilidade (26/09):** em GUE sintético, o resumo espectral não autorizou avançar em nenhuma severidade (k = 6, 30: parar; k = 2, 12: inconclusivo) | B | `results/exp26_2_viabilidade_20260926/RELATORIO.md` |
| **Leituras Collatz–Riemann:** Meinardus 2001, Siegel (Parte I.5), Bell–Lagarias 2015 e bibliografias de Lagarias: **nenhuma ligação com os zeros de ζ**; ζ só aparece como série da sequência constante. Siegel (2.25)/(2.26) têm erro, corrigido e verificado numericamente | A/B | `hipoteses/leituras/B18`–`B20` |

| **MN-1 (27/09): Conjectura 7 de Pearce-Crump** (Σ 1/\|L′(ρ,χ)\|² ∼ (A_q/2π)T, arXiv jun/2026): teste diferencial χ/ζ favorece o fator aritmético em χ₋₄ (R = 0,655 [0,592; 0,715], previsto 2/3) e χ₅ (0,827 [0,753; 0,901], previsto 5/6), excluindo as alternativas | **C** (novidade a investigar) | `results/momentos_negativos_20260927/RESULTADO.md` |
| **MN-2 (27/09): Conjectura 8 de Pearce-Crump** (Σ \|L(2ρ,χ²)/L′(ρ,χ)\|² ∼ (φ(q)/q)T/2π): χ₋₄ R₈ = 0,490 [0,430; 0,549], previsto 1/2, excluindo 1 e 2/3; χ₅ 0,753, previsto 4/5 | **C** | `results/momentos_negativos_20260927/RESULTADO_C8.md` |
| **MN-3 (28/09): χ₈ e χ₁₂** — χ₁₂: Conj. 7 R = 0,501 [0,445; 0,555] (1/2), Conj. 8 R = 0,340 [0,301; 0,381] (1/3); χ₈: 0,687 (2/3) e 0,558 (1/2). **Total: 4 caracteres, 8 testes, 8 favoráveis** | **C** | `results/momentos_negativos_20260927/RESULTADO_MN3.md` |

**Balanço honesto:** os primeiros candidatos a resultado C são a MN-1 e a MN-2, ainda sem busca bibliográfica adequada. O resto é
infraestrutura rigorosa e reprodução numérica de teoria conhecida (B).

## 5. Estado das frentes

| Frente | Estado |
|---|---|
| Etapas 0–10 (M1–M4) | validadas |
| 11.1–11.4 | matriz madura (1 pendência: K7 M4); 11.3b encerrada com itens abertos; 11.4 documental |
| 11.5 | não iniciada |
| 11.6 controles | Dirichlet: dados validados (exceto V2′ de χ₅); Maass: não passa; estádio: **encerrado por prioridade** (diagnóstico de poder abortou em g04, parcial e `inconclusivo`) |
| **H-004** (previsão do erro do estimador em L(s, χ)) | **adiada por prioridade** (`results/registro_hipoteses/H-004/ADENDO_H004_3.md`): exigiria a V2′ de χ₅ (~40–50 h-CPU), e o desfecho é quase determinado pela fórmula explícita. Reserva e02–e04/f02–f04 mantida |
| **VN-1** | concluída (ver §4) |
| **Pico de K_c em τ = 1 (PT-1)** | executado em 27/09: primário **inconclusivo**, agregado incompatível. Pico real (não GUE); altura superestimada ~2,3× pelo modelo gaussiano; correção de 1/6 confirmada diretamente; **falha localizada na gaussianidade** (`results/pico_tau1_20260926/RESULTADO.md`) |
| EXP26-1, EXP26-3 a 5 (`hipoteses/DIRECAO_EXPERIMENTAL_20260926.md`) | propostas; não iniciadas |
| Collatz | CL0 entregue (documental); CL1 não executada; ponte direta sem mecanismo encontrado; A₅(x) (ramos 5/16) como pergunta barata, não iniciada |
| Etapas 12–13 | pendentes |

## 6. Próxima tarefa recomendada

1. **PT-1 concluída** (ver §5). Aberto (D): a função característica dos k-desvios em 2π, que controla a altura do pico.
2. **Norte científico: momentos negativos discretos (MN-1).** Busca bibliográfica adequada de testes numéricos
   anteriores; extensão a mais caracteres (condutores compostos e caracteres complexos) e à Conjectura 8.
3. **Relatório consolidado reprodutível** (C1–C3, VN-1, pico τ = 1, Dirichlet), como produto final citável.
4. Manter as demais frentes congeladas até o relatório existir.

## 7. Outras pendências

- Reclassificar K7 M4 como L (aguarda o usuário).
- Auditoria independente do certificado; procedência/licença completas de `zeros1`.
- `archive/fontes_etapa11/Lagarias&Weiss.tex`: transcrição de origem não registrada, **não é fonte**; fica fora do git.
- `docs/PLANO_COLLATZ.md` e `docs/RELATORIO_CONSOLIDADO.md` ainda mencionam `AGENTS.md`/`prompt.txt`, ausentes do
  repositório público.

## 8. Ambiente e git

- Python: `.venv/bin/python3`; testes: `.venv/bin/python -m pytest -q tests` (**53 passam**, ~50 s, em 27/09).
- Trabalho em curso no branch `revisao-poder-e-hipoteses`. `main` em `e78f96a` (19/09/2026).
- Fora do git por decisão: `paper/`, `hyperref/`, `archive/fontes_etapa11/odlyzko_zeros6_primeiros_2001052.txt`
  (36 MB), PDFs/HTML/TeX de fontes, estados de execução retomável (`progresso_*.json`).

## Atualização documental — 08/10/2026

Família 003 de openai/math: [auditoria dirigida e errata](../results/auditoria_openai_math_20261007/REVISAO_20261008.md). Identidade algébrica local conferida; verificação Lean bloqueada na pré-verificação e prova global não auditada integralmente. A hipótese de região sem zeros 7/8 não substitui RH na nossa cota uniforme. As prioridades e conclusões científicas anteriores permanecem.

### 11/10/2026 — auditoria localizada de QRH

Conferida a aplicação da densidade de zeros à equação (16) do manuscrito de Kintali: sem incompatibilidade encontrada, tomando o Lema 3.3 externo como entrada. Isso não valida a demonstração global. Nota: [auditoria de densidade](../hipoteses/leituras/QRH_AUDITORIA_DENSIDADE_20261011.md). Próximo ponto sugerido: Lema 3/Apêndice B; não executado nesta auditoria. Nenhum dado reservado consultado.

### 12/10/2026 — alvo matemático dos filtros de Collatz

Fechamento derivado em família infinita de congruências, com período mínimo 3^m para a contagem completa de ancestrais. Normas controladas para R=L+/2, mas a normalização natural de média um exige trabalho adicional. [Nota matemática](../hipoteses/COLLATZ_FILTROS_FECHAMENTO_20261012.md). Controles exatos pequenos passaram (5,52 s-CPU); CL1 e campanhas extensas não executadas. Nenhuma ligação com zeros de funções L demonstrada.

### 12/10/2026 — memória finita de médias das árvores

[Nota](../hipoteses/COLLATZ_MEMORIA_FINITA_20261012.md): fechamento exato das médias módulo 3^K na normalização natural, contração Hölder e erro fraco uniforme demonstrados. Controle forte das densidades continua inconclusivo e foi reduzido a convergência uniforme a uma densidade contínua. Relação com antecedentes de Applegate–Lagarias conferida, sem novidade reivindicada. Próxima revisão: resultados posteriores de regularidade; não ampliar campanhas. Piloto racional completo em 0,297 s-CPU, nenhum dado reservado.

### 12/10/2026 — fontes organizadas e lacuna aritmética localizada

[Síntese da leitura](../hipoteses/COLLATZ_REVISAO_REGULARIDADE_20261012.md): Wirsching preliminar lido; Tavares e Hateley v1 lidos de forma dirigida. O primeiro explicita a lacuna por resíduos; Tavares afirma resolver dois elos, sem resolver (⋆3), e apresenta identidade Mellin com ζ conferida localmente. A identidade vale para outras bases, portanto ainda falta especificidade aritmética. Hateley v1 tem inconsistências demonstradas e não fornece fechamento. PDFs organizados com hashes, nenhuma execução científica nova. Próximo trabalho permanece analítico: custo e resíduos conjuntos, não aumento de profundidade.

### 12/10/2026 — Collatz: custo condicionado e resolução residual

- Recorrência conjunta g_ℓ(k,a), lei condicionada w_{ℓ,k} e composição afim: `validado` por derivação. Para ℓ≥16 e 0≤k≤2ℓ, cauda j≥J ≤min(1,5(4/5)^J), sem RH/Collatz.
- Controle absoluto de um passo não dá controle relativo por resíduo: aparece C_ℓ=2·3^{ℓ−1}. Controle relativo crescente e Conjectura 2 seguem `inconclusivo`; não foi propagado erro de truncamento entre todos os passos.
- Declaração ed3b3e30… anterior à implementação; 48 identidades, 181 projeções e 60 cotas exatas passaram. 18 testes rápidos passaram na .venv; Python do sistema sem pytest. CPU 0,156 s, parede 0,156 s, ru_maxrss reportado 261.412 KiB; RLIMIT_CPU=60 s. Sem dados de zeros, CL1, campanhas ou commit.
- Nota: `hipoteses/COLLATZ_CUSTO_RESIDUOS_20261012.md`; código independente `collatz/cost_residues.py`; artefatos `results/collatz_custo_residuos_20261012/`. Próximo alvo: recorrência dos caracteres residuais condicionados ao custo, antes de ampliar resolução.

### 12/10/2026 — Collatz: caracteres condicionados ao custo

- Recorrência exata de caracteres: cada levantamento reduz o condutor em um fator 3, multiplica a frequência por 2^{−j−1} e introduz fase; conserva estados de custo k−j. Identidade `validado`; estimativa de cancelamento `inconclusivo`.
- Referência Haar nas unidades: coeficiente −1/2 nas duas frequências não triviais de condutor 3, zero nas primitivas de condutor maior. Derivada condição suficiente D_ℓ<3/2 para minorante relativa positiva; não demonstrada na janela central. Custos zero dão contraexemplo a contração estrita irrestrita.
- Declaração f05dd9b4…; 1.422 identidades ciclotômicas e 120 de Haar passaram exatamente; 21 testes rápidos passaram. CPU 0,095 s, parede 0,096 s, RSS 17.032 KiB; teto 60 s. Sem dados de zeros, enumeração extensa, CL1 ou commit.
- Nota `hipoteses/COLLATZ_CARACTERES_CONDICIONADOS_20261012.md`; código `collatz/residue_characters.py`; artefatos `results/collatz_caracteres_20261012/`. Próximo alvo: estimativas por condutor na janela central e conferência da referência adequada, antes de ampliar cálculos.

### 12/10/2026 — Collatz: limite central não uniforme

- Para C e K fixos, na janela |k−ℓ|≤C√ℓ, derivada convergência TV dos primeiros K custos para geométricas independentes Pr(J=j)=2^{−j−1}; resíduos convergem a π_K não uniforme. Prova por inclusão-exclusão, majorante somável e razão de coeficientes. Resultado `validado` no escopo da derivação; revisão independente não feita.
- π_1=(0,1/3,2/3); π_2 nas unidades (1,2,4,5,7,8)=(8,16,11,4,2,22)/63. π é estacionária da mistura 1/2,1/2 dos mapas x/2 e (3x+1)/2, distinta do kernel anterior 3/4,1/4. Não há prova de regularidade ou minorante uniforme da densidade em resolução crescente.
- Declaração 74f781b3…; verificação geométrica versus sistema estacionário e projeção passaram; 24 testes passaram. Diagnóstico exato de 24 pares, CPU 0,044 s, parede 0,045 s, RSS 16.684 KiB, teto 60 s. Sem dados de zeros, CL1 ou commit.
- Nota `hipoteses/COLLATZ_LIMITE_CENTRAL_20261012.md`; código `collatz/central_residues.py`; resultados `results/collatz_centro_20261012/`. Próximo alvo: regularidade/minorante de π e comparação bibliográfica, sem inferir K=ℓ do limite com K fixo.

### 12/10/2026 — Collatz: antecedente Tao e regularidade de π

- π identificada exatamente com Syrac de Tao, arXiv:1909.03562v5, Lema 1.12/Remark 1.13. Massas em módulos 3 e 9 já impressas na fonte: reprodução, sem novidade. PDF arquivado com hash, pp.10–11 conferidas visualmente; prova profunda não refeita.
- Aceitando Proposição 1.14, derivada densidade L1 com aproximação L1 superpolinomial. Derivados positividade quase em toda parte nas unidades e obstáculo à limitação: π(−1+3^KZ3)≥2^{−K}; densidade não limitada e não Lp para p≥log3/log(3/2). Não refuta minorante positiva.
- Minorante uniforme e passagem à resolução K=ℓ seguem `inconclusivo`. Identidade exata dos geradores como lei Syrac condicionada ao custo total e aos limites individuais; não é consequência automática dos coeficientes não condicionados de Tao. Próximo trabalho: revisão dirigida de estimativas conjuntas/condicionadas antes de nova grade.
- Declaração a03d082e…; 39 identidades da recorrência da fonte e 52 do ramo fixo passaram; CPU 0,0047 s, parede 0,0052 s, RSS reportado 228.304 KiB, teto 60 s. Sem mínimos experimentais, dados de zeros, CL1 ou commit.
- Nota `hipoteses/COLLATZ_REGULARIDADE_PI_20261012.md`, B34, artefatos `results/collatz_regularidade_pi_20261012/`.

### 12/10/2026 — Collatz: custo conjunto e dois alcances analíticos

- Fórmula conjunta custo/caractere e extração por coeficiente derivadas. Refinamento uniforme q/B=A(θ)+O(1/ℓ) permite TV(p^K,π_K)→0 para K=o(√ℓ), na janela |k−ℓ|≤C√ℓ. Erro relativo aditivo tende a zero para K≤(1/2−ε)log_3ℓ; em k=ℓ exatamente, K≤(1−ε)log_3ℓ. Constantes não avaliadas e revisão independente não feita.
- Aceitando Tao Prop.7.3, derivado decaimento superpolinomial dos caracteres primitivos na resolução K=ℓ, com custo e limites individuais impostos. Prova controla numerador com indicador via majorante positiva; pares (1,2)/(2,1) preservados porque c_i≥2. Não é divisão de coeficiente complexo não condicionado.
- Nem caracteres individuais nem alcance logarítmico dão a minorante por resíduo em K=ℓ: controle agregado segue `inconclusivo`. Estimativa profunda de renovação de Tao não foi refeita. Nenhuma conclusão de RH/Collatz ou novidade.
- Revisão B35/B36: Tao já formula menor massa de Syracuse; Si trata custo condicionado sem nossos limites e não foi usado como premissa. Fontes arquivadas com hash/commit; manifesto anterior preservado.
- Declaração de6b8e1a… e adendo anterior aos pares: 28 majorantes de coeficientes, 39 identidades ciclotômicas e 351 conferências de orientações passaram; 36 diagnósticos parciais não são TV completa. CPU 0,0445 s e 0,0066 s; teto60 s/processo. Sem dados de zeros, CL1, produção extensa ou commit.
- Nota `hipoteses/COLLATZ_CUSTO_CONJUNTO_20261012.md`; artefatos `results/collatz_custo_conjunto_20261012/`. Próximo alvo: estimativa agregada por escala sob condicionamento, com norma e conclusão escolhidas antes de novo cálculo.

### 13/10/2026 — Collatz: mistura L1 condicionada em escalas finais

- Derivado, aceitando Tao Prop.7.3: oscilação O_{m,n}(k)≪_{A,C,ρ}n^{−A}, para |k−n|≤C√n e m≥ρn, log3/(2log2)<ρ<1. Alvo m=ceil(0,9n) fechado como derivação dependente; constantes não avaliadas e revisão independente não feita.
- Separação por corte R e soma t explicita custo restante, limites do sufixo e medida não normalizada. Injetividade do prefixo e controle de colisões permitem Plancherel sem perda exponencial. A cota profunda do sufixo controla numerador com indicador, evitando segunda divisão por probabilidade.
- Minorante por resíduo e escalas sublineares permanecem `inconclusivo`; L1 permite classes excepcionais e não resolve RH/Collatz. Próximo passo: auditar os três pontos críticos da derivação, antes de novos alvos ou CPU.
- Declaração e15f44f4…; 150 decomposições, 714 offsets racionais e 712 offsets modulares passaram. Dois offsets fora do intervalo modular declarado não são falhas. CPU 0,2231 s; parede 0,2439 s; RSS reportado265.244 KiB, teto60 s. Nenhuma oscilação numérica, dados de zeros, CL1 ou commit.
- Nota `hipoteses/COLLATZ_MISTURA_CONDICIONADA_20261013.md`; artefatos `results/collatz_mistura_condicionada_20261013/`.

### 13/10/2026 — auditoria interna da mistura condicionada

- Conferidos preservação dos pares, corte/injetividade, medidas não normalizadas, filtro de frequências e normalização final. Nenhuma falha estrutural encontrada neste escopo; mesma sessão/autoria, NÃO revisão independente ou prova formal. Dependência de Tao Prop.7.3 mantida.
- Correção local: para limiar real b≥0, cauda geométrica é 2^{−floor b}≤2^{1−b}. Fator2 não muda taxa; versão anterior preservada com hash. Convenção de logaritmos explicitada. Scripts e declarações anteriores intactos.
- 126 produtos de Fourier, 28 identidades de Parseval/projeção, 6 massas e 33 cotas de cauda passaram exatamente. CPU0,924 s, parede0,928 s, RSS244.616 KiB reportado, teto60 s.
- Derivado controle do peso de exceções sob p e sua média q. Contraexemplo geral mostra L1 exponencialmente pequeno com classes de massa zero: não é contraexemplo aos geradores, mas bloqueia inferência de minorante sem estrutura adicional.
- Nota `hipoteses/COLLATZ_AUDITORIA_MISTURA_20261013.md`; artefatos `results/collatz_auditoria_mistura_20261013/`. Piores classes e minorante seguem `inconclusivo`; próximo alvo é mecanismo de preenchimento por resíduo e custo, antes de enumerar mínimos. Sem zeros, CL1, produção extensa ou commit.
