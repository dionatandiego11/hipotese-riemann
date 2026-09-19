# Etapa 11.3b — registro de fontes e hipóteses pendentes

**Data:** 14/09/2026, 09:28. **Estado da 11.3b:** `em execução`. Os itens de fonte abaixo estão `bloqueado` por acesso
de rede nesta sessão, não por decisão metodológica.

**Uso:** a seleção de candidatos e o congelamento de testes esperam as evidências pertinentes. Nenhum item abaixo
pode ser tratado como conferido enquanto a coluna "Conferido" disser "não". Mais casos numéricos não substituem
estas justificativas.

## 1. Pendências prioritárias (fórmula explícita e instrumento)

| ID | Fonte ou hipótese | Para que serve | Onde é usada | Situação | Tentativas de acesso (14/09/2026) | Conferido |
|---|---|---|---|---|---|---|
| F1 | Platt & Trudgian (2021), *The Riemann hypothesis is true up to 3·10¹²*, Bull. London Math. Soc., doi:10.1112/blms.12460 (arXiv:2004.09765) | criticidade de todos os zeros com 0 < γ ≤ 3·10¹² | L-EF2a(a2) criticidade; L-EF2b (H₀, R_longe); hipótese Σ_ρ h = 2Σ_{γ>0} h da checagem gaussiana; K3a N1–N4 | **conferido em 17/09/2026** (§5): Teorema 1 lido | página editorial 403 (curl, WebFetch); arXiv conexão recusada (curl, com e sem sandbox); repositório de Bristol sem resposta (WebFetch); ADS recusado | sim (arXiv v1, p. 2) |
| F2 | Simplicidade dos zeros usados (índices ≤ 100.000) | identificar a soma com multiplicidade com a tabela; D_t = ½Σ k_t | L-EF2a(a2), L-EF2b; K3a M6 e N | **conferido em 17/09/2026** (§5): simplicidade dos primeiros 1.500.000.001 zeros lida | depende de F1 ou de outra verificação publicada (não identificada nesta sessão) | sim (Math. Comp. 46, p. 667) |
| F3 | Cota explícita de contagem, por exemplo \|S(T)\| ≤ a log T + b log log T + c (Trudgian 2014, J. Number Theory; arXiv:1208.5846), da qual sai N(T) ≤ T² para T ≥ 7·10⁴ | cauda de zeros distantes | L-EF2b R_longe; E_z2 da checagem gaussiana | **conferido em 17/09/2026** (§5): Teorema 1 lido; continua não usado (Z1 §4 basta) | arXiv recusado; ScienceDirect e UNSW recusados; ANU openresearch recusado (WebFetch) | sim (arXiv v2, p. 1) |
| F4 | N(T) = θ(T)/π + 1 + S(T) contando todos os zeros por Im ρ, sem supor ordenadas reais (Titchmarsh, *The Theory of the Riemann Zeta-Function*, cap. 9) | identidade de Stieltjes incondicional | L-EF2a(a1); plano M3 | **conferido em 17/09/2026** (§7): Titchmarsh 1986, §9.3, p. 212 | DLMF §25.10 arquivada **não** contém a fórmula; BK SIAM p. 239 contém, "for the t_n (assumed real)" | sim (p. 212) |
| F5 | Classe de funções-teste da fórmula explícita: Weil (1952) ou enunciado moderno (por exemplo, Carneiro–Chandee–Milinovich, arXiv:1309.1526, Lema 5) | hipóteses de h e g em L-EF1; admissibilidade de h_ε | L-EF1; L-EF2b | **Weil 1952 lido em transcrição em 19/09/2026 (§16)**; enunciado moderno sob RH lido em 17/09/2026 (§5) | cópia da transcrição enviada pelo usuário | sim, na transcrição (condições (A) e (B), p. 6; fórmula (11), pp. 8–9); conferência contra o fac-símile do original continua desejável |
| F6 | Convenção de Frobenius e P₁(T) = det(I − TF \| H¹): Milne, *Lectures on Étale Cohomology*; Deligne, *La conjecture de Weil I* (Publ. IHÉS 43, Numdam) | normalização de C19; C11 | correspondências C11, C19 | **conferido em 17/09/2026** (§5): Milne Teor. 27.6 e mapa de Frobenius; Deligne (1.15) | jmilne.org recusado (curl, WebFetch); Numdam recusado | sim (Milne LEC v2.21, PDF p. 155; Deligne PMIHÉS 43, p. 279) |
| F8 | Z1: Σ_ρ 1/(1 + (Im ρ)²) < ∞ | convergência dominada da soma sobre zeros na extensão para 𝒜 | [ETAPA11_3B_ADMISSIBILIDADE.md](ETAPA11_3B_ADMISSIBILIDADE.md) §2 | **resolvida por derivação** ([ETAPA11_3B_Z1_CONTAGEM.md](ETAPA11_3B_Z1_CONTAGEM.md): N(T) ≤ 31 + 5,25·T·log(T+9) via DLMF 25.2.1, 25.2.10 e Jensen) | — | derivação; pendência bibliográfica J1 |
| F9 | Gonek (1993), *An explicit formula of Landau and its applications to the theory of the zeta-function*, Contemp. Math. 143 | rota R2 de H1 | [ETAPA11_3B_H1_FORMULACAO.md](ETAPA11_3B_H1_FORMULACAO.md) §6 | `bloqueado` (acesso) | não tentada individualmente; hosts de editoras e arXiv recusados nesta sessão | não |
| F10 | Fórmula truncada explícita para S(t) (Selberg; Tsang) | rota R3 de H1 | idem | `bloqueado` | não localizada em servidor acessível | não |
| F11 | Forma explícita truncada de ψ(x) ou de Σ Λ(n)n^{−1/2+iτ} com erro explícito (Davenport cap. 17; Montgomery–Vaughan cap. 12) | Lema de Cauda Projetada, Rota B sob RH | [ETAPA11_3B_H1_CAUDA_PROJETADA.md](ETAPA11_3B_H1_CAUDA_PROJETADA.md) II.4 | **conferido em 17/09/2026** (§7): Montgomery–Vaughan, Teorema 12.5, p. 400 | não tentada individualmente | sim (p. 400) |
| J1 | Fonte arquivada para a fórmula de Jensen (teorema clássico de análise complexa) | Z1; cota N(T) | ETAPA11_3B_Z1_CONTAGEM §§2–3 | **resolvida em 17/09/2026**: Titchmarsh, *The Theory of Functions*, 2.ª ed., Oxford, 1939, §3.61, pp. 125–126, lido no exemplar digitalizado do Internet Archive (`in.ernet.dli.2015.2588`; OCR SHA-256 `dc00331963a4c887…`, não arquivado por direitos); registro em [BUSCA_BIBLIOGRAFICA_MANUSCRITO.md](BUSCA_BIBLIOGRAFICA_MANUSCRITO.md) §6 | acessado | sim (só URL e hash) |
| F7 | Declaração de procedência e completude da tabela `zeros1` (página de Odlyzko) | completude documental da tabela, além da recontagem B | L-EF2a(a2) | **parcialmente conferido em 17/09/2026** (§5): precisão declarada lida; completude e procedência não declaradas na página | www-users.cse.umn.edu recusado | parcial |

**Natureza das pendências (revisão 11.3b-5):**
- **bibliográficas** (conferir fonte original de um enunciado já usado a partir de fonte secundária conferida): F5, J1;
- **hipóteses de fato ainda não sustentadas** por fonte lida ou derivação: F1 (criticidade até H₀), F2
  (simplicidade), F4 (forma incondicional da contagem), F6 (Frobenius), F7 (procedência da tabela).

## 2. Hipóteses sem fonte a obter (trabalho matemático)

| ID | Hipótese ou problema | Onde | Situação |
|---|---|---|---|
| H1 | L-EF2c: passagem do observável congelado para o modelo de linhas com erro controlado | ETAPA11_3B §2.3; [ETAPA11_3B_H1_FORMULACAO.md](ETAPA11_3B_H1_FORMULACAO.md) | aberto; **registrado como item em aberto no encerramento da 11.3b (17/09/2026)**, ver [ETAPA11_3B_ENCERRAMENTO.md](ETAPA11_3B_ENCERRAMENTO.md). Enunciado formulado (observável O₁/O₂, truncamentos, normas, uniformidade; candidatos S1–S5; rotas R1–R5). A cota absoluta de R1 não fecha; R2 e R3 dependem de F9 e F10. **Revisão 11.3b-26:** S3b derivada condicionalmente; S1 quantificado e aberto; R5 formalizado e encerrado; Cauda Projetada com condição suficiente para S2-ratio′(U₂) certificada sob RH para M^math em (8, 2), 461/461 elegíveis (execução 4, dependência herdada eliminada; [ETAPA11_3B_H1_CAUDA_PROJETADA.md](ETAPA11_3B_H1_CAUDA_PROJETADA.md) §II.20); S3a, S3c e passagem ao estimador registrado pendentes |
| H2 | Termo arquimediano de L-EF1 derivado analiticamente das eqs. (10)–(11) e (31) de Connes | [ETAPA11_3B_TERMO_ARQUIMEDIANO.md](ETAPA11_3B_TERMO_ARQUIMEDIANO.md) | **derivação concluída** (14/09/2026) para a classe 𝒢; evidência E-LEF1-ARCH; aplicabilidade do Teorema 1 a 𝒢 depende de F5 |
| H3 | Regularidade adicional exigida por Weil além do decaimento (se houver) | L-EF1 | depende de F5. Classe suficiente 𝒜 especificada e admissibilidade derivada via Teorema 6 de Connes (conferido) com Z1 derivado; F5 permanece como conferência bibliográfica ([ETAPA11_3B_ADMISSIBILIDADE.md](ETAPA11_3B_ADMISSIBILIDADE.md)) |

