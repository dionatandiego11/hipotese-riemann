# Etapa 11.6 — controle aritmético: autovalores de Maass de PSL(2,ℤ), setor ímpar — declaração prévia (19/09/2026)

Gravada **antes** de qualquer código deste controle, do cálculo do catálogo geométrico G1 e de qualquer aplicação do
instrumento aos autovalores de Maass. Os dados do LMFDB já foram obtidos, mas só foram conferidos quanto a formato,
contagem, paridade e licença (§13 das pendências de fontes); nenhuma transformada foi calculada.
SHA-256 em `DECLARACAO_MAASS.sha256`. Nenhum artefato de m3/m4, lock ou certificado é alterado. Nenhuma afirmação sobre RH.

**Identificador do protocolo:** `ctrl-maass-v1` (item B2 da 11.6).

## 1. Pergunta e papel no projeto

Os três controles se completam:
- **Dirichlet:** mesma aritmética de ζ, com pesos trocados;
- **estádio:** dinâmica caótica **sem** aritmética;
- **este controle:** um sistema **aritmético de outra natureza**, o triângulo modular com condição de Dirichlet. Nele a
  fórmula de traço é **exata** (tipo Selberg), e as linhas ficam nos comprimentos de geodésicas l = 2 arccosh(n/2) e
  2 arcsinh(n/2), com n inteiro e multiplicidades aritméticas. Esses comprimentos **não** são log de inteiros (K5b,
  fato 1).

As perguntas são:
1. O instrumento encontra as linhas geométricas?
2. Ele mede os **sinais** previstos, negativos para órbitas com número ímpar de reflexões?
3. Ele deixa de ver linhas em log p e em 2 log n, onde este sistema não as tem?

## 2. Dados (fixados)

