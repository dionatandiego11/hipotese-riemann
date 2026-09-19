# Estado atual do projeto — ponto de retomada (19/09/2026)

Documento de entrada para quem retoma o trabalho (pessoa ou agente). Resume onde o projeto está, o que está congelado,
quais regras seguir e qual é a próxima tarefa. Os detalhes ficam nos documentos citados; em caso de conflito, eles
prevalecem sobre este resumo.

## 1. O que é o projeto (em uma linha)

Espectroscopia inversa dos zeros da função zeta: medir, com protocolos pré-registrados e controles, que informação
aritmética (linhas em log p com coeficientes −Λ(n)/(π√n)) é recuperável de listas finitas de zeros, e avaliar classes de
operadores candidatos (programa de Hilbert–Pólya). **O projeto não tenta provar RH e não afirma nada a favor dela.**

## 2. Regras de trabalho (obrigatórias)

- **Declaração prévia antes de código ou cálculo:** todo experimento, controle ou derivação que decide algo é escrito
  antes, com SHA-256 registrado em arquivo `.sha256` ao lado (modelo: `results/etapa11_r5/DECLARACAO_*.md`,
  `results/etapa11_6_controles/`). Protocolos não mudam depois de ver dados; mudanças só por adendo com causa.
- **Resultados negativos e falhas são registrados**, nunca apagados (execuções invalidadas ficam preservadas).
- **Rótulos:** A (matemática conhecida, com hipóteses), B (reprodução numérica), C (achado experimental cuja novidade
  ainda não foi investigada), D (conjectura). Separar sempre o que é condicional (RH, H-tab, conjecturas) do que não é.
- **Sem afirmação de novidade** sem busca bibliográfica (a feita até agora é preliminar:
  [BUSCA_BIBLIOGRAFICA_MANUSCRITO.md](BUSCA_BIBLIOGRAFICA_MANUSCRITO.md)).
- **Fontes:** só vale o que foi lido na fonte, com página. Resumo de busca ou texto gerado por IA não é fonte.
  Cada fonte baixada vai para `archive/fontes_etapa11/` e é registrada em `archive/fontes_etapa11/MANIFESTO.csv`
  (URL, versão, data, páginas, SHA-256). Os PDFs/HTML **não** entram no git (`.gitignore`); só o manifesto.
- **Código e artefatos congelados de m3/m4 e do certificado não são editados** (locks em `configs/*.lock.json`; manifesto
  de 59 hashes em `results/etapa11_r5/MANIFESTO_CERT.csv`). Código novo vai em caminho novo.
- **Execuções longas são rodadas pelo usuário:** o agente entrega os comandos (sempre com `.venv/bin/python3`, a partir da
  raiz do repositório) e o usuário decide quando rodar.
- **Formato de arquivos:** o repositório usa `* -text` (`.gitattributes`); vários CSVs usam **CRLF** (por exemplo
  `docs/etapa11_*.csv`, `archive/fontes_etapa11/MANIFESTO.csv`). Editar preservando os bytes de fim de linha.
- **Documentação em português.** Commits só quando o usuário pedir; não commitar direto na `main` (usar branch; o usuário
  integra e faz o push).
- Instruções de agente adicionais podem existir num `AGENTS.md` local (fora do repositório público).

## 3. Onde cada coisa está

