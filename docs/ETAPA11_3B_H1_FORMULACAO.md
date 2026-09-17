# Etapa 11.3b / H1 — formulação precisa do enunciado de passagem "observável → linhas"

**Data:** 14/09/2026. **Estado de H1:** `em execução`, só formulação. Nenhum resultado demonstrado, nenhum cálculo novo.

**Estado de referência:**
- Z1 derivada (J1 bibliográfica);
- admissibilidade em 𝒜 derivada;
- L-EF1 com fechamento documental pendente de F5 e J1;
- F1, F2, F4, F6 e F7 `bloqueado`.

**Objetivo desta nota.** Fixar, antes de escolher uma rota, os quatro componentes do enunciado desejado:
1. observável;
2. modelo e truncamento;
3. norma do erro;
4. uniformidade.

Depois, listar enunciados candidatos e rotas **sem** pressupor que o limite ε → 0 seja a única abordagem.

---

## 1. Observável (instrumento congelado m4-v3)

**Parâmetros:** bloco com A < B zeros consecutivos da tabela, L = B − A, E_c = (A + B)/2. Nas faixas m4:
A ∈ [9,9·10³; 7,3·10⁴], L ∈ [2,0·10³; 2,6·10³], 3.000 zeros por bloco.

**O₁. Transformada:**

F_w(t) = Σ_{A≤γ≤B} w(γ)e^{−i(γ−E_c)t} − ∫_A^B w(E)d̄_rvm(E)e^{−i(E−E_c)t}dE, t ∈ I = [t_min, t_max] = [0,5; 5],

com w = sin²(π(E − A)/L) em [A, B] (código `periods.py`, idêntico ao arquivado m4-v3). Grades e tolerâncias
numéricas não fazem parte do enunciado matemático.

**O₂. Coeficientes estimados (usados em C2).** Catálogo 𝒦 = {(p, r) : r log p ∈ I}, isto é, n = p^r com 2 ≤ n ≤ 148.
Para cada k ∈ 𝒦, com T_k = r log p:
- **Bandas:** B_k = [T_k − δ, T_k + δ], δ = 0,5·FWHM = 2π/L, com 9 pontos por banda (`targeted_fit_half_width_fwhm =
  0.5`, `sampling = "band"`, `include_conjugate = true`).
- **Modelo linear:** F(t) ≈ Σ_k [(C_k/2)e^{iE_cT_k}W(t − T_k) + (C̄_k/2)e^{−iE_cT_k}W(t + T_k)], com W(ω) =
  ∫w e^{−i(E−E_c)ω}dE.
- **Estimador:** Ĉ = 𝒫(F|_{∪B_k}), mínimos quadrados reais nas partes real e imaginária. 𝒫 é linear e determinado só
  por (L, E_c, 𝒦, pontos).

**O₃. Detecção** (C1): |F_w(t)|/σ_null(t) numa grade de I, com limiar calibrado por nulos. O₃ envolve modelos
estatísticos nulos e **não** entra na formulação determinística de H1 (§6).

## 2. Modelo e truncamento

Para um conjunto finito 𝒩 de inteiros n ≥ 2, com c(n) = −Λ(n)/(π√n) (plano §3.2, derivado em 11.3b §2.2b):

M_𝒩(t) = Σ_{n∈𝒩} (c(n)/2)[e^{iE_c log n}W(t − log n) + e^{−iE_c log n}W(t + log n)].

**Resto:** R_𝒩(t) := F_w(t) − M_𝒩(t). Está **bem definido** para todo t, por ser diferença de quantidades finitas, sem
nenhuma hipótese de convergência.

**Truncamentos a comparar:**

| Nome | 𝒩 | Comentário |
|---|---|---|
| τ_cat | {n : log n ∈ I} (= catálogo 𝒦) | o usado em O₂ |
| τ_U | {n : log n ≤ U}, U ≥ t_max | inclui linhas acima de I, cuja cauda lateral atinge I |
| τ_ψ | pesos ψ(log n/U) suaves, ψ = 1 em [0, 1] | "somabilidade" com núcleo ψ; a família gaussiana e^{−ε²(log n)²/2} é um caso (rota R1) |

**Estrutura da cauda:**
- As linhas com log n > U atingem I só pelos lóbulos laterais de W. Para Hann, |W(ω)| = O(L⁻²|ω|⁻³) para |ω|L ≫ 1.
- A soma dos **módulos** dessas contribuições diverge, porque Σ_{log n≤U}Λ(n)n^{−1/2} ~ 2e^{U/2} (11.3b §2.3).
- Logo a majoração absoluta termo a termo está excluída. Isso **não** determina sozinho qual alternativa funciona
  (cancelamento nas fases, identidade exata, somabilidade; ver S3a/S3b/S3c).

## 3. Normas do erro