- **Arquivo:** `Mass-Forms/lmfdb_maass_rigor_0919_1121.txt` (SHA-256 `f4ca1d21…`, 283.876 bytes), obtido do LMFDB
  (https://www.lmfdb.org/ModularForm/GL2/Q/Maass/?level=1) em 19/09/2026. Contém 2.202 formas de nível 1, peso 0 e
  caractere trivial, com R de 9,5337 a 184,9240, com 93 ou mais dígitos.
- **Licença:** CC BY-SA 4.0 (§13). A decisão de versionar o arquivo é do usuário; o protocolo usa o arquivo pelo hash.
- **Completude (fonte lida em 19/09/2026):** página "Reliability of Maass form data" do LMFDB (SHA-256 `bc338566…`):
  "rigorous Maass forms are proven to be consecutive, i.e. there are no 'missing' Maass forms with eigenvalues between
  known rigorous Maass forms". O nome do arquivo e a consulta indicam formas rigorosas. **Conferência B antes do uso:**
  todas as 2.202 linhas têm nível 1, os R são estritamente crescentes e sem repetição, e o primeiro R ímpar é 9,5337. Não
  se usa nenhuma afirmação de completude acima de R = 184,924.
- **Paridade:** código 1 = ímpar, 0 = par, conferido em três páginas do LMFDB (§13).

## 3. Setor e faixa

- **Setor primário: ímpar** (1.092 formas), isto é, o triângulo modular com **Dirichlet** na fronteira (BLS 1996,
  arXiv:chao-dyn/9509019, p. 10: "odd and even … correspond to … Neumann and Dirichlet conditions on the boundary of the
  fundamental domain").
  - **Motivo:** o setor ímpar não tem espectro contínuo. As séries de Eisenstein são pares em x ↦ −x, porque
    E(z, s) = Σ_{(c,d)=1} y^s/|cz + d|^{2s} é invariante pela troca (c, d) ↦ (−c, d), que dá o conjugado da reflexão
    (argumento elementar). Pela fonte de M1 de K5b (Iwaniec, p. 6), o espectro contínuo vem das séries de Eisenstein.
    Logo, no setor ímpar **não há termo de espalhamento** e, portanto, nenhuma linha em ±2 log n (K5b, fato 2).
  - **Setor par:** só descritivo, porque tem o termo de espalhamento com ζ.
- **Faixa:** todas as formas ímpares do arquivo, R ∈ [9,5337; 184,924].
  - **Bloco primário H:** as 1.092 formas, com FWHM ≈ 4π/175 ≈ 0,072.
  - **Replicação descritiva:** as metades h1 (546 primeiras) e h2 (546 últimas).

## 4. Previsão congelada

**Fontes lidas:**
- BLS §2, eqs. (2.9) e (2.12), pp. 7–8: fórmula de Selberg e densidade oscilante;
- BLS §6, eqs. (6.2)–(6.5), pp. 33–34: bilhar modular, matrizes com det = ±1, comprimento 2 sinh(l/2) = |Tr M| para
  det = −1, sinal − para número ímpar de reflexões com Dirichlet, e área π/6;
- BK SIAM p. 241, eq. (2.9): amplitude 1/√|det(M_p − I)|; "exact" no caso de Selberg;
- Iwaniec, p. 9: lei de Weyl.

**P1 (posições).** Linhas nos comprimentos das órbitas periódicas do bilhar modular, uma para cada classe de conjugação
de PGL(2,ℤ) (matrizes inteiras com det = δ = ±1, módulo ±1) com traço |n|:
- δ = +1, n ≥ 3: l = 2 arccosh(n/2);
- δ = −1, n ≥ 1: l = 2 arcsinh(n/2).

Elementos elípticos, parabólicos e reflexões (traço 0, det −1) entram nos termos de "corner and horn" (BLS p. 7).
Esses termos dão contribuição suave, sem linhas em t > 0; é uma suposição registrada, que o relatório confere
descritivamente.

**P2 (coeficientes, na convenção do instrumento).** Pela mesma conta da §2.2(b) de ETAPA11_3B_FORMULA_EXPLICITA (e da D1
do Dirichlet), um termo A·g(l) da fórmula de traço vira a linha de coeficiente c = A/π. Com BLS (2.9):

- **δ = +1:** c = +L_p/(2π sinh(l/2)), em que L_p é o comprimento da órbita primitiva e o sinal é + (número par de
  reflexões);
- **δ = −1 (Dirichlet):** c = −L_p/(2π S(l/2)), com duas hipóteses para S, fixadas agora:
  - **H_cosh:** S = cosh. Derivada de BK (2.9): a monodromia de uma reflexão com deslizamento tem autovalores −e^{±l},
    e |det(M − I)| = 4cosh²(l/2). A derivação vai por escrito em D1-M;
  - **H_sinh:** S = sinh, a leitura literal de BLS p. 34 ("looks like the usual trace formula").
- **Linhas com o mesmo l:** os coeficientes das classes somam.
- **Potências:** uma classe que é k-ésima potência de uma classe primitiva contribui com L_p da primitiva. Exemplo que
  a declaração já fixa: o quadrado da classe δ = −1, n = 1 (l = 0,9624) tem δ = +1 e traço 3 (l = 1,9248).

**P3 (catálogo G1, a calcular depois desta declaração).** Para n ≤ 13 (todo l ≤ 5,1):
- cada classe de PGL(2,ℤ) com (n, δ) corresponde a uma forma quadrática binária (A, B, C) = (c, d − a, −b) de
  discriminante D = n² − 4δ;
- as classes são as de equivalência própria de **todas** as formas de discriminante D, primitivas ou não, identificadas
  pela involução ι(A, B, C) = (−A, B, −C), que é a conjugação por diag(1, −1);
- **dois algoritmos independentes**, que precisam concordar em todas as contagens: (a) ciclos de formas reduzidas de
  Gauss; (b) componentes conexas pelos geradores S e T numa caixa grande de coeficientes;
- a raiz primitiva de cada classe se obtém por divisão do conteúdo pela Chebyshev U_{k−1}(n₀, δ₀);
- G1 é gravado com hash **antes** de qualquer transformada dos dados.

**P4 (ausências).** Não há linha prevista em t = log p (catálogo de ζ) nem em t = 2 log n (espalhamento, ausente no setor
ímpar). Nenhum desses valores coincide com um comprimento de P1: e^l é irracional nos dois casos, porque n² ∓ 4 não é
quadrado perfeito para os n considerados.

**D1-M (derivação a escrever antes do código):**
1. conferir, a partir de BLS (2.9) e (2.12), a normalização c = A/π na variável R, com a densidade em R;
2. escrever a derivação de H_cosh;
3. fixar a janela de ajuste da densidade suave (§5).

Se a derivação contradisser P2, prevalece a derivação, com adendo antes de qualquer cálculo.

## 5. Instrumento e critérios

**Instrumento:** o de m4-v3 (Hann, t ∈ [0,5; 5], estimador primário `band_conjugate`, detector sem catálogo), com os
parâmetros numéricos de `configs/m4_v3.toml`, exceto:
- **variável:** R;
- **densidade suave:** d̄(R) = dN̄/dR, com N̄(R) = R²/24 + βR log R + γR + δ₀. O coeficiente R²/24 é fixo, pela área π/6
  (BLS p. 34) e pela forma de Weyl de Iwaniec p. 9. β, γ e δ₀ são ajustados por mínimos quadrados à função escada do
  bloco. Um ajuste suave de três parâmetros não produz linhas;
- **catálogo:** G1;
- **modelos nulos:** shuffle (como em m4-v3) e **Poisson** no lugar do GUE. A estatística local do triângulo modular com
  Dirichlet é próxima de Poisson (Bogomolny, notas de 2003, p. 68; rótulo D, fato empírico);
- **semente:** 20260922;
- **erro de tabela declarado:** 10⁻²⁰ (desprezível).

**Critérios (bloco H):**

| Código | Critério | Passa se |
|---|---|---|
| **M-C1** | detecção sem catálogo | recuperação ≥ 0,9 das linhas de G1 "claramente detectáveis" (margem 1,5 sobre o limite de detecção, calculada com a **menor** amplitude entre H_cosh e H_sinh) **e** no máximo 10% das detecções claras sem correspondência em G1 |
| **M-C2s** | sinal | Re Ĉ tem o sinal previsto (+ para δ = +1, − para δ = −1) em **todas** as linhas elegíveis (regra de elegibilidade de m4-v3) sem coincidência de classes com sinais opostos a menos de 1 FWHM |
| **M-C2a+** | amplitude, δ = +1 (Selberg, exata) | \|Re Ĉ − c\| ≤ 3σ_c em ≥ 90% das linhas elegíveis δ = +1, com σ_c = 2·ruído_rms/W(0) (a fórmula de `detection_limit_coefficient` com z = 1) |
| **M-C4** | ausência de ζ | entre as linhas t = log n (catálogo de ζ, n ≤ 148) a mais de 1 FWHM de qualquer l de G1, fração com detecção clara ≤ 0,05 |
| **M-C4s** | ausência de espalhamento | idem para t = 2 log n |
| M-C2a− | amplitude, δ = −1 | **só descritivo:** registra \|Re Ĉ/c − 1\| sob H_cosh e sob H_sinh, e qual fica mais perto de 1. Não decide o controle |
| M-C3 | estatística local | só descritivo (Poisson contra GOE; rótulo D) |

**Resultado do controle:** "passa" se M-C1, M-C2s, M-C2a+, M-C4 e M-C4s passam no bloco H. As metades h1 e h2 e o setor
par são reportados sem critério.

## 6. Regras de leitura fixadas agora

1. **Passa:** o instrumento distingue um espectro aritmético não ligado a ζ, com posições, sinais e amplitudes exatas, e
   não vê primos onde não há. Não diz nada sobre RH e não muda K5b M4 (P), que trata de igualdade com a fórmula explícita.
2. **Falha com dados conferidos:** resultado negativo registrado, sem reajustar nada. Uma nova execução exige adendo com a
   causa identificada.
3. **Só M-C2a+ falha:** registrar como limitação (bloco pequeno ou σ_c subestimado), sem trocar a tolerância.
4. O resultado de M-C2a− é uma **medida** de qual normalização vale para as órbitas δ = −1. Ele só vira afirmação depois
   de conferido com uma fonte (Venkov; Bogomolny–Georgeot–Giannoni–Schmit 1997; Hejhal), que ainda não foi lida.

## 7. Ordem de execução

1. D1-M (derivação escrita, com hash).
2. Catálogo G1 (código, dois algoritmos, testes; arquivo com hash).
3. Código do instrumento para R e testes (inclusive um teste sintético com linhas de sinais conhecidos sobre fundo de
   Poisson).
4. Conferência B dos dados (§2) e execução nos blocos H, h1 e h2; relatório.

Tudo o que for longo é entregue ao usuário para rodar. O custo aqui é pequeno, com 1.092 níveis.
