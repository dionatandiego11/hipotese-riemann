# Reconstrução de Adriazola: arquitetura e dependências

Data: 24/11/2026. Fonte: Jimmie Adriazola, *The Alpöge proof of the Riemann hypothesis*, PDF de 287 páginas na revisão `aa9c86bf2a7d29b08575641fecea19a2a603e87c` do [repositório do autor](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/tree/aa9c86bf2a7d29b08575641fecea19a2a603e87c). A cópia e seus dados de proveniência estão em `archive/leituras/adriazola_20261124/`.

**Escopo da leitura:** mapeamento de todas as seções, leitura dirigida da introdução, do teorema de janelas na §2, das dependências nas §§11–15, da §17.4.3 e da montagem nas §§18.3 e 18.7. Não é leitura linha a linha nem verificação independente das 287 páginas, das fontes citadas ou do código Lean. Os enunciados abaixo descrevem o manuscrito; não são uma certificação matemática feita pelo projeto.

## Situação da reconstrução

O próprio autor afirma na introdução que sua reconstrução em linguagem matemática convencional está incompleta: a dedução depende de afirmações internas cujas provas convencionais ainda faltam, e parte das fontes citadas não foi cotejada linha a linha. Na p. 282 ele registra que a implicação final permanece condicional às hipóteses listadas. Na p. 277 observa que a Hipótese 18.10 não foi estabelecida no texto nem mesmo a partir de todas as hipóteses das seções anteriores, pois a compatibilidade exata das constantes e dos expoentes ainda não foi conferida linha a linha.

O artigo relata uma certificação do enunciado e da prova formal em Lean pela comunidade Lean/Mathlib. Isso é uma informação atribuída ao artigo, cuja verificação independente não foi realizada nesta leitura. A certificação relatada do desenvolvimento formal, a correspondência do enunciado formal com o enunciado matemático pretendido e a completude desta reconstrução escrita são questões distintas. Em particular, **não se pode inferir das lacunas do manuscrito uma falha do desenvolvimento formal**.

A §17.4.3, pp. 260–262, apresenta uma prova alternativa de uma estimativa de cohomologia; o texto afirma expressamente que essa alternativa não foi formalizada em Lean e aguarda verificação humana independente. Ela não deve ser confundida com a prova formal original.

## Mapa das seções

| Seção, página inicial | Papel na arquitetura relatada |
| --- | --- |
| 1, p. 4 | Contexto, arquitetura e limite da reconstrução. |
| 2, p. 7 | Critério analítico de janelas e somas de primos suavizadas. |
| 3, p. 11 | Contabilidade aritmética e sete desigualdades. |
| 4, p. 15 | Média de pesos e passagem a combinação positiva. |
| 5, p. 19 | Escolha de parâmetros e primos auxiliares; uniformidade. |
| 6, p. 41 | Enunciado aritmético A e redução à conclusão sobre funções L. |
| 7, p. 45 | Núcleos theta, modelo de Fock e covariância. |
| 8, p. 54 | Funções theta em primos inertes e grupo formal. |
| 9, p. 69 | Emparelhamentos e divisibilidade local. |
| 10, p. 78 | Composição dos passos ao longo de uma cadeia. |
| 11, p. 86 | Construção dos passos e normalizações; hipóteses N1–N3. |
| 12, p. 106 | Perdas e não degenerescência de operadores de Hecke. |
| 13, p. 146 | Reticulados, matrizes de Gram e desigualdade de inclinação. |
| 14, p. 158 | Séries de Bessel–Poincaré e quase ortogonalidade. |
| 15, p. 208 | Alturas, normas e inclinações arquimedianas. |
| 16, p. 240 | Termos locais e comparação de perdas. |
| 17, p. 247 | Lugares torcidos, limites de Selmer e congruências. |
| 18, p. 269 | Montagem, dados, limites de erro e hipóteses finais. |

## Dependências que merecem atenção

- A §2.3 enuncia um critério de janelas: para uma função com propriedades analíticas especificadas, uma cota superior uniforme em toda uma sequência de intervalos extensos, para escalas arbitrariamente grandes, pode excluir polos em certo semiplano. Não basta verificar alguns pontos nem um conjunto finito de dados.
- A Hipótese 12.12 reúne mecanismos de não degenerescência de Hecke; o texto afirma na §12.7 que os passos restantes não estão demonstrados ali.
- A Hipótese 14.61 reúne insumos de pré-traço expressamente identificados como não demonstrados no manuscrito.
- A Hipótese 15.69 trata de uma cota uniforme de inclinações em coberturas profundas; a §15.14.4 indica passos e limites ainda não escritos.
- A Hipótese 17.11 é uma cota de Selmer em janelas. A Proposição 17.22 relaciona essa hipótese a uma estimativa na direção de Vandiver; não se deve confundir esse resultado condicional com uma prova incondicional da conjectura de Vandiver.
- A Hipótese 18.10 agrega as estimativas da cadeia com constantes e expoentes absolutos; sua verificação precisa é um gargalo destacado pelo autor.

Essas observações são **relatos bibliográficos**, não uma auditoria das provas, nem uma classificação independente de cada resultado como estabelecido.

## Relação com o trabalho do projeto

1. **Riemann e Dirichlet.** A arquitetura considera famílias de caracteres e combinações positivas; as restrições são uniformes em janelas de escalas. Nossas simulações e espectros finitos podem testar implementações e comportamentos em regimes acessíveis, mas não substituem essas hipóteses assintóticas.
2. **Hamiltoniano.** As matrizes de Gram e a quase ortogonalidade da §13 sugerem estudar estabilidade e perda de informação numa família de operadores. Não há, nesta leitura, construção de um Hamiltoniano auto-adjunto com espectro dos zeros. Uma cota sobre traço ou norma de Hilbert–Schmidt não garante, por si, cota inferior uniforme do menor autovalor.
3. **Collatz.** A composição de passos e o controle uniforme das perdas são inspiração para examinar nossos operadores de ramos. É uma analogia metodológica: não foi identificada uma equivalência, uma função L de Collatz, nem uma ligação demonstrada com a hipótese de Riemann.

## Verificação separada necessária no trabalho local

No arquivo de trabalho `docs/LOOP_ESTUDO_IT3_CONEXAO_COLLATZ_RIEMANN_20261124.md`, a expressão exibida para Q tem denominador constante `1-e^{-s}` em todos os fatores. Para s > 0, cada fator tende a `1/(1-e^{-s}) > 1`, portanto o produto infinito como escrito diverge. É necessário rever a definição ou a normalização antes de usar essa fórmula como ponte matemática; a eventual soma logarítmica dos numeradores é outro objeto. Esta observação não decide o que acontece para uma definição corrigida. O arquivo preexistente foi preservado.

## Continuação sugerida

Auditar primeiro um elo preciso e limitado: explicitar os espaços e as hipóteses do argumento de Gram da §13.3, distinguir controle médio de limite espectral inferior e construir um exemplo finito que mostre a diferença. Só então formular uma versão própria para os operadores de Collatz, com condições que possam ser verificadas e sem atribuir ao artigo uma aplicação que ele não faz. Uma leitura completa linha a linha e a conferência das referências permanecem trabalho futuro.
