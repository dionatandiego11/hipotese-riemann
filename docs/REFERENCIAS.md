# Referências bibliográficas e fundamentação teórica

Este documento registra as referências primárias que fundamentam o protocolo, os algoritmos e a interpretação dos resultados do projeto de espectroscopia inversa dos zeros da função zeta de Riemann.

## 1. Dados e cálculos dos zeros

- **Odlyzko, A. M.** *Tables of zeros of the Riemann zeta function*.
  URL: <https://www-users.cse.umn.edu/~odlyzko/zeta_tables/>
  Tabelas de alta precisão dos primeiros 100.000 zeros não triviais e de zeros em grandes alturas. Declara precisão de até $3 \times 10^{-9}$ nas ordenadas publicadas.

- **mpmath development team.** *mpmath: Python library for arbitrary-precision floating-point arithmetic (version 1.3+)*.
  Documentação: <https://mpmath.org/doc/current/functions/zeta.html#zetazero>
  Utilizado para validação independente de alta precisão (40 dígitos decimais de trabalho) de amostras determinísticas estratificadas de zeros.

- **NIST Digital Library of Mathematical Functions (DLMF).** *Chapter 25: Zeta and Related Functions*.
  URL: <https://dlmf.nist.gov/25.10>
  Fórmula de Riemann–von Mangoldt para $N(T)$, função $Z(t)$ e fase suave de Riemann–Siegel $\theta(t)$.

## 2. Estatística espectral e Teoria de Matrizes Aleatórias (RMT)

- **Montgomery, H. L. (1973).** *The pair correlation of zeros of the zeta function*. Analytic number theory (Proc. Sympos. Pure Math., Vol. XXIV, St. Louis Univ., St. Louis, Mo., 1972), pp. 181–193. Amer. Math. Soc., Providence, R.I.
  Formulação original da função de correlação de pares $R_2(s) = 1 - \left(\frac{\sin \pi s}{\pi s}\right)^2$ sob a Hipótese de Riemann para funções de teste com suporte de Fourier restrito $|\alpha| < 1$.

- **Dyson, F. J. (1962).** *Statistical theory of the energy levels of complex systems. I, II, III*. Journal of Mathematical Physics, 3(1), 140–175.
  Definição e propriedades do Gaussian Unitary Ensemble (GUE) e correlação de pares.

- **Dumitriu, I., & Edelman, A. (2002).** *Matrix models for beta ensembles*. Journal of Mathematical Physics, 43(11), 5830–5847. arXiv:math-ph/0206043.
  Representação tridiagonal para ensembles $\beta$, permitindo amostragem rápida e exata de autovalores de GUE ($\beta = 2$) sem diagonalização densa $\mathcal{O}(N^3)$.

- **Mehta, M. L. (2004).** *Random Matrices*. 3rd Edition, Pure and Applied Mathematics, Academic Press.
  Distribuições de espaçamentos, funções de correlação e spectral form factor para matrizes aleatórias gaussianas.

## 3. Caos quântico e analogias espectrais

- **Berry, M. V., & Keating, J. P. (1999).** *The Riemann zeros and eigenvalue asymptotics*. SIAM Review, 41(2), 236–266.
  Discussão exaustiva das correspondências e divergências entre a fórmula explícita de Riemann–von Mangoldt e a fórmula de traço de Gutzwiller para sistemas caóticos quânticos.

- **Berry, M. V., & Keating, J. P. (1999).** *$H = xp$ and the Riemann zeros*. In: Supersymmetry and Trace Formulae: Chaos and Disorder, pp. 355–367. Springer US.
  Proposta clássica e quantização do operador $H = \frac{1}{2}(xp + px)$, identificação das condições de contorno e dificuldades analíticas para obter espectro discreto.

- **Gutzwiller, M. C. (1990).** *Chaos in Classical and Quantum Mechanics*. Springer-Verlag New York.
  Dedução e propriedades da fórmula de traço semiclássica que conecta a densidade oscilatória de estados com a soma sobre órbitas periódicas clássicas.

