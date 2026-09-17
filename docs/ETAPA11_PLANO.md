# Etapa 11 — plano: fórmulas de traço e classes de operadores

**Data:** 14/09/2026. **Revisão 11.3** e **ajustes 11.3b-1:** 14/09/2026, após duas auditorias do usuário (registro em
[ETAPA11_MATRIZ_OPERADORES.md](ETAPA11_MATRIZ_OPERADORES.md) §0.1 e §0.4).
**Escopo desta entrega:** plano e matriz bibliográfica **preliminar**
([ETAPA11_MATRIZ_OPERADORES.md](ETAPA11_MATRIZ_OPERADORES.md); CSV longo
[etapa11_matriz_operadores.csv](etapa11_matriz_operadores.csv); evidências
[etapa11_evidencias.csv](etapa11_evidencias.csv)). Os códigos não devem ser usados para selecionar ou excluir
candidatos enquanto houver entradas PC relevantes (§4).
**Fora do escopo:** implementação de candidatos, cálculo de autovalores e novos experimentos (Etapa 11b/12).
**Base empírica:** resultados congelados de M2–M4 nos zeros 1–100.000 ([RELATORIO_CONSOLIDADO.md](RELATORIO_CONSOLIDADO.md)).

## 1. Objetivo

Avaliar classes de operadores e sistemas dinâmicos propostos, ou propostáveis, para a interpretação espectral dos
zeros. Cada classe é descrita pelo que está **demonstrado**, **condicionado**, **não especificado** ou **incompatível**,
com fonte primária e hipóteses explícitas. Os resultados numéricos entram como restrições, **não** como reconstrução
dinâmica. Nenhum candidato é ajustado aos zeros observados.

## 2. Três tipos de restrição, mantidos separados

### 2.1 Tipo M — requisitos matemáticos de uma identificação espectral completa

Uma identificação espectral completa (programa de Hilbert–Pólya) exigiria **todos** os requisitos abaixo. Nenhum é
satisfeito pelos dados numéricos, que só podem ser compatíveis com eles.

| Código | Requisito |
|---|---|
| M1 | Espaço de Hilbert, domínio e operador **definidos sem usar os zeros**; auto-adjunticidade demonstrada (igualdade dos domínios do operador e do adjunto). |
| M2 | Espectro, com multiplicidades, **igual** ao conjunto {γ : ζ(½ + iγ) = 0 para zeros não triviais}, incluindo todos os zeros. Se algum zero estivesse fora da linha, seu γ seria complexo; M1 + M2 implicam RH, e por isso nenhuma construção pode assumir RH para provar M2. |
| M3 | Contagem espectral N(E) = θ(E)/π + 1 + S(E) (Berry–Keating 1999, SIAM p. 239, eqs. 2.1–2.4, secundária, escrita "for the t_n (assumed real)"; versão incondicional em Titchmarsh, 2.ª ed. rev. Heath-Brown (1986), §9.3, p. 212, **conferida em 17/09/2026**: N(T) conta todos os zeros de Ξ com 0 < t < T, e a forma exata sai somando as variações de argumento de s(s − 1), π^{−s/2}, Γ(s/2) e ζ(s); a citação anterior "DLMF §25.10" foi corrigida em 11.3b: a página define Z e ϑ, mas não traz a fórmula), o que inclui a média de Riemann–von Mangoldt N̄(E) = (E/2π)log(E/2π) − E/2π + 7/8 + O(1/E). |
| M4 | Fórmula de traço igual à fórmula explícita de Guinand–Weil (§3), com termo suave, amplitudes Λ(n)n^{−1/2} e sinal. |
| M5 | Simetria γ ↔ −γ (equação funcional) ou restrição explícita a γ > 0. |
| M6 | Multiplicidades compatíveis com as dos zeros. A simplicidade de todos os zeros não está demonstrada: é **lacuna** de referência. |

M3 e M4 são consequências de M2 somado a teoremas conhecidos. Aparecem separados porque candidatos parciais podem
reivindicar a estrutura de M3/M4 sem M2.

### 2.2 Tipo N — compatibilidade numérica com os zeros 1–100.000 (este projeto; classe B)

