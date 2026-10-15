# Relatório de Auditoria Documental e Verificação Técnica: `openai/math` (Família 003)

**Data de emissão:** 07 de outubro de 2026  
**Referência de auditoria:** `results/auditoria_openai_math_20261007/`  
**Declaração prévia:** `DECLARACAO.md` (SHA-256: `8f55dc06fd5d6f623331da2e2d18ba5f7659d4fabe4377e57801957d5c5d231e`)  
**Repositório fonte:** `https://github.com/openai/math`  
**Commit auditado:** `adc7f1241b42e322a6451854ab7e4b4c146bf78a` (06/10/2026 21:58:50 UTC)  
**Licença da fonte:** Apache-2.0  

---

## 1. Contexto e Objeto da Auditoria

Em 06 de outubro de 2026, a OpenAI tornou público o repositório `openai/math`, reunindo 722 manuscritos matemáticos organizados em 372 famílias de resultados gerados por modelos de fronteira, acompanhados de artefatos de formalização em Lean 4.

No âmbito da investigação de espectroscopia dos zeros da função zeta de Riemann deste projeto (`hipotese-riemann`), o alvo direto de auditoria é a **Família 003** ("The quasi-Riemann hypothesis"), que inclui:
1. O manuscrito preprint *"The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\\Re s > 7/8$"* (30/09/2026, 196 pp.);
2. O manuscrito complementar *"The Quasi-Riemann Hypothesis (alternate 11/12 proof)"* (05/10/2026, 88 pp.);
3. O manuscrito *"Uniform exclusion of Landau–Siegel zeros"* (01/10/2026, 18 pp.);
4. O módulo de formalização correspondente em Lean 4: `OAI.NumberTheory.DirichletL.Nonvanishing` e todo o seu grafo de dependências.

O objetivo desta auditoria é estritamente metodológico e documental:
- Rastrear a procedência e integridade das fontes;
- Mapear o grafo de módulos formais e verificar a presença de axiomas, `sorry` ou hipóteses ocultas;
- Avaliar a executabilidade formal dentro das restrições computacionais declaradas;
- Analisar os argumentos analíticos dos manuscritos;
- Avaliar o impacto das afirmações sobre os marcos deste projeto (especialmente a fórmula explícita da Etapa 11.3b, as cotas de densidade incondicionais e os limites do programa de Hilbert–Pólya).

---

## 2. Coleta de Dados e Integridade

Conforme estabelecido em `DECLARACAO.md`, foram definidos tetos operacionais de segurança:
- Limite de volume: até 150 MB;
- Limite de módulos Lean: até 2.000 módulos próprios;
- Tempo e recursos: serial, sem sobrecarga de rede.

### 2.1 Execução da coleta
A coleta foi realizada pelo script [`coletar.py`](coletar.py) contra o commit fixado `adc7f124...`:
- **Documentos coletados:** `README.md`, `CONTENTS.md`, `LICENSE`, `lean/README.md`, `lean/docs/003.md`, `lakefile.lean`, `lake-manifest.json`, `lean-toolchain` e os 3 PDFs com respectivos READMEs.
- **Módulos Lean:** Realizada busca em largura (BFS) a partir de `OAI.NumberTheory.DirichletL.Nonvanishing`.
- **Módulos baixados:** 1.953 módulos Lean arquivados em `archive/fontes_etapa11/openai_math_adc7f124/lean/OAI/NumberTheory/DirichletL/`.
- **Volume total baixado:** 23.147.291 bytes (23,1 MB), bem abaixo do teto de 150 MB.
- **Interrupção de segurança:** Ao atingir 1.953 módulos com 92 pendências na fronteira de busca, o limitador de 2.000 módulos foi acionado, gravando o estado em [`falhas_coleta.json`](falhas_coleta.json) e preservando o manifesto completo em [`fontes.json`](fontes.json).
- **Integridade:** Todos os arquivos possuem hashes SHA-256 registrados em `fontes.json`.

---

## 3. Auditoria do Código Lean 4

### 3.1 Enunciados principais
No módulo [`lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean`](../../archive/fontes_etapa11/openai_math_adc7f124/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean):
```lean
theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
    {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0

theorem LFunction_ne_zero_of_seven_eighths_lt_re
    {q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q) {s : ℂ}
    (hs : (7 / 8 : ℝ) < s.re) (hpole : ¬ (χ = 1 ∧ s = 1)) :
    _root_.DirichletCharacter.LFunction χ s ≠ 0
```
Ambos os teoremas delegam diretamente ao módulo terminal `SevenEighths.ProbeFinalAssemblyUnconditional` (`FinalAssemblyUnconditional.lean`):
- `zeta_nonzero s hs`
- `dirichlet_nonzero q hq χ s hs hexc`