| Norma | Definição | Relevância |
|---|---|---|
| N∞(I) | sup_{t∈I} \|R_𝒩(t)\| | enunciado uniforme em frequência |
| N_band | max_k sup_{t∈B_k} \|R_𝒩(t)\| | é o que alimenta O₂ |
| N_coef | max_{k elegível} \|Re Ĉ_k/c_k − 1\| | é a grandeza **implementada** em C2 (`ratio_to_theory` = Re Ĉ_k/c_k; fase avaliada à parte); tolerância 10⁻⁶. A versão complexo \|Ĉ_k/c_k − 1\| é extensão (S2-complexo), não atribuída ao protocolo |
| N₂(I) | (∫_I \|R_𝒩\|² dt)^{1/2} | enunciado médio em t |
| N_bloco | média de N∞ ou N₂ sobre blocos, ou sobre A numa faixa de alturas | enunciado médio em altura |

**Normalização:** a escala natural das linhas é (|c_k|/2)W(0) = |c_k|L/4. As normas absolutas devem ser comparadas com
ela.

**Passagem N_band → N_coef (álgebra linear, sem hipótese analítica).** Como 𝒫 é linear e reproduz exatamente o modelo
quando F = M_𝒦:
- Ĉ − c = 𝒫(R_𝒦|_{∪B}), logo |Ĉ_k − c_k| ≤ ‖𝒫‖_{∞→∞} · N_band(R_𝒦).
- Com o condicionamento κ do sistema de O₂, ‖𝒫‖ ≲ κ·(escala 1/(L/4)).
- Um enunciado em N_band implica enunciado em N_coef com constante calculável a partir de (L, E_c, 𝒦). Um fator
  explícito de ‖𝒫‖ não foi calculado nesta nota.

## 4. Uniformidade exigida

Um enunciado utilizável deve declarar:
- **(U1)** uniformidade em t ∈ I (frequência), incluindo as bandas B_k, cujos centros T_k se acumulam (densidade de log n
  em I);
- **(U2)** dependência explícita em A (altura) e L (comprimento), na faixa A ∈ [10⁴; 7,5·10⁴], L ≈ 2·10³, ou
  assintótica com constantes explícitas;
- **(U3)** dependência em 𝒩 (U ou ψ);
- **(U4)** condicionalidade: incondicional, sob RH, ou sob outra hipótese nomeada;
- **(U5)** determinístico por bloco × médio (em t ou em blocos).

## 5. Enunciados candidatos (ainda não demonstrados)

| ID | Observável | Truncamento | Norma | Uniformidade | Força |
|---|---|---|---|---|---|
| S1 | O₁ | τ_cat ou τ_U | N∞(I) | por bloco, explícito em (A, L, U), incondicional | "nível de detecção"; **quantificado** em [ETAPA11_3B_H1_R5_ESTIMADOR.md](ETAPA11_3B_H1_R5_ESTIMADOR.md) §1 como sup_I\|F* − M_{≤U}\| ≤ B(A, L, U), com domínio de U e escala fixados; não implica C1 |
| S2 | O₂ | τ_cat | ver S2-ratio (implementado: Re Ĉ_k/c_k) e S2-complexo (extensão) em ETAPA11_3B_H1_R5_ESTIMADOR §3.3 | por bloco, explícito | condição por linha da parte (a) de C2; não inclui elegibilidade, agregação nem fase |
| S3 | O₁ | τ_ψ, U → ∞ | ver variantes S3a (corte abrupto), S3b (gaussiana), S3c (distribucional) em ETAPA11_3B_H1_R5_ESTIMADOR §2 | — | S3b derivada condicionalmente; S3a e S3c abertas |
| S4 | O₁ | τ_U | N₂(I) ou N_bloco | médio | versão média de S1 |
| S5 | O₁ com janela admissível w̃ (não compacta) | τ_ψ | N∞(I) | por bloco | vale para um **outro** instrumento; não reclassifica N3 de m4 |

**Escala empírica (classe B; não é hipótese nem demonstração).**
- **C2:** registrou |Ĉ_k/c_k − 1| ≤ 2,6·10⁻⁹ nas linhas elegíveis (RELATORIO_CONSOLIDADO §3.2), com tolerância 10⁻⁶.
- **Tradução para o resíduo local:** N_band(R_𝒦) é, empiricamente, várias ordens abaixo de |c_k|L/4.
- **Tamanho de uma demonstração útil (escala PROVISÓRIA, substituída):** a cifra 10⁻⁵–10⁻⁴ em unidades de F supunha
  norma de linha do estimador ~4/L, sem condicionamento nem acoplamento. **Substituída** por 5,5·10⁻⁶ a 1,2·10⁻⁴ (B),
  calculada em ETAPA11_3B_H1_R5_ESTIMADOR §3.6; não citar a cifra antiga como exigência. Resíduo
  pequeno em N_band é condição suficiente possível, não necessária: a condição exata é |e_kᵀM⁺ρ| ≤ τ|c_k|.
- Qualquer rota deve ser julgada contra essa distância. Não se infere daqui que S2 seja verdadeiro nem que seja
  demonstrável com as ferramentas listadas.