| Código | Restrição | Validade e ressalvas |
|---|---|---|
| N1 | Espaçamento médio unfolded 1,000 ± 0,0002 com N̄ de Riemann–von Mangoldt; variância de espaçamentos 0,145–0,164, crescendo com a altura | Alturas 14–7,5·10⁴ |
| N2 | Linhas em t = r log p (p ≤ 139, t ∈ [0,5; 5]) recuperadas sem catálogo; nenhuma detecção sem correspondência em 30 blocos | Só acima do limite de detecção de cada bloco; ausência de linha abaixo do limite não é evidência |
| N3 | Coeficientes −log p/(π p^{r/2}) e sinal negativo, na convenção de §3.2, concordância ≤ 2,6·10⁻⁹ nas linhas claramente detectáveis | Medição direcionada (não cega); dependência de janela/estimador ~10⁻⁶ nas linhas fracas |
| N4 | **Restrição empírica ao procedimento de comparação:** CDF de espaçamentos e K_c distintos de Poisson e do **controle GUE finito utilizado** (3.000 níveis centrais de GUE tridiagonal, unfolding pelo semicírculo); R₂ não rejeitado em 29 de 30 blocos | **Não implica incompatibilidade com universalidade GUE assintótica.** Vale para essas alturas, esse controle e esses estimadores |

**Consequência lógica central.** Qualquer operador que satisfaça M2 satisfaz automaticamente N1–N4, porque seu
espectro **é** o conjunto de zeros. N1–N4 só discriminam **candidatos parciais**: os que fazem predições independentes
(semiclássicas, assintóticas, estatísticas) sem reproduzir o espectro exato.

**Qualificações (revisão 11.3):**
- **"Por construção" vale só para os níveis efetivamente reproduzidos, com precisão suficiente.** Um candidato
  ajustado aos primeiros 500 zeros não satisfaz N1–N4 nos 100.000 zeros por construção. Fora dos níveis reproduzidos,
  a situação é L até ser calculada. Mesmo quando vale, isso não tem poder explicativo (controle K12).
- **Construções condicionais:** propriedades que dependem de hipótese não demonstrada (RH, multiplicidade limitada,
  suposições adicionais do autor) recebem **C**, nunca S.
- **Espectros de absorção ou ressonâncias** não são espectros de emissão. N1–N4 foram formuladas para uma sequência
  discreta de níveis reais. Aplicá-las a outro objeto espectral exige uma tradução explícita (qual sequência, qual
  medida, qual sinal), sem a qual a entrada é L.

### 2.3 Tipo T — resultados teóricos externos (classes A e D)

| Código | Enunciado | Classe e hipóteses |
|---|---|---|
| T1 | Correlação de pares de Montgomery com suporte de Fourier restrito (\|α\| < 1) | A, **sob RH** (Montgomery 1973) |
| T2 | Correlações de n níveis para suporte restrito | A, **sob RH** (Rudnick–Sarnak 1996, Duke Math. J. 81, 269–322) |
| T3 | Universalidade GUE/CUE completa das estatísticas locais dos zeros | D, conjectura |
| T4 | Correções de altura finita via CUE de dimensão efetiva | D, heurístico (Bogomolny et al. 2006); domínio validado N_eff ≳ 7,7 |
| T5 | Estatística local de sistemas caóticos genéricos segue GOE/GUE conforme a simetria de reversão temporal | D, conjectura BGS (Bohigas–Giannoni–Schmit 1984) |
| T6 | Sistemas com "caos aritmético" violam essa universalidade, com estatística próxima de Poisson | B/D: evidência numérica e semiclássica (Bolte–Steil–Steiner 1992; Bogomolny et al. 1992) |

## 3. Convenções da fórmula explícita (fixadas antes da avaliação das classes)

### 3.1 Forma de referência

Fontes primárias: Guinand (1948), Proc. London Math. Soc. (2) 50, 107–119; Weil (1952), Comm. Sém. Math. Univ.
Lund (vol. suppl. M. Riesz), 252–265.

Forma usada como referência de trabalho. As **constantes e a classe exata de funções-teste devem ser conferidas na
fonte primária antes de qualquer uso quantitativo**: esta é a lacuna L-EF1.

**Estado de L-EF1 (11.3b; [ETAPA11_3B_FORMULA_EXPLICITA.md](ETAPA11_3B_FORMULA_EXPLICITA.md) §1):**
- **Parcialmente resolvida.**
- A soma sobre todos os zeros, os termos de polo e o termo primo (coeficiente 2, sinal −, peso n^{−1/2}) foram
  derivados de Weil na forma de Connes (App. II, p. 68–79; secundária).
