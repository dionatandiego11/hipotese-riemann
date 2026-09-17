# Revisão da especificação para a implementação independente

**Data:** 13/09/2026. **Fonte da especificação:** `docs/PROTOCOLO.md` §3, §7.2, §8.1–8.3, §9.1–9.5 e configurações
`configs/m4_v1.toml` / `configs/m4_v2.toml` (parâmetros numéricos). A implementação `independent/riemann_indep` não importa,
copia nem adapta `src/`; um teste verifica a ausência de importações de `riemann_spectra`.

## Limites de independência (registrados antes da comparação)

1. **Mesmo autor.** O código independente foi escrito pelo mesmo agente que escreveu `src/` e que conhece sua estrutura.
   Isso reduz a independência: escolhas de projeto podem ser repetidas por memória. Mitigação: seguir a especificação
   escrita, usar caminhos numéricos deliberadamente diferentes (abaixo) e resolver ambiguidades por escrito.
2. **Resultados agregados já vistos.** Contagens de detecções, critérios C1–C3, inconclusivos (log 127, log 131) e várias
   medianas dos blocos escolhidos já foram lidos neste projeto. A comparação **não é cega**. Os arquivos de referência por
   bloco (`nulls.npz`, `blind_peaks.csv`, `arithmetic_matches.csv`, tabelas M2) só são abertos pelo script de comparação
   depois do congelamento deste documento e do plano.
3. **Especificação comum.** A especificação foi escrita pelo mesmo autor da implementação de referência; um erro
   matemático nela (convenção, normalização, fórmula de referência) seria reproduzido. A revisão abaixo verifica as
   fórmulas por derivação e por testes com resultados conhecidos.
4. **Dependências compartilhadas.** Python 3.12, NumPy 2.5.3, SciPy 1.18.1 (LAPACK/BLAS, `scipy.special`), mpmath 1.4.1;
   mesmo arquivo de dados Odlyzko (`data/raw/zeros1`; lido diretamente do arquivo bruto, não do CSV processado);
   mesmas fórmulas de referência (N̄ de Riemann–von Mangoldt, coeficientes −log p/(π p^{r/2}), Bogomolny et al.).

## Caminhos numéricos diferentes (deliberados)

| Componente | Referência (`src/`) | Independente |
|---|---|---|
| Soma discreta de F na malha | NUFFT tipo 1 gaussiana | Soma direta trigonométrica em blocos (cos/sin reais) |
| Termo suave ∫ w d̄ e^{−i(E−E_c)t} | Gauss–Legendre composto | **Forma fechada** com integral exponencial E₁ complexa (validada contra mpmath `quadosc`) |
| Inversa de N̄ | Iteração de Halley | **Função W de Lambert** (fórmula fechada) + um passo de Newton |
| GUE | Tridiagonal (implementação própria de `src/`) | Tridiagonal reescrita a partir de Dumitriu–Edelman e validada contra GUE **denso** em dimensão pequena |
| Máximos locais separados | `scipy.signal.find_peaks(distance)` | Supressão gulosa de não-máximos escrita à mão |
| Refinamento de período | parábola em log|F| | parábola em |F|² (ambiguidade A14; só descritivo) |
| Mínimos quadrados | `numpy.linalg.lstsq` | `scipy.linalg.lstsq` (driver `gelsy`) |
| Resposta da janela | fórmula em `sinc` | soma de integrais exatas de exponenciais (forma diferente) |
| Catálogo de primos | crivo | divisão por tentativa |
| Correlação de pares | offsets vetorizados | `searchsorted` em janela deslizante |
| CUE p₀ | Gauss–Legendre (Bornemann) | Clenshaw–Curtis (Bornemann) |

## Ambiguidades e resoluções adotadas (antes de consultar resultados por bloco)

- **A1 FWHM:** largura total a meia altura de |W(ω)|, com W a transformada da janela de Hann de comprimento L.
- **A2 Malha:** t_k = t_min + k·dt, dt = FWHM/8, k = 0..⌊(t_max − t_min)/dt⌋.
- **A3 Janela:** [A, B] = [γ_primeiro, γ_último] do bloco (ambos incluídos), w = ½(1 − cos(2π(E − A)/L)), E_c = (A + B)/2.
- **A4 Densidade média:** d̄(E) = log(E/2π)/(2π).
- **A5 Suavização de σ:** "média móvel de largura 0,05": número ímpar de pontos mais próximo de 0,05/dt, centrado; bordas por
  reflexão. *Não especificado no protocolo* — afeta sobretudo as bordas da malha.
