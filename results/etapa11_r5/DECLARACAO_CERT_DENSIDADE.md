# Termo determinístico ρ_Δ: cota de densidade sob a base atual e projeção por a_k — declaração prévia (16/09/2026)

Gravada **antes** de qualquer código ou cálculo. SHA-256 em `DECLARACAO_CERT_DENSIDADE.sha256`.

**Reaproveita, sem alterar:** DECLARACAO_CERT.md (b7a7980c…), os adendos CORRECAO1 (0a693179…), CORRECAO2 (75eee940…) e
RECONF_C1C2 (a8253e9c…), e DECLARACAO_CERT_CONTAMINACAO.md (1d46bced…).

**Artefatos vigentes lidos, não recalculados:** `cert_tabela.csv` (execução 4; coluna `a_l1_sup`) e
`cert_contaminacao_tabela.csv` (coluna `total_sup`). `cert_calculo.py` (95bec528…) e `cert_contaminacao.py` (4baff933…)
não são modificados.

**Corte:** o mesmo, (d₁, Δ) = (8, 2), escolhido após a avaliação exploratória.

## 0. Objeto

Pela decomposição registrada (R5, notação): F_w = F* + ρ_Δ + ρ_ord, com
- ρ_Δ(t) := ∫ w(E) e_t(E) Δ(E) dE, onde e_t(E) = e^{−i(E−E_c)t};
- Δ(E) := θ′(E)/π − d̄_rvm(E).

**Densidades:**
- θ(t) = ph Γ(¼ + ½it) − ½t ln π (DLMF 25.10.2, arquivada);
- d̄_rvm(E) = (1/2π) ln(E/2π) (`src/riemann_spectra/unfolding.py`, `d_bar_rvm`).

Logo Δ(E) = (1/2π)[Re ψ(¼ + iE/2) − ln(E/2)].

**Observável alvo:** F^rvm := F* + ρ_Δ, isto é, zeros exatos na janela e densidade d̄_rvm integrada exatamente. É o F_w
sem o erro das ordenadas tabuladas nem o erro numérico.

**Desigualdade pretendida, por par:**

|a_k·(F^rvm − M_𝒦)| ≤ |a_k·(F* − M_𝒦)| + |a_k·ρ_Δ|, e o critério é

total^Δ_k := total_k (contaminação) + |a_k·ρ_Δ|^sup / |c_k|_inf ≤ 10⁻⁶.

## 1. Janela: definição fixada (achado da verificação prévia)

- **No mundo matemático,** o modelo de linhas ℓ_n usa W(·; L) e as fases e^{±iE_c log n}, e as frequências de P-RH são
  ν_A = E_c − L/2 e ν_B = E_c + L/2 (DECLARACAO_CERT §1), com L := fl(B − A). A identidade F* ↔ linhas só vale exatamente
  com a janela **centrada em E_c e de comprimento L**. Fixa-se então:

  **A\* := E_c − L/2 e B\* := E_c + L/2** (racionais exatos a partir dos floats registrados).

- **Verificado antes desta declaração:** [A*, B*] coincide exatamente com [A, B] de `metrics.json` em **15 dos 30 blocos**.
  Nos outros 15, a diferença é de ordem ulp.
  - Essa diferença pertence à camada registrada (ρ_num) e não é tratada aqui.
  - A execução 4 e a contaminação já usavam implicitamente essa mesma janela, via ν_A = E_c − L/2; nada muda nelas.

## 2. Derivação (a registrar em §II.22; fontes arquivadas)

Para E > 0 e z := ¼ + iE/2:

1. **Stirling para ψ** (DLMF 5.11.2, `dlmf_5.11.html`, SHA-256 2199a198…): ψ(z) ~ ln z − 1/(2z) − Σ_{k≥1} B_{2k}/(2k z^{2k}).
   - Por DLMF §5.11(ii): "If the sums … are terminated at k = n − 1 … and z is complex, the remainder terms are bounded in
     magnitude by sec^{2n+1}(½ ph z) for (5.11.2) times the first neglected terms."
   - Com n = 1: ψ(z) = ln z − 1/(2z) + R, |R| ≤ sec³(½ ph z)·|B₂|/(2|z|²) = sec³(½ ph z)/(12|z|²).