- **Main, J., Mandelshtam, V. A., Wunner, G., & Taylor, H. S. (1997).** *Harmonic inversion as a general method for periodic orbit quantization*. Physical Review E, 55(4), 5157. arXiv:chao-dyn/9709009.
  Uso de inversão harmônica e métodos de subespaço para extrair períodos e amplitudes de espectros discretos.

## 4. Referências acrescentadas na revisão de 13/09/2026

Estado de verificação indicado em cada item. "Registro verificado" significa que título, autores e local foram
conferidos numa busca; não significa leitura integral.

- **Bogomolny, E., Bohigas, O., Leboeuf, P., & Monastra, A. G. (2006).** *On the spacing distribution of the Riemann
  zeros: corrections to the asymptotic result*. J. Phys. A 39, 10743–10754. arXiv:math/0602270.
  <https://arxiv.org/abs/math/0602270> — registro verificado. Em ordem dominante, os desvios de espaçamento em altura
  finita são os de matrizes unitárias de dimensão efetiva N_eff = ln(E/2π)/√(12Λ), Λ = 1,57314…
  **Correção (auditoria de 13/09/2026):** a construção de tamanho finito do artigo (§2) usa **CUE** e distingue sua
  expansão da do GUE. Não basta trocar a dimensão de matrizes GUE por N_eff. Nos centros das janelas atuais,
  N_eff ≈ 1,5–1,7, o que exige cautela com expansões de grande dimensão. Nenhuma comparação quantitativa foi
  executada; o artigo oferece argumentos assintóticos, não uma causa demonstrada dos desvios medidos.

- **Greengard, L., & Lee, J.-Y. (2004).** *Accelerating the nonuniform fast Fourier transform*. SIAM Review 46(3),
  443–454. — registro a verificar. O algoritmo implementado é validado numericamente contra soma direta em cada
  execução, independentemente da referência.

- **Harris, F. J. (1978).** *On the use of windows for harmonic analysis with the discrete Fourier transform*.
  Proc. IEEE 66(1), 51–83. — registro a verificar. Coeficientes da janela Blackman–Harris de 4 termos. A resposta
  (primeiro zero em v = 4, lóbulo lateral ≈ −92 dB) é conferida numericamente nos testes.

- **Selberg, A. — distribuição de S(t).** — registro e hipóteses a verificar. **Correção:** a interpretação do pico de
  K_c em τ = 1 pela pequena variância de N̄(γₙ) − (n − ½) é **heurística**. A variância não determina a função
  característica numa frequência fixa, e o enquadramento usual (t amostrado num intervalo) não se transfere
  automaticamente para amostragem nos zeros. Enquadramento em Lugar, Milinovich & Quesada-Herrera, *Mathematika*,
  §1.1: <https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/mtk.12184> (indicado pela auditoria; não lido
  integralmente nesta sessão).

- **Fórmula explícita de Guinand–Weil.** A classe de funções-teste, os termos (incluindo contribuições suaves e de
  borda) e os erros que justificariam identificar exatamente a observável finita com janela Hann não foram
  estabelecidos. A concordância medida é classificada como **B**. Uma classificação **A** exigirá enunciado preciso
  com hipóteses e fonte primária (Etapa 13).

## 5. Referências da Etapa 11 (matriz de classes de operadores, 14/09/2026)

Detalhes, hipóteses e uso por classe em [ETAPA11_MATRIZ_OPERADORES.md](ETAPA11_MATRIZ_OPERADORES.md). "Registro
verificado" = título, autores e local conferidos por busca; não significa leitura integral.

- **Berry, M. V., & Keating, J. P. (2011).** *A compact hamiltonian with the same asymptotic mean spectral density as
  the Riemann zeros*. J. Phys. A 44, 285203. doi:10.1088/1751-8113/44/28/285203 — registro verificado. (K2a)
- **Sierra, G. (2008).** *A quantum mechanical model of the Riemann zeros*. New J. Phys. 10, 033016.
  doi:10.1088/1367-2630/10/3/033016 — registro verificado. (K2b)
- **Sierra, G., & Townsend, P. K. (2008).** *Landau levels and Riemann zeros*. Phys. Rev. Lett. 101, 110201.
  arXiv:0805.4079 — registro verificado. (K2c)
