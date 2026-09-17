# Camada numérica ρ_num: enclausuramento direto do estimador sobre os dados tabulados e comparação com o valor registrado — declaração prévia (16/09/2026)

Gravada **antes** de qualquer código ou cálculo. SHA-256 em `DECLARACAO_CERT_NUMERICO.sha256`.

**Reaproveita, sem alterar:** DECLARACAO_CERT.md (b7a7980c…), os adendos CORRECAO1 (0a693179…), CORRECAO2 (75eee940…) e
RECONF_C1C2 (a8253e9c…), DECLARACAO_CERT_CONTAMINACAO.md (1d46bced…), DECLARACAO_CERT_DENSIDADE.md (6a69c0d7…) e
DECLARACAO_CERT_ORDENADAS.md (a3382442…).

**Lidos, não recalculados:** `cert_ordenadas_tabela.csv` (coluna `total_ordenadas_sup`), `cert_tabela.csv` (`a_l1_sup`,
só diagnóstico) e os valores registrados de m4 (§2).

**Não modificados:** `cert_calculo.py` (95bec528…), `cert_contaminacao.py` (4baff933…), `cert_densidade.py` (598871cf…),
`cert_ordenadas.py` (884de087…), o código congelado de `src/` e os runs de m4.

**Corte:** o mesmo, (d₁, Δ) = (8, 2), escolhido após a avaliação exploratória.

## 0. Verificação prévia e enquadramento

**Fatos conferidos no código congelado e nos runs (16/09/2026):**
- O estimador primário `band_conjugate` (`arithmetic.targeted_joint_fit`) resolve `np.linalg.lstsq(Mr, rhs)`. **Não forma
  â_k.**
- F(t_j) nos nós de banda vem de `OscillatoryTransform.evaluate`: soma direta de exponenciais sobre os zeros em float do CSV
  processado, menos a soma direta do termo suave em quadratura de Gauss–Legendre (painel 0,5, ordem 8). **Não usa NUFFT.**
- Os nós t_j seguem a mesma fórmula de M^math (`np.unique(linspace(T_k ∓ h, 9))`, h = 0,5·FWHM).
- O valor registrado é `fit_ratio_to_theory` em `tables/<bloco>/arithmetic_matches.csv`: 47 linhas por bloco nos 30 blocos,
  chaves iguais ao catálogo, ida-e-volta exata nos 1.410 valores. Maior |r̂ − 1| registrado: 2,77·10⁻⁶. O coeficiente
  ajustado é `fit_coefficient_real`; `amplitude_real` é a amplitude do pico detectado e **não** entra aqui.
- O "≤ 2,0·10⁻¹⁰" do PROTOCOLO §11.2 é medição B, **não** cota, e não é usado.

**Enquadramento (o que é trivial e o que é acrescentado):**
- |r̂_k − 1| **já é conhecido exatamente** por leitura: r̂_k é um float registrado. Esta etapa **não** "descobre" que
  r̂_k ≈ 1.
- Ela acrescenta duas coisas distintas:
  - **(N) Fidelidade numérica, incondicional.** O número registrado r̂_k difere por no máximo ε_k do valor **matemático**
    X_k/c_k do estimador (a_k de M^math) aplicado a F^tab (ordenadas decimais da tabela, d̄_rvm exata, janela [A*, B*]). A
    enclausura de X_k/c_k − 1 é uma medição exata sobre os dados tabulados. **Sem RH, sem H-tab.**
  - **(T) Ligação teórica, condicional.** |X_k/c_k − 1| = |a_k·(F^tab − M_𝒦)|/|c_k| ≤ total^γ_k (§II.23), sob RH, F5, J1 e
    H-tab. Com (N): **|r̂_k − 1| ≤ ε_k^sup + total^γ_k.** A desigualdade diz que a proximidade registrada é **garantida pela
    teoria sob as hipóteses**, e não só observada.
- (N) e (T) são registradas em **seções separadas** e não se misturam.

## 1. Objeto e quantidades

- **Nós e estimador:** para cada bloco, t_j (j = 1..J) são os nós de M^math, e a_k = (aR_k, aI_k) é enclausurado por Arows
  (reconstrução com parada bit a bit contra a execução 4).
- **F^tab(t)** := D(t) − S(t), com
  - D(t) = Σ_{n∈I} f̃_t(γ_n^tab), f̃_t = w·e_t em [A*, B*] e 0 fora, w(E) = sin²(π(E − A*)/L), e_t(E) = e^{−i(E−E_c)t};
  - S(t) = ∫_{A*}^{B*} w(E) d̄_rvm(E) e_t(E) dE.
