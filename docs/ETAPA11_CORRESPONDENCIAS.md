# Etapa 11.4 — tabela de correspondências aritmética ↔ dinâmica

**Data:** 14/09/2026. **Estado:** entrega documental preliminar **concluída**, após os ajustes 11.4-1 (§6). As dependências de 11.3b continuam abertas (§5). Isto **não** libera seleção de candidatos nem congelamento de testes.

**Arquivos relacionados:**
- **Tabela completa:** [etapa11_correspondencias.csv](etapa11_correspondencias.csv), 20 linhas e 14 campos.
- **Matriz de classes:** [ETAPA11_MATRIZ_OPERADORES.md](ETAPA11_MATRIZ_OPERADORES.md).
- **Plano e convenções:** [ETAPA11_PLANO.md](ETAPA11_PLANO.md).
- **Fontes:** as páginas referem-se às cópias arquivadas em `archive/fontes_etapa11/`. Os SHA-256 foram reconferidos
  contra `MANIFESTO.csv` antes desta leitura, e todos coincidem. A eq. (2.17) de Berry–Keating foi conferida
  visualmente na página renderizada, porque a extração de texto era ambígua.

**Fora do escopo:** seleção de candidatos, protocolos experimentais e congelamento de testes (11.5).

## 1. Regras de leitura

1. **Uma linha é uma relação proposta**, não uma conclusão sobre uma classe. As 15 entradas da matriz que sustentam
   decisão continuam limitadas aos requisitos e às identificações declaradas. Nada aqui aprova ou exclui uma classe
   inteira.
2. **Objeto dinâmico "não especificado"** quando não há sistema definido. O papel que o objeto teria numa dinâmica
   hipotética vai em `papel_hipotetico`, separado, para não parecer um objeto existente.
3. **Natureza da relação.** Onde uma relação combina tipos, os dois são registrados. Os tipos:
   - **identidade demonstrada**: vale como teorema ou álgebra elementar, **com escopo** declarado;
   - **identidade condicional ou formal**: exige hipótese não demonstrada, ou é cálculo formal da fonte;
   - **aproximação**: assintótica ou semiclássica, com o limite indicado;
   - **analogia**: semelhança de forma sem mecanismo;
   - **reprodução numérica**: classe B do projeto;
   - **não especificado**.
4. **Conferência:**
   - `conferido`: página lida no arquivo arquivado; `conferido-secundaria` quando só a fonte secundária foi lida;
   - `derivacao`: argumento escrito nesta nota;
   - `PC`: pendente;
   - `NA`.
5. **A fórmula explícita como densidade de deltas** é condicional a RH enquanto identidade global (plano §3.2, L-EF2).
   Isso vale para toda linha que use (2.6) de Berry–Keating ou c(p, r).

## 2. Coerência de convenções (derivação; `conferencia=derivacao`)

**Relações usadas:**
- Berry–Keating (2.16): d_fl(E) = (1/πħ) Σ_j A_j cos(S_j/ħ);
- Berry–Keating (2.18): A_j = −log p / p^{m/2};
- no lado "Riemann": ħ = 1, S_j = E m log p.

**Consequências:**
- O coeficiente de cos(E m log p) na densidade é −log p/(π p^{m/2}). É exatamente o c(p, r) do plano §3.2, com r = m,
  na convenção e^{−iEt} e com linha em t = r log p.
- Pareando essa densidade com h par: ∫ h(E) cos(E log n) dE = 2π g(log n), para g(u) = (1/2π)∫h(r)e^{−iru}dr. Então
  −(1/π)Λ(n)n^{−1/2} · 2π g(log n) = −2Λ(n)n^{−1/2} g(log n), que é o termo primo da forma de referência (plano §3.1).
- As três formas (Berry–Keating, plano §3.1 e c(p, r) do instrumento) são **coerentes entre si**.

**Limite:** isso não substitui L-EF1. As constantes e a classe de funções-teste continuam sem conferência na fonte
primária (Guinand, Weil), e (2.6) é "divergent but formally exact" (Berry–Keating p. 240).

## 3. Correspondências prioritárias (resumo)

### 3.1 Primos ↔ órbitas primitivas