## 3. Pendências da matriz de classes (menor prioridade para a fórmula explícita)

Resumidas de [ETAPA11_MATRIZ_OPERADORES.md](ETAPA11_MATRIZ_OPERADORES.md) §0.3; estado inalterado (PC):
- Berry–Keating 2011 (K2a M1);
- Wu–Sprung 1993 (K8 M1);
- Hörmander 1968 e Duistermaat–Guillemin 1975 (K9);
- Balian–Bloch 1972 e lei de Weyl para domínios limitados (K7);
- Selberg 1956 e Hejhal, incluindo o caso cofinito e PSL(2,ℤ) (K5b);
- BGGS 1992 e BSS 1992 (K5 N4, T6);
- Lagarias 2006 (K4, `conferencia`).

## 4. Hosts testados nesta sessão

Entre 08:55 e 09:28 de 14/09/2026, por curl, com resposta HTTP ou falha:

| Resultado | Hosts |
|---|---|
| **Responderam 200** | dlmf.nist.gov (§25.2, §25.10, §5.9 e §5.11 arquivadas com SHA-256; versão 1.2.7 lida no rodapé), core.ac.uk (desafio Cloudflare, sem conteúdo útil), www.semanticscholar.org (página; a API não respondeu), www.google.com |
| **Responderam 403** | londmathsoc.onlinelibrary.wiley.com, www.ams.org |
| **Conexão recusada ou sem resposta** | arxiv.org, export.arxiv.org, www.jmilne.org, jmilne.org, www.numdam.org, projecteuclid.org, link.springer.com, www.cambridge.org, www.lmfdb.org, www.math.u-bordeaux.fr, web.maths.unsw.edu.au, maths.anu.edu.au, www.dpmms.cam.ac.uk, scholar.archive.org, research-information.bris.ac.uk, openresearch-repository.anu.edu.au, ui.adsabs.harvard.edu, research.unsw.edu.au, www.sciencedirect.com, www-users.cse.umn.edu |

WebFetch falhou para arXiv, Wiley, Bristol, ANU e jmilne.org.

**Próxima ação:** repetir F1–F7 quando houver acesso, arquivar com SHA-256 e atualizar evidências. Não inferir conteúdo
a partir de resultados de busca.

## 5. Rodada de acesso de 17/09/2026

Downloads por curl a partir das URLs registradas em `archive/fontes_etapa11/MANIFESTO.csv` (SHA-256, bytes, páginas e
correspondência de páginas). Os arquivos ficam fora do git (`.gitignore`). Cada linha abaixo registra **o que foi lido**,
não só o que foi baixado.

| ID | Fonte arquivada | Enunciado lido (página) | Consequência para a pendência |
|---|---|---|---|
| F1 | Platt & Trudgian, arXiv:2004.09765v1 (`3362f66a…`) | Teorema 1 (p. 2): "The Riemann hypothesis is true up to height 3 000 175 332 800. That is, the lowest 12 363 153 437 138 non-trivial zeroes ρ have ℜρ = 1/2." Verificação com aritmética intervalar (resumo, p. 1) | criticidade até H₀ = 3·10¹² passa a ter fonte lida. Ressalva: versão arXiv; a publicada (Bull. LMS 53, 2021) não foi comparada |
| F2 | van de Lune, te Riele & Winter, Math. Comp. 46 (1986) 667–681, cópia do CWI (`3c48d6e7…`) | resumo e §1 (p. 667): os primeiros 1.500.000.001 zeros na faixa crítica, com 0 < t < 545.439.823,215, têm parte real ½ "and are simple" | simplicidade dos zeros de índice ≤ 100.000 (γ ≤ 74.920,83) passa a ter fonte lida. É enunciado dos autores sobre sua computação; o método de separação não foi reexaminado |
| F3 | Trudgian, arXiv:1208.5846v2 (`274b3a0a…`) | Teorema 1 (p. 1): \|S(T)\| ≤ 0,111 log T + 0,275 log log T + 2,450 para T ≥ e | fonte lida; **nenhum uso novo**: R_longe/E_z2 continuam pela derivação própria (Z1 §4) |
| F5 | Carneiro, Chandee & Milinovich, arXiv:1309.1526v1 (`6ad94674…`) | Lema 5 (pp. 6–7): **sob RH**, fórmula explícita para h analítica na faixa \|Im s\| ≤ ½ + ε, com \|h(s)\| ≪ (1 + \|s\|)^−(1+δ), h real na reta real, e ĥ com a convenção e^{−2πixw} | enunciado moderno **condicional a RH**; não substitui Weil 1952 para a forma incondicional. O ponto de partida do projeto continua sendo Connes Teorema 6 + Lema 3. **F5 continua pendente** como conferência do original |
| F6 | Milne, *LEC* v2.21 (`ac4f122f…`); Deligne, *La conjecture de Weil : I*, PMIHÉS 43 (`8392b345…`) | Milne Teor. 27.6 (PDF p. 155): Z(X₀, t) = P₁⋯P_{2d−1}/(P₀⋯P_{2d}) com **P_r(X, t) = det(1 − Ft \| H^r(X, ℚ_ℓ))**, F o mapa de Frobenius de X (§27, "The Frobenius map": coordenadas elevadas à q); Teor. 27.15 (PDF p. 158): autovalores de F em H^r com valor absoluto q^{r/2}. Deligne p. 279 (conferido na imagem da página): (1.14.3) Z(X₀, 𝓕₀, t) = Π_i det(1 − F*t, H^i_c(X, 𝓕))^{(−1)^{i+1}}; (1.15) Frobenius geométrico F := φ⁻¹, φ a substituição de Frobenius, e (1.15.1) F* = F | a forma de P₁ e a convenção "Frobenius geométrico" usadas em C19 passam a ter fonte lida. A dedução "zeros em T = α⁻¹, \|α\| = q^{1/2} ⇔ ℜs = ½" é elementar a partir de 27.6 e 27.15 |
| F7 | índice das tabelas de Odlyzko (`7d0399f7…`) | "The first 100,000 zeros of the Riemann zeta function, accurate to within 3*10^(-9)." | a **precisão declarada** usada em H-tab passa a ter fonte lida. A página **não** declara completude, método nem licença; essas partes continuam pendentes |
| K9 (matriz) | Hörmander, Acta Math. 121 (1968) 193–218 (`a633994c…`) | Teorema 1.1 (p. 194): para P elíptico, formalmente positivo, de ordem m, e uma extensão auto-adjunta P̂, R(x, λ) = O(λ^{−1/m}) uniformemente em compactos, com R(x, λ) = λ^{−n/m}e(x, x, λ) − (2π)^{−n}∫_{p(x,ξ)<1}dξ (eq. 1.1, p. 193) | lei de Weyl **local** com resto ótimo, para a função espectral. A passagem para a contagem N(λ) numa variedade compacta e as hipóteses de Duistermaat–Guillemin (1975, não obtido) ficam por escrever antes de alterar códigos |

**Ainda não obtidas (dependem de acesso externo):** Weil 1952 (F5 original), Titchmarsh 1986 cap. 9 (F4), Gonek 1993
(F9), Selberg/Tsang (F10), Davenport ou Montgomery–Vaughan (F11), e as da matriz §0.3: BK 2011, Wu–Sprung 1993,
Duistermaat–Guillemin 1975, Balian–Bloch 1972, Selberg 1956/Hejhal/Iwaniec, BGGS 1992, BSS 1992, Lagarias 2006.

**Não alterado nesta rodada:** códigos `situacao`/`conferencia` da matriz e `etapa11_evidencias.csv`. A atualização exige
as linhas de evidência correspondentes e é o próximo passo.


## 6. Fontes enviadas pelo usuário (17/09/2026, 09:25–09:28)

Arquivos renomeados para o padrão do arquivo e registrados em `MANIFESTO.csv`.

| Item | Arquivo | O que foi lido (página) | Consequência |
|---|---|---|---|
| **K8, M1** (matriz §0.3, item 6) | Wu & Sprung, Phys. Rev. E 48 (1993) 2595–2598 (`7ccb97d2…`) | p. 2596, imagem da página conferida: V₀ fixado por ajuste ao primeiro zero (14,134725); V(x) obtido minimizando F = Σ_n(e_n − E_n)² (eq. 9) sobre os primeiros N zeros, com os E_n calculados (via Mathematica) e derivada funcional δF/δV = 2Σ(e_n − E_n)φ_n² (eq. 11); ajuste até N = 500 | **respondido: o método usa os zeros como dado de entrada.** O potencial não é definido independentemente dos níveis que reproduz; cai no mesmo caso do controle de ajuste K12 para N1–N4. Atualização do código exige linha de evidência |
| **K5, N4** (item 3), apoio parcial | Bogomolny, *Quantum and Arithmetical Chaos*, HAL-00000984v1 (`ab4531e6…`) | resumo (PDF p. 3): superfícies geradas por grupos aritméticos têm estatística "close to the Poisson statistics"; Cap. 3 (PDF p. 68): observação numérica (refs. [3], [52]) para o triângulo modular (π/2, π/3, 0) com Dirichlet, e mecanismo pela degenerescência exponencial dos comprimentos de órbitas | fonte **secundária e declaradamente não formal** ("analogies are used instead of theorems"). Sustenta P (heurístico/numérico) com página; **não** sustenta S/V. BGGS 1992 e BSS 1992 continuam necessários para a página primária |
| (removidos) | Srednicki, arXiv:1104.1850v3; Scharlemann, *Transversality theories at dimension four* | — | **apagados em 17/09/2026 a pedido do usuário**: não correspondiam a nenhuma pendência (Srednicki não é BK 2011; Scharlemann é de topologia). Linha do Srednicki retirada do manifesto |

