# P-RH — declaração prévia da avaliação da força da cota (14/09/2026)

Gravada **antes** do cálculo. SHA-256 em `DECLARACAO_PRH.sha256`.

## Natureza
- Avaliação numérica de uma **cota analítica condicional** (P-RH, `docs/ETAPA11_3B_H1_CAUDA_PROJETADA.md` §II.9).
- **Não** usa dados de zeros.
- **Não** testa nem refuta S2-ratio′ ou C2.
- **Regra de leitura fixada agora:** se a majorante normalizada superar τ_C2 = 10⁻⁶, o resultado é "essa cota não
  certifica a tolerância", não uma refutação de S2-ratio′ nem dos resultados numéricos.
- **Classe:**
  - a_k vem de SVD em ponto flutuante (classe B; cond ≤ 1,025);
  - a aritmética da cota, dados a_k e os parâmetros, é intervalar com extremos exportados arredondados para fora;
  - c₁ e c₂ são enclosures intervalares.

## Corte ϕ
- **Definição:** ϕ(x) = f(x)/(f(x) + f(1−x)), com f(x) = e^{−1/x} para x > 0 e f = 0 para x ≤ 0. É C^∞, com ϕ = 0 em
  (−∞, 0], ϕ = 1 em [1, ∞) e todas as derivadas nulas em 0 e 1.
- **c₁ = sup|ϕ′| e c₂ = sup|ϕ″|:** enclosure intervalar em [δ, 1 − δ] com δ = 0,01 e 20.000 subintervalos, usando
  - ϕ′ = (f′(x)f(1−x) + f(x)f′(1−x))/S², com S = f(x) + f(1−x);
  - ϕ″ = (N′S − 2NS′)/S³, com N = f′(x)f(1−x) + f(x)f′(1−x), N′ = f″(x)f(1−x) − f(x)f″(1−x) e
    S′ = f′(x) − f′(1−x);
  - f′ = e^{−1/x}x⁻² e f″ = e^{−1/x}x⁻⁴(1 − 2x).
- **Pontas** (0, δ] e [1 − δ, 1): cota analítica grosseira (f ≤ e^{−1/δ}, |f′| ≤ e^{−1/δ}δ⁻², |f″| ≤ e^{−1/δ}δ⁻⁴,
  f(1−x) ≥ e^{−1/(1−δ)}, |f′(1−x)| ≤ e^{−1}(1−δ)⁻²), com simetria ϕ(1−x) = 1 − ϕ(x).

## Parâmetros (grade fixada antes)
- t_max = 5,0; U₁ = t_max + d₁, com d₁ ∈ {1, 2, 4, 8}; U₂ = U₁ + Δ, com Δ ∈ {0,5; 1; 2}; ε₀ = 0,1.
- Hipótese d₁ ≥ √2·2π/L verificada em todos os blocos.
- Relatar **todas** as 12 combinações.
- Como a cota vale para cada combinação, relatar também, por (bloco, linha), o **mínimo sobre a grade declarada**. Não
  há otimização fora da grade.

## Blocos, linhas e fórmulas
- **Blocos e linhas:** os 30 blocos de m4 (A, B, L de `metrics.json`) e as 47 linhas do catálogo.
  - a = ‖a_k‖₁ por linha: linha x de M⁺ calculada como em `r5_calculo.py`.
  - ν ∈ {A_rec, B_rec}.
- **Fórmulas** de §II.9:
  - C_Ψ = 4π²a/L², L₀ = C_Ψ/(2d₁²), L₂ (Lema 2), n(ν) = 10,5·log(ν + 8), N₆ = 31 + 10,5·log 13;
  - Z_ν (Lema 4), Pol_ν e Arq (Lema 5);
  - B = (1/π)Σ_ν ½[Z_ν + 2Pol_ν + Arq].
- **Parcelas relatadas separadamente e normalizadas por |c_k|:**
  - zeros: (1/π)Σ_ν ½Z_ν;
  - polos: (1/π)Σ_ν Pol_ν;
  - arquimediano: (1/π)Arq.

## Saídas
- **Arquivos:** `results/etapa11_r5/prh_forca.py`, `prh_forca_tabela.csv` (bloco × linha × combinação) e
  `prh_forca_resumo.json`.
- **Resumo:**
  - máximo e mínimo sobre (bloco, linha) de B/|c_k| e de cada parcela, por combinação;
  - mínimo sobre a grade por (bloco, linha);
  - contagem de pares com B/|c_k| ≤ τ_C2;
  - o mesmo restrito às linhas elegíveis de C2, lidas de `cruzamento_tabela.csv` (descritivo).
