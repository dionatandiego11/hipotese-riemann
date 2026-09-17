# Etapa 11 — pendências da matriz que dependem de derivação ou experimento

**Data:** 17/09/2026. **Estado:** derivações escritas; **códigos aplicados na matriz em 17/09/2026**, com aprovação do usuário (E-K5-M4-SINAL, E-K5-N3-SINAL; matriz §0.6).
Nenhum cálculo numérico. Nenhuma afirmação sobre RH.

Entradas tratadas (todas com `PC` na matriz): **K5a M4**, **K5a N3**, **K5a N1**, **K7 N1**, **K9 N1**.
Ficam fora (dependem de fonte ou de desenho próprio): K7 M1 e K7 M4.

## 1. Fórmulas usadas

**(W) Fórmula explícita** (forma de referência;
[ETAPA11_3B_ADMISSIBILIDADE.md](ETAPA11_3B_ADMISSIBILIDADE.md) §2 e [ETAPA11_3B_TERMO_ARQUIMEDIANO.md](ETAPA11_3B_TERMO_ARQUIMEDIANO.md) §§4–6; ponto de partida: Connes, Teorema 6 e Lema 3, lidos;
enunciado independente: Montgomery–Vaughan, Teorema 12.13, p. 410, lido). Para g par em C_c^∞(ℝ), com
h(r) = ∫g(x)e^{irx}dx:

Σ_ρ m_ρ h(γ_ρ) = h(i/2) + h(−i/2) − g(0) log π + (1/2π)∫h(r) Re ψ(¼ + ir/2) dr − 2 Σ_{n≥2} Λ(n) n^{−1/2} g(log n).

**(S) Fórmula de Selberg**, superfície hiperbólica compacta M (Marklof, arXiv:math/0407288v2, Teorema 4, eq. (182),
lido): se h satisfaz (H1) analítica em |Im ρ| ≤ σ, σ > ½, (H2) par, (H3*) |h(ρ)| ≪_N (1 + |Re ρ|)^{−N} na faixa, então

Σ_{j≥0} h(ρ_j) = (Area/4π)∫h(ρ) tanh(πρ) ρ dρ + Σ_{γ primitivas} Σ_{n≥1} ℓ_γ g(nℓ_γ) / (2 sinh(nℓ_γ/2)),

com λ_j = ¼ + ρ_j², g(t) = (1/2π)∫h(ρ)e^{−iρt}dρ (mesma convenção de (W)), convergência absoluta.

**Classe comum.** Se g é par, C^∞ e de suporte compacto, h é inteira e, em cada faixa horizontal, decai mais rápido que
qualquer potência de |Re ρ| (Paley–Wiener). Logo h satisfaz (H1)–(H3*), e (W) e (S) valem para o mesmo g.

## 2. Lema (estrutura das duas fórmulas em x > 0)

Seja g par, C^∞, com suporte em {δ ≤ |x| ≤ R}, 0 < δ < R. Então:

1. **(W)** Os termos h(±i/2), g(0) log π e o arquimediano são integrais de g contra **densidades contínuas** em x > 0:
   h(±i/2) = ∫g(x)e^{∓x/2}dx; g(0) = 0; e, por [ETAPA11_3B_TERMO_ARQUIMEDIANO.md](ETAPA11_3B_TERMO_ARQUIMEDIANO.md) §§4–5 com g(0) = 0 (T[g] = −½∫₀^∞ gK),
   (1/2π)∫h Re ψ = −½∫₀^∞ g(x)K(x)dx, com K(x) = 1/sinh(x/2) + 1/cosh(x/2) contínua em x > 0. O último termo é
   uma soma de **massas pontuais** em x = log n, com massa −2Λ(n)n^{−1/2} ≤ 0, estritamente negativa quando n é potência
   de primo.
2. **(S)** O termo de área é ∫g(x)D(x)dx com D contínua em x > 0: escrevendo ρ tanh(πρ) = |ρ| + r(ρ), a transformada de |ρ|
   é −1/(πx²) fora da origem e r é par, contínua e com decaimento exponencial, de transformada analítica. Os termos com
   ρ_j não reais (autovalores λ_j < ¼, em número finito, incluindo λ₀ = 0) são h(ρ_j) = ∫g(x)e^{iρ_j x}dx, também com
   densidade contínua. O termo geométrico é uma soma de **massas pontuais** em x = nℓ_γ, com massa
   ℓ_γ/(2 sinh(nℓ_γ/2)) > 0 (os comprimentos são discretos numa superfície compacta: a soma é localmente finita).

Uma distribuição em (0, ∞) da forma "densidade contínua + soma localmente finita de massas pontuais" determina de forma
única as massas (teste com g concentrada perto de cada ponto).

## 3. K5a M4 — a fórmula de traço não pode ser a fórmula explícita

**Hipótese de identificação (a mesma de E-K5-M2/M3).** O espectro de −Δ em M é identificado com as ordenadas dos zeros:
o multiconjunto {±ρ_j : ρ_j real} coincide com {γ_ρ} (com multiplicidades), a menos de um número finito de elementos.

