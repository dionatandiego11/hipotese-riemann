# Etapa 11 — matriz bibliográfica de classes de operadores (preliminar)

- **Plano, convenções e códigos:** [ETAPA11_PLANO.md](ETAPA11_PLANO.md).
- **Resumo por classe × requisito:** [etapa11_matriz_operadores.csv](etapa11_matriz_operadores.csv), em formato longo com
  campos separados `situacao` (estado matemático) e `conferencia` (estado bibliográfico), além de `sustenta_decisao`.
- **Evidência de cada S e V** (página, enunciado, hipóteses, argumento): [etapa11_evidencias.csv](etapa11_evidencias.csv).
- **Fontes arquivadas** (versão, URL, data, SHA-256, correspondência de páginas):
  [archive/fontes_etapa11/MANIFESTO.csv](../archive/fontes_etapa11/MANIFESTO.csv).

**Estado:** preliminar, revisão 11.3 de 14/09/2026, com ajustes 11.3b-1 na mesma data (§0.4). **Os códigos não devem ser usados para selecionar ou excluir
candidatos** enquanto houver entradas PC relevantes (§0.3).

Convenções de citação:
- páginas de artigos lidos no arXiv seguem a paginação da versão arXiv indicada;
- "resumo" indica que só o resumo foi lido;
- "não lida" indica que a fonte não foi obtida nesta revisão.

## 0. Revisão 11.3

### 0.1 Pontos da auditoria e tratamento