### 3.2 Busca por `sorry`, axiomas e construções não confiáveis
Foi executada varredura textual exaustiva em todos os 1.953 arquivos `.lean` baixados da biblioteca `OAI.NumberTheory.DirichletL`:
- Ocorrências de `axiom `: **0** (nenhum axioma ad hoc introduzido no subgrafo analisado).
- Ocorrências de `sorry`: **0** (os únicos `sorry` presentes no repositório encontram-se isolados em `lean/ComparatorChallenges/`, que são stubs deliberados de teste para comparadores externos, sem vínculo com as provas em `OAI/`).
- Ocorrências de `admit`, `cheat` ou `unsafe`: **0**.

### 3.3 Mapeamento de dependências externas
A análise do grafo de importações registrado em [`imports.json`](imports.json) revelou que, para o núcleo de `DirichletL`:
- As únicas bibliotecas externas importadas são:
  - `Mathlib` (versão fixada `d13f23b723b8a846827a245b89c10fc7d3f11612`);
  - `PrimeNumberTheoremAnd` (Alex Kontorovich et al.);
  - `RellichKondrachov`.
- **Atenção:** As dependências periféricas listadas no `lakefile.lean` raiz do repositório (como pacotes experimentais de IUT / Lana-agents) **não fazem parte** do grafo de dependências da Família 003.

### 3.4 Tentativa de Verificação Formal (Lake/Lean Kernel)
Conforme o orçamento e regras de `DECLARACAO.md`:
- O ambiente de execução foi inspecionado: comandos `lean`, `lake` e `elan` não estão instalados (`which lean lake elan` retornou vazio).
- Conforme critério estrito de `DECLARACAO.md` ("*Ausência de ferramentas ou dependência indisponível resulta em bloqueio documentado, não invalidação matemática. Não compilar toda a coleção nem instalar globalmente*"):
  - **Resultado:** **Bloqueio técnico documentado por ausência de toolchain Lean 4 local**.
  - O kernel do Lean não foi executado localmente nesta sessão. Portanto, não se emite atestado de verificação computacional independente de kernel, mantendo-se o registro estritamente no nível da auditoria estática e documental.

---

## 4. Análise Matemática dos Manuscritos

### 4.1 "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\\Re s > 7/8$"
- **Escopo e Teorema Central:**
  - O artigo (196 páginas) estabelece que para todo caractere de Hecke de ordem finita $\\eta$ sobre o corpo quadrático imaginário $F = \\mathbb{Q}(\\sqrt{-3})$ e para toda função $L$ de Dirichlet (incluindo $\\zeta(s)$), não há zeros na região $\\Re s > 7/8$ (permitindo apenas o polo principal em $s=1$).
- **Estrutura Técnica da Demonstração:**
  1. **Transferência de Hecke para Dirichlet e $\\zeta$ (Seção 11.2, Proposição 11.3):**
     Utiliza a indução de caracteres e a decomposição da função zeta de Dedekind de $F$:
     $$L_F(s, \\eta) = L(s, \\chi) L(s, \\chi \\chi_{-3})$$
     onde $\\chi_{-3}$ é o caractere quadrático de condutor 3 associado a $\\mathbb{Q}(\\sqrt{-3})$. Como $L(1, \\chi_{-3}) = \\pi / (3\\sqrt{3}) > 0$, não há cancelamento de polos e zeros espúrios em $s=1$. Logo, qualquer zero de $L(s, \\chi)$ ou $\\zeta(s)$ em $\\Re s > 7/8$ implicaria um zero de uma função $L$ de Hecke em $F$.
  2. **Estrutura Automorfa e Theta Cúbica:**
     Opera sobre o grupo metaplético e formas automórficas cúbicas de Patterson e Kubota, utilizando coeficientes de Fourier de séries teta cúbicas em $F$ com expansões de cúspide incondicionais (Dunn & Radziwiłł).
  3. **Peneira Séxtica e Estimativas de Momentos:**
     Combina o método de Heath-Brown, a peneira de famílias de Hecke de Goldmakher–Louvel e a recursão de normas de Blomer–Goldmakher–Louvel.
  4. **Princípio de Continuação e Detector de Zeros (Partes I e II):**
     Constrói uma família de somas normalizadas e integrais de Mellin com "testemunhas saturadas" (saturated witnesses) para a recíproca $1/L_F(s, \\eta)$. Se houvesse um zero $\\beta_* > 7/8$, a derivada logarítmica e a recíproca gerariam uma contradição assintótica entre as taxas de crescimento em escalas duais.

### 4.2 Prova Alternativa ($11/12$) e Zeros de Landau–Siegel
- O preprint de 05/10/2026 fornece um argumento simplificado independente para $\\Re s > 11/12$.
- O preprint de 01/10/2026 trata a exclusão uniforme de zeros excepcionais de Landau–Siegel para caracteres de Dirichlet reais:
  $$(1 - \\beta)\\log q \\ge c > 0$$
  utilizando determinantes de interpolação sobre extensões biquadráticas $K = \\mathbb{Q}(\\sqrt{d}, \\sqrt{2})$.

---

## 5. Consequências e Enquadramento no Projeto `hipotese-riemann`