- O termo arquimediano (−g(0)log π + (1/2π)∫h Re ψ) foi **derivado analiticamente** (H2;
  [ETAPA11_3B_TERMO_ARQUIMEDIANO.md](ETAPA11_3B_TERMO_ARQUIMEDIANO.md)) de Connes App. II e DLMF 5.9.12, para a classe 𝒢
  (h par, ∫|h|(1+r²) < ∞, g ∈ L¹). A checagem B é verificação final.
- Aplicar o Teorema 1 de Weil a 𝒢 exige ainda o decaimento (G4) e o que F5 vier a exigir.
- **Classe suficiente 𝒜** (g par C^∞, e^{|x|/2}|g^{(j)}| ∈ L¹ para j ≤ 4, |g| ≤ Ce^{−b|x|} com b > ½): admissibilidade
  derivada do Teorema 6 de Connes por aproximação ([ETAPA11_3B_ADMISSIBILIDADE.md](ETAPA11_3B_ADMISSIBILIDADE.md)),
  com ponto de partida no Teorema 6 e no Lema 3 de Connes (conferidos) e Z1 derivado
  ([ETAPA11_3B_Z1_CONTAGEM.md](ETAPA11_3B_Z1_CONTAGEM.md)). Pendências só bibliográficas: F5 (Weil original) e J1
  (fonte de Jensen). As gaussianas e h_ε pertencem a 𝒜; a janela de Hann sem suavização não. A admissibilidade para
  cada ε > 0 não controla o limite ε → 0 (H1).
- A classe exata de funções-teste continua **PC**: fonte primária não obtida.
- A classe de hipóteses escrita abaixo é a de trabalho, não a conferida. Para h par, holomorfa numa faixa
|Im r| ≤ ½ + δ, com decaimento |h(r)| ≪ (1 + |r|)^{−1−δ}, e g(u) = (1/2π) ∫ h(r) e^{−iru} dr:

```
Σ_ρ h(γ_ρ) = h(i/2) + h(−i/2) − g(0) log π + (1/2π) ∫ h(r) Re ψ(¼ + ir/2) dr − 2 Σ_{n≥1} Λ(n) n^{−1/2} g(log n)
```

A soma é sobre **todos** os zeros não triviais ρ = ½ + iγ_ρ. Sem RH, γ_ρ pode ser complexo e h precisa ser avaliada
fora do eixo real; daí a exigência de holomorfia.

### 3.2 Leitura distribucional e convenção de Fourier deste projeto

- **Variável.** E = γ, a ordenada. Coeficientes e períodos valem em E. O unfolding x = N̄(E) é não linear e muda as
  frequências; nenhum coeficiente é transferido para x.
- **Ressalva de RH (revisão 11.3).** A forma §3.1 soma h(γ_ρ) sobre todos os zeros, com γ_ρ possivelmente complexo.
  Escrever uma densidade de deltas numa variável **real** E pressupõe γ_ρ real para todos os zeros. Sem RH, a passagem
  de §3.1 para a densidade abaixo **não** é uma identidade incondicional. A medida Σ δ(E − Im ρ) existe sempre, mas a
  fórmula explícita pareia h(γ_ρ), não h(Im ρ), e as duas diferem para zeros fora da linha. Nos dados usados, as
  ordenadas vêm de zeros verificados na linha crítica. A contribuição dos zeros não incluídos, com h avaliada fora do
  eixo real se houver zeros não críticos, é parte da lacuna L-EF2. Leitura válida sem RH: a densidade abaixo é
  **condicional a RH** como identidade global, e **incondicional só como aproximação local** cujo erro exige o
  enunciado de L-EF2.
- **Densidade formal (condicional a RH; ver ressalva).** d(E) = Σ δ(E − γ) = (1/2π)[Re ψ(¼ + iE/2) − log π] − (1/π) Σ_n Λ(n) n^{−1/2} cos(E log n) + (termos de h(±i/2)).
  A soma sobre n **não converge** pontualmente na linha crítica; tem sentido só pareada com funções-teste
  adequadas. É uma identidade de distribuições, não uma série ordinária.
- **Coeficiente.** Com n = p^r, Λ(n) = log p e n^{−1/2} = p^{−r/2}, o coeficiente de cos(E r log p) é
  c(p, r) = −log p / (π p^{r/2}), com período T = r log p na convenção e^{−iEt}. Para uma FFT em e^{−2πifE}, T = 2πf.