| ID | Aritmético | Dinâmico | Natureza | Fonte | Lacuna |
|---|---|---|---|---|---|
| C01 | primo p | **não especificado** (papel: órbita primitiva de uma "dinâmica de Riemann") | analogia | BK p. 240 (2.6), p. 241 (2.9), p. 242 (2.14); Connes p. 6 (A) | nenhum sistema com órbitas primitivas indexadas por primos |
| C02 | lugar v = p | órbita H_v da ação de C_k em X, isotropia k_v^* | identidade condicional (formal no global; demonstrada S-local, Teorema 4) | Connes p. 18, 26–27, 31 | global ⇔ RH (característica positiva; análogo para ℚ); avaliação p-ádica derivada em 11.3b §3 (log p·p^{−m/2} por camada m); não é fluxo hamiltoniano |
| C03 | análogo: geodésica primitiva ("primo geodésico") | geodésica fechada primitiva, comprimento ℓ_γ | identidade demonstrada (para a superfície) + analogia (com ζ) | Marklof p. 32–34 (Teorema 5, eq. 251) | ℓ_γ ≠ log p; a zeta de Selberg não é ζ |

### 3.2 Potências ↔ repetições

| ID | Aritmético | Dinâmico | Natureza | Fonte | Lacuna |
|---|---|---|---|---|---|
| C04 | p^r, com Λ(p^r) = log p | **não especificado** (papel: r-ésima repetição) | analogia, com coincidência estrutural | BK p. 242–243 (2.14), (2.17), (2.18); Marklof p. 25; Connes p. 18 (16), p. 86 (46) | repetições exigem objeto dinâmico existente |