2. **Fase:** ph z ∈ (0, π/2), logo ½ ph z ∈ (0, π/4) e sec³(½ ph z) < 2√2.
3. **Módulo:** |z|² = 1/16 + E²/4 ≥ E²/4.
4. **Três parcelas de Δ(E)·2π** = [ln|z| − ln(E/2)] − Re(1/(2z)) + Re R:
   - ln|z| − ln(E/2) = ½ ln(1 + 1/(4E²)) ∈ [0, 1/(8E²)], porque ln(1 + x) ≤ x;
   - Re(1/(2z)) = (¼)/(2|z|²) ∈ (0, 1/(2E²)];
   - |Re R| ≤ 2√2/(12|z|²) ≤ 2√2/(3E²).
5. **Cota pontual:** |Δ(E)| ≤ C/E², com **C := (1/8 + 1/2 + 2√2/3)/(2π)**.
6. **Janela Hann:** 0 ≤ w ≤ 1 e ∫_{A*}^{B*} w = L/2. Como C/E² é decrescente e A* > 0:

   sup_t |ρ_Δ(t)| ≤ ∫ w|Δ| ≤ C·(L/2)/A*² =: D_bloco.

7. **Projeção:** o vetor do sistema é (Re ρ_Δ(t_j))_j ⊕ (Im ρ_Δ(t_j))_j, e cada entrada tem módulo ≤ |ρ_Δ(t_j)|. Logo

   **|a_k·ρ_Δ| ≤ ‖a_k‖₁ · D_bloco ≤ ‖a_k‖₁^sup · D_bloco.**

**Hipóteses:**
- nenhuma além das fontes citadas;
- **não usa RH** nesta parcela. O total continua condicional a RH por causa de B^{RH″};
- a derivada de ph Γ independe do ramo, porque d/dE Im ln Γ = Im(ψ·i/2) = ½ Re ψ.

## 3. Dependência herdada: não usada

- `results/etapa11_3b/density_error_certified.py` (dd0a55bd…) e `.json` (64a8ad49…), da revisão 11.3b-6, anteriores aos
  adendos 1–3, **não entram** no cálculo.
- Diferença de definição registrada: o script antigo usava [A − 10⁻⁶, B + 10⁻⁶] de `metrics.json`, e não [A*, B*].
- Comparação com os valores antigos: **só diagnóstico** (T21).

## 4. Método de cálculo (tudo exato, sem ponto flutuante na decisão)

- **C:** enclausurado em `mpmath.iv`, C_iv = (1/8 + 1/2 + 2·iv.sqrt(2)/3)/(2·iv.pi); **C^sup := extremo superior exato**
  (Fraction, via `hi_q`).
- **D_bloco** = C^sup·(L/2)/A*², em `Fraction` exata, com L = Fraction(fl(B − A)) e E_c = Fraction(E_c) dos floats
  registrados.
- **‖a_k‖₁^sup** = Fraction(float(`a_l1_sup`)) da execução 4. É o valor binário exato do float certificado; a leitura
  ida-e-volta é conferida.
- **|c_k|_inf** = extremo inferior exato de log p/(π√(p^r)).
- **Total da contaminação:** Fraction(`total_sup`), string já verificada como ≥ extremo superior do total exato.
- **Decisão:** total^Δ_k ≤ Fraction(1, 10⁶).
- **Exportação:** `sup_chk`, com asserção Fraction(string) ≥ valor exato.
- Script único, `cert_densidade.py`, que importa `cert_calculo.py` só pelas primitivas (`hi_q`, `lo_q`, `sup_chk`, `PI`),
  sem editá-lo. Execução com trava `--executar`.

## 5. Testes obrigatórios (antes da execução)