- **Instrumento.** F_w(t) = Σ w(γ) e^{−i(γ−E_c)t} − ∫ w(E) d̄(E) e^{−i(E−E_c)t} dE, com janela de Hann em [A, B] ⊂ (0, ∞).
  Um termo c·cos(ET) produz (c/2)e^{iE_cT}W(t − T) + (c/2)e^{−iE_cT}W(t + T), e o estimador é C = 2a·e^{−iE_cT}.
- **Lacuna L-EF2 (ampliada na revisão 11.3).** Duas questões:
  - **(a) Admissibilidade.** A janela de Hann tem suporte compacto em E, não é analítica e é unilateral (E > 0).
    **Não** é uma função-teste admissível na forma de §3.1.
  - **(b) Condicionalidade.** Passar da soma sobre γ_ρ complexos para deltas reais exige RH ou um termo de erro
    explícito para eventuais zeros fora da linha, fora da janela e na cauda.

  A concordância numérica (N3) usa a leitura distribucional com corte, e o enunciado rigoroso para essa observável,
  com (a) e (b), está pendente desde PROTOCOLO §8.5. Por isso N3 é classe **B**, não **A**.

  **Estado 11.3b** (revisão 11.3b-2; [ETAPA11_3B_FORMULA_EXPLICITA.md](ETAPA11_3B_FORMULA_EXPLICITA.md) §2):
  - **(a)** Identidade de Stieltjes exata para todas as ordenadas com multiplicidade. A identificação com a tabela
    exige completude (conferida, classe B, nos 30 blocos) e criticidade e simplicidade (PC). O termo determinístico
    integrado tem cota **certificada** ≤ 3,2·10⁻⁶, módulo DLMF §5.11(ii); a estimativa B é ≤ 8,6·10⁻⁸.
  - **(b)** Identidade suavizada com fator 2 explícito. O termo de linha (c/2)[e^{iE_cT}W(t − T) + e^{−iE_cT}W(t + T)]
    sai por derivação. Os restos têm prefatores. A cauda de zeros acima de H₀ é separada, não eliminada. Condicionada a
    L-EF1, a Platt–Trudgian (PC) e a uma cota explícita de contagem (PC).
  - **(c)** Aberta. A cota absoluta utilizada não fecha. Enunciado formulado em
    [ETAPA11_3B_H1_FORMULACAO.md](ETAPA11_3B_H1_FORMULACAO.md): alvo inicial S1 (N∞ em I, truncamento por log n ≤ U,
    por bloco); rotas R1–R5. Janelas de suporte compacto em E nunca estão em 𝒜.
    **Estado de H1 (revisão 11.3b-26, 16/09/2026):**
    - **S3b:** derivada condicionalmente (|F* − M_ε| ≤ Kε²; F1, com F5 e J1 bibliográficas);
    - **S1:** quantificado e **aberto**;
    - **R5:** formalizado, cálculo finito B executado e diagnósticos **encerrados**
      ([ETAPA11_3B_H1_R5_ESTIMADOR.md](ETAPA11_3B_H1_R5_ESTIMADOR.md));
    - **Cauda Projetada:**
      - P-RH (condicional a RH) e P-RH-trunc derivadas;
      - condição suficiente para S2-ratio′(U₂) certificada computacionalmente em (d₁, Δ) = (8, 2) para M^math, em
        461/461 linhas elegíveis;
      - execução 4 vigente e congelada, com a dependência herdada de c₁ e c₂ eliminada; auditoria integral independente
        pendente ([ETAPA11_3B_H1_CAUDA_PROJETADA.md](ETAPA11_3B_H1_CAUDA_PROJETADA.md) §II.20);
    - **Abertos:** S3a e S3c; a passagem ao estimador registrado (ordenadas, densidade, código) é camada adicional
      pendente. **H1 continua aberta.**
  - A checagem gaussiana de L-EF1 é consistência (B) dentro de um orçamento estimado, não precisão certificada. A
    diferença entre quadraturas é estimativa de estabilidade, não cota.
  - Fontes e hipóteses pendentes, com o registro de acesso: [ETAPA11_PENDENCIAS_FONTES.md](ETAPA11_PENDENCIAS_FONTES.md).

### 3.3 Fórmula de Selberg e fórmula de Gutzwiller, para comparação

