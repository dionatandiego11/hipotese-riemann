# Anexo — diagnóstico da reprovação de V1 e V2 em χ₋₄ (22/09/2026)

Anexo citado no [ADENDO_DIRICHLET_3.md](../../ADENDO_DIRICHLET_3.md) (`02340a5c…`), §0.3. **Este diagnóstico foi
executado antes do adendo**, entre 21:45 e 22:15 de 22/09/2026, com um script fora do repositório (pasta temporária da
sessão), sobre a lista reprovada `dados/zeros_chi_m4_12000.txt` (SHA-256 `698e7dba…`). Ele não alterou nenhum arquivo,
nenhum critério e nenhum parâmetro; serviu só para achar a causa e dimensionar o passe de completude.

## 1. O que a V1 mostra

S(n) = n − θ_χ(γ_n)/π sobre a lista reprovada. A mediana de S em janelas de 200 zeros:

| início da janela | mediana de S |
|---|---|
|     0 |  +0.498 |
|  1000 |  +0.502 |
|  2000 |  +0.508 |
|  3000 |  +0.486 |
|  4000 |  +0.495 |
|  4200 |  -1.453 |
|  5000 |  -1.492 |
|  5400 |  -3.509 |
|  6000 |  -3.524 |
|  7000 |  -3.503 |
|  7400 |  -5.446 |
|  8000 |  -7.511 |
|  9000 | -11.518 |
| 10000 | -11.517 |
| 10200 | -13.380 |
| 11000 | -13.506 |

A curva não deriva: são platôs planos (variação interna medida < 0,05) com **degraus de exatamente −2**. O valor de
partida, +0,50, é a constante de convenção S(0, χ) da declaração, não um erro.

## 2. Reexame dos 20 maiores intervalos (passo d̄/32)

Método: para cada um dos 20 maiores intervalos entre zeros consecutivos, varredura em (γ_i + 10⁻⁹, γ_{i+1} − 10⁻⁹)
com o `ZeroFinder` do script congelado (`65056bc2…`), `step_scale = 0,25`, isto é, passo d̄/32 — quatro vezes mais fino
que o da produção.

**Com par escondido (7 intervalos, 14 zeros):**

| índice | intervalo | s/d̄ | zeros encontrados | separação |
|---|---|---|---|---|
| 4223 | 3893.1962 – 3895.0981 | 2.366 | 3893.887460453 / 3893.977078497 | 0.0896 |
| 5354 | 4791.2944 – 4793.3374 | 2.609 | 4792.399221931 / 4792.482772594 | 0.0836 |
| 7434 | 6391.8883 – 6393.8248 | 2.561 | 6392.876192802 / 6392.936474859 | 0.0603 |
| 7955 | 6785.6489 – 6787.6734 | 2.697 | 6786.913692583 / 6786.966386183 | 0.0527 |
| 8929 | 7513.6447 – 7516.1784 | 3.417 | 7514.668864274 / 7514.735641828 | 0.0668 |
| 8998 | 7566.2417 – 7568.4122 | 2.929 | 7567.429286797 / 7567.453983401 | 0.0247 |
| 10256 | 8493.1291 – 8495.6223 | 3.411 | 8494.446640266 / 8494.514232087 | 0.0676 |

**Sem nenhum zero (13 intervalos):**

| índice | intervalo | s/d̄ |
|---|---|---|
| 2054 | 2083.5209 – 2085.4904 | 2.254 |
| 5826 | 5160.0609 – 5161.9028 | 2.374 |
| 6509 | 5687.0747 – 5688.8536 | 2.320 |
| 6576 | 5738.3280 – 5740.0466 | 2.244 |
| 7658 | 6561.7023 – 6563.4004 | 2.253 |
| 8427 | 7139.8093 – 7141.5162 | 2.288 |
| 8505 | 7198.0574 – 7199.7241 | 2.236 |
| 9534 | 7963.3032 – 7964.9754 | 2.270 |
| 10272 | 8506.0910 – 8507.7647 | 2.290 |
| 10555 | 8712.7217 – 8714.4748 | 2.405 |
| 10790 | 8883.7490 – 8885.3950 | 2.264 |
| 10963 | 9009.3978 – 9011.0454 | 2.269 |
| 11745 | 9575.1289 – 9576.7577 | 2.259 |

Os 14 zeros recuperados coincidem com os sete degraus da §1, um par por degrau, e fecham o déficit de 14 que a
V1 acusava. O tamanho do intervalo, sozinho, **não** separa os dois grupos: há intervalos de 2,374 d̄ e 2,405 d̄ sem par
e um de 2,366 d̄ com par.

## 3. O mecanismo

Em cada caso a separação do par é menor que o passo da varredura de produção (d̄/8) naquela altura:

| índice | separação do par | passo d̄/8 local | separação < passo? |
|---|---|---|---|
| 4223 | 0.0896 | 0.1005 | sim |
| 5354 | 0.0836 | 0.0979 | sim |
| 7434 | 0.0603 | 0.0945 | sim |
| 7955 | 0.0527 | 0.0938 | sim |
| 8929 | 0.0668 | 0.0927 | sim |
| 8998 | 0.0247 | 0.0926 | sim |
| 10256 | 0.0676 | 0.0914 | sim |

Z_χ troca de sinal duas vezes entre dois pontos amostrados consecutivos; a varredura por troca de sinal vê os dois
extremos com o mesmo sinal e não registra nada. Perda sempre **par**, o que explica os degraus de −2 e a impossibilidade
de degrau ímpar.

## 4. Descartes

- **Ramo de θ_χ:** `Im loggamma(1 + it/2)` comparado com a série de Stirling (termos até 1/(360 z³)) em 19 pontos,
  incluindo os dois lados de cada degrau: diferença ≤ 3·10⁻²⁰ em todos. Não há salto de 2π.
- **Refinamento:** o manifesto registra `bisection_fallbacks: 0` e `max_refine_iterations: 27`, ou seja, nenhum zero foi
  aceito no limite de iterações; V3 (segunda avaliação com `mpmath.dirichlet` a 40 e 60 dígitos) e V4 (realidade de Z nos
  pontos médios) passaram. Os zeros da lista estão certos um a um; o que falta é completude.
- **Rescan automático:** `ZeroFinder.rescan_large_gaps` só dispara acima de 4 d̄, e o maior buraco tem 3,42 d̄.

## 5. Consequência

O passe de completude D3, fixado no adendo, varre com passo d̄/32 todo intervalo acima de 1,6 d̄ — limiar bem abaixo do
menor intervalo com par (2.366 d̄) — e depois exige o certificado D3-C1 sobre a lista
corrigida. Rótulo **B**: reprodução numérica de um modo de falha conhecido de varredura por troca de sinal, sem
novidade científica.

*Gerado em 22/09/2026 22:13 a partir de `diag_gaps.json` (saída bruta do
diagnóstico, preservada na pasta da sessão).*
