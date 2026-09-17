# Etapa 11.3b / H1 — Lema de Cauda Projetada (proposta, revisão e Rota A)

**Data:** 14/09/2026.

**Estado:** proposta analítica, **não demonstrada** (revisões 11.3b-12 a 11.3b-14: §II.1b, §II.6, §II.7, §II.8).

**Notação (revisão 11.3b-14):** ν denota a frequência de borda (ν ∈ {A, B}); τ_{C2} = 10⁻⁶ é a tolerância de C2 e
S2-ratio′. Antes, as duas eram escritas τ.

Nenhum experimento novo foi executado. As únicas verificações são identidades algébricas conferidas numericamente
(classe B), sem dados de zeros.

**Escopo:** reduzir H1, no nível do estimador O₂, a uma cota explícita para a cauda projetada.

**Não altera:** C1–C3, m4-v3, os resultados de R5, nem o estado de S1 e S2-ratio′. H1 continua aberta.

---

## Parte I — Nota proposta (registro fiel do conteúdo)

### 1. Estado já estabelecido
Os resultados finitos de R5 (ETAPA11_3B_H1_R5_ESTIMADOR §3.6–§3.8) são:
- o estimador primário tem posto completo e cond(M) ≤ 1,025 nos 30 blocos;
- a contaminação finita acima de 10⁻⁶ aparece só em linhas não elegíveis;
- nas linhas elegíveis de C2, a contaminação projetada fica ≤ 10⁻⁹;
- para U ∈ [5,5; 10], o vazamento de linhas adicionais reproduz grande parte dos desvios das linhas fracas.

Esses resultados não controlam a cauda infinita e não demonstram S1, S2-ratio′, S3a ou S3c, nem reclassificam C1–C3.

### 2. Álgebra do estimador
- θ̂ − θ* = M⁺ρ.
- a_k := e_{x_k}ᵀM⁺, logo θ̂_{x_k} − c_k = a_k·ρ.
- Para C2 basta controlar a projeção a_k·ρ, não ρ em norma uniforme. É o ponto de partida de S2-ratio′.

### 3. Resposta projetada de uma linha arbitrária
- Para u = log n: ℓ_u(t) = ½[e^{iE_cu}W(t − u) + e^{−iE_cu}W(t + u)].
- Q_k(u) := a_k·ℓ_u, avaliada nos pontos de banda (vetor real empilhado).
- O que é preciso entender em Q_k: magnitude, fase, zeros, assintótica, cancelamento induzido pelas fases e interação com
  a distribuição dos n.

### 4. Decomposição do erro projetado
Com truncamento em U e amortecimento w_ε(n) = e^{−ε²(log n)²/2}:
- **4.1 Resto de S3b:** |a_k·R_{S3b}| ≤ ‖a_k‖₁Kε² =: B_{S3b,k}.
- **4.2 Mudança de pesos na soma finita:** B_{peso,k}(U, ε) := |Σ_{log n≤U}(1 − w_ε(n))c(n)Q_k(log n)|, finita, com
  c(n) = −Λ(n)/(π√n).
- **4.3 Cauda amortecida:** R_{tail,k} := Σ_{log n>U} w_ε(n)c(n)Q_k(log n) =
  −(1/π)Σ_{log n>U} e^{−ε²(log n)²/2}Λ(n)n^{−1/2}Q_k(log n).

  Alvo: |R_{tail,k}| ≤ B_{tail,k}(A, L, U, ε).

### 5. Obstáculo da majoração absoluta
Tornar Kε² pequeno exige ε pequeno. Com ε pequeno, Σ w_ε|c(n)||Q_k(log n)| cresce a uma escala inútil. É preciso explorar
oscilação.

### 6. Forma oscilatória
A cauda tem estrutura de soma aritmética oscilatória Σ Λ(n)n^{−1/2+iν}G_{k,ε}(log n) mais o termo conjugado. A frequência
ν foi proposta como E_c; ver a correção R-3.

### 7. Lema de Cauda Projetada (alvo)
Encontrar B_{tail,k}(A, L, U, ε) explícita com |Σ_{log n>U} w_ε(n)c(n)a_k·ℓ_n| ≤ B_{tail,k}, sob hipóteses declaradas. A
cota deve:
- preservar o cancelamento;
- declarar a dependência em k, A, L, U e ε;
- declarar se é incondicional, condicional a RH ou a outra hipótese;
- ser comparável com τ_{C2}.

### 8. Erro total projetado
|θ̂_k − θ_k*| ≤ B_{S3b,k} + B_{peso,k} + B_{tail,k} + B_{outros,k}. Deve existir (U, ε) com (B_{S3b} + B_{peso} + B_{tail})/|c_k| ≤ τ_{C2}.
Ver a correção R-1.

### 9. Rotas analíticas

| Rota | Ideia | Estado |
|---|---|---|
| A | derivar Q_k(u) explicitamente | Parte II |
| B | somação por partes contra S_ν(x) = Σ_{n≤x}Λ(n)n^{−1/2+iν} | avaliada em II.4 |
| C | Landau–Gonek | F9, bloqueada |
| D | fórmula truncada de S(t) | F10, bloqueada |

### 10. Relação com S1 e S2-ratio′
O lema é mais fraco que S1. O controle da cauda projetada implica S2-ratio′ sem exigir S1. É rota independente.

### 11. Critério de sucesso
Cota explícita com |Re Ĉ_k/c_k − 1| ≤ τ_{C2} (versão implementada) ou |Ĉ_k/c_k − 1| ≤ τ_{C2} (S2-complexo), com hipóteses e
constantes rastreáveis, sem ajuste aos erros observados de C2. Ver a correção R-4.

### 12. Próxima ação recomendada
Derivar Q_k(u) para a Hann e o estimador congelado, obter sua forma para u > t_max, identificar a soma aritmética
padrão e verificar qual resultado conhecido basta. Só depois escolher a rota.

### 13. Limites
Não demonstra o lema, S1 nem S2-ratio′; não fecha H1; não altera C1–C3; não reabre m4-v3; não seleciona candidato; não
substitui F9 e F10.

---

## Parte II — Revisão técnica e Rota A (executada analiticamente)

### II.1 Correções à nota

**R-1 (§8 omite a contaminação ponderada).** A decomposição exata do erro de truncamento projetado é
a_k·(F* − M_𝒦) = a_k·(F* − M_ε) + a_k·(M_ε − M_𝒦), com

M_ε − M_𝒦 = Σ_{n∈𝒦}(w_ε(n) − 1)c(n)ℓ_n + Σ_{n∉𝒦, log n≤U} w_ε(n)c(n)ℓ_n + Σ_{log n>U} w_ε(n)c(n)ℓ_n.

O termo do meio, a **contaminação ponderada** B_{lin,k}(U, ε) := |Σ_{n∉𝒦, log n≤U} w_ε(n)c(n)Q_k(log n)|, é finito e
calculável. Deve aparecer explicitamente, não diluído em "B_outros". Nas linhas não elegíveis de R5 ele chega a
~2,8·10⁻⁶|c_k|.

**R-2 (termo de pesos nas linhas do catálogo é explícito).** Para n ∈ 𝒦, a_k·ℓ_n = δ_{kn}: as colunas x de M são
exatamente ℓ_n, e M⁺M = I (posto completo). Conferido numericamente no d01: max|a_k·ℓ_n − δ_{kn}| ≤ 2,8·10⁻¹⁵ (B).
Logo:

Σ_{n∈𝒦}(w_ε(n) − 1)c(n)a_k·ℓ_n = (w_ε(n_k) − 1)c_k, e |·|/|c_k| = 1 − e^{−ε²T_k²/2} ≤ ε²T_k²/2 ≤ 12,5·ε².

Com T_k ≤ 5, **esta estratégia de orçamento** (que controla a mudança de pesos separadamente) fica ≤ τ_{C2} = 10⁻⁶ se
ε ≤ 2,8·10⁻⁴. A condição é **suficiente para esse termo**, não necessária para o erro total (§II.1b, correção 4).

**R-3 (as frequências da cauda são as bordas A e B, não E_c).** Derivado em II.2. Numericamente consistente: no d01,
linha 2⁷, os picos espectrais locais de Q_k(u) em u ∈ [6; 6,02] ficam em torno de A = 54.512 e B = 56.586, dentro da
resolução 2π/0,02 ≈ 314 (B).

**R-4 (§11 e elegibilidade).** A elegibilidade de C2 depende de ensembles nulos e de limiares estimados. O lema deve ser
enunciado **por linha k do catálogo**, com dependência em k declarada, e só depois aplicado ao conjunto elegível. Isso
evita que o enunciado analítico dependa de quantidades estatísticas.

**R-5 (escala de ε imposta por S3b; heurística).** O termo dominante de K em S3b é ½M₂*N_V ≈ ½·25·3.000 ≈ 3,8·10⁴ (d01;
K completo não avaliado). Com ‖a_k‖₁ ≤ 3,5·10⁻³ e |c_k| ≥ 0,0195, majorar B_{S3b,k}/|c_k| ≤ τ_{C2} por essa
majorante levaria a ε ≲ 1·10⁻⁵ (**ordem de grandeza heurística**, não certificada). O regime delimita o que essa
**estratégia de orçamento** exige; **não** demonstra que toda prova precise de ε ≲ 10⁻⁵ (§II.1b, correção 4). Daí a
preferência por cotas uniformes em ε.

**R-6 (pontos de banda em I).** O maior T_k é log 139 ≈ 4,934 e a meia largura é ≤ 2π/L ≈ 3·10⁻³, logo todos os pontos
de banda estão em I = [0,5; 5]. A cota uniforme de S3b se aplica a a_k·R_{S3b}.

### II.2 Forma exata de Q_k(u) para a Hann

**(a) Forma fechada da Hann.** Com os coeficientes (½, ½) de `periods.py` e v = ωL/(2π):

W(ω) = −(L/2π)·sin(πv)/(v(v² − 1)), com W(0) = L/2 e W(±2π/L) = L/4.

Derivação:
- sinc(v ± 1) = −sin(πv)/(π(v ± 1));
- logo W = (L/2)(sin πv/π)[1/v − v/(v² − 1)] = −(L/2π) sin(πv)/(v(v² − 1)).

Conferido contra `window_response`: diferença máxima ≤ 1,1·10⁻¹⁶·W(0) em 2.003 pontos (B).

**(b) Expansão exata longe da linha.** Para |v| > 1, 1/(v(v² − 1)) = Σ_{m≥1} v^{−(2m+1)}, série convergente.

**(c) Projeção.** Escreva a_k = (a^R, a^I) em ℝ^J × ℝ^J e α_j = a^R_j + i a^I_j. Para z ∈ ℂ^J,
a_k·[Re z; Im z] = Re Σ_j ᾱ_j z_j. Logo Q_k(u) = Re Σ_j ᾱ_j ℓ_u(t_j).

**(d) Separação das frequências.** Com sin(x) = (e^{ix} − e^{−ix})/(2i), E_c − L/2 = A e E_c + L/2 = B:
- e^{iE_cu} sin((t_j − u)L/2) = (1/2i)[e^{it_jL/2}e^{iAu} − e^{−it_jL/2}e^{iBu}];
- e^{−iE_cu} sin((t_j + u)L/2) = (1/2i)[e^{it_jL/2}e^{−iAu} − e^{−it_jL/2}e^{−iBu}].

Com R(v) := 1/(v(v² − 1)), v_j^∓(u) := (t_j ∓ u)L/(2π) e κ := −L/(8πi):
- Φ_A^+(u) = κΣ_j ᾱ_j e^{it_jL/2}R(v_j^−(u));
- Φ_B^+(u) = κΣ_j ᾱ_j e^{−it_jL/2}R(v_j^−(u));
- Φ_A^−(u) e Φ_B^−(u) iguais, com v_j^+(u).

Usando Re(e^{−iAu}Φ) = Re(e^{iAu}Φ̄), obtém-se, **exatamente para u na região da cauda** (onde nenhum v_j^∓(u) é igual a
0 ou ±1):

**Q_k(u) = Re{ e^{iAu}Ψ_{k,A}(u) − e^{iBu}Ψ_{k,B}(u) }**, com Ψ_{k,A} = Φ_A^+ + conj(Φ_A^−) e Ψ_{k,B} = Φ_B^+ + conj(Φ_B^−).

**Consequências:**
- A oscilação de Q_k em u vem **só** de e^{iAu} e e^{iBu}. Ψ_{k,A} e Ψ_{k,B} não oscilam com frequência da ordem de E_c;
  as fases e^{±it_jL/2} são constantes em u.
- **Mecanismo:** o vazamento da Hann nasce das bordas da janela, onde w″ salta.
- **Polos.** R(v) tem **polos** em v = 0 e v = ±1, que não são removíveis isoladamente. Só sin(πv)R(v) (isto é, W),
  ou a expressão completa após os cancelamentos, admite extensão contínua. A separação em Ψ_{k,A} e Ψ_{k,B} é usada
  **apenas** na região da cauda, longe desses polos.
- **Cota das amplitudes** para u ≥ U com **U − t_max ≥ √2·(2π/L)**, que garante |v_j^∓(u)| ≥ √2: |R(v)| ≤ 2|v|⁻³ e
  Σ_j|α_j| ≤ ‖a_k‖₁. Os cortes numéricos já examinados (U ≥ 5,5, 2π/L ≤ 3,2·10⁻³) satisfazem essa margem. Logo

  |Ψ_{k,A}(u)|, |Ψ_{k,B}(u)| ≤ (4π²/L²)‖a_k‖₁(u − t_max)⁻³.

  Com L = 2.000, ‖a_k‖₁ ≤ 3,5·10⁻³ e u − t_max ≥ ½: ≤ 2,8·10⁻⁷. Derivadas em u com o mesmo tipo de cota, um grau a mais.

### II.3 Soma aritmética padrão

Substituindo em §4.3:

R_{tail,k} = −(1/π) Re Σ_{log n>U} w_ε(n)Λ(n)[n^{−1/2+iA}Ψ_{k,A}(log n) − n^{−1/2+iB}Ψ_{k,B}(log n)].

As somas padrão são as **somas de Chebyshev torcidas** S_ν(x) := Σ_{n≤x}Λ(n)n^{−1/2+iν}, com ν ∈ {A, B}, contra os pesos
suaves G_{k,ν,ε}(u) = w_ε(u)Ψ_{k,ν}(u) = O(u⁻³).

**Observação estrutural (corrigida).** É preciso distinguir a versão **ideal** do instrumento **registrado**.
- **Ideal:** as bordas são as ordenadas exatas A* e B* do primeiro e do último zero do bloco.
- **Registrado (congelado):** as bordas são A_rec = A* + δ_A e B_rec = B* + δ_B, valores da tabela com |δ| ≤ 3·10⁻⁹
  pela precisão declarada. As frequências de Q_k são as **registradas**, porque E_c e L vêm de A_rec e B_rec.
- **Consequência:** não se afirma ressonância exata. Para um zero ρ = ½ + iγ (sob RH), o desajuste é η_ρ := γ + ν.
  Os zeros conjugados em γ ≈ −A* e −B* dão |η| ≈ |δ|, isto é, **quase ressonância**; os demais zeros próximos das bordas
  dão |η| da ordem do espaçamento.
- **Forma regularizada:** a contribuição de cada zero à integração deve ser escrita como
  (e^{iη log x} − 1)/(iη), que tende a log x quando η → 0, com a multiplicidade m_ρ e a constante do limite inferior.
  Assim ressonância e quase ressonância são tratadas juntas.
- Um δ pequeno **não** pode ser descartado uniformemente quando log x cresce sem limite: (e^{iδu} − 1)/(iδ) ≈ u só para
  u ≪ 1/|δ| ~ 3·10⁸.

### II.4 Avaliação das rotas para a soma padrão (sem demonstração)

Somação por partes (Rota B), com x = e^u:

R_tail ~ −S_ν(e^U)G(U) − ∫_U^∞ S_ν(e^u)G′(u) du, com |G′(u)| ≲ u⁻⁴ + ε²u·u⁻³.

| Informação sobre S_ν | Consequência para B_tail | Situação |
|---|---|---|
| Incondicional clássica: S_ν(x) = x^{1/2+iν}/(½+iν) + O(x^{1/2}e^{−c√log x}) | o resto cresce exponencialmente em u; a integral contra u⁻⁴ **diverge**. O termo principal x^{1/2+iν}, integrado contra o peso, fica como **subproblema pendente** (B_main, §II.6): escrevê-lo explicitamente não fornece por si a cota uniforme necessária | **insuficiente**; B_main pendente |
| Sob RH, cota grosseira via ψ(x) − x = O(√x log²x) | S_ν − termo principal = O(\|ν\| log³x); contra u⁻⁴ dá O(\|ν\|·log(1/ε)): **dependente de ε** e com fator \|ν\| ~ 10⁴–10⁵ | **insuficiente** para ε ~ 10⁻⁵ (R-5) |
| Sob RH, forma explícita truncada com zeros (S_ν ≈ termo principal − Σ_ρ x^{i(γ+ν)}/(i(γ+ν)) + erro), tratando à parte a ressonância γ = −ν | se S_ν − termo principal = O((log x)^{3−δ}) uniformemente, B_tail fica **uniforme em ε**, e ε → 0 é permitido | **plausível, não verificado**; exige fonte com enunciado explícito (**F11**) |
| Rota dual (nova, R6): reaplicar a fórmula explícita à cauda projetada com corte suave em U, obtendo zeros convoluídos com núcleo concentrado em γ ≈ −A, −B | a cauda passa a ser controlada por zeros perto das bordas e pelo termo de polo h(−i/2) = ∫g(u)e^{u/2}du, oscilatório com frequência A | **ponto crítico:** a **majoração absoluta** do termo de polo h(−i/2) produz a escala e^{1/(8ε²)}; a integral é oscilatória (frequência A), e a oscilação pode mudar radicalmente seu tamanho. A técnica adequada (integração por partes, deformação de contorno ou outra) depende do peso efetivamente escolhido; a nota **não** demonstra que sejam necessárias estimativas do tipo Gevrey. Não demonstrado |

**Conclusão da Rota A:**
- Q_k(u) está **derivado exatamente**.
- A soma aritmética padrão é S_ν com ν ∈ {A, B}, frequências nas bordas, que no instrumento são zeros.
- A rota incondicional por somação por partes **não fecha** com a informação clássica.
- A rota condicional a RH precisa de uma forma **explícita truncada** das somas torcidas (F11), com tratamento do termo
  ressonante.
- A rota dual (R6) tem um ponto crítico identificado: a estimativa oscilatória do termo de polo, cuja majoração
  absoluta não é a escala da integral.
- **Nenhuma rota foi escolhida.**

### II.1b Correções da revisão 11.3b-12

1. **Polos de R.** A frase "R contínua pelos valores-limite" foi retirada. Os polos 0, ±1 de R não são removíveis
   isoladamente; a separação Ψ_A/Ψ_B vale na região da cauda. A hipótese da cota passou a U − t_max ≥ √2·(2π/L)
   (§II.2(d)).
2. **Bordas ideais × registradas.** A "ressonância exata" foi substituída pela distinção entre bordas ideais e
   registradas, com desajuste η e fator regularizado (e^{iη log x} − 1)/(iη) (§II.3).
3. **Escala e^{1/(8ε²)}.** Passa a ser descrita como escala da **majoração absoluta**, não da integral oscilatória (R6).
   O termo principal da Rota B fica como subproblema pendente B_main.
4. **Restrições em ε.** R-2 e R-5 delimitam o regime exigido **pela estratégia de orçamento** usada; não são necessárias
   para o erro total.

### II.5 Pendências novas

| ID | Item | Natureza | Situação |
|---|---|---|---|
| F11 | forma explícita truncada de ψ(x) ou das somas torcidas Σ Λ(n)n^{−1/2+iν} com erro explícito (por exemplo Davenport, *Multiplicative Number Theory*, cap. 17; Montgomery–Vaughan, cap. 12) | fonte para a Rota B sob RH | `bloqueado` (acesso) |
| H1-QK | cota de B_{tail,k} uniforme em ε (lema-alvo) | matemático | aberto |
| H1-R6 | estimativa oscilatória de h(−i/2) na rota dual | matemático | aberto |
| B_lin | contaminação ponderada B_{lin,k}(U, ε) | cálculo finito, sem dados de zeros | não executado (a sequência numérica de R5 foi encerrada; só com nova declaração) |

### II.6 Formulação da cota uniforme em ε e no desajuste η (revisões 11.3b-12 e 11.3b-13; alvo, não demonstrado)

**Objetos:**
- bloco com bordas registradas A_rec e B_rec e bordas ideais A* e B*;
- linha k do catálogo;
- ν ∈ {A_rec, B_rec} (frequência de borda; ν > ½, de fato ≥ 9,8·10³ nas faixas m4);
- G_{k,ν,ε}(u) := w_ε(u)Ψ_{k,ν}(u) para u ≥ U, com U − t_max ≥ √2·(2π/L);
- cauda R_tail,k = −(1/π) Re[Σ_{log n>U}Λ(n)n^{−1/2+iA}G_{k,A,ε}(log n) − Σ_{log n>U}Λ(n)n^{−1/2+iB}G_{k,B,ε}(log n)].

**Enunciado-alvo L-CP(U).** Para 0 < ε ≤ ε₀:

|R_tail,k(U, ε)| ≤ B_main,k(U) + B_zeros,k(U) + B_err,k(U).

**Os três termos** devem ser **independentes de ε**, ou ter dependência residual em ε explicitamente declarada e
aceita, e uniformes no desajuste η_ρ de cada zero. A cota não pode depender de δ_A, δ_B nem de |η_ρ|⁻¹.

**Componentes:**

| Componente | Definição | Exigência | Situação |
|---|---|---|---|
| B_main,k | (1/π)Σ_ν \|I_ν(U, ε)\|, com I_ν := ∫_U^∞ e^{(1/2+iν)u}w_ε(u)Ψ_{k,ν}(u)du, a contribuição da parte contínua x^{−1/2+iν}dx de dS_ν | uniforme em ε, sem majoração absoluta | **derivada** em §II.7 (condição: U − t_max ≥ √2·2π/L) |
| B_zeros,k | contribuição dos zeros na forma regularizada, somada com pesos de multiplicidade m_ρ | uniforme em ε e η | aberto (ver abaixo) |
| B_err,k | erro da representação usada para S_ν − termo principal (por exemplo, forma explícita truncada) e fatores de zeros fora da linha | explícito | **aberto**; depende da representação escolhida |

**Ingredientes para B_zeros** (derivação elementar sobre uma representação explícita com zeros, ainda não fixada):
- **(i)** |G′(u)| ≤ w_ε(u)(|Ψ′(u)| + ε²u|Ψ(u)|), com |Ψ| ≲ (4π²/L²)‖a_k‖₁(u − t_max)⁻³ e |Ψ′| do mesmo tipo com um grau a
  mais.