Estas formas são usadas na matriz só para comparar **estrutura** (períodos, amplitudes, sinais). As versões precisas
ficam nas fontes primárias.

- **Selberg** (1956), J. Indian Math. Soc. 20, 47–87, para superfícies hiperbólicas compactas:
  - lado espectral Σ_j h(r_j), com λ_j = ¼ + r_j²;
  - termo de área (Area/4π) ∫ h(r) r tanh(πr) dr;
  - termos geométricos Σ_{γ primitivas} Σ_{n≥1} ℓ_γ g(nℓ_γ) / (2 sinh(nℓ_γ/2)), com **sinal positivo**. A amplitude
    completa contém o **comprimento primitivo ℓ_γ** como fator; comparar só 1/(2 sinh(nℓ/2)) omite esse fator.
  - Enunciado conferido em fonte secundária rigorosa: Marklof, *Selberg's trace formula: an introduction*,
    arXiv:math/0407288, Teorema 4 (p. 25 da versão arXiv). Superfície compacta; h satisfaz (H1) analítica em
    |Im ρ| ≤ σ com σ > ½, (H2) par, (H3*) decaimento rápido na faixa (p. 12); g(t) = (1/2π)∫h(ρ)e^{−iρt}dρ (eq. 69,
    p. 13), mesma convenção de §3.1. A fonte primária (Selberg 1956) não foi lida.
  - Ressalva: termos elípticos e parabólicos (caso cofinito) não estão cobertos por esse enunciado (Marklof §15, p. 35–36).
- **Gutzwiller** (1971), J. Math. Phys. 12, 343–358: aproximação semiclássica (ħ → 0), não identidade exata.
  - amplitudes T_p / |det(M_p^r − I)|^{1/2};
  - fases de Maslov.

## 4. Campos obrigatórios por classe

Todos os campos abaixo são obrigatórios. Um campo vazio é marcado **L (lacuna)**, que não conta nem como aprovação
nem como refutação.

1. Espaço, domínio, medida e condições de contorno.
2. Auto-adjunticidade, tipo de espectro (discreto, contínuo, ressonâncias) e contagem espectral.
3. Fórmula de traço: forma, regularização, períodos, amplitudes e sinais.
4. Resultados **demonstrados**, com fonte e hipóteses.
5. Propriedades **não especificadas**.
6. **Incompatibilidades conhecidas ou derivadas**: fonte com página, ou derivação escrita para o sistema concreto e suas
   hipóteses de regularidade. Sem isso, o requisito recebe L ou PC, não V.
7. **Teste discriminante possível**, formulado sem ajustar o candidato aos zeros.

Códigos de situação por requisito, usados no CSV:

| Código | Significado |
|---|---|
| S | Demonstrado satisfeito. **Exige** registro de página, enunciado, hipóteses e argumento aplicável (tabela de evidências) |
| V | Violado ou incompatível: demonstrado, ou derivado de forma elementar com o argumento escrito. **Mesma exigência de S** |
| C | Condicional: depende de RH, de conjectura ou de suposição adicional não demonstrada |
| P | Parcial ou heurístico (semiclássico, assintótico, apenas alguns termos, suposições adicionais declaradas) |
| L | Lacuna: não especificado. Não é aprovação nem refutação |
| PC | Pendente de conferência (código criado na revisão 11.3): há alegação na literatura ou argumento plausível, mas página, enunciado ou hipóteses ainda não foram conferidos. **Não** pode ser usado para selecionar nem excluir |
| NA | Não se aplica |

Um registro bibliográfico verificado (título, autores, periódico) **não** sustenta sozinho S ou V. Cada S e V da
matriz tem uma linha em [etapa11_evidencias.csv](etapa11_evidencias.csv).

**Dois campos separados (revisão 11.3b-1).** O CSV da matriz registra, para cada classe × requisito:
- `situacao`: estado matemático ou empírico, com os códigos acima. Aqui PC significa que o estado ainda não foi
  estabelecido por derivação ou estimativa;
- `conferencia`: estado bibliográfico do suporte:
  - `conferido`: página lida no arquivo arquivado;
  - `derivacao`: argumento escrito na tabela de evidências;
  - `elementar`;
  - `PC`: enunciado ou página não conferidos;
  - `NA`.

"Depende de RH" (`situacao=C`) e "enunciado não conferido" (`conferencia=PC`) são informações distintas. Uma entrada só
sustenta decisão (`sustenta_decisao=sim`) se for S/V com `conferencia` ∈ {conferido, derivacao, elementar}. Mesmo
assim, a seleção de candidatos e o congelamento de testes aguardam as evidências pertinentes (11.5).