| Assunto | Documento |
|---|---|
| Plano geral (etapas 0–13, marcos M1–M5) | [../PLANO_IMPLEMENTACAO.md](../PLANO_IMPLEMENTACAO.md) |
| Tabela de estado por etapa e log | [ANDAMENTO.md](ANDAMENTO.md) |
| Protocolos pré-registrados m3/m4 | [PROTOCOLO.md](PROTOCOLO.md); configs em `configs/` |
| Resultados M1–M4 consolidados | [RELATORIO_CONSOLIDADO.md](RELATORIO_CONSOLIDADO.md) |
| Plano da Etapa 11 (tipos M, N, T; códigos S/V/C/P/L/PC) | [ETAPA11_PLANO.md](ETAPA11_PLANO.md) |
| Matriz de operadores (classes K1–K12) | [ETAPA11_MATRIZ_OPERADORES.md](ETAPA11_MATRIZ_OPERADORES.md), `etapa11_matriz_operadores.csv`, `etapa11_evidencias.csv` |
| Fontes pendentes e lidas | [ETAPA11_PENDENCIAS_FONTES.md](ETAPA11_PENDENCIAS_FONTES.md) (§§5–12 registram as rodadas de 17/09) |
| Certificado condicional (11.3b) | [ETAPA11_3B_H1_CAUDA_PROJETADA.md](ETAPA11_3B_H1_CAUDA_PROJETADA.md) §§II.17–II.24; `results/etapa11_r5/`; auditoria: [PROTOCOLO_AUDITORIA_CERTIFICADO.md](PROTOCOLO_AUDITORIA_CERTIFICADO.md) |
| Encerramento da 11.3b | [ETAPA11_3B_ENCERRAMENTO.md](ETAPA11_3B_ENCERRAMENTO.md) |
| Controles da 11.6 | `results/etapa11_6_controles/` |
| Frente Collatz (não iniciada) | [PLANO_COLLATZ.md](PLANO_COLLATZ.md) |

## 4. Estado por etapa

| Etapa | Estado |
|---|---|
| 0–9 (M1–M3) | validadas |
| 10 (M4, zeros 10.001–100.000) | validada (m4-v1, m4-v2, m4-v3; R2 de m4-v3 acionada e investigada). Restos: implementação independente completa, densidade θ na cadeia completa, inversão harmônica |
| 11.1–11.2 | matriz de operadores madura: **27 entradas sustentam decisão**; resta **1 pendência de conferência (K7 M4)** |
| 11.3b | **encerrada em 17/09/2026** com itens abertos registrados (H1, S1, S3a, S3c, C2 completo, H-tab, F5, auditoria); F5 conferido depois, em 19/09, numa transcrição |
| 11.4 | entrega documental preliminar (correspondências; C19 conferida) |
| 11.5 | **não iniciada** (protocolo dos testes discriminantes). Quase todas as classes caíram por derivação; pode restar pouco para testar numericamente |
| 11.6 | **em execução**: K12 declarado (sem cálculo novo); controle Dirichlet declarado e com derivação D1 escrita; controles dinâmico (bilhar) e aritmético (triângulo modular) pendentes |
| 12, 13 | pendentes |
| Collatz CL0–CL5 | pendente |

**Resultados centrais já registrados (não refazer):**
- M3/M4: recuperação de linhas em log p sem catálogo (C1) e concordância de coeficientes (C2, máximo entre elegíveis
  ≤ 2,6·10⁻⁹) nos 30 blocos (classe B).
- Estatística local (C3, classe B), com Holm entre blocos: CDF de espaçamentos e K_c **rejeitam** tanto Poisson quanto o
  **GUE finito usado como controle** (3.000 níveis centrais de GUE tridiagonal, unfolding pelo semicírculo) em todos os
  blocos; R₂ é rejeitado em só 1 dos 30 blocos (b02, m4-v1); Var(s) fica abaixo do envelope desse GUE e cresce lentamente com a
  altura. Isso é uma restrição ao **procedimento de comparação** e **não** implica incompatibilidade com a
  universalidade GUE assintótica (plano da Etapa 11, §2.2, N4; [RELATORIO_CONSOLIDADO.md](RELATORIO_CONSOLIDADO.md) §3.3).
- Certificado (11.3b), corte (8, 2), 461 linhas elegíveis: **(N)** fidelidade numérica do valor registrado,
  incondicional na base de confiança; **(T)** |r̂ − 1| ≤ 10⁻⁶ **sob RH e H-tab**. Sem auditoria independente.
  Publicado no GitHub e no Zenodo (doi:10.5281/zenodo.22811040).