- **(ii)** Para um zero ρ = ½ + iγ, com η = γ + ν e **uniformemente em η**:
  ∫_U^∞|G′(u)|·min(u − U, 2/|η|) du ≤ min(C₁, 2C₀/|η|), com C₀ = ∫|G′| e C₁ = ∫|G′|(u − U).
  - A parte de Ψ′ é finita porque (u − t_max)⁻⁴(u − U) é integrável.
  - A parte com ε²u|Ψ| usa a majorante elementar, **válida para todo ε > 0 e U > 0**:
    ∫_U^∞ u⁻¹e^{−ε²u²/2}du ≤ log⁺(1/(εU)) + √(π/2). Basta separar em u₀ = max(U, 1/ε): antes de u₀, ∫du/u; depois,
    1/u ≤ ε e ∫ε e^{−ε²u²/2}du ≤ √(π/2).
  - Assim essa parte é ≤ c·ε²(log⁺(1/(εU)) + √(π/2)), limitada uniformemente para 0 < ε ≤ ε₀.
- **(iii)** Multiplicidades: as contribuições somam-se com pesos m_ρ. As cotas de contagem já estabelecidas
  (ETAPA11_3B_Z1_CONTAGEM) incluem multiplicidade. **F2 não é necessária**; só seria usada para substituir m_ρ por 1.
- **(iv)** Limite da majorante por zero:
  - Σ_ρ m_ρ min(C₁, 2C₀/|η_ρ|) não é somável. Isso mostra que **essa estimativa por zero é insuficiente**.
  - **Não** mostra que truncamento em altura seja a única solução. Agrupamento de zeros, cancelamento entre zeros (as
    fases e^{iη_ρu} variam com ρ) ou estimativas mais fortes do fator oscilatório continuam possibilidades não
    examinadas.
  - Uma forma explícita truncada **não exige necessariamente RH**. RH simplifica o tratamento dos fatores x^{β−1/2};
    sem RH, eles precisam de controle explícito (densidade de zeros ou região livre de zeros).

**O que esta formulação estabelece e o que não estabelece:**
- **Estabelece:** a estrutura exigida da cota; o tratamento conjunto de ressonância e quase ressonância pelo fator
  regularizado; a uniformidade em ε e η do fator por zero (ii); B_main (§II.7).
- **Não estabelece:** a soma sobre zeros (iv); B_err; a representação de S_ν a usar.
- **Não escolhe rota.**

**Pendências atualizadas:**

| ID | Item | Situação |
|---|---|---|
| H1-QK-main | cota de B_main,k uniforme em ε | **derivada** (§II.7) |
| H1-QK-zeros | soma sobre zeros com pesos m_ρ e fator regularizado, uniforme em ε e η (por truncamento, agrupamento, cancelamento ou outra técnica) | aberto |
| H1-QK-err | erro da representação de S_ν, com ou sem RH | aberto; fontes F11 e F10 bloqueadas |
| H1-QK-edges | bordas registradas × ideais | tratado pela uniformidade em η; multiplicidade por pesos m_ρ (sem F2) |

### II.7 Cota de B_main uniforme em ε (derivação; revisão 11.3b-13)

**Hipóteses:**
- estimador primário de posto completo;
- U − t_max ≥ √2·(2π/L), com todos os pontos de banda t_j ≤ t_max;
- **ν > ½** (necessário para c = (ν² − ¼)/2 > 0; as bordas A, B ≥ 9,8·10³ satisfazem amplamente);
- 0 < ε ≤ ε₀;
- λ := L/(2π) e |κ| = L/(8π).

**Estrutura de Ψ.** Ψ_{k,ν}(u) é soma finita de termos c_j R(λ(t_j − u)) e c′_j R(λ(t_j + u)), com
Σ_j(|c_j| + |c′_j|) ≤ 2|κ|‖a_k‖₁ e R(v) = 1/(v(v² − 1)). Para u real, conj(Φ⁻(u)) usa R(λ(t_j + u)) com coeficientes
conjugados, porque R tem coeficientes reais. Essa expressão é analítica em u.

**Analiticidade.**
- Os polos de R(λ(t_j − u)) estão em u ∈ {t_j, t_j ± 1/λ}, reais e < U.
- Os de R(λ(t_j + u)) estão em u ∈ {−t_j, −t_j ± 1/λ}, reais e negativos.
- A integranda f(u) := e^{(1/2+iν)u}e^{−ε²u²/2}Ψ_{k,ν}(u) é analítica numa vizinhança de {Re u ≥ U, Im u ≥ 0}.

**Cota de R no semiplano.** Para v complexo com |v| ≥ √2, |v² − 1| ≥ |v|² − 1 ≥ |v|²/2, logo |R(v)| ≤ 2|v|⁻³.
- Em u = X + iy com X ≥ U e y ≥ 0: |λ(t_j − u)| ≥ λ·max(X − t_j, y) ≥ λ(U − t_max) ≥ √2.
- |λ(t_j + u)| ≥ λ(U + t_j) é ainda maior.

**Deslocamento do contorno.** Aplica-se Cauchy no retângulo [U, X] × [0, Y], com Y := ν/ε².
- **Lado direito** (Re u = X, 0 ≤ y ≤ Y): |f| ≤ e^{X/2}e^{−ε²(X² − Y²)/2}·C, que tende a 0 quando X → ∞ (ε, Y fixos).
- **Resultado:** I_ν = ∫_{vertical: U → U+iY} f + ∫_{horizontal: U+iY → ∞+iY} f.

**Segmento vertical** (u = U + iy, 0 ≤ y ≤ Y):
- |e^{(1/2+iν)u}| = e^{U/2 − νy};
- |e^{−ε²u²/2}| = e^{−ε²(U² − y²)/2} ≤ e^{ε²y²/2};
- para y ≤ ν/ε², ε²y²/2 ≤ νy/2;
- logo |f| ≤ e^{U/2}e^{−νy/2}·2|κ|‖a_k‖₁·2(λ(U − t_max))⁻³, e

  |∫_vert| ≤ 2|κ|‖a_k‖₁ · 2(λ(U − t_max))⁻³ · e^{U/2} · 2/ν.

**Segmento horizontal** (u = X + iY, X ≥ U):
- |e^{(1/2+iν)u}e^{−ε²u²/2}| = e^{X/2 − ε²X²/2}·e^{−νY + ε²Y²/2} = e^{X/2 − ε²X²/2}·e^{−ν²/(2ε²)};
- |Ψ| ≤ 2|κ|‖a_k‖₁·2(λY)⁻³;
- com ∫_ℝ e^{X/2 − ε²X²/2}dX = √(2π)ε⁻¹e^{1/(8ε²)}:

  |∫_hor| ≤ 2|κ|‖a_k‖₁ · 2(λν)⁻³ε⁶ · √(2π)ε⁻¹ · exp(−(ν² − ¼)/(2ε²)),

  que tende a 0 quando ε → 0 e é limitado para 0 < ε ≤ ε₀.

**Resultado (uniforme em ε):**

|I_ν(U, ε)| ≤ 2|κ|‖a_k‖₁ · [ 4e^{U/2} / (ν(λ(U − t_max))³) + 2√(2π)(λν)⁻³ε₀⁵ e^{−(ν² − ¼)/(2ε₀²)} ],

onde, no segundo termo, ε⁵e^{−c/ε²} (c = (ν² − ¼)/2 > 0) é crescente em ε para todo ε > 0 (derivada logarítmica
5/ε + 2c/ε³ > 0); daí o valor em ε₀.

Logo **B_main,k(U) ≤ (1/π)Σ_{ν∈{A,B}} |I_ν|**, **independente de ε**.

**Aritmética de ordem de grandeza** (cota no pior caso combinado dos parâmetros das faixas m4, não certificada):
- L ≥ 2,0·10³ (λ ≥ 318, |κ| ≤ 104 para L ≤ 2,6·10³), ν ≥ 9,8·10³, ‖a_k‖₁ ≤ 3,54·10⁻³ (R5), U = 5,5,
  U − t_max = 0,5;
- primeiro termo: 4e^{2,75}/(9,8·10³·(159)³) ≈ 1,6·10⁻⁹; vezes 2·104·3,54·10⁻³ ≈ 0,74 dá ≈ 1,2·10⁻⁹ por ν;
- B_main ≲ (2/π)·1,2·10⁻⁹ ≈ 7·10⁻¹⁰;
- relativo a min|c_k| = 0,0195: ≈ 4·10⁻⁸, cerca de **25 vezes menor** que τ_{C2} = 10⁻⁶ (margem útil, ainda estimada numericamente).

**Escopo e limites:**
- B_main **não depende de RH, de fontes externas nem dos zeros**: é uma integral de peso analítico com oscilação e^{iνu}.
- A oscilação é o que evita a escala e^{1/(8ε²)} da majoração absoluta.
- A cota vale para a parte **contínua** de dS_ν. Como S_ν − (parte contínua) é tratado — zeros, erro, representação —
  continua em B_zeros e B_err.
- A decomposição Σ_{log n>U}Λ(n)n^{−1/2+iν}G(log n) = ∫_{e^U}^∞G(log x)x^{−1/2+iν}dx + ∫G(log x)d(S_ν − M_ν)(x) é uma
  identidade de Stieltjes com M_ν(x) = x^{1/2+iν}/(½ + iν). Não depende de hipóteses sobre zeros.
- Não demonstra L-CP(U), S2-ratio′, S1 nem H1.

### II.8 Representação de S_ν − M_ν: escolha, truncamento e erro requerido (revisão 11.3b-14; formulação)

**Objetivo.** Fixar, antes de qualquer cálculo, a representação da parte não contínua da cauda, com multiplicidades e
quase ressonâncias. Nenhuma cota desta seção está demonstrada integralmente; os esboços indicam o que precisa ser
provado.

#### II.8.1 Duas representações possíveis

| Representação | Forma | Truncamento | Erro | Estado |
|---|---|---|---|---|
| **R-Perron** (fórmula explícita truncada) | S_ν(x) = M_ν(x) − Σ_{\|γ\|≤T} m_ρ x^{ρ−s}/(ρ−s) − (ζ′/ζ)(s) + Σ_k x^{−2k−s}/(2k+s) + E(x, T; s), com s = ½ − iν | em altura T = T(x) | E(x, T; s) explícito, exigido de fonte (F11) | forma padrão, **não conferida**; exige F11; somação por partes introduz 1/η e somas harmônicas (§II.6 iv) |
| **R-EF-χ** (fórmula explícita admissível aplicada à cauda com partição suave) | a cauda suave é o lado primo da forma de referência §3.1, aplicada a uma função-teste g_ν ∈ 𝒜 (ETAPA11_3B_ADMISSIBILIDADE) | **nenhum truncamento em altura**; soma completa sobre zeros | sem termo de truncamento; o erro vira as contribuições de polos, arquimediana e de zeros, cada uma a limitar | **escolhida como representação de trabalho** (§II.8.2); a **identidade** depende só da admissibilidade em 𝒜 (Connes Teorema 6 e Lema 3 conferidos; F5 e J1 bibliográficas) e vale, para cada ε > 0, somando sobre **todos** os zeros, inclusive com γ_ρ complexo; F1 ou RH entram **só nas estimativas uniformes** (revisão 11.3b-15) |

**Motivo da escolha.**
- R-EF-χ usa uma identidade já derivada para 𝒜 e dispensa F11.
- Na forma de Stieltjes, a contribuição de cada zero é uma integral oscilatória **limitada**, sem o fator 1/η: a
  singularidade em η = 0 vinha só da somação por partes. A quase ressonância fica sob controle por construção.

A R-Perron continua registrada como alternativa.

#### II.8.2 R-EF-χ: definição

**Partição suave.** Seja χ ∈ C^∞(ℝ) com χ = 0 em (−∞, U₁], χ = 1 em [U₂, ∞) e 0 ≤ χ ≤ 1, com
U₁ − t_max ≥ √2·(2π/L) e U₁ < U₂. A decomposição de §4 fica:

M_ε − M_𝒦 = Σ_{n∈𝒦}(w_ε(n) − 1)c(n)ℓ_n + Σ_{n∉𝒦}(1 − χ(log n))w_ε(n)c(n)ℓ_n + Σ_{n≥2} χ(log n)w_ε(n)c(n)ℓ_n.

- O primeiro termo, projetado, dá (w_ε(n_k) − 1)c_k (R-2).
- O segundo é **finito**, porque 1 − χ(log n) = 0 para log n ≥ U₂, e calculável: é a contaminação suavizada B_lin,χ.
- O terceiro é a **cauda suave**.

**Cauda suave projetada.** Para u ≥ U₁ vale Q_k(u) = Re{e^{iAu}Ψ_{k,A}(u) − e^{iBu}Ψ_{k,B}(u)} (§II.2(d)). Logo

a_k·Σ_n χ(log n)w_ε(n)c(n)ℓ_n = −(1/π) Re[P_A − P_B], com P_ν := Σ_{n≥2}Λ(n)n^{−1/2}g_ν(log n),

e g_ν(u) := χ(u)w_ε(u)Ψ_{k,ν}(u)e^{iνu} para u > 0, estendida par: g_ν(−u) = g_ν(u).

**Admissibilidade para cada ε > 0.** g_ν é C^∞ (χ = 0 perto de 0) e tem decaimento gaussiano com todas as derivadas.
Logo g_ν ∈ 𝒜 (as condições A1 e A2 valem com qualquer b). Pela forma de referência, com h_ν(r) = ∫_ℝ g_ν(u)e^{iru}du:

P_ν = −½[Σ_ρ m_ρ h_ν(γ_ρ) − h_ν(i/2) − h_ν(−i/2) + g_ν(0) log π − (1/2π)∫h_ν(r) Re ψ(¼ + ir/2) dr], com g_ν(0) = 0.

#### II.8.3 Componentes e cotas exigidas (uniformes em ε e no desajuste)

| Componente | Expressão | Exigência | Esboço (não demonstrado formalmente) | Hipóteses |
|---|---|---|---|---|
| **Polos** | h_ν(±i/2) = ∫_0^∞ χw_εΨ_{k,ν}e^{iνu}(e^{u/2} + e^{−u/2})du | uniforme em ε | parte e^{−u/2}: trivial. Parte e^{u/2}: separar [U₁, U₂] (compacto, limitado por e^{U₂/2}(U₂ − U₁)sup\|Ψ\|) e [U₂, ∞), onde χ = 1 e vale o deslocamento de contorno de §II.7 com U₂ no lugar de U | ν > ½; U₂ − t_max ≥ √2·2π/L |
| **Arquimediano** | −(1/2π)∫h_ν Re ψ = ½∫_0^∞ g_ν(x)K(x)dx (H2 §4–§5, com g(0) = 0) | uniforme em ε | ≤ ½∫\|χΨ\|K, com K(x) ≲ e^{−x/2} para x ≥ U₁ | (G1) de H2 para cada ε, válido para g_ν suave |
| **Zeros com \|γ\| ≤ H₀** (críticos, F1) | m_ρ h_ν(γ_ρ) = m_ρ∫_0^∞ χw_εΨ(e^{i(ν+γ)u} + e^{i(ν−γ)u})du | somável, uniforme em ε e em η± = ν ± γ | \|h_ν(γ)\| ≤ 2 min(∫\|χw_εΨ\|, ∫\|(χw_εΨ)″\|/min(η₊², η₋²)), por duas integrações por partes sem termos de fronteira. ∫\|(χw_εΨ)″\| é limitada uniformemente em ε (termos ε⁴u²·u⁻³ via a majorante log⁺ de §II.6). A soma com pesos m_ρ converge pela contagem local derivada (ETAPA11_3B_Z1_CONTAGEM §2): Σ_ρ m_ρ min(1, η⁻²) < ∞, **sem 1/η** e com quase ressonância (\|η\| ≲ 3·10⁻⁹) limitada por ∫\|χw_εΨ\| | F1; multiplicidades por m_ρ (sem F2) |
| **Zeros com \|γ\| > H₀** | idem, com γ possivelmente complexo, \|Im γ\| < ½ | uniforme em ε **ou** dependência residual declarada | sob **RH**: mesmo esboço da linha anterior, uniforme. **Sem RH**: majorando e^{\|Im γ\|u} ≤ e^{u/2} e integrando por partes, a **majorante proposta** é da ordem de e^{1/(8ε²)}·C_N·H₀^{−N}. Essa majorante **não fornece o controle desejado** no regime de ε pequeno (por exemplo, ε ≲ 10⁻⁵ da estratégia de R-5). Isso **não** demonstra que a contribuição real seja incompatível com esse regime (revisão 11.3b-15) | RH, ou dependência residual declarada |

**Erro requerido.** Em R-EF-χ não há erro de truncamento. A cota da cauda suave projetada é

|a_k·(cauda suave)| ≤ (1/π)Σ_ν ½[|polos| + |arquimediano| + Σ_ρ m_ρ|h_ν(γ_ρ)|],

e L-CP exige cada parcela uniforme em ε (ou com dependência residual declarada).

**Leitura (sem escolher resultado):**
1. **Sob RH,** todos os componentes têm esboço de cota uniforme em ε e no desajuste, com multiplicidades e quase
   ressonâncias incluídas. Resta formalizar os esboços e avaliar as constantes.
2. **Sem RH,** F1 cobre os zeros até H₀ nas estimativas. Para os zeros acima de H₀, a majorante proposta não dá
   controle uniforme no regime de ε pequeno. Isso é limite da majorante, não da contribuição real, e pede outra técnica
   (densidade de zeros, cancelamento) ou dependência residual declarada.
3. **A escolha de U₁ e U₂ tem uma troca:**
   - a cota dos zeros quase ressonantes escala com ∫|χw_εΨ| ~ (4π²/L²)‖a_k‖₁(U₁ − t_max)⁻², vezes o número de zeros com
     |η| ≲ 1 perto de ±A e ±B;
   - aumentar U₂ amplia o **conjunto de termos** incluídos na contaminação suavizada B_lin,χ. A soma tem sinais e fases,
     então **não** cresce necessariamente; só uma majorante absoluta, com uma família de cortes adequadamente ordenada,
     pode ser monótona em U₂ (revisão 11.3b-15).
   - Nenhum valor numérico dessa troca foi avaliado, e nenhuma escolha foi feita.
4. **R-EF-χ reescreve a cauda pela mesma fórmula explícita** que gera F*. Não é circular: aplica a identidade a outra
   função-teste (g_ν). A identidade usa só a admissibilidade em 𝒜; F1 ou RH entram apenas nas estimativas.

#### II.8.4 Pendências atualizadas

| ID | Item | Situação |
|---|---|---|
| H1-QK-rep | representação de S_ν − M_ν | **fixada** como R-EF-χ (proposta de trabalho); R-Perron registrada como alternativa (F11) |
| H1-QK-polos | formalizar a cota dos polos com a partição χ | aberto (esboço via §II.7) |
| H1-QK-arq | formalizar a cota arquimediana | aberto (esboço elementar) |
| H1-QK-zeros | formalizar Σ m_ρ\|h_ν(γ_ρ)\| uniforme em ε e η (\|γ\| ≤ H₀; sob RH, todos) | aberto (esboço por integração por partes e contagem local) |
| H1-QK-alto | zeros acima de H₀ sem RH | aberto; dependência residual em ε |
| B_lin,χ | contaminação suavizada finita | cálculo finito; exige nova declaração |
| F11 | fonte para R-Perron | `bloqueado`; **não necessária** para R-EF-χ |

### II.9 Proposição P-RH: cota uniforme condicional da cauda suave projetada (revisão 11.3b-15)

**Estado:** derivação escrita, **condicional a RH**. Constantes explícitas em forma simbólica, **não avaliadas
numericamente**. Finitude e uniformidade **não** garantem que a constante seja pequena o bastante para τ_{C2} = 10⁻⁶;
isso é uma verificação posterior.

#### II.9.1 Hipóteses e notação

- **(H-RH)** Todos os zeros não triviais ρ = ½ + iγ_ρ têm γ_ρ real, com multiplicidade m_ρ. F1 fica subsumida.
- **(H-EF)** Forma de referência §3.1 válida para g ∈ 𝒜 (ETAPA11_3B_ADMISSIBILIDADE; pendências só bibliográficas F5 e
  J1).
- **(H-cont)** Contagem local derivada (ETAPA11_3B_Z1_CONTAGEM §2 e §3), com multiplicidade:
  - #{γ ∈ (T − 1, T + 1]} ≤ n(T) := 10,5 log(T + 8) para T ≥ 5;
  - N(6) ≤ N₆ := 31 + 10,5 log 13.
- **Estimador e bloco:** a := ‖a_k‖₁, λ := L/(2π), κ := L/(8π) e C_Ψ := 4π²a/L².
- **Frequências:** ν ∈ {A_rec, B_rec}, com ν ≥ 9, o que vale nas faixas m4 (≥ 9,8·10³).
- **Cortes:** ϕ ∈ C^∞(ℝ) fixa, com ϕ = 0 em (−∞, 0], ϕ = 1 em [1, ∞), 0 ≤ ϕ ≤ 1, c₁ := ‖ϕ′‖_∞ e c₂ := ‖ϕ″‖_∞. Para
  U₁ < U₂, Δ := U₂ − U₁ e χ(u) := ϕ((u − U₁)/Δ).
  - Todas as derivadas de χ se anulam em U₁.
  - |χ′| ≤ c₁/Δ e |χ″| ≤ c₂/Δ², ambas suportadas em [U₁, U₂].
- **Margem:** d₁ := U₁ − t_max ≥ √2/λ e ρ₁ := 1 + t_max/d₁.
- **Amortecimento:** 0 < ε ≤ ε₀, w_ε(u) = e^{−ε²u²/2}; G := χw_εΨ_{k,ν} e g_ν(u) := G(|u|)e^{iν|u|}.

#### II.9.2 Lema 1 (derivadas de Ψ)

Para u ≥ U₁, com s := u − t_max:

|Ψ| ≤ C_Ψ s⁻³,  |Ψ′| ≤ 6C_Ψ s⁻⁴,  |Ψ″| ≤ 96C_Ψ s⁻⁵.

**Prova.**
- Ψ = Σ_j[c_jR(λ(t_j − u)) + c′_jR(λ(t_j + u))], com Σ_j(|c_j| + |c′_j|) ≤ 2κa (§II.2, §II.7), e |λ(t_j ∓ u)| ≥ λs ≥ √2.
- Para v real com v² ≥ 2: |v³ − v| ≥ |v|³/2 e |3v² − 1| ≤ 3v².
- Então R′ = −(3v² − 1)/(v³ − v)² dá |R′| ≤ 12|v|⁻⁴.
- R″ = [−6v(v³ − v) + 2(3v² − 1)²]/(v³ − v)³ dá |R″| ≤ 24v⁴/(|v|⁹/8) = 192|v|⁻⁵.
- Pela regra da cadeia, com o fator λ por derivada, e usando 4κaλ⁻³ = C_Ψ, obtêm-se as três cotas. ∎

#### II.9.3 Lema 2 (L₀ e L₂ uniformes em ε)

**L₀.** ‖G‖₁ ≤ ∫_{U₁}^∞ C_Ψ s⁻³ du = **L₀ := C_Ψ/(2d₁²)**.

**L₂.** ‖G″‖₁ ≤ **L₂**, onde

L₂ := C_Ψ·[ c₂Δ⁻²·min(Δd₁⁻³, (2d₁²)⁻¹) + 24d₁⁻⁴ + 12c₁Δ⁻¹·min(Δd₁⁻⁴, (3d₁³)⁻¹)
      + ε₀²·( (2d₁²)⁻¹ + 2c₁ρ₁Δ⁻¹·min(Δd₁⁻², d₁⁻¹) + 6ρ₁d₁⁻² )
      + ρ₁²·( (4e)⁻¹d₁⁻⁴ + ε₀⁴√(π/2) ) ].