- **Bender, C. M., Brody, D. C., & Müller, M. P. (2017).** *Hamiltonian for the zeros of the Riemann zeta function*.
  Phys. Rev. Lett. 118, 130201. arXiv:1608.03679 — registro verificado. Comentário: Bellissard, arXiv:1704.02644;
  resposta: arXiv:1705.06767 — registros verificados. (K2d)
- **Connes, A. (1999).** *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*.
  Selecta Math. (N.S.) 5, 29–106. doi:10.1007/s000290050042 — registro verificado; enunciado exato da equivalência
  com RH a conferir (11.3). (K3)
- **Lagarias, J. C. (2006).** *Hilbert spaces of entire functions and Dirichlet L-functions*. Em *Frontiers in Number
  Theory, Physics and Geometry I*, Springer, 365–377 — registro verificado. (K4)
- **Conrey, J. B., & Li, X.-J. (2000).** *A note on some positivity conditions related to zeta and L-functions*.
  IMRN 2000(18), 929–940. arXiv:math/9812166 — registro verificado. (K4)
- **de Branges, L. (1968).** *Hilbert Spaces of Entire Functions*. Prentice-Hall — a verificar. (K4)
- **Selberg, A. (1956).** *Harmonic analysis and discontinuous groups in weakly symmetric Riemannian spaces with
  applications to Dirichlet series*. J. Indian Math. Soc. 20, 47–87 — registro verificado. (K5)
- **Hejhal, D. A.** *The Selberg Trace Formula for PSL(2, ℝ)*, Lecture Notes in Math. 548 (1976), 1001 (1983) — a
  verificar, incluindo a matriz de espalhamento de PSL(2, ℤ). (K5)
- **Bolte, J., Steil, G., & Steiner, F. (1992).** *Arithmetical chaos and violation of universality in energy level
  statistics*. Phys. Rev. Lett. 69, 2188 — registro verificado. (K5, T6)
- **Bogomolny, E. B., Georgeot, B., Giannoni, M.-J., & Schmit, C. (1992).** *Chaotic billiards generated by arithmetic
  groups*. Phys. Rev. Lett. 69, 1477 — registro verificado. (K5, T6)
- **Gutzwiller, M. C. (1971).** *Periodic orbits and classical quantization conditions*. J. Math. Phys. 12, 343–358 —
  registro verificado. (K6)
- **Bohigas, O., Giannoni, M.-J., & Schmit, C. (1984).** *Characterization of chaotic quantum spectra and universality
  of level fluctuation laws*. Phys. Rev. Lett. 52, 1–4 — registro verificado. (K6, K7, T5)
- **Balian, R., & Bloch, C. (1972).** *Distribution of eigenfrequencies for the wave equation in a finite domain III*.
  Ann. Phys. 69, 76–160 — registro confirmado pela lista de referências de Berry–Keating (1999, SIAM, ref. [20]);
  texto não lido. (K7)
- **Wu, H., & Sprung, D. W. L. (1993).** *Riemann zeros and a fractal potential*. Phys. Rev. E 48, 2595 — registro
  verificado. (K8)
- **Duistermaat, J. J., & Guillemin, V. W. (1975).** *The spectrum of positive elliptic operators and periodic
  bicharacteristics*. Invent. Math. 29, 39–80. doi:10.1007/BF01405172 — registro verificado. (K9)
- **Hörmander, L. (1968).** *The spectral function of an elliptic operator*. Acta Math. 121, 193–218 — a verificar. (K9)
- **Rudnick, Z., & Sarnak, P. (1996).** *Zeros of principal L-functions and random matrix theory*. Duke Math. J. 81,
  269–322 — registro verificado. (K11, T2)
- **Keating, J. P., & Snaith, N. C. (2000).** *Random matrix theory and ζ(1/2+it)*. Comm. Math. Phys. 214, 57–89; e
  **Katz, N. M., & Sarnak, P. (1999).** *Zeroes of zeta functions and symmetry*. Bull. AMS 36, 1–26 — a verificar. (K11)
