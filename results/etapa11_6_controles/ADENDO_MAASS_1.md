# Adendo 1 ao `ctrl-maass-v1` — normalização por classes de PSL(2, ℤ) e H_cosh com fonte (19/09/2026)

Gravado **antes** do catálogo G1, de qualquer código do controle e de qualquer transformada dos autovalores de Maass.
SHA-256 em `ADENDO_MAASS_1.sha256`. Declaração: [DECLARACAO_MAASS.md](DECLARACAO_MAASS.md) (`5db97004…`). Derivação que
o motiva: [D1M_DERIVACAO_MAASS.md](D1M_DERIVACAO_MAASS.md) (`773a077b…`).

## 1. Motivo

A declaração (§4) previa: "Se a derivação contradisser P2, prevalece a derivação, com adendo antes de qualquer
cálculo". A D1-M, a partir de Bolte & Grosche (2.31) e Bolte & Steiner (13), lidos na fonte, mostrou dois pontos:
1. As somas da fórmula de traço correm sobre **classes de conjugação de Γ̂ = PSL(2, ℤ)**, com pesos
   l_p/(4 sinh(l/2)) para as hiperbólicas e l(ρ²)/(4 cosh(l/2)) para as reflexões com deslizamento. **Não** correm
   sobre classes de PGL(2, ℤ) com peso ½, como na leitura de BLS usada em P2 e P3.
2. **H_cosh é o resultado da fonte;** H_sinh fica refutada por fonte.

## 2. Mudanças

**P2 (substitui o texto da declaração).** Coeficientes, por classe de conjugação de PSL(2, ℤ):
- **hiperbólica** γ = γ_p^k, com γ_p primitiva em PSL(2, ℤ) e |tr γ_p| = n ≥ 3; l = k·2 arccosh(n/2):
  **c = +l_p/(4π sinh(l/2))**;
- **reflexão com deslizamento** ρ = ρ_p^{2k−1}, com det = −1, |tr ρ_p| = n ≥ 1 e l_ρ = 2 arcsinh(n/2); l = (2k − 1)·l_ρ:
  **c = −l_ρ/(2π cosh(l/2))**;
- linhas com o mesmo l somam os coeficientes.

**P3 (substitui).**
- As classes vêm de **classes de equivalência própria de todas as formas binárias** (primitivas ou não), **sem a
  involução ι**: discriminante n² − 4 para as hiperbólicas e n² + 4 para as reflexões com deslizamento.
- A raiz primitiva é determinada pelo conteúdo da forma e pela Chebyshev U_{k−1} (D1-M §5).
- Continuam valendo:
  - dois algoritmos independentes (ciclos de formas reduzidas de Gauss; componentes pelos geradores S e T numa caixa),
    que precisam concordar em todas as contagens;
  - n ≤ 13;
  - gravação com hash antes de qualquer transformada.
- **Conferência obrigatória em G1:** as contagens das classes primitivas com n = 1, 2 (δ = −1) e n = 3 (δ = +1) devem
  bater com os números de classes de discriminante 5, 8 e 5. Se baterem, as previsões de D1-M §3 ficam (−0,137003;
  −0,198379; +0,137003). Se não baterem, G1 prevalece e a divergência é registrada.

**Critérios (§5 da declaração).**
- **M-C2a−** deixa de ser descritivo e passa a ser **critério**, com a mesma forma de M-C2a+: \|Re Ĉ − c\| ≤ 3σ_c em
  ≥ 90% das linhas elegíveis de reflexão com deslizamento, com c pela fórmula acima (H_cosh).
- **Descritivo:** o relatório continua mostrando a razão Re Ĉ/c sob H_cosh e sob H_sinh.
- **Resultado do controle:** "passa" se M-C1, M-C2s, M-C2a+, **M-C2a−**, M-C4 e M-C4s passam no bloco H.
- No M-C1, o "claramente detectável" passa a usar os coeficientes desta versão de P2, e não mais a menor amplitude
  entre H_cosh e H_sinh.

## 3. O que não muda

Setor ímpar; dados e hash; faixa e blocos (H, h1, h2); densidade suave e ajuste; nulos shuffle e Poisson; semente
20260922; M-C1, M-C2s, M-C2a+, M-C4 e M-C4s nas outras partes; regras de leitura; ordem de execução.

A regra de leitura 4 da declaração ("o resultado de M-C2a− é uma medida… só vira afirmação depois de conferido com uma
fonte") fica **cumprida antes do cálculo**: a fonte foi lida. O teste agora é uma previsão com fonte.