- **X_k** := Σ_j [aR_kj·Re F^tab(t_j) + aI_kj·Im F^tab(t_j)] (coordenada x_k).
- **c_k** = −Λ(n_k)/(π√n_k), enclausurado com sinal.
- **ε_k** := |r̂_k − X_k/c_k|, com r̂_k = Fraction(float(s)) da string `fit_ratio_to_theory`.
- **Identidade usada em (T):** a_k·M_𝒦 = c_k exatamente, porque M_𝒦 = M^math·(c e_x) e a_k·M^math = e_{x_k}ᵀ (posto
  completo certificado). Logo X_k/c_k − 1 = a_k·(F^tab − M_𝒦)/c_k.

## 2. Método

### 2.1 Parte discreta D(t_j)

- **Pares:** para cada n ∈ I (decimais brutos de `data/raw/zeros1`, hash conferido) e cada nó t_j, com `mpmath.iv`:
  - f̃ = w·(cos φ − i sin φ), φ = (E − E_c)t_j;
  - Re = w cos φ e Im = −w sin φ;
  - zeros fora de [A*, B*] contribuem 0 (comparação exata).
- **Acumulação:** por nó, em intervalos numpy (`cc.I`, arredondamento para fora), sobre os 3.000 zeros.
- **Custo:** ~1,27·10⁶ pares por bloco, da ordem de ρ_ord (~2 h nos 30 blocos, 3 processos).

### 2.2 Termo suave S(t_j): expansão de log E e momentos fechados

Com x := E − E_c ∈ [−a, a], a := L/2 e w = cos²(πx/L) = ½ + ½cos(βx), β := 2π/L:

d̄_rvm(E_c + x) = (1/2π)[ln(E_c/2π) + ln(1 + y)], com y := x/E_c e |y| ≤ y_max := a/E_c < 1.

**(a) Resto de Taylor (elementar).** ln(1 + y) = Σ_{m=1}^{K}(−1)^{m+1}y^m/m + R_K(y), com

|R_K(y)| ≤ Σ_{m>K}|y|^m/m ≤ y_max^{K+1}/((K + 1)(1 − y_max)).

Logo |∫ w·(1/2π)R_K·e_t dx| ≤ ρ_K := (1/2π)·a·y_max^{K+1}/((K + 1)(1 − y_max)), usando ∫w = a.

**(b) Regra de corte (fixada agora).** K_bloco := menor K ≥ 1 tal que ρ_K ≤ 10⁻²⁰, com ρ_K em frações exatas (π inferior por
extremo exato). O intervalo de S(t_j) é alargado em ±ρ_K nas partes real e imaginária.

**(c) Momentos.**

S(t) = (1/2π)[ln(E_c/2π)·M_0(t) + Σ_{m=1}^{K}(−1)^{m+1}M_m(t)/(m·E_c^m)] ± ρ_K,

com M_m(t) := ∫_{−a}^{a} x^m w(x) e^{−ixt} dx = ½J_m(t) + ¼J_m(t − β) + ¼J_m(t + β) e J_m(ω) := ∫_{−a}^{a} x^m e^{−iωx} dx.

**(d) Recorrência (integração por partes), para ω ≠ 0:**
- J_0(ω) = 2 sin(ωa)/ω;
- J_m(ω) = [x^m e^{−iωx}/(−iω)]_{−a}^{a} + (m/(iω))·J_{m−1}(ω), m ≥ 1.

**Hipótese de aplicação:** ω ∈ {t_j, t_j ± β} com t_j ≥ 0,69 e β ≤ 3,2·10⁻³, logo ω > 0 (asserção exata).

**(e) Precisão.**
- `mpmath.iv` com **dps = 60** só no cálculo dos momentos, porque os termos de fronteira de J_m (~a^m/ω) se cancelam entre
  as três exponenciais (w(±a) = 0);
- a largura final de S(t_j) é conferida (T31);
- conversão para `cc.I` por extremos exatos (`ivf`).

### 2.3 X_k, ε_k e decisões

- **X_k:** por `isum` sobre Arows e o vetor [Re F^tab, Im F^tab]. X_k/c_k é um intervalo exato (c_k com sinal).
- **ε_k^sup** := extremo superior exato de |r̂_k − X_k/c_k|.
- **(N):** registra-se o intervalo de X_k/c_k − 1 e ε_k^sup. Não há limiar de aceitação: é medição.
- **(T):** certificado ⇔ ε_k^sup + total^γ_k ≤ 10⁻⁶, por frações exatas (total^γ_k lido como Fraction da string verificada).
- **Checagem de consistência, não decisória:** extremo inferior de |X_k/c_k − 1| ≤ total^γ_k. Uma violação seria
  **alarme**: indicaria defeito de implementação ou falha de alguma hipótese. A execução para, registra e **não** lê pares
  como certificados.