- **Fórmula explícita (Weil; Guinand).** Weil, *Sur les « formules explicites » de la théorie des nombres premiers*
  (Œuvres II, 48–61); Guinand, Proc. London Math. Soc. (2) 50 (1948), 107 — registros a conferir; constantes e classe
  de funções-teste na convenção do projeto: lacunas L-EF1 e L-EF2 ([ETAPA11_PLANO.md](ETAPA11_PLANO.md) §3).

### 5.1 Revisão 11.3 (14/09/2026): fontes lidas e correções de registro

Cópias exatas dos PDFs lidos, com versão, URL, data e hora, SHA-256 e correspondência de páginas:
`archive/fontes_etapa11/MANIFESTO.csv`. No arXiv, a página do PDF coincide com a impressa. Na cópia de Berry–Keating
(SIAM), página impressa = página do PDF + 235.

Leitura do texto (não só registro). Páginas usadas na matriz seguem estas versões. Evidências em
[etapa11_evidencias.csv](etapa11_evidencias.csv).

- **Connes (1999)** — lido em arXiv:math/9811068v1. Teorema 1 (p. 13), Corolário 2 (p. 14), Teorema 4 (p. 31),
  Teorema 5 (p. 42, **característica positiva**), extensão a ℚ (p. 45–47), contagem semiclássica (p. 47–48).
  **Correção bibliográfica do projeto** (não é novidade científica): a matriz anterior atribuía a equivalência entre
  fórmula de traço global e RH a ζ sem registrar que o Teorema 5 é enunciado para característica positiva.
- **Conrey & Li (2000)** — lido em arXiv:math/9812166v1. Teorema 1 (p. 2), exemplos para ζ (p. 6–7).
- **Bender, Brody & Müller (2017)** — lido em arXiv:1608.03679v4. **Bellissard** — arXiv:1704.02644v1 (3 p.).
  **Réplica** — *Comment on 'Comment on "Hamiltonian for the zeros of the Riemann zeta function"'*, arXiv:1705.06767v1.
- **Sierra (2008)** — lido em arXiv:0712.0705v1. **Sierra & Townsend (2008)** — lido em arXiv:0805.4079v2.
- **Berry & Keating (1999), SIAM Rev. 41, 236–266** — lido em cópia do artigo publicado hospedada em
  <https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/berry-keating1.pdf> (hospedagem de terceiros; paginação da
  revista). p. 241–243 e 260–262.
- **Marklof, J. (2004).** *Selberg's trace formula: an introduction*. arXiv:math/0407288; publicado em *Hyperbolic
  Geometry and Applications in Quantum Chaos and Cosmology*, Cambridge Univ. Press, 83–119. Fonte **secundária
  rigorosa** para Selberg (compacto): Teorema 4 (p. 25), Prop. 10 (p. 26), hipóteses (p. 12). A fonte primária
  (Selberg 1956) não foi lida.
- **Correção de registro:** uma busca atribuiu a Lagarias (2006) o identificador arXiv:math/0010324. Esse identificador
  é de outro artigo (*Apollonian Circle Packings… III*). O texto de Lagarias (2006) não foi obtido; uso limitado ao
  resumo.
- **Wu & Sprung (1993)** — texto não obtido. "Primeiros 500 zeros" e "dimensão 1,5" vêm de descrições secundárias
  (resultado de busca); uso restrito a P/PC.
- **Bogomolny, Georgeot, Giannoni & Schmit (1997).** *Arithmetical chaos*. Phys. Rep. 291, 219–326 — registro por busca;
  candidato para conferir T6/K5 N4 (11.3b).

- **Platt, D. J., & Trudgian, T. S. (2021).** *The Riemann hypothesis is true up to 3·10¹²*. Bull. London Math. Soc.
  53(3), 792–797. doi:10.1112/blms.12460. Referência editorial indicada pela auditoria de 14/09/2026. A página
  respondeu 403 e o arXiv recusou conexão: **texto não lido**. Usada só como hipótese rotulada (H₀) em
  ETAPA11_3B_FORMULA_EXPLICITA §2.2; volume, número e páginas também a conferir.

### 5.2 Revisão 11.3b-26 (16/09/2026): fontes arquivadas e pendências de H1