**Escopo assintótico × faixa finita.** Uma incompatibilidade assintótica de contagens (lei de Weyl contra
Riemann–von Mangoldt) sustenta V em M2/M3 sob as identificações declaradas. **Não** sustenta V em N1, que é uma
tolerância numérica numa faixa finita de alturas. Para N1 é preciso estimativa com erro controlado na faixa ou
experimento específico. Densidades locais não podem ser obtidas derivando uma equivalência assintótica de uma
contagem em degraus sem justificativa.

**Fontes consultadas** ficam arquivadas em `archive/fontes_etapa11/` (versão, URL, data, SHA-256, correspondência de
páginas).

## 5. Princípios dos testes discriminantes

1. **Predição antes do cálculo.** Para cada candidato, registrar e congelar a predição (contagem, períodos, amplitudes,
   sinais, classe de simetria) a partir da teoria do candidato, antes de calcular autovalores.
2. **Nenhum parâmetro estimado a partir dos zeros.** Parâmetros livres vêm da teoria do candidato ou de princípios
   declarados. Se inevitável, a calibração usa só dados já consultados (índices ≤ 10.000), com penalização explícita
   de complexidade; conclusões nesse caso são exploratórias.
3. **Mesmo instrumento.** Espectros de candidatos passam pela cadeia congelada (m4-v3): contagem, F_w, detector sem
   catálogo, matching, medição direcionada e envelopes, com os mesmos critérios e as mesmas incertezas.
4. **Incompatibilidades analíticas primeiro.** Quando a contagem ou a estrutura da fórmula de traço já é incompatível
   por teorema (por exemplo, lei de Weyl polinomial), o teste é analítico e não exige cálculo. Registra-se a derivação.
5. **Controles obrigatórios:**
   - **K12, controle de ajuste:** matriz diagonal com os zeros, que passa por N1–N4 **nos níveis inseridos** sem explicar nada;
   - **controle dinâmico:** sistema caótico com espectro conhecido e simetria declarada (original, Etapa 11.6), para
     verificar que o instrumento distingue períodos genéricos de log p;
   - **controle aritmético:** superfície hiperbólica (compacta aritmética ou de congruência), com caos aritmético e
     estatística não universal. **Revisão 11.3:** o controle **não** exige "nenhuma detecção em r·log p". Comprimentos
     geodésicos distintos podem cair dentro da resolução do instrumento (FWHM = 4π/L) de algum r·log p. O protocolo
     deve fixar antes do cálculo:
     1. a lista prevista de comprimentos nℓ_γ no intervalo de t;
     2. as amplitudes completas ℓ_γ/(2 sinh(nℓ_γ/2)), com a normalização de §3.3 convertida para a convenção de §3.2;
     3. a tolerância de correspondência;
     4. a taxa esperada de **correspondências acidentais** com o catálogo r·log p, calculada a partir das duas listas
        e da resolução.

     O resultado é avaliado contra a predição geométrica, não contra a ausência de linhas aritméticas.
6. **Discrepâncias.** Uma incompatibilidade com N4 **nunca** é tratada como refutação de universalidade GUE assintótica;
   só como diferença nas condições comparadas.

## 6. Sequência de trabalho da Etapa 11

