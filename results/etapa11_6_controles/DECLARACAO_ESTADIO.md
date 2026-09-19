# Etapa 11.6 — controle dinâmico: níveis do quarto de estádio (setor ímpar-ímpar) — declaração prévia (19/09/2026)

Gravada **antes** de qualquer código do controle, busca de órbitas, cálculo de níveis além do teste de funcionamento de
k = 100 (§14 de [ETAPA11_PENDENCIAS_FONTES.md](../../docs/ETAPA11_PENDENCIAS_FONTES.md)) e execução do instrumento.
SHA-256 em `DECLARACAO_ESTADIO.sha256`. Nenhum artefato de m3/m4, lock ou certificado é alterado. Nenhuma afirmação
sobre RH.

**Identificador do protocolo:** `ctrl-estadio-v1` (item B1 da 11.6).

## 1. Pergunta e papel no projeto

Nos zeros de ζ, o instrumento congelado (cadeia m4-v3) recupera linhas em t = log n com pesos aritméticos conhecidos.
Este controle aplica o **mesmo instrumento** aos níveis de um sistema dinâmico caótico, **sem aritmética**, cuja
resposta é conhecida por outra via: as linhas devem aparecer nos **comprimentos das órbitas periódicas** do bilhar, e
**não** em log p. As perguntas são:
1. O instrumento encontra, sem catálogo, as linhas previstas pela dinâmica clássica?
2. A amplitude da linha mais forte, a da família de órbitas "bouncing ball", bate com a previsão?
3. O instrumento deixa de "ver primos" quando eles não estão lá?

Diferenças em relação a ζ, fixadas agora:
- a fórmula de traço dos bilhares é **assintótica**, não uma igualdade exata;
- as amplitudes das órbitas isoladas dependem de monodromia e de índices de Maslov;
- a classe de simetria é **GOE**, porque há reversão temporal, e não GUE.

Por isso, as tolerâncias são mais largas que as de ζ e são **convenções fixadas a priori**, não cotas demonstradas.

## 2. Sistema (fixado)

- **Bilhar:** estádio de Bunimovich com raio r = 1 e trecho reto de comprimento total 2, ou seja, o estádio "2×4" do
  pacote `vergini` (`-l qust:2`). No código, `alpha` é o comprimento total do trecho reto e o quarto tem trecho reto
  a = alpha/2 = 1. Conferido em `billiard.cc`: o perímetro externo é (π + alpha)/2 (linhas 32–34), a área é
  (π + 2·alpha)/4 (linhas 119–121) e o centro do arco fica em x = alpha/2 (linha 398). O teste de k = 100 imprimiu área
  1,7854 e perímetro externo 2,5708, os valores para alpha = 2.
- **Domínio de cálculo:** o quarto de estádio 0 ≤ x, 0 ≤ y, formado pelo retângulo [0, 1] × [0, 1] unido ao quarto de
  disco de centro (1, 0) e raio 1.
- **Setor:** **ímpar-ímpar**, com Dirichlet nos dois eixos de simetria e na fronteira externa, portanto Dirichlet em todo
  o contorno do quarto. É o setor da base `vepwoo` do `vergini`; os outros três setores ficam fora deste protocolo.
- **Constantes geométricas:**
  - área A = 1 + π/4 ≈ 1,785398;
  - comprimento de Dirichlet L = 4 + π/2 ≈ 5,570796, somando os eixos 2 + 1, o reto externo 1 e o arco π/2;
  - não há fronteira de Neumann.
- **Variável espectral:** k = √E (autofrequência), em que −Δψ = k²ψ.

**Fatos usados (fontes lidas; arquivos no manifesto):**
- **Bäcker, arXiv:nlin/0204061v1:**
  - p. 18: o estádio é "hyperbolic, ergodic, mixing and K-system";
  - p. 22, eq. (49), fórmula de Weyl generalizada: N̄(E) = (A/4π)E − (L/4π)√E + C + ⋯, com L = L₋ − L₊ e C trazendo
    correções de curvatura e cantos;
  - p. 23, eqs. (50)–(53): estatística δ_n para completude e contribuição das órbitas "bouncing ball";
  - p. 26, eq. (73): dessimetrização Dirichlet-Dirichlet nos dois eixos.
