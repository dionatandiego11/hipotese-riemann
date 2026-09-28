# Etapa A — os fatores aritméticos das Conjecturas 7 e 8 pelo modelo de Hughes–Keating–O'Connell (28/09/2026)

Entrega de derivação **heurística** (rótulo D), com verificações numéricas exploratórias. Continua
`AVALIACAO_DERIVACAO_RAZOES.md`. Código e saídas em `results/derivacao_etapa_a_20260928/`.

## 1. Premissa (HKO; Conrey–Snaith (7.2)–(7.3), B27)

Hughes, Keating e O'Connell conjecturam, para k > −3/2,

  Σ_{0<γ≤T} |ζ′(ρ)|^{2k} ∼ (T/2π) · G²(k+2)/G(2k+3) · a(k) · (log T)^{k(k+2)+1},

com a(k) = ∏_p (1 − 1/p)^{k²} Σ_m (Γ(m+k)/(m!Γ(k)))² p^{−m}. O fator de Euler equivale a
(1 − 1/p)^{k²} · E_θ |1 − p^{−1/2} e^{iθ}|^{−2k}, com θ uniforme: a média local de |ζ_p(½+iθ)|^{2k}.

- **Conferência em k = 1:** a(1) = 1 e G²(3)/G(5) = 1/12 dão (T/2π)(1/12) log⁴T = T log⁴T/24π, que é o teorema de
  Gonek (Conrey–Snaith (7.1)).
- **k = −1:** G²(1)/G(1) = 1, potência de log 0, e a(−1) = ∏_p (1 − 1/p)(1 + 1/p) = 6/π², isto é, a conjectura
  de Gonek, 3/π³.

## 2. Extensão a L(s,χ), χ primitivo mod q (modelo usado aqui)

Mesma simetria unitária, portanto o mesmo fator G, e a mesma forma do fator aritmético, com a média local de
|L_p(½+iθ,χ)|^{2k}:

  a_χ(k) = ∏_p (1 − 1/p)^{k²} · E_θ |1 − χ(p) p^{−1/2} e^{iθ}|^{−2k}.

Para p | q, χ(p) = 0: a média local vale 1, **mas o fator (1 − 1/p)^{k²} permanece**. Esse fator vem da normalização
pela densidade tipo ζ, comum a todos os primos, e não da média local.

**Âncora em k = 1 (média quadrática).** O modelo dá a_χ(1) = ∏_{p|q}(1 − 1/p) = φ(q)/q, isto é,
d/dT ∫_0^T |L(½+it,χ)|² dt ≈ (φ(q)/q) log(qT/2π). É o que dá a equação funcional aproximada com o teorema do valor médio
de Montgomery–Vaughan: |L|² ≈ |Σ_{n≤x} χ(n) n^{−½−it}|² + termo dual, cuja média é Σ_{n≤x,(n,q)=1} 1/n ≈ (φ(q)/q) log x,
com x² ≈ qT/2π. Os inteiros não coprimos a q desaparecem; é exatamente o fator (1 − 1/p) em p | q. *(Esboço padrão;
fonte com enunciado exato a conferir.)*

**Verificação numérica exploratória** (`ancora_k1.py`, 3.000 pontos t ∈ [50, 650] por caractere, 474 s de CPU):
inclinação da média de |L(½+it,χ)|² contra log(qt/2π):
- χ₋₄: 0,447 [0,142; 0,746], contra φ(q)/q = 0,5;
- χ₁₂: 0,243 [0,014; 0,467], contra 1/3.

Os dois são compatíveis com φ(q)/q e excluem 1, que é o valor que se obteria descartando (1 − 1/p) em p | q.
Intervalos largos; verificação feita **depois** de formular o modelo, mas sem ficha pré-registrada.

## 3. Resultado para os momentos negativos

- **Conjectura 7** (k = −1): a_χ(−1) = ∏_{p∤q}(1 − 1/p)(1 + 1/p) · ∏_{p|q}(1 − 1/p)
  = (6/π²) ∏_{p|q} (1 − 1/p)/(1 − 1/p²) = (6/π²) ∏_{p|q} p/(p+1) = **A_q**. Portanto
  Σ 1/|L′(ρ,χ)|² ∼ (A_q/2π) T.
- **Conjectura 8**: média local de |L_p(2ρ,χ²)|² |L_p(ρ,χ)|^{−2}. Para p ∤ q, com x = χ(p)p^{−1/2}e^{−iθ}:
  E |1−x|²/|1−x²|² = E 1/|1+x|² = 1/(1 − 1/p); vezes (1 − 1/p) dá 1. Para p | q, χ(p) = 0 e χ²(p) = 0: local 1,
  vezes (1 − 1/p). Total ∏_{p|q}(1 − 1/p) = **φ(q)/q**. Portanto Σ |L(2ρ,χ²)/L′(ρ,χ)|² ∼ (φ(q)/q) T/2π. Para q = 1, é a
  conjectura de Ng.
- **Conferência numérica** (`verifica_fatores_locais.py`): as médias locais batem com as formas fechadas (erro
  < 10⁻⁹), e os produtos de Euler reproduzem A_q e φ(q)/q para q = 1, 4, 5, 8, 12.

## 4. Consequências

- **Dois caminhos heurísticos independentes dão as mesmas constantes:** o mollifier longo de Farmer, que é o caminho de
  Pearce-Crump, e o fator aritmético tipo HKO/CFKRS, que é este documento. Isso reforça as Conjecturas 7 e 8 no plano
  heurístico. Não é prova. O modelo supõe, como HKO, que o fator aritmético dos momentos discretos é o dos
  momentos contínuos, o que foi verificado para ζ em k = 1 (Gonek) e, com a receita, reproduz k = −1 (Gonek, Ng).
- **As alternativas excluídas pelos dados têm interpretação:**
  - HE = descartar (1 − 1/p) em p | q, a mesma normalização que a âncora k = 1 exclui;
  - H7 (trocar os fatores) = aplicar a média local de um momento ao outro.
- **Não cobre os termos de ordem inferior** (etapa B), que exigem a conjectura das razões completa.
- **Novidade:** não se achou este cálculo publicado para L(s,χ). É uma conta de poucas linhas a partir de HKO, e
  especialistas provavelmente a conhecem, então **não se reivindica novidade**. Serve como reforço heurístico na nota.
