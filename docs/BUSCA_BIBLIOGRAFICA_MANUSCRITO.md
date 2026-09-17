# Busca bibliográfica preliminar para o manuscrito (17/09/2026)

**Objetivo.** Preencher a Seção 1.2 (trabalhos relacionados) do rascunho local `paper/manuscript.tex` só com fontes cujos
dados foram conferidos, e procurar ativamente trabalhos próximos antes de qualquer formulação de lacuna.

**Natureza e limites:**
- busca **preliminar**, feita em uma sessão, com ferramenta de busca na web e leitura de páginas de resumo do arXiv;
- **não é exaustiva**: sem MathSciNet/zbMATH, sem busca por citações, sem leitura integral dos textos (exceção parcial:
  Büthe, abaixo);
- **não autoriza** afirmação de novidade ou de prioridade. O manuscrito não faz nenhuma.

## 1. Níveis de conferência usados

| Nível | Significado |
|---|---|
| **L** (lido) | texto ou trechos lidos na fonte primária; trechos indicados |
| **R** (resumo) | página de resumo da fonte primária (arXiv) lida; texto não lido |
| **M** (metadados) | autores, título, revista, volume, páginas e ano vistos em resultado de busca que aponta para a página do editor ou indexador; nem resumo nem texto lidos |

Uma referência de nível M só pode sustentar, no manuscrito, a atribuição de um resultado amplamente conhecido e
descrito de forma genérica. Nenhuma afirmação sobre o **conteúdo detalhado** é feita com base em M.

## 2. Consultas feitas

1. Büthe, método analítico para ψ(x); 2. Platt, π(x) analítico; 3. Platt–Trudgian, RH até 3·10¹²;
4. transformada de Fourier dos zeros e picos em log p; 5. Guinand 1948; 6. Weil 1952; 7. Odlyzko 1987;
8. Bogomolny–Keating 1996; 9. primos a partir de zeros com cotas de erro rigorosas; 10. Tucker 2002; 11. Booker 2006;
12. Berry 1986; 13. "espectroscopia" dos zeros e órbitas periódicas; 14. reconstrução de primos por ajuste;
15. Büthe 2016; 16. Gonek 1993; 17. Cramér 1919; 18. Landau 1912; 19. Arb; 20. testes numéricos com tabelas de Odlyzko.

## 3. Fontes registradas

### 3.1 Fórmula explícita e fórmulas de Landau

| Referência | Dados | Nível | Uso possível |
|---|---|---|---|
| Guinand, *A summation formula in the theory of prime numbers* | Proc. London Math. Soc. (2) 50 (1948), 107–119; doi:10.1112/plms/s2-50.2.107 | M | atribuição histórica da fórmula de somação |
| Weil, *Sur les « formules explicites » de la théorie des nombres premiers* | Comm. Sém. Math. Univ. Lund (vol. dédié à M. Riesz) (1952), 252–265 | M | atribuição histórica; **F5 continua pendente** (enunciado não conferido) |
| Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* | arXiv:math/9811068v1; Selecta Math. 5 (1999) 29–106 (paginação publicada não conferida) | L (já arquivado) | ponto de partida da classe 𝒜 |
| Landau, *Über die Nullstellen der Zetafunktion* | Math. Ann. 71 (1912), 548–564; doi:10.1007/BF01456808 | M | fórmula de Landau (soma de x^ρ) |
| Cramér, *Studien über die Nullstellen der Riemannschen Zetafunktion* | Math. Z. 4 (1919), 104–130; doi:10.1007/BF01203390 | M | somas sobre zeros (atribuição genérica) |
| Gonek, *An explicit formula of Landau and its applications to the theory of the zeta-function* | Contemp. Math. 143 (1993), 395–413 | M (já F9) | versão uniforme da fórmula de Landau |
| Balanzario, Cárdenas Romero, Chacón Serna, *A smooth version of Landau's explicit formula* | arXiv:2311.04347v1 (07/11/2023) | R | **próximo**: sob RH, primalidade a partir de um número finito de zeros; resumo não menciona cotas numéricas certificadas |
| Balanzario, Cárdenas Romero, *An explicit formula for the zeros of the Riemann zeta function* | arXiv:2312.00108 (30/11/2023) | R | direção inversa (primos → zeros) |

### 3.2 Caos quântico, estatística e dados

