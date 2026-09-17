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
| F5 | Classe de funções-teste da fórmula explícita: Weil (1952) ou enunciado moderno (por exemplo, Carneiro–Chandee–Milinovich, arXiv:1309.1526, Lema 5) | hipóteses de h e g em L-EF1; admissibilidade de h_ε | L-EF1; L-EF2b | `bloqueado` para Weil 1952; **enunciado moderno sob RH lido** em 17/09/2026 (§5) | arXiv recusado; fonte de Weil não localizada em servidor acessível | parcial: Carneiro–Chandee–Milinovich, Lema 5 (arXiv v1, pp. 6–7), só sob RH |
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