**Prova.** Expanda G″ = χ″wΨ + χw″Ψ + χwΨ″ + 2χ′w′Ψ + 2χ′wΨ′ + 2χw′Ψ′. Use:
- |w| ≤ 1, |w′| ≤ ε²u·w, |w″| ≤ (ε⁴u² + ε²)w;
- u ≤ ρ₁s e w(u) ≤ e^{−ε²s²/2} (porque u ≥ s);
- o Lema 1 e os suportes de χ′ e χ″ em [U₁, U₂].

Termo a termo:

| Termo | Cota |
|---|---|
| χ″wΨ | ≤ (c₂/Δ²)C_Ψ·min(Δd₁⁻³, (2d₁²)⁻¹) |
| χw″Ψ | ≤ ε²C_Ψ/(2d₁²) + ε⁴ρ₁²C_Ψ∫_{d₁}^∞ s⁻¹e^{−ε²s²/2}ds ≤ ε²C_Ψ/(2d₁²) + ε⁴ρ₁²C_Ψ(log⁺(1/(εd₁)) + √(π/2)) (majorante de §II.6) |
| χwΨ″ | ≤ 96C_Ψ∫s⁻⁵ = 24C_Ψd₁⁻⁴ |
| 2χ′w′Ψ | ≤ 2(c₁/Δ)ε²ρ₁C_Ψ·min(Δd₁⁻², d₁⁻¹) |
| 2χ′wΨ′ | ≤ 2(c₁/Δ)·6C_Ψ·min(Δd₁⁻⁴, (3d₁³)⁻¹) |
| 2χw′Ψ′ | ≤ 12ε²ρ₁C_Ψ∫s⁻³ = 6ε²ρ₁C_Ψd₁⁻² |

**Uniformidade.** x⁴log⁺(1/(xd₁)) ≤ (4e)⁻¹d₁⁻⁴ para todo x > 0 (o máximo está em xd₁ = e^{−1/4}), e ε ≤ ε₀ nos demais
termos. ∎

#### II.9.4 Lema 3 (cota por zero, as duas frequências separadas)

Sob (H-RH), para todo zero:

|h_ν(γ)| ≤ min(L₀, L₂/(ν + γ)²) + min(L₀, L₂/(ν − γ)²),

com h_ν(γ) := ∫_ℝ g_ν e^{iγu}du = ∫_0^∞ G(u)[e^{i(ν+γ)u} + e^{i(ν−γ)u}]du.

**Prova.**
- Cada parcela é ≤ ‖G‖₁ ≤ L₀.
- Para η ≠ 0 real: G e G′ se anulam em U₁ (χ plana) e decaem com as derivadas no infinito (w_ε gaussiana). Duas
  integrações por partes dão ∫G e^{iηu}du = −η⁻²∫G″e^{iηu}du, de módulo ≤ L₂/η².
- Quando η = 0, vale a cota L₀. ∎

#### II.9.5 Lema 4 (soma sobre zeros com multiplicidade)

Sob (H-RH) e (H-cont), com φ(x) := min(L₀, L₂/x²):

Σ_ρ m_ρ|h_ν(γ_ρ)| ≤ Z_ν := 2·{ n(ν)·L₀ + L₂·[ 21(1,5·log(ν + 8) + 2√2) + 3N₆/(ν − 6)² + 2N₆/ν² + 5,25·(log(ν + 2) + 1)/(ν + 2) ] }.

**Prova.**

1. **Redução a γ > 0.** Pelo Lema 3, Σ_ρ m_ρ|h_ν(γ_ρ)| é **majorada** por Σ_ρ m_ρ[φ(ν + γ) + φ(ν − γ)] (não é igual a
   ela). Pela simetria γ ↦ −γ, esta última é igual a 2Σ_{γ>0} m[φ(γ − ν) + φ(γ + ν)].
   - Não há zero com γ = 0: por DLMF 25.2.3 (arquivada), ζ(½) = (1 − √2)⁻¹Σ(−1)^{n−1}n^{−1/2}, e a série alternada tem
     soma em (1 − 1/√2, 1), logo ζ(½) < 0.
2. **Parcela φ(γ − ν).** Particione (0, ∞) em I_j = (ν + 2j − 1, ν + 2j + 1].
   - **j = 0:** a contagem é ≤ n(ν) (centro ν ≥ 5) e φ ≤ L₀.
   - **j ≠ 0:** |γ − ν| ≥ 2|j| − 1 ≥ 1, logo φ ≤ L₂/(2|j| − 1)².
   - **Centros ≥ 5:** a contagem é ≤ 10,5[log(ν + 8) + log(1 + 2|j|)]. Com S₁ := Σ_{j≥1}(2j − 1)⁻² ≤ 1 + ∫_1^∞(2x − 1)⁻²dx = 3/2
     e S₂ := Σ_{j≥1}log(1 + 2j)/(2j − 1)² ≤ √2·Σ_{j≥1}(2j − 1)^{−3/2} ≤ 2√2 (usando log(1 + x) ≤ √x e 2j ≤ 2(2j − 1)),
     os j ≠ 0 somam ≤ 2·10,5·[1,5·log(ν + 8) + 2√2] = 21(1,5·log(ν + 8) + 2√2).
   - **Centros em (−1, 5)** (no máximo 3 valores de j, todos com 2|j| − 1 ≥ ν − 6): contagem ≤ N₆ cada, somando
     ≤ 3N₆/(ν − 6)².
3. **Parcela φ(γ + ν) ≤ L₂/(γ + ν)².** Particione (0, ∞) em (2j, 2j + 2].
   - **j = 0 e j = 1:** contagem ≤ N₆, com γ + ν ≥ ν.
   - **j ≥ 2:** contagem ≤ 10,5·log(2j + 9) ≤ 10,5·log(ν + 2j) (porque ν ≥ 9), com γ + ν ≥ ν + 2j. Como log y/y² é
     decrescente para y ≥ √e, Σ_{j≥2}log(ν + 2j)/(ν + 2j)² ≤ ½∫_{ν+2}^∞ log y/y² dy = ½(log(ν + 2) + 1)/(ν + 2).
   - Total ≤ L₂[2N₆/ν² + 5,25(log(ν + 2) + 1)/(ν + 2)].

Somando e multiplicando por 2 obtém-se Z_ν. ∎

#### II.9.6 Lema 5 (polos e termo arquimediano)

**Polos.** Sob ν ≥ 9 e U₂ − t_max ≥ √2/λ (automático, pois U₂ > U₁):

|h_ν(±i/2)| ≤ Pol_ν := (e^{−U₁/2} + e^{U₂/2})·L₀ + 2κa·[ 4e^{U₂/2}/(ν(λ(U₂ − t_max))³) + 2√(2π)(λν)⁻³ε₀⁵e^{−(ν² − ¼)/(2ε₀²)} ].

**Prova.**
- h_ν(±i/2) = ∫_0^∞ G e^{iνu}(e^{−u/2} + e^{u/2})du.
- A parte e^{−u/2} é ≤ e^{−U₁/2}L₀.
- A parte e^{u/2} se divide em [U₁, U₂], que é ≤ e^{U₂/2}‖G‖_{L¹[U₁,U₂]} ≤ e^{U₂/2}L₀, e [U₂, ∞), onde χ = 1 e vale a
  cota de §II.7 com U₂ no lugar de U. ∎

**Arquimediano.** |(1/2π)∫h_ν(r) Re ψ(¼ + ir/2) dr| ≤ Arq := e^{−U₁/2}(1 + (1 − e^{−U₁})⁻¹)·L₀.

**Prova.**
- Com g_ν(0) = 0, H2 §4–§5 dá (1/2π)∫h_ν Re ψ = −½∫_0^∞ G(x)e^{iνx}K(x)dx, com K(x) = 1/sinh(x/2) + 1/cosh(x/2).
  (G1) vale porque g_ν é suave com decaimento gaussiano.
- Para x ≥ U₁: 1/sinh(x/2) = 2e^{−x/2}/(1 − e^{−x}) ≤ 2e^{−U₁/2}/(1 − e^{−U₁}) e 1/cosh(x/2) ≤ 2e^{−U₁/2}. ∎

#### II.9.7 Proposição P-RH

Sob (H-RH), (H-EF), (H-cont) e as hipóteses de §II.9.1, para todo 0 < ε ≤ ε₀:

**|a_k·Σ_{n≥2}χ(log n)w_ε(n)c(n)ℓ_n| ≤ (1/π)·Σ_{ν∈{A_rec, B_rec}} ½·[ Z_ν + 2·Pol_ν + Arq ] =: B^{RH}_{χ,k}(U₁, U₂, L, ε₀).**

**Prova.** Por §II.8.2, a expressão é −(1/π)Re[P_A − P_B], com P_ν = −½[Σ_ρ m_ρh_ν(γ_ρ) − h_ν(i/2) − h_ν(−i/2) −
(1/2π)∫h_ν Re ψ], pois g_ν(0) = 0. Aplicam-se os Lemas 3, 4 e 5. ∎

**Dependências explícitas** de B^{RH}:
- em k, via a = ‖a_k‖₁;
- em L, via λ, κ e C_Ψ;
- em ν, via Z_ν e Pol_ν;
- nos cortes, via U₁, U₂, d₁, Δ, c₁ e c₂;
- em ε₀, via L₂ e Pol_ν.

**Nenhuma** depende de ε, de η_ρ ou das bordas ideais.

**O que P-RH estabelece:**
- sob RH, a cauda suave projetada tem cota **uniforme em ε**, com multiplicidades e quase ressonâncias incluídas;
- com a parte finita B_lin,χ, o termo de pesos (w_ε(n_k) − 1)c_k e o resto de S3b (que tende a 0 quando ε → 0), controla
  a_k·(F* − M_𝒦), o **resíduo ideal relativo ao catálogo**: em ε → 0 restam B_lin,χ (limite finito) e B^{RH}. **Não** se
  identifica automaticamente com o truncamento abrupto a_k·(F* − M_{≤U}) (revisão 11.3b-16).

**O que P-RH não estabelece:**
- que B^{RH}/|c_k| ≤ τ_{C2} (constantes não avaliadas);
- S2-ratio′ como enunciado verificado;
- S1, S3a e S3c;
- versão sem RH.

**Observações:**
- Os termos de L₀ com fator n(ν) ~ 10,5·log ν e os de Pol_ν com e^{U₂/2} podem dominar. A escolha de (U₁, U₂) deve ser
  declarada antes de qualquer avaliação.
- H1 continua **aberta**.

### II.10 Força da cota P-RH (avaliação sob declaração prévia; revisão 11.3b-16)

**Registro:**
- **Declaração:** `results/etapa11_r5/DECLARACAO_PRH.md`, gravada às 22:56:30 de 14/09/2026, SHA-256 `7bc392fa…`.
- **Saídas:** `prh_forca.py`, `prh_forca_tabela.csv` (30 blocos × 47 linhas × 12 combinações) e `prh_forca_resumo.json`.

**Método:**
- sem dados de zeros;
- a_k por SVD em ponto flutuante (classe B);
- aritmética da cota intervalar, com exportação arredondada para cima;
- c₁ e c₂ por enclosure intervalar.

**Corte e grade:**
- ϕ(x) = e^{−1/x}/(e^{−1/x} + e^{−1/(1−x)}), com **c₁ ≤ 2,000982** e **c₂ ≤ 9,854620**;
- d₁ = U₁ − t_max ∈ {1, 2, 4, 8}, Δ = U₂ − U₁ ∈ {0,5; 1; 2}, ε₀ = 0,1.

**Regra de leitura (fixada antes):** acima de τ_{C2} = 10⁻⁶, o resultado é "essa cota **não certifica** a tolerância", não
refutação de S2-ratio′ nem dos resultados numéricos.

#### II.10.1 Parcelas normalizadas por |c_k| (máximo sobre os 1.410 pares bloco × linha)

| d₁ | Δ | B/\|c_k\| máx | B/\|c_k\| mín | zeros máx | polos máx | arquimediano máx | pares com B/\|c_k\| ≤ τ_{C2} |
|---|---|---|---|---|---|---|---|
| 1 | 0,5 | 2,9·10⁻² | 7,7·10⁻⁴ | 2,9·10⁻² | 1,4·10⁻⁵ | 2,7·10⁻⁸ | 0 |
| 1 | 1 | 1,8·10⁻² | 5,0·10⁻⁴ | 1,8·10⁻² | 1,8·10⁻⁵ | 2,7·10⁻⁸ | 0 |
| 1 | 2 | 1,5·10⁻² | 4,0·10⁻⁴ | 1,5·10⁻² | 3,0·10⁻⁵ | 2,7·10⁻⁸ | 0 |
| 2 | 0,5 | 2,6·10⁻³ | 6,9·10⁻⁵ | 2,6·10⁻³ | 5,9·10⁻⁶ | 4,2·10⁻⁹ | 0 |
| 2 | 1 | 1,8·10⁻³ | 4,8·10⁻⁵ | 1,8·10⁻³ | 7,5·10⁻⁶ | 4,2·10⁻⁹ | 0 |
| 2 | 2 | 1,1·10⁻³ | 3,1·10⁻⁵ | 1,1·10⁻³ | 1,2·10⁻⁵ | 4,2·10⁻⁹ | 0 |
| 4 | 0,5 | 2,4·10⁻⁴ | 6,4·10⁻⁶ | 2,3·10⁻⁴ | 4,0·10⁻⁶ | 3,8·10⁻¹⁰ | 0 |
| 4 | 1 | 1,7·10⁻⁴ | 4,6·10⁻⁶ | 1,7·10⁻⁴ | 5,1·10⁻⁶ | 3,8·10⁻¹⁰ | 0 |
| 4 | 2 | 1,3·10⁻⁴ | 3,4·10⁻⁶ | 1,2·10⁻⁴ | 8,4·10⁻⁶ | 3,8·10⁻¹⁰ | 0 |
| 8 | 0,5 | 3,2·10⁻⁵ | 9,0·10⁻⁷ | 2,5·10⁻⁵ | 7,4·10⁻⁶ | 1,4·10⁻¹¹ | 2 |
| 8 | 1 | 2,6·10⁻⁵ | 7,3·10⁻⁷ | 1,6·10⁻⁵ | 9,4·10⁻⁶ | 1,4·10⁻¹¹ | 15 |
| 8 | 2 | 2,8·10⁻⁵ | 8,0·10⁻⁷ | 1,2·10⁻⁵ | 1,6·10⁻⁵ | 1,4·10⁻¹¹ | 4 |

Os máximos da tabela ocorrem nas linhas de menor |c_k|.

#### II.10.2 Mínimo sobre a grade declarada, por par (bloco, linha)

| Grupo | pares | B/\|c_k\| máx | B/\|c_k\| mín | mediana | pares ≤ τ_{C2} |
|---|---|---|---|---|---|
| todas as linhas | 1.410 | 2,6·10⁻⁵ | 7,3·10⁻⁷ | — | 15 |
| linhas elegíveis de C2 (descritivo) | 461 | 3,07·10⁻⁶ | 7,3·10⁻⁷ | 1,78·10⁻⁶ | 15 |

**Detalhe dos mínimos:**
- **Combinação:** o menor valor ocorre em (d₁, Δ) = (8, 1) para **todos** os pares. É apenas o **melhor valor entre as
  combinações declaradas**, na borda da grade, e **não** um ótimo.
- **Pares abaixo de τ_{C2}:** os 15 pares **com majorante calculada abaixo de 10⁻⁶** são todos elegíveis e todos de m4-v1. São as linhas 11 (3), 5 (2),
  7 (2), 29 (2), 3, 13, 17, 19, 23 e 43.
- **Parcelas nas elegíveis, no mínimo da grade:**
  - zeros: mediana 1,1·10⁻⁶, máximo 1,9·10⁻⁶;
  - polos: mediana 6,6·10⁻⁷, máximo 1,1·10⁻⁶;
  - arquimediano: ≤ 3·10⁻¹².

#### II.10.3 Leitura

1. **Pela regra declarada, P-RH não certifica τ_{C2} na grande maioria dos pares.** Nas linhas elegíveis, 446 de 461
   pares ficam acima; nas não elegíveis, todos. Nos 15 pares restantes, a **majorante calculada** da cauda suave fica
   abaixo de 10⁻⁶. **Não** é refutação de S2-ratio′ nem dos resultados de C2.
   - **Avaliação híbrida:** a aritmética intervalar da fórmula **não** certifica as normas ‖a_k‖₁, obtidas por SVD em
     ponto flutuante. Até haver limite rigoroso para essas normas, os 15 pares **não** estão numericamente certificados.
     P-RH continua sendo derivação condicional; sua avaliação numérica é híbrida.
2. **Nem os 15 pares são certificação de S2-ratio′.** B^{RH} controla só a cauda suave. Requisitos restantes,
   **separados por alvo**:
   - **Alvo S2-ratio′** (truncamento ideal, projetado):
     - justificar a passagem entre a cauda suave (partição χ) e o **truncamento escolhido** para o alvo, que é o
       requisito principal;
     - o termo de pesos (w_ε(n_k) − 1)c_k e o resto de S3b, que tendem a 0 quando ε → 0;
     - a parte finita B_lin,χ, se o alvo for o resíduo relativo ao catálogo (**não** é necessário calculá-la agora).
   - **Relação com o estimador registrado** (necessária para aplicar a análise ao observável congelado, mas **fora**,
     por definição, do truncamento ideal de S2-ratio′): erros de ordenadas ρ_ord, densidade ρ_Δ e implementação ρ_num.

   Tudo isso é condicional a RH e às pendências bibliográficas F5 e J1.
3. **Estrutura da cota:**
   - a parcela dos zeros cai com d₁⁻² (via L₀ e L₂);
   - a dos polos cresce com e^{U₂/2}, pela majoração absoluta do trecho compacto [U₁, U₂] (e^{U₂/2}L₀);
   - o termo arquimediano é desprezível;
   - no mínimo, zeros e polos têm ordens comparáveis.
4. **Borda da grade.** O melhor valor entre as combinações declaradas está na borda (d₁ = 8); não é um ótimo. Valores maiores de d₁ não foram avaliados, porque ficam fora da
   declaração, e não se infere que melhorariam: o termo de polos cresce exponencialmente com U₂.
5. **Refinamentos analíticos possíveis** (não executados):
   - tratar o trecho compacto dos polos com a oscilação e^{iνu} em vez da majoração absoluta;
   - refinar a contagem local (constante 10,5);
   - refinar o fator n(ν)·L₀ da parcela de zeros próximos.

**Estado:** P-RH derivada; utilidade quantitativa avaliada (certifica a cauda suave em 15 de 1.410 pares; não certifica
τ_{C2} em geral); S2-ratio′ não verificado; H1 aberta.

### II.11 Refinamento dos polos no trecho compacto por oscilação (revisão 11.3b-17)

**Motivo.** Em §II.10, a parcela dos polos é dominada pela majoração absoluta e^{U₂/2}L₀ do trecho [U₁, U₂]. Aqui ela é
substituída por uma estimativa que usa a oscilação e^{iνu}. A grade não muda.

**Lema 5′ (trecho compacto).** Nas hipóteses de §II.9.1, com z := ½ + iν (|z| ≥ ν), F := χw_εΨ_{k,ν} e
s₂ := U₂ − t_max = d₁ + Δ:

|∫_{U₁}^{U₂} F(u)e^{zu}du| ≤ e^{U₂/2}·[ C_Ψs₂⁻³/ν + (ε₀²U₂C_Ψs₂⁻³ + 6C_Ψs₂⁻⁴)/ν² + L₂/ν² ].

**Prova.**
- Integração por partes duas vezes com e^{zu} = (e^{zu}/z)′:

  ∫_{U₁}^{U₂}F e^{zu} = [F e^{zu}/z − F′e^{zu}/z²]_{U₁}^{U₂} + z⁻²∫_{U₁}^{U₂}F″e^{zu}.

- **Fronteira em U₁:** χ e todas as derivadas se anulam, logo F(U₁) = F′(U₁) = 0.
- **Fronteira em U₂:** χ = 1 e χ′ = 0, logo F(U₂) = w_εΨ(U₂) e F′(U₂) = (w_εΨ)′(U₂).
  - |F(U₂)| ≤ C_Ψs₂⁻³ (Lema 1).
  - |F′(U₂)| ≤ |w′||Ψ| + |Ψ′| ≤ ε₀²U₂C_Ψs₂⁻³ + 6C_Ψs₂⁻⁴.
- **Integral restante:** |e^{zu}| ≤ e^{U₂/2} em [U₁, U₂], e ∫_{U₁}^{U₂}|F″| ≤ ‖F″‖₁ ≤ L₂ (Lema 2). ∎

**Pol′_ν** (substitui Pol_ν de §II.9.6, com o mesmo trecho [U₂, ∞) de §II.7):

Pol′_ν := e^{−U₁/2}L₀ + e^{U₂/2}[C_Ψs₂⁻³/ν + (ε₀²U₂C_Ψs₂⁻³ + 6C_Ψs₂⁻⁴ + L₂)/ν²]
        + 2κa·[4e^{U₂/2}/(ν(λs₂)³) + 2√(2π)(λν)⁻³ε₀⁵e^{−(ν²−¼)/(2ε₀²)}].

- Continua **uniforme em ε**.
- O fator e^{U₂/2}L₀ vira e^{U₂/2}·O(C_Ψ/(νs₂³) + L₂/ν²), um ganho da ordem de 1/ν nos termos de fronteira e 1/ν² na
  integral restante.
- A Proposição P-RH vale com Pol′_ν no lugar de Pol_ν.

**Avaliação:** sob nova declaração prévia, na mesma grade (§II.12).


### II.12 Reavaliação com o Lema 5′ (avaliação híbrida, sob declaração prévia; revisão 11.3b-17)

**Registro:**
- **Declaração:** `results/etapa11_r5/DECLARACAO_PRH2.md`, gravada às 23:04:13 de 14/09/2026, SHA-256 `21a2bff3…`.
- **Saídas:** `prh2_forca.py`, `prh2_forca_tabela.csv` e `prh2_forca_resumo.json`.
- **Mudança única:** Pol_ν foi trocado por Pol′_ν; mesma grade e mesmos c₁, c₂.

**Natureza:** híbrida. ‖a_k‖₁ vem de SVD em ponto flutuante (**não certificada**) e a fórmula é avaliada em aritmética
intervalar. Os resultados são "pares com **majorante calculada** abaixo de 10⁻⁶", não pares certificados.

#### II.12.1 Por combinação (máximo e mínimo sobre os 1.410 pares, normalizados por |c_k|)