- **T1–T15:** reaplicação de `cert_testes.py` e `cert_contaminacao_testes.py`. Os arquivos de resultado vigentes
  (`cert_testes_resultado.json` 13a6508c…, `cert_contaminacao_testes_resultado.json` 13e8a417…) são salvos, regenerados,
  comparados byte a byte e restaurados.
- **T16 (constante C):**
  - C^sup < 0,24953;
  - C^sup ≤ cota racional elementar independente (1/8 + 1/2 + 2·(99/70)/3)/(2·3), usando √2 ≤ 99/70 (99² = 9801 ≥ 9800)
    e π > 3;
  - C^inf > 0,2495.
- **T17 (diagnóstico B da cota pontual, sem valor de prova):** em 2.000 valores de E entre 9,8·10³ e 7,4·10⁴ e em 20 valores
  de E entre 10 e 100, calcular Δ(E) com `mpmath.digamma` a 50 dígitos e verificar |Δ(E)| ≤ C^sup/E².
- **T18 (janela):**
  - A* > 0 e B* − A* = L exatamente, nos 30 blocos;
  - número de blocos com [A*, B*] ≠ [A, B] registrado (esperado 15, só diagnóstico).
- **T19 (decisão):** casos sintéticos total^Δ = 10⁻⁶ e 10⁻⁶ ± 10⁻²⁵.
- **T20 (leituras):**
  - nos 1.410 pares, Fraction(`total_sup`) ≥ B_rel_sup + Sabs_rel_sup + (P + C)/|c_k|_inf, exatamente;
  - `a_l1_sup` lido é igual nas duas tabelas vigentes;
  - repr(float(s)) reconstrói o mesmo binário.
- **T21 (diagnóstico da herança):** D_bloco novo × `cota_sup_arredondada_para_cima` antigo, por bloco. Só registro; não
  entra na decisão.

## 6. Regras de decisão, falha e leitura (fixadas agora)

- **Par certificado** ⇔ total^Δ_k ≤ 10⁻⁶ por frações exatas e todos os testes passam.
- **Nenhuma expectativa registrada como premissa.**
  - Orientação algébrica feita **com os valores herdados**, portanto não decisória: ‖a_k‖₁^sup × cota antiga acrescenta no
    máximo 5,04·10⁻⁸ em relação a |c_k| nos elegíveis (m4-v1/b01, p = 53).
- **Se falhar em linhas elegíveis:** "não certifica", sem refutar nada. Nesta entrega **não** se subdivide [A*, B*], não se
  troca 1/E² ≤ 1/A*² por integração mais fina e não se usa cancelamento em e_t.
- **Execução:** sem execução de desenvolvimento separada. O cálculo é exato e curto; a trava `--executar` só é liberada
  após os testes e a revisão.
- **Grade:** nenhuma ampliação.

## 7. O que fica estabelecido, se certificado

Para M^math, condicional a RH (F5 e J1 bibliográficas), na base de confiança declarada:

|a_k·(F^rvm − M_𝒦)| ≤ 10⁻⁶·|c_k|, com F^rvm = F* + ρ_Δ (zeros exatos, densidade d̄_rvm integrada exatamente, janela [A*, B*]).

**Não estabelece:**
- ρ_ord (ordenadas tabuladas; condicional à precisão declarada, F7);
- ρ_num (â_k em ponto flutuante, T_j em ponto flutuante, NUFFT/quadratura, [A, B] × [A*, B*] no nível ulp);
- C2;
- S1, S3a, S3c;
- H1, que continua **aberta**.

## 8. Saídas

`cert_densidade.py`, `cert_densidade_testes.py`, `cert_densidade_testes_resultado.json`, `cert_densidade_blocos.csv`
(D_bloco, A*, B*, comparação T21), `cert_densidade_tabela.csv` e `cert_densidade_resumo.json`. Todos entram em
`MANIFESTO_CERT.csv`, e os artefatos vigentes não mudam.
