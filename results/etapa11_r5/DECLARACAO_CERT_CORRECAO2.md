# Adendo 2 à DECLARACAO_CERT.md — operações de ponto flutuante e exportação (15/09/2026)

Gravado **antes** de alterar o código. SHA-256 em `DECLARACAO_CERT_CORRECAO2.sha256`. O método de DECLARACAO_CERT
(b7a7980c…) e o adendo 1 (0a693179…) continuam valendo. Este adendo fecha lacunas de justificativa apontadas na revisão
11.3b-24.

## 1. Estado da execução 2
Os arquivos `cert_*_exec2.*` e `cert_calculo_exec2.py` ficam preservados. Os 461/461 da execução 2 são atribuídos a ela e à
sua base de confiança. A coincidência com a execução 1 não é validação. A execução 2 é **substituída** pela execução 3,
porque tem duas lacunas de justificativa:
- **L1.** `dn(vmn**4)` usa uma potência binary64 seguida de um único `nextafter`. A base de confiança declarada cobre
  +, −, ×, ÷, mas não o erro de `**`.
- **L2.** A string exportada por `sup_str` não era verificada contra o extremo superior exato. A concordância das marcações
  não verifica essa propriedade.

**Achados adicionais da mesma varredura:**
- **L3.** `math.sqrt(2)` nas comparações da região da cauda (a raiz quadrada não está na base declarada);
- **L4.** `math.pi` como cota inferior de π sem justificativa;
- **L5.** ausência de asserções de finitude nas operações vetorizadas, embora a justificativa de `isum` e de `nextafter`
  exija ausência de overflow e de valores excepcionais.

## 2. Correções
- **L1:** v⁴ por duas multiplicações dirigidas: q = dn(vmn·vmn), v4 = dn(q·q), com vmn > 0.
- **L2:** em cada exportação, verificação Fraction(string) ≥ extremo superior exato, com asserção. Novo teste T7.
- **L3:** vmin > 0 e Fraction(vmin)² ≥ 2, comparação exata.
- **L4:** π_inf := float_dn(extremo inferior exato de iv.pi).
- **L5:** asserção `np.isfinite` nas entradas e saídas de cada operação da classe I e de `isum`, e nos escalares
  convertidos.

## 3. Justificativa escrita de `isum` (a registrar em §II.19)
- **Hipóteses:**
  - IEEE-754 binary64 com arredondamento ao mais próximo;
  - toda adição executada é uma operação binária do padrão, em qualquer ordem ou árvore;
  - sem overflow, sem NaN e sem ±∞ (garantido pelas asserções L5).
- **Modelo:** fl(x + y) = (x + y)(1 + δ), com |δ| ≤ u := ε_mach/2. Vale também em subfluxo gradual, onde a adição é exata.
- **Cota:** ŝ = Σ_i x_iΠ_{k∈caminho(i)}(1 + δ_k), com caminhos de comprimento ≤ m − 1. Logo
  |ŝ − s| ≤ γ_{m−1}Σ|x_i|, com γ_n := nu/(1 − nu).
- **Soma dos módulos calculada:** Â ≥ (1 − γ_{m−1})Σ|x_i|. Logo |ŝ − s| ≤ [γ_m/(1 − γ_m)]·Â.
- **Regime:** com mε ≤ 0,1, tem-se mu ≤ 0,05, γ_m ≤ 0,0527 e γ_m/(1 − γ_m) ≤ 1,12·mu < 2mε. O fator 2mε é exato em binary64
  (m inteiro, ε potência de 2).
- **Produto e exportação:** f·Â é arredondado para cima por `nextafter`; s ∓ erro, para fora.
- **`nextafter` após operação arredondada ao mais próximo:** o resultado r é um dos dois binary64 adjacentes ao valor exato
  (ou o próprio). Portanto nextafter(r, −∞) ≤ valor exato ≤ nextafter(r, +∞), desde que não haja overflow.

## 4. Testes
- T1–T6 do adendo 1, reaplicados ao script corrigido.
- **T7:** `sup_str` e `inf_str` por frações exatas, com 6, 12 e 15 dígitos:
  - 5.000 intervalos aleatórios, de sinais e magnitudes variadas (10⁻³⁰⁰ a 10³⁰⁰);
  - casos com o extremo superior exatamente decimal (p.ex. 10⁻⁶) e muito próximo de múltiplos de 10^{−dígitos};
  - intervalos de |c_k| e dos totais.
  - **Critério:** Fraction(sup_str) ≥ extremo superior exato e Fraction(inf_str) ≤ extremo inferior exato.
- **T8:** v⁴ dirigido ≤ Fraction(vmn)⁴ em 10⁴ valores, incluindo a faixa usada (10³–10⁴).

## 5. Reexecução
- **Saídas da execução 3:** `cert_blocos.csv`, `cert_tabela.csv`, `cert_resumo.json` e `cert_testes_resultado.json`,
  registrando os hashes dos três documentos.
- **Diagnóstico:** comparação com a execução 2, sem valor de validação.
- **Regras de leitura** inalteradas.
- Continua recomendada uma auditoria integral independente.
