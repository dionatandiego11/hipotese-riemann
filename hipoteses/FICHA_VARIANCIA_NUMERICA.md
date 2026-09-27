# VN-1 — variância numérica dos zeros e órbitas curtas: ficha congelada antes da medição (26/09/2026)

**Estado:** congelada; medição **não executada** no momento do congelamento. SHA-256 em
`FICHA_VARIANCIA_NUMERICA.sha256`. Categoria: **previsão declarada antes da medição, em dados já consultados para
outras observáveis** (T0 para ζ; e01/f01 exploratórios para χ). **Não** é teste prospectivo no sentido do registro v2.
A H-004 foi adiada por prioridade (`ADENDO_H004_3`, `85e5ebee…`).

## 1. Pergunta

A estatística de longo alcance dos zeros se afasta do GUE do modo previsto pelas **órbitas periódicas curtas** (potências
de primos), sem parâmetros livres? E, quando uma órbita **não existe**, a estatística muda como previsto?

- **Q1 (ζ):** Σ²(L) medida segue a fórmula semiclássica de Berry (1988) e não a do GUE.
- **Q3 (remoção de órbita):** para L(s, χ₋₄), em que χ(2) = 0 e portanto não há órbita de período log 2, Σ²(L)
  segue a fórmula com o conjunto correto de primos, e **não** a mesma fórmula com todos os primos. Idem para χ₅,
  sem o primo 5.

## 2. Teoria usada (fixa)

- **Fonte:** Berry (1988), Nonlinearity 1, 399, eq. (19). O original **não foi obtido** (IOP pago); a fórmula foi
  tirada da transcrição em Lugar, Milinovich e Quesada-Herrera, arXiv:2211.14918, §1.4
  (`archive/fontes_etapa11/variancia_numerica_20260926/`, `3a4d23bc…`), que a prova sob RH e uma conjectura de Chan.
- **Implementação:** `src/riemann_spectra/number_variance.py` (`sigma2_gue`, `sigma2_berry`, `number_variance`), com
  testes em `tests/test_number_variance.py` (8 testes: limites da fórmula GUE, redução de Berry ao GUE para L → 0,
  remoção da parte τ < τ*, peso de χ removendo exatamente o primo excluído, estimador em Poisson, rede e GUE).
- **Extensão a χ real primitivo** (derivação própria, **não** conferida em fonte): Λ = log(qE/2π), corte
  (qE/2π)^{τ*}, peso χ(p)^{2r}. Se a extensão estiver errada, Q3 testa a extensão, não a física.
- **τ* principal = 0,5.** A fórmula só é independente de τ* assintoticamente. A diferença para τ* ∈ {0,25; 0,75} é a
  **incerteza de modelo** m(L), já calculada (até ~0,02).

## 3. Dados e acesso

- **ζ:** `data/processed/zeros_100k.csv` (T0). Blocos b01–b10 de 10.000 zeros; **b02–b10 são primários**; b01
  (alturas 14–9.878, onde log(E/2π) é pequeno) é descritivo.
- **χ₋₄ e χ₅:** zeros 1–3.000 (e01, f01; fora da reserva da H-004) das listas corrigidas `zeros_chi_m4_12000_completo.txt`
  (`81fdfc0a…`) e `zeros_chi_5_12000_completo.txt` (`abe42070…`). O script lê o arquivo e **corta os 3.000 primeiros
  antes de qualquer cálculo**. Nenhum valor dos blocos reservados entra em cálculo algum.
- **Unfolding:** ζ por N_θ(t) = 1 + θ(t)/π (`n_bar_theta`); χ por θ_χ(t)/π (mesma fórmula de `dirichlet_zeros.theta_chi`,
  vetorizada com `scipy.special.loggamma`). A constante aditiva não afeta Σ².

## 4. Previsões congeladas

`results/variancia_numerica_20260926/previsao/previsao.json`, gerado por `previsao.py` (242 s de CPU, semente
20260926), usando **só primos, alturas obtidas por inversão da contagem suave e substitutos GUE**. Grade:
L ∈ {0,25; 0,5; 1; 1,5; 2; 3; 4; 5; 6; 8; 10; 12; 15; 20; 25; 30}. Resumo:

- ζ: a previsão de Berry fica **7–20 σ abaixo do GUE** para L ≥ 1 em todos os blocos, com ressurgências em L que
  dependem da altura (por exemplo, b05: 0,458 em L = 20, contra 0,327 em L = 15).
- χ₋₄: a previsão correta difere da previsão com todos os primos em 5,2–8,6 σ para L ∈ [1,5; 6].
- χ₅: 3,4–5,1 σ para L ∈ [1; 2].
- Ruído do estimador (substitutos GUE, uma matriz por réplica): 10⁴ níveis, 30 réplicas; 3.000 níveis, 60 réplicas. O σ
  por sub-blocos subestima o desvio entre réplicas em até ~25% com 10⁴ níveis.

## 5. Estimador e incerteza

- V(L) = média, numa grade de centros de passo 0,05, de [n(L; y) − L]² (definição de Berry).
- **σ_eff(L) = max(σ por 10 sub-blocos, desvio entre réplicas GUE com o mesmo N)**. É conservador; não trata janelas
  sobrepostas como independentes.
- z_M(L) = (V_obs − V_M)/√(σ_eff² + m_M²), com m = incerteza de τ* para Berry e m = 0 para o GUE.
  RMS_M = √(média de z_M² na grade).

## 6. Critérios (fixados antes de medir)

**Q1 (ζ, blocos b02–b10):**
- **sucesso:** RMS_Berry ≤ 2 **e** RMS_GUE ≥ 4 em pelo menos 8 dos 9 blocos;
- **falha de Berry nesta altura:** RMS_Berry > 3 em pelo menos 5 dos 9 blocos;
- **inconclusivo:** o resto.

**Q3 (χ, zeros 1–3.000):** Δχ² = Σ_{L ∈ R} (z_todos² − z_correto²), com R = {1,5; 2; 3; 4; 5; 6} para χ₋₄ e
R = {1; 1,5; 2} para χ₅, onde "correto" exclui o primo que divide q e "todos" o inclui:
- **conjunto correto preferido:** Δχ² ≥ 9, e também RMS_correto ≤ 2 na grade inteira para afirmar concordância
  quantitativa;
- **conjunto errado preferido (refutação da previsão):** Δχ² ≤ −9;
- **inconclusivo:** o resto.

A primária de Q3 é **χ₋₄**, cuja previsão tem maior separação; χ₅ é secundária.

**Descritivo (sem veredito):** b01; a média do viés de unfolding; a relação com o C3 (Var(s) abaixo do GUE); a
estimativa inversa do período da órbita mais curta a partir de V(L), que fica para ficha própria.

## 7. O que se pode concluir

- Sucesso em Q1: reprodução (B) de um resultado conhecido (Berry; Odlyzko). Liga o desvio do GUE observado no projeto
  às órbitas curtas. **Não é novidade.**
- Sucesso em Q3: demonstração numérica (B) de que remover uma órbita altera a estatística como previsto. A novidade
  depende de busca na literatura (Bogomolny–Keating trata o caso geral); rótulo C só depois dela.
- Falha: registrada como está, com o diagnóstico (modelo de τ*, extensão a χ, estimador). Nenhum critério muda
  depois da medição.
- Nada aqui é evidência a favor de RH ou de um operador de Hilbert–Pólya.

## 8. Custo

Previsão: 242 s de CPU (feita). Medição: estimada em menos de 10 min. Bem abaixo do limiar de 4 h-CPU.

*Dionatan Resende & Claude Opus — 26/09/2026.*