**Derivação.** Sob essa identificação, para g como no Lema,
Σ_ρ m_ρ h(γ_ρ) = 2 Σ_{j: ρ_j real} h(ρ_j) + (soma finita de valores de h),
porque cada ρ_j real aparece como ±ρ_j e h é par. Substituindo (W) à esquerda e 2×(S) à direita, e usando o Lema, as
**massas pontuais** dos dois lados em x > 0 têm de coincidir. À esquerda, a massa em x = log 2 é −2 log 2/√2 < 0. À
direita, todas as massas são ≥ 0, e somas finitas de h(z) não têm massas. Contradição.

**Conclusão.** Nenhuma superfície hiperbólica compacta tem fórmula de Selberg igual à fórmula explícita sob a
identificação espectro = zeros. O obstáculo é o **sinal** das massas, e não depende de constantes positivas de
normalização. A mesma conclusão vale se a identificação for reescalada por a > 0 (ρ_j = aγ), porque massas positivas
continuam positivas.

**Escopo.** Identificação espectro ↔ zeros (afim com a > 0, b = 0); superfície compacta. Não trata superfícies
cofinitas (K5b) nem reparametrizações não afins.

**Proposta:** K5a M4 `PC/PC` → **`V/derivacao`**, sustenta decisão.

## 4. K5a N3 — sinal dos coeficientes das linhas

**N3 (plano §2.2):** na convenção de §3.2 do plano, as linhas medidas em t = r log p têm coeficiente −log p/(π p^{r/2}),
**negativo**, com concordância ≤ 2,6·10⁻⁹ nas linhas claramente detectáveis.

**Derivação.** No instrumento, F_w(t) = Σ_n f_t(E_n) − termo suave, e o modelo de linhas vem de (W) com o fator ½ da
simetrização ([ETAPA11_3B_FORMULA_EXPLICITA.md](ETAPA11_3B_FORMULA_EXPLICITA.md) §2.2(b)): o coeficiente de cada linha é
a massa pontual de (W) em x = log n, dividida pelo mesmo fator positivo, o que dá c(n) = −Λ(n)/(π√n) < 0. Se a
sequência E_n for o espectro de uma superfície compacta, o mesmo cálculo com (S) no lugar de (W) dá linhas em x = nℓ_γ
com coeficientes proporcionais, pelo **mesmo** fator positivo, a ℓ_γ/(2 sinh(nℓ_γ/2)) > 0. Portanto, em qualquer
posição onde houver linha (inclusive em x = r log p, se ℓ_γ = log p), o sinal previsto é **positivo**, oposto ao medido.

**Escopo.** Sinal das linhas na convenção do instrumento, para espectro exato de superfície compacta. Não usa a
tolerância numérica de N3 (basta o sinal) nem a faixa de alturas. Não trata superfícies cofinitas.

**Proposta:** K5a N3 `PC/PC` → **`V/derivacao`**, sustenta decisão.

## 5. N1 em K5a, K7 e K9 — não decidível no nível da classe

**N1 (plano §2.2):** espaçamento médio unfolded 1,000 ± 0,0002 com N̄ de Riemann–von Mangoldt, e variância 0,145–0,164,
nas alturas 14 a 7,5·10⁴.

**Análise.** As leis de Weyl disponíveis dão contagens c·E^α + O(E^β) com **constante do resto não explícita**:
Marklof Prop. 10 (K5a), Bäcker eq. (49) com C não especificado (K7), Hörmander Teor. 5.1 com C não explícito (K9). Numa
faixa finita de alturas, uma constante de resto desconhecida pode, em princípio, compensar a diferença entre c·E^α e
(E/2π)log E. Além disso, a classe inclui infinitos sistemas (áreas, formas, métricas), e nenhum cálculo finito cobre a
classe inteira. Logo:
- não há **derivação** de V em N1 para a classe;
- um **experimento** só decide N1 para um **sistema concreto** (por exemplo, o bilhar ou a superfície escolhidos como
  controle na 11.6), não para a classe.

**Proposta:** K5a N1, K7 N1, K9 N1 `PC` → **`L`**, com observação "não decidível no nível da classe sem constantes
explícitas; decidir apenas para sistema concreto (11.6)". A incompatibilidade assintótica (M2/M3 = V) continua registrada
separadamente. Não sustenta decisão.

## 6. Resumo

| Entrada | Antes | Proposta | Base | Sustenta decisão |
|---|---|---|---|---|
| K5a M4 | PC / PC | **V / derivacao** | §3: massas negativas de (W) contra massas positivas de (S) | sim |
| K5a N3 | PC / PC | **V / derivacao** | §4: sinal positivo previsto contra sinal negativo medido | sim |
| K5a N1 | PC / NA | **L / NA** | §5: resto sem constante explícita; classe infinita | não |
| K7 N1 | PC / NA | **L / NA** | §5 | não |
| K9 N1 | PC / NA | **L / NA** | §5 | não |

**Limites.**
- A estrutura de (W) usada aqui (sinal −2Λ(n)n^{−1/2}) vem da forma de referência derivada no projeto a partir de Connes
  (conferido) e coincide com Montgomery–Vaughan 12.13 (lido); o enunciado original de Weil continua não lido (F5).
- Marklof é fonte secundária rigorosa; Selberg 1956 não foi lido.
- Os argumentos de §3 e §4 não foram auditados independentemente.