**Matriz atualizada em 17/09/2026** com o que foi lido: K3a N1–N4 (`C/conferido`), K8 M1 (`V/conferido`), K8 M2
(`P/conferido`) e C19 (`conferido`). Ver [ETAPA11_MATRIZ_OPERADORES.md](ETAPA11_MATRIZ_OPERADORES.md) §0.5.


## 7. Segundo lote enviado pelo usuário (17/09/2026, 09:47–10:12)

Arquivos úteis renomeados e registrados em `MANIFESTO.csv`. **Nenhum código da matriz foi alterado neste registro.**

| Pendência | Arquivo | O que foi lido (página) | Consequência |
|---|---|---|---|
| **F4** | Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2.ª ed. (Heath-Brown, 1986) (`ee495ba7…`) | §9.3, p. 212 (imagem conferida): para T que não é ordenada de zero, S(T) = π⁻¹ arg ζ(½ + iT) por variação contínua; N(T) conta os zeros de Ξ no retângulo de vértices ±T ± 3i/2, isto é, **todos** os zeros não triviais com 0 < t < T, sem supor RH; πN(T) = Δ arg s(s − 1) + Δ arg π^{−s/2} + Δ arg Γ(s/2) + Δ arg ζ(s), com Δ arg s(s − 1) = π, Δ arg π^{−s/2} = −½T log π, Δ arg Γ(s/2) = Im log Γ(¼ + ½iT). Teorema 9.3: N(T) = L(T) + S(T) + O(1/T) | **resolvida**: a forma exata N(T) = θ(T)/π + 1 + S(T), com θ(T) = Im log Γ(¼ + ½iT) − ½T log π (DLMF 25.10.2), sai somando as três variações antes da aproximação de Stirling, contando todos os zeros. Afeta o plano M3 e L-EF2a(a1) |
| **F5** (reforço) | Montgomery & Vaughan, *Multiplicative Number Theory I* (`0b1129e6…`) | Teorema 12.13 (Weil), p. 410: fórmula explícita **incondicional** para F mensurável com ∫e^{(½+δ₀)2π\|x\|}\|F(x)\|dx < ∞ e ∫e^{(½+δ₀)2π\|x\|}\|dF(x)\| < ∞, F(x) = ½(F(x⁻) + F(x⁺)), F(x) + F(−x) = 2F(0) + O(\|x\|), soma sobre zeros como lim_{T→∞} Σ_{\|γ\|≤T} | segundo enunciado moderno **lido**, independente de Connes e sem RH. Cobre as funções-teste com decaimento gaussiano usadas no certificado (g_ν, h_ε); **não** cobre toda a classe 𝒜 (exige peso e^{(½+δ₀)\|u\|} também na variação). **F5 original (Weil 1952) continua não lido** |
| **F11** | Montgomery & Vaughan (mesmo arquivo) | Teorema 12.5, p. 400: ψ₀(x) = x − Σ_{\|γ\|≤T} x^ρ/ρ − log 2π − ½ log(1 − 1/x²) + R(x, T), com R(x, T) ≪ (log x) min(1, x/(T⟨x⟩)) + (x/T)(log xT)² | **resolvida** (fonte da Rota B; prioridade baixa enquanto H1 não for retomada) |
| **K2a** (matriz §0.3 item 1) | Berry & Keating 2011, J. Phys. A 44, 285203 (`ed80fdfc…`) | p. 5: condição de contorno ∂ₓχ(0)/χ(0) = e^{iα}/η (eq. 2.22), "derived as the condition for hermiticity" e "first guessed from numerical explorations"; "Each choice of α corresponds to a different self-adjoint extension of the formal operator"; a condição "holds only for states decaying as x → ∞". Resumo: espectro discreto real e os dois primeiros termos da densidade iguais aos dos zeros | o texto **afirma** as extensões auto-adjuntas a partir de uma condição de hermiticidade; não há prova de igualdade de domínios. **Aplicado em 17/09/2026** (§5 lida, pp. 12–13): K2a M1 `S/PC` → `P/conferido`; K2a M3 e N1 `P/PC` → `P/conferido` (matriz §0.6) |
| **K5** (opcional) | Selberg 1956, tradução russa (`ae262fdb…`) | identificação: texto de Selberg sobre a fórmula de traço (classes hiperbólicas, elípticas e parabólicas); dados da coletânea não conferidos | original de Selberg disponível só em tradução; Marklof continua sendo a fonte usada |
| **K5b** (secundárias) | Arakawa, notas sobre fórmulas de traço de Selberg para SL₂(ℝ) (`6ab38fa4…`); notas de curso "785" sobre formas automórficas, sem autor declarado (`67e3ad13…`) | sumários: séries de Eisenstein, matriz de espalhamento, termos parabólicos; lei de Weyl | fontes **secundárias sem dados de publicação**; podem orientar a leitura, mas não sustentam S/V. Hejhal ou Iwaniec continuam necessários |
| **F9** (secundária) | Durkan, Hughes & Pearce-Crump, arXiv:2601.18025v1 (`9b29bb43…`) | resumo: generalizações do teorema de Landau–Gonek | secundária para a rota R2; Gonek 1993 continua não lido |

**Não correspondem a pendências** (não registrados; **apagados em 17/09/2026 a pedido do usuário**): `1110.5627v1.pdf` (Sjamaar, memorial sobre
Duistermaat, não é Duistermaat–Guillemin 1975); `Quantum_and_Arithmetical_Chaos.pdf` (versão arXiv nlin/0312061 das
mesmas notas de Bogomolny já registradas pela cópia HAL); `Pretentious010611.pdf` (Granville & Soundararajan, rascunho de
livro marcado "Please do not circulate", não pedido).

## 8. Terceiro lote enviado pelo usuário (17/09/2026, 10:21–10:23)

| Pendência | Arquivo | O que foi lido (página) | Consequência |
|---|---|---|---|
| **K4** (matriz §0.3 item 7b) | Lagarias, *Hilbert Spaces of Entire Functions and Dirichlet L-Functions*, preprint de 2006 (`5e0cef3b…`; publicado em *Frontiers I*, 365–377, versão publicada não comparada). Texto em fontes Type 3, lido por imagem | Teorema 1 (p. 9): E_χ(z) = ξ_χ(½ − iz) + ξ′_χ(½ − iz) é de de Branges ⇔ RH para L(s, χ), e estrita ⇔ RH e zeros simples. p. 7: M_z(A) tem espectro discreto simples nos zeros de A de multiplicidade maior que a de B | K4 M1, M2, M3, M6 e N1–N4 passam de `C/PC` para **`C/conferido`** (E-K4-TEOR1; matriz §0.6). Situação inalterada |
| (duplicata, apagada) | `berry4401.pdf` | SHA-256 idêntico ao de `berry_keating_2011_JPhysA44_285203.pdf` | apagado |

## 9. Conferência de cobertura do item A4 (K5b, PSL(2,ℤ)) pelas notas secundárias (17/09/2026)

O item A4 pede: (a) fórmula de traço de Selberg com termos parabólicos e elípticos; (b) matriz de espalhamento de
PSL(2,ℤ) em termos de ξ; (c) lei de Weyl para formas cuspidais com o termo logarítmico do espectro contínuo.

| Parte | Arakawa, notas (`6ab38fa4…`) | Notas "785", sem autor (`67e3ad13…`) | Cobertura |
|---|---|---|---|
| (a) | **Teorema 2.7 (STF), p. 20** (PDF p. 21): fórmula de traço para subgrupo cofinito de SL₂(ℝ) com sistema multiplicador unitário e peso k, com termos de identidade, hiperbólicos, elípticos e parabólicos; segue Fischer (LNM) e Roelcke/Elstrodt. PSL(2,ℤ) é o caso de peso 0 e multiplicador trivial (especialização não escrita no texto) | só anuncia a fórmula como ferramenta do curso (introdução) | **parcial**: enunciado geral em notas secundárias sem dados de publicação |
| (b) | calcula Φ(s) para Γ₀(4) com multiplicador theta (p. 10), **não** para PSL(2,ℤ) de peso 0 | **p. 116** (PDF): termo constante de E(z,s) para SL(2,ℤ): a₀(y,s) = 2y^s + 2π^{2s−1}[Γ(1−s)ζ(2−2s)/(Γ(s)ζ(2s))]y^{1−s}, "we may compute" (sem prova) | **parcial**: fórmula presente só em notas sem autoria, sem demonstração |
| (c) | não encontrada (nenhuma ocorrência de "Weyl") | só menção na introdução | **não coberta** |

**Conclusão:** as notas orientam a leitura, mas não sustentam códigos S/V em K5b (secundárias, sem publicação
identificada; (c) ausente). K5b continua PC. Fontes que resolvem: Hejhal, LNM 1001; Iwaniec, *Spectral Methods of
Automorphic Forms*; ou Fischer, *An approach to the Selberg trace formula via the Selberg zeta-function*, LNM 1253
(fonte seguida por Arakawa; dados a conferir).


## 10. Quarto lote: equivalentes livres indicados pelo usuário (17/09/2026, 10:57–11:10)