## 6. Rotas e o que cada uma pode dar

**Fato estrutural** (derivação elementar, tipo Paley–Wiener):
- Se g(u) = O(e^{−b|u|}) com b > 0, então h(r) = ∫g e^{iru}du é holomorfa na faixa |Im r| < b.
- Se, além disso, h tem suporte compacto na reta real, h ≡ 0 pelo teorema da identidade.
- Logo **nenhuma janela de suporte compacto em E** (como Hann em [A, B]) gera função-teste em 𝒜.
- Todo enunciado sobre o observável **congelado** O₁/O₂ sai da classe 𝒜 e exige outra ferramenta além da forma de
  referência aplicada diretamente.

| Rota | Ideia | Enunciado alcançável (esperado, não demonstrado) | Obstáculo conhecido | Fontes necessárias |
|---|---|---|---|---|
| R1 (mollifier gaussiano, ε → 0) | identidade exata para h_ε ∈ 𝒜 (11.3b §2.2b), depois ε → 0 | S3b **derivada condicionalmente** (R5 §2.1); S1 **aberta** (quantificada em R5 §1) | cota absoluta da cauda ~ e^{1/(8ε²)} não fecha (§2.3); precisa de controle uniforme em ε via cancelamento | as já lidas |
| R2 (fórmula de Landau–Gonek com janela) | Σ_{0<γ≤T} x^ρ = −(T/2π)Λ(x) + erro uniforme em x (Gonek); somação parcial contra w, com x = e^{t} (e conjugação complexa para a convenção e^{−iEt}; x^ρ = √x·x^{iγ} sob ρ = ½ + iγ) | S1 com erro relativo da ordem de (log A)/L (**expectativa heurística**, a verificar): suficiente para "detecção", provavelmente insuficiente para S2 | enunciado exato e termos de erro de Gonek não lidos; conversão de corte abrupto para janela; tratamento de x não inteiro (forma de W) | **F9**: Gonek (1993), *An explicit formula of Landau and its applications to the theory of the zeta-function* (Contemp. Math. 143), `bloqueado` por acesso |
| R3 (identidade de Stieltjes com S(E)) | F_w(t) = −∫S f_t′ + ∫f_tΔ (11.3b §2.2a) com fórmula truncada para S(E) (tipo Selberg) | S1 ou S4; sob RH, termos de erro menores | fórmulas explícitas para S com erro dependem de zeros próximos (incondicional) ou de RH | F4 e fonte de Selberg/Tsang para S(t) (**F10**, não identificada em servidor acessível) |
| R4 (trocar o observável) | janela w̃ admissível (por exemplo gaussiana em E), com a forma de referência aplicada diretamente | S5, com restos explícitos já parcialmente disponíveis (análogos a R_ε) | não fala do instrumento congelado; exige novo protocolo pré-registrado (Etapa 11.5+) | as já lidas, mais F1 para zeros fora da tabela |
| R5 (álgebra de O₂) | N_band → N_coef pela norma de 𝒫 | converte S1/S4 em enunciados sobre coeficientes | só transfere; não produz cota de R | nenhuma |

**Observação sobre R1 × R3.** R1 e R3 tratam o mesmo resto R por lados diferentes: primos amortecidos (R1) e S(E)
integrado contra f_t′ (R3). Por (a1), essa relação é exata. Uma cota em R3 dá imediatamente cota para o observável
**sem** passar por ε → 0. Isso mostra que o limite ε → 0 não é a única rota.

## 7. Recomendação de sequência (sem executar)

1. **Fixar o alvo inicial em S1**, com norma N∞(I) e truncamento τ_U, por bloco, com dependência explícita em (A, L, U).
   É o enunciado mais fraco que ainda diz algo sobre O₁, e as rotas R2 e R3 apontam para ele.
2. **Escolher entre R2 e R3 pela disponibilidade de fonte** (F9 × F4/F10). Enquanto as fontes estiverem bloqueadas,
   registrar o enunciado alvo e os lemas intermediários necessários, sem afirmar o resultado.
3. **Tratar S2 (nível C2) como problema separado**, cuja viabilidade não se deduz de S1. A distância empírica (§5)
   deve ser registrada, não interpretada.
4. **R4/S5** é o caminho para enunciados rigorosos de protocolos **futuros**, sem reclassificar resultados congelados.
5. **R5** (norma de 𝒫) é álgebra linear finita, útil depois que houver cota de N_band.

## 8. Pendências novas

| ID | Item | Natureza | Situação |
|---|---|---|---|
| F9 | Gonek (1993), fórmula de Landau uniforme | fonte para R2 | `bloqueado` (acesso) |
| F10 | fórmula truncada explícita para S(t) (Selberg 1944/1946; Tsang) | fonte para R3 | `bloqueado` (acesso; não localizada) |
| H1-S1 | enunciado S1 com constantes | matemático | aberto |
| H1-S2 | enunciado S2 (nível C2) | matemático | aberto; possivelmente fora do alcance das rotas listadas |
