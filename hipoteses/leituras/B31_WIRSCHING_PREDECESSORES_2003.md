# B31 — Wirsching: densidade positiva de predecessores

Leitura: 12/10/2026. Referência publicada: G. J. Wirsching, *On the problem of positive predecessor density in 3n+1 dynamics*, DCDS 9(3) (2003), 771–787, DOI 10.3934/dcds.2003.9.771.

**Cópia efetivamente lida:** `archive/fontes_etapa11/collatz_regularidade_20261012/wirsching_positive_predecessor_prelim_bielefeld.pdf`, 18 pp., título *On positive predecessor density in 3n+1 dynamics*, explicitamente “preliminary version”. Obtida em https://www.math.uni-bielefeld.de/baake/algdyn/posden.pdf. SHA-256 `c1fef3ffaa08fdea949ba927664f3b5fc2c0b146c515cceed465a395b2234bc5`. Data impressa não indicada. Metadados de composição não foram tratados como data de publicação.

O endpoint editorial devolveu zero bytes; uma URL antiga de PDF devolveu 404. A versão publicada não foi obtida. Não presumir identidade textual ou paginação com ela, nem com uma versão preliminar de 19 pp. descrita por outra fonte. Todas as páginas abaixo são desta cópia de 18 pp.; número impresso coincide com o PDF.

**Escopo:** lidas as sete seções, definições e conjecturas; a prova de convergência do Teorema 3 foi percorrida. Seus Teorema 6 e resultados anteriores remetem ao livro de 1998, que não foi obtido; leitura integral da cópia não é reconstrução independente de toda sua base. Eq. (5.1), Teorema 3 e Lema 4 na p. 11 conferidos visualmente.

## 1. Objetos e resultados

| Objeto | Página | Significado / hipóteses |
|---|---|---|
| Densidade positiva uniforme | 2, Def. 1 | Uma constante c>0, comum aos alvos admissíveis a, com liminf_X #predecessores≤X / X ≥ c/a. Exclui múltiplos de 3 e alvos cíclicos no alvo declarado. |
| e_ℓ(k,a) | 3–4 | Contagem de caminhos com ℓ passos ímpares e k pares, e não profundidade total fixa. Depende de a módulo 3^ℓ. |
| g_ℓ(k,a) | 7–8, (2.1) | Geradores de suporte finito, ligados a e_ℓ por convolução com contagens de partições p_ℓ. |
| Espaço X | 8–9 | I3 × Z3^×: I3 é o completamento digital de ternários, com projeção não injetiva em [0,1]; a variável a é uma unidade 3-ádica. |
| S_ℓ | 10, (4.2) | Sequência de operadores que gera as densidades normalizadas g̃_ℓ. |
| S∞ | 11, (5.1) | Integra a coordenada a em Haar nas unidades; o resultado independe dessa coordenada. |
| Teorema 3 | 11–13 | S_ℓ→S∞ fortemente em C(X), uniformemente em famílias limitadas e equicontínuas. Não é uma estimativa uniforme sobre todas as funções cuja resolução cresce com ℓ. |
| W3 | 13–14 | W3f(x)=(3/2)∫_{3x−2}^{3x} f(t)dt, com funções estendidas por zero. Age na variável real [0,1]. Preserva integrais; contrai por 1/2 em L1 para diferenças de mesma massa, conforme Teorema 6 citado do livro. |
| φ | 14 | Densidade real estacionária de W3; não é uma densidade em Z3 nem o limite de médias de Applegate–Lagarias. |

O crescimento de resolução reaparece no uso de g̃_ℓ, funções que registram dígitos em níveis crescentes. A equicontinuidade necessária ao Teorema 3 não foi demonstrada para essa família de entrada com os controles relativos que a conjectura exige. Isso é a lacuna, não uma contradição ao Teorema 3.

## 2. Cadeia e o que permanece conjectural nesta fonte

O artigo deixa três conjecturas explícitas:

- Conjectura 1, p. 8: a cota relativa dos geradores (⋆2) implica a cota relativa das funções e_ℓ (⋆1), suficiente para densidade positiva pelo Teorema 1.
- Conjectura 2, p. 14: a cota da razão (W3^ℓχ1)(x_ℓ)/(W3^ℓχ0)(x_ℓ) na janela Ã_δ implica a cota relativa dos geradores (⋆3). É a passagem do controle da coordenada real ao controle aritmético em a.
- Conjectura 3, p. 17: φ(z_ℓ)/φ0(z_ℓ) converge para uma constante positiva uniformemente na classe de sequências Ã_δ5. Não é a afirmação irrestrita φ(t)~cφ0(t) para todo t→0.

A classe relevante tem k_ℓ próximo de ℓ por O(√ℓ), com k_ℓ=⌊3^ℓx_ℓ⌋. Constantes e quantificadores em a devem ser explicitados antes de usar o programa. Na transcrição, a ocorre livre em algumas condições; não atribuir ao original uma ordem de quantificadores que ele não imprime.

O próprio texto ressalva, p. 2, que o alvo de densidade positiva não fornece, por si só, a conjectura de convergência de Collatz.

## 3. Comparação com nosso operador

Nosso A=(3/4)L+ e seu dual Q, sobre Z3, registram profundidade total m e produzem uma estacionária ν não uniforme em resíduos. Wirsching condiciona o número de passos ímpares ℓ e o custo k; seu S∞ elimina a variável a por integração e conserva uma densidade real φ. Não há identidade automática entre Q, S_ℓ, W3, ν e φ.

Assim a contração Hölder de Q e o fechamento de médias módulo 3^K que derivamos não encerram a Conjectura 2. Também não encerram a regularidade forte das densidades de Applegate–Lagarias. São três objetos que precisam de relações demonstradas.

## 4. Decisão

Fonte central para definir o alvo **conjunto de custo e resíduos**, além da profundidade total. O item prioritário é uma cota relativa em resolução crescente para g_ℓ(k,a), com a janela e os quantificadores declarados. Antes de qualquer piloto, comparar com Tavares v1, que afirma resolver as Conjecturas 1 e 3 e preserva essa lacuna.

Rótulos: A para resultados enunciados na fonte com suas hipóteses e dependências; D para suas conjecturas. Não reivindicamos novidade nem declaramos o estado atual completo do programa apenas pela fonte de 2003.