- Matriz: K1, K5a, K5b, K7, K8, K9 com incompatibilidades demonstradas ou derivadas (escopo registrado em cada
  evidência); K3a e K4 condicionais (C); K12 é o controle de ajuste.

## 5. Próxima tarefa (em andamento)

**Controle `ctrl-dirichlet-v1`** (11.6), com resposta conhecida: aplicar o instrumento m4-v3 a zeros de L(s, χ₋₄) e
L(s, χ₅) e verificar linhas com coeficiente −Λ(n)χ(n)/(π√n) (sinal trocado onde χ(n) = −1, ausentes onde χ(n) = 0).

- Declaração: `results/etapa11_6_controles/DECLARACAO_DIRICHLET.md` (SHA-256 `e6cb8ab8…`).
- Derivação D1 (feita, confere P1 e P2, sem adendo): `results/etapa11_6_controles/D1_DERIVACAO_DIRICHLET.md`
  (SHA-256 `f07972a4…`).
- **Passo 3 (feito em 19/09/2026):** código e testes em `results/etapa11_6_controles/dirichlet/`, fora do pacote
  congelado (o lock `package` de m4-v3 cobre todos os módulos de `src/riemann_spectra`):
  - `dirichlet_zeros.py`: zeros por troca de sinal de Z_χ (Hurwitz em mpmath, 30 dígitos, passo ≤ 1/8 do espaçamento,
    refinamento Illinois até 10⁻¹⁰) e verificações V1–V4; grava zeros com 9 casas e manifesto JSON;
  - `instrumento_chi.py`: instrumento m4-v3 com d̄_χ, unfolding por N̄_χ nos nulos e nas linhas sintéticas, catálogo com
    c_χ(n) e critérios D-C1, D-C1z, D-C2, D-C2s, D-C2z; reaproveita as funções do pacote sem editá-las;
  - `ctrl_dirichlet_v1.toml`: parâmetros de m4-v3 com as trocas declaradas; `test_dirichlet.py`: 19 testes (incluindo
    reprodução do termo suave congelado com q = 1 e recuperação diferencial de linhas com sinais conhecidos).
  - Custo observado no desenvolvimento: ~0,7 s por avaliação de L(½ + it, χ) em t ≈ 9.000 (mpmath). A extrapolação para
    12.000 zeros por caractere é da ordem de dezenas de horas; o piloto mede o custo real, e uma troca de método exigiria
    adendo antes da execução completa.
- **Passo 4 (feito em 19/09/2026): piloto** de 500 zeros por caractere, rodado pelo usuário. V1–V3 aprovados; V4 falhou
  por defeito de desenho (o último ponto de teste caía sobre o último zero, onde |Z| ≈ 0). **Adendo 1**
  (`ADENDO_DIRICHLET_1.md`, SHA-256 `6ee78368…`, gravado antes da correção): pontos médios entre zeros. Com ele, V4 foi
  refeita sem recalcular os zeros e os dois pilotos ficaram **aprovados**. Registro e custo em
  `results/etapa11_6_controles/dados_piloto/REGISTRO_PILOTO.md`: ~20–35 h para χ₋₄ e ~35–55 h para χ₅ nos 12.000 zeros,
  em estimativa, e sem ponto de retomada.
- **Adendo 2 (operacional, 19/09/2026; `ADENDO_DIRICHLET_2.md`, SHA-256 `61995046…`):**
  - salvamento e retomada determinísticos (`progresso_<carater>_<n>.json`, trava por PID, SIGINT/SIGTERM);
  - aceitação estrita do refinamento: Illinois ≤ 100 iterações, depois bisseção, e erro se não convergir. Antes, um
    intervalo não convergido era aceito em silêncio;
  - testes T1–T4 aprovados: 31 testes, incluindo um processo real terminado por SIGTERM e retomado com arquivo final
    idêntico bit a bit;
  - os 1.000 zeros dos pilotos têm troca de sinal em ±6·10⁻¹⁰ (`verificacao_refinamento_*.json`);
  - benchmark em `dados_piloto/BENCHMARK.md`: ~53 h (χ₋₄) e ~108 h (χ₅) em paralelo, ±30%;
  - versões anteriores do script preservadas em `dirichlet/versoes/`.