Cada indicação foi conferida no próprio arquivo antes do registro. Duplicatas byte a byte foram apagadas; arquivos sem
relação com as pendências também (ensaio de divulgação, artigo de Watkins et al. sobre curvas elípticas, folha de rosto
do volume 176 da CMP, tese de Lester, impressão em PDF da página da Scholarpedia).

| Item | Arquivo | Conferido no texto | Correções à indicação |
|---|---|---|---|
| A1(b) Weyl de bilhares | Bäcker, arXiv:nlin/0204061 (`baecker_2002…`) | PDF p. 22, eqs. (48)–(49): N̄(E) = (A/4π)E − (L/4π)√E + C + ⋯, L = L₋ − L₊ (Dirichlet/Neumann), C com correções de curvatura e cantos; método de integral de contorno ilustrado no estádio | fonte **secundária** (revisão; cita [39] para a fórmula) |
| A1(a) auto-adjunticidade | Hörmander 1968 (já lido) | p. 193: extensão de Friedrichs de operador elíptico formalmente positivo em variedade paracompacta | a identificação "extensão de Friedrichs de −Δ em C₀^∞(Ω) = laplaciano de Dirichlet" e o espectro discreto em domínio limitado não estão escritos na fonte |
| A1(c) períodos genéricos | Bogomolny, notas de Les Houches (já registradas); Bogomolny & Schmit, arXiv:nlin/0312057 | resumo de nlin/0312057: multiplicidade média de comprimentos cresce exponencialmente em certos grupos **não aritméticos** de Hecke | nlin/0312057 **enfraquece** a leitura "genérico ⇒ multiplicidade 1": há modelos não aritméticos com degenerescência. Ambos são heurísticos/numéricos |
| A2 (T5) | Ullmo, Scholarpedia 11(9):31721 (2016), doi:10.4249/scholarpedia.31721 | enunciado original citado: "Spectra of time reversal-invariant systems whose classical analogues are K systems show the same fluctuation properties as predicted by GOE"; "still not proven" | a conjectura original fala só de **GOE** para sistemas com reversão temporal; a versão GUE é uma das "natural extensions" |
| A3 (T6) | Bogomolny–Leyvraz–Schmit, arXiv:chao-dyn/9509019; Sarnak, *Arithmetic Quantum Chaos* (1993, digitalização); notas de Les Houches | BLS, resumo: correlações de dois pontos no domínio modular, Poisson para separações pequenas com oscilações aritméticas; §2: multiplicidade de órbitas identificada com números de classe | BLS é derivação semiclássica com comparação numérica; Sarnak é texto expositivo sem dados de publicação conferidos |
| A4 (K5b) | Iwaniec, notas manuscritas (IAS/AMS 2001); Garrett, *Modern analysis of automorphic forms by examples* (versão on-line autorizada, 2018) | Iwaniec (imagens conferidas): p. 6 laplaciano auto-adjunto e espectro contínuo [¼, ∞); p. 8 fórmula de traço com o termo −(1/4π)∫h(r)φ′/φ(½+ir)dr e "+ ⋯" para os demais termos; **p. 9 lei de Weyl N_Γ(T) + M_Γ(T) = (vol/4π)T² − (k/π)T log T + c_Γ T + O(T/log T)**. Garrett, Obs. 11.1.5 (PDF p. 315): c_s = ξ(2s−1)/ξ(2s) | (a) só parcial (termos elípticos e parabólicos abreviados por "⋯"); (b) e (c) cobertas. Garrett escreve "Γ = SL₂(R)" onde o contexto indica SL₂(Z) (provável erro tipográfico). Notas manuscritas: secundárias |
| A5 (K9 M4) | Dyatlov & Zworski, *Mathematical theory of scattering resonances* v1.0 | fórmulas de traço de Birman–Krein, Melrose e Sjöstrand (ressonâncias) | **não cobre** a fórmula de Duistermaat–Guillemin em variedade compacta (nenhuma ocorrência de geodésicas fechadas/relação de Poisson). Hörmander vol. IV **não** foi obtido. A5 continua pendente |
| B1 | Alt, Dembowski, Gräf, Hofferbert, Rehfeld, Richter & Schmit, arXiv:chao-dyn/9906032 | 955 ressonâncias experimentais até 20 GHz no estádio γ = 1 comparadas a espectro numérico | **autoria corrigida** (não inclui Bäcker). Não traz tabela de níveis; a tabela longa ainda não foi obtida |
| B2 | BLS 1996; Li & Sarnak, *Number variance for SL(2,Z)\H* (2004); Jorgenson, Smajlović & Then, Math. Comp. 83 (2014) 3039–3070 | Li–Sarnak: variância do número de autovalores da superfície modular; JST: autovalores de formas de Maass em grupos moonshine | **autoria corrigida** do preprint de 2004 (Li & Sarnak). Nenhum arquivo traz ainda **lista de autovalores + lista de comprimentos** pronta para uso; B2 continua a identificar |
| C1 (F5) | Bombieri, *Problems of the Millennium: the Riemann Hypothesis* (Clay) | PDF p. 8: classe W de Weil (f contínua e C¹ por partes, f(x) = O(x^δ) em 0⁺ e O(x^{−1−δ}) no infinito) e a fórmula explícita | **autoria corrigida**: o documento do Clay é de **Bombieri**, não de Connes. Enunciado secundário; o original de Weil continua não lido |
| C2 (F7) | Odlyzko, Math. Comp. 48 (1987), cópia JSTOR; tabela `zeros6` (2.001.052 zeros) | resumo (p. 273): primeiros 10⁵ zeros **com precisão ±10⁻⁸**, calculados no Cray-1 e Cray X-MP. Conferência B: os 100.000 primeiros valores de `zeros6` coincidem exatamente com `zeros1` | a precisão do artigo (10⁻⁸) **não** é a da tabela `zeros1` (3·10⁻⁹): a procedência da tabela usada continua só parcial. A distribuição no SageMath é precedente prático, **não** declaração de licença. `zeros6` (36 MB) ficou fora do git |
| D2 | Gourdon 2004 | não baixado | fica para quando a H1 for retomada |

**Aplicado em 17/09/2026 (aprovado pelo usuário):** K7 M2, M3 → `V/derivacao`; K7 N4 → `C/conferido`; K5a N4 → `P/conferido` (matriz §0.6). K5b aguarda análise própria; K7 M1 e M4 continuam PC.

## 11. Quinto lote enviado pelo usuário (17/09/2026, conferido após o commit 43bf2a6)

| Arquivo | Identificação | Consequência |
|---|---|---|
| `braun_haake_2010_arXiv_1001.3339v2.pdf` | Braun & Haake, *Level statistics in arithmetical and pseudo-arithmetical chaos* | **Útil, com nuance para T6.** Resumo: em bilhares de curvatura negativa constante com comprimentos de órbitas muito degenerados, a estatística é Poisson **ou** Wigner–Dyson **conforme a condição de contorno** (Dirichlet/Neumann), com a mesma dinâmica clássica; o fator decisivo são os índices de Maslov dentro dos multipletos. Consequência: E-T6-ARIT (K5a N4 = P) continua válido, mas "aritmético ⇒ Poisson" não é incondicional para bilhares; o protocolo do controle aritmético (11.6) precisa fixar a condição de contorno e o setor de simetria antes do cálculo |
| `kieburg_2026_arXiv_2604.12141v2.pdf` | Kieburg, *Quantum chaotic systems: a random-matrix approach* (revisão) | **Útil como secundária de método** para os controles: classificação de simetria (GOE/GUE/GSE) e unfolding. Não altera códigos |
| `9906032v1.pdf` | outra versão arXiv do artigo de Alt et al. (bytes diferentes, mesmo conteúdo) | duplicata; apagada |
| `1102.4822v1.pdf` | Anderson, Bender & Morone, órbitas periódicas com energia complexa | sem pendência correspondente; apagado |
| `2402.01455v1.pdf` | Walker, autocorrelações de números de classe de Hurwitz | sem pendência correspondente; apagado |
| `9403001v1.pdf` | Kennel, Abarbanel & Sidorowich, erros de predição e expoentes de Lyapunov locais | sem relação; apagado |
| `BLZ2015.pdf` | Bruggeman, Lewis & Zagier, *Period functions for Maass wave forms and cohomology* (AMS Memoirs), cópia licenciada a uma instituição | sem pendência correspondente e com restrição de redistribuição; apagado |

**Nenhum código da matriz alterado.** K7 M1 e K7 M4 continuam pendentes: nenhum arquivo do lote trata da identificação
Friedrichs = Dirichlet com espectro discreto nem da genericidade dos comprimentos em bilhares. Dados de controle (B1, B2)
continuam não obtidos.

## 12. Material gerado por outro assistente (pasta `kimi/`, 17/09/2026) — avaliação

A pasta `kimi/` contém três arquivos produzidos por outro assistente de IA, **sem código, manifesto ou hashes de
execução**. Pelas regras do projeto, não entram como dados nem como fontes; foram conferidos só como indicações. A pasta
foi **apagada pelo usuário** após esta avaliação; nenhum desses dados foi incorporado ao projeto.

