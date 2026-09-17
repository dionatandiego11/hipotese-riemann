# Adendo 3 à DECLARACAO_CERT.md — eliminação da dependência herdada de c₁^sup e c₂^sup (16/09/2026)

Gravado **antes** de qualquer alteração de código ou cálculo. SHA-256 em `DECLARACAO_CERT_RECONF_C1C2.sha256`. O método de
DECLARACAO_CERT (b7a7980c…), o adendo 1 (0a693179…) e o adendo 2 (75eee940…) continuam valendo. O corte (d₁, Δ) = (8, 2)
e a base de confiança (i)–(iv), com o lema de somação de §II.19.2, não mudam.

## 1. Origem (tarefa 1)
- **Constantes:** c₁ := ‖ϕ′‖_∞ e c₂ := ‖ϕ″‖_∞, com ϕ(x) = e^{−1/x}/(e^{−1/x} + e^{−1/(1−x)}) em (0, 1).
- **Strings usadas pela execução 3:** `prh_forca_resumo.json` (SHA-256 56e4c373…), `"c1_sup": "2.000982"` e
  `"c2_sup": "9.854620"`.
- **Produzidas por:** `prh_forca.py` (SHA-256 bb9a6973…), execução de 14/09/2026, sob DECLARACAO_PRH.md, via
  `sup_str(c, 6)`.
- **Método original:**
  - malha de 20.000 subintervalos em [0,01; 0,99], com as fórmulas de ϕ′ e ϕ″ por f(x) = e^{−1/x};
  - cotas grosseiras nas pontas (0; 0,01] e [0,99; 1);
  - máximo acumulado por `iv.mpf(max(c.b, |d|.b))`.
- **Os intervalos originais não foram persistidos:** só as strings de 6 dígitos existem.
- **Nota:** `prh2_forca_resumo.json` contém "2.000984" e "9.854622", reexportações das strings anteriores com uma unidade
  a mais. Não são usadas pela execução 3.

## 2. Método escolhido (tarefa 2): **B — recálculo interno**
**O Método A (reconferência) não é executável:** os intervalos originais não existem. Uma reexecução do código original
também não serviria como reconferência, porque ele usa construções do tipo auditado nos adendos 1 e 2:
- extremos de subintervalos via `iv.mpf([(…).a, (…).b])`;
- máximos via `.b`, sem garantia demonstrada de que os subintervalos cubram [0,01; 0,99] sem lacunas;
- máximos sem garantia demonstrada de que o extremo superior seja preservado.

**Recálculo dentro de `cert_calculo.py` (execução 4):**
- **Mesma matemática.** ϕ′ = N/S² e ϕ″ = (N′S − 2NS′)/S³, com S = f(x) + f(1 − x), N = f′(x)f(1 − x) + f(x)f′(1 − x),
  N′ = f″(x)f(1 − x) − f(x)f″(1 − x), S′ = f′(x) − f′(1 − x), f′(x) = e^{−1/x}/x² e f″(x) = e^{−1/x}(1 − 2x)/x⁴. As
  derivações ficam registradas em §II.20.
- **Malha:** 20.000 subintervalos de [1/100, 99/100], com extremos racionais exatos x_i = 1/100 + i·(98/100)/20000.
  - Cada subintervalo é construído como envoltória exata: extremo inferior de iv(x_i) e extremo superior de iv(x_{i+1}),
    via `iv.make_mpf` com extremos brutos.
  - A cobertura sem lacunas é verificada por frações exatas: extremo superior do subintervalo i ≥ extremo inferior do
    subintervalo i + 1, primeiro extremo inferior ≤ 1/100 e último extremo superior ≥ 99/100.
- **Máximos:** comparação exata de extremos superiores (Fraction); o resultado é o ponto degenerado do maior extremo superior.
- **Pontas (0; δ] e [1 − δ; 1), δ = 1/100:** mesmas cotas grosseiras do código original. As hipóteses de monotonia ficam
  escritas em §II.20:
  - e^{−1/x}/x² crescente em (0, ½);
  - e^{−1/x}/x⁴ crescente em (0, ¼);
  - e^{−1/(1−x)} ≥ e^{−1/(1−δ)};
  - e^{−1/y}/y² ≤ e^{−1}/(1 − δ)² e |f″(y)| ≤ 3e^{−1}/(1 − δ)⁴ para y ∈ [1 − δ, 1);
  - simetria ϕ(1 − x) = 1 − ϕ(x).
  δ entra como intervalo que contém 1/100, avaliado em funções crescentes pelo extremo superior.
- **Fora de (0, 1):** ϕ é constante; ϕ′ = ϕ″ = 0, por extensão suave.
- **Uso no certificado:** c₁ e c₂ entram em B^{RH″} como os pontos degenerados calculados, sem strings. **Nenhuma leitura de
  `prh_forca_resumo.json`.**
- **Registro:** as strings exportadas por `sup_chk` (6 e 15 dígitos, com asserção Fraction ≥ extremo superior) ficam apenas
  como informação.

## 3. Diagnóstico (sem valor de validação)
Comparação exata dos novos extremos superiores com Fraction("2.000982") e Fraction("9.854620"):
- se os novos forem maiores, registra-se que as strings antigas **não** eram majorantes garantidas pelo cálculo novo;
- se forem menores ou iguais, registra-se só a compatibilidade.

## 4. Testes (tarefa 4)
- **T1–T8**, reaplicados ao script modificado.
- **T9:**
  - (a) cobertura exata da malha;
  - (b) c₁^sup ≥ |ϕ′| e c₂^sup ≥ |ϕ″| em 10⁴ pontos racionais de (0, 1), incluindo pontos a 10⁻⁶ das pontas e perto de
    ½, avaliados em `iv` a 50 dígitos (interseção com o extremo superior, por frações exatas);
  - (c) as pontas só com operações intervalares;
  - (d) varredura: `cert_calculo.py` não lê `prh_forca_resumo.json`, `c1_sup` nem `c2_sup`.
- **Critério adicional:** a execução 4 não pode mudar a marcação de nenhum par em relação à execução 3. Se mudar, o motivo
  é registrado e a leitura muda conforme DECLARACAO_CERT §5.

## 5. Saídas e congelamento (tarefa 6)
- **Execução 4:** `cert_calculo.py`, `cert_testes.py`, `cert_testes_resultado.json`, `cert_blocos.csv`, `cert_tabela.csv`,
  `cert_resumo.json`, com os hashes dos quatro documentos e as constantes c₁ e c₂ (extremos superiores exatos, em fração
  e decimal).
- **Execução 3** preservada como `cert_*_exec3.*`.
- **Manifesto:** `MANIFESTO_CERT.csv`, com arquivo, SHA-256, papel e execução.
- **Congelamento:** nenhuma alteração posterior sem nova declaração.

## 6. Regras de leitura (inalteradas)
- Resultado condicional a RH (F5 e J1 bibliográficas); não fecha H1.
- Auditoria integral independente continua recomendada.
