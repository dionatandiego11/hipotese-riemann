> **Errata de 13/10/2026:** as conclusões abaixo sobre erro O(T^(1/2+ε)), ausência de T/log T e derivação completa de C7/C8 estão suspensas por falta de uniformidade no limite do deslocamento. O original foi preservado em `results/razoes_momentos_negativos_20261013/antes/`. A álgebra das diagonais permanece válida; ver `hipoteses/RAZOES_REGULARIZACAO_20261013.md`.

# Etapa B — as Conjecturas 7 e 8 pela conjectura das razões, com termo de erro (28/09/2026)

Derivação **heurística** (rótulo D), na forma de "receita" usual de Conrey–Farmer–Zirnbauer / Conrey–Snaith (B27).
Continua `DERIVACAO_ETAPA_A.md` e `AVALIACAO_DERIVACAO_RAZOES.md`. **Não é prova.**

## 1. O obstáculo e como contorná-lo

- A representação de Conrey–Snaith (7.6), Σ_ρ f(ρ) = (1/2πi)∮ (ζ′/ζ)(z) f(z) dz, com f(z) = 1/(ζ(z+α)ζ(1−z+β)), **não
  serve** para o momento negativo. f tem polos em z = ρ − α e z = 1 − ρ + β, dentro do contorno, e os resíduos deles
  **cancelam exatamente** os resíduos em ρ quando α, β → 0. Conta feita: a soma dos três resíduos associados a cada
  zero é O(α).
- **Contorno usado:** o resíduo de 1/ζ(s) em ρ é 1/ζ′(ρ). Com um único deslocamento α (Re α > 0),

  J(α) := Σ_{0<γ≤T} 1/(ζ′(ρ) ζ(1−ρ+α)) = (1/2πi)∮_C ds / (ζ(s) ζ(1−s+α)),

  com C o retângulo de lados verticais Re s = ½ − ε e Re s = ½ + ε′, **0 < ε′ < Re α**. Os polos de 1/ζ(1−s+α) ficam em
  s = ρ̄′ + α, com Re = ½ + Re α, **fora** de C. Dentro ficam só os ρ, que são polos simples se α ≠ 0.
- Como ζ(1−ρ+α) = ζ(ρ̄+α) ≈ α ζ′(ρ̄) = α conj(ζ′(ρ)) (sob RH), **J(T) := Σ 1/|ζ′(ρ)|² = lim_{α→0} α·J(α)**.

## 2. Lado direito (Re s = ½ + ε′)

O integrando é 1/(ζ(½+γ+it) ζ(½+δ−it)), com γ = ε′ > 0 e δ = α − ε′ > 0. Sem funções ζ no numerador, a receita
(Conrey–Snaith (2.4)–(2.10); ou (2.10) com os fatores do numerador levados a 1, o que zera o termo de troca) retém só a
diagonal das séries de 1/ζ:

  (1/T)∫_0^T dt / (ζ(½+γ+it) ζ(½+δ−it)) = Σ_h μ(h)²/h^{1+γ+δ} + O(T^{−1/2+ε}) = ζ(1+γ+δ)/ζ(2+2γ+2δ) + O(T^{−1/2+ε}).

Isso depende só de γ + δ = α, não de ε′. Contribuição: (T/2π) · ζ(1+α)/ζ(2+2α).

## 3. Lado esquerdo (Re s = ½ − ε) e lados horizontais

Pela equação funcional, 1/ζ(s) = χ(1−s)/ζ(1−s). O integrando fica χ(½+ε−it)/(ζ(½+ε−it) ζ(½+ε+α−it)). Os dois
denominadores estão do mesmo lado (−it) e sobra um fator χ não compensado. **A receita descarta** termos com número
desigual de fatores χ: são oscilatórios, e por fase estacionária dão somas do tipo Σ_{k≤T/2π} (μ∗μ)(k)k^{…}, que sob RH
são O(T^{1/2+ε}). Os lados horizontais também são desprezados, como em Conrey–Snaith.

## 4. Resultado para ζ

  J(α) = (T/2π) ζ(1+α)/ζ(2+2α) + O(T^{1/2+ε}),  e  α ζ(1+α)/ζ(2+2α) → 1/ζ(2) = 6/π².

  **Σ_{0<γ≤T} 1/|ζ′(ρ)|² = (3/π³) T + O(T^{1/2+ε}).**