- **Passo 5 (em execução desde 19/09/2026, 13:42):** cálculo completo dos 12.000 zeros por caractere em
  `results/etapa11_6_controles/dados/`, retomável (se parar, rode de novo os comandos de `dados_piloto/BENCHMARK.md`).
  Estimativa: ~2 dias para χ₋₄ e ~4,5 dias para χ₅.
  Depois: execução do instrumento nos 8 blocos (e01–e04, f01–f04) e relatório com os critérios D-C1, D-C1z, D-C2,
  D-C2s e D-C2z.

## 6. Outras pendências

- **Decisão possível:** reclassificar K7 M4 como L (a fórmula de traço de bilhares é semiclássica; não há igualdade exata
  a comparar). Aguarda o usuário.
- **Controle aritmético `ctrl-maass-v1` (19/09):**
  - declaração `DECLARACAO_MAASS.md` (`5db97004…`): setor ímpar, 1.092 formas do LMFDB, fórmula de traço exata;
  - derivação `D1M_DERIVACAO_MAASS.md` (`773a077b…`), a partir de Bolte & Grosche (2.31) e Bolte & Steiner (13), lidos
    na fonte: normalização por classes de PSL(2,ℤ) e **cosh** para as reflexões com deslizamento;
  - `ADENDO_MAASS_1.md` (`4efb9020…`) corrige P2 e P3 da declaração;
  - catálogo `G1_CATALOGO_GEODESICAS.md` (`8705bd7f…`): 22 linhas em t ≤ 5; dois algoritmos concordam em todos os
    discriminantes.
  - **Próximo:** código do instrumento em R e execução nos blocos H, h1 e h2 (minutos de CPU).
- **Controle dinâmico `ctrl-estadio-v1`:**
  - declaração `DECLARACAO_ESTADIO.md` (`c7ce5d5b…`);
  - derivação `D1E_DERIVACAO_ESTADIO.md` (`c0c28ed9…`): linha "bouncing ball" exata e C̄_bb operacional;
  - catálogo de órbitas `O1_CATALOGO_ORBITAS.md` (`0f7cb16e…`): 6 comprimentos em t ≤ 5;
  - `vergini` compilado pelo usuário e com teste de funcionamento em k = 100 aprovado.
  - **Próximo:** código do instrumento em k e comandos de convergência e produção para o usuário.
- **Externas:** auditoria independente do certificado; procedência/licença completas de `zeros1`. Weil (1952), F5, foi
  conferido em 19/09 numa transcrição LaTeX (Vella-Chemla, 2020): as condições (A) e (B) cobrem as gaussianas e h_ε
  (§16 das pendências de fontes). Conferir o fac-símile continua desejável, mas não bloqueia nada.
- **Limpeza:** `docs/PLANO_COLLATZ.md` e `docs/RELATORIO_CONSOLIDADO.md` ainda mencionam `AGENTS.md`/`prompt.txt`, que
  não estão no repositório público.

## 7. Ambiente e estado do git

- Python do projeto: `.venv/bin/python3` (mpmath 1.4.1, numpy 2.5.3). Não há TeX no sistema.
- `main` sincronizada com `origin/main` em `e78f96a` (19/09/2026). Mudanças posteriores a esse commit, se houver, estão
  listadas em `git status`.
- Fora do git por decisão: `paper/` (rascunho de manuscrito, **não será publicado**), `hyperref/`,
  `archive/fontes_etapa11/odlyzko_zeros6_primeiros_2001052.txt` (36 MB), PDFs/HTML de fontes.