| Referência | Dados | Nível | Uso possível |
|---|---|---|---|
| Berry, *Riemann's zeta function: a model for quantum chaos?* | Lecture Notes in Phys. 263 (1986), 1–17; doi:10.1007/3-540-17171-1_1 | M | analogia fórmula de traço / órbitas com períodos log p |
| Berry, Keating, *The Riemann zeros and eigenvalue asymptotics* | SIAM Rev. 41(2) (1999), 236–266 | L (cópia consultada no projeto) | idem, com a densidade oscilatória |
| Berry, Keating, *H = xp and the Riemann zeros* | em *Supersymmetry and Trace Formulae: Chaos and Disorder* (Plenum, 1999) | M | só menção; páginas não conferidas |
| Bogomolny, Keating, *Gutzwiller's trace formula and spectral statistics: beyond the diagonal approximation* | Phys. Rev. Lett. 77 (1996), 1472 | M | estatística espectral (correlações), não recuperação de log p |
| Odlyzko, *On the distribution of spacings between zeros of the zeta function* | Math. Comp. 48 (1987), 273–308 | M | cálculo de zeros e comparação com GUE |
| Odlyzko, tabela `zeros1` | página do autor | L (dados usados) | dados |
| Mazur, Stein, *Prime Numbers and the Riemann Hypothesis* | Cambridge Univ. Press, 2016 | M | exposição do "espectro de Riemann" dos primos |
| Csoka, *The Fourier transform of the non-trivial zeros of the zeta function* | arXiv:1712.08434v1 (math.GM) | R | exploração numérica sem cotas; não recomendada como referência central |
| Csoka, *Detection and discrimination of the periodicity of prime numbers by discrete Fourier transform* | arXiv:1501.06939v1 (math.GM) | R | idem |
| Ionescu, *On Prime Numbers and The Riemann Zeros* | arXiv:2204.00899 | R | exploratório; não recomendada |

### 3.3 Cálculos rigorosos e provas assistidas por computador

| Referência | Dados | Nível | Uso possível |
|---|---|---|---|
| Büthe, *An analytic method for bounding ψ(x)* | arXiv:1511.02032v2 (22/10/2017); Math. Comp. 87 (2018), 1991–2009 | **L parcial** (§3 início, §6); PDF arquivado localmente, SHA-256 `350f9631…` | **o mais próximo encontrado**: usa fórmula explícita com soma sobre zeros até altura T para cotas de ψ(t), com erro controlado; §6 relata MPFR, aritmética de ponto fixo de 64 bits e cota separada dos erros de arredondamento (referida à tese [1] do autor, não lida) |
| Büthe, *Estimating π(x) and related functions under partial RH assumptions* | arXiv:1410.7015; Math. Comp. 85 (2016), 2483–2498 | M | cálculo analítico sob RH parcial |
| Platt, *Computing π(x) analytically* | arXiv:1203.5712v3; Math. Comp. 84 (2015), 1521–1535 | R | "rigorous implementation" do método de Lagarias–Odlyzko; aritmética intervalar (segundo resultado de busca; resumo não a cita) |
| Platt, Trudgian, *The Riemann hypothesis is true up to 3·10¹²* | arXiv:2004.09765; Bull. London Math. Soc. 53(3) (2021), 792–797 | R | verificação rigorosa com aritmética intervalar |
| Booker, *Artin's conjecture, Turing's method, and the Riemann hypothesis* | Experiment. Math. 15(4) (2006), 385–407 | M | método de Turing rigoroso para funções L |
| Tucker, *A rigorous ODE solver and Smale's 14th problem* | Found. Comput. Math. 2(1) (2002), 53–117; doi:10.1007/s002080010018 | M | referência clássica de prova assistida por aritmética intervalar |
| Johansson, *Arb: efficient arbitrary-precision midpoint-radius interval arithmetic* | arXiv:1611.02831 (cs.MS) | R | biblioteca de referência (não usada no projeto) |

## 4. Leitura preliminar (sem afirmação de novidade)

1. **A combinação "fórmula explícita + soma sobre zeros tabulados + controle rigoroso de erro" já existe** (Büthe 2018;
   em outra direção, Platt 2015). A lacuna, se houver, **não** pode ser formulada como "primeira certificação da
   fórmula explícita" nem como "primeira prova assistida em espectroscopia de zeros".