| d₁ | Δ | B máx | B mín | zeros máx | polos′ máx | arquimediano máx | pares abaixo de 10⁻⁶ |
|---|---|---|---|---|---|---|---|
| 1 | 0,5 / 1 / 2 | 2,9·10⁻² / 1,8·10⁻² / 1,5·10⁻² | 7,7·10⁻⁴ / 5,0·10⁻⁴ / 4,0·10⁻⁴ | igual a B | ≤ 2,8·10⁻⁸ | 2,7·10⁻⁸ | 0 |
| 2 | 0,5 / 1 / 2 | 2,6·10⁻³ / 1,8·10⁻³ / 1,1·10⁻³ | 6,8·10⁻⁵ / 4,7·10⁻⁵ / 3,0·10⁻⁵ | igual a B | ≤ 4,3·10⁻⁹ | 4,2·10⁻⁹ | 0 |
| 4 | 0,5 / 1 / 2 | 2,3·10⁻⁴ / 1,7·10⁻⁴ / 1,2·10⁻⁴ | 6,3·10⁻⁶ / 4,4·10⁻⁶ / 3,1·10⁻⁶ | igual a B | ≤ 4,5·10⁻¹⁰ | 3,8·10⁻¹⁰ | 0 |
| 8 | 0,5 | 2,5·10⁻⁵ | 6,7·10⁻⁷ | 2,5·10⁻⁵ | 2,0·10⁻¹⁰ | 1,4·10⁻¹¹ | 26 |
| 8 | 1 | 1,6·10⁻⁵ | 4,4·10⁻⁷ | 1,6·10⁻⁵ | 2,1·10⁻¹⁰ | 1,4·10⁻¹¹ | 221 |
| 8 | 2 | 1,2·10⁻⁵ | 3,2·10⁻⁷ | 1,2·10⁻⁵ | 2,5·10⁻¹⁰ | 1,4·10⁻¹¹ | 559 |

#### II.12.2 Melhor valor entre as combinações declaradas, por par

O melhor valor ocorre em (8, 2) para **todos** os pares. É o canto da grade, **não** um ótimo.

| Grupo | pares | B máx | mediana | B mín | pares abaixo de 10⁻⁶ | zeros: mediana (máx) | polos′: máx | arquimediano: máx |
|---|---|---|---|---|---|---|---|---|
| elegíveis de C2 (descritivo) | 461 | 1,43·10⁻⁶ | 8,2·10⁻⁷ | 3,2·10⁻⁷ | **361** (m4-v1: 159; m4-v2: 127; m4-v3: 75) | 8,2·10⁻⁷ (1,43·10⁻⁶) | 3,3·10⁻¹¹ | 3·10⁻¹² |
| não elegíveis | 949 | 1,2·10⁻⁵ | 1,35·10⁻⁶ | 4,5·10⁻⁷ | 198 | 1,35·10⁻⁶ (1,2·10⁻⁵) | 2,5·10⁻¹⁰ | 1,4·10⁻¹¹ |
| todas | 1.410 | 1,2·10⁻⁵ | — | 3,2·10⁻⁷ | 559 | — | — | — |

Entre as elegíveis acima de 10⁻⁶, as linhas mais frequentes são 2 (20 pares), 43 (13), 47 (12), 37 (11), 41 (9) e 31 (9).

#### II.12.3 Leitura

1. **O Lema 5′ tornou a parcela dos polos desprezível** (≤ 2,5·10⁻¹⁰·|c_k|). Na grade avaliada, a majorante passou a ser
   dominada **inteiramente pela parcela dos zeros**.
2. **Nas linhas elegíveis,** a majorante calculada fica abaixo de 10⁻⁶ em 361 de 461 pares e acima em 100, com máximo de
   1,43·10⁻⁶. Pela regra declarada, nos 100 pares acima e nas não elegíveis acima, **essa cota não certifica** a
   tolerância. Não é refutação de S2-ratio′ nem de C2.
3. **Abaixo de 10⁻⁶ não significa certificação:**
   - avaliação híbrida (‖a_k‖₁ em ponto flutuante);
   - condicional a RH e às pendências bibliográficas F5 e J1;
   - só a **cauda suave**. Para o alvo S2-ratio′ falta sobretudo justificar a passagem entre a cauda suave e o truncamento
     escolhido (§II.10.3, item 2).
4. **Melhor valor no canto (8, 2).** A parcela dos zeros cai com d₁ e com Δ. Valores maiores ficaram fora da declaração e
   não foram avaliados. Não se infere que melhorariam: agora cresce a parte de fronteira de Pol′ (e^{U₂/2}/ν), ainda
   desprezível na grade.
5. **Próximo refinamento localizado** (não executado): a parcela dos zeros, isto é, o termo n(ν)·L₀ dos zeros próximos
   (constante 10,5 da contagem local) e a contribuição de L₂ via 21·(1,5·log(ν + 8) + 2√2).

**Estado:** P-RH válida no escopo demonstrado (condicional a RH); avaliação numérica híbrida; com o Lema 5′, majorante
calculada abaixo de 10⁻⁶ em 361 de 461 pares elegíveis; S2-ratio′ não verificado; H1 aberta.

### II.13 Passagem da cauda suave ao truncamento abrupto (revisão 11.3b-18; formulação e derivação)

**Motivo.** P-RH e as avaliações de §II.10–§II.12 controlam a **cauda suave** T_χ := Σ_n χ(log n)w_ε(n)c(n)ℓ_n. O alvo
S2-ratio′(U) é a projeção do **truncamento abrupto**, a_k·ρ_trunc(U) = a_k·(F* − M_{≤U}), com U declarado
(ETAPA11_3B_H1_R5_ESTIMADOR §3.4). Esta seção fixa a passagem entre os dois antes de refinar a parcela dos zeros.

Nenhuma avaliação nova foi feita. A grade atual continua a mesma. F5 e J1 continuam **pendências bibliográficas**,
distintas da hipótese matemática RH.

#### II.13.1 Identidade exata para U qualquer

Para ε > 0 e qualquer U > 0 (com 𝟙 a indicadora), de 𝟙_{log n>U} = χ(log n) − 𝟙_{log n≤U}χ(log n) +
𝟙_{log n>U}(1 − χ(log n)):

Σ_{log n>U} w_ε c ℓ_n = T_χ − Σ_{log n≤U} χ(log n)w_ε c ℓ_n + Σ_{log n>U}(1 − χ(log n))w_ε c ℓ_n.

- A primeira soma de transição é **finita**, porque χ = 0 para log n ≤ U₁.
- A segunda também é **finita**, porque 1 − χ = 0 para log n ≥ U₂.

Com a decomposição de §2.2 do estimador, F* − M_{≤U} = (F* − M_ε) + Σ_{log n≤U}(w_ε − 1)cℓ_n + Σ_{log n>U}w_εcℓ_n, e
projetando por a_k:

a_k·(F* − M_{≤U}) = a_k·R_{S3b}(ε) + Σ_{log n≤U}(w_ε(n) − 1)c(n)Q_k(log n) + a_k·T_χ − Θ_k(U, ε),

com o **termo de transição**

Θ_k(U, ε) := Σ_{log n≤U} χ(log n)w_ε(n)c(n)Q_k(log n) − Σ_{log n>U}(1 − χ(log n))w_ε(n)c(n)Q_k(log n).

#### II.13.2 Limite ε → 0 (sob RH)

- O lado esquerdo **não depende de ε**.
- |a_k·R_{S3b}| ≤ ‖a_k‖₁Kε² → 0 (S3b).
- A soma de pesos é finita, e cada w_ε(n) − 1 → 0.
- Θ_k(U, ε) → Θ_k(U) := Σ_{U₁<log n≤U} χ(log n)c(n)Q_k(log n) − Σ_{U<log n<U₂}(1 − χ(log n))c(n)Q_k(log n), soma
  finita.
- |a_k·T_χ| ≤ B^{RH′}_{χ,k} uniformemente em ε (P-RH com o Lema 5′).

**Proposição P-RH-trunc.** Sob as hipóteses de P-RH, para todo U > 0:

|a_k·(F* − M_{≤U})| ≤ B^{RH′}_{χ,k}(U₁, U₂, L, ε₀) + |Θ_k(U)|.

**Prova.** Tomar ε → 0 na identidade de §II.13.1. ∎

#### II.13.3 Escolha do truncamento abrupto

| Escolha | Θ_k(U) | Leitura |
|---|---|---|
| **U = U₂** | Σ_{U₁<log n≤U₂} χ(log n)c(n)Q_k(log n) | só linhas da faixa de transição (U₁, U₂], com pesos χ |
| U = U₁ | −Σ_{U₁<log n<U₂}(1 − χ(log n))c(n)Q_k(log n) | mesma faixa, com pesos 1 − χ |
| U < U₁ (por exemplo, U ∈ [5,5; 10] de R5, com U₁ = 13) | −Σ_{U<log n<U₂}(1 − χ(log n))c(n)Q_k(log n) | inclui **inteiras** as linhas de (U, U₁], do tipo contaminação, que em R5 chegam a ~2,8·10⁻⁶·\|c_k\| nas não elegíveis; é outro alvo |

**Proposta:** declarar **U = U₂** para cada combinação da grade, de modo que o alvo S2-ratio′(U₂) e P-RH usem o mesmo
corte superior. O alvo S2-ratio′(U) depende de U; resultados para U diferentes não são intercambiáveis.

#### II.13.4 Orçamento total para S2-ratio′(U₂)

**Condição suficiente** (sob RH; F5 e J1 bibliográficas; avaliação híbrida enquanto ‖a_k‖₁ e Q_k vierem de ponto
flutuante):

(B^{RH′}_{χ,k} + |Θ_k(U₂)|)/|c_k| ≤ τ_{C2}.

**Quanto a parcela dos zeros precisa diminuir.** Com Θ_k(U₂) conhecido, a margem disponível para a cauda suave é
τ_{C2}|c_k| − |Θ_k(U₂)|. Se ela for ≤ 0 para algum par, nenhum refinamento de B^{RH′} basta para esse par com esse corte.

**Sobre Θ_k(U₂):**
- É uma **soma finita e determinística** (não calculada exatamente: envolve funções transcendentes e M⁺; ver §II.14), sem dados de zeros, sobre as potências de primo com U₁ < log n ≤ U₂. No canto
  (d₁, Δ) = (8, 2), isso é log n ∈ (13, 15], ou seja, n ∈ (4,4·10⁵; 3,3·10⁶].
- Tem sinais e fases (n^{iA}, n^{iB} via Q_k). Sua majoração absoluta não é seu tamanho.
- **Majorante absoluta, só como ordem de grandeza** (heurística, não usada para decidir):
  Σ_{U₁<log n≤U₂}Λ(n)n^{−1/2}·C_Ψ(log n − t_max)⁻³/π ≈ 2(e^{U₂/2} − e^{U₁/2})·C_Ψ/(π d₁³). No canto (8, 2), com
  C_Ψ ≈ 3,5·10⁻⁸, dá ≈ 2,3·10³·3,5·10⁻⁸/(π·512) ≈ 5·10⁻⁸, ou seja, ≈ 2,5·10⁻⁶ relativo a |c_k| = 0,0195. **Essa
  majorante não permite concluir**; o valor exato da soma pode ser muito menor.
- **Cálculo de Θ_k(U₂):** finito e determinístico; executado em §II.14 (ponto flutuante, classe B). Exige declaração prévia (grade atual,
  U = U₂, 30 blocos × 47 linhas). Não é avaliação voltada a aumentar a contagem abaixo da tolerância: completa o
  orçamento do alvo.

#### II.13.5 Estado

| Item | Situação |
|---|---|
| Passagem cauda suave → truncamento abrupto | **derivada** (identidade exata + limite ε → 0; P-RH-trunc) |
| Truncamento escolhido | U = U₂, declarado (`DECLARACAO_THETA.md`) |
| Termo de transição Θ_k(U₂) | calculado sob declaração (§II.14; B) |
| Orçamento S2-ratio′(U₂) | (B^{RH′} + \|Θ_k(U₂)\|)/\|c_k\| ≤ τ_{C2}, suficiente |
| Refinamento da parcela dos zeros | margem conhecida (§II.14); refinamento não iniciado |
| H1 | aberta |

### II.14 Cálculo de Θ_k(U₂) sob declaração prévia (revisão 11.3b-19; classe B)

**Declaração:** `results/etapa11_r5/DECLARACAO_THETA.md` (SHA-256 4b6959bb…), gravada antes do cálculo e conferida pelo
script. Grade, blocos e linhas mantidos: 12 combinações (d₁, Δ) × 30 blocos × 47 linhas = 16.920 registros.
**Saídas:** `theta_calculo.py` (SHA-256 0d4c0868…), `theta_tabela.csv` (0c253822…) e `theta_resumo.json` (1b6f8088…).

#### II.14.1 Natureza do resultado

- **Finito e determinístico não significa calculado exatamente.** Θ_k(U₂) envolve fases e^{±iE_c log n}, a resposta
  W (seno), log n e M⁺ (SVD), tudo em ponto flutuante de dupla precisão. O resultado é **classe B**.
- **Erro numérico estimado, não certificado:** δ·S_abs + n_termos·ε_mach·max|termo|, com δ = 10⁻⁹ declarado.
- **Diagnósticos de estabilidade (B; não são cotas de erro):**
  - a forma fechada de W coincide com `window_response` até 1,4·10⁻¹³ em ω ∈ [7, 40] (bloco b01);
  - recalculando Θ com `window_response` em (1; 0,5) e (8, 2), nos blocos b01, c01 e d01, a diferença máxima é
    6,4·10⁻¹⁶·|c_k|;
  - a_k·ℓ_n = δ_kn nas 47 linhas até 4·10⁻¹⁵ (b01; conferência fora do script).
- **Observação (revisão 11.3b-20):** a diferença entre as duas avaliações de W (≤ 6,4·10⁻¹⁶|c_k|) supera o erro
  estimado (≲ 10⁻¹⁷|c_k|). A regra declarada **subestimou a discrepância** e não é cota do erro de ponto flutuante.
  - A comparação entre implementações é **diagnóstico de estabilidade**, não cota de erro.
  - "Margem positiva após descontar o erro estimado" **não acrescenta garantia** além da margem calculada.
  - A leitura exploratória não muda: as margens são mais de 10⁷ vezes maiores que as discrepâncias observadas.
- **Colunas adicionais** (não previstas na declaração, só aditivas): `S_abs` (soma dos módulos), `margem_rel` e
  `orcamento_rel_com_err`.

#### II.14.2 Resultados separados por U₂ (cada corte é um alvo distinto)

| d₁ | Δ | U₂ | termos | max\|Θ\|/\|c\| | mediana\|Θ\|/\|c\| | max S_abs/\|c\| | margem > 0 (todas; elegíveis) | orçamento ≤ 10⁻⁶ (todas; elegíveis) | min orçamento |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0,5 | 6,5 | 45 | 3,33e-9 | 2,59e-11 | 1,13e-8 | 1410/1410; 461/461 | 0; 0 | 7,70e-4 |
| 1 | 1 | 7,0 | 111 | 2,25e-9 | 2,53e-11 | 1,33e-8 | 1410; 461 | 0; 0 | 4,95e-4 |
| 1 | 2 | 8,0 | 367 | 1,89e-9 | 1,98e-11 | 1,45e-8 | 1410; 461 | 0; 0 | 4,01e-4 |
| 2 | 0,5 | 7,5 | 99 | 1,21e-9 | 1,19e-11 | 3,98e-9 | 1410; 461 | 0; 0 | 6,84e-5 |
| 2 | 1 | 8,0 | 256 | 1,25e-9 | 1,23e-11 | 5,86e-9 | 1410; 461 | 0; 0 | 4,74e-5 |
| 2 | 2 | 9,0 | 859 | 6,94e-10 | 9,33e-12 | 8,69e-9 | 1410; 461 | 0; 0 | 3,02e-5 |
| 4 | 0,5 | 9,5 | 574 | 2,64e-10 | 3,55e-12 | 1,76e-9 | 1410; 461 | 0; 0 | 6,29e-6 |
| 4 | 1 | 10,0 | 1.464 | 2,19e-10 | 3,44e-12 | 3,19e-9 | 1410; 461 | 0; 0 | 4,43e-6 |
| 4 | 2 | 11,0 | 5.071 | 2,16e-10 | 3,56e-12 | 6,17e-9 | 1410; 461 | 0; 0 | 3,13e-6 |
| 8 | 0,5 | 13,5 | 21.646 | 1,83e-11 | 5,38e-13 | 1,91e-9 | 1410; 461 | 26; 25 | 6,69e-7 |
| 8 | 1 | 14,0 | 56.063 | 4,44e-11 | 8,14e-13 | 4,10e-9 | 1410; 461 | 221; 163 | 4,37e-7 |
| 8 | 2 | 15,0 | 197.912 | 4,99e-11 | 8,89e-13 | 9,38e-9 | 1410; 461 | 559; 361 | 3,20e-7 |

Os valores de U₂ = 8,0 em (1, 2) e (2, 1) coincidem no corte, mas χ difere. São registros distintos.

**Leitura:**
1. **Margem 10⁻⁶|c_k| − |Θ_k(U₂)| positiva, na avaliação B, em todos os 16.920 registros.** Descontar o erro
   estimado não acrescenta garantia (§II.14.1).
   |Θ_k|/|c_k| ≤ 3,4·10⁻⁹ em toda a grade e ≤ 5·10⁻¹¹ em d₁ = 8. Na avaliação B, o termo de transição não é o obstáculo em nenhum
   par. **Para reduzir a majorante calculada**, o que falta está só na parcela dos zeros de B^{RH′}. **Para
   certificação**, faltam ainda limites rigorosos para as normas obtidas por SVD (‖a_k‖₁, Q_k) e para os cálculos
   finitos (incluindo Θ_k).
2. **Θ é desprezível no orçamento:** max |Θ_k|/B^{RH′}_{χ,k} ≤ 4,8·10⁻⁶ em toda a grade. A contagem com orçamento
   ≤ 10⁻⁶ é **idêntica** à de §II.12 em cada combinação (0 mudanças; com e sem o erro estimado). Em (8, 2): elegíveis
   361/461 (máx 1,43e-6; mediana 8,19e-7; m4-v1 159, m4-v2 127, m4-v3 75); todas 559/1410.
3. **A majorante heurística de §II.13.4 (≈ 2,5·10⁻⁶ relativo em (8, 2)) era frouxa.** Mesmo a soma dos módulos
   S_abs fica ≤ 9,4·10⁻⁹|c_k|, cerca de 270 vezes menor. Logo, **para a soma finita de transição examinada** (cuja soma
   dos módulos foi calculada, em B), a pequenez de Θ_k não depende de cancelamento de sinais. Essa afirmação não se
   estende à cauda suave nem ao resíduo real.
   Em (8, 2), Θ_k é positivo em 675 e negativo em 735 dos 1410 pares.
4. O melhor valor segue no canto (8, 2) da grade declarada. É o melhor entre as combinações declaradas, não um ótimo.

#### II.14.3 Regras de leitura (fixadas na declaração)

- Margem positiva **não** certifica S2-ratio′(U₂): o resultado é B, e a condição suficiente continua condicional a RH
  (F5 e J1 bibliográficas) e híbrida.
- Onde o orçamento excede 10⁻⁶ (elegíveis: 100/461 em (8, 2)), a condição suficiente **não fecha** para esse par e corte.
  Isso **não** refuta S2-ratio′ nem exclui compensação no resíduo real.
- Nenhum refinamento da parcela dos zeros foi feito nesta etapa.

#### II.14.4 Estado

| Item | Situação |
|---|---|
| Θ_k(U₂), 12 cortes × 1410 pares | calculado (B), margens todas positivas |
| Orçamento S2-ratio′(U₂), condição suficiente | ≤ 10⁻⁶ em 361/461 elegíveis e 559/1410 pares, só em (8, 2); resultado híbrido, sob RH |
| Gargalo | para reduzir a majorante: parcela dos zeros de B^{RH′}; para certificar: também normas por SVD e cálculos finitos |
| Refinamento da parcela dos zeros | liberado pela margem conhecida; não iniciado |
| H1 | aberta |

### II.15 Parcela dos zeros: decomposição e refinamento analítico (revisão 11.3b-20)

**Escopo:** cortes, alvos, grade, blocos e linhas inalterados. Nenhum dado de C2 é usado. Nenhuma constante é ajustada
a erros observados.

**Estado geral (inalterado):** orçamento exploratório completo; P-RH-trunc condicional; H1 aberta.

#### II.15.1 Decomposição de Z_ν (passos 1 e 2)

**Declaração:** `results/etapa11_r5/DECLARACAO_ZDEC.md` (SHA-256 34e51253…), gravada antes do cálculo.
**Saídas:** `zdec_calculo.py` (3f8b8349…), `zdec_tabela.csv` (6e7869d2…) e `zdec_resumo.json` (17580a57…).
**Aritmética:** intervalar, com ‖a_k‖₁ em ponto flutuante (híbrida).

Z_ν/2 foi repartida, sem alterar constantes, em:

| Parte | Zeros cobertos | Constante |
|---|---|---|
| P0 = n(ν)L₀ | \|γ − ν\| ≤ 1 (j = 0) | L₀ |
| P1a = 21(log(ν + 8) + log 3)L₂ | 1 < \|γ − ν\| ≤ 3 (j = ±1) | L₂ |
| P1b = 21(0,5·log(ν + 8) + 2√2 − log 3)L₂ | \|j\| ≥ 2, centro ≥ 5 | L₂ |
| P2 = 3N₆(ν − 6)⁻²L₂ | centros em (−1, 5) | L₂ |
| P3 = (2N₆ν⁻² + 5,25(log(ν + 2) + 1)/(ν + 2))L₂ | parcela espelhada φ(γ + ν) | L₂ |

**Agrupamentos:** "próximos de ±ν" = P0 + P1a; "distantes" = P1b + P2 + P3.

**Desvio da declaração (registrado):**
- A conferência declarada (soma das partes contra `zeros_rel_sup` de PRH2, desvio relativo < 10⁻⁹) **não foi
  satisfeita**: o desvio máximo foi 2,2·10⁻⁵.
- **Causa:** a tabela PRH2 exporta cotas superiores com 12 casas decimais, mais uma unidade de margem. Para valores
  ~3·10⁻⁷, essa granularidade chega a ~10⁻⁵ relativo. A tolerância declarada era incompatível com a exportação.
- **Conferência posterior**, adicionada e marcada como tal: desvio absoluto ≤ 8,0·10⁻¹², dentro de 6 × 2·10⁻¹² (seis
  valores arredondados).
- **A conferência declarada continua registrada como falha.** A verificação posterior explica a compatibilidade com o
  arredondamento, mas **não a aprova retrospectivamente**. Declarações futuras que comparem com tabelas exportadas devem
  fixar a tolerância pela granularidade da exportação.

**Resultados (frações da majorante dos zeros; faixas sobre blocos e linhas):**

| (d₁, Δ) | L₂/L₀ | P0 (L₀) | P1a | P1b | P2 + P3 | próximos | distantes |
|---|---|---|---|---|---|---|---|
| (1; 0,5) | 127 | 0,002 | 0,62 | 0,37–0,38 | < 3·10⁻⁵ | 0,62–0,63 | 0,37–0,38 |
| (2; 1) | 31,1 | 0,009 | 0,61–0,62 | 0,37–0,38 | idem | 0,62–0,63 | 0,37–0,38 |
| (4; 2) | 8,00 | 0,034 | 0,60–0,61 | 0,36–0,37 | idem | 0,63–0,64 | 0,36–0,37 |
| (8; 0,5) | 6,81 | 0,040 | 0,60 | 0,36 | idem | 0,64 | 0,36 |
| (8; 1) | 4,35 | 0,061 | 0,58–0,59 | 0,35–0,36 | idem | 0,64–0,65 | 0,35–0,36 |
| (8; 2) | 3,12 | 0,083 | 0,57 | 0,34–0,35 | idem | 0,65–0,66 | 0,34–0,35 |

As 12 combinações estão em `zdec_resumo.json`.

