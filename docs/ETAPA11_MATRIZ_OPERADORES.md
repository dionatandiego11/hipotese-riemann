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

Não obtidas:
- Berry & Keating 2011 (só o resumo);
- Lagarias 2006 (só o resumo; a busca devolveu um identificador arXiv incorreto, math/0010324, que é outro artigo);
- Wu & Sprung 1993 (resumo por descrições secundárias);
- Duistermaat & Guillemin 1975;
- Hörmander 1968;
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
| Condicionalidade × conferência | O CSV separa `situacao` (S, V, C, P, L, PC, NA) de `conferencia` (conferido, derivacao, elementar, PC, NA). Exemplos: K4 fica `situacao=C`, `conferencia=PC` (resumo de Lagarias); K3a N1–N4 fica `C/PC` (citação da verificação dos zeros pendente). `sustenta_decisao = sim` só para S/V com conferência concluída ou derivação escrita (15 entradas) |
| Arquivo das fontes | Cópias exatas em `archive/fontes_etapa11/`, com `MANIFESTO.csv` (versão, URL, data e hora do download, SHA-256, correspondência de páginas) e `README.md`. As páginas citadas referem-se a esses arquivos. Novos downloads só valem como idênticos após comparar o SHA-256 |
| Connes, característica positiva | Registrada como **correção bibliográfica do projeto**, sem classificação de novidade (§0.1) |

### 0.3 Entradas PC e pendências (11.3b)

1. **K2a, M1:** auto-adjunticidade das extensões, com página em BK 2011 (texto integral).
2. **K5, M4 e N3:** incompatibilidade de sinal e normalização entre Selberg e Weil. Depende de L-EF1 (constantes da
   fórmula explícita na convenção de §3.1).
3. **K5, N4:** estatística das superfícies aritméticas, com página em BGGS 1992, BSS 1992 ou Bogomolny et al.,
   Phys. Rep. 291 (1997).
4. **K5b:** caso cofinito e PSL(2,ℤ). Lei de Weyl para formas cuspidais e matriz de espalhamento com ξ (Hejhal ou
   Iwaniec).
5. **K7, M1–M4 e N1:** lei de Weyl para domínios limitados e auto-adjunticidade do laplaciano de Dirichlet, com fonte e
   hipóteses sobre a fronteira.
6. **K8, M1:** o método de Wu–Sprung usa os zeros? Conferir no texto integral.
7. **K9, M1–M3 e N1:** lei de Weyl de Hörmander e hipóteses de Duistermaat–Guillemin.
7a. **K5a, K7, K9, N1:** para V seria necessária estimativa quantitativa com erro controlado na faixa de alturas do
   projeto (por exemplo, lei de Weyl com resto explícito para o sistema concreto) ou experimento específico. A diferença
   assintótica de contagens não basta.
7b. **K4:** obter o texto de Lagarias (2006) para conferir o enunciado condicional (`conferencia`).
8. **K3a, N1–N4:** citar o resultado de verificação computacional de que os zeros 1–100.000 são críticos e simples.
   Sem essa citação, a condição de C não está documentada.
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
11. **C11/C19:** fontes (Milne, Deligne) inacessíveis nesta sessão (conexão recusada); convenção de Frobenius PC.

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

**Fonte:** J. Phys. A 44, 285203 (**resumo**; texto integral não lido).

| Campo | Conteúdo |
|---|---|
| Espaço / domínio / contorno | Semieixo x > 0; família de extensões auto-adjuntas rotuladas por um ângulo α na origem (resumo) |
| Espectro / contagem | Discreto real; os dois primeiros termos da densidade assintótica coincidem com os dos zeros (resumo) → M3: **P** |
| Fórmula de traço | L |
| Demonstrado (com página) | Nada conferido. M1: **PC** |
| Não especificado | Relação dos autovalores individuais com os zeros; flutuações; dependência de α; estrutura das órbitas periódicas |
| Incompatibilidades | **Nenhuma registrada.** A exclusão 1D anterior foi retirada (auditoria, ponto 3): ser 1D não implica período dependente da energia, e mesmo com período variável a exclusão exige argumento para esta hamiltoniana |
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
| Códigos | M1: **P**. O operador é definido sem L-funções (p. 14); a auto-adjunticidade de iD_χ não é afirmada e W não é unitária. M2: **C**. Para o δ fixado, só coincide com todos os zeros, com multiplicidades, se todos forem críticos (RH) **e** cada multiplicidade satisfizer m_ρ < (1+δ)/2. Um limite uniforme (p. 14: "one expects… this multiplicity is bounded") só permitiria escolher δ suficientemente grande. M4: **P** (lado geométrico formal). M6: **C**. N1–N4: **C**, condicionais a que os zeros 1–100.000 sejam críticos e de multiplicidade m_ρ < (1+δ)/2 para o δ fixado (citação da verificação pendente, §0.3 item 8). **Não discriminantes** |
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
- Lagarias 2006, *Frontiers I*, 365–377 (**resumo**);
- Conrey & Li 2000, IMRN 2000(18), 929–940, lida em arXiv:math/9812166v1;
- de Branges 1968 (não lida).

