# Etapa 11 — análise da classe K5b (superfície cofinita, PSL(2,ℤ)\ℍ)

**Data:** 17/09/2026. **Estado:** análise escrita; **códigos aplicados na matriz em 17/09/2026**, com aprovação do usuário (evidências E-K5b-M1 a M4; matriz §0.6).
Nenhum cálculo numérico. Nenhuma afirmação sobre RH.

**Modelo avaliado.** Operador: −Δ = −y²(∂²_x + ∂²_y) em L²(Γ\ℍ, dx dy/y²), Γ = PSL(2,ℤ), como candidato a operador
cujo espectro seria a sequência das ordenadas γ dos zeros de ζ (requisitos M e N do plano, §2).

**Fontes usadas** (registradas em `archive/fontes_etapa11/MANIFESTO.csv`):
- Iwaniec, notas manuscritas *Spectral theory of automorphic forms and analytic number theory* (IAS/AMS 2001),
  conferidas por imagem: p. 4 (matriz de espalhamento), p. 6 (teorema espectral), p. 8 (fórmula de traço), p. 9 (lei de
  Weyl). Fonte **secundária** (notas de palestra).
- Garrett, *Modern analysis of automorphic forms by examples* (versão on-line autorizada, 31/10/2018): [1.9.4] (PDF p. 33),
  termo constante η^s + c_s η^{1−s}; Observação 11.1.5 (PDF p. 315), c_s = ξ(2s − 1)/ξ(2s), ξ(s) = π^{−s/2}Γ(s/2)ζ(s)
  (o texto escreve "Γ = SL₂(R)"; o contexto indica SL₂(ℤ)).
- Bogomolny, Leyvraz & Schmit, arXiv:chao-dyn/9509019, §2: fórmula de traço (2.8) e órbitas indexadas pelo traço n.

## 1. M1 — espaço, operador e auto-adjunticidade

**Fonte.** Iwaniec p. 6: em L²_k(Γ) com ⟨f, g⟩ = ∫_{Γ\ℍ} f ḡ dμ, "the Laplace operator Δ_k is self-adjoint"; espectro
puramente pontual em 𝒞_k(Γ) ⊕ ℛ_k(Γ) (formas cuspidais e resíduos de séries de Eisenstein) e **espectro puramente
contínuo** no complemento ortogonal, "which covers the segment ¼ ≤ λ < ∞ uniformly with multiplicity equal to the
number of singular cusps".

**Leitura.** O operador é definido geometricamente, sem usar os zeros. A auto-adjunticidade vem com página, mas de notas
de palestra.

**Proposta:** `S` / `conferido` (fonte secundária), sustenta decisão.

## 2. M2 — espectro igual às ordenadas dos zeros

**Argumento (elementar).** Pela fonte de M1, o espectro de −Δ em L²(PSL(2,ℤ)\ℍ) contém o intervalo [¼, ∞) (espectro
contínuo, uma cúspide). O conjunto das ordenadas dos zeros é enumerável e sem pontos de acumulação finitos. Uma
identificação afim γ = aλ + b (a ≠ 0), ou pelo parâmetro espectral λ = ¼ + t², leva o intervalo num intervalo, que não é
enumerável. Logo o espectro **não** pode coincidir com as ordenadas, com ou sem multiplicidades.

**Escopo.** Vale para o operador em todo L²(Γ\ℍ). A restrição ao subespaço cuspidal (espectro discreto de formas de Maass)
é **outro modelo**, não avaliado aqui (ver §3 para a sua contagem).

**Proposta:** `V` / `elementar`, sustenta decisão.

## 3. M3 — contagem N(E) = θ(E)/π + 1 + S(E)

**Fonte.** Iwaniec p. 9: com N_Γ(T) = #{j : |t_j| ≤ T} (autovalores cuspidais λ_j = ¼ + t_j²) e
M_Γ(T) = (1/4π)∫_{−T}^{T} −(φ′/φ)(½ + it) dt,
N_Γ(T) + M_Γ(T) = (vol(Γ\ℍ)/4π)T² − (k/π)T log T + c_Γ T + O(T/log T);
"for congruence groups" M_Γ(T) ≪ T log T e N_Γ(T) ~ (vol(Γ\ℍ)/4π)T². PSL(2,ℤ) é grupo de congruência.