2. **Recuperação de primos a partir de zeros sob RH** também já é estudada (Landau; Gonek; Balanzario et al. 2023).
3. O que o projeto faz de **específico** é mais estreito: certificar, para um **estimador estatístico congelado**
   (ajuste por mínimos quadrados de coeficientes de linhas em janela de Hann, com seleção por elegibilidade) e para dados
   tabulados concretos, (N) a fidelidade numérica do valor registrado e (T) uma cota condicional do desvio relativo à
   previsão. **Não se sabe** se isso já foi feito; a busca não encontrou, o que não prova ausência.
4. Formulação permitida no manuscrito: descrever o escopo e dizer que a busca foi preliminar; **não** dizer "primeiro".

## 5. Pendências

- Leitura integral de Büthe 2018 (inclusive a tese citada para os erros de arredondamento) e de Balanzario et al. 2023.
- Busca em MathSciNet/zbMATH e por citações de Büthe 2018 e de Gonek 1993.
- Conferir no editor os dados de nível M antes de qualquer submissão.
- F5 (Weil) e J1 (Jensen) continuam pendências bibliográficas do certificado.

## 6. Conferências adicionais (17/09/2026, segunda rodada)

Motivo: textos e referências propostos para os TODOs do manuscrito. Cada item foi conferido antes de entrar.

| Item proposto | Conferência | Resultado | Entrou no manuscrito |
|---|---|---|---|
| Balanzario, Cárdenas-Romero, Chacón-Serna, IJNT 21 (2025) no. 1, 177–192 | API do Crossref (`api.crossref.org/works`, consulta bibliográfica) | **confere**: autores, volume 21, número 01, páginas 177–192, fevereiro de 2025 (online 26/08/2024), doi:10.1142/S1793042125500095 | sim (texto continua não lido) |
| Büthe, Math. Comp. 87 (2018) no. 312 | resultado de busca anterior (número 312) | confere no nível M | sim |
| **J1:** Titchmarsh, *The Theory of Functions*, 2.ª ed., 1939, §3.61, pp. 125–126 | texto OCR do exemplar digitalizado do Internet Archive (`in.ernet.dli.2015.2588`, arquivo `2015.2588.The-Theory-Of-Functions_djvu.txt`, SHA-256 `dc00331963a4c887…`); página de rosto "SECOND EDITION 1939" | **confere**: "3.61. Jensen's theorem" começa na p. 125; a forma com n(x) está na p. 126. A desigualdade n(r)log(R/r) ≤ log(M_R/\|f(s₀)\|) usada em Z1 segue imediatamente (n crescente; translação s₀) | sim. **J1 passa de pendência a fonte lida (nível L)**; o OCR **não** foi arquivado no repositório (direitos), só URL e hash |
| Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (Heath-Brown, 1986), §9.2, pp. 211–214, "discos de centro 2 + iT e raio 3" | busca: só a 1.ª edição de 1930 (outro livro) está no Internet Archive; nenhuma cópia acessível da 2.ª ed. | **não conferido**. Além disso, os discos de Z1 (R = 3, r = 9/4) foram escolhidos neste projeto; a afirmação "exatamente como usamos" não pode ser feita sem leitura | **não** |
| Weil 1952, reimpresso em *Oeuvres Scientifiques*, vol. II, Springer, 1979, pp. 48–61 | resultado de busca que reproduz citação secundária ("Oeuvres Sci., II, 48–61") | nível M (secundário) | sim, marcado; **F5 continua pendente** (texto não lido) |
| Texto proposto para a "tradução de Connes" | PDF arquivado de Connes (`dfd4e992…`), Apêndice II, extraído com `pdftotext` | **parcialmente correto**: Teorema 1 na p. 70, eqs. (5)–(11) nas pp. 68–70, Lema 3 na p. 76 e Teorema 6 nas pp. 77–78 conferem. **Não conferem**: (i) eqs. (8)–(9) **definem** D_v e o Pfw local; a fórmula D_p = 2 log p Σ p^{−m/2} g(m log p) é **derivação do projeto** (ETAPA11_3B_FORMULA_EXPLICITA §1.2); (ii) ψ(eˣ) = ¼ g(x)K(x) e D_∞ = g(0) log π − T[g] são **derivações do projeto** (ETAPA11_3B_TERMO_ARQUIMEDIANO §§2–4), não equações de Connes; (iii) a eq. (31) do Apêndice II é o **valor particular** Pfw∫f₀³ = log π + γ, não a fórmula geral de D_∞ | sim, **reescrito** com a atribuição corrigida: Connes para o enunciado; o projeto para os termos locais; (31) só como checagem numérica |
| Extensão prevista "15 a 16 páginas" | sem compilação | **não verificável** | não |