| Subetapa | Conteúdo | Entregável | Estado |
|---|---|---|---|
| 11.1 | Fixar convenções (§3) e restrições M, N, T (§2) | este plano | `em execução` (revisado em 11.3: ressalva de RH, L-EF2 ampliada, "por construção" qualificado) |
| 11.2 | Matriz bibliográfica por classe, com fontes primárias e hipóteses | `ETAPA11_MATRIZ_OPERADORES.md`, CSV | `em execução` (matriz preliminar) |
| 11.3 | Conferência (inclui ajustes 11.3b-1: N1 de K5a/K7/K9 → PC, campos `situacao`/`conferencia`, arquivo de fontes): seis pontos da auditoria; evidências por S/V; fontes acessíveis lidas (Connes, Conrey–Li, BBM, Bellissard, réplica, Sierra, Sierra–Townsend, Berry–Keating SIAM, Marklof) | matriz revisada, `etapa11_evidencias.csv` | `em execução`: seis pontos da auditoria tratados (fechados); o trabalho seguinte continua em 11.3b; entradas PC restantes listadas na matriz §0.3 |
| 11.3b | Fórmula explícita e passagem observável → linhas: L-EF1 (termo primo, fator 2; **H2** termo arquimediano derivado para 𝒢), **admissibilidade** (classe 𝒜 via Teorema 6 de Connes), **Z1** (contagem N(T) ≤ 31 + 5,25·T·log(T + 9) via DLMF e Jensen), L-EF2a/b, **H1** (formulação S1–S5, rotas R1–R5), **R5** (operador resíduo → coeficientes) e **Cauda Projetada** (P-RH, P-RH-trunc, Lemas 4′ e 5′, certificação computacional) | [ETAPA11_3B_FORMULA_EXPLICITA.md](ETAPA11_3B_FORMULA_EXPLICITA.md), [ETAPA11_3B_TERMO_ARQUIMEDIANO.md](ETAPA11_3B_TERMO_ARQUIMEDIANO.md), [ETAPA11_3B_ADMISSIBILIDADE.md](ETAPA11_3B_ADMISSIBILIDADE.md), [ETAPA11_3B_Z1_CONTAGEM.md](ETAPA11_3B_Z1_CONTAGEM.md), [ETAPA11_3B_H1_FORMULACAO.md](ETAPA11_3B_H1_FORMULACAO.md), [ETAPA11_3B_H1_R5_ESTIMADOR.md](ETAPA11_3B_H1_R5_ESTIMADOR.md), [ETAPA11_3B_H1_CAUDA_PROJETADA.md](ETAPA11_3B_H1_CAUDA_PROJETADA.md), [ETAPA11_PENDENCIAS_FONTES.md](ETAPA11_PENDENCIAS_FONTES.md), `results/etapa11_3b/`, `results/etapa11_r5/` | `em execução`: H2 derivada; 𝒜 e Z1 derivados (F5, J1 bibliográficas); S3b derivada condicionalmente; S1 quantificado e aberto; R5 encerrado; condição suficiente para S2-ratio′(U₂) certificada sob RH para M^math em (8, 2), 461/461 elegíveis (execução 4 vigente); S3a, S3c e passagem ao estimador registrado pendentes; **H1 aberta**; F1–F11 bloqueadas por acesso |
| 11.4 | Tabela de correspondências "primo ↔ órbita primitiva", "r ↔ repetição", frequências/ações, amplitudes/estabilidade, sinais/fases, separando identidade demonstrada, identidade condicional, aproximação e analogia | [ETAPA11_CORRESPONDENCIAS.md](ETAPA11_CORRESPONDENCIAS.md), `etapa11_correspondencias.csv` | **concluída como entrega documental preliminar** (20 linhas; ajustes 11.4-1). Dependências de 11.3b abertas (C02, C09, C11, C19); não libera seleção de candidatos nem congelamento de testes |
| 11.5 | Protocolo pré-registrado dos testes discriminantes para 2–3 classes com operador concreto (§5) | `ETAPA11b_PROTOCOLO.md` | pendente (próxima etapa) |
| 11.6 | Controles dinâmico, aritmético e de ajuste: especificação e fontes | idem; declarações em `results/etapa11_6_controles/` | `em execução`: **K12 declarado** em 17/09/2026 ([DECLARACAO_K12.md](../results/etapa11_6_controles/DECLARACAO_K12.md), identificação com as execuções primárias m4-v1/v2/v3, sem cálculo novo); controles dinâmico e aritmético pendentes |

**Critério de aceite da Etapa 11** (plano original):
- nenhum candidato é favorecido só por ajustar níveis ou apresentar repulsão;
- cada incompatibilidade está ligada a uma propriedade verificável;
- cada propriedade desconhecida está explícita.

## 7. Limites desta entrega

- A matriz é bibliográfica e **preliminar**. Um V derivado só é mantido com o argumento escrito na tabela de
  evidências. Exclusões sem derivação para o sistema concreto foram rebaixadas a L ou PC (revisão 11.3).
- Afirmações apoiadas só em resumo ou em fonte não lida são PC ou P, nunca S ou V.
- Páginas citadas de artigos lidos no arXiv seguem a paginação da versão arXiv, que pode diferir da publicada.
- A matriz não ordena candidatos. Nenhum critério de proximidade a uma identificação completa foi definido.
- Nenhuma classe foi avaliada numericamente.