**Pares elegíveis com orçamento > 10⁻⁶ em (8, 2), 100 pares:**
- P0 0,083–0,084; P1a 0,572–0,574; P1b 0,342–0,345;
- a parcela dos zeros é ≥ 0,99998 do orçamento.

**Leitura (sobre a majorante; as frações identificam onde a cota perde precisão e não descrevem a distribuição real das contribuições dos zeros):**
1. A contribuição de L₂ domina, com 92–99,8% conforme o corte. n(ν)L₀ é ≤ 8,4%.
2. As janelas adjacentes j = ±1 (P1a) sozinhas respondem por ~57–62%, mais que a janela central.
3. P2 e P3 são desprezíveis.
4. Duas folgas do Lema 4 ficam identificadas:
   - **(F-a)** Nas janelas j ≠ 0, o Lema 4 usa L₂/(2|j| − 1)² **sem** tomar o mínimo com L₀, embora o Lema 3 dê
     min(L₀, L₂/η²). Como L₂/L₀ > 1 em toda a grade, em j = ±1 a cota usa L₂ onde L₀ basta.
   - **(F-b)** Todas as partes principais (P0, P1a, P1b) carregam a contagem local 10,5·log(T + 8) por janela de largura 2,
     obtida por Jensen (ETAPA11_3B_Z1_CONTAGEM §2), que é grosseira. Só como orientação, sem uso em decisão: a densidade
     média heurística de zeros, (1/2π)log(T/2π), dá ~2,4 zeros por janela em T ~ 10⁴, contra a cota ~97.

#### II.15.2 Lema 4′ (refinamento de F-a; derivado)

**Enunciado.** Sob as hipóteses do Lema 4, seja J := min{j ≥ 1 : (2j − 1)² ≥ L₂/L₀}. Então:

Σ_ρ m_ρ|h_ν(γ_ρ)| ≤ Z′_ν := 2·{ n(ν)L₀ + 21·[ L₀·Σ_{1≤j<J}(log(ν + 8) + log(1 + 2j)) + L₂·(log(ν + 8)·S₁(J) + S₂(J)) ]
                         + L₂·[ 3N₆/(ν − 6)² + 2N₆/ν² + 5,25(log(ν + 2) + 1)/(ν + 2) ] },

com:
- S₁(J) := (2J − 1)⁻² + 1/(2(2J − 1));
- S₂(J) := log 3·S₁(J) + σ(J), onde:
  - σ(1) := log 3/9 + (log 3 + 1)/6;
  - σ(J) := log(2J − 1)/(2J − 1)² + (log(2J − 1) + 1)/(2(2J − 1)) para J ≥ 2.

**Prova.**
1. Mesma partição do Lema 4.
2. Nas janelas j ≠ 0 com centro ≥ 5, todo zero tem |γ − ν| > 2|j| − 1. Pelo Lema 3, φ(γ − ν) ≤ min(L₀, L₂/(2|j| − 1)²).
   Esse mínimo é L₀ para |j| < J e L₂/(2|j| − 1)² para |j| ≥ J.
3. **Contagem:** 10,5[log(ν + 8) + log(1 + 2|j|)], como no Lema 4. Somando os dois sinais de j, obtém-se o fator 2·10,5 = 21.
4. **Cauda Σ_{j≥J}(2j − 1)⁻²:** é ≤ (2J − 1)⁻² + ∫_J^∞(2x − 1)⁻²dx = S₁(J).
5. **Cauda Σ_{j≥J}log(1 + 2j)(2j − 1)⁻²:**
   - 1 + 2j ≤ 3(2j − 1) dá log(1 + 2j) ≤ log 3 + log(2j − 1).
   - f(y) := log y/y² é decrescente para y ≥ √e. Para 2J − 1 ≥ 3: Σ_{j≥J}f(2j − 1) ≤ f(2J − 1) + ½∫_{2J−1}^∞ f(y)dy =
     f(2J − 1) + (log(2J − 1) + 1)/(2(2J − 1)).
   - Para J = 1, o termo j = 1 é log 1 = 0 e o resto começa em y = 3, o que dá σ(1).
6. P2 e P3 ficam inalteradas (majorantes válidas; o mínimo com L₀ também caberia, mas é irrelevante). ∎

**Observações:**
- Z′_ν ≤ Z_ν sempre: S₁(1) = 3/2 e S₂(1) ≤ 2,12 < 2√2; para J ≥ 2, cada janela trocada tem L₀ < L₂/(2j − 1)².
- J depende só de (d₁, Δ, ε₀), via L₂/L₀, e não de k nem de L: em (8, 2), J = 2; em (1; 0,5), J = 7.
- **Não avaliado.** A força do Lema 4′ na grade exige nova declaração. Pela estrutura (frações de §II.15.1 e L₂/L₀
  = 3,12), a redução esperada em (8, 2) é da ordem de um fator ~2 na majorante dos zeros. É estimativa algébrica, não
  contagem de pares, e não é usada para decidir.

#### II.15.3 Lema C (refinamento de F-b): contagem local pela fórmula explícita, sob RH (formulado; não derivado)

**Ideia.**
- **Hipóteses estritas (revisão 11.3b-21):** 0 < σ < π; φ₀ ∈ C_c^∞(ℝ) par, real, ≥ 0, φ₀ ≢ 0, com suporte em
  [−σ/2, σ/2]; T > 1.
  - σ < π garante cos(σ/2) > 0: em σ = π, o denominador abaixo se anula.
  - T > 1 separa as janelas (T − 1, T + 1] e [−T − 1, −T + 1), usadas no fator 2.
  - φ₀ ≢ 0 e φ₀ ≥ 0 dão ∫φ₀ > 0.
- Tomar g_T(u) := 2(φ₀∗φ₀)(u)cos(Tu), que é par, C_c^∞ e está em 𝒜.
- **Continuação holomorfa.** φ̂₀(z) := ∫φ₀(u)e^{izu}du é inteira. A função h_T associada a g_T é
  **h_T(z) = φ̂₀(z − T)² + φ̂₀(z + T)²** para todo z ∈ ℂ, e é essa forma que se usa em argumentos complexos, inclusive
  nos polos ±i/2.
  - Para r real, como φ₀ é real e par, φ̂₀(r) é real, e h_T(r) = |φ̂₀(r − T)|² + |φ̂₀(r + T)|² ≥ 0.
  - O módulo quadrado **não** define a continuação holomorfa e não deve ser usado fora da reta.

**Sob RH** (γ reais):
- para r real com |r| ≤ 1, φ̂₀(r) = ∫φ₀(u)cos(ru)du ≥ cos(σ/2)∫φ₀ > 0, porque |ru| ≤ σ/2 < π/2 e φ₀ ≥ 0;
- pela simetria γ ↦ −γ, as janelas em T e em −T contribuem igualmente;
- logo #{γ ∈ (T − 1, T + 1]} (com multiplicidade) ≤ Σ_ρ m_ρh_T(γ_ρ)/(2cos²(σ/2)(∫φ₀)²).

**Aplicação da forma de referência** (H2 §6):
- Σ_ρ m_ρh_T(γ) = h_T(i/2) + h_T(−i/2) − g_T(0)log π + T[g_T] − 2Σ_{log n≤σ}Λ(n)n^{−1/2}g_T(log n);
- T[g_T] é exato (H2 §5);
- a soma prima é finita (n ≤ e^σ ≤ 23).

**Termo principal esperado da soma:** g_T(0)·log(T/2π) = 2∫φ₀²·log(T/2π). Dividindo pelo denominador acima, a contagem fica ≈ [∫φ₀²/(cos²(σ/2)(∫φ₀)²)]·log(T/2π). Por Cauchy–Schwarz, a razão ∫φ₀²/(cos²(σ/2)(∫φ₀)²)
é ≥ 1/(σcos²(σ/2)), cujo mínimo em σ ∈ (0, π) é ≈ 1,22 (perto de σ ≈ 1,3, onde cot(σ/2) = σ).
- **1,22 é um limite inferior** do coeficiente que essa estimativa pode dar (igualdade só para φ₀ indicadora, fora de
  C_c^∞). Não é uma constante alcançada por um corte suave.
- A escolha concreta de φ₀ também afeta os restos (polos, soma prima, termo arquimediano) e as normas de suas derivadas.
- O número fica **só como orientação, sem promessa quantitativa**. A comparação com 10,5·log(T + 8) só pode ser feita
  depois da derivação completa, com φ₀ e σ declarados.

**Requisitos antes de usar:**
1. **Cota explícita, com constantes, de T[g_T] − g_T(0)log π** em termos de log T. Por H2 §4–§5, isso reduz a integrais
   elementares de g_T·K. A oscilação cos(Tx) exige separar x < 1/T. Sem fonte nova.
2. **Cota dos polos |h_T(±i/2)|**, por integração por partes em φ̂₀ na faixa: decai em T, com e^{σ/4}.
3. **Soma prima finita** por módulos.
4. **Faixa de validade T ≥ T₀**, com T₀ explícito. Abaixo de T₀, mantém-se 10,5·log(T + 8).
5. **Escolha de φ₀ e σ (0 < σ < π) fixada antes de qualquer avaliação** e justificada analiticamente (razão acima e restos), não por C2.
6. **Hipóteses:** RH (já em P-RH, para h_T(γ) ≥ 0) e 𝒜 (F5 e J1 bibliográficas). J1 deixa de ser usada nas janelas
   com T ≥ T₀.

**Efeito, se derivado:** substitui n(·) em P0, P1a e P1b (todas as partes principais). Com o Lema 4′, as duas folgas
identificadas ficam tratadas. A avaliação exigirá declaração própria.

#### II.15.4 Estado

| Item | Situação |
|---|---|
| Decomposição de Z_ν | calculada (híbrida); L₂ domina; próximos ~65%; desvio de conferência registrado |
| Lema 4′ (mínimo com L₀) | derivado; não avaliado |
| Lema C (contagem local por fórmula explícita, sob RH) | formulado com hipóteses estritas e continuação holomorfa; requisitos 1–6 pendentes; derivação adiada até a avaliação do Lema 4′ |
| Certificação | exige ainda cotas rigorosas de normas por SVD e cálculos finitos |
| Grade | inalterada (não ampliada) |
| P-RH-trunc | condicional |
| H1 | aberta |

### II.16 Avaliação isolada do Lema 4′ (sob declaração prévia; revisão 11.3b-21; avaliação híbrida)

**Declaração:** `results/etapa11_r5/DECLARACAO_PRH3.md` (SHA-256 f33773b9…), gravada antes do cálculo.
**Saídas:** `prh3_calculo.py` (f8b941e3…), `prh3_tabela.csv` (1979668f…) e `prh3_resumo.json` (580f318c…).

**O que muda:** só o Lema 4 é trocado pelo Lema 4′. Lema 5′, Arq, Θ_k(U₂), grade, blocos, linhas e alvos ficam iguais.
Sem Lema C.

**Natureza:** aritmética intervalar para as cotas; ‖a_k‖₁ (SVD) e Θ_k em ponto flutuante. O resultado é **híbrido**,
condicional a RH (F5 e J1 bibliográficas), e **não certificado**.

#### II.16.1 Conferências (declaradas; ambas satisfeitas)

1. **Lema 4 recalculado no script contra a tabela PRH2:** tabela − recálculo ∈ [0; 2,0·10⁻¹²] para zeros_rel e para
   B_rel. A tolerância declarada era 3·10⁻¹², fixada pela granularidade da exportação.
2. **Z′_ν ≤ Z_ν** nos 16.920 registros.

**Diagnóstico adicional** (fora da declaração; não substitui as conferências): para um par (m4-v3, d05, p = 3, (8, 2)),
a soma direta janela a janela com min(L₀, L₂/(2|j| − 1)²), em ponto flutuante, deu 4,14·10⁻⁷. Isso fica abaixo da forma
fechada do Lema 4′ (4,50·10⁻⁷), que fica abaixo do Lema 4 (1,00·10⁻⁶), como esperado pelas caudas majoradas.

#### II.16.2 Resultados por combinação (orçamento″ = B^{RH″}/|c_k| + |Θ_k(U₂)|/|c_k|)

| (d₁, Δ) | J | Z′/Z | orçamento″ max (todas) | elegíveis: max; mediana | ≤ 10⁻⁶ todas (antes) | ≤ 10⁻⁶ elegíveis (antes) |
|---|---|---|---|---|---|---|
| (1; 0,5) | 7 | 0,069–0,070 | 1,99e-3 | 2,38e-4; 1,37e-4 | 0 (0) | 0 (0) |
| (1; 1) | 6 | 0,086–0,087 | 1,60e-3 | 1,91e-4; 1,09e-4 | 0 (0) | 0 (0) |
| (1; 2) | 5 | 0,097–0,098 | 1,45e-3 | 1,73e-4; 9,91e-5 | 0 (0) | 0 (0) |
| (2; 0,5) | 4 | 0,119–0,120 | 3,04e-4 | 3,63e-5; 2,08e-5 | 0 (0) | 0 (0) |
| (2; 1) | 4 | 0,141–0,142 | 2,49e-4 | 2,97e-5; 1,71e-5 | 0 (0) | 0 (0) |
| (2; 2) | 3 | 0,181–0,182 | 2,04e-4 | 2,44e-5; 1,40e-5 | 0 (0) | 0 (0) |
| (4; 0,5) | 3 | 0,196–0,197 | 4,61e-5 | 5,50e-6; 3,15e-6 | 0 (0) | 0 (0) |
| (4; 1) | 3 | 0,235 | 3,89e-5 | 4,64e-6; 2,66e-6 | 0 (0) | 0 (0) |
| (4; 2) | 2 | 0,301–0,302 | 3,52e-5 | 4,20e-6; 2,41e-6 | 1 (0) | 1 (0) |
| (8; 0,5) | 2 | 0,319 | 7,96e-6 | 9,50e-7; 5,45e-7 | 1044 (26) | 461 (25) |
| (8; 1) | 2 | 0,382–0,383 | 6,24e-6 | 7,45e-7; 4,27e-7 | 1146 (221) | 461 (163) |
| (8; 2) | 2 | 0,448–0,449 | 5,38e-6 | 6,42e-7; 3,68e-7 | 1180 (559) | 461 (361) |

**Polos:** ≤ 2,8·10⁻⁸ relativo em toda a grade (≤ 2,5·10⁻¹⁰ com d₁ = 8). **A parcela dos zeros** é ≥ 0,99986 do orçamento″
em todos os registros (mínimo 0,9998686, em (8, 2); correção da revisão 11.3b-22: a versão anterior dizia ≥ 0,9999 por
arredondamento da impressão). A dominância não muda.

**Melhor combinação por par:** (8, 2) para os 1.410 pares. É o melhor entre as combinações declaradas, não um ótimo.
- **Elegíveis:** 461/461 com orçamento″ ≤ 10⁻⁶ (máximo 6,42·10⁻⁷; mediana 3,68·10⁻⁷); por versão, m4-v1 160, m4-v2 151,
  m4-v3 150.
- **Todas:** 1.180/1.410 (máximo 5,38·10⁻⁶, em linhas não elegíveis).

#### II.16.3 Leitura (regras fixadas na declaração)

1. **O efeito do Lema 4′ é grande.** Ele reduz a majorante dos zeros por fator 0,07–0,45, conforme o corte. A estimativa
   algébrica de §II.15.2 (~2 em (8, 2)) confere com a razão medida, 0,449.
2. **Na avaliação híbrida, sob RH**, a condição suficiente (B^{RH″} + |Θ_k(U₂)|)/|c_k| ≤ 10⁻⁶ para S2-ratio′(U₂) vale nos
   461 pares elegíveis com d₁ = 8, nos três Δ declarados. Em (8, 2), a folga mínima nos elegíveis é de um fator ~1,56.
3. **Isto não certifica S2-ratio′(U₂).** Faltam:
   - cotas rigorosas das normas do estimador obtidas por SVD (‖a_k‖₁) e de Q_k;
   - cotas rigorosas dos cálculos finitos (Θ_k, hoje em B, com regra de erro que subestimou a discrepância, §II.14.1);
   - a conferência bibliográfica de F5 e J1;
   - RH, que permanece hipótese.
4. **O alvo é o observável ideal F*** com o truncamento U = U₂. Duas coisas **não** são tratadas aqui, e são distintas
   (correção da revisão 11.3b-22):
   - **S1, S3a e S3c:** alvos formulados sobre a transformada ideal F* e suas aproximações (truncamento abrupto,
     distribucional). Não são sinônimos dos erros do estimador registrado.
   - **Passagem para o código:** ordenadas tabuladas, densidade usada e implementação (ρ_ord, ρ_Δ e aritmética). É uma
     camada adicional, separada de S1, S3a e S3c.
   **H1 continua aberta.**
5. Nas 230 linhas não elegíveis ainda acima de 10⁻⁶ em (8, 2), a condição suficiente não fecha. Isso não refuta
   S2-ratio′ nem exclui compensação.
6. **O Lema C deixa de ser necessário para a contagem de elegíveis abaixo da tolerância**, na grade declarada e nesta
   avaliação híbrida. Continua útil para margem e robustez, mas sua derivação não é prioritária para esse fim. A grade
   não foi ampliada.

#### II.16.4 Estado

| Item | Situação |
|---|---|
| Lema 4′ | derivado (§II.15.2) e avaliado sob declaração (híbrido) |
| Orçamento S2-ratio′(U₂), condição suficiente, sob RH | ≤ 10⁻⁶ em 461/461 elegíveis com d₁ = 8 (híbrido; não certificado) |
| Certificação | pendente: normas por SVD, Q_k e Θ_k rigorosos; F5 e J1 bibliográficas |
| Lema C | formulado; não derivado; não prioritário para a contagem |
| S1, S3a, S3c (alvos sobre F* e suas aproximações) | pendentes |
| Passagem ao estimador registrado (ordenadas tabuladas, densidade usada, código) | camada adicional; pendente |
| P-RH-trunc | condicional a RH |
| H1 | aberta |

### II.17 Certificação computacional da condição suficiente em (8, 2), condicional a RH (revisão 11.3b-22)

> **Estado (revisão 11.3b-23): execução 1 = certificação pendente de correção numérica.** Uma auditoria externa encontrou
> falhas reproduzíveis de enclausuramento: conversões de extremos por `mpf` na precisão comum (`ck_inf`, `mn`), o ramo
> |v| ≈ 1 de `W_iv` com intervalos disjuntos da função e a decisão final por conversão comum. As falhas foram
> reproduzidas localmente. Elas **não** mostram que a desigualdade falhe, mas **invalidam a justificativa computacional**
> da execução 1. Os resultados abaixo (II.17.1–II.17.5) referem-se à execução 1, preservada em `cert_*_exec1_pendente.*`,
> e **não** devem ser lidos como certificados. A correção e a reexecução estão em §II.18.

**Declaração:** `results/etapa11_r5/DECLARACAO_CERT.md` (SHA-256 b7a7980c…), gravada antes da implementação e da execução.
**Saídas:** `cert_calculo.py` (df9f2a6c…), `cert_blocos.csv` (88a0dbfe…), `cert_tabela.csv` (db8ac7e4…) e
`cert_resumo.json` (9ab2ae0c…).

**Corte:** (d₁, Δ) = (8, 2), isto é, U₁ = 13 e U₂ = 15. **Foi escolhido depois da avaliação exploratória** (§II.12,
§II.16), como o melhor entre as combinações declaradas. Não é um ótimo, e a grade não foi ampliada.

#### II.17.1 O que foi certificado

Para a matriz matemática M^math (declaração §1: nós e parâmetros registrados tomados como racionais binários exatos,
T_j = log n_j exatos, W exata) e o estimador a_k := linha k de (M^mathᵀM^math)⁻¹M^mathᵀ, certifica-se

**(B^{RH″}_{χ,k} + S^{abs}_k)/|c_k| ≤ 10⁻⁶**, com S^{abs}_k = Σ_{13<log n≤15}χ|c(n)||Q_k(log n)| ≥ |Θ_k(U₂)|,

nos pares marcados como certificados. Por P-RH-trunc (§II.13), isso dá |a_k·(F* − M_{≤15})| ≤ 10⁻⁶|c_k|.

**Hipóteses de que a conclusão depende:**
- **RH** (hipótese; não demonstrada);
- forma de referência para 𝒜 (Connes, Teorema 6 e Lema 3; **F5 e J1** como pendências bibliográficas);
- contagem local derivada (Jensen, J1);
- S3b para o limite ε → 0 (derivação condicional; F1 subsumida por RH).

**Base de confiança computacional:**
- (i) IEEE-754 binary64 para +, −, ×, ÷ e `nextafter` no numpy (x86-64);
- (ii) arredondamento dirigido de `mpmath.iv`;
- (iii) inteiros exatos do Python;
- (iv) crivo conferido por implementação independente (segmentada): 234.855 primos até 3.269.017, idênticos nas duas.

#### II.17.2 Passos e verificações

| Passo | Resultado |
|---|---|
| Entradas de M^math (`mpmath.iv`; sinc enclausurado perto de v = 0, ±1) | 30 blocos, 423 nós × 47 linhas |
| **Posto:** ρ = sup‖I − R·G‖_∞ intervalar | ρ ≤ 8,62·10⁻¹³ < 1 em todos os blocos, logo **posto 94 certificado** |
| **Linhas:** ‖a_k‖₁ ≤ ‖y_k‖₁ + ρ/(1 − ρ)·max‖y_i‖₁ | diferença para o a_l1 em ponto flutuante ≤ 3,9·10⁻¹¹ relativo (diagnóstico) |
| **Região da cauda:** \|v_j^∓\| ≥ √2 | min \|v\| ≥ 2.579 |
| **S^abs:** 512 células δ = 1/256; P em intervalos no centro, mais a derivada pelo Lema 1 | S^abs cert ≤ 23× o S_abs em ponto flutuante; bordas ambíguas: 0; 197.912 potências de primo (igual a THETA) |
| **Orçamento:** Lema 4′ + Lema 5′ + Arq em `mpmath.iv`, \|c_k\| inferior, exportação para fora | total cert ≤ 1,016× o orçamento híbrido de PRH3 (diagnóstico) |

**Diagnóstico da álgebra da cota de |Q_k|** (ponto flutuante, antes da execução completa; não substitui a prova):
- em 3.000 valores de u ∈ (13, 15], nos blocos b01 e d07, a identidade Σ_jᾱ_jℓ_u(t_j) = −(L/8πi)·{…} de §II.2(d) confere
  até 1,3·10⁻¹⁰ relativo;
- a cota (L/8π)Σ|P| ≥ |Q_k| vale em todos os pontos.

**Registro de implementação:**
- antes da execução completa, houve um teste de desenvolvimento no bloco b01, com o mesmo método, cujos arquivos foram
  descartados;
- nenhuma mudança de método depois da declaração.

#### II.17.3 Resultados

| Conjunto | Certificados | Máximo de total (sup) | Mediana |
|---|---|---|---|
| **Elegíveis** | **461/461** (m4-v1 160, m4-v2 151, m4-v3 150) | **6,45224355·10⁻⁷** | 3,706·10⁻⁷ |
| Não elegíveis | 717/949 | 5,45·10⁻⁶ (entre os não certificados) | — |
| Todos | 1.178/1.410 | — | — |

