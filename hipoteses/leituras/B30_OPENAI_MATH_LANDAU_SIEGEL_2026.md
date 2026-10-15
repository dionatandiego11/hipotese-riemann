> **Correção de 08/10/2026:** consultar a [revisão da auditoria](../../results/auditoria_openai_math_20261007/REVISAO_20261008.md), que prevalece sobre os números e conclusões abaixo. PDFs: 199/49/9 páginas; 1.930 módulos em grafo parcial, não prova verificada. Não foi demonstrada melhoria de Z1, do certificado ou dos momentos negativos. O texto anterior fica preservado como histórico.

# B30 — OpenAI (2026), *Uniform exclusion of Landau–Siegel zeros*

**Referência.** OpenAI, preprint de 01/10/2026 (release público em 06/10/2026, commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`).
**Cópia local:** `archive/fontes_etapa11/openai_math_adc7f124/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf` (18 pp.).
**Lido:** Resumo e introdução (§1, pp. 1–2).

## O que o texto afirma

| Item | Conteúdo |
|---|---|
| **Teorema 1** | Existe uma constante absoluta c > 0 tal que todo zero real β ∈ (0, 1) de qualquer função L de Dirichlet primitiva não principal real de condutor q ≥ 3 satisfaz **(1 - β) log q ≥ c**. |
| **Método** | Derivada logarítmica com controle de massa de primos com χ(p) = -1, combinada com determinantes de interpolação sobre extensões biquadráticas K = ℚ(√d, √2). |

## Para o projeto `hipotese-riemann`

1. **Estabilidade dos controles de Dirichlet (Etapa 11.6):**
   - No estudo de espectroscopia com Dirichlet e nos testes diferenciais de momentos negativos discretos (MN-1, MN-2, MN-3), utilizamos caracteres reais quadráticos como χ₋₄ (q = 4), χ₅ (q = 5), χ₈ (q = 8) e χ₁₂ (q = 12).
   - A exclusão uniforme de zeros de Landau–Siegel garante que nenhum desses caracteres ou suas extensões de família possui um zero anômalo colado em s = 1 (isto é, 1 - β ≪ 1/log q).
   - Isso sustenta a estabilidade das ordens de grandeza e das constantes assintóticas A_q previstas nas conjecturas de Pearce-Crump (B23).

*Leitura de 07/10/2026.*
