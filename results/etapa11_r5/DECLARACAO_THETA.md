# Θ_k(U₂) — declaração prévia do cálculo do termo de transição (14/09/2026)

Gravada **antes** do cálculo. SHA-256 em `DECLARACAO_THETA.sha256`.

## Objeto
- Θ_k(U₂) = Σ_{U₁<log n≤U₂} χ(log n)c(n)Q_k(log n), com χ(u) = ϕ((u − U₁)/Δ) (ϕ de `DECLARACAO_PRH.md`),
  c(n) = −Λ(n)/(π√n) e Q_k(u) = a_k·ℓ_u, onde a_k é a linha x de M⁺ do estimador primário `band_conjugate`
  (`docs/ETAPA11_3B_H1_CAUDA_PROJETADA.md` §II.13).
- Truncamento abrupto do alvo: **U = U₂**. Resultados **separados por U₂**; cada corte define um alvo distinto.

## Grade e universo (inalterados)
- d₁ = U₁ − 5 ∈ {1, 2, 4, 8} e Δ = U₂ − U₁ ∈ {0,5; 1; 2} (12 combinações).
- 30 blocos de m4 (A, B, L, E_c de `metrics.json`) e 47 linhas do catálogo.

## Método numérico (classe B; não certificado)
- **Ponto flutuante de dupla precisão.**
- **Resposta da janela** pela forma fechada da Hann, W(ω) = −(L/2π)·sin(πv)/(v(v² − 1)) com v = ωL/(2π) (§II.2(a)).
  Evita o cancelamento da soma de sincs para |v| grande. Todos os |v| aqui são ≥ λ·d₁ ≫ 1.
- **M⁺** pela SVD truncada ao posto, como em R5.
- **Potências de primo** até e^{U₂} por crivo.
- **Erro numérico estimado (não certificado)**, por par e combinação: δ·S_abs + n_termos·ε_mach·max|termo|, com
  - S_abs = Σ|χ(log n)c(n)Q_k(log n)| (a soma dos módulos, relatada também como majorante absoluta);
  - δ = 10⁻⁹, cota conservadora declarada para o erro relativo por termo (fase E_c·log n, resposta W e M⁺, com
    cond ≤ 1,025).
- **Checagem de consistência** (B): recalcular Θ_k com `window_response` (soma de sincs) nas combinações
  (d₁, Δ) = (8, 2) e (1, 0,5), nos blocos b01, c01 e d01, e relatar a diferença máxima.

## Registros por (bloco, linha, combinação)
- U₁, U₂, Θ_k com sinal, erro numérico estimado, S_abs e |c_k|;
- margem = 10⁻⁶|c_k| − |Θ_k|;
- orçamento total normalizado = B^{RH′}/|c_k| + |Θ_k|/|c_k|, com B^{RH′}/|c_k| de `prh2_forca_tabela.csv` para a mesma
  combinação;
- elegibilidade (descritiva, de `cruzamento_tabela.csv`).

## Resumos
- **Por combinação (U₂):** max e mediana de |Θ_k|/|c_k|; número de pares com margem > 0 (todas; elegíveis); número com
  orçamento ≤ 10⁻⁶ (todas; elegíveis); máximo do erro estimado relativo.

## Regras de leitura (fixadas agora)
- Margem ≤ 0 impede fechar **a condição suficiente baseada na soma dos módulos** (B^{RH′} + |Θ_k|). **Não** refuta
  S2-ratio′ nem exclui compensação no resíduo real.
- Orçamento ≤ 10⁻⁶ é resultado **híbrido e condicional a RH** (F5 e J1 bibliográficas), **não** certificação.
- Nenhum refinamento da parcela dos zeros é feito nesta etapa.

## Saídas
- `results/etapa11_r5/theta_calculo.py`
- `theta_tabela.csv`
- `theta_resumo.json`