| # | Ponto | Tratamento |
|---|---|---|
| 1 | "Satisfeito por construção" amplo demais; construções condicionais devem receber C | K8: N1–N4 passam de S a **L**, porque a reprodução dos primeiros 500 zeros não cobre os 100.000. K4: N1–N4 passam de S a **C**. K12: S mantido só com qualificação explícita (N ≥ 100.000 níveis inseridos com a precisão do dado). Regra geral no plano §2.2 |
| 2 | Connes precisa de descrição própria do objeto espectral | K3 dividido em **K3a** (Teorema 1, com parâmetro δ > 1: espectro pontual dos zeros **críticos**, multiplicidade truncada) e **K3b** (formulação sem δ: espectro de **absorção**, zeros não críticos como **ressonâncias**, fórmula de traço global). N1–N4 para K3b: **L**, com a tradução para uma sequência de emissão não especificada. Para K3a: **C**. Leitura do [artigo original](https://arxiv.org/abs/math/9811068) |
| 3 | Exclusões 1D não demonstradas (o oscilador harmônico é contraexemplo) | V retirado de K2a (M4, N2, N3) e de K8 (M4). Agora **L**. A regra "sem derivação para o sistema concreto, sem V" está no plano §4 |
| 4 | A leitura distribucional deve preservar a ressalva de RH | Plano §3.2: a densidade de deltas reais é condicional a RH como identidade global. L-EF2 ampliada com a parte (b), condicionalidade |
| 5 | O controle de Selberg não deve exigir ausência de r·log p; a amplitude completa contém ℓ_γ | Plano §5 e K5: o teste passa a prever comprimentos, amplitudes completas ℓ_γ/(2 sinh(nℓ_γ/2)), tolerâncias e taxa de coincidências acidentais. A frase anterior "sem o fator log p/π" estava **errada**: com ℓ_γ = log p, a amplitude contém log p. Ver K5 |
| 6 | Registro verificado não sustenta "demonstrado"; retirar ranking | Todo S/V tem linha de evidência. Afirmações sem página conferida passam a **PC** (código novo) ou P. A frase "Connes e de Branges chegam mais perto" foi retirada |
| — | Estado administrativo | `em andamento` → `em execução` no ANDAMENTO |

Correções adicionais encontradas na leitura:
- **Sierra 2008 (K2b), M2:** era V, passa a P. O texto afirma que, sob suposições adicionais, os zeros críticos são
  estados ligados (arXiv p. 4, p. 30–31). A classificação anterior ("apenas ressonâncias médias") descrevia só a
  seção VI.
- **K1, M4:** era V, passa a L. "Sem órbitas periódicas" é um enunciado clássico/semiclássico, não uma
  incompatibilidade demonstrada de uma fórmula de traço do operador.
- **Connes, Teorema 5 — correção bibliográfica do projeto** (não é resultado nem novidade científica: o próprio artigo
  declara o escopo). O teorema está enunciado e provado para corpos globais de característica positiva (arXiv p. 42).
  Para k = ℚ, o texto descreve a extensão como análogo (p. 45–47). A matriz anterior do projeto atribuía a equivalência
  a ζ sem essa distinção.

### 0.2 Fontes lidas nesta revisão

| Fonte | Versão lida | Uso |
|---|---|---|
| Connes 1999, *Trace formula in noncommutative geometry…* | arXiv:math/9811068v1 (88 p.) | K3a, K3b |
| Conrey & Li 2000 | arXiv:math/9812166v1 | K4 |
| Bender, Brody & Müller 2017 | arXiv:1608.03679v4 | K2d |
| Bellissard 2017, comentário | arXiv:1704.02644v1 | K2d, K1 (M1) |
| Bender, Brody & Müller 2017, réplica | arXiv:1705.06767v1 | K2d |
| Sierra 2008 | arXiv:0712.0705v1 | K2b |
| Sierra & Townsend 2008 | arXiv:0805.4079v2 | K2c |
| Berry & Keating 1999, SIAM Rev. 41, 236–266 | cópia do artigo publicado (paginação da revista) | K1, K6 |
| Marklof 2004, *Selberg's trace formula: an introduction* | arXiv:math/0407288v2 | K5 (fonte secundária rigorosa; Selberg 1956 não lida) |
| van de Lune, te Riele & Winter 1986, Math. Comp. 46, 667–681 (lida em 17/09/2026) | cópia da versão publicada (repositório CWI) | K3a N1–N4 |
| Platt & Trudgian 2021 (lida em 17/09/2026) | arXiv:2004.09765v1 | K3a N1–N4 |
| Wu & Sprung 1993, Phys. Rev. E 48, 2595–2598 (lida em 17/09/2026) | versão publicada (obtida pelo usuário) | K8 |
| Berry & Keating 2011, J. Phys. A 44, 285203 (lida em 17/09/2026) | versão publicada (obtida pelo usuário) | K2a |
| Lagarias 2006, *Hilbert Spaces of Entire Functions and Dirichlet L-Functions* (lida em 17/09/2026) | preprint de janeiro de 2006 (obtido pelo usuário) | K4 |
| Hörmander 1968, *The spectral function of an elliptic operator*, Acta Math. 121 (lida em 17/09/2026) | arquivo da Acta Mathematica (Tsinghua) | K9 |

Não obtidas:
- Duistermaat & Guillemin 1975;
- Balian & Bloch 1972;
- Selberg 1956;
- Hejhal;
- BGGS 1992 e BSS 1992 (só os resumos);
- Gutzwiller 1971.

### 0.4 Ajustes 11.3b-1 (segunda auditoria)

| Ponto | Tratamento |
|---|---|
| K5a: evidência não sustenta V em N1 | N1 passa a **PC** (`situacao`). O escopo de M2/M3 fica explícito: incompatibilidade **assintótica global**, sob as identificações afins declaradas, que não implica violação das tolerâncias numéricas de N1 na faixa finita. `E-K5-N1` foi retirada: diferenciava uma equivalência assintótica de uma função em degraus sem justificativa. `E-K5-M3` foi reescrita como comparação de contagens, sem derivar |
| Mesma distinção em K7 e K9 | N1 = PC em ambas, e M2/M3 alegados via Weyl ficam com escopo assintótico e `conferencia=PC` |
| Condicionalidade × conferência | O CSV separa `situacao` (S, V, C, P, L, PC, NA) de `conferencia` (conferido, derivacao, elementar, PC, NA). Exemplos: K4 fica `situacao=C`, `conferencia=PC` (resumo de Lagarias); K3a N1–N4 fica `C/PC` (citação da verificação dos zeros pendente; **atualizado em 17/09/2026: `C/conferido`, §0.5**). `sustenta_decisao = sim` só para S/V com conferência concluída ou derivação escrita (15 entradas; **16 após §0.5**) |
| Arquivo das fontes | Cópias exatas em `archive/fontes_etapa11/`, com `MANIFESTO.csv` (versão, URL, data e hora do download, SHA-256, correspondência de páginas) e `README.md`. As páginas citadas referem-se a esses arquivos. Novos downloads só valem como idênticos após comparar o SHA-256 |
| Connes, característica positiva | Registrada como **correção bibliográfica do projeto**, sem classificação de novidade (§0.1) |


### 0.5 Atualização com fontes lidas em 17/09/2026

Fontes registradas em `archive/fontes_etapa11/MANIFESTO.csv` e [ETAPA11_PENDENCIAS_FONTES.md](ETAPA11_PENDENCIAS_FONTES.md)
§§5–6. Só as três entradas abaixo mudaram.

| Entrada | Antes | Depois | Evidência | Motivo |
|---|---|---|---|---|
| K3a N1–N4 | `C` / `PC` | `C` / `conferido` | E-K3a-N-ZEROS | criticidade e simplicidade dos zeros 1–100.000 com fonte lida (van de Lune, te Riele & Winter 1986, p. 667; Platt & Trudgian, Teor. 1). O código **continua C**: a promoção a S não foi decidida, depende também de H-tab, e o teste segue não discriminante |
| K8 M1 | `PC` / `PC` | **`V` / `conferido`**, `sustenta_decisao = sim` | E-K8-M1 | Wu & Sprung p. 2596: potencial obtido por mínimos quadrados sobre os primeiros N zeros |
| K8 M2 | `P` / `PC` | `P` / `conferido` | E-K8-M1 | 500 zeros, desvio médio < 4·10⁻⁶ (p. 2596) |
| C19 (correspondências) | `conferencia = PC` | `conferido` | — | Milne LEC Teor. 27.6/27.15 e Deligne (1.15), p. 279 |

Nenhuma dessas mudanças seleciona candidatos nem congela testes (§0.3 e plano §4 continuam valendo).

### 0.6 Segunda atualização de 17/09/2026 (Berry & Keating 2011)

| Entrada | Antes | Depois | Evidência | Motivo |
|---|---|---|---|---|
| K2a M1 | `S` / `PC` | **`P` / `conferido`** | E-K2a-M1 | p. 5: extensões auto-adjuntas afirmadas a partir de condição de hermiticidade, sem prova de domínio. **Rebaixamento**: o S anterior vinha só do resumo |
| K2a M3 | `P` / `PC` | `P` / `conferido` | E-K2a-M3 | pp. 12–13: só os dois primeiros termos da contagem coincidem; falta 7/8 |
| K2a N1 | `P` / `PC` | `P` / `conferido` | E-K2a-M3 | primeira correção da densidade com sinal oposto; sem avaliação na faixa |
| K2a M4 | `L` | `L` (só observação) | — | §6: uma órbita primitiva por energia, contra períodos log p |
| K9 M1 | `S` / `PC` | `S` / `conferido`, sustenta decisão | E-K9-M1 | Hörmander pp. 193 e 205 |
| K9 M2, M3 | `V` / `PC` | `V` / `derivacao`, sustentam decisão | E-K9-M2, E-K9-M3 | Weyl com resto (Teor. 5.1, p. 215) integrado + comparação de contagens, como em K5a; escopo assintótico |
| K7 M2, M3 | `V` / `PC` | `V` / `derivacao`, sustentam decisão | E-K7-M2, E-K7-M3 | Weyl de bilhares (Bäcker, eq. 49) + comparação de contagens; escopo assintótico |
| K7 N4 | `C` / `PC` | `C` / `conferido` | E-T5-BGS | conjectura BGS (Scholarpedia); enunciado original GOE |
| K5a N4 | `PC` / `PC` | **`P` / `conferido`** | E-T6-ARIT | Poisson em superfícies aritméticas, heurístico/numérico (Bogomolny; BLS 1996) |
| K5a M4, N3 | `PC` / `PC` | `V` / `derivacao`, sustentam decisão | E-K5-M4-SINAL, E-K5-N3-SINAL | argumento de sinal das massas pontuais (Weil negativo, Selberg positivo) |
| K7 M1 | `S` / `PC` | `S` / `conferido`, sustenta decisão | E-K7-M1 | Pankrashkin, Ex. 2.10, Def. 2.13, Props. 3.23 e 3.30 |
| K5a N1, K7 N1, K9 N1 | `PC` | `L` | — | não decidível no nível da classe (resto de Weyl sem constante explícita; classe infinita) |
| K5b M1 | `PC` / `PC` | `S` / `conferido`, sustenta decisão | E-K5b-M1 | Iwaniec p. 6 (secundária) |
| K5b M2 | `PC` / `PC` | `V` / `elementar`, sustenta decisão | E-K5b-M2 | espectro contínuo [¼,∞) não é enumerável |
| K5b M3 | `PC` / `PC` | `V` / `derivacao`, sustenta decisão | E-K5b-M3 | Weyl (vol/4π)T² contra (E/2π)log E; escopo assintótico |
| K5b M4 | `PC` / `PC` | `P` / `conferido` | E-K5b-M4 | estrutura parcial; igualdade nem demonstrada nem refutada |
| K4 M1, M2, M3, M6, N1–N4 | `C` / `PC` | `C` / `conferido` | E-K4-TEOR1 | Lagarias, Teorema 1 (p. 9) e p. 7: de Branges ⇔ RH; estrita ⇔ RH e zeros simples; espectro simples. Situação inalterada |

`sustenta_decisao = sim`: 16 entradas após K2a (K2a M1 era S/PC, portanto já não sustentava); **19 após K9** (M1, M2, M3); **21 após K7** (M2, M3); **24 após K5b** (M1, M2, M3); **26 após K5a** (M4, N3); **27 após K7 M1**.

### 0.3 Entradas PC e pendências (11.3b)

1. ~~**K2a, M1:** auto-adjunticidade das extensões, com página em BK 2011 (texto integral).~~ **Resolvido em 17/09/2026 (§0.6): texto lido; M1 rebaixado de S para P.**
2. **K5, M4 e N3:** incompatibilidade de sinal e normalização entre Selberg e Weil. Depende de L-EF1 (constantes da
   fórmula explícita na convenção de §3.1).
3. **K5, N4:** estatística das superfícies aritméticas, com página em BGGS 1992, BSS 1992 ou Bogomolny et al.,
   Phys. Rep. 291 (1997).
4. **K5b:** caso cofinito e PSL(2,ℤ). Lei de Weyl para formas cuspidais e matriz de espalhamento com ξ (Hejhal ou
   Iwaniec).
5. **K7, M1–M4 e N1:** lei de Weyl para domínios limitados e auto-adjunticidade do laplaciano de Dirichlet, com fonte e
   hipóteses sobre a fronteira.
6. ~~**K8, M1:** o método de Wu–Sprung usa os zeros? Conferir no texto integral.~~ **Resolvido em 17/09/2026 (§0.5): usa; M1 = V.**
7. **K9, M1–M3 e N1:** lei de Weyl de Hörmander e hipóteses de Duistermaat–Guillemin. **M1–M3 resolvidos em 17/09/2026 com Hörmander (§0.6)**; N1 continua PC; Duistermaat–Guillemin só para M4.
7a. **K5a, K7, K9, N1:** para V seria necessária estimativa quantitativa com erro controlado na faixa de alturas do
   projeto (por exemplo, lei de Weyl com resto explícito para o sistema concreto) ou experimento específico. A diferença
   assintótica de contagens não basta.
7b. ~~**K4:** obter o texto de Lagarias (2006) para conferir o enunciado condicional (`conferencia`).~~ **Resolvido em 17/09/2026 (§0.6): preprint lido; códigos mantidos C, conferência concluída.**
8. ~~**K3a, N1–N4:** citar o resultado de verificação computacional de que os zeros 1–100.000 são críticos e simples.
   Sem essa citação, a condição de C não está documentada.~~ **Resolvido em 17/09/2026 (§0.5): citação lida; código mantido C.**
9. **K3b:** especificar uma tradução entre espectro de absorção e as restrições N. Enquanto isso não existir, fica L.
10. **L-EF1 e L-EF2**, com estado 11.3b em [ETAPA11_3B_FORMULA_EXPLICITA.md](ETAPA11_3B_FORMULA_EXPLICITA.md):
    - L-EF1 parcial: estrutura, termo primo e termo arquimediano derivados (H2, classe 𝒢); aplicabilidade do Teorema 1
      de Weil a 𝒢 PC (F5); classe suficiente 𝒜 derivada via Teorema 6 de Connes (conferido) com Z1 derivado; pendências bibliográficas F5 e J1;
    - L-EF2a/b (revisão 11.3b-2): completude da tabela B, fator 2 e restos explícitos; criticidade até H₀ e cota de
      contagem PC;
    - L-EF2c: aberta (a cota absoluta utilizada não fecha). **Estado de H1 (revisão 11.3b-26):**
      - S3b derivada condicionalmente; S1 quantificado e aberto;
      - R5 formalizado e encerrado;
      - Cauda Projetada: condição suficiente para S2-ratio′(U₂) certificada, condicional a RH, para M^math em (8, 2),
        461/461 elegíveis (execução 4 vigente, dependência herdada eliminada);
      - S3a, S3c e passagem ao estimador registrado pendentes; **H1 aberta**.
      Nada disso altera códigos da matriz nem libera seleção de candidatos.
    Com as constantes do termo primo derivadas, a incompatibilidade de sinal de K5a M4/N3 fica desbloqueada para
    derivação, mas não foi feita.
11. **C11/C19:** fontes (Milne, Deligne) inacessíveis nesta sessão (conexão recusada); convenção de Frobenius PC. **C19 resolvido em 17/09/2026 (§0.5)**; C11 mantém `conferido-secundaria` (o sinal de Lefschetz não foi reconferido).

---

## K1 — Berry–Keating: H = xp

**Fontes:**
- Berry & Keating 1999, SIAM Rev. 41, 236–266 (lida);
- Berry & Keating 1999, *H = xp and the Riemann zeros* (não lida);
- Bellissard, arXiv:1704.02644, p. 2 (auto-adjunticidade do gerador de dilatações).

| Campo | Conteúdo |
|---|---|
| Espaço / domínio / contorno | L²(ℝ₊, dx); A = −i(x d/dx + ½), gerador do grupo unitário de dilatações. Em BK, a "regularização" \|X\| ≥ ℓ_x, \|P\| ≥ ℓ_p é contagem semiclássica de células, não domínio de operador (SIAM p. 260–261) |
| Auto-adjunticidade / espectro / contagem | A é auto-adjunto (Bellissard p. 2). **Espectro puramente absolutamente contínuo ℝ**, por derivação elementar (evidência E-K1-M2): conjugação unitária com −i d/du em L²(ℝ). BK p. 261: "motion generated by H = XP is unbounded, and so does not give discrete quantum energies… closing the phase space… is a central unsolved problem". Contagem semiclássica com corte: N̄ com 7/8 (p. 261, heurística) |
| Fórmula de traço | Nenhuma definida para o operador. Trajetórias X(t) = X(0)eᵗ, P(t) = P(0)e⁻ᵗ (p. 260, eq. 6.2): não há órbitas fechadas no plano clássico |
| Demonstrado | M1: S. M2: V (derivação elementar escrita) |
| Não especificado | Domínio ou regularização quântica concreta com espectro discreto; mecanismo para log p |
| Incompatibilidades | M2 (operador não regularizado). M4: **L**, não V, porque a ausência de órbitas periódicas clássicas não é, por si, teorema sobre uma fórmula de traço regularizada |
| Teste discriminante | Só após uma regularização concreta (operador + domínio), definida sem os zeros. Então cadeia m4-v3 sobre autovalores convergidos. Até lá, N1–N4: NA |

## K2 — Variantes de xp

### K2a — Berry & Keating 2011, H = (x + 1/x)(p + 1/p)

**Fonte:** J. Phys. A 44, 285203 (**lida em 17/09/2026**, versão publicada, SHA-256 `ed80fdfc…`).

| Campo | Conteúdo |
|---|---|
| Espaço / domínio / contorno | Semieixo x > 0; condição de contorno ∂ₓχ(0)/χ(0) = e^{iα}/η (eq. 2.22, p. 5), derivada como condição de hermiticidade para estados que decaem e "first guessed from numerical explorations"; os autores afirmam que cada α dá uma extensão auto-adjunta, sem prova de igualdade de domínios |
| Espectro / contagem | Discreto real (resumo). Com E = t/2π e η = 1/2π (eq. 5.3), os dois primeiros termos da contagem coincidem com os dos zeros (5.6–5.7, pp. 12–13); o termo 7/8 falta e a primeira correção da densidade tem sinal oposto → M3: **P** |
| Fórmula de traço | L |
| Demonstrado (com página) | Nada demonstrado no sentido de M1. M1: **P** (E-K2a-M1; rebaixado de S em 17/09/2026). M3 e N1: **P/conferido** (E-K2a-M3) |
| Não especificado | Relação dos autovalores individuais com os zeros; flutuações; dependência de α; estrutura das órbitas periódicas |
| Incompatibilidades | **Nenhuma registrada como V.** Os autores registram (§6, p. 13) que não afirmam conexão imediata com ζ: a densidade difere após os primeiros termos e há uma única órbita primitiva por energia, contra a família indexada por primos (enunciado clássico; M4 mantido L, como em K1). A exclusão 1D anterior foi retirada (auditoria, ponto 3): ser 1D não implica período dependente da energia, e mesmo com período variável a exclusão exige argumento para esta hamiltoniana |
| Teste discriminante | α fixado **a priori**. Predição congelada derivada da dinâmica clássica deste H (órbitas, períodos, amplitudes) **antes** de calcular autovalores. Depois, cadeia m4-v3 |

### K2b — Sierra 2008

**Fonte:** New J. Phys. 10, 033016; lida em arXiv:0712.0705v1.

| Campo | Conteúdo |
|---|---|
| Espaço / domínio / contorno | xp com termo de interação que depende de duas funções de onda de fronteira, associadas às fronteiras clássicas no espaço de fases (p. 1, resumo) |
| Espectro | Solução exata: contínuo sobre ℝ com estados ligados imersos nos zeros da função de Jost F(E) (p. 18). Com as funções de fronteira de BK, os zeros **médios** tornam-se assintoticamente estados ligados, "or more appropriately resonances" (p. 25) |
| Realização dos zeros | As funções de fronteira que dão os zeros exatos são obtidas **a partir da fórmula de Riemann–Siegel de ζ** (p. 1, p. 30–31). "Making some additional assumptions, we show that the Riemann zeros on the critical line are bound states… we cannot exclude the existence of zeros outside the critical line" (p. 4). Eq. 7.48 (p. 31): Z(t) = 2ρ(t)cos(πn(t)), com a ressalva de possíveis polos de ρ(t) |
| Fórmula de traço | L |
| Códigos | M1: **L**. O modelo usa ζ (Riemann–Siegel) na definição; falta um critério para "definido sem os zeros" quando a definição usa ζ. M2: **P** (suposições adicionais). M3: **P**. N1–N4: **L**, porque a tradução de estados ligados sob suposições para uma sequência testável não está feita |
| Incompatibilidades | Nenhuma registrada. **Correção:** o V anterior em M2 foi retirado |
| Teste discriminante | Especificar as funções de fronteira sem entrada de zeros e as suposições adicionais. Calcular estados ligados. Cadeia m4-v3. Registrar se a construção herda N1–N4 via ζ (não discriminante) |

### K2c — Sierra & Townsend 2008

**Fonte:** Phys. Rev. Lett. 101, 110201; lida em arXiv:0805.4079v2.

| Campo | Conteúdo |
|---|---|
| Espaço | Partícula carregada no plano, com potencial elétrico e campo magnético uniforme (p. 1) |
| Espectro | O modelo de "espectro de absorção" de Connes emerge no limite do nível de Landau mais baixo, contando estados "missing" de um contínuo (p. 1). Níveis superiores têm papel apenas **sugerido** em S(E) |
| Códigos | M3: P. Demais: L. N1–N4: L (objeto de absorção; plano §2.2) |
| Teste discriminante | Derivar a contribuição oscilatória dos níveis superiores antes de qualquer comparação |

### K2d — Bender, Brody & Müller 2017

**Fontes:** PRL 118, 130201 (arXiv:1608.03679v4); Bellissard, arXiv:1704.02644v1; réplica, arXiv:1705.06767v1.

| Campo | Conteúdo |
|---|---|
| Operador / contorno | Ĥ = (1 − e^{−ip̂})⁻¹(x̂p̂ + p̂x̂)(1 − e^{−ip̂}), com condição ψ(0) = 0. Se as autofunções satisfazem essa condição, {½(1 − iE_n)} são os zeros não triviais (BBM p. 1) |
| Auto-adjunticidade | "Ĥ is not Hermitian in the conventional sense"; iĤ tem simetria PT quebrada, "allowing for the possibility" de autovalores reais. A métrica que tornaria Ĥ hermitiano é tratada heuristicamente (BBM p. 1, resumo) |
| Crítica | Bellissard p. 2: em L²(0,∞), p̂ com ψ(0) = 0 tem índices de deficiência n₊ = 1, n₋ = 0, portanto nenhuma extensão auto-adjunta. ψ_z não é de quadrado integrável para Re z = ½ (a norma converge só para Re z > 3/2) |
| Réplica | p. 1–2: os autores não afirmam ter provado a realidade dos autovalores ("We are not able to prove that the eigenvalues of Ĥ are real"). Os fatos apontados já estavam no artigo. Os argumentos usam produto interno biortogonal/pseudo-hermitiano ainda não construído rigorosamente |
| Códigos | M1: **L**. O produto interno e o domínio não estão construídos; a crítica aponta obstáculos em L²(0,∞) e a réplica desloca o problema para outro produto interno. Contestação não é refutação demonstrada. Demais: L |
| Teste discriminante | Matemático: construir domínio e produto interno sem usar os zeros e verificar M1. Sem isso, não há teste numérico discriminante |

## K3 — Connes: espaço de classes de adeles

**Fonte:** Connes 1999, Selecta Math. (N.S.) 5, 29–106; lida em arXiv:math/9811068v1 (páginas arXiv).

**O objeto espectral não é um espectro de emissão.** Abstract e p. 2:
- "spectral interpretation of the critical zeros… as an absorption spectrum, while eventual noncritical zeros appear
  as resonances";
- "as missing spectral lines";
- os não críticos entram "through their harmonic potential with respect to the critical line".

### K3a — realização com parâmetro δ (Teorema 1, seção III)

| Campo | Conteúdo |
|---|---|
| Espaço | H: quociente de L²_δ(C_k) pela imagem de L²_δ(X)₀ (sequência exata (33), p. 15), com δ > 1 atuando como expoente de tipo Sobolev (p. 2). Setor H_χ por caractere χ de K (eq. 23, p. 13) |
| Operador | D_χ, gerador da ação de ℝ*₊ em H_χ (eq. 26, p. 13). A representação W **não é unitária** em geral: ‖W(g)‖ = O(log\|g\|)^{δ/2} (eq. 22, p. 13) |
| Espectro | **Teorema 1 (p. 13):** para δ > 1, D_χ tem espectro discreto, Sp D_χ ⊂ iℝ é o conjunto das partes imaginárias dos zeros de L(χ̃, ·) **com parte real ½**. A multiplicidade de ρ é o maior inteiro n < (1+δ)/2 com n ≤ multiplicidade do zero. Zeros não críticos **não aparecem** no espectro |
| Traço | Corolário 2 (p. 14): Trace W(h) = Σ ĥ(χ̃, ρ) sobre os zeros críticos, com a multiplicidade do Teorema 1. O lado geométrico vem de um cálculo **formal** (seção VI; p. 2) |
| Códigos | M1: **P**. O operador é definido sem L-funções (p. 14); a auto-adjunticidade de iD_χ não é afirmada e W não é unitária. M2: **C**. Para o δ fixado, só coincide com todos os zeros, com multiplicidades, se todos forem críticos (RH) **e** cada multiplicidade satisfizer m_ρ < (1+δ)/2. Um limite uniforme (p. 14: "one expects… this multiplicity is bounded") só permitiria escolher δ suficientemente grande. M4: **P** (lado geométrico formal). M6: **C**. N1–N4: **C**, condicionais a que os zeros 1–100.000 sejam críticos e de multiplicidade m_ρ < (1+δ)/2 para o δ fixado. A condição está **documentada** (E-K3a-N-ZEROS): van de Lune, te Riele & Winter 1986 (p. 667) verificam que os primeiros 1.500.000.001 zeros são críticos e simples, logo m_ρ = 1 < (1+δ)/2 para todo δ > 1; resta a correspondência índice da tabela ↔ zero (H-tab). Código mantido C. **Não discriminantes** |
| Tradução para N | Sequência −iSp D_χ ∩ (0, E], identificada com as ordenadas γ. Válida nas condições acima |

### K3b — formulação sem δ: absorção e fórmula de traço global (seções VII–VIII)

| Campo | Conteúdo |
|---|---|
| Espaço / regularização | L²(X), X = 𝔸/k*, com projeção de corte Q_Λ sobre funções f com f e f̂ nulas para \|x\| > Λ. Para a place arquimediana, via funções esferoidais prolatas de Landau–Pollak–Slepian (p. 46–47) |
| Objeto espectral | Espectro de **absorção**. No lema do caso de característica positiva (p. 45), todos os zeros aparecem com multiplicidade completa: os críticos "per se" e os não críticos "as resonances as in the Fermi theory" |
| Fórmula de traço | **Teorema 4 (p. 31):** fórmula de traço S-local provada, para conjunto finito S de places. **Teorema 5 (p. 42):** para **k de característica positiva**, equivalência entre a fórmula de traço global (a) e RH para todas as L-funções com Grössencharakter (b). Para k = ℚ, p. 45–47 descrevem a extensão ("This gives the analogue of Lemma 1, Theorem 5, and Lemma 3", p. 47). A introdução (p. 3) apresenta a equivalência como resultado principal; a forma exata do análogo para ℚ deve ser lida contra o texto publicado |
| Contagem | p. 47–48: cálculo semiclássico com H = qp e corte Λ. O termo ⟨N(E)⟩ aparece **com sinal negativo** em relação a 4E/2π log Λ, consistente com absorção |
| Códigos | M1: L. M2: **L**, pois não há sequência de emissão especificada. M3: P. M4: **C**, global ⇔ RH (Teorema 5 em característica positiva; análogo para ℚ). N1–N4: **L**, porque uma tradução do espectro de absorção para as restrições N não está especificada |
| Não especificado | Operador auto-adjunto com espectro de emissão igual aos zeros; enunciado e prova completos do análogo do Teorema 5 para ℚ na forma publicada |
| Teste discriminante | Não numérico nas escalas do projeto. Qualquer teste precisa primeiro definir a tradução absorção → observável |

## K4 — Espaços de de Branges e sistemas canônicos

**Fontes:**
- Lagarias 2006, *Frontiers I*, 365–377 (**preprint lido em 17/09/2026**, SHA-256 `5e0cef3b…`; versão publicada não comparada);
- Conrey & Li 2000, IMRN 2000(18), 929–940, lida em arXiv:math/9812166v1;
- de Branges 1968 (não lida).

| Campo | Conteúdo |
|---|---|
| Espaço | H(E): funções inteiras F com F/E de quadrado integrável na reta, E de Hermite–Biehler (\|E(z̄)\| < \|E(z)\| em Im z > 0) (Conrey–Li p. 1) |
| Resultado condicional | Lagarias, **Teorema 1 (p. 9)**: com E_χ(z) = ξ_χ(½ − iz) + ξ′_χ(½ − iz), (i) E_χ é função de de Branges **se e só se** RH vale para L(s, χ); (ii) é estrita **se e só se** RH vale e todos os zeros são simples. p. 7: a extensão auto-adjunta M_z(A) tem espectro puramente discreto e **simples** nos zeros de A(z) = ξ(½ − iz) cuja multiplicidade excede a de B(z). A construção parte de ξ, não de uma definição independente de ζ |
| Critério de positividade | Conrey–Li, Teorema 1 (p. 2, atribuído a de Branges). Hipóteses: E sem zeros reais, \|E(z̄)\| < \|E(z)\| em Im z > 0, Ē(z̄) = εE(z − i), \|E(x+iy)\| estritamente crescente em y > 0. Então Re⟨F(z), F(z+i)⟩ ≥ 0 implica zeros de E em Im z = −½ |
| Falha para ζ | Conrey–Li p. 6: H(E) com E(z) = ξ(1 − iz) **não** satisfaz a condição (3.1). p. 7: para W(z) = 1/ξ(1 − iz), a condição (3.3) do Teorema 2 falha, via o valor numérico Re{ξ(1+282i)/ξ(2+282i)} = −0,000131957 < 0 (calculado com Mathematica) |
| Códigos | M1, M2, M3, M6 e N1–N4: `situacao=C` (dependem de RH; M6 também de zeros simples, porque o espectro é simples), `conferencia=conferido` desde 17/09/2026 (E-K4-TEOR1; antes PC, só resumo). **Correção anterior:** eram S "por construção" |
| Não especificado | Construção independente de RH; fórmula de traço |
| Teste discriminante | Não numérico: a construção pressupõe RH |

## K5 — Laplaciano em superfícies hiperbólicas (Selberg)

**Fontes:**
- Marklof, arXiv:math/0407288 (lida; secundária rigorosa);
- Selberg 1956 (não lida);
- BGGS 1992 e BSS 1992 (resumos).

### K5a — superfície compacta

| Campo | Conteúdo |
|---|---|
| Espaço / operador | L²(Γ\ℍ²), M = Γ\ℍ² compacta; −Δ de Laplace–Beltrami |
| Espectro / contagem | Marklof p. 24: −Δ tem espectro discreto 0 = λ₀ < λ₁ ≤ … → ∞, com autofunções formando base ortonormal. λ_j = ¼ + ρ_j². **Lei de Weyl** (Prop. 10, p. 26): N(λ) ~ Area(M)λ/4π |
| Fórmula de traço | **Teorema 4 (p. 25):** Σ_j h(ρ_j) = (Area/4π)∫h(ρ)tanh(πρ)ρ dρ + Σ_{γ primitivas} Σ_{n≥1} ℓ_γ g(nℓ_γ)/(2 sinh(nℓ_γ/2)). Hipóteses (H1) analítica em \|Im ρ\| ≤ σ, σ > ½; (H2) par; (H3*) (p. 12). g(t) = (1/2π)∫h(ρ)e^{−iρt}dρ (eq. 69, p. 13). Coeficientes geométricos **positivos** |
| Comparação de amplitudes (corrigida) | Com ℓ_γ = log p (hipotético), ℓ_γ/(2 sinh(nℓ_γ/2)) = log p / (p^{n/2} − p^{−n/2}) = log p · p^{−n/2}/(1 − p^{−n}). O fator log p **está presente**. A frase anterior "sem o fator log p/π" estava errada. Diferenças em relação ao termo primo de §3.1 (−2Λ(n)n^{−1/2}g(log n)): **sinal**; fator 1/(1 − p^{−n}); fator numérico. As constantes de §3.1 dependem de L-EF1, logo a comparação quantitativa é **PC** |
| Demonstrado / derivado | M1: S (E-K5-M1). M3: **V derivada**, com escopo assintótico global, para identificação ρ_j = γ_j ou λ_j = γ_j; comparação de contagens, sem derivar (E-K5-M3). M2: V, que decorre de M3 sob a mesma identificação e com o mesmo escopo (E-K5-M2). M5: S (E-K5-M5) |
| N1 (revisão 11.3b-1) | **L desde 17/09/2026** (não decidível no nível da classe; [ETAPA11_PENDENCIAS_DERIVACAO.md](ETAPA11_PENDENCIAS_DERIVACAO.md) §5). Registro anterior: **PC.** A incompatibilidade assintótica não demonstra violação da tolerância de N1 (espaçamento médio 1,000 ± 0,0002 nas alturas 14–7,5·10⁴). O argumento anterior diferenciava uma equivalência assintótica de uma contagem em degraus, sem justificativa (E-K5-N1, retirada). Para decidir: estimativa com resto controlado na faixa ou experimento específico |
| Incompatibilidades pendentes | M4 e N3: **V/derivacao** desde 17/09/2026 (E-K5-M4-SINAL, E-K5-N3-SINAL; [ETAPA11_PENDENCIAS_DERIVACAO.md](ETAPA11_PENDENCIAS_DERIVACAO.md) §§3–4: massas pontuais de Weil negativas contra as de Selberg positivas; escopo: superfície compacta). N4: **P/conferido** desde 17/09/2026 (E-T6-ARIT: estatística tipo Poisson em superfícies aritméticas, heurística/numérica; não se aplica a superfície compacta não aritmética) |
| Não especificado | Superfície com comprimentos primitivos {log p}. Reparametrizações não afins γ = f(ρ) ficam fora de M (escolha livre, penalizada na Etapa 12) |
| Teste discriminante / controle aritmético | Plano §5, revisado. Predição congelada: lista de nℓ_γ no intervalo de t, amplitudes completas convertidas para a convenção de §3.2, tolerância e taxa de coincidências acidentais com r·log p na resolução FWHM = 4π/L. Avaliar contra a predição geométrica, **não** contra a ausência de linhas r·log p |

### K5b — caso cofinito (ex.: PSL(2,ℤ))

| Campo | Conteúdo |
|---|---|
| Espectro | Formas cuspidais (discreto), espectro contínuo e fase de espalhamento. Termos parabólicos e elípticos não cobertos pelo Teorema 4 de Marklof (p. 35–36) |
| Relação com ζ | Matriz de espalhamento φ(s) = ξ(2s−1)/ξ(2s) (Garrett, Obs. 11.1.5): os zeros de ζ aparecem como **ressonâncias** (polos de φ em s = ρ/2), não como autovalores |
| Códigos | Desde 17/09/2026 ([ETAPA11_K5B_ANALISE.md](ETAPA11_K5B_ANALISE.md)): M1 **S/conferido** (E-K5b-M1; Iwaniec p. 6, secundária); M2 **V/elementar** (E-K5b-M2; espectro contínuo [¼,∞), operador completo); M3 **V/derivacao** (E-K5b-M3; Weyl (vol/4π)T², escopo assintótico); M4 **P/conferido** (E-K5b-M4; estrutura parcial, igualdade não decidida). M5, M6, N1–N4: L. Papel útil: controle aritmético (11.6) |

## K6 — Sistemas hamiltonianos caóticos e fórmula de Gutzwiller

**Fontes:**
- Gutzwiller 1971 (não lida);
- Berry & Keating 1999, SIAM (lida, p. 241–243);
- BGS 1984 (resumo).

| Campo | Conteúdo |
|---|---|
| Espaço / operador | Hamiltoniano quântico cujo limite clássico é caótico |
| Fórmula de traço | Semiclássica, ħ → 0, **aproximada** (BK p. 241). A exceção exata é Selberg. Amplitude A_j ~ T_j/√\|det(M_j − I)\| (eq. 2.17, p. 243) |
| Discordâncias registradas pela fonte | BK p. 243: (i) no caso quântico o decaimento exponencial das órbitas longas **aproxima** o determinante, enquanto nos zeros o exponencial é **exato**; (ii) o **sinal negativo** exigiria fase de Maslov π para todas as órbitas, "hard to understand because if the index is π for a given orbit it should be 2π for the same orbit traversed twice". BK p. 260 remete uma explicação ao esquema de Connes |
| Códigos | M3: P. M4: **P** (analogia com discordâncias escritas). N3: P. N4: **C** (T5, conjectura BGS; GUE exige ausência de reversão temporal, BK p. 242). Demais: L |
| Teste discriminante | Para um sistema proposto independentemente: órbitas, períodos, amplitudes e Maslov calculados sem os zeros; predição congelada; cadeia m4-v3 sobre níveis convergidos |

## K7 — Bilhares quânticos (controle dinâmico)

**Fontes:** Balian–Bloch 1972, Ann. Phys. 69, 76–160 (registro confirmado pela lista de referências de BK SIAM, ref.
[20]; texto não lido); BGS 1984 (resumo); **Bäcker, arXiv:nlin/0204061, eqs. (48)–(49) (lida em 17/09/2026, secundária)**; **Ullmo, Scholarpedia 11(9):31721 (lida)**.

| Campo | Conteúdo |
|---|---|
| Operador | Laplaciano de Dirichlet ou Neumann em domínio plano limitado |
| Códigos | M1: **S/conferido** desde 17/09/2026 (E-K7-M1; Pankrashkin, notas 2020: Friedrichs = Dirichlet, resolvente compacto e espectro discreto em domínio limitado). M2, M3: **V/derivacao** (E-K7-M2, E-K7-M3; Weyl de bilhares N̄(E) ~ (A/4π)E contra (E/2π)log E; escopo assintótico). M4: V alegado, PC (comprimentos genéricos; Bogomolny & Schmit, nlin/0312057, mostram degenerescência também em modelos não aritméticos). N1: **L** desde 17/09/2026 (antes PC; não decidível no nível da classe, só para sistema concreto na 11.6). N2, N3: L. N4: **C/conferido** (E-T5-BGS; conjectura BGS, enunciado original GOE). M5: NA |
| Função | Controle de validação do instrumento, não candidato. Mesmo desenho do controle de Selberg revisado: prever comprimentos, amplitudes, tolerâncias e coincidências acidentais |

## K8 — Schrödinger 1D e potencial inverso (Wu–Sprung)

**Fonte:** Wu & Sprung 1993, PRE 48, 2595–2598 (**lida em 17/09/2026**, versão publicada, SHA-256 `7ccb97d2…`). Modelo 1D
de potencial local ajustado aos primeiros 500 zeros; dimensão fractal ≈ 1,5 (resumo, p. 2595).

| Campo | Conteúdo |
|---|---|
| Construção (p. 2596) | V₀ fixado para ajustar o primeiro zero; V(x) obtido minimizando F = Σ_n(e_n − E_n)² sobre os primeiros N zeros (eq. 9), com δF/δV = 2Σ(e_n − E_n)φ_n² (eq. 11), gradiente conjugado e Numerov; ajuste até N = 500, desvio médio < 4·10⁻⁶ |
| Códigos | M1: **V** (E-K8-M1): o potencial é função dos zeros por mínimos quadrados, logo não é definido sem usá-los. M2: P (ajuste aos primeiros 500 zeros; `conferencia` conferido). M4: **L**, com a exclusão 1D anterior retirada. **N1–N4: L**, com o S anterior retirado: a reprodução dos primeiros 500 níveis não garante N1–N4 nos 100.000 |
| Teste discriminante | Predição fora da amostra: um potencial construído com índices ≤ N prediz os níveis N+1…N+M sem reajuste. Etapa 12, com índices separados |

## K9 — Operadores pseudodiferenciais elípticos em variedades compactas

**Fontes:** Hörmander 1968, Acta Math. 121 (**lida em 17/09/2026**, SHA-256 `a633994c…`); Duistermaat & Guillemin 1975 (não lida; necessária só para M4).

| Campo | Conteúdo |
|---|---|
| Auto-adjunticidade | Hörmander p. 193: extensão de Friedrichs de operador elíptico formalmente positivo; p. 205: em variedade compacta, fecho auto-adjunto semilimitado de ΨDO elíptico de ordem 1, domínio H(1) |
| Lei de Weyl com resto | Teorema 5.1, eq. (5.3), p. 215: \|e(x,x,λ) − (2π)^{−n}∫_{p(x,ξ)<λ}dξ\| ≤ C(1+\|λ\|)^{(n−1)/m}; integrando em Ω compacta, N(λ) = cλ^{n/m} + O(λ^{(n−1)/m}) |
| Códigos | M1: **S/conferido** (E-K9-M1). M2, M3: **V/derivacao** (E-K9-M2, E-K9-M3): contagem polinomial cλ^{n/m} contra (E/2π)log E, sob identificações afins; escopo assintótico. N1: **L** desde 17/09/2026 (antes PC; mesma análise de K5a). M4: L (fórmula de traço de Duistermaat–Guillemin não lida). M5: NA |
| Teste discriminante | Analítico, após conferência de 11.3b |

## K10 — Operadores integrais (classe ampla)

Todos os campos **L**. Não é candidato concreto.

## K11 — Modelos estatísticos (não operadores)

Montgomery 1973; Rudnick–Sarnak 1996; Keating–Snaith 2000; Katz–Sarnak 1999.
- M1–M6 e N1–N4: **NA**. Esses modelos não definem um operador cujo espectro seja o dos zeros.
- N4 é restrição ao procedimento de comparação e não refuta a universalidade GUE assintótica (T3).

## K12 — Controle de ajuste: H = diag(γ₁, …, γ_N)

| Campo | Conteúdo |
|---|---|
| Códigos | M1: V (E-K12-M1). M2, M3, M4: V para N finito (E-K12-M2/M3/M4). M5: S (restrição explícita a γ > 0, por definição). M6: L. N1–N4: **S apenas com N ≥ 100.000 níveis inseridos com a precisão do dado** (E-K12-N) |
| Função | Controle negativo. Poder preditivo nulo fora dos níveis inseridos |

---

## Síntese transversal (sem ordenação de candidatos)

- **Nenhuma entrada S/V de M1 + M2** mostra uma classe que satisfaça ambas de forma demonstrada e independente de RH.
  Isso é um registro de ausência, não uma ordenação. **A matriz não define critério de proximidade** a uma
  identificação completa, e nenhuma classe é ranqueada.
- **Construções condicionais ou com objeto espectral distinto:** K3a é C, condicional a RH e à multiplicidade; K3b
  é absorção, com N em L; K4 é C.
- **Incompatibilidades com argumento escrito:**
  - K1: espectro contínuo do gerador de dilatações;
  - K5a: lei de Weyl de superfície compacta contra a contagem de Riemann–von Mangoldt, para identificações afins
    (escopo **assintótico global**; N1 na faixa finita permanece PC);
  - K12: finitude e definição a partir dos zeros.
- **Retiradas nesta revisão:**
  - exclusões 1D (K2a, K8);
  - M2 de Sierra;
  - M4 de K1;
  - S "por construção" de K4 e K8;
  - V em N1 de K5a (revisão 11.3b-1).
- **Pendentes:** §0.3.