| Campo | Conteúdo |
|---|---|
| Espaço | H(E): funções inteiras F com F/E de quadrado integrável na reta, E de Hermite–Biehler (\|E(z̄)\| < \|E(z)\| em Im z > 0) (Conrey–Li p. 1) |
| Resultado condicional | Lagarias (resumo): **assumindo RH** para L, existe espaço de de Branges com operador auto-adjunto cujos autovalores são as ordenadas dos zeros críticos |
| Critério de positividade | Conrey–Li, Teorema 1 (p. 2, atribuído a de Branges). Hipóteses: E sem zeros reais, \|E(z̄)\| < \|E(z)\| em Im z > 0, Ē(z̄) = εE(z − i), \|E(x+iy)\| estritamente crescente em y > 0. Então Re⟨F(z), F(z+i)⟩ ≥ 0 implica zeros de E em Im z = −½ |
| Falha para ζ | Conrey–Li p. 6: H(E) com E(z) = ξ(1 − iz) **não** satisfaz a condição (3.1). p. 7: para W(z) = 1/ξ(1 − iz), a condição (3.3) do Teorema 2 falha, via o valor numérico Re{ξ(1+282i)/ξ(2+282i)} = −0,000131957 < 0 (calculado com Mathematica) |
| Códigos | M1, M2, M3, M6 e N1–N4: `situacao=C` (dependem de RH), `conferencia=PC` (só o resumo de Lagarias foi lido; enunciado e página não conferidos). As duas informações são distintas. **Correção:** eram S "por construção" |
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
| N1 (revisão 11.3b-1) | **PC.** A incompatibilidade assintótica não demonstra violação da tolerância de N1 (espaçamento médio 1,000 ± 0,0002 nas alturas 14–7,5·10⁴). O argumento anterior diferenciava uma equivalência assintótica de uma contagem em degraus, sem justificativa (E-K5-N1, retirada). Para decidir: estimativa com resto controlado na faixa ou experimento específico |
| Incompatibilidades pendentes | M4 e N3 (sinal e normalização): **PC** até L-EF1. N4: **PC** (T6; página não conferida) |
| Não especificado | Superfície com comprimentos primitivos {log p}. Reparametrizações não afins γ = f(ρ) ficam fora de M (escolha livre, penalizada na Etapa 12) |
| Teste discriminante / controle aritmético | Plano §5, revisado. Predição congelada: lista de nℓ_γ no intervalo de t, amplitudes completas convertidas para a convenção de §3.2, tolerância e taxa de coincidências acidentais com r·log p na resolução FWHM = 4π/L. Avaliar contra a predição geométrica, **não** contra a ausência de linhas r·log p |

### K5b — caso cofinito (ex.: PSL(2,ℤ))

| Campo | Conteúdo |
|---|---|
| Espectro | Formas cuspidais (discreto), espectro contínuo e fase de espalhamento. Termos parabólicos e elípticos não cobertos pelo Teorema 4 de Marklof (p. 35–36) |
| Relação com ζ | Matriz de espalhamento de PSL(2,ℤ) com razão de ξ: **PC** (Hejhal/Iwaniec) |
| Códigos | M1–M4: PC ou L; N: L |

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
[20]; texto não lido); BGS 1984 (resumo).

| Campo | Conteúdo |
|---|---|
| Operador | Laplaciano de Dirichlet ou Neumann em domínio plano limitado |
| Códigos | M1 (S alegado), M2–M4 (V alegado): `conferencia=PC`. Lei de Weyl e auto-adjunticidade são padrão, mas sem página e hipóteses sobre a fronteira conferidas. Escopo de M2/M3: assintótico. N1: `situacao=PC`, pois a diferença assintótica não implica violação na faixa finita. N2, N3: L. N4: C/PC (T5). M5: NA |
| Função | Controle de validação do instrumento, não candidato. Mesmo desenho do controle de Selberg revisado: prever comprimentos, amplitudes, tolerâncias e coincidências acidentais |

## K8 — Schrödinger 1D e potencial inverso (Wu–Sprung)

**Fonte:** Wu & Sprung 1993, PRE 48, 2595 (texto integral não lido). Descrição por fontes secundárias: modelo 1D de
potencial local que reproduz os primeiros 500 zeros; dimensão fractal ≈ 1,5.

| Campo | Conteúdo |
|---|---|
| Códigos | M1: **PC**, pois se a construção usa os zeros como entrada o código seria V; conferir no texto. M2: P (primeiros 500 zeros, com precisão a conferir). M4: **L**, com a exclusão 1D anterior retirada. **N1–N4: L**, com o S anterior retirado: a reprodução dos primeiros 500 níveis não garante N1–N4 nos 100.000 |
| Teste discriminante | Predição fora da amostra: um potencial construído com índices ≤ N prediz os níveis N+1…N+M sem reajuste. Etapa 12, com índices separados |

## K9 — Operadores pseudodiferenciais elípticos em variedades compactas

**Fontes:** Duistermaat & Guillemin 1975; Hörmander 1968 (não lidas).

| Campo | Conteúdo |
|---|---|
| Códigos | M1 (S alegado), M2, M3 (V alegado, escopo assintótico): `conferencia=PC`. O argumento "Weyl polinomial × E log E" é plausível, mas a lei de Weyl com hipóteses não foi conferida em página. N1: `situacao=PC` (mesma distinção de K5a). M4: L. M5: NA |
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