| Item | O que foi indicado | Conferência feita | Resultado |
|---|---|---|---|
| **K7 M1** | Friedrichs de −Δ em C_c^∞(Ω) = laplaciano de Dirichlet; resolvente compacto; espectro discreto. Refs.: Reed–Simon Thm X.23; Davies 1995; Pankrashkin, "Prop. 3.32" | Baixadas e lidas as notas de Pankrashkin (Oldenburg 2020, `pankrashkin_2020_spectral_oldenburg.pdf`): **Ex. 2.10** (p. 19): A₀ gerado pela forma ∫∇u·∇v com domínio H₀¹(Ω), fecho de C_c^∞(Ω), é o laplaciano de Dirichlet; **Def. 2.13** (p. 21): extensão de Friedrichs = operador gerado pelo fecho da forma a partir do domínio original; **Prop. 3.30**: Ω limitado ⇒ H₀¹(Ω) ↪ L²(Ω) compacto e T_D com resolvente compacto (via **Teor. 3.24**); **Prop. 3.23** (p. 35): semilimitado com resolvente compacto ⇒ espectro só de autovalores de multiplicidade finita, λ_n → ∞ | **Confere**, com correções: a proposição certa é a **3.30** (a 3.32 trata do laplaciano de **Neumann** em domínios de extensão); não é preciso fronteira Lipschitz para Dirichlet. Nota: o Ex. 3.29 das notas troca os domínios de t_D e t_N em relação ao Ex. 2.10 (erro tipográfico da fonte). Reed–Simon e Davies **não** foram lidos |
| **K7 M4** | Petkov–Stojanov (via Bessa et al., GAFA 2024, "Thm 2.8"): em conjunto residual de corpos convexos, órbitas periódicas não degeneradas e sem pontos de reflexão compartilhados | resumo do arXiv:2201.01362 lido (conjunto C² aberto e denso de corpos convexos com fronteira suave; entropia topológica positiva); Thm 2.8 **não** lido | **Não resolve K7 M4**: (i) o resultado é sobre **corpos convexos de fronteira suave genéricos**; o estádio não é genérico nem tem fronteira C²; (ii) genericidade de órbitas não demonstra que os comprimentos evitem r·log p; (iii) a fórmula de traço de bilhares é semiclássica, então não há igualdade exata a comparar |
| **B1** (níveis do estádio) | 200 autovalores de Dirichlet do estádio γ = 1 (área 4 + π) por diferenças finitas de 5 pontos com extrapolação de Richardson; "precisão ~10⁻² em n = 200" | Contagem compatível com Weyl (N̄(377,66) ≈ 214,6 − 15,9 ≈ 199) | **Não serve como dado de controle**: (i) erro relativo declarado 10⁻² em λ ≈ 378 dá ≈ 3,8, maior que o espaçamento médio 4π/Área ≈ 1,76, o que inviabiliza estatística de níveis; (ii) 200 níveis contra os milhares por bloco usados no instrumento; (iii) diferenças finitas com fronteira curva têm erro de fronteira de ordem h, o que torna a extrapolação em h² sem justificativa; (iv) sem código nem setor de simetria declarado |
| **B2** (triângulo modular) | 10 parâmetros espectrais r_j de formas de Maass (Booker–Strömbergsson–Venkatesh; LMFDB) e 28 linhas "t, D = t² − 4, h⁺(D), comprimento" | r₁ = 9,5336952614 dá λ₁ = 91,1413 (aritmética confere); LMFDB bloqueou o acesso automático (captcha), valores **não conferidos na fonte**. Comprimentos 2 log((t + √(t² − 4))/2): conferidos (t = 3, 4, 20). Números de classe estreitos h⁺(D) de formas **primitivas**: **conferidos** por contagem independente de ciclos de formas reduzidas (Zagier) para t = 3…30 (controles h⁺(5) = 1, h⁺(8) = 1, h⁺(12) = 2, h⁺(13) = 1, h⁺(21) = 2) | **Correto como números de classe, errado como multiplicidade de geodésicas**: o número de classes de conjugação de SL(2,ℤ) com traço t inclui formas **não primitivas** (ordens de condutor f com f² ∣ D) e difere de h⁺(D) em 15 dos 28 traços (ex.: t = 6: 3, não 2; t = 30: 14, não 8). Parte dessas classes são potências de elementos primitivos (ex.: t = 7 é o quadrado de t = 3), logo a coluna "geodésicas primitivas" também está mal rotulada. 10 autovalores sem paridade (par/ímpar) não servem para estatística nem para o controle |

**Consequências.**
- **K7 M1:** `S/PC` → **`S/conferido`**, aplicado em 17/09/2026 com aprovação do usuário (E-K7-M1).
- **K7 M4:** continua PC.
- **B1 e B2:** continuam sem dados utilizáveis. A contagem exata de classes por traço (feita aqui para t ≤ 30, por
  ciclos de Zagier) é um ponto de partida para o lado geométrico do controle aritmético, mas exige declaração prévia,
  código registrado e separação entre elementos primitivos e potências antes de qualquer uso.

## 13. Dados de autovalores de Maass do LMFDB (19/09/2026) — registro de procedência

**Arquivo:** `Mass-Forms/lmfdb_maass_rigor_0919_1121.txt` (obtido pelo usuário; SHA-256 `f4ca1d21…`, 283.876 bytes; ainda
fora do git). Cabeçalho do próprio arquivo: "Maass forms downloaded from the LMFDB on 19 September 2026", consulta
`{'level': 1}` em https://www.lmfdb.org/ModularForm/GL2/Q/Maass/?level=1, **2.202 formas**. Campos: rótulo, nível, peso,
caractere, parâmetro espectral R (λ = ¼ + R²), simetria, Fricke; definições no fim do arquivo.

**Conferências feitas (classe B):**
- 2.202 linhas de dados; todas com nível 1, peso 0 e caractere trivial; R crescente, sem repetição; 93 ou mais dígitos
  por valor; R de 9,5336952614 a 184,9239502919.