Termo principal: a conjectura de Gonek. **Não há termos de ordem T/log T, T/log² T, …**: a receita prevê que o único
termo de ordem T é o principal. É coerente com Hughes–Keating–O'Connell, cuja potência de log para k = −1 é zero; o
"polinômio em log T" do termo principal é uma constante.

## 5. Resultado para L(s,χ), χ primitivo mod q

Mesma receita com as séries Σ μ(h)χ(h)h^{−s} e sua conjugada. A diagonal fica Σ μ(h)²|χ(h)|² h^{−1−α} = L(1+α,χ₀)/L(2+2α,χ₀),
com χ₀ o caractere principal mod q. Como L(1+α,χ₀) = ζ(1+α)∏_{p|q}(1−p^{−1−α}):

  α L(1+α,χ₀)/L(2+2α,χ₀) → ∏_{p|q}(1−1/p) / (ζ(2)∏_{p|q}(1−p^{−2})) = (6/π²)∏_{p|q} p/(p+1) = **A_q**.

  **Σ_{0<γ≤T} 1/|L′(ρ,χ)|² = (A_q/2π) T + O(T^{1/2+ε})**, que é a Conjectura 7 com termo de erro.

**Conjectura 8:** com L(2s,χ²)/L(s,χ) = Σ λ(h)χ(h)h^{−s} (Pearce-Crump (1.2)), a diagonal é
Σ λ(h)²|χ(h)|² h^{−1−α} = L(1+α,χ₀), e α L(1+α,χ₀) → ∏_{p|q}(1−1/p) = φ(q)/q:

  **Σ |L(2ρ,χ²)/L′(ρ,χ)|² = (φ(q)/q) T/2π + O(T^{1/2+ε})**. Em q = 1, é a conjectura de Ng.

## 6. Leitura

- **Responde, no plano heurístico, à pergunta deixada em aberto por Pearce-Crump** (derivar as Conjecturas 7 e 8 pela
  receita CFKRS ou pela conjectura das razões). A receita reproduz as duas constantes e acrescenta a previsão de que o
  erro é O(T^{1/2+ε}). Três caminhos heurísticos independentes (mollifier longo, fator tipo HKO e razões) dão as mesmas
  constantes.
- **Correção de interpretação (registrada):** na avaliação anterior e na nota v1, eu disse que os desvios de altura
  finita (0,912 → 0,963 → 0,992) seriam termos de ordem inferior "de alguns por cento, mensuráveis". A receita prevê
  que **não há** tais termos. Os desvios seriam flutuação de uma soma de cauda pesada: o termo 1/|ζ′|² tem cauda
  P(u > x) ∼ x^{−3/2}, pela repulsão quadrática dos zeros, portanto variância infinita. Uma amostra finita tende a ficar
  abaixo da média.
- **Conferência exploratória nos dados já vistos** (zeros de ζ 1–27.000, sem ficha):
  - razões por janela de 3.000 zeros: 0,920, 1,033, 0,907, 0,940, 0,929, 0,940, 1,088, 0,948 e 1,080, **sem tendência
    com a altura**, a maioria abaixo de 1 e algumas acima (assimetria de cauda pesada);
  - (J(T) − 3T/π³)/√T estável entre −0,07 e −0,63 de N = 1.000 a 27.000, compatível com erro O(√T) e não com um
    termo ∝ T/log T.
- **Novidade:** a conta é curta e especialistas provavelmente a conhecem; não se encontrou escrita (busca breve).
  Não se reivindica novidade. Vale como resposta heurística à pergunta do autor e como correção da nossa leitura.

## 7. Consequências para o projeto

1. **Nota:** corrigir §2.2 e §6. Os desvios não devem ser chamados de termos de ordem inferior; a justificativa do teste
   diferencial muda (ele passa a comparar duas somas de cauda pesada, e a incerteza já é tratada pelo bootstrap); a
   derivação desta etapa entra como seção.
2. **Teste em dados novos (proposta, não executada):** a receita prevê razão média 1 sem deriva em log T. Um teste
   justo usaria zeros de ζ ainda não vistos (27.001–100.000) e uma referência de flutuação sem parâmetros livres, a
   distribuição da razão por janela em matrizes aleatórias (CUE). A previsão da receita é mais fraca do que "medir
   termos de ordem inferior": é **ausência** de deriva, e distinguir um termo de ~2% exigiria muitos zeros por causa da
   cauda pesada.
