# Etapa 11.3b — registro de fontes e hipóteses pendentes

**Data:** 14/09/2026, 09:28. **Estado da 11.3b:** `em execução`. Os itens de fonte abaixo estão `bloqueado` por acesso
de rede nesta sessão, não por decisão metodológica.

**Uso:** a seleção de candidatos e o congelamento de testes esperam as evidências pertinentes. Nenhum item abaixo
pode ser tratado como conferido enquanto a coluna "Conferido" disser "não". Mais casos numéricos não substituem
estas justificativas.

## 1. Pendências prioritárias (fórmula explícita e instrumento)

| ID | Fonte ou hipótese | Para que serve | Onde é usada | Situação | Tentativas de acesso (14/09/2026) | Conferido |
|---|---|---|---|---|---|---|
| F1 | Platt & Trudgian (2021), *The Riemann hypothesis is true up to 3·10¹²*, Bull. London Math. Soc., doi:10.1112/blms.12460 (arXiv:2004.09765) | criticidade de todos os zeros com 0 < γ ≤ 3·10¹² | L-EF2a(a2) criticidade; L-EF2b (H₀, R_longe); hipótese Σ_ρ h = 2Σ_{γ>0} h da checagem gaussiana; K3a N1–N4 | `bloqueado` | página editorial 403 (curl, WebFetch); arXiv conexão recusada (curl, com e sem sandbox); repositório de Bristol sem resposta (WebFetch); ADS recusado | não. Dados bibliográficos e resumo só por resultado de busca |
| F2 | Simplicidade dos zeros usados (índices ≤ 100.000) | identificar a soma com multiplicidade com a tabela; D_t = ½Σ k_t | L-EF2a(a2), L-EF2b; K3a M6 e N | `bloqueado` | depende de F1 ou de outra verificação publicada (não identificada nesta sessão) | não. A igualdade de contagens (B) é só compatível com simplicidade |
| F3 | Cota explícita de contagem, por exemplo \|S(T)\| ≤ a log T + b log log T + c (Trudgian 2014, J. Number Theory; arXiv:1208.5846), da qual sai N(T) ≤ T² para T ≥ 7·10⁴ | cauda de zeros distantes | L-EF2b R_longe; E_z2 da checagem gaussiana | `bloqueado` para constantes finas de S(T); **uso em R_longe/E_z2 (N(T) ≤ T² para T ≥ 7·10⁴) resolvido por derivação** (ETAPA11_3B_Z1_CONTAGEM §4) | arXiv recusado; ScienceDirect e UNSW recusados; ANU openresearch recusado (WebFetch) | não. Constantes vistas só em resultado de busca, não usadas |
| F4 | N(T) = θ(T)/π + 1 + S(T) contando todos os zeros por Im ρ, sem supor ordenadas reais (Titchmarsh, *The Theory of the Riemann Zeta-Function*, cap. 9) | identidade de Stieltjes incondicional | L-EF2a(a1); plano M3 | `bloqueado` (livro; sem cópia acessível) | DLMF §25.10 arquivada **não** contém a fórmula; BK SIAM p. 239 contém, "for the t_n (assumed real)" | parcial: secundária com ressalva |
| F5 | Classe de funções-teste da fórmula explícita: Weil (1952) ou enunciado moderno (por exemplo, Carneiro–Chandee–Milinovich, arXiv:1309.1526, Lema 5) | hipóteses de h e g em L-EF1; admissibilidade de h_ε | L-EF1; L-EF2b | `bloqueado` como **conferência bibliográfica** do enunciado original. Não é hipótese matemática adicional: o ponto de partida é o Teorema 6 + Lema 3 de Connes, conferidos (ETAPA11_3B_ADMISSIBILIDADE §1a) | arXiv recusado; fonte de Weil não localizada em servidor acessível | não. Connes App. II registra só decaimento de F |
| F6 | Convenção de Frobenius e P₁(T) = det(I − TF \| H¹): Milne, *Lectures on Étale Cohomology*; Deligne, *La conjecture de Weil I* (Publ. IHÉS 43, Numdam) | normalização de C19; C11 | correspondências C11, C19 | `bloqueado` | jmilne.org recusado (curl, WebFetch); Numdam recusado | não |
| F8 | Z1: Σ_ρ 1/(1 + (Im ρ)²) < ∞ | convergência dominada da soma sobre zeros na extensão para 𝒜 | [ETAPA11_3B_ADMISSIBILIDADE.md](ETAPA11_3B_ADMISSIBILIDADE.md) §2 | **resolvida por derivação** ([ETAPA11_3B_Z1_CONTAGEM.md](ETAPA11_3B_Z1_CONTAGEM.md): N(T) ≤ 31 + 5,25·T·log(T+9) via DLMF 25.2.1, 25.2.10 e Jensen) | — | derivação; pendência bibliográfica J1 |
| F9 | Gonek (1993), *An explicit formula of Landau and its applications to the theory of the zeta-function*, Contemp. Math. 143 | rota R2 de H1 | [ETAPA11_3B_H1_FORMULACAO.md](ETAPA11_3B_H1_FORMULACAO.md) §6 | `bloqueado` (acesso) | não tentada individualmente; hosts de editoras e arXiv recusados nesta sessão | não |
| F10 | Fórmula truncada explícita para S(t) (Selberg; Tsang) | rota R3 de H1 | idem | `bloqueado` | não localizada em servidor acessível | não |
| F11 | Forma explícita truncada de ψ(x) ou de Σ Λ(n)n^{−1/2+iτ} com erro explícito (Davenport cap. 17; Montgomery–Vaughan cap. 12) | Lema de Cauda Projetada, Rota B sob RH | [ETAPA11_3B_H1_CAUDA_PROJETADA.md](ETAPA11_3B_H1_CAUDA_PROJETADA.md) II.4 | `bloqueado` (livros; acesso) | não tentada individualmente | não |
| J1 | Fonte arquivada para a fórmula de Jensen (teorema clássico de análise complexa) | Z1; cota N(T) | ETAPA11_3B_Z1_CONTAGEM §§2–3 | pendência **bibliográfica** (não hipótese matemática) | não tentada (livros-texto não acessíveis nesta sessão) | não |
| F7 | Declaração de procedência e completude da tabela `zeros1` (página de Odlyzko) | completude documental da tabela, além da recontagem B | L-EF2a(a2) | `bloqueado` | www-users.cse.umn.edu recusado | não. Recontagem B por `mpmath.nzeros` nos 30 blocos |

