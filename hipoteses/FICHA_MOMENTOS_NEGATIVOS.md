# MN-1 — teste numérico da Conjectura 7 de Pearce-Crump: ficha congelada antes do cálculo (27/09/2026)

**Estado:** congelada **antes** de calcular qualquer derivada nos zeros. SHA-256 em `FICHA_MOMENTOS_NEGATIVOS.sha256`.
Nota de leitura: `hipoteses/leituras/B23_PEARCE_CRUMP_2026.md`.

## 1. Hipótese (D, da literatura)

Pearce-Crump (arXiv:2606.25094, jun/2026), Conjectura 7: para χ primitivo mod q, sob GRH e zeros simples,
Σ_{0<γ≤T} 1/|L′(ρ,χ)|² ∼ (A_q/2π) T, com A_q = (6/π²) ∏_{p|q} p/(p+1). Para q = 1 é a conjectura de Gonek (3/π³).
A constante vem de uma heurística (mollifier longo de Farmer) que o autor declara não ser prova; o artigo não traz
teste numérico. **A parte discriminável é o fator aritmético ∏_{p|q} p/(p+1).**

## 2. Estatística

v_n = log(qγ_n/2π)/|L′(ρ_n)|² (média → A_q sob a conjectura, em primeira ordem). **Teste diferencial:**
R = média(v, χ) / E_ζ[v | mesma distribuição de densidades log(qγ/2π)], com 10 bins nos quantis das densidades de χ.
Isso cancela, em primeira ordem, o viés de altura finita comum a ζ e χ. Previsões para R:

| hipótese | χ₋₄ (q = 4) | χ₅ (q = 5) |
|---|---|---|
| **PC** (Conj. 7) | **2/3** | **5/6** |
| H0: sem fator aritmético | 1 | 1 |
| HE: só remover os fatores de Euler p | q | 4/3 | 25/24 |

## 3. Dados

- ζ: zeros 1–20.000 (`data/processed/zeros_100k.csv`, T0); cobre as densidades de χ.
- χ₋₄, χ₅: zeros 1–3.000 das listas corrigidas (e01/f01, fora da reserva da H-004; corte imediato no script).
- Derivadas: ζ por `mpmath.siegelz(t, derivative=1)` (dps 15; igual a dps 25 nos testes); χ por diferença central de
  `Z_real` com h = 10⁻⁶, dps 20 (erro relativo < 4·10⁻¹⁰ contra h = 10⁻⁵ e dps 30). |Z′(γ)| = |L′(ρ)|
  (Z_χ = e^{iθ_χ}L, real por V4).

## 4. Código

`src/riemann_spectra/discrete_moments.py` (4 testes em `tests/test_discrete_moments.py`, incluindo recuperação de razão
conhecida com cauda pesada); `results/momentos_negativos_20260927/calc_derivadas.py`; `analise.py`.

## 5. Incerteza

IC de 95% por bootstrap de blocos de 100 zeros consecutivos (2.000 réplicas, semente 20260927), reamostrando χ e ζ
independentemente. **Limitação declarada:** 1/|L′|² tem cauda pesada (média finita, variância possivelmente infinita,
por causa dos pares de zeros quase colados); o bootstrap pode subcobrir. Robustez: R recalculado sem os 5 maiores
termos de χ; se isso mudar o lado da decisão, a decisão é marcada como **frágil**.

## 6. Critérios (χ₋₄ primária; χ₅ secundária; fixados antes do cálculo)

- **Conjectura 7 favorecida:** o previsto (2/3; 5/6) está no IC **e** 1 (H0) está fora.
- **Conjectura 7 contrariada:** o previsto está fora do IC.
- **Inconclusivo:** previsto e H0 ambos no IC.
- Registrar também se HE está no IC e a razão absoluta média(v)/A_q (descritiva: termos de ordem inferior podem ser
  grandes em alturas baixas).
- **Descritivo ζ:** média de v contra 6/π² nas faixas 1–3.000, 3.001–10.000 e 10.001–20.000 (convergência da
  conjectura de Gonek em altura finita; fração da soma vinda do 1% maior).

## 7. O que se pode concluir

- Favorecida: primeira evidência numérica (B) do fator aritmético da Conjectura 7, em dois caracteres e alturas
  baixas; não prova nada. **Rótulo C só depois de busca bibliográfica** de testes numéricos anteriores.
- Contrariada: evidência contra a constante heurística nesta faixa, com a ressalva de ordem inferior e cauda pesada.
- Nada aqui é evidência sobre GRH.

## 8. Custo e teto

ζ: 20.000 zeros, teto `RLIMIT_CPU` de 10.800 s. χ₋₄ e χ₅: 3.000 zeros cada, teto de 5.400 s cada. Total estimado
~2,7 h-CPU; teto total de 6 h. Checkpoint a cada 100 zeros. Sem extensão automática.

**Correção antes de qualquer cálculo (11:07):** a regra de fragilidade de `analise.py` tinha uma primeira parte
vazia (condição comparada consigo mesma). Fica só a definição do §5: frágil se tirar os 5 maiores termos de χ mudar o
lado de R em relação ao ponto médio entre PC e H0. Recongelada; nenhuma derivada tinha sido calculada.

*Dionatan Resende & Claude Opus — 27/09/2026.*