### 2.4 Implementação

- Script `cert_numerico.py`.
- Importa `cert_ordenadas` (tabela bruta, geometria) e `cert_contaminacao` (reconstrução), sem editar.
- Trava `--executar`.
- Exportação por `sup_chk`.

## 3. Testes obrigatórios (antes da execução completa)

- **T1–T27:** reaplicação de `cert_ordenadas_testes.py`. O resultado vigente é salvo, regenerado, comparado sem campos de
  tempo e restaurado.
  - Pelo mesmo motivo registrado na rodada 2 de ρ_ord, a meta-condição "nenhuma saída de execução criada" de ρ_ord já é
    falsa: só podem diferir `nenhuma_saida_de_execucao_criada` e `todos_passaram`.
- **T28 (leitura dos registrados):** 30 blocos × 47 linhas; chaves = catálogo; repr(float(s)) == s; coluna do estimador
  primário (`fit_ratio_to_theory`) conferida contra `targeted_fit.primary_estimator = band_conjugate` em `metrics.json`.
- **T29 (reprodução, diagnóstico):** em b01, c01 e d01, reexecutar `targeted_joint_fit` do código congelado com a
  configuração resolvida e comparar com os valores registrados. Registrar igualdade bit a bit ou a diferença máxima. **Não**
  entra na decisão.
- **T30 (momentos):** J_m(ω) pela recorrência × `mpmath.quad` a 60 dígitos, em 20 pares (m ≤ K_max, ω amostrados dos nós),
  como diagnóstico; asserção ω > 0 para todos os ω usados.
- **T31 (resto e largura):**
  - K_bloco e ρ_K exatos por bloco;
  - diagnóstico de ln(1 + y) contra a série em 1.000 valores de y;
  - largura de S(t_j) ≤ 10⁻¹⁸ em todos os nós (asserção).
- **T32 (diagnóstico do termo suave):** S(t_j) enclausurado × soma em quadratura do código congelado nos nós de 3 blocos.
  Registrar a diferença máxima; atribuída a ρ_num.
- **T33 (diagnóstico da parte discreta):** D(t_j) enclausurado em 50 zeros × `direct_exponential_sum` do código sobre os
  floats correspondentes. Registrar a diferença máxima.
- **T34 (decisões):** casos sintéticos para (T) com total = 10⁻⁶ e 10⁻⁶ ± 10⁻²⁵; caso sintético de violação da checagem de
  consistência, que deve disparar o alarme.

**Execução de desenvolvimento:** uma, em b01, com saídas descartadas. Depois dela, método, K-regra, dps e critérios ficam
travados.

## 4. Regras de decisão, falha e leitura (fixadas agora)

- **Nenhum compromisso a priori** com 461/461 em (T), nem com valor algum de ε_k.
- **Se (T) falhar em linhas elegíveis:** "não certifica (T)" para elas. (N) continua registrada. Nada é refutado. Nesta
  entrega não se refina K, dps ou método.
- **Se o alarme de consistência disparar:** a execução para, investiga-se e **nenhum** par é lido como certificado até nova
  declaração.
- **Parada bit a bit** da reconstrução contra a execução 4 nos 30 blocos: obrigatória.
- **(N)** é afirmação sobre os **dados tabulados** e o **número registrado**. Não diz nada sobre zeros verdadeiros.
- **(T)** continua condicional a RH, F5, J1 e H-tab.
- **Grade:** nenhuma ampliação.

## 5. O que fica estabelecido, se executado

**(N), incondicional, na base de confiança declarada:** para cada um dos 1.410 pares, a enclausura de X_k/c_k (estimador
matemático sobre F^tab) e a distância ε_k^sup ao valor registrado r̂_k.

**(T), sob RH, F5, J1 e H-tab:** |r̂_k − 1| ≤ ε_k^sup + total^γ_k ≤ 10⁻⁶ nos pares certificados.

**Não estabelece:**
- C2 inteiro (elegibilidade, agregação por fração, critério de fase Q);
- S1, S3a, S3c;
- H-tab, que não é certificada;
- H1, que continua **aberta**.

## 6. Saídas

`cert_numerico.py`, `cert_numerico_testes.py`, `cert_numerico_testes_resultado.json`, `cert_numerico_blocos.csv` (K, ρ_K,
larguras, diagnósticos), `cert_numerico_tabela.csv` (por par: r̂_k, intervalo de X_k/c_k − 1, ε_k^sup, total^γ_k, (T)
certificado, alarme) e `cert_numerico_resumo.json`. Todos entram em `MANIFESTO_CERT.csv`.