**Concordância com a avaliação híbrida:**
- nenhum par certificado tinha orçamento híbrido > 10⁻⁶;
- dois pares não elegíveis com orçamento híbrido ≤ 10⁻⁶ **não** foram certificados, porque o arredondamento para fora e
  a cota de S^abs os levaram acima da tolerância.

#### II.17.4 Leitura

1. **Certificação computacional, condicional a RH**, da desigualdade |a_k·(F* − M_{≤15})| ≤ 10⁻⁶|c_k| para os 461 pares
   elegíveis e para 717 não elegíveis, com os parâmetros e o corte declarados. Vale para o estimador matemático M^math,
   sob a base de confiança (i)–(iv).
2. **Não é:**
   - prova de RH;
   - certificação retrospectiva de C2;
   - tratamento de S1, S3a, S3c (alvos sobre F* e suas aproximações);
   - tratamento da camada adicional de passagem ao estimador registrado (ordenadas tabuladas, densidade usada, código em
     ponto flutuante);
   - resposta a H1, que continua **aberta**.
3. Os 232 pares não certificados não refutam a desigualdade nem S2-ratio′.
4. **Pendências bibliográficas que afetam o enunciado:** F5 e J1. Nenhuma fonte nova foi usada.

#### II.17.5 Estado

| Item | Situação |
|---|---|
| Posto e linhas da pseudoinversa (M^math) | certificados (ρ ≤ 8,62·10⁻¹³) |
| Cota de Θ_k(U₂) via S^abs | certificada |
| Desigualdade (B^{RH″} + S^abs)/\|c_k\| ≤ 10⁻⁶ em (8, 2) | certificada, sob RH, em 461/461 elegíveis e 1.178/1.410 pares |
| Passagem ao estimador registrado (ordenadas, densidade, código) | pendente (camada adicional) |
| S1, S3a, S3c | pendentes |
| F5, J1 | bibliográficas |
| Lema C | não prioritário |
| H1 | aberta |

### II.18 Correção de enclausuramento e reexecução do certificado (revisão 11.3b-23)

**Documentos:**
- **Adendo:** `results/etapa11_r5/DECLARACAO_CERT_CORRECAO1.md` (SHA-256 0a693179…), gravado antes de alterar o código.
  O método da declaração original (b7a7980c…) não muda.
- **Execução 1**, preservada como pendente: `cert_calculo_exec1_pendente.py` (df9f2a6c…), `cert_blocos_exec1_pendente.csv`,
  `cert_tabela_exec1_pendente.csv` e `cert_resumo_exec1_pendente.json`.
- **Execução 2:** `cert_calculo.py` (cad037a7…), `cert_testes.py` (4df0dd87…), `cert_testes_resultado.json` (6a6a090d…),
  `cert_blocos.csv` (9bc6d8ea…), `cert_tabela.csv` (2f689d7d…) e `cert_resumo.json` (792e80f6…).

#### II.18.1 Defeitos e correções

| Defeito | Onde | Correção |
|---|---|---|
| D1: extremo inferior de \|c_k\| convertido por `mpf` (15 dígitos); fica acima do extremo superior em 28 das 47 linhas (reproduzido) | `ck_inf` | ponto degenerado do extremo inferior bruto (`iv.make_mpf`) |
| D2: majorante do mínimo convertida por `mpf` | `mn` em B^{RH″} | comparação exata de extremos superiores (Fraction) |
| D3: ramo \|v\| ≈ 1 de `W_iv` disjunto da função (21 de 27 casos sensíveis na execução 1); ramo v ≈ 0 com extremos convertidos | `W_iv` | ramos decididos por frações exatas; só operações `mpmath.iv`; asserção de denominador sem 0 |
| D4: decisão `mpf(tot.b) <= mpf(TAU)` | decisão | extremo superior exato ≤ Fraction(1, 10⁶) |
| D5: floor de bordas, `float(mpf(·))` e razão de J | células, `ivf`, J | Fraction exata e conversão binary64 dirigida |

#### II.18.2 Testes obrigatórios (todos passaram antes da reexecução)

| Teste | Conteúdo | Resultado |
|---|---|---|
| T1 | W_iv (via ω intervalar) × fórmula direta a 80 dígitos, casos sensíveis perto de 0 e ±1 + 2.000 aleatórios, três L | 6.114 casos, 0 interseções vazias |
| T2 | valores exatos L/2 (v = 0) e L/4 (v = ±1) | contidos |
| T3 | conversões dirigidas, ivf, pt_lo em 6.052 intervalos (inclui \|c_k\| das 47 linhas e p = 2, 3, 5, 11, 139) | 0 falhas |
| T4 | mínimo de extremos superiores com diferenças de 10⁻²⁰ a 10⁻²⁹ | exato |
| T5 | decisão com extremo superior 10⁻⁶ ± 10⁻²⁵ | "não" / "sim" corretos |
| T6 | varredura textual por `mpf(` e `.a)`/`.b)` no script | nenhuma ocorrência |

**Sensibilidade (diagnóstico):** os mesmos testes aplicados ao script da execução 1 detectam as falhas: 21 de 27 casos
disjuntos no ramo |v| ≈ 1 e `ck_inf` acima do extremo inferior em 28 de 47 linhas.

**Fora do escopo de T6:** a função de exportação `sup_str` (`interval_export.py`) converte com 60 dígitos e acrescenta uma
unidade de margem. Foi conferida em casos pontuais, mas **não entra na decisão**, que usa frações exatas. A marcação e a
comparação da string exportada com 10⁻⁶ concordam nos 1.410 pares.

#### II.18.3 Resultados da execução 2

| Item | Execução 2 |
|---|---|
| ρ máx (posto 94) | 8,612·10⁻¹³ < 1 em todos os blocos |
| min \|v\| na cauda | 2.579 ≥ √2 |
| Crivo | 234.855 primos, conferido; 197.912 potências; 0 bordas ambíguas |
| **Elegíveis certificados** | **461/461** (m4-v1 160, m4-v2 151, m4-v3 150); máximo **6,45224355·10⁻⁷** |
| Todos certificados | 1.178/1.410 |
| Comparação com a execução 1 | 0 mudanças de marcação; totais exportados (15 dígitos) idênticos |

**Leitura:**
1. As falhas da execução 1 eram reais e invalidavam a justificativa. Seu efeito numérico ficou abaixo da granularidade
   exportada, e a margem sobreviveu. **O certificado vale pela execução 2 com os testes, não pela margem.**
2. **Certificação computacional, condicional a RH** (F5 e J1 bibliográficas), da desigualdade
   (B^{RH″}_{χ,k} + S^{abs}_k)/|c_k| ≤ 10⁻⁶ em (d₁, Δ) = (8, 2), para M^math, nos 461 pares elegíveis e em 1.178 dos 1.410
   pares, sob a base de confiança (i)–(iv) de DECLARACAO_CERT §2. O corte foi escolhido após a avaliação exploratória.
3. **Riscos residuais declarados:**
   - correção do argumento de erro de somas em binary64 (`isum`) e do uso de `nextafter`;
   - correção de `mpmath.iv`;
   - ausência de revisão independente do script corrigido.
   A auditoria anterior mostra que essa revisão é pertinente.
4. **Não é:** prova de RH; certificação retrospectiva de C2; tratamento de S1, S3a, S3c ou da passagem ao estimador
   registrado. H1 continua **aberta**. P-RH-trunc (derivação) não foi afetada pelas falhas.

#### II.18.4 Estado

| Item | Situação |
|---|---|
| Execução 1 | pendente de correção numérica; não válida como certificado (preservada) |
| Execução 2 | **substituída pela execução 3** (§II.19): lacunas de justificativa em `vmn**4`, `sup_str`, `math.sqrt`, `math.pi` e finitude; os 461/461 dela eram atribuídos só a ela e à sua base de confiança |
| Passagem ao estimador registrado; S1, S3a, S3c | pendentes |
| H1 | aberta |

### II.19 Lacunas de justificativa em ponto flutuante e exportação; execução 3 (revisão 11.3b-24)

**Documentos:**
- **Adendo 2:** `results/etapa11_r5/DECLARACAO_CERT_CORRECAO2.md` (SHA-256 75eee940…), gravado antes das alterações.
- **Execução 2**, preservada: `cert_calculo_exec2.py`, `cert_testes_exec2.py` e `cert_*_exec2.*`.
- **Execução 3:** `cert_calculo.py` (ca87480a…), `cert_testes.py` (3b0466dc…), `cert_testes_resultado.json` (dc07d0c2…),
  `cert_blocos.csv` (9a7d5347…), `cert_tabela.csv` (2f689d7d…) e `cert_resumo.json` (cad3a518…).

**Sobre a execução 2:** os 461/461 eram atribuídos só a ela e à sua base de confiança. A coincidência com a execução 1
**não** foi usada como validação.

#### II.19.1 Lacunas e correções

| Lacuna | Correção |
|---|---|
| L1: `dn(vmn**4)`, potência binary64 com um único `nextafter` (fora da base +, −, ×, ÷) | q = dn(vmn·vmn), v⁴ = dn(q·q), vmn > 0 |
| L2: string de `sup_str` não verificada contra o extremo superior exato | em cada exportação, asserção Fraction(string) ≥ extremo superior exato; teste T7 |
| L3: `math.sqrt(2)` na verificação da região da cauda | vmin > 0 e Fraction(vmin)² ≥ 2 |
| L4: `math.pi` como cota inferior de π sem justificativa | π_inf := arredondamento para baixo do extremo inferior exato de `iv.pi` |
| L5: sem asserções de finitude | `np.isfinite` em toda construção de intervalo e nos escalares derivados |

#### II.19.2 Justificativa de `isum` (lema de somação)

**Hipóteses:**
- (H-a) IEEE-754 binary64 com arredondamento ao mais próximo;
- (H-b) cada adição executada pelo numpy é uma operação binária do padrão, em qualquer ordem ou árvore de redução,
  sem precisão estendida intermediária (x86-64, SSE/AVX);
- (H-c) sem overflow, NaN ou ±∞ (asserções L5).

**Modelo:** fl(x + y) = (x + y)(1 + δ), com |δ| ≤ u := ε_mach/2. Em subfluxo gradual, a adição é exata.

**Lema.** Para m termos, a soma calculada ŝ e a soma calculada dos módulos Â satisfazem

|ŝ − s| ≤ [γ_m/(1 − γ_m)]·Â, com γ_n := nu/(1 − nu).

**Prova.**
1. Em qualquer árvore, ŝ = Σ_i x_iΠ_{k∈caminho(i)}(1 + δ_k), com caminhos de comprimento ≤ m − 1. Como
   |Π(1 + δ_k) − 1| ≤ (1 + u)^{m−1} − 1 ≤ γ_{m−1}, vale |ŝ − s| ≤ γ_{m−1}Σ|x_i|.
2. Da mesma forma, Â ≥ (1 − u)^{m−1}Σ|x_i| ≥ (1 − γ_{m−1})Σ|x_i|.
3. Combinando, e usando γ_{m−1} ≤ γ_m, obtém-se a cota. ∎

**Uso no script:**
- Com mε ≤ 0,1 (asserção), mu ≤ 0,05 e γ_m/(1 − γ_m) ≤ mu/(1 − 2mu) ≤ 1,12·mu < 2mε.
- O fator 2mε é exato em binary64.
- O produto 2mε·Â é arredondado para cima, e ŝ ∓ erro para fora.

**`nextafter`:** após uma operação arredondada ao mais próximo, sem overflow, o resultado r é adjacente ao valor exato ou
igual a ele. Logo nextafter(r, −∞) ≤ exato ≤ nextafter(r, +∞). Isso vale também em subfluxo.

**Testes isolados não substituem este lema;** apenas conferem a implementação.

#### II.19.3 Testes (antes da execução 3; todos passaram)

- **T1–T6** (adendo 1), reaplicados: 6.114 casos de W_iv e 6.052 conversões, com 0 falhas; T2, T4 e T5 corretos; T6
  sem ocorrências.
- **T7:** `sup_str`/`inf_str` contra extremos exatos, com 6, 12 e 15 dígitos, em 22.311 casos (magnitudes de 10⁻³⁰⁰ a
  10³⁰⁰, sinais variados, valores exatamente decimais e a 10⁻²⁸ de múltiplos de 10^{−d}, |c_k|): 0 falhas.
- **T8:** v⁴ dirigido ≤ v⁴ exato em 10⁴ valores: 0 falhas.

**Dependência herdada (execução 3; eliminada na execução 4, §II.20):** c₁^sup e c₂^sup vinham de `prh_forca_resumo.json`,
exportados antes por `sup_str` com 6 dígitos.

#### II.19.4 Resultados da execução 3

| Item | Execução 3 |
|---|---|
| ρ máx (posto 94) | 8,612·10⁻¹³ |
| min \|v\| na cauda (verificação exata de ≥ √2) | 2.579 |
| Crivo | conferido; 197.912 potências; 0 bordas ambíguas |
| Exportações conferidas por frações exatas | todas (asserção em tempo de execução) |
| **Elegíveis certificados** | **461/461** (m4-v1 160, m4-v2 151, m4-v3 150); máximo **6,45224355·10⁻⁷** |
| Todos certificados | 1.178/1.410 |

#### II.19.5 Leitura e estado

1. **Atribuição:** os 461/461 são atribuídos à **execução 3** e à sua base de confiança:
   - IEEE-754 binary64 (H-a)–(H-c);
   - `mpmath.iv`;
   - inteiros exatos;
   - crivo conferido;
   - lema de somação de §II.19.2;
   - dependência herdada de c₁^sup e c₂^sup.
   **Diagnóstico sem valor de validação:** 0 mudanças de marcação e totais exportados idênticos aos da execução 2.
2. **Certificação computacional condicional a RH** (F5 e J1 bibliográficas) da desigualdade
   (B^{RH″}_{χ,k} + S^{abs}_k)/|c_k| ≤ 10⁻⁶ para M^math em (8, 2), corte escolhido após a avaliação exploratória.
3. **Revisões até aqui:** a revisão externa parcial (11.3b-23 e 11.3b-24) não reencontrou as falhas de conversão. **Não**
   equivale a uma auditoria integral independente, que continua recomendada.
4. **Não é:** prova de RH; certificação de C2; tratamento de S1, S3a, S3c ou da passagem ao estimador registrado. H1
   continua **aberta**.

| Item | Situação |
|---|---|
| Execução 1 | inválida (enclausuramento); preservada |
| Execução 2 | substituída (lacunas L1–L5); preservada |
| Execução 3 | **substituída pela execução 4** (§II.20), por eliminar a dependência herdada de c₁^sup e c₂^sup; preservada em `cert_*_exec3.*` |
| Dependência herdada de c₁^sup e c₂^sup | eliminada por recálculo interno (§II.20) |
| H1 | aberta |

### II.20 Eliminação da dependência herdada de c₁^sup e c₂^sup; execução 4 (revisão 11.3b-25, 16/09/2026)

**Documentos:**
- **Adendo 3:** `results/etapa11_r5/DECLARACAO_CERT_RECONF_C1C2.md` (SHA-256 a8253e9c…), gravado antes de qualquer
  alteração.
- **Manifesto:** `results/etapa11_r5/MANIFESTO_CERT.csv` (SHA-256 56d6c6cf…), com arquivo, hash, papel e execução de todos
  os artefatos do certificado (execuções 1–4 e documentos).

#### II.20.1 Origem e escolha do método

- **Origem:**
  - as strings "2.000982" e "9.854620" vinham de `prh_forca_resumo.json` (56e4c373…);
  - foram exportadas por `prh_forca.py` (bb9a6973…, 14/09/2026, sob DECLARACAO_PRH) via `sup_str(·, 6)`;
  - vinham de uma malha intervalar de 20.000 subintervalos em [0,01; 0,99] mais cotas nas pontas.
- **Método A (reconferência): não executável.** Os intervalos originais não foram persistidos. Reexecutar o código original
  também não serviria como reconferência, pois ele usa construções do tipo auditado nos adendos 1 e 2 (extremos por `.a`/`.b`
  e máximos por `.b`), sem garantia demonstrada de cobertura sem lacunas nem de preservação do extremo superior.
- **Método B (recálculo interno): adotado.** c₁ e c₂ são recalculados dentro de `cert_calculo.py`. O script não lê mais
  nenhum arquivo com essas constantes.

#### II.20.2 Matemática do recálculo

**Definições:** ϕ(x) = f(x)/(f(x) + f(1 − x)) em (0, 1), com f(x) = e^{−1/x}. Então:
- f′(x) = e^{−1/x}/x² e f″(x) = e^{−1/x}(1 − 2x)/x⁴;
- S = f(x) + f(y), com y = 1 − x;
- ϕ′ = N/S², com N = f′(x)f(y) + f(x)f′(y), já que d/dx f(y) = −f′(y);
- ϕ″ = (N′S − 2NS′)/S³, com N′ = f″(x)f(y) − f(x)f″(y) (os termos cruzados f′(x)f′(y) se cancelam) e
  S′ = f′(x) − f′(y).

**Malha [1/100, 99/100]:**
- 20.000 subintervalos com extremos racionais exatos, cada um construído como envoltória exata do extremo inferior de
  iv(x_i) e do extremo superior de iv(x_{i+1});
- **cobertura verificada por frações exatas:** 0 lacunas, primeiro extremo inferior ≤ 1/100 e último extremo superior ≥ 99/100;
- a extensão intervalar natural enclausura ϕ′ e ϕ″ em cada subintervalo; o máximo dos |·| é tomado por comparação exata de
  extremos superiores.

**Ponta (0, δ], δ = 1/100:**
- S ≥ f(y) ≥ e^{−1/(1−δ)}, pois y ≥ 1 − δ e f é crescente;
- f′(x) ≤ e^{−1/δ}/δ², pois e^{−1/x}/x² é crescente em (0, ½) (derivada e^{−1/x}(1 − 2x)/x⁴ > 0);
- |f″(x)| ≤ e^{−1/δ}/δ⁴, pois |1 − 2x| ≤ 1 e e^{−1/x}/x⁴ é crescente em (0, ¼) (derivada e^{−1/x}(1 − 4x)/x⁶ > 0);
- f(y) ≤ e^{−1} ≤ 1, f′(y) ≤ e^{−1}/(1 − δ)² e |f″(y)| ≤ 3e^{−1}/(1 − δ)⁴ para y ∈ [1 − δ, 1);
- daí |ϕ′| ≤ N_b/S_min² e |ϕ″| ≤ N′_b/S_min² + 2N_bS′_b/S_min³, avaliados só com operações intervalares, com δ como
  intervalo que contém 1/100.

**Ponta [1 − δ, 1):** por simetria, ϕ(1 − x) = 1 − ϕ(x), logo |ϕ′| e |ϕ″| são simétricos.

**Fora de (0, 1):** ϕ é constante, e ϕ′ = ϕ″ = 0 (extensão C^∞).

#### II.20.3 Valores obtidos

| Constante | Extremo superior exato (fração) | Decimal (15 dígitos, para cima) | String antiga | Contribuição das pontas |
|---|---|---|---|---|
| c₁ | 5073087604928147986514589564823/2535301200456458802993406410752 | 2,000980240144558 | 2,000982 | < 3·10⁻³⁹ |
| c₂ | 6246106425398266510255250913437/633825300114114700748351602688 | 9,854618337692911 | 9,854620 | < 3·10⁻³⁵ |

**Diagnóstico** (sem valor de validação): os novos extremos são ≤ às strings antigas, que eram compatíveis. Os valores
usados no certificado são agora os pontos degenerados acima, sem strings.

#### II.20.4 Testes (T1–T9; todos passaram antes da execução 4)

- **T1–T8:** inalterados, reaplicados ao script modificado (`cert_testes_resultado.json`, script SHA-256 95bec528…).
- **T9:**
  - (a) cobertura exata: 0 lacunas;
  - (b) em 9.998 pontos racionais de (0, 1), incluindo a 10⁻⁶ das pontas e perto de ½, avaliados a 50 dígitos: extremo
    inferior de |ϕ′| e |ϕ″| ≤ c₁^sup e c₂^sup, com 0 falhas. Máximos amostrais: |ϕ′| = 2,0 (em x = ½) e |ϕ″| = 9,841;
  - (c) `phi_constants` e `phi_derivs` sem `float`, `mpf`, `np.` ou `math.`;
  - (d) o script não lê `prh_forca_resumo.json`, `["c1_sup"]` ou `["c2_sup"]`, nem usa `_prev`.

#### II.20.5 Execução 4

| Item | Execução 4 |
|---|---|
| **Artefatos** | `cert_calculo.py` (95bec528…), `cert_testes.py` (2f69e972…), `cert_testes_resultado.json` (13a6508c…), `cert_blocos.csv` (7dcc46bd…), `cert_tabela.csv` (58b0d493…), `cert_resumo.json` (f008d5e2…) |
| ρ máx (posto 94) | 8,612·10⁻¹³ |
| **Elegíveis certificados** | **461/461**; máximo **6,45224274·10⁻⁷** |
| Todos certificados | 1.178/1.410 |
| Frente à execução 3 (diagnóstico) | 0 mudanças de marcação; nenhum total maior |

**Leitura e estado:**
1. O certificado não depende mais de strings exportadas em arquivos anteriores. As entradas lidas de arquivo são:
   - **definicionais:** `metrics.json` dos runs m4 (A, B, E_c registrados) e o catálogo de `src/`;
   - **descritivas ou diagnósticas:** elegibilidade (`cruzamento_tabela.csv`) e comparações com PRH2, THETA e PRH3.
     Nenhuma delas entra na desigualdade certificada.
2. Os 461/461 são atribuídos à **execução 4** e à sua base de confiança (DECLARACAO_CERT §2, lema de §II.19.2, adendos 1–3).
3. O resultado continua **condicional a RH** (F5 e J1 bibliográficas). Não certifica C2, não trata S1, S3a e S3c nem a
   passagem ao estimador registrado, e **não fecha H1**.
4. **Congelado:** nenhuma alteração posterior sem nova declaração. A auditoria integral independente continua pendente.

| Item | Situação |
|---|---|
| Execução 4 | vigente; certificado computacional condicional a RH; congelada |
| Dependência herdada de c₁, c₂ | eliminada |
| Auditoria integral independente | pendente |
| H1 | aberta |

### II.21 Resíduo contra o catálogo 𝒦: contaminação em (5, 15) certificada, condicional a RH (revisão 11.3b-26, 16/09/2026)

**Declaração:** `results/etapa11_r5/DECLARACAO_CERT_CONTAMINACAO.md` (SHA-256 1d46bced…), gravada antes de qualquer
implementação. Reaproveita DECLARACAO_CERT.md e os adendos 1–3.

**Artefatos** (todos em `MANIFESTO_CERT.csv`):
- `cert_contaminacao.py` (4baff933…);
- `cert_contaminacao_testes.py` (43e941fe…);
- `cert_contaminacao_testes_resultado.json` (13e8a417…);
- `cert_contaminacao_blocos.csv` (be3daaa6…);
- `cert_contaminacao_tabela.csv` (31abb5a4…);
- `cert_contaminacao_resumo.json` (c44f730e…).

**Execução 4 inalterada:** `cert_calculo.py` segue com 95bec528…; B_rel_sup e Sabs_rel_sup são **lidos** de `cert_tabela.csv`.

**Corte:** (d₁, Δ) = (8, 2), o mesmo, escolhido após a avaliação exploratória.

#### II.21.1 Objeto e identidade

