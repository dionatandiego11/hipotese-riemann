# B15 — Candès & Fernandez-Granda (2012), *Towards a Mathematical Theory of Super-Resolution*

**Referência.** E. J. Candès e C. Fernandez-Granda, arXiv:1203.5871v3 [cs.IT] (14/11/2012), 48 pp. Versão publicada
(Comm. Pure Appl. Math., de memória) não conferida. **Cópia local:**
`archive/fontes_etapa11/hipoteses_20260925/super_resolution.pdf`, SHA-256 `454ae7ad…`.
**Lido:** pp. 1–13 (introdução, resultados, estabilidade, trabalhos relacionados) e pp. 34–36 (experimentos e
discussão); das §§2–4 e do apêndice, só enunciados e estrutura. Provas não auditadas.

## O que o texto afirma

| item | página | conteúdo |
|---|---|---|
| modelo | 4 | x = Σ a_j δ_{t_j} em [0, 1) periódico, amplitudes complexas; observam-se os 2f_c + 1 coeficientes de Fourier mais baixos; λ_c = 1/f_c |
| programa | 4 | minimizar a norma de variação total sujeita aos dados (análogo contínuo do ℓ¹) |
| **Teor. 1.2** | 5 | se a separação mínima satisfaz Δ(T) ≥ 2λ_c (com f_c ≥ 128), x é a **única** solução; para x real, 1,87 λ_c. Não depende das amplitudes: **picos pequenos são recuperados mesmo enterrados nos lóbulos laterais dos grandes** |
| Teor. 1.3 | 6 | versão 2D, Δ ≥ 2,38 λ_c |
| Cor. 1.4 | 7 | versão discreta; fator de super-resolução SRF = N/n |
| **Teor. 1.5** | 9 | estabilidade: ‖x̂ − x‖₁ ≤ C₀ SRF² δ, com ruído de norma ℓ¹ limitada (modelo determinístico) |
| mal-posto | 9–10 | sem condição de separação, o problema é "irremediavelmente mal-posto" (sequências prolatas de Slepian) |
| limites | 34, 36 | numericamente, separação ≳ λ_c é **necessária**; a suficiente é 2λ_c (1,85 λ_c com prova não publicada). O valor crítico fica entre λ_c e 1,85 λ_c, **em aberto** no texto |
| §4 | ≈29–34 | solução por programa semidefinido no dual e busca de raízes; a justificativa rigorosa fica para trabalho futuro (p. 34) |

## Para o projeto

- **É exatamente o problema do instrumento, em outra roupagem.** A fórmula explícita escreve a densidade de zeros como
  soma de oscilações de frequências T = log p^k; observar os zeros numa janela de comprimento L equivale a observar
  essa soma com corte ~L. A "resolução" do instrumento (FWHM = 4π/L para Hann) é o λ_c daqui.
- **Conta de ordem de grandeza, sem dado reservado:** no catálogo até T ≤ 5, o par mais próximo é log 127 e log 128,
  separados por 0,0078. Num bloco com L ≈ 2.400, 2π/L ≈ 0,0026: separação ≈ 3λ_c, **dentro** do regime do Teorema 1.2.
  O catálogo que usamos é, em princípio, super-resolvível no sentido de Candès–Fernandez-Granda.
- **Diferenças que impedem aplicação direta:** o "ruído" aqui é a flutuação dos zeros (tipo GUE), não um ruído ℓ¹
  limitado; e a medida em T tem **infinitas** linhas de amplitude lentamente decrescente (c(p^k) ~ log p/p^{k/2}), não
  um número finito de picos — as linhas acima de T = 5 vazam para dentro da faixa, que é justamente o mecanismo da H-004.
- **Possível uso futuro, não candidata agora:** um detector cego por variação total (ou norma atômica) no lugar da
  seleção de picos contra o nulo. Seria mudança de método, com CPU, e cairia na regra de custo (ADENDO_REGISTRO_v2_2):
  exige ganho discriminante antes de rodar. Registro só como pista.

Rótulos: Teoremas 1.2, 1.3, 1.5, **A** (provas não auditadas); limite necessário ≳ λ_c, **evidência numérica** dos
autores; a conta do catálogo acima, **B** (aritmética nossa, sem dado).

*Leitura de 25/09/2026, Claude Opus.*
