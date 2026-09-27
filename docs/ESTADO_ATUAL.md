# Estado atual do projeto — ponto de retomada (27/09/2026)

Documento de entrada para quem retoma o trabalho (pessoa ou agente). Resume onde o projeto está, o que está congelado,
quais regras seguir e qual é a próxima tarefa. Os detalhes ficam nos documentos citados; em conflito, eles prevalecem.
Versão anterior (19/09/2026) no histórico do git.

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

**Balanço honesto:** nenhum resultado C (novidade a investigar) está estabelecido. O que existe é infraestrutura
rigorosa e reprodução numérica de teoria conhecida (B).

## 5. Estado das frentes

| Frente | Estado |
|---|---|
| Etapas 0–10 (M1–M4) | validadas |
| 11.1–11.4 | matriz madura (1 pendência: K7 M4); 11.3b encerrada com itens abertos; 11.4 documental |
| 11.5 | não iniciada |
| 11.6 controles | Dirichlet: dados validados (exceto V2′ de χ₅); Maass: não passa; estádio: **encerrado por prioridade** (diagnóstico de poder abortou em g04, parcial e `inconclusivo`) |
| **H-004** (previsão do erro do estimador em L(s, χ)) | **adiada por prioridade** (`results/registro_hipoteses/H-004/ADENDO_H004_3.md`): exigiria a V2′ de χ₅ (~40–50 h-CPU), e o desfecho é quase determinado pela fórmula explícita. Reserva e02–e04/f02–f04 mantida |
| **VN-1** | concluída (ver §4) |
| **Pico de K_c em τ = 1** | **pausado a pedido do usuário** (ver §6) |
| EXP26-1, EXP26-3 a 5 (`hipoteses/DIRECAO_EXPERIMENTAL_20260926.md`) | propostas; não iniciadas |
| Collatz | CL0 entregue (documental); CL1 não executada; ponte direta sem mecanismo encontrado; A₅(x) (ramos 5/16) como pergunta barata, não iniciada |
| Etapas 12–13 | pendentes |

## 6. Próxima tarefa recomendada

1. **Pico de K_c em τ = 1 (retomar só com aval do usuário).** Derivação feita: em τ = 1, K_c mede E[e^{2πi S_n}]
   amostrado nos zeros. Com amostragem uniforme em t, esse valor é **exatamente zero**, e a variância de S nos zeros
   é menor por 1/12 por ponto (identidade de integração por partes). Modelo: V_k ≈ Σ²_Berry(k) − 1/6 com fases
   gaussianas. Estado: `src/riemann_spectra/bragg_peak.py` escrito, **sem testes**; controle em GUE rodado, com saída
   **não lida** em `results/pico_tau1_20260926/rascunho/`; **nenhuma ficha congelada; nenhum valor medido do pico
   foi olhado para esta análise.** Próximos passos: ler o controle GUE, escrever testes, congelar a ficha e medir.
2. **Relatório consolidado reprodutível** (C1–C3, VN-1, pico τ = 1, Dirichlet), como produto final citável.
3. Manter as demais frentes congeladas até o relatório existir.

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