- **Berry & Keating 1999, SIAM Rev. 41, p. 241, eq. (2.9):** fórmula de Gutzwiller para N_fl, com o símbolo "∼"
  (assintótica; exata só no caso de Selberg).
- **Ullmo, Scholarpedia 11(9):31721 (conjectura BGS):** o enunciado original, para sistemas com reversão temporal cujo
  análogo clássico é um K-sistema, leva a GOE. Rótulo **D** (conjectura).
- **Pankrashkin, notas de 2020:** o laplaciano de Dirichlet em domínio limitado tem espectro discreto (E-K7-M1).

O valor da literatura C = 11/48, somando curvatura 1/24 e três cantos retos com 1/16 cada, **não** foi conferido em
fonte lida (Balian–Bloch 1972 não foi lido) e **não é usado**. Tudo neste protocolo usa diferenças de N̄, em que C se
cancela, ou densidades, em que C não aparece.

## 3. Predição congelada

**P1 (família "bouncing ball").** Órbitas perpendiculares aos dois lados paralelos, com y indo de 0 a 1 e voltando, para
x ∈ (0, 1). O comprimento da m-ésima repetição é L_m = 2m. A contribuição para a função escada é a eq. (52) de Bäcker,
com a = 1 e E_n^bb = π²n²:

N_fl^bb(E) = (a/π) Σ_{n≥1} √(E − π²n²) Θ(√E − πn) − (a/4π)E + (a/2π)√E.

- **Divergência registrada na fonte:** o texto extraído da eq. (53) mostra a fase como cos(2an√E − 3π/4). Uma soma de
  Poisson direta da eq. (52) com caixa de comprimento 1 dá fase 2n√E, sem o fator a. Com a = 1 as duas coincidem, então
  a divergência não afeta este protocolo. A derivação D1-E (abaixo) fixa a forma usada.
- **Linhas usadas quantitativamente:** só **m = 1** (L = 2). A linha m = 2 (L = 4) coincide com o comprimento da órbita
  de fronteira ao longo do eixo x (ida e volta entre x = 0 e x = a + r = 2, comprimento 4). Por isso fica **excluída**
  dos critérios quantitativos e entra só como descritiva.

**P2 (órbitas isoladas).** Os comprimentos das órbitas periódicas do quarto de estádio com L ≤ 5,5 formam o catálogo O1.
O quarto de estádio tem reflexão especular nos quatro trechos de fronteira, e as órbitas de fronteira ao longo dos eixos
entram no catálogo com essa marcação. O1 é calculado por um procedimento declarado:
- busca por sequências de reflexões até 8 colisões;
- refinamento de Newton dos pontos de colisão;
- eliminação de repetições e de órbitas não primitivas;
- conferência de que as reflexões são especulares até 10⁻¹².

O1 é gravado com hash **antes** de qualquer nível ser calculado. As amplitudes de Gutzwiller (monodromia e Maslov)
entram só como **descritivas**, porque a fórmula é assintótica (BK p. 241) e K7 M4 não está conferida.

**P3 (densidade suave).** d̄(k) = dN̄/dk = A k/(2π) − L/(4π), obtida da eq. (49) com E = k². Ocupa a posição de
`density = "rvm"` em m4-v3, com k no lugar de E.

**P4 (ausência de aritmética).** Nenhuma linha é prevista em t = log n, a não ser por coincidência com um comprimento de
O1 ∪ {2m}.

**D1-E (derivação a escrever antes do código).** Em documento próprio, com hash e antes de qualquer código:
1. a tradução do modelo de linhas da §2.2(b) de
   [ETAPA11_3B_FORMULA_EXPLICITA.md](../../docs/ETAPA11_3B_FORMULA_EXPLICITA.md) para a variável k, com a convenção de
   Fourier e o fator de simetrização;
2. a amplitude complexa prevista C_bb(k) da linha L = 2, em que o módulo cresce com √k e a fase é fixa;
3. a média dessa amplitude com o peso da janela de Hann em cada bloco, que é o valor que o estimador `band_conjugate`
   deve recuperar;
4. a verificação da soma de Poisson citada em P1.

Se a derivação contradisser P1–P3, prevalece a derivação, e a divergência é registrada como adendo antes de qualquer
cálculo de níveis.

## 4. Dados: cálculo próprio dos níveis