**Catálogo.** 𝒦 = todas as potências de primo n ≤ 148 (47 linhas; conferido por enumeração independente). Logo n ∉ 𝒦
com Λ(n) > 0 ⇔ log n > 5.

**Identidade.** Para 0 < ε ≤ ε₀, com T_χ(ε) := Σ_n χ(log n)w_ε(n)c(n)ℓ_n:

a_k·(F* − M_𝒦) = a_k·(F* − M_ε) + (w_ε(n_k) − 1)c_k + a_k·T_χ(ε) + Σ_{5<log n<15}(1 − χ(log n))w_ε(n)c(n)Q_k(log n).

**Limite ε → 0:**
- o primeiro termo tende a 0 (S3b);
- o segundo tende a 0;
- |a_k·T_χ| ≤ B^{RH″}_{χ,k} uniformemente em ε (P-RH com os Lemas 4′ e 5′; sob RH);
- a soma é finita.

Então:

|a_k·(F* − M_𝒦)| ≤ B^{RH″}_{χ,k} + P_k + C_k + Σ_{13<log n<15}(1 − χ)|c(n)||Q_k(log n)|,

com P_k := Σ_{5<log n≤6}|c||Q_k| e C_k := Σ_{6<log n≤13}|c||Q_k|.

**Não usa Θ_k** nem o corte em U₂. A cota P-RH-trunc de §II.13 continua válida, mas não entra aqui.

**Amarração com a execução 4 (verificada no código):**
- `cell_sums()` de `cert_calculo.py` soma Λ(n)/√n por célula **sem peso χ**. A declaração original registra isso como
  "com χ ≤ 1".
- Logo Sabs_rel_sup já majora Σ_{13<log n≤15}|c||Q_k|/|c_k| sem peso.
- Como 0 ≤ 1 − χ ≤ 1, a última soma é dominada por Sabs_rel_sup.

**Orçamento certificado:**

total_k := B_rel_sup + Sabs_rel_sup + (P_k^sup + C_k^sup)/|c_k|_inf ≤ 10⁻⁶, decidido por frações exatas.

#### II.21.2 Conferência das premissas (registrada na declaração, antes do cálculo)

- **Contagens:**
  - π(442.413) = 37.128;
  - (e⁶, e¹³] tem 37.049 primos + 161 potências = 37.210 termos;
  - (e⁵, e⁶] tem 45 primos + **6** potências (169, 243, 256, 289, **343 = 7³**, 361) = 51 termos.
- **Margem em (5, 6]:**
  - t_max ≤ 4,93760 nos 30 blocos (catálogo até log n = 4,9345);
  - no primeiro n fora do catálogo (149), s ≥ 0,0663 e v ≥ 21,23;
  - o Lema 1 vale ali, então a envoltória por células seria **válida**;
  - o regime I ponto a ponto foi adotado por **precisão**, não por validade. O ganho frente à alternativa por células
    **não foi medido**, porque a variante não foi implementada.
- **Sem expectativa de fechamento:** a estimativa B de contaminação ≤ 1·10⁻⁹|c_k| é **com sinal**; P_k e C_k são somas de
  **módulos**. Nenhuma expectativa foi registrada.

#### II.21.3 Método

- **Reconstrução (Passos 1–3):** repetida com as primitivas de `cert_calculo.py` importado como módulo, sem editá-lo.
  - **Parada obrigatória:** ρ e as 47 ‖a_k‖₁^sup coincidem **bit a bit** com a execução 4.
- **Regime I (5, 6]:** 51 termos. Q_k(log n) é calculado ponto a ponto pela definição, com Q_k = Σ_j aR_j·Re ℓ_u(t_j) +
  aI_j·Im ℓ_u(t_j), ℓ_u por `W_iv` e cos/sin(E_c u) em `mpmath.iv`, e Arows intervalar. **Não usa** a forma separada de
  §II.2(d).
- **Regime II (6, 13]:** 1.792 células δ = 1/256 com bordas exatas, mesmo Passo 4 da execução 4 (envoltórias P e derivada
  do Lema 1). Margem v_min² ≥ 2 verificada exatamente em cada célula.
- **Somas por célula:** sem peso, com o crivo conferido por duas implementações.
- **Decisão:** frações exatas.
- **Trava:** a execução completa só dispara com `--executar`.

#### II.21.4 Testes (T1–T15; todos passaram antes da execução completa)

| Teste | Resultado |
|---|---|
| T1–T9 (reaplicados) | todos passaram; o resultado regenerado é idêntico ao da execução 4 (13a6508c…), e o arquivo original foi restaurado |
| T10 enumeração | floor(e⁵) = 148, floor(e⁶) = 403, floor(e¹³) = 442.413, sem ambiguidade; 51 termos no regime I (duas enumerações iguais); crivo do regime II conferido |
| T11 cobertura | 1.792 células com expoentes exatos e contíguos de 6 a 13; 37.210 termos; 0 não atribuídos, 0 em duas células, 0 bordas ambíguas. Fronteira u = 6: maior termo do regime I = 401, menor do regime II = 409; a união é igual a uma enumeração independente dos 37.261 termos de (5, 13], sem sobreposição |
| T12 consistência entre regimes | 20 valores de n em (6, 7] e (12, 13], 3 blocos: o extremo superior pontual ≤ o sup da célula, com razão 0,28–0,79. Mostra que a célula não fica abaixo do extremo pontual; **não** mede a sobrestimação em relação ao valor verdadeiro |
| T13 diagnóstico B | 7.191 comparações: Q_k em ponto flutuante dentro do intervalo em todas |
| Reconstrução bit a bit (3 blocos) | idêntica |
| T14 decisão | 10⁻⁶ exato → sim; +10⁻²⁵ → não; −10⁻²⁵ → sim |
| T15 margem | 53.760 células nos 30 blocos, 0 falhas; menor v = 339,89 |

**Correção de implementação do teste T11 (registrada):**
- Na primeira rodada, o teste exigia que o menor termo do regime II fosse 404. Mas 404–408 não são potências de primo; a
  menor acima de 403 é 409.
- A exigência declarada (n ≤ 403 no regime I, n ≥ 404 no regime II, nenhum n fora ou em ambos) passou a ser verificada
  por completude e disjunção.
- O método não mudou.

**Execução de desenvolvimento** (declarada; bloco b01):
- 16/16 elegíveis e 40/47 pares abaixo de 10⁻⁶, em 61 s;
- script e log ficaram só no scratchpad e foram **apagados**; nada foi gravado em `results/`;
- regimes, δ e fronteira ficaram travados a partir dela.

#### II.21.5 Resultados (execução completa, 30 blocos)

| Item | Valor |
|---|---|
| Parada bit a bit (ρ e 47 ‖a_k‖₁ × 30 blocos) | **limpa** (`parada_bit_a_bit = []`) |
| Margem nas células; ρ máx | todos os blocos; v_min = 339,89; ρ ≤ 8,612·10⁻¹³ |
| **Elegíveis certificados** | **461/461** (m4-v1 160, m4-v2 151, m4-v3 150) |
| Máximo de total_k nos elegíveis | **6,6090905·10⁻⁷** (m4-v3/d07, p = 2, r = 1); folga 1,51×, ≈ 3,39·10⁻⁷ |
| Acréscimo (P_k + C_k)/\|c_k\| nos elegíveis | 5,2·10⁻⁹ / 1,2·10⁻⁸ / **2,20·10⁻⁸** (mín / mediana / máx; máx em m4-v3/d05, p = 47) |
| P_k/\|c_k\| nos elegíveis | 2,7·10⁻¹¹ / 3,6·10⁻¹⁰ / 2,5·10⁻⁹ |
| C_k/\|c_k\| nos elegíveis | 5,0·10⁻⁹ / 1,1·10⁻⁸ / 2,0·10⁻⁸; **C_k > P_k nos 461** |
| P_k/\|c_k\| em todos os pares | até 3,9·10⁻⁶, só em linhas não elegíveis |
| Todos os pares certificados | **1.093/1.410**; máximo de total_k 8,70·10⁻⁶ |
| Marcação × string exportada | concordam nos 1.410 pares |
| Tempo | 1.214 s (93–148 s por bloco, 3 processos) |

**Frente à execução 4 (diagnóstico):**
- nenhum par passou a certificar;
- **85 pares não elegíveis** deixaram de certificar (1.178 → 1.093);
- nenhum elegível foi perdido.

**Os 85 pares perdidos:**
- 66 são as linhas de topo do catálogo: p = 139 (29), 137 (26) e 131 (11), com log n ≈ 4,88–4,93, próximas de
  t_max ≈ 4,94;
- os demais 19 são 11² (8), 127 (3), 2³ (2), 7² (2), 2⁵, 5³, 2⁴ e 5²;
- nos 85, |c_k| vai de 0,039 a 0,137, logo **não** se explicam por |c_k| pequeno;
- a concentração no topo do catálogo é um fato da tabela. O **mecanismo** (proximidade entre essas linhas e os primeiros
  n fora do catálogo) é plausível, mas **não foi verificado** termo a termo.

A elegibilidade segue a definição protocolar: "resolvida e claramente detectável, com margem 1,5".

#### II.21.6 Leitura

**Estabelecido.** Para M^math, condicional a RH (F5 e J1 bibliográficas), na base de confiança declarada (DECLARACAO_CERT
§2, lema de somação de §II.19.2, adendos 1–3):

**|a_k·(F* − M_𝒦)| ≤ 10⁻⁶·|c_k| nas 461 linhas elegíveis** (e em 1.093 dos 1.410 pares).

É a condição por linha no **observável ideal F\***, contra o **catálogo real** 𝒦, **sem corte em U₂**.

**Não estabelecido:**
- **C2:** elegibilidade, agregação por fração, critério de fase Q;
- **camada do estimador registrado:** projeção de ρ_Δ e ρ_ord por a_k; ρ_num, isto é, â_k em ponto flutuante, T_j =
  `period_theoretical` em ponto flutuante, termo suave por NUFFT e quadratura; a elegibilidade também foi calculada no
  pipeline registrado;
- S1, S3a, S3c;
- **H1**, que continua **aberta**.

Os 317 pares não certificados (todos não elegíveis) **não** refutam a desigualdade nem S2-ratio.

**Riscos residuais:** os de §II.19–§II.20 (IEEE-754 binary64, `mpmath.iv`, lema de somação) e a ausência de auditoria
integral independente.

#### II.21.7 Estado e próximos passos declarados

| Enunciado | Alvo | Situação |
|---|---|---|
| S2-ratio′(U₂ = 15) | \|a_k·(F* − M_{≤15})\| ≤ 10⁻⁶\|c_k\| | certificado sob RH, para M^math, 461/461 elegíveis (execução 4, §II.20) |
| S2-ratio no ideal | \|a_k·(F* − M_𝒦)\| ≤ 10⁻⁶\|c_k\| | **certificado sob RH, para M^math, 461/461 elegíveis (§II.21)** |
| S2-ratio registrado | \|Re Ĉ_k/c_k − 1\| no código | não tratado |
| S1, S3a, S3c | alvos sobre F* | abertos |
| H1 | observável → linhas | **aberta** |

**Próximos passos (cada um com declaração própria):**
1. **ρ_Δ.** Reconferir ou recalcular sob a base atual a cota de densidade de `density_error_certified.py` (revisão
   11.3b-6, anterior aos adendos 1–3; **dependência herdada**) e depois projetar por a_k.
   - **Orientação algébrica, não decisória:** ‖a_k‖₁ × cota por bloco acrescenta ≤ 5,0·10⁻⁸ em relação a |c_k| nos
     elegíveis.
2. **ρ_ord.** Precisa da estrutura linear em δγ, porque ‖a_k‖₁ × 4,5·10⁻⁵ não cabe no orçamento relativo. A cota será
   **condicional à precisão declarada da tabela** (3·10⁻⁹; classe B; pendência F7).
3. **ρ_num.** Cota própria.
4. **Auditoria integral independente**, ainda pendente.

### II.22 Termo determinístico ρ_Δ: cota de densidade sob a base atual e observável F^rvm (revisão 11.3b-27, 16/09/2026)

**Declaração:** `results/etapa11_r5/DECLARACAO_CERT_DENSIDADE.md` (SHA-256 6a69c0d7…), gravada antes de qualquer código.
Reaproveita DECLARACAO_CERT.md, os adendos 1–3 e DECLARACAO_CERT_CONTAMINACAO.md.

**Artefatos** (todos em `MANIFESTO_CERT.csv`):
- `cert_densidade.py` (598871cf…);
- `cert_densidade_testes.py` (2c583bbb…);
- `cert_densidade_testes_resultado.json` (dd01ccb0…);
- `cert_densidade_blocos.csv` (193f996e…);
- `cert_densidade_tabela.csv` (294ad352…);
- `cert_densidade_resumo.json` (b436cc1a…).

**Execuções anteriores inalteradas:** `cert_calculo.py` (95bec528…) e `cert_contaminacao.py` (4baff933…) não foram
modificados. `a_l1_sup` (execução 4) e `total_sup` (contaminação) são **lidos**.

**Corte:** (d₁, Δ) = (8, 2), escolhido após a avaliação exploratória.

#### II.22.1 Objeto e janela

**Decomposição registrada (R5):** F_w = F* + ρ_Δ + ρ_ord, com ρ_Δ(t) := ∫ w(E)e_t(E)Δ(E)dE e Δ := θ′/π − d̄_rvm.

**Fontes:**
- θ(t) = ph Γ(¼ + ½it) − ½t ln π (DLMF 25.10.2, arquivada);
- d̄_rvm(E) = (1/2π) ln(E/2π) (`d_bar_rvm` no código).

Logo Δ(E) = (1/2π)[Re ψ(¼ + iE/2) − ln(E/2)]. A derivada de ph Γ independe do ramo.

**Observável alvo:** F^rvm := F* + ρ_Δ, isto é, zeros exatos na janela e d̄_rvm integrada exatamente. Critério por par:

total^Δ_k := total_k(contaminação) + ‖a_k‖₁^sup·D_bloco/|c_k|_inf ≤ 10⁻⁶,

que majora |a_k·(F^rvm − M_𝒦)|/|c_k|.

**Janela fixada:** A* := E_c − L/2 e B* := E_c + L/2, com L = fl(B − A). É a única compatível com W(·; L), com as fases em
E_c e com ν_A, ν_B de P-RH.
- [A*, B*] coincide exatamente com [A, B] de `metrics.json` em 15 dos 30 blocos.
- Nos outros 15 (b04, b07, b10, c03, c05, c06, c08, c10, d01–d07), a diferença é ≤ 7,3·10⁻¹² e pertence à camada ρ_num.

#### II.22.2 Derivação da cota (sem dependência herdada)

Para E > 0 e z = ¼ + iE/2:

1. **Stirling para ψ.** DLMF 5.11.2: ψ(z) ~ ln z − 1/(2z) − Σ_{k≥1} B_{2k}/(2k z^{2k}). DLMF §5.11(ii), com n = 1:
   ψ(z) = ln z − 1/(2z) + R, |R| ≤ sec³(½ ph z)/(12|z|²).
   - Texto conferido no HTML arquivado (SHA-256 2199a198…).
2. **Fase e módulo:** ½ ph z ∈ (0, π/4), logo sec³ < 2√2; e |z|² ≥ E²/4.
3. **Três parcelas:**
   - ln|z| − ln(E/2) = ½ ln(1 + 1/(4E²)) ∈ [0, 1/(8E²)];
   - Re(1/(2z)) = (¼)/(2|z|²) ∈ (0, 1/(2E²)];
   - |Re R| ≤ 2√2/(3E²).
4. **Cota pontual:** |Δ(E)| ≤ C/E², com C := (1/8 + 1/2 + 2√2/3)/(2π).
5. **Janela Hann:** 0 ≤ w ≤ 1, ∫w = L/2, e C/E² decrescente. Logo sup_t|ρ_Δ(t)| ≤ D_bloco := C·(L/2)/A*².
6. **Projeção:** cada entrada Re/Im do vetor tem módulo ≤ |ρ_Δ(t_j)|, logo |a_k·ρ_Δ| ≤ ‖a_k‖₁^sup·D_bloco.

**Esta parcela não usa RH.** O total continua condicional a RH por causa de B^{RH″}.

**Dependência herdada eliminada:** `density_error_certified.py`/`.json` (revisão 11.3b-6; dd0a55bd…/64a8ad49…) **não
entram** no cálculo. Diferença de definição: o script antigo usava [A − 10⁻⁶, B + 10⁻⁶].

#### II.22.3 Cálculo

- **Constante:** C enclausurado em `mpmath.iv`; C^sup = extremo superior exato (fração), 0,249524558791954….
- **D_bloco** = C^sup·(L/2)/A*², em `Fraction` exata a partir dos floats registrados.
- **‖a_k‖₁^sup:** Fraction do float certificado da execução 4.
- **|c_k|_inf:** extremo inferior exato.
- **Total da contaminação:** Fraction de `total_sup`, string verificada ≥ soma exata.
- **Decisão:** frações exatas; ponto flutuante só em diagnóstico.
- **Exportações:** `sup_chk`.
- **Trava:** `--executar`.

#### II.22.4 Testes (T1–T21; todos passaram antes da execução)

| Teste | Resultado |
|---|---|
| T1–T15 (reaplicação de `cert_contaminacao_testes.py`, que reaplica `cert_testes.py`) | todos passaram. O resultado da execução 4 foi regenerado idêntico. O resultado da contaminação teve **conteúdo sem campos de tempo idêntico** (byte a byte difere só pelos tempos). Arquivos vigentes restaurados |
| T16 constante C | C^sup < 0,24953; C^sup ≤ cota racional elementar 0,26131 (√2 ≤ 99/70 porque 9801 ≥ 9800; π > 3); C > 0,2495 |
| T17 diagnóstico B | 2.020 valores de E (9,8·10³–7,4·10⁴ e 10–100), com Δ por `mpmath.digamma` a 50 dígitos: 0 violações de \|Δ\| ≤ C^sup/E². O máximo de \|Δ\|E²/C^sup é **0,0266**: a cota é ~37× frouxa. A causa **não foi medida** |
| T18 janela | A* > 0 e B* − A* = L, exatos, nos 30 blocos; 15 blocos com [A*, B*] ≠ [A, B], diferença ≤ 7,3·10⁻¹² |
| T19 decisão | 10⁻⁶ exato → sim; +10⁻²⁵ → não; −10⁻²⁵ → sim |
| T20 leituras | 1.410 pares com as mesmas chaves; total_sup ≥ soma exata em todos; B_rel e Sabs_rel iguais nas duas tabelas; ida-e-volta de `a_l1_sup` sem falhas; parada bit a bit da contaminação = [] |
| T21 herança (diagnóstico) | D_novo/D_antigo ∈ [0,99999996; 0,999999998], com D de 4,72·10⁻⁸ a 3,22·10⁻⁶ |

**Desvios de redação da declaração**, fixados **antes** de rodar os testes:
- **(a)** A comparação byte a byte de `cert_contaminacao_testes_resultado.json` é impossível, porque o arquivo contém tempos.
  O critério passou a ser o conteúdo sem campos de tempo.
- **(b)** T20 previa "`a_l1_sup` igual nas duas tabelas", mas a tabela da contaminação não tem essa coluna. Foi substituído
  por ida-e-volta, mesmas chaves e parada bit a bit limpa.

#### II.22.5 Resultados

| Item | Valor |
|---|---|
| **Elegíveis certificados** | **461/461**; nenhum elegível perdido frente à contaminação |
| Máximo de total^Δ nos elegíveis | **6,62126197·10⁻⁷** (m4-v3/d07, p = 2; antes 6,6090905·10⁻⁷); folga 1,51× |
| \|a_k·ρ_Δ\|/\|c_k\| nos elegíveis | 5,5·10⁻¹⁰ / 2,2·10⁻⁹ / **5,04·10⁻⁸** (mín / mediana / máx; máx em m4-v1/b01, p = 53) |
| Máximo por bloco | cai com a altura: b01 5,0·10⁻⁸, b02 3,6·10⁻⁸, b03 2,4·10⁻⁸ … d09 9,3·10⁻¹⁰, d10 9,0·10⁻¹⁰ (D ∝ L/A*²) |
| D_bloco máximo | 3,220602541·10⁻⁶ (b01) |
| Todos os pares certificados | **1.089/1.410** (antes 1.093); nenhum par passou a certificar |
| Tempo | 0,7 s de cálculo |

**Os 4 não elegíveis perdidos** estavam todos logo abaixo de 10⁻⁶:

| Par | Total na contaminação | Total^Δ |
|---|---|---|
| m4-v1/b02, 2⁴ | 9,176·10⁻⁷ | 1,0162·10⁻⁶ |
| m4-v1/b04, 139 | 9,912·10⁻⁷ | 1,0125·10⁻⁶ |
| m4-v1/b06, 3³ | 9,836·10⁻⁷ | 1,0100·10⁻⁶ |
| m4-v2/c07, 131 | 9,989·10⁻⁷ | 1,0017·10⁻⁶ |

#### II.22.6 Leitura e estado

**Estabelecido.** Para M^math, condicional a RH (F5 e J1 bibliográficas), na base de confiança declarada:

**|a_k·(F^rvm − M_𝒦)| ≤ 10⁻⁶·|c_k| nas 461 linhas elegíveis** (e em 1.089 dos 1.410 pares),

com F^rvm = F* + ρ_Δ: zeros exatos, d̄_rvm integrada exatamente, janela [A*, B*].

**Não estabelecido:**
- **ρ_ord:** ordenadas tabuladas; condicional à precisão declarada de 3·10⁻⁹ (classe B; F7);
- **ρ_num:** â_k em ponto flutuante, T_j em ponto flutuante, NUFFT/quadratura do termo suave, [A, B] × [A*, B*];
- **C2:** elegibilidade calculada no pipeline registrado, agregação, fase Q;
- S1, S3a, S3c;
- **H1**, que continua **aberta**.

Os 321 pares não certificados (todos não elegíveis) não refutam a desigualdade.

| Enunciado | Alvo | Situação |
|---|---|---|
| S2-ratio′(U₂ = 15) | \|a_k·(F* − M_{≤15})\| ≤ 10⁻⁶\|c_k\| | certificado sob RH, M^math, 461/461 (§II.20) |
| S2-ratio no ideal | \|a_k·(F* − M_𝒦)\| ≤ 10⁻⁶\|c_k\| | certificado sob RH, M^math, 461/461 (§II.21) |
| S2-ratio com densidade rvm | \|a_k·(F^rvm − M_𝒦)\| ≤ 10⁻⁶\|c_k\| | **certificado sob RH, M^math, 461/461 (§II.22)** |
| S2-ratio registrado | \|Re Ĉ_k/c_k − 1\| no código | não tratado (faltam ρ_ord e ρ_num) |
| S1, S3a, S3c | alvos sobre F* | abertos |
| H1 | observável → linhas | **aberta** |

**Próximos passos, com declaração própria:** ρ_ord (estrutura linear em δγ, condicional a F7), ρ_num e auditoria integral
independente.

### II.23 Erro das ordenadas tabuladas ρ_ord: observável F^tab, sob a hipótese H-tab (revisão 11.3b-28, 16/09/2026)

**Declaração:** `results/etapa11_r5/DECLARACAO_CERT_ORDENADAS.md` (SHA-256 a3382442…), gravada antes de qualquer código.
Reaproveita DECLARACAO_CERT.md, os adendos 1–3, DECLARACAO_CERT_CONTAMINACAO.md e DECLARACAO_CERT_DENSIDADE.md.