- Simetria: 1.110 com valor 0 e 1.092 com valor 1. A definição no arquivo diz "par se f(−z̄) = f(z), ímpar se
  f(−z̄) = −f(z)", mas não diz qual código é qual. **Mapeamento conferido (19/09/2026, classe B):** 1 = ímpar e 0 = par.
  As páginas individuais do LMFDB (espelho https://beta.lmfdb.org, lidas nesta data) dão "Symmetry: odd" para 1.0.1.1.1
  (R = 9,53369526…, código 1 no arquivo) e 1.0.1.2.1 (R = 12,17300832…, código 1), e "Symmetry: even" para 1.0.1.3.1
  (R = 13,77975135…, código 0). Os R das páginas coincidem com os do arquivo em todos os dígitos exibidos. SHA-256 das
  páginas salvas (HTML, só como registro de conferência; não versionadas): `2df60072…`, `7af79c20…`, `78fae3a8…`.
- Completude: não verificada. A contagem sobe para ~0,78 de T²/12 em T = 184, o que é compatível em ordem de grandeza
  com um segundo termo negativo do tipo T log T na lei de Weyl de PSL(2,ℤ) (Iwaniec, notas, p. 9), mas isso **não** é
  prova de completude.
- **Licença de redistribuição do LMFDB (conferida em 19/09/2026, https://beta.lmfdb.org/license, SHA-256 da página
  `21e14d60…`):** "The database underpinning the LMFDB is licensed under the Creative Commons Attribution-ShareAlike 4.0
  International License (CC-BY-SA)"; o código do site é GPL v2. Consequência: o arquivo **pode** ser redistribuído no
  repositório, desde que mantenha atribuição, indicação da licença CC BY-SA 4.0 e que o próprio arquivo (e derivados
  diretos dos dados) continue sob CC BY-SA 4.0. O código do projeto continua MIT; a licença dos dados vale só para os
  dados. Citação pedida pela página https://beta.lmfdb.org/citation (SHA-256 `4f402911…`): "The LMFDB Collaboration,
  *The L-functions and modular forms database*, https://www.lmfdb.org, <ano>, [Online; accessed <data>]". A decisão de
  versionar é do usuário.

**Referência indicada pelo usuário, conferida no arXiv:** a citação "H. Then (2005), *Arithmetic quantum chaos for the
modular group*, Math. Proc. Camb. Phil. Soc. 138, 183–202, arXiv:math-ph/0305047" **mistura dois trabalhos**:
- arXiv:math-ph/0305047 é H. Then, *Maass cusp forms for large eigenvalues*, Math. Comp. 74 (2005) 363–381 (resumo: dois
  autovalores acima de R = 40.000; sem tabela dos primeiros autovalores);
- arXiv:math-ph/0305048 é H. Then, *Arithmetic quantum chaos of Maass waveforms*, em *Frontiers in Number Theory, Physics,
  and Geometry I* (2006) 183–212 (resumo: espaço hiperbólico **tridimensional**).
A "tabela canônica dos primeiros 5.000 autovalores" não foi localizada nesses resumos.

**Uso:** estes dados cobrem o lado espectral do controle aritmético (item B2), com paridade. Nenhum uso antes de uma
declaração prévia do controle, que deve fixar setor de simetria, faixa, unfolding (lei de Weyl de PSL(2,ℤ) com fonte) e
a predição geométrica (comprimentos e multiplicidades por traço, calculados exatamente).

## 14. Níveis do estádio (item B1) — conferência das indicações (19/09/2026)

| Indicação | Conferido | Resultado |
|---|---|---|
| Setores de simetria do estádio (C₂ᵥ): par-par = Neumann nos eixos de corte e Dirichlet na fronteira externa; ímpar-ímpar = Dirichlet em todas as bordas do quarto de estádio | argumento elementar: função par em relação a um eixo tem derivada normal nula nele; ímpar anula-se nele | **correto** |
| MPSpack (github.com/ahbarnett/mpspack) | página do repositório | código **MATLAB** (GPL v3), "legacy code; barely supported", versão 1.41 (31/05/2023); **sem tabelas de autovalores**; não há MATLAB/Octave nesta máquina |
| Página de A. Bäcker (physik.tu-dresden.de/~baecker) | páginas "home" e "computing" | redireciona para a nova página; menciona código em Python só para mapas quânticos; **nenhuma tabela nem código de bilhares** encontrado |
| Pacote `vergini` de A. Barnett | https://users.flatironinstitute.org/~ahb/software/ (a URL indicada, `.../software.html`, dá 404); `README.vergini` lido; `vergini.tar.gz` baixado (SHA-256 `1da91d3b…`, 61.635 bytes; fora do repositório) | **útil**: código **C++** (g++, BLAS, LAPACK, GSL, OpenMP opcional) do método de escala de Vergini–Saraceno, com o quarto de estádio embutido (`-l qust:2`, "quarter of the 2x4 stadium") e base plano-onda + evanescente de simetria ímpar-ímpar (`-s vepwoo:…`); calcula autovalores numa janela estreita de k por chamada; o README não declara licença e diz que o erro é estimado pela "tension", **sem análise de erro** para o método de escala |
| Alt et al. 1999, PRE 60, 2851 | versão arXiv chao-dyn/9906032 já registrada (§10) | compara 955 ressonâncias experimentais com cálculo numérico; **não** traz tabela longa de níveis |

**Conclusão:** não há tabela pública de níveis do estádio obtida até agora; o caminho viável é **calcular** os níveis do setor
ímpar-ímpar com `vergini`. Pré-requisitos: bibliotecas de desenvolvimento (GSL, LAPACK/BLAS) instaladas pelo usuário, compilação
local, piloto de convergência (base e discretização) e **declaração prévia** do controle B1 (setor, faixa de k, critério de
completude pela lei de Weyl com os termos de área e perímetro, tolerância de precisão, predição dos comprimentos de órbitas
periódicas) antes de produzir dados para o instrumento. O código não entra no repositório (licença não declarada); só URL e
hash.

**Compilação e teste de funcionamento (19/09/2026, executados pelo usuário; classe B, sem valor de critério):** `vergini`
compilado em `~/vergini_build/vergini` (fora do repositório) com o Makefile original (`linux-gnu-openmp`; só avisos
`-Wwrite-strings`). Teste com o exemplo do README em k = 100: `verg -l qust:2 -s vepwoo:1.3:10:1.5 -u -4 5 -b 10 -k 100
-V 0.2 -o teste100`. Resultado: 11 estados em [99,8; 100,2], todos mantidos como não espúrios. O programa informa área
1,7854, "perim" 2,5708 (só a fronteira externa, 1 + π/2; os eixos entram pela base ímpar-ímpar) e espaçamento de Weyl de
primeira ordem 0,0352. Estimativa independente, com Dirichlet em todo o contorno do quarto (P = 4 + π/2): densidade
≈ A·k/(2π) − P/(4π) ≈ 27,97 por unidade de k, ou seja **≈ 11,2 níveis na janela**, compatível com os 11 encontrados.
"Tension" de 6·10⁻⁹ a 5·10⁻⁸ no centro da janela, subindo para 1,5·10⁻⁵ e 2,1·10⁻⁵ nas bordas. Se a tension for de fato
≈ (erro em k)², como diz o README, que não traz análise de erro, os erros iriam de ~10⁻⁴ no centro (~0,3% do espaçamento)
a ~4,5·10⁻³ nas bordas (~13% do espaçamento). Consequência para a declaração do B1: usar janelas sobrepostas e aproveitar
só a parte central de cada uma, fixar um limite de tension e fazer um piloto de convergência (variando `-b` e o
parâmetro η da base) antes de qualquer dado para o instrumento.

## 15. Página "Weil's Explicit Formula" (researchai.dev), indicada pelo usuário (19/09/2026) — avaliação

**Página:** https://www.researchai.dev/resources/Weil%27s%20Explicit%20Formula/ (HTML lido em 19/09/2026, SHA-256
`9c051f93…`, não arquivado). É parte de um painel de pesquisa automatizada ("NGUYEN-RH-1", com seções "Conversations",
"Lean Proofs" e "Graveyard"), sem autor humano identificado nem referência de página para os enunciados. **Não é fonte**
pelas regras do projeto: é texto secundário com indício de geração por IA e não contém o texto de Weil. A própria página
diz, sobre Weil 1952: "No public scan; accessible via the Collected Works". **F5 continua pendente.**

