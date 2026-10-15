> **Correção de 08/10/2026:** consultar a [revisão da auditoria](../../results/auditoria_openai_math_20261007/REVISAO_20261008.md), que prevalece sobre os números e conclusões abaixo. PDFs: 199/49/9 páginas; 1.930 módulos em grafo parcial, não prova verificada. Não foi demonstrada melhoria de Z1, do certificado ou dos momentos negativos. O texto anterior fica preservado como histórico.

# B28 — OpenAI (2026), *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane ℜs > 7/8*

**Referência.** OpenAI, preprint de 30/09/2026 (release público em 06/10/2026, commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`).
**Cópia local:** `archive/fontes_etapa11/openai_math_adc7f124/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf` (196 pp.).
**Formalização Lean 4:** `archive/fontes_etapa11/openai_math_adc7f124/lean/OAI/NumberTheory/DirichletL/` (1.953 módulos coletados).
**Auditoria local:** `results/auditoria_openai_math_20261007/` (`DECLARACAO.md`, `RELATORIO.md`).
**Lido:** Resumo, §1 (Introdução, pp. 4–8), §11.2 (Transferência quadrática, pp. 84–85) e §20 (Fechamento do expoente 7/8, pp. 186–196). Auditoria estática dos 1.953 arquivos `.lean` do grafo de `Nonvanishing.lean`.

## O que o texto afirma

| Item | Conteúdo |
|---|---|
| **Teorema 1.1** | Toda função L de Hecke de ordem finita sobre F = ℚ(√-3) e toda função L de Dirichlet (incluindo ζ(s)) não possui zeros em ℜs > 7/8 (polo principal em s = 1 permitido). |
| **Quase-RH** | Afirmação afirmativa da quase-hipótese de Riemann com σ₀ = 7/8. |
| **Teorema 3.1** | Demonstração intermediária da Parte I: semiplano livre de zeros ℜs > 11/12. |
| **Proposição 11.3** | Transferência quadrática exata: L_F(s, η) = L(s, χ) L(s, χ χ₋₃). Como L(1, χ₋₃) = π/(3√3) > 0, zeros de L(s, χ) ou ζ(s) em ℜs > 7/8 implicariam zeros da função L de Hecke sobre F. |
| **Teorema 20.1** | Fechamento do limite analítico com sonda compensada, quarto momento com fatores primos curtos e peneira séxtica. |

## O que a formalização Lean 4 contém

- **Enunciados terminais:** `OAI.NumberTheory.DirichletL.Nonvanishing`
  - `riemannZeta_ne_zero_of_seven_eighths_lt_re`
  - `LFunction_ne_zero_of_seven_eighths_lt_re`
- **Integridade verificada:** 0 ocorrências de `axiom`, 0 ocorrências de `sorry`, 0 ocorrências de `admit`/`cheat`/`unsafe` no subgrafo baixado.
- **Dependências externas:** Apenas `Mathlib`, `PrimeNumberTheoremAnd` e `RellichKondrachov`.
- **Estado de verificação no sistema local:** Bloqueio técnico documentado por ausência de compilador Lean 4 (`which lean lake elan` vazio).

## Para o projeto `hipotese-riemann`

1. **Não prova RH:** A faixa crítica 1/2 < ℜs ≤ 7/8 permanece inteiramente aberta.
2. **Não viabiliza o operador de Hilbert–Pólya:** Um operador autoadjunto H = H† exige autovalores puramente reais, o que requer ℜρ_n = 1/2 exato. Qualquer zero em (1/2, 7/8] destruiria a autoadjunção.
3. **Uso condicional na Etapa 11.3b:**
   - Permite deslocar contornos verticais em integrais de contorno até σ ∈ (7/8, 1) sem encontrar singularidades de 1/ζ(s).
   - Melhora a cota incondicional da cauda de contagem de zeros Z1 (`docs/ETAPA11_3B_Z1_CONTAGEM.md`).
4. **Correspondências C16–C20 (`docs/ETAPA11_CORRESPONDENCIAS.md`):** Fornece citação estruturada e demonstrada da relação de Dedekind para o corpo de Eisenstein F = ℚ(√-3).

*Leitura de 07/10/2026.*