**Código:** `vergini` de A. Barnett. É o arquivo `vergini.tar.gz` com SHA-256
`1da91d3b44fc48f26bb6a5cdc3d4075dda39de9cee1caed04aa4b4ce7a002048`, obtido de
https://users.flatironinstitute.org/~ahb/software/, com licença não declarada. **Não entra no repositório**; registram-se
só a URL e o hash. A compilação é feita pelo usuário com o Makefile original (`linux-gnu-openmp`).

**Chamada padrão (parâmetros do exemplo do README para o quarto de estádio, sem saída de autofunções):**

```
verg -l qust:2 -s vepwoo:1.3:10:1.5 -u -4 5 -b 10 -k K0 -V 0.2 -o <cabeçalho>
```

**Janelas e junção:**
- centros K0 = 85,2 + 0,2·j, para j = 0, 1, 2, …, até cobrir 304,1;
- de cada janela [K0 − 0,2, K0 + 0,2] aproveita-se **só** o miolo [K0 − 0,1, K0 + 0,1), de modo que os miolos formam
  uma partição de [85,1; 304,1+);
- se níveis de miolos adjacentes ficarem a menos de 10⁻³ um do outro, são contados como o mesmo nível e fica o de menor
  tension.

**Blocos (fixados agora pela contagem de Weyl sem C):** N̄₀(k) = A k²/(4π) − L k/(4π). As bordas são os k em que
N̄₀ = 1.000, 4.000, 7.000, 10.000 e 13.000:

| Bloco | Faixa de k | Níveis esperados | Espaçamento médio no fim |
|---|---|---|---|
| g01 | [85,4699; 169,3579) | 3.000 | 0,0210 |
| g02 | [169,3579; 223,5316) | 3.000 | 0,0159 |
| g03 | [223,5316; 266,8648) | 3.000 | 0,0133 |
| g04 | [266,8648; 304,0528) | 3.000 | 0,0116 |

**Aceitação de cada nível:** tension ≤ **10⁻⁶**. Um nível acima do limite é recalculado numa janela centrada nele
(K0 = k do nível). Se continuar acima, o nível é mantido com marcação e conta como falha de E3.

**Meta de precisão:** |k̂ − k| ≤ 10⁻³. Para L ≤ 5, isso é um erro de fase kL de no máximo 5·10⁻³ rad.

**Verificações de dados (classe B, obrigatórias antes de usar os blocos):**
- **E1 completude:**
  - em cada bloco, |n_encontrado − 3.000| ≤ 3. É uma diferença de N̄, portanto C se cancela; a tolerância 3 é
    convenção de conferência, não cota demonstrada;
  - além disso, δ_n − N_fl^bb(k_n²), com δ_n da eq. (50) de Bäcker, calculado com N̄₀ e com C estimado como a média do
    próprio bloco (um único parâmetro), não pode ter degrau: a média móvel em 200 níveis consecutivos deve variar menos
    de 0,5 ao longo do bloco. Um nível faltando ou sobrando produz degrau de 1 (Bäcker p. 23, fig. 14).
- **E2 convergência:** antes da execução completa, rodar 5 janelas consecutivas em torno de K0 = 100, 200 e 300 com a
  chamada padrão e com uma chamada refinada (`-s vepwoo:1.6:14:1.5 -b 15`). Passa se o número de níveis nos miolos for
  igual e se max|Δk| ≤ 10⁻³.
- **E3 tension:** todos os níveis aceitos têm tension ≤ 10⁻⁶.
- **E4 setor:** garantido pela base ímpar-ímpar. Registrar a versão e a chamada no manifesto; não há teste numérico
  adicional.
- **Piloto de custo:** junto com E2, medir o tempo por janela em k = 100, 200 e 300 e registrar a estimativa do custo
  total (cerca de 1.100 janelas) antes da execução completa.

Falha em E1–E3 significa que os dados não são usados e nenhuma conclusão sobre o instrumento é tirada.

**Formato de saída:** um arquivo com uma autofrequência k por linha e 9 casas decimais, mais um manifesto com SHA-256,
versões, chamadas, tempos e contagem por bloco. O arquivo de tension e a janela de origem de cada nível vão num CSV à
parte. Os níveis são cálculo próprio e podem ser versionados.

## 5. Instrumento e critérios