**Arquivadas e lidas.** Todas em `archive/fontes_etapa11/`, com SHA-256 em `MANIFESTO.csv`, versão 1.2.7 da DLMF
(release 2026-06-15) lida no rodapé de cada arquivo.

- **DLMF §25.2 — Definition and Expansions** (Riemann zeta). <https://dlmf.nist.gov/25.2>, arquivada em 14/09/2026.
  Usos:
  - eq. 25.2.3 (ζ(½) < 0, exclusão de γ = 0 no Lema 4);
  - eqs. 25.2.1 e 25.2.10 (cota N(T), Z1);
  - eq. 25.2.11 (C16).
- **DLMF §25.10 — Zeros** (Riemann zeta). <https://dlmf.nist.gov/25.10>, arquivada em 14/09/2026. Eqs. 25.10.1–25.10.3.
  **Não** contém N(T) = θ(T)/π + 1 + S(T) (correção de citação do plano M3).
- **DLMF §5.9 — Integral Representations** (Gamma/psi). <https://dlmf.nist.gov/5.9>, arquivada em 14/09/2026. Eq. 5.9.12
  (termo arquimediano, H2; sup|θ‴| em S3b).
- **DLMF §5.11 — Asymptotic Expansions** (Gamma/psi). <https://dlmf.nist.gov/5.11>, arquivada em 14/09/2026. Eq. 5.11.2 e
  §5.11(ii), limites de resto (cota certificada de L-EF2a(a3)).
- **mpmath (versão instalada 1.4.1)**, contexto `iv` (aritmética intervalar com arredondamento dirigido). Usado nos
  enclausuramentos das etapas 11.3b e R5 e no certificado da Cauda Projetada (execução 4). Sua correção faz parte da base
  de confiança declarada; documentação do contexto `iv` não arquivada.

**Pendentes (não lidas; dados bibliográficos a conferir antes de qualquer uso como S ou V):**
- **J1 — Fórmula de Jensen** (teorema clássico de análise complexa). Usada em Z1 (ETAPA11_3B_Z1_CONTAGEM §§2–3) e na
  contagem local do Lema 4. **Nenhuma fonte arquivada.** Candidatos usuais: livros-texto de análise complexa (p.ex.
  Ahlfors, *Complex Analysis*; Titchmarsh, *The Theory of Functions*). Edição e seção **não conferidas**; indicar só após
  leitura.
- **F3 — Trudgian, T. S. (2014).** Cota explícita para |S(T)| (*J. Number Theory*; arXiv:1208.5846). Dados por resultado
  de busca, **texto não lido**. O uso em R_longe/E_z2 foi resolvido por derivação própria (Z1 §4); as constantes finas de
  S(T) não são usadas.
- **F9 — Gonek, S. M. (1993).** *An explicit formula of Landau and its applications to the theory of the zeta-function*,
  Contemp. Math. 143. Dados por busca, **texto não lido**. Rota R2 de H1.
- **F10 — Fórmulas truncadas explícitas para S(t)** (tradição de Selberg; Tsang). Referências específicas **não
  identificadas** em servidor acessível; nenhum dado bibliográfico registrado como conferido. Rota R3 de H1.
- **F11 — Forma explícita truncada de ψ(x)** ou de somas de Chebyshev torcidas com erro explícito (p.ex. Davenport,
  *Multiplicative Number Theory*, cap. 17; Montgomery–Vaughan, *Multiplicative Number Theory I*, cap. 12). Capítulos
  **não conferidos**. Rota B do Lema de Cauda Projetada.
- **Estado de acesso:** consolidado em [ETAPA11_PENDENCIAS_FONTES.md](ETAPA11_PENDENCIAS_FONTES.md) §4.

## Busca preliminar para o manuscrito (17/09/2026)

Registro separado, com níveis de conferência (lido / resumo / só metadados) e trabalhos próximos (Büthe 2018; Balanzario
et al. 2023): [BUSCA_BIBLIOGRAFICA_MANUSCRITO.md](BUSCA_BIBLIOGRAFICA_MANUSCRITO.md). Não autoriza afirmação de novidade.