**Natureza das pendências (revisão 11.3b-5):**
- **bibliográficas** (conferir fonte original de um enunciado já usado a partir de fonte secundária conferida): F5, J1;
- **hipóteses de fato ainda não sustentadas** por fonte lida ou derivação: F1 (criticidade até H₀), F2
  (simplicidade), F4 (forma incondicional da contagem), F6 (Frobenius), F7 (procedência da tabela).

## 2. Hipóteses sem fonte a obter (trabalho matemático)

| ID | Hipótese ou problema | Onde | Situação |
|---|---|---|---|
| H1 | L-EF2c: passagem do observável congelado para o modelo de linhas com erro controlado | ETAPA11_3B §2.3; [ETAPA11_3B_H1_FORMULACAO.md](ETAPA11_3B_H1_FORMULACAO.md) | aberto. Enunciado formulado (observável O₁/O₂, truncamentos, normas, uniformidade; candidatos S1–S5; rotas R1–R5). A cota absoluta de R1 não fecha; R2 e R3 dependem de F9 e F10. **Revisão 11.3b-26:** S3b derivada condicionalmente; S1 quantificado e aberto; R5 formalizado e encerrado; Cauda Projetada com condição suficiente para S2-ratio′(U₂) certificada sob RH para M^math em (8, 2), 461/461 elegíveis (execução 4, dependência herdada eliminada; [ETAPA11_3B_H1_CAUDA_PROJETADA.md](ETAPA11_3B_H1_CAUDA_PROJETADA.md) §II.20); S3a, S3c e passagem ao estimador registrado pendentes |
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