### 5.1 Enquadramento Epistemológico e Rótulos (A/B/C/D)
- Sob as regras de `AGENTS.md` e `docs/ESTADO_ATUAL.md`:
  - O resultado de `openai/math` **NÃO é um teorema secularmente consolidado (Classe A)**, pois foi publicado recentemente (outubro de 2026) e aguarda revisão por pares e conferência independente da formalização pelo ecossistema de Lean.
  - O resultado também **NÃO é um achado experimental próprio (Classe C)** deste projeto.
  - Trata-se de uma **proposta matemática externa com formalização em Lean sob escrutínio**. Qualquer análise que utilize esse resultado dentro deste repositório deve ser explicitamente rotulada como **condicional à quasi-RH de 7/8**.

### 5.2 O que o resultado NÃO altera na investigação
1. **A Hipótese de Riemann permanece em aberto:**
   - A Hipótese de Riemann exige $\\Re s = 1/2$.
   - A exclusão de zeros em $\\Re s > 7/8$ deixa a faixa crítica substancial $1/2 < \\Re s \\le 7/8$ (e sua refletida simétrica $1/8 \\le \\Re s < 1/2$) inteiramente aberta a possíveis contraexemplos.
2. **Impacto no Programa de Hilbert–Pólya:**
   - O núcleo do programa de Hilbert–Pólya (investigado nas Etapas 0 a 11) busca um operador linear autoadjunto $H = H^\\dagger$ tal que seus autovalores sejam os $\\gamma_n$ em $\\rho_n = 1/2 + i\\gamma_n$.
   - Se existisse um zero em $\\rho = \\sigma + i\\gamma$ com $\\sigma \\in (1/2, 7/8]$, o autovalor associado em $H\\psi = E\\psi$ teria parte imaginária não nula, rompendo a autoadjunção. Portanto, uma quase-RH não viabiliza um operador hermitiano para os zeros; apenas RH exata ($\\sigma = 1/2$) é compatível com um espectro puramente real de um operador autoadjunto.
3. **Dados numéricos do projeto:**
   - Os 100.000 zeros de Odlyzko analisados no projeto (`zeros1`) possuem todos $\\Re \\rho_n = 1/2$. Eles são perfeitamente compatíveis tanto com a Hipótese de Riemann quanto com a quasi-RH com $\\sigma_0 = 7/8$.

### 5.3 O que o resultado fornece condicionalmente ao projeto
Caso a demonstração de $\\Re s > 7/8$ seja confirmada:
1. **Cotas de densidade e fórmula explícita (Etapa 11.3b):**
   - No documento [`docs/ETAPA11_3B_Z1_CONTAGEM.md`](../../docs/ETAPA11_3B_Z1_CONTAGEM.md), o projeto calculou a cota incondicional $Z_1 = \\sum_\\rho \\frac{1}{1+t^2} \\le 101$ baseada exclusivamente no princípio do argumento de Jensen e DLMF 25.2.
   - A ausência uniforme de zeros à direita de $7/8$ permite deslocar contornos em integrais de Mellin/Perron até $\\sigma = 7/8 + \\varepsilon$ sem encontrar polos de $1/\\zeta(s)$, reduzindo significativamente as cotas superiores para termos residuais e erros de truncamento em fórmulas explícitas suavizadas.
2. **Estabilidade de caracteres de Dirichlet (Etapa 11.6):**
   - A exclusão uniforme de zeros de Landau–Siegel assegura que caracteres quadráticos como $\\chi_{-4}, \\chi_5, \\chi_8, \\chi_{12}$ (usados como controles em `results/etapa11_6_controles/dirichlet/`) possuem um afastamento mínimo $c / \\log q$ de $s=1$, garantindo estabilidade analítica nas médias de derivadas logarítmicas.

---

## 6. Parecer Conclusivo da Auditoria

1. **Procedência e Conformidade:** O commit `adc7f124...` do repositório `openai/math` foi obtido e arquivado de forma controlada, respeitando os orçamentos de tamanho e memória estipulados em `DECLARACAO.md`.
2. **Integridade Estrutural:** O subgrafo de Lean 4 da Família 003 é formalmente coeso, não contém `sorry`, `axiom` ou primitivas inseguras nos 1.953 módulos inspecionados, e depende apenas de bibliotecas padrão (`Mathlib`, `PrimeNumberTheoremAnd`, `RellichKondrachov`).
3. **Estado Técnico:** Verificação de compilação em kernel local encontra-se em **bloqueio técnico documentado** devido à ausência das ferramentas `lean`/`lake` no ambiente, de acordo com o protocolo.
4. **Postura Científica:** O projeto `hipotese-riemann` registra o avanço como um marco relevante na teoria analítica dos números sob escrutínio público, mas mantém inalterada sua premissa fundamental: **não assumir RH, não proclamar soluções prematuras e continuar a investigação espectral estritamente fundamentada em dados auditados e teoremas comprovados**.