**Argumento.** Mesmo restrito à parte discreta: com t_j ↔ γ_j (identificação afim), #{γ_j ≤ E} ~ c·E², contra
N_ζ(E) ~ (E/2π) log E; a razão tende a ∞. Com λ_j ↔ γ_j, #{λ_j ≤ E} ~ (vol/4π)E, e a razão com N_ζ(E) tende a 0.

**Escopo.** Incompatibilidade **assintótica** sob identificações afins; não vale como violação numérica em faixa finita
(como em K5a, K7, K9).

**Proposta:** `V` / `derivacao`, sustenta decisão.

## 4. M4 — fórmula de traço igual à fórmula explícita

**Fonte.** Iwaniec p. 8 (k = 0, multiplicador trivial):
Σ_j h(t_j) + (1/4π)∫ h(t)(−φ′/φ)(½ + it) dt = (vol/4π)∫ h(t) t tanh(πt) dt + Σ_P g(log NP)(NP^{1/2} − NP^{−1/2})^{−1} log P + ⋯,
com os demais termos (elípticos, parabólicos) abreviados por "⋯". BLS §2: órbitas indexadas pelo traço n do elemento.

**Dois fatos parciais (derivados aqui).**
1. **Termos hiperbólicos não estão em log de inteiros.** Um elemento hiperbólico de PSL(2,ℤ) tem traço inteiro n ≥ 3 e
   norma NP = ((n + √(n² − 4))/2)². Para n ≥ 3, (n − 1)² < n² − 4 < n², logo n² − 4 não é quadrado perfeito, √(n² − 4) é
   irracional e NP é irracional. Portanto log NP ≠ log m para todo inteiro m: os deltas hiperbólicos ficam em posições
   diferentes das da fórmula explícita (±log m).
2. **O termo de espalhamento carrega ζ.** Com φ(s) = ξ(2s − 1)/ξ(2s) (Garrett), φ′/φ(s) = 2ξ′/ξ(2s − 1) − 2ξ′/ξ(2s). Em
   s = ½ + it, pela equação funcional e por ζ′/ζ(w) = −Σ Λ(n)n^{−w} (ℜw > 1), aparecem somas Σ Λ(n)n^{−1}n^{±2it}. No lado
   de Fourier isso dá massas em u = ±2 log n com pesos proporcionais a Λ(n)/n, **não** Λ(n)n^{−1/2} em ±log n.
   (Esboço: constantes e termos de Γ não fixados.) Além disso, os polos de φ nos zeros de ξ(2s) ficam em s = ρ/2: os zeros
   de ζ aparecem como **ressonâncias** do espalhamento, não como autovalores.

**Leitura.** A fórmula de Selberg para PSL(2,ℤ) contém ζ, mas com posições (2 log n, log NP irracional) e amplitudes
(Λ(n)/n) diferentes das da fórmula explícita. Uma **igualdade** como distribuições exigiria somar todos os termos
(identidade, elípticos, parabólicos, espalhamento) e comparar; isso não foi feito, e a fonte omite termos ("⋯").

**Proposta:** `P` / `conferido` (estrutura parcial com fonte e derivação parcial; nem igualdade nem incompatibilidade
demonstradas). Não sustenta decisão.

## 5. N1–N4

Com M2 = V para o operador completo, K5b não é candidato a reproduzir a sequência dos zeros. N1–N4 continuam **L**. O papel
útil de PSL(2,ℤ) no projeto é o de **controle aritmético** da 11.6 (T6: estatística tipo Poisson, E-T6-ARIT), que depende
dos dados do item B2 (autovalores cuspidais e comprimentos de geodésicas), ainda não obtidos.

## 6. Resumo da proposta

| Requisito | Antes | Proposta | Tipo de suporte | Sustenta decisão |
|---|---|---|---|---|
| M1 | PC / PC | **S / conferido** | Iwaniec p. 6 (secundária) | sim |
| M2 | PC / PC | **V / elementar** | espectro contínuo [¼, ∞) (Iwaniec p. 6) + argumento de cardinalidade | sim |
| M3 | PC / PC | **V / derivacao** | Weyl, Iwaniec p. 9; escopo assintótico | sim |
| M4 | PC / PC | **P / conferido** | Iwaniec p. 8 + Garrett 11.1.5 + fatos parciais do §4 | não |
| M5, M6, N1–N4 | L | L (sem mudança) | — | não |

**Limites.** As notas de Iwaniec são manuscritas e secundárias; uma fonte primária rigorosa (Iwaniec, *Spectral Methods of
Automorphic Forms*; Hejhal, LNM 1001) reforçaria M1–M3. O cálculo completo de M4 fica em aberto.