**Coincidência estrutural registrada.** Nas três fórmulas lidas (Gutzwiller via BK (2.17), Selberg via Marklof
Teorema 4, Connes IV (16)), a amplitude de uma repetição carrega o período ou comprimento **primitivo** (T_p, ℓ_γ,
T_γ^#). Na fórmula explícita, Λ(p^r) = log p também é o "período primitivo". A coincidência é de forma e não fornece
mecanismo.

### 3.3 Frequências ↔ ações

| ID | Aritmético | Dinâmico | Natureza | Fonte | Lacuna |
|---|---|---|---|---|---|
| C05 | cos(E r log p); linha em t = r log p (e^{−iEt}); FFT: T = 2πf | **não especificado** (papel: S_p(E) = E T_p, T_p = log p, ħ = 1; sistema de escala) | analogia | BK p. 241 (2.11), p. 242 (2.14); Connes p. 6 | nenhum sistema com S_p = E log p; em bilhares S/ħ = kL é linear em k, e identificar k com E é reparametrização livre (Etapa 12) |
| C06 | linhas medidas em t = r log p, p ≤ 139 | **não especificado** | reprodução numérica (B) | RELATORIO_CONSOLIDADO; plano N2 | recupera a estrutura aritmética, não um objeto dinâmico |

### 3.4 Amplitudes ↔ estabilidade

| ID | Aritmético | Dinâmico | Natureza | Fonte | Lacuna |
|---|---|---|---|---|---|
| C07 | A_j = −log p/p^{m/2} = −(T_j/m)e^{−T_j/2}, "an identity rather than an asymptotic approximation" | **não especificado** (papel: expoente λ_p = 1 por unidade de tempo) | aproximação (e^{mλT} aproxima o determinante) + analogia | BK p. 242 (2.12), p. 243 (2.17)–(2.18); Connes p. 6–7 | nos zeros o exponencial é exato, no lado quântico é aproximação (BK p. 243) |
| C08 | p^{m/2} | **matriz transversal de retorno** 2×2 de uma órbita isolada (sem as direções neutras da monodromia completa do fluxo), com autovalores reais **positivos** e^{±Λ}, Λ > 0 | identidade demonstrada (álgebra, sob essas hipóteses, m ≥ 1) + analogia (Λ = log p) | derivação abaixo; Connes p. 7, p. 18 (restrição ao transversal); Marklof p. 25 | fator (1 − p^{−m}) sem contrapartida aritmética |
| C09 | −2Λ(n)n^{−1/2}g(log n) | ℓ_γ g(nℓ_γ)/(2 sinh(nℓ_γ/2)) | analogia (sinal, fator 2 e fator (1 − p^{−n})^{−1} diferem) | Marklof p. 13, 25; termo primo derivado de Weil via Connes App. II e verificado numericamente (11.3b §1) | ℓ_γ ≠ log p; classe de funções-teste de Weil PC |

**Normalização do expoente de instabilidade** (duas convenções nas fontes lidas):
- Berry–Keating (2.14) usa λ_p por unidade de tempo e obtém λ_p = 1, com T_p = log p.
- Connes p. 6 (A) escreve "instability exponents λ_p = ± log p", isto é, por período.
- As duas coincidem: λ_BK · T_p = λ_Connes.
- Registrado para evitar trocar uma pela outra em 11.5.

**Derivação (C08).**

**Hipóteses:**
- M é a matriz transversal de retorno 2×2, não a monodromia completa do fluxo, que tem direções neutras ao longo do
  fluxo e da energia;
- os autovalores são reais **positivos** e^{Λ}, e^{−Λ}, com Λ > 0;
- m ≥ 1.

"Hiperbólica em SL(2, ℝ)" sozinha não basta, porque admite autovalores negativos.

**Cálculo:**
- det(M^m − I) = (e^{mΛ} − 1)(e^{−mΛ} − 1) = 2 − 2cosh(mΛ) = −4 sinh²(mΛ/2), logo √|det(M^m − I)| = 2 sinh(mΛ/2);
- caso **não coberto** (autovalores −e^{±Λ}): det(M^m − I) = 2 − (−1)^m·2cosh(mΛ). Então √|det| = 2cosh(mΛ/2) para m
  ímpar e 2sinh(mΛ/2) para m par (conferido numericamente para m = 1, 2, 3);
- com Λ = log p: p^{m/2} − p^{−m/2} = p^{m/2}(1 − p^{−m});
- Connes (p. 7) registra o mesmo descasamento: "we do not have an equality for finite values of m".

### 3.5 Sinais ↔ fases

| ID | Aritmético | Dinâmico | Natureza | Fonte | Lacuna |
|---|---|---|---|---|---|
| C10 | sinal global − | **não especificado** (papel: Maslov π em todas as órbitas) | analogia com obstáculo registrado | BK p. 243 ("hard to understand… 2π for the same orbit traversed twice"); p. 260 | nenhuma atribuição de Maslov consistente com repetições |
| C11 | sinal global − | corpos de funções: Frobenius em H¹_et, com sinal − no traço de Lefschetz; ℚ: **não especificado** | identidade demonstrada (característica positiva; fonte primária não lida) + analogia (ℚ) | Connes p. 7–8, dicionário e princípio (C) | "absorção" para ℚ é interpretação; a tradução para N não está especificada |
| C12 | — | termos geométricos de Selberg, sinal + | identidade demonstrada (para a superfície) | Marklof p. 25 | sinal oposto ao da fórmula explícita |
| C13 | prefator 1/π | **não especificado** (papel: ausência de reversão temporal; com reversão, 2/π) | analogia | BK p. 242; Connes p. 7 (B), que exclui fluxos geodésicos | relação com N4 é compatibilidade empírica ao procedimento; T5 conjectural |

## 4. Correspondências complementares

| ID | Relação | Natureza | Lacuna principal |
|---|---|---|---|
| C14 | termo suave N̄ ↔ volume de fase (xp truncado reproduz 7/8; Connes com sinal −) | aproximação heurística | a regularização não define operador (BK p. 261) |
| C15 | teorema dos números primos ↔ proliferação de órbitas e^{λT}/T, λ = 1 | analogia | consistência, não derivação |
| C16 | produto de Euler ↔ determinante espectral semiclássico (BK 5.16) | analogia. Estatutos distintos: o produto de Euler é **identidade convergente para ℜs > 1** ([DLMF 25.2.11](https://dlmf.nist.gov/25.2#iv)), e seu uso direto na linha crítica exige outro tratamento (BK p. 240: "formally exact"); a expressão dinâmica é **aproximação semiclássica** (ħ → 0), sem convergência garantida | continuação do lado aritmético à faixa crítica não se faz pelo produto; ressomação semiclássica heurística |
| C17 | zeros ↔ autovalores de operador auto-adjunto | **não especificado** | lacuna central (M1 + M2) |
| C18 | zeros críticos ↔ Sp D_χ (Connes, δ > 1 **fixado**) | identidade demonstrada, com escopo (só críticos; multiplicidade espectral = maior n < (1+δ)/2 com n ≤ m_ρ; W não unitária) | para o δ fixado, igualdade total com multiplicidades ⇔ todos os zeros críticos (RH) **e** m_ρ < (1+δ)/2 para todo ρ. Um limite uniforme permitiria *escolher* δ grande, mas não garante a condição para um δ já fixado; nenhum limite é demonstrado |
| C19 | zeros de ζ_X(s) = Z(X, q^{−s}) para curva lisa X sobre F_q ↔ autovalores α_j do Frobenius geométrico F em H¹_et | identidade demonstrada (característica positiva) + analogia (ℚ). **Transformação explícita:** P_1(T) = det(I − TF \| H¹) = Π_j(1 − α_jT). Os zeros estão em T = α_j^{−1}, não em α_j. Com T = q^{−s}: q^s = α_j, e \|α_j\| = q^{1/2} ⇔ ℜs = ½ | convenção de Frobenius (geométrico × aritmético inverte os autovalores) e enunciado a conferir na fonte primária (**PC**; [Milne, LEC](https://www.jmilne.org/math/CourseNotes/LECc.pdf) indicada, não obtida: conexão recusada); não se transfere a ℚ sem construção |
| C20 | dilatação por K ↔ evolução por tempo log K no fluxo de xp | identidade demonstrada (elementar) + analogia (primos) | sem órbitas fechadas; compactificação não especificada (BK p. 262) |

## 5. O que a tabela sustenta e o que não sustenta

**Sustenta:**
- coerência interna das convenções (§2);
- três identidades demonstradas **dentro de seus objetos**:
  - Selberg para superfícies (C03, C12);
  - Connes, Teorema 1, para zeros críticos com δ > 1 fixado e multiplicidade truncada (C18);
  - a álgebra 2×2 sob as hipóteses da matriz transversal com autovalores positivos (C08);
- a lista de discordâncias registradas pelas próprias fontes: exatidão contra aproximação (C07), sinal e Maslov (C10),
  fator (1 − p^{−m}) (C08);
- a posição do resultado numérico do projeto (C06) como reprodução da estrutura aritmética.

**Não sustenta:**
- existência de um objeto dinâmico para ζ (C01, C04, C05, C10, C13, C17 com objeto não especificado);
- escolha entre classes;
- qualquer interpretação de N2, N3 ou N4 como reconstrução dinâmica.

**Pendências que afetam a tabela** (11.3b):
- L-EF1 (C09): parcialmente resolvida em 11.3b (termo primo derivado; termo arquimediano B; classe de funções-teste PC);
- integrais locais de Connes (C02): avaliação p-ádica derivada em 11.3b §3;
- fonte primária para o caso de corpos de funções (C11, C19);
- as demais da matriz §0.3.

## 6. Ajustes 11.4-1 (auditoria de 14/09/2026)

| # | Linha | Ajuste |
|---|---|---|
| 1 | C08 | M identificada como **matriz transversal de retorno**. Hipóteses Λ > 0, autovalores reais positivos e m ≥ 1 registradas também na coluna `hipoteses`. Caso de autovalores negativos registrado como não coberto |
| 2 | C18 | Para δ **fixado**, a condição é m_ρ < (1+δ)/2 para todo ρ, além de RH. "Multiplicidade limitada" só permitiria escolher δ. A mesma precisão foi aplicada na matriz (K3a) e na evidência E-K3a-M2 |
| 3 | C19 | Transformação explícita: P_1(T) = det(I − TF \| H¹), zeros em T = α_j^{−1}, T = q^{−s}; Frobenius geométrico. `conferencia=PC`, porque a fonte indicada (Milne, LEC) não pôde ser obtida (conexão recusada) e a convenção não foi conferida em página |
| 4 | C16 | Estatutos separados: produto de Euler convergente para ℜs > 1 (DLMF 25.2.11, HTML arquivado com SHA-256), uso direto na linha crítica exige outro tratamento; expressão dinâmica semiclássica |

Esses ajustes não alteram as demais linhas nem os códigos da matriz, exceto a redação da condição de K3a.