**Separação acordada:** esta etapa trata só de ρ_ord; ρ_num terá declaração própria.

**Artefatos** (todos em `MANIFESTO_CERT.csv`, SHA-256 3eb6b49e…):
- `cert_ordenadas.py` (884de087…);
- `cert_ordenadas_testes.py` (ca1365f1…, rodada 2);
- `cert_ordenadas_testes_resultado.json` (d68d8f1f…, rodada 2);
- `cert_ordenadas_testes_resultado_rodada1.json` (f9245a4a…, rodada 1, que falhou; preservado);
- `cert_ordenadas_blocos.csv` (2019550f…);
- `cert_ordenadas_tabela.csv` (c97f2c1c…);
- `cert_ordenadas_resumo.json` (b50e7f5a…).

**Não modificados:** `cert_calculo.py` (95bec528…), `cert_contaminacao.py` (4baff933…) e `cert_densidade.py` (598871cf…).
`a_l1_sup` e `total_densidade_sup` são **lidos**.

**Corte:** (d₁, Δ) = (8, 2), escolhido após a avaliação exploratória.

#### II.23.1 Hipótese H-tab e objeto

**(H-tab).** Com γ₁ ≤ γ₂ ≤ … as ordenadas positivas dos zeros não triviais **listadas com multiplicidade**, o decimal da
tabela satisfaz |γ_n^tab − γ_n| ≤ 3·10⁻⁹ para todo n ≤ 100.000.

**H-tab reúne:**
- a precisão declarada da fonte (F7, `bloqueado`);
- a correspondência índice ↔ posto (completude conferida só em classe B);
- a listagem com multiplicidade. A simplicidade (F2) deixa de ser necessária.

**Estado:** hipótese **não certificada**. Tem só validação amostral B: erro máximo ≤ 2,50·10⁻⁹ na etapa 2 e ≤ 2,22·10⁻⁹ em
30 índices no T23.

**Janela e extensão:** [A*, B*] = [E_c ∓ L/2]. f̃_t := w·e_t em [A*, B*] e 0 fora; f̃_t é C¹ em ℝ e f̃_t′ é lipschitziana,
mas f̃_t″ salta nas bordas.

**Índices:** I = índices com γ_n^tab ∈ [A^tab, B^tab], com os decimais da tabela; são 3.000 por bloco.

**Observável:** F^tab(t) := Σ_{n∈I} f̃_t(γ_n^tab) − ∫ f_t d̄_rvm. Usa as ordenadas **decimais** brutas de `data/raw/zeros1`
(3436c916…), não os floats do CSV processado.

#### II.23.2 Derivação

Seja S₂(t) = 2π²/L² + 2tπ/L + t².

1. **Lipschitz:** |f̃_t(y) − f̃_t(x) − f̃_t′(x)(y − x)| ≤ ½S₂(t)(y − x)² para quaisquer x, y reais, inclusive através das
   bordas, onde Lagrange de 2ª ordem não se aplica.
2. **Expansão em torno do valor tabulado (conhecido):** com δ_n = γ_n^tab − γ_n,
   f̃(γ^tab) − f̃(γ) = f̃′(γ^tab)δ_n − R_n, |R_n| ≤ ½S₂δ_n².
3. **Parcela linear projetada:** |a_k·Lin| ≤ 3·10⁻⁹·Σ_{n∈I}|g_k(γ_n^tab)|, com
   g_k(E) = Σ_j[aR_kj·Re f̃′_{t_j}(E) + aI_kj·Im f̃′_{t_j}(E)] e f̃′_t = e_t(w′ − itw) na janela.
   - É **pior caso sobre os sinais de δ_n**: não se supõe independência nem cancelamento.
4. **Resto projetado:** ≤ ‖a_k‖₁^sup·|I|·½(3·10⁻⁹)²·S₂(t_max).
5. **Zeros de borda fora de I que caem na janela:**
   - ficam a distância ≤ η = 3·10⁻⁹ + max|A* − A^tab|, |B* − B^tab| de uma borda, onde |f̃| ≤ (πη/L)²;
   - são contados por Z1 (derivada; J1 bibliográfica);
   - isso cobre d10, cuja borda superior é o último zero da tabela.
6. **Critério:** total^γ_k := total^Δ_k + [3·10⁻⁹Σ|g_k| + ‖a_k‖₁^sup(Resto + Borda)]/|c_k|_inf ≤ 10⁻⁶, por frações
   exatas.

#### II.23.3 Método

- **g_k(γ_n^tab):**
  - w e w′ por zero, em `mpmath.iv`;
  - cos e sin da fase por par (n, j), em `mpmath.iv` (~1,27·10⁶ pares por bloco);
  - soma em j com `isum` sobre Arows.
- **Reconstrução:** Arows vem de `cert_contaminacao.reconstruct`, com **parada bit a bit** contra a execução 4.
- **Termos analíticos:** S₂, η, Resto e Borda em frações exatas, com π e log por extremos exatos.
- **Execução:** decisão por frações exatas; exportações por `sup_chk`; trava `--executar`.
- **Desvio de custo (registrado):** a declaração estimava 3–8 min por bloco. O medido foi 405–1.051 s por bloco, e a execução
  completa levou **7.118 s** com 3 processos. O método não mudou.

#### II.23.4 Testes

**Rodada 1 (falhou; preservada).** Três falhas, diagnosticadas antes de qualquer alteração:
- **T1–T21:** a meta-condição "nenhuma saída de execução criada" dos testes da densidade só vale antes do `--executar` da
  densidade.
- **T22:** um sub-item acrescentado na implementação, e não na declaração, comparava o decimal bruto com o CSV processado. Deu
  73.341 divergências, todas ≤ 7,0·10⁻¹²: ruído de float do CSV, que pertence a ρ_num.
- **T25:** o critério relativo explodia nos zeros de borda (g ≈ 10⁻²¹, float exatamente 0). Nos zeros internos a distância
  absoluta ficou ≤ 1,7·10⁻¹³, compatível com avaliar em fl(E).

**Nenhuma das três indicou erro de método ou de enclausuramento.**

**Correções nos testes**, autorizadas explicitamente antes da rodada 2; método e decisão inalterados:
- **(1) T1–T21:** só podem diferir `nenhuma_saida_de_execucao_criada` e `todos_passaram`, e todos os `ok` substantivos
  continuam exigidos;
- **(2) T22:** a comparação bruto × processado vira diagnóstico ρ_num;
- **(3) T25:** tolerância 10⁻¹⁰·max|g| + ‖a_k‖₁·S₂·|fl(E) − E_dec|·1,01.

**Os critérios foram revistos depois de ver a rodada 1.** Isso fica registrado com a rodada 1 preservada.

**Rodada 2 (todos passaram):**

| Teste | Resultado |
|---|---|
| T1–T21 | diferem só as duas chaves previstas; T1–T15 e T16–T20 passaram; arquivos vigentes restaurados |
| T22 | tabela bruta com hash conferido, 100.000 linhas em ordem, 3.000 zeros por bloco, seleção do pipeline = I, bordas decimais = floats de `metrics.json`; \|A* − A^tab\| ≤ 1,09·10⁻¹¹; diagnóstico ρ_num: CSV × bruto ≤ 7,0·10⁻¹² |
| T23 (diagnóstico B de H-tab) | 30 índices contra `mpmath.zetazero`: máximo 2,22·10⁻⁹. **Não valida H-tab** |
| T24 Lipschitz | 10.000 pares, inclusive cruzando as bordas: 0 violações; pior razão 0,9988 (a cota é apertada) |
| T25 enclausuramento de g_k | 3 × 2.303 comparações: 0 acima da tolerância corrigida. Pior razão distância/tolerância: 0,67 (d01). Reconstrução bit a bit idêntica |
| T26 borda | η ≤ 3,011·10⁻⁹; vizinhos além do limiar; único bloco sem vizinho: d10 |
| T27 decisão | 10⁻⁶ exato → sim; ±10⁻²⁵ corretos |

**Execução de desenvolvimento (b01; descartada):**
- 16/16 elegíveis; parcela linear ≤ 1,05·10⁻⁷, consumindo ≤ 15,5% da margem;
- script e log apagados; nada gravado em `results/`.

#### II.23.5 Resultados (30 blocos)

| Item | Valor |
|---|---|
| Parada bit a bit | **limpa** (`parada_bit_a_bit = []`) |
| **Elegíveis certificados** | **461/461**; nenhum elegível perdido frente à densidade |
| Máximo de total^γ nos elegíveis | **7,31323657·10⁻⁷** (m4-v3/d10, p = 47; antes 6,0860·10⁻⁷); folga 1,37× |
| Parcela linear/\|c_k\| nos elegíveis | 2,09·10⁻⁸ / 7,53·10⁻⁸ / 1,13·10⁻⁷ / **1,25·10⁻⁷** (mín / mediana / p90 / máx; máx em m4-v3/d08, p = 47). Máximo por bloco estável, entre 1,0 e 1,3·10⁻⁷ nos 30 |
| m4-v3/d07, p = 2 (antigo pior caso) | linear 2,58·10⁻⁸; total 6,621·10⁻⁷ → 6,879·10⁻⁷; consumo de 7,6% da margem |
| Fração da margem consumida nos elegíveis | mediana 11,9%, máximo **31,4%** |
| Resto | ≤ 6,1·10⁻¹⁴ relativo |
| Borda | a string exportada vale 2,0·10⁻¹⁵, que é **piso da exportação com 15 casas**; o valor real é ≤ ~10⁻²¹ e a decisão usa frações exatas |
| Todos os pares certificados | **1.024/1.410** (antes 1.089); nenhum par passou a certificar |
| Marcação × string exportada | concordam nos 1.410 |

**Os 65 não elegíveis perdidos** se concentram nas linhas 127 (12), 7² (11), 5² (10), 131 (8), 2³ (7), 11² (4), 3³ (4) e
113 (3). O mecanismo não foi examinado.

#### II.23.6 Leitura e estado

**Estabelecido.** Para M^math, condicional a RH (F5 e J1 bibliográficas) **e a H-tab (não certificada)**, na base de
confiança declarada:

**|a_k·(F^tab − M_𝒦)| ≤ 10⁻⁶·|c_k| nas 461 linhas elegíveis** (e em 1.024 dos 1.410 pares),

com F^tab usando as ordenadas decimais da tabela, d̄_rvm exata e janela [A*, B*].

**Não estabelecido:**
- **ρ_num:** floats do CSV (≤ 7·10⁻¹² por ordenada), â_k e T_j em ponto flutuante, NUFFT/quadratura do termo suave, [A, B] ×
  [A*, B*] (≤ 1,1·10⁻¹¹);
- **C2:** elegibilidade do pipeline, agregação, fase Q;
- S1, S3a, S3c;
- **H-tab**, que não é certificada;
- **H1**, que continua **aberta**.

Os 386 pares não certificados (todos não elegíveis) não refutam a desigualdade.

| Enunciado | Alvo | Situação |
|---|---|---|
| S2-ratio′(U₂ = 15) | \|a_k·(F* − M_{≤15})\| | certificado sob RH, M^math, 461/461 (§II.20) |
| S2-ratio no ideal | \|a_k·(F* − M_𝒦)\| | certificado sob RH, M^math, 461/461 (§II.21) |
| S2-ratio com densidade rvm | \|a_k·(F^rvm − M_𝒦)\| | certificado sob RH, M^math, 461/461 (§II.22) |
| S2-ratio com ordenadas tabuladas | \|a_k·(F^tab − M_𝒦)\| | **certificado sob RH e H-tab, M^math, 461/461 (§II.23)** |
| S2-ratio registrado | \|Re Ĉ_k/c_k − 1\| no código | não tratado (falta ρ_num) |
| S1, S3a, S3c | alvos sobre F* | abertos |
| H1 | observável → linhas | **aberta** |

**Próximos passos, com declaração própria:** ρ_num e auditoria integral independente.

### II.24 Camada numérica ρ_num: fidelidade do valor registrado (N) e ligação teórica (T) (revisão 11.3b-29, 17/09/2026)

**Declaração:** `results/etapa11_r5/DECLARACAO_CERT_NUMERICO.md` (SHA-256 a120c1e2…), gravada antes de qualquer código.

**Artefatos** (todos em `MANIFESTO_CERT.csv`, SHA-256 2a2cd3bd…):
- `cert_numerico.py` (98e08195…);
- `cert_numerico_testes.py` (fd3c5599…);
- `cert_numerico_testes_resultado.json` (e32ff2f4…);
- `cert_numerico_blocos.csv` (45629bd8…);
- `cert_numerico_tabela.csv` (300d41bc…);
- `cert_numerico_resumo.json` (986a9859…).

**Não modificados:** `cert_calculo.py` (95bec528…), `cert_contaminacao.py`, `cert_densidade.py`, `cert_ordenadas.py`
(884de087…), o código congelado de `src/` e os runs de m4. `total_ordenadas_sup` é **lido**.

**Corte:** (d₁, Δ) = (8, 2), escolhido após a avaliação exploratória.

#### II.24.1 Fatos do código congelado (verificados antes da declaração)

- **Estimador primário:** `band_conjugate` resolve `np.linalg.lstsq(Mr, rhs)` e **não forma â_k**.
- **F(t_j) nos nós:** vem de `OscillatoryTransform.evaluate`, por soma direta sobre os zeros em float do CSV processado menos
  a soma direta do termo suave em quadratura de Gauss–Legendre. **Não usa NUFFT.**
- **Valor registrado:** `fit_ratio_to_theory` em `tables/<bloco>/arithmetic_matches.csv`, com 47 linhas por bloco e
  ida-e-volta exata nos 1.410 valores.
- **PROTOCOLO §11.2:** o "≤ 2,0·10⁻¹⁰" é medição B, não cota, e não foi usado.

**Consequência de método:** em vez de decompor em dados × operador, o que exigiria modelar a propagação de erro de
`lstsq`, das somas em float e da quadratura, enclausura-se diretamente X_k := a_k·F^tab (a_k de M^math) e compara-se com o
**número registrado**.

#### II.24.2 Enquadramento: o que é trivial e o que é acrescentado

- **Trivial:** |r̂_k − 1| **já é conhecido** por leitura do float registrado. Esta etapa não "descobre" que r̂_k ≈ 1.
- **(N) Fidelidade numérica, incondicional:** ε_k := |r̂_k − X_k/c_k|. X_k/c_k − 1 é medido em intervalo exato sobre os
  **dados tabulados**. **Sem RH, sem H-tab.** Não diz nada sobre zeros verdadeiros.
- **(T) Ligação teórica, sob RH, F5, J1 e H-tab:** como a_k·M_𝒦 = c_k, vale |X_k/c_k − 1| = |a_k·(F^tab − M_𝒦)|/|c_k| ≤
  total^γ_k (§II.23). Logo **|r̂_k − 1| ≤ ε_k^sup + total^γ_k**, ou seja, a proximidade registrada é **garantida pela teoria
  sob as hipóteses**, e não só observada.

#### II.24.3 Método

- **Parte discreta D(t_j):** Σ_{n∈I} w(γ_n^tab)e^{−i(γ_n^tab − E_c)t_j} sobre os decimais brutos, em `mpmath.iv` por par
  (zero, nó), com acumulação em intervalos com arredondamento para fora.
- **Termo suave S(t_j):**
  - **Expansão:** ln(E/2π) = ln(E_c/2π) + Σ_{m≤K}(−1)^{m+1}y^m/m + R_K, com y = x/E_c e resto
    |R_K| ≤ y_max^{K+1}/((K + 1)(1 − y_max)).
  - **Regra:** K_bloco = menor K com ρ_K := (1/2π)(L/2)·(esse resto) ≤ 10⁻²⁰; S alargado em ±ρ_K. Deu K = 22 (b01) a 11
    (blocos altos).
  - **Momentos da Hann:** M_m = ½J_m(t) + ¼J_m(t − β) + ¼J_m(t + β), com J_m = C_m − iS_m pela recorrência por partes
    (C_0 = 2 sin(ωa)/ω) e asserção ω > 0, em `mpmath.iv` com dps 60.
- **Decisões:**
  - X_k via `isum` sobre Arows e X_k/c_k com c_k enclausurado com sinal, em frações exatas;
  - ε_k^sup = sup|r̂_k − X_k/c_k|;
  - **(T)** ⇔ ε_k^sup + total^γ_k ≤ 10⁻⁶;
  - **alarme de consistência:** inf|X_k/c_k − 1| > total^γ_k interromperia a leitura.
- **Parada bit a bit** da reconstrução contra a execução 4.

#### II.24.4 Testes (T1–T34; todos passaram na primeira rodada)

| Teste | Resultado |
|---|---|
| T1–T27 | diferem só as chaves de meta-condição pós-execução (`nenhuma_saida_de_execucao_criada`, `todos_passaram`); `ok` substantivos passaram; arquivo vigente restaurado |
| T28 leitura | 30 × 47 linhas; 0 falhas de ida-e-volta; primário = `band_conjugate` em todos os blocos |
| T30 momentos | nos 20 casos, a primitiva fechada fica dentro do intervalo da recorrência; diferença relativa ≤ 9·10⁻¹⁷ |
| T31 resto e largura | K ∈ [11, 22]; ρ_K ≤ 10⁻²⁰ nos 30 blocos; largura de S ≤ 2,7·10⁻²⁰ |
| T34 decisões e alarme | borda de 10⁻⁶ correta; alarme dispara e silencia conforme esperado |
| T29 (diagnóstico) | reprodução de `targeted_joint_fit` com o `src/` atual: **d01 bit a bit (47/47)**; b01 e c01 diferem até 5,6·10⁻¹³ e 4,4·10⁻¹², consistente com m4-v1 e m4-v2 terem rodado com a versão anterior do código (PROTOCOLO §11.2). ε_k absorve essa diferença porque a comparação é com o valor **registrado** |
| T32 (diagnóstico) | \|S enclausurado − quadratura do código\| ≤ 2,2·10⁻¹¹ (\|S\| ~ 3·10⁻⁵) |
| T33 (diagnóstico) | \|D enclausurado − soma em float do código\| ≤ 9,6·10⁻¹¹ em 50 zeros |

**Desvio de redação, fixado antes de rodar:** T30 usou a primitiva fechada ∫x^m e^{cx}dx em `mpmath.mpc` (60 dígitos) em
vez de `mpmath.quad`, que é impraticável com ωa ~ 10³ oscilações.

**Execução de desenvolvimento (b01; descartada):**
- 16/16 elegíveis em (T), 0 alarmes;
- ε_k^sup nos elegíveis de 2,7 a 4,0·10⁻¹¹;
- script e log apagados.

#### II.24.5 Resultados (30 blocos; 5.277 s; execução iniciada pelo usuário com `.venv`)

| Item | Valor |
|---|---|
| Parada bit a bit | **limpa** (`[]`) |
| Alarme de consistência | **0 disparos** (resumo e tabela). Maior razão inf\|X_k/c_k − 1\|/total^γ_k: **0,609** |
| **(N)** ε_k^sup nos elegíveis | 2,65·10⁻¹¹ / 3,23·10⁻¹¹ / **6,27·10⁻¹¹** (mín / mediana / máx) |
| **(N)** ε_k^sup nos não elegíveis | 3,59·10⁻¹¹ / 4,93·10⁻¹¹ / 4,10·10⁻¹⁰ |
| **(N)** X_k/c_k − 1 nos elegíveis (ponto médio) | de −2,19·10⁻⁹ a 2,60·10⁻⁹; o maior \|r̂_k − 1\| registrado nos elegíveis é 2,605·10⁻⁹. Largura máxima dos intervalos: 6,8·10⁻¹⁰ |
| **(T) Elegíveis certificados** | **461/461** |
| Máximo de ε_k^sup + total^γ_k nos elegíveis | **7,313615663·10⁻⁷** (m4-v3/d10, p = 47); folga 1,37× |
| (T) todos os pares | **1.024/1.410**, conjunto idêntico ao certificado em §II.23 (ε_k não derrubou nenhum par) |
| Marcação × strings exportadas | concordam nos 1.410 pares |
| Larguras | S ≤ 2,7·10⁻²⁰; D ≤ 7,8·10⁻¹¹ (acumulada nos 3.000 zeros) |

**Leitura de ε_k:** o valor fica dominado pela **largura do intervalo** de X_k/c_k, e não por erro do código. Os
diagnósticos T32 e T33 mostram discrepâncias do código em float na ordem de 10⁻¹¹ em unidades de F.

#### II.24.6 Leitura e estado

**(N), incondicional, na base de confiança declarada.** Para os 1.410 pares, o valor registrado `fit_ratio_to_theory` coincide,
a menos de ε_k^sup ≤ 4,1·10⁻¹⁰ (≤ 6,3·10⁻¹¹ nos elegíveis), com o estimador matemático a_k de M^math aplicado a F^tab
(ordenadas decimais da tabela, d̄_rvm exata, janela [A*, B*]). A enclausura de X_k/c_k − 1 é uma medição exata sobre os
dados tabulados. **Não diz nada sobre zeros verdadeiros.**

**(T), sob RH (F5 e J1 bibliográficas) e H-tab (não certificada).** **|r̂_k − 1| ≤ ε_k^sup + total^γ_k ≤ 10⁻⁶ nas 461
linhas elegíveis** (e em 1.024 dos 1.410 pares): a condição por linha do C2 medida pelo pipeline registrado fica garantida
pela teoria sob essas hipóteses.

**Não estabelecido:**
- C2 inteiro (a elegibilidade calculada no pipeline, a agregação por fração e o critério de fase Q não foram tratados);
- S1, S3a, S3c;
- H-tab (não certificada);
- **H1**, que continua **aberta** (o que se tem é uma cadeia certificada condicional para o corte (8, 2) e o estimador
  primário).

**Riscos residuais:**
- base de confiança: IEEE-754 binary64, `mpmath.iv`, lema de somação, crivo;
- corte escolhido após a avaliação exploratória;
- ausência de auditoria integral independente.

| Enunciado | Alvo | Situação |
|---|---|---|
| S2-ratio′(U₂ = 15) | \|a_k·(F* − M_{≤15})\| | certificado sob RH, M^math, 461/461 (§II.20) |
| S2-ratio no ideal | \|a_k·(F* − M_𝒦)\| | certificado sob RH, M^math, 461/461 (§II.21) |
| S2-ratio com densidade rvm | \|a_k·(F^rvm − M_𝒦)\| | certificado sob RH, M^math, 461/461 (§II.22) |
| S2-ratio com ordenadas tabuladas | \|a_k·(F^tab − M_𝒦)\| | certificado sob RH e H-tab, M^math, 461/461 (§II.23) |
| Fidelidade do valor registrado (N) | \|r̂_k − X_k/c_k\| | **medido, incondicional: ≤ 6,3·10⁻¹¹ nos elegíveis (§II.24)** |
| S2-ratio registrado (T) | \|r̂_k − 1\| no código | **certificado sob RH e H-tab, 461/461 (§II.24)** |
| C2 inteiro; S1, S3a, S3c | — | abertos |
| H1 | observável → linhas | **aberta** |

**Próximos passos possíveis (a decidir):**
- auditoria integral independente da cadeia;
- elegibilidade, fração e fase Q (C2 inteiro);
- S1, S3a, S3c.