**Pistas bibliográficas (dados a conferir na fonte antes de qualquer uso):**
- K. Barner (1981), *On A. Weil's explicit formula*, J. reine angew. Math. 323, 139–152, que a página diz trazer as
  condições mínimas de regularidade da função-teste. EuDML (https://eudml.org/doc/152356) respondeu 403 nesta sessão.
  Se lido, pode servir a F5 como enunciado **incondicional** moderno; o que temos hoje (Carneiro–Chandee–Milinovich,
  Lema 5) é só sob RH;
- A. P. Guinand (1948), *A summation formula in the theory of prime numbers*, Proc. London Math. Soc. (2) 50, 107–119,
  doi:10.1112/plms/s2-50.2.107;
- A. Weil (1972), *Sur les formules explicites de la théorie des nombres*, Izv. Akad. Nauk SSSR Ser. Mat. 36, 3–18;
- Iwaniec & Kowalski, *Analytic Number Theory* (AMS, 2004), cap. 5, que a página diz ser o "Theorem 5.12".

**Observação:** a forma da fórmula na §1 da página, com f̂(ξ) = ∫f e^{iξx}, polos f̂(±1/2i) e termo arquimediano
Re ψ(¼ + it/2) − log π, é compatível na estrutura com o Teorema 6 de Connes já conferido. A página não é usada para
nada.

## 16. Weil (1952), *Sur les "formules explicites"…*: transcrição conferida (19/09/2026) — F5

**Arquivo:** `archive/fontes_etapa11/transc-Weil-1952.pdf` (enviado pelo usuário; SHA-256 `1edd4a83…`, 301.266 bytes,
11 páginas; não versionado). É uma **transcrição em LaTeX** feita por Denise Vella-Chemla (dezembro de 2020), **não** um
fac-símile. Não marca as páginas originais (Comm. Sém. Math. Univ. Lund, volume dedicado a M. Riesz, 1952, pp. 252–265),
então as referências abaixo usam a paginação da transcrição. Há erros de digitação visíveis ("diserète", "δx" no lugar
de δ_χ, "[γ| < T"), que não mudam o conteúdo matemático lido. **Classe B de fonte:** leitura do texto de Weil, com a
ressalva da transcrição.

**O que o texto diz (lido):**
- p. 4: Φ(s) = ∫ F(x)e^{(s−½)x} dx. As hipóteses preliminares são F(x)e^{(½+a′)|x|} ∈ L¹ e Φ(s) = o((log|t|)⁻²) na faixa
  −a ≤ σ ≤ 1 + a.
- p. 6, hipóteses definitivas:
  - **(A)** F contínua e continuamente diferenciável, exceto num número finito de pontos com descontinuidade de primeira
    espécie de F e F′, onde F vale a média dos limites laterais;
  - **(B)** existe b > 0 com F(x) e F′(x) = O(e^{−(½+b)|x|}).
- pp. 8–9, fórmula (11), "le résultat définitif": sob (A) e (B), a soma Σ Φ(ω) sobre os zeros ω = β + iγ de L(s) com
  0 ≤ β ≤ 1 e |γ| < T tem limite quando T → ∞, igual a:
  - δ_χ∫F(x)(e^{x/2} + e^{−x/2})dx;
  - mais F(0) log A;
  - menos a soma sobre p e n de (log Np/Np^{n/2})[χ(p)ⁿF(log Npⁿ) + χ(p)⁻ⁿF(log Np⁻ⁿ)];
  - menos Σ_λ PF∫F(x)e^{iφ_λx}K_{η_λ,f_λ}(x)dx.
- **O enunciado não supõe RH.** A soma é simétrica em |γ| < T, e os zeros são contados sem supor β = ½.
- p. 9, lema: RH para L(s) equivale à positividade de (11) para todo F = F₀ ∗ F₀(−x), com F₀ satisfazendo (A) e (B).

**Consequência para F5 e L-EF1 (classe B, comparação feita nesta data):** com Φ(½ + ir) = ∫F(x)e^{irx}dx = h(r),
a função F de Weil é a g do projeto.
- **Gaussianas da checagem de L-EF1** (g = soma de gaussianas deslocadas): g e g′ decaem mais rápido que qualquer
  exponencial, e g é C^∞. Portanto **(A) e (B) valem** e o teorema de Weil se aplica diretamente.
- **h_ε = k_t ∗ φ_ε com ε > 0 (L-EF2b):** g_{h_ε}(u) = g_{k_t}(u)e^{−ε²u²/2}, com g_{k_t} inteira e derivadas limitadas
  (ETAPA11_3B_ADMISSIBILIDADE, tabela da §6). Então g e g′ = O(e^{−cu²}), **(A) e (B) valem** e o teorema de Weil se
  aplica diretamente.
- **Classe 𝒜 do projeto:** (A1) dá só integrabilidade de e^{|x|/2}g^{(j)}, e não a cota pontual de g′ exigida em (B).
  Portanto 𝒜 **não** está contida, em geral, na classe (A)+(B) de Weil. Isso não afeta o projeto: a admissibilidade de
  𝒜 foi derivada a partir do Teorema 6 de Connes (conferido), e as funções efetivamente usadas estão nas duas classes.
- **Janela de Hann sem suavização:** continua fora, como já registrado.
- **Não feito:** a identificação termo a termo das constantes de (11), com k = ℚ e χ = χ₀ (em que A = (2π)⁻¹,
  K_{1,0}(x) = e^{x/2}/|eˣ − e⁻ˣ| e δ_χ = 1), com o termo arquimediano de Connes usado em L-EF1. Se for necessária, é
  uma derivação a registrar à parte; F5 pede a **classe** de funções-teste, e essa ficou conferida.

**Situação de F5:** conferida na transcrição. Ler o fac-símile do original (ou das *Œuvres Scientifiques* II) continua
**desejável** para eliminar a ressalva da transcrição, mas deixa de bloquear qualquer item.

## 17. Contribuição "bouncing ball" (Sieber et al. 1993) — pistas conferidas (19/09/2026)

**Original:** M. Sieber, U. Smilansky, S. C. Creagh & R. G. Littlejohn, *Non-generic spectral statistics in the quantized
stadium billiard*, J. Phys. A 26 (1993) 6217–6230, doi:10.1088/0305-4470/26/22/022. Atrás de paywall (IOP); **não lido**.
Continua desejável por acesso institucional.

**Resumo de pistas trazido pelo usuário (gerado por outro assistente), conferido na fonte:**
- "arXiv:0804.1551 (Dietz et al.) segue Sieber et al. para a contagem bouncing ball no estádio 2D": **incorreto.**
  - O artigo (B. Dietz, B. Moessner, T. Papenbrock, U. Reif & A. Richter, *Bouncing ball orbits and symmetry breaking
    effects in a three-dimensional chaotic billiard*, PRE 77, 046221 (2008); PDF SHA-256 `1be2d025…`, não arquivado)
    diz "We follow Ref. [15]", e a ref. [15] é **H. Alt et al., Phys. Rev. E 54, 2303 (1996)**, não Sieber et al.
  - A fórmula, eq. (4), é para o bilhar **tridimensional** (dois quartos de cilindro), não para o estádio 2D.
  - Não usado.
- "*On the number of bouncing ball modes in billiards*, página em people.maths.bris.ac.uk": **não localizado.** A busca no
  arXiv por título achou só trabalhos relacionados, entre eles S. Löck, A. Bäcker & R. Ketzmerick, *Coupling of
  bouncing-ball modes to the chaotic sea and their counting function*, PRE 85, 016210 (2012), arXiv:1110.6307v2 (PDF
  SHA-256 `ddcc7e06…`, não arquivado). Esse artigo trata da contagem N_bb(E) ∼ E^δ de **modos**, não da amplitude da
  linha no traço; fica como referência futura.

**Fonte útil encontrada nesta conferência (classe A secundária, lida):** G. Tanner, *How chaotic is the stadium
billiard? A semiclassical analysis*, arXiv:chao-dyn/9610013v1 (1996); arquivo
`tanner_1996_arXiv_chao-dyn-9610013v1.pdf`, SHA-256 `f7b3db4d…`, no manifesto. Na §2 (PDF pp. 3–4), "following Ref.
[22, 23]", sendo [22] Sieber et al. 1993 e [23] Alonso & Gaspard, J. Phys. A 27, 1599 (1994), para o **quarto de
estádio**, com a = comprimento do retângulo e b = raio:
- eq. (3): traço da função de Green da parte bouncing ball, com Σ H₀⁽¹⁾(2bkn);
- eq. (4)–(5): traço integrado Ig_bb(k) = B_bb(k²) − iπN̄_bb(k) − i(a/2)√(k/πb) Σ_{n≥1} n^{−3/2} e^{2ikbn − 3iπ/4}, na forma
  assintótica das funções de Hankel;
- eq. (8): N̄_bb(k) = ab k²/4π − 2a k/4π.

**Consequências para `ctrl-estadio-v1` (classe B, comparação feita nesta data):**
1. Com N = −(1/π) Im Ig, a parte oscilante é N_osc^bb(k) = (a/2π)√(k/πb) Σ n^{−3/2} cos(2kbn − 3π/4). Com b = 1, o
   prefator coincide com o da eq. (53) de Bäcker, a√k/(2π^{3/2}), e a fase é **2kbn = 2kn**, com o raio b e não o
   comprimento a. Isso confirma a leitura da declaração (P1): o "2an√E" extraído da eq. (53) de Bäcker não vale em geral
   e coincide com a forma correta só porque a = b = 1 no nosso bilhar.
2. As condições de contorno não aparecem escritas no texto de Tanner. O termo −2a k/4π da eq. (8) corresponde a Dirichlet
   nas duas paredes paralelas do retângulo (y = 0 e y = b), que é o caso do setor ímpar-ímpar. Isso é **inferência**, a
   registrar na derivação D1-E.
3. A fórmula é **assintótica** e vale só para a família (Tanner, §2: "The bouncing ball part does, however, not
   contribute to individual eigenvalues"; §§3–4 tratam das órbitas instáveis próximas da família, que Gutzwiller não
   descreve). Isso sustenta tratar a tolerância de 10% de E-C2bb como convenção, não como cota.

## 18. Sexto lote enviado pelo usuário (19/09/2026, 10:20–10:40) — conferência

Cinco PDFs em `archive/fontes_etapa11/`. Os quatro úteis estão no manifesto; os arquivos não entram no git.

| Arquivo | Obra | Conferido | Uso |
|---|---|---|---|
| `CM_1986__58_2_209_0.pdf` (`98150bde…`) | J.-F. Mestre, *Formules explicites et minorations de conducteurs de variétés algébriques*, Compositio Math. 58 (1986) 209–232 (Numdam) | §I.2, pp. 212–213 (lidas na imagem da página, porque as fórmulas não saem no texto extraído) | **útil (F5).** Enunciado **incondicional** da fórmula explícita para funções L com equação funcional, incluindo as de Dirichlet. Hipóteses: (i) F(x)e^{(½+c+ε)x} somável; (ii) F(x)e^{(½+c+ε)x} de variação limitada, com valor médio nos saltos; (iii) (F(x) − F(0))/x de variação limitada. Σ_ρ Φ(ρ) entendido como lim_{T→∞} Σ_{\|Im ρ\|<T}. "La démonstration est calquée sur celle de [10]" |
| `RLIN_2000_9_11_3_183_0.pdf` (`20bd544f…`) | E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I*, Rend. Mat. Acc. Lincei (9) 11 (2000) 183–233 (BDIM) | §2, p. 186 | **útil (constantes).** Fórmula explícita de Guinand–Weil para ζ, para f ∈ C_c^∞((0, ∞)) em forma de Mellin, com constantes explícitas (log 4π + γ) e a forma alternativa com Γ′/Γ e log π. A classe é estreita (suporte compacto), mas serve para conferir constantes do termo arquimediano, se essa derivação for feita |
| `1112.5665v1.pdf` (`58162089…`) | A. Barnett & A. Hassell, *Fast computation of high frequency Dirichlet eigenmodes via the spectral flow of the interior Neumann-to-Dirichlet map*, arXiv:1112.5665v1 | introdução, p. 3; §7, pp. 31–32 | **útil (B1).** Sobre o método de escala de Vergini–Saraceno, que é o do `vergini`: o erro absoluto em k é empiricamente O(ε³), com ε a distância ao centro da janela ("not the O(ε⁴) claimed in [61]"), e "the error analysis of the scaling method … is very primitive, and certainly no rigorous results exist" (p. 3). Com base plana, o método parece exigir domínio convexo (p. 31); o quarto de estádio é convexo |
| `a71915.pdf` (`33213269…`) | A. Bäcker, R. Schubert & P. Stifter, *On the number of bouncing ball modes in billiards*, J. Phys. A 30 (1997) 6783–6795 | resumo; p. 6789 | **contexto.** Conta os **modos** bouncing ball, N_bb(E) ∼ αE^δ com δ = 3/4 no estádio (p. 6789, atribuído a [7]). Não dá a amplitude da linha no traço; **não** é usado na D1-E |
| `0804.1551v1.pdf` (`1be2d025…`) | Dietz et al. 2008 (bilhar 3D) | já avaliado na §17 | **não ajuda** (3D; ref. [15] = Alt et al. 1996). Fora do manifesto; pode ser apagado |

**Consequências:**
1. **F5 e L-EF1:** Mestre (1986) dá um segundo enunciado incondicional publicado, com hipóteses de variação limitada,
   mais fracas que (A) e (B) de Weil. As gaussianas e h_ε (ε > 0) satisfazem (i)–(iii) com c = 0: g e g′ decaem mais
   rápido que qualquer exponencial, e (g(x) − g(0))/x é suave com derivada integrável. A classe 𝒜 do projeto cumpre (i)
   e (iii), mas (ii) exigiria e^{(½+ε)|x|}g′ ∈ L¹, e (A1) dá só e^{|x|/2}g′ ∈ L¹. É a mesma conclusão da §16: as funções
   usadas estão cobertas, e 𝒜 continua justificada pelo Teorema 6 de Connes.
2. **`ctrl-estadio-v1`:** Barnett & Hassell dão apoio de fonte ao desenho da declaração (§4): aproveitar só o miolo
   |k − K0| ≤ 0,1 de janelas de meia-largura 0,2 reduz o erro empírico em cerca de (0,2/0,1)³ = 8 vezes em relação às bordas.
   O limite de tension e o piloto E2 continuam sendo convenções empíricas, porque não há cota rigorosa.

## 19. `houches.pdf` (enviado pelo usuário, 19/09/2026) — cópia repetida; releitura para a questão sinh × cosh

`archive/fontes_etapa11/houches.pdf` tem o **mesmo SHA-256** (`ab4531e6…`) que
`bogomolny_2003_quantum_arithmetical_chaos_HAL-00000984v1.pdf`, já arquivado: E. Bogomolny, *Quantum and Arithmetical
Chaos* (notas de Les Houches, 103 pp.). Não é fonte nova; a cópia repetida pode ser apagada.

**Releitura dirigida ao ponto aberto de `ctrl-maass-v1`** (amplitude das órbitas com det = −1: sinh ou cosh):
- **p. 38 (lido):** na dedução da fórmula de Gutzwiller em duas dimensões, a contribuição de uma órbita tem amplitude
  T_p/(πħ|m₁₁ + m₂₂ − 2|^{1/2}), e a forma geral é 1/|det(M_p^n − 1)|^{1/2}, com M a matriz de monodromia (det M = 1).
  É a mesma estrutura de BK (2.9), p. 241.
- **Consequência (derivação, não citação):**
  - se a monodromia tem autovalores e^{±l} (órbita comum, traço > 2), então |Tr M − 2| = 4 sinh²(l/2);
  - se tem autovalores −e^{±l} (traço < −2, "inversa hiperbólica"), então |Tr M − 2| = 4 cosh²(l/2).

  A fonte dá a fórmula geral. **Falta com fonte** o passo "órbita com número ímpar de reflexões no triângulo modular ⇒
  monodromia inversa hiperbólica", que é o argumento geométrico de H_cosh (inversão da orientação transversal). Esse
  passo fica para a derivação D1-M.
- **Nas pp. 94–97 (triângulos de Hecke) não há** fórmula de traço com os termos de reflexão.
- **Situação:** H_cosh ganha apoio de fonte na parte geral (p. 38) e continua dependendo de um passo derivado. A fonte
  direta (Venkov; Bogomolny–Georgeot–Giannoni–Schmit 1997) continua pendente. A declaração `ctrl-maass-v1` não muda.

## 20. Amplitude das órbitas com reflexão (sinh × cosh) — resolvida com fontes lidas (19/09/2026)

**Origem:** o usuário trouxe um resumo gerado por outro assistente afirmando H_cosh, com citações de Bolte & Steiner
(1993, eq. 13) e de "Venkov, Teorema 2.2, p. 137". Conferido na fonte:

| Afirmação do resumo | Conferido |
|---|---|
| Bolte & Steiner, CMP 156 (1993) 1–16 | **existe** (Crossref, doi:10.1007/BF02096730). Preprint DESY 90-082 obtido do INSPIRE e **lido na imagem**: Teorema, eq. (13), p. 6 |
| forma do termo de reflexão | **confere**: −Σ_{ρ_p} Σ_{k≥0} l(ρ_p²)/(4 cosh[(k + ½) l(ρ_p²)/2]) · g((k + ½) l(ρ_p²)), com Dirichlet |
| "Venkov (1990), Teorema 2.2, p. 137" | **atribuição trocada:** o "Theorem 2.2 [55]" é de **Bolte & Grosche** (preprint DESY 92-118, pp. 8–9, eq. (2.31)), que o atribuem a Venkov [55]. Venkov não foi lido |
| BLS "desprezando a diferença entre 2 cosh L e e^L", p. 13 | a frase existe ("Neglecting the difference between 2 cosh L and e^L"), mas está na **p. 12** do preprint, na §2 (grupo modular sem reflexões). A leitura de que a §6 (pp. 33–34) usa a mesma aproximação é **plausível, mas não está escrita** |
| "a medição será comprovação empírica de alta precisão" | **exagero:** só com os dados se sabe se o ruído do bloco permite distinguir as hipóteses (declaração §5) |

**O que as fontes lidas estabelecem:**
- **Bolte & Steiner, eq. (13), p. 6:** para superfícies de Riemann compactas com bordo e condição de Dirichlet, as
  classes hiperbólicas contribuem com +l(γ) g(k l(γ))/(4 sinh(k l(γ)/2)), e as reflexões com deslizamento primitivas ρ_p
  (e suas potências ímpares) com **−l(ρ_p²) g((k + ½) l(ρ_p²))/(4 cosh[(k + ½) l(ρ_p²)/2])**, com k ≥ 0. Observação 2 na
  mesma página: para Neumann, o sinal muda.
- **Bolte & Grosche, Theorem 2.2 [55], eq. (2.31), pp. 8–9:** a mesma estrutura, para superfícies com bordo
  **arbitrárias**, incluindo classes elípticas (cantos) e parabólicas (cúspides). O termo de reflexão é
  −Σ_{ρ_p, tr ρ ≠ 0} Σ_{k≥1} l_{ρ²} g[(k − ½) l_{ρ²}] / (4 cosh ½(k − ½) l_{ρ²}); o termo de área é A(F̂)/(8π)∫ p tanh(πp) h(p) dp;
  e os termos elípticos, parabólicos e de reflexões puras (tr ρ = 0) **não** são linhas em t > 0, só termos suaves ou em
  g(0). Isso **confirma a suposição P1** de `ctrl-maass-v1` sobre os "corner and horn" terms.
- **H_cosh está confirmada por fonte lida.** Para a reflexão primitiva de comprimento de translação l_ρ = ½ l(ρ²), o
  peso é l(ρ²)/(4 cosh(l_ρ/2)) = l_ρ/(2 cosh(l_ρ/2)), igual à derivação pela monodromia (§19).

**Consequência que a declaração não previa (normalização):** nas duas fontes, as somas correm sobre classes de
conjugação no grupo **Γ̂ da superfície dobrada**, que no caso modular é PSL(2,ℤ), com peso **1/4** (4 sinh, 4 cosh), e
não sobre classes de PGL(2,ℤ) com peso 1/2 (2 sinh), como na leitura de BLS usada em P2 e P3 de `ctrl-maass-v1`:
- uma classe de PGL(2,ℤ) que se divide em duas classes de PSL(2,ℤ) (órbita e imagem espelhada distintas) contribui
  2 × 1/4 = 1/2, igual a BLS;
- uma classe **autoespelhada** (uma só classe em PSL(2,ℤ)) contribui **1/4**, metade do que P2 previa.

O §4 da declaração já prevê isso ("se a derivação contradisser P2, prevalece a derivação, com adendo antes de qualquer
cálculo"). A **D1-M** vai escrever a normalização a partir de Bolte & Grosche (2.31), e um **adendo** a
`ctrl-maass-v1` vai corrigir P2 e P3 (contagem por classes de PSL(2,ℤ) para δ = +1 e por classes de Γ̂ das reflexões
para δ = −1, com pesos 1/4), antes de calcular G1. A comparação sinh × cosh (M-C2a−) continua descritiva, como foi
declarada; agora ela tem **previsão com fonte**: H_cosh.

## 21. Sétimo lote enviado pelo usuário (19/09/2026, ~13:10) — conferência

| Arquivo | Obra | Conferido | Uso |
|---|---|---|---|
| `0812.4382v1.pdf` (`12cf4929…`) | L. A. Forte, *Arithmetical chaos and quantum cosmology*, arXiv:0812.4382v1 | p. 16; pp. 18–19 | **útil em parte (secundária).** p. 16: "the spectrum of Δ on PSL(2, ℤ) is purely discrete on the space of odd functions, but on the even space there is a continuous spectrum given by the interval [¼, ∞)". Dá apoio de fonte ao argumento elementar do §3 de `ctrl-maass-v1` (setor ímpar sem espectro contínuo). **Não usado:** a lista das pp. 18–19 ("E₁ = 91,12, E₂ = 148,43, E₃ = 190,13, E₄ = 206,16. They are respectively even, odd, odd, even and odd") tem 5 rótulos para 4 valores e chama de par o primeiro autovalor (R = 9,5326), que o LMFDB dá como **ímpar** (conferido nas páginas, §13). Além disso, E₄ corresponde a R = 14,3496, contra 14,3585 no LMFDB. As paridades do LMFDB, conferidas diretamente, prevalecem |
| `ArithmeticQuantumChaos.pdf` (`5453881a…`) | J. Marklof, *Arithmetic quantum chaos* (verbete para a Encyclopedia of Mathematical Physics, versão do autor) | p. 4, eqs. (23)–(26) | **útil (secundária).** Na superfície modular, 2 cosh(ℓ/2) = \|tr γ\| e os comprimentos distintos são {2 arcosh(n/2) : n ≥ 3}. Confere a parte δ = +1 de P1 |
| `0312061v1.pdf` (`030adc71…`) | Bogomolny, *Quantum and Arithmetical Chaos*, arXiv:nlin/0312061v1 | comparação de texto | **repetida:** mesmo texto que a cópia do HAL e `houches.pdf`, com diferenças só de formatação. Pode ser apagada |
| `P_00_83.pdf` (`8c6d8da7…`) | T. Damour & M. Henneaux, *E10, BE10 and arithmetical chaos in superstring cosmology*, IHES/P/00/83, hep-th/0012172 | resumo e busca | **não ajuda** nos controles: bilhares cosmológicos em dimensão 9, sem fórmula de traço nem espectro. Pode ser apagado |

**Limpeza (19/09/2026, a pedido do usuário):** foram apagadas as cópias locais dos textos avaliados como sem uso:
`houches.pdf` e `0312061v1.pdf` (cópias repetidas das notas de Bogomolny, §§19 e 21), `P_00_83.pdf` (Damour &
Henneaux, §21) e `0804.1551v1.pdf` (Dietz et al., §§17–18). Os hashes continuam nas seções citadas. Nenhum constava do
manifesto.