- **A6 Ordem RMS/suavização:** média de |F|² sobre as realizações, suavização da potência, depois raiz. *Protocolo ambíguo.*
- **A7 Nulo shuffle:** x = N̄(γ), permutação dos n − 1 espaçamentos, soma acumulada a partir de x₀ = N̄(γ_primeiro), inversão de N̄.
- **A8 Nulo GUE:** dimensão ⌈n/0,6⌉, n níveis centrais por índice, unfolding dim·F_semicírculo, reescala linear para [N̄(γ_primeiro), N̄(γ_último)], inversão de N̄.
- **A9 Máximos locais:** z_k > z_{k−1} e z_k ≥ z_{k+1} com z_k ≥ 3,0; entre máximos a menos de 1 FWHM, mantém-se o maior (guloso por altura).
- **A10 Decisão:** z no ponto da malha do máximo local.
- **A11 Faixa inconclusiva:** K ~ Bin(B, 0,95); l = maior índice com P(K ≤ l − 1) ≤ 0,025; u = menor índice com P(K ≥ u) ≤ 0,025;
  detectado se z > X_(u); inconclusivo se X_(l) ≤ z ≤ X_(u); não detectado se z < X_(l).
- **A12 Limiar pontual:** menor s com (1 + #{max nulo ≥ s})/(B + 1) ≤ α.
- **A13 Estatística máxima:** máximo de z em toda a malha.
- **A14 Período refinado:** *não especificado no protocolo*; adota-se parábola em |F|² nos três pontos; o período refinado é usado no matching.
- **A15 Sintéticos:** *parcialmente especificados* (z verdadeiro em [0,5; 4]×limiar; quantil 0,99; limite 0,5 FWHM; ≥ 90%).
  Resoluções próprias: linhas isoladas com separação mínima de 10 FWHM; linha "recuperada" se existe detecção a ≤ 0,5 FWHM;
  pares com z verdadeiro em [2; 4]×limiar; orçamento de positividade Σ|C| ≤ 0,8·d̄(A) com descarte de linhas.
- **A16 Catálogo:** todos (p, r), r ≥ 1, com r log p ∈ [t_primeiro, t_último] da malha.
- **A17 Resolvida:** separação ao vizinho do catálogo ≥ separação de resolução calibrada.
- **A18 Matching:** guloso por distância crescente sobre pares a ≤ tolerância (especificado). Sensibilidade: atribuição ótima (Hungarian).
- **A19 Escore nulo:** mesma regra estrita (z > X_(u)) no conjunto-escore.
- **A20 z previsto:** |c|·W(0)/(2σ(T)), σ(T) por interpolação linear.
- **A21 Ajuste `band_conjugate`:** 9 pontos igualmente espaçados em [T − ½FWHM, T + ½FWHM] por linha, união; sistema real em
  (Re C, Im C) com lóbulos W(t − T) e W(t + T).
- **A22 Q:** C_k lido no ponto da malha mais próximo de T_k, fase corrigida com e^{−iE_c T_k} (T exato); controle: fases
  uniformes independentes por linha preservando |F|; p = (1 + #{Q_nulo ≥ Q})/(B + 1).
- **A23 Recuperação C1:** entre linhas com z previsto ≥ 1,5·X_(u) (sem exigir "resolvida"); C2 exige resolvida e clara.
- **A24 M2:** CDF de espaçamentos em 1001 pontos de [0, 5]; R₂ com normalização de contagem fixa n(n−1)/L²·∫(L − s)ds em 50 bins;
  K_c com 10 sub-blocos contíguos de contagem igual, Hann por sub-bloco, μ analítico, Q = 3L/8, τ em 100 pontos de [0,02; 2];
  envelope: teste de posto simétrico com distância L2 (RMS) à média dos outros B membros; GUE com 60% centrais e unfolding
  pelo semicírculo (sem reescala); Poisson com n pontos uniformes em [0, n − 1].
  *Detalhes de K_c (divisão em sub-blocos, grade de τ) não estão no protocolo; foram lidos das configurações e do registro de andamento.*
- **A25 CUE:** conforme §9.5 (p₀ por Fredholm do núcleo seno; p₁ por Richardson N = 32, 64 sobre a fórmula exata de E_N;
  N_eff e α na mediana de γ do bloco).

## Verificação das fórmulas (revisão da especificação)

Derivações conferidas antes de implementar e cobertas por testes:
- Uma linha de densidade c·cos(ET) produz F(t) ≈ (c/2)e^{iE_cT}W(t − T) + (c/2)e^{−iE_cT}W(t + T); portanto C = 2a·e^{−iE_cT}.
- W(0) = ∫w = L/2 para Hann; FWHM de Hann = 2·(2π/L).
- Termo suave em forma fechada: ∫_A^B log(E/2π) e^{iΩE} dE = [log(E/2π)e^{iΩE}/(iΩ)]_A^B − (1/(iΩ))[E₁(−iΩA) − E₁(−iΩB)].
- N̄(E) = y log y − y + 7/8 com y = E/2π ⇒ y = (x − 7/8)/W((x − 7/8)/e).
- Normalização de R₂ e de K_c: Poisson dá R₂ = 1 e K_c = 1; GUE dá rampa min(τ, 1).