**Instrumento:** o de m4-v3, com os mesmos parâmetros numéricos de `configs/m4_v3.toml`:
- janela de Hann;
- t ∈ [0,5; 5], em que t agora é um comprimento de órbita;
- estimador primário `band_conjugate`;
- detector sem catálogo.

Mudanças em relação a m4-v3, todas num caminho novo, sem editar o código congelado nem os locks:
- **variável:** k em vez de E, com a densidade P3;
- **catálogo:** {2m} ∪ O1 no lugar de {log n}, e o catálogo de ζ {log n} usado só em E-C4;
- **modelo nulo de matriz aleatória:** GOE (β = 1) no lugar de GUE, gerado pelo mesmo desenho do gerador tridiagonal,
  com β = 1; o nulo shuffle continua;
- **semente:** 20260921;
- **erro de tabela declarado:** `declared_table_error` = 10⁻³ (meta do §4);
- **blocos:** g01–g04.

**Critérios:**

| Código | Critério | Passa se |
|---|---|---|
| **E-C1** | detecção sem catálogo da linha "bouncing ball" L = 2 | detecção clara, pela regra de m4-v3, correspondida a L = 2 em **todos** os 4 blocos |
| **E-C1o** | detecções claras sem catálogo em t ∈ [0,5; 5] | no máximo 2 blocos com alguma detecção clara que não corresponde a nenhum comprimento de O1 ∪ {2, 4}, com a tolerância de correspondência de m4-v3 |
| **E-C2bb** | amplitude da linha L = 2 | \|Ĉ/C̄_bb − 1\| ≤ **0,10** (razão complexa) em cada bloco, com C̄_bb a média na janela de D1-E; 0,10 é convenção a priori |
| **E-C4** | ausência de primos | entre as linhas t = log n do catálogo de ζ que distam mais de 1 FWHM de qualquer comprimento de O1 ∪ {2m}, a fração com detecção clara é ≤ **0,05** em cada bloco |
| E-C2o | amplitudes das órbitas isoladas contra Gutzwiller (BK eq. 2.9) | **só descritivo** (fórmula assintótica; K7 M4 é PC) |
| E-C3 | estatística local (GOE contra GUE) | **só descritivo** (BGS é conjectura, rótulo D) |
| — | linha L = 4 | **só descritiva** (coincidência de P1 com a órbita de fronteira) |

**Resultado do controle:** "passa" se E-C1, E-C1o, E-C2bb e E-C4 passam.

## 6. Regras de leitura fixadas agora

1. **Passa:** o instrumento recupera linhas de um sistema sem aritmética nos lugares que a dinâmica prevê e não inventa
   linhas em log p. Isso não diz nada sobre RH, não decide K7 M4 e não valida o certificado da 11.3b.
2. **Falha com dados aprovados em E1–E3:** resultado negativo registrado. Nenhum parâmetro é reajustado. Uma nova execução
   exige adendo com a causa identificada, escrito antes de rodar.
3. **Falha só em E-C2bb com E-C1 aprovado:** registrar como limitação da previsão assintótica ou do estimador. A
   tolerância não é trocada a posteriori.
4. **Falha só em E-C1o:** as detecções sem correspondência são listadas. Candidatas naturais são as órbitas de difração
   na junção reta–arco, onde a curvatura é descontínua, ou órbitas acima de 8 colisões. Isso é registrado, **sem**
   ampliar O1 depois de ver os dados.
5. O relatório põe lado a lado este controle, K12 e ctrl-dirichlet-v1.

## 7. Ordem de execução e responsabilidades

1. D1-E (derivação escrita, com hash).
2. Catálogo O1 (código de busca de órbitas, testes e arquivo com hash), sem nenhum nível calculado.
3. Código novo do instrumento para bilhares e testes sem rede, incluindo um teste sintético com uma linha de amplitude
   conhecida em L = 2 sobre um fundo GOE.
4. E2 (convergência) e piloto de custo, executados pelo usuário; registro.
5. Cálculo dos níveis em k ∈ [85,1; 304,1+), executado pelo usuário; E1–E4.
6. Execução do instrumento nos 4 blocos e relatório.

Os comandos de cálculo e execução são entregues ao usuário, que decide quando rodar. Nenhuma etapa começa sem a anterior
registrada. A compilação e a execução do `vergini` são sempre feitas pelo usuário.
