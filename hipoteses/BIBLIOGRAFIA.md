# Busca bibliográfica inicial — 19/09/2026

**Varredura dirigida, não revisão sistemática concluída.** Não se encontrou nesta sessão uma lacuna cuja originalidade esteja estabelecida. Foram consultadas fontes primárias e o levantamento anterior do projeto. Buscas retornaram também textos informais, que não foram usados como evidência matemática.

Estados: **L-parcial** = trechos do texto primário lidos; **R** = resumo primário; **M** = metadados; **PC** = conteúdo a conferir. Nenhum destes estados significa auditoria de uma prova inteira.

## Fontes e o que realmente foi lido

| ID | Fonte primária | Conferência nesta entrega | Consequência para a triagem |
|---|---|---|---|
| B1 | [Büthe, An analytic method for bounding ψ(x)](https://arxiv.org/abs/1511.02032) | Levantamento local de 17/09 consultado; artigo não relido nesta sessão | Já há métodos de fórmula explícita com cotas rigorosas; reler §3 e §6 antes de comparar originalidade com P-R1 |
| B2 | [Balanzario, Cárdenas Romero, Chacón Serna, A smooth version of Landau’s explicit formula](https://arxiv.org/html/2311.04347v1) | L-parcial: PDF pp. 1–2; HTML §1, Teoremas 1–2 e §2, Corolário 1 | Sob RH, o resumo dá ordem μ log^(3/2)μ para número de zeros; necessidade é conjectural. Não confundir com resolução Hann |
| B3 | [Bogomolny, Bohigas, Leboeuf, Monastra, On the spacing distribution of the Riemann zeros](https://arxiv.org/abs/math/0602270) | L-parcial: PDF pp. 1–2, resumo e introdução; restante não auditado aqui | Correções finitas de espaçamentos já estudadas. Não é descoberta do projeto e não cobre automaticamente o form factor |
| B4 | [Bernstein–Lagarias, The 3x+1 Conjugacy Map](https://websites.umich.edu/~lagarias/doc/bernstein.pdf) | L-parcial via ferramenta web: PDF pp. 1–3, §1; pp. 4–6, enunciados de conjecturas; download local falhou | Conjugação no espaço 2-ádico é conhecida; ciclos da conjugação e ciclos do mapa são objetos diferentes |
| B5 | [Monks–Yazinski, The autoconjugacy of the 3x+1 function](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf) | L-parcial: PDF pp. 1–3, definições e Teorema 2.1; provas não auditadas | Existe uma simetria explícita Ω=Φ∘V∘Φ⁻¹, V(x)=−1−x, que comuta com T e satisfaz Ω²=id; não apresentar busca genérica de simetrias como inédita |
| B6 | [Tao, Almost all orbits of the Collatz map attain almost bounded values](https://arxiv.org/abs/1909.03562) | L-parcial: PDF v7 pp. 1–3, resumo e definição de densidade logarítmica | Resultado para quase todas as órbitas nesse sentido; não prova que todas chegam a 1, nem fornece previsão para Fourier dos zeros |
| B7 | [Ruelle, Dynamical zeta functions and transfer operators](https://www.ihes.fr/~ruelle/PUBLICATIONS/137zeta.pdf) | Arquivo obtido; extração local ilegível, conteúdo técnico PC nesta entrega | Referência para CL4; não usar o arquivo baixado como prova conferida de uma identidade de operadores |
| B8 | [Lagarias, Li Coefficients for Automorphic L-Functions](https://arxiv.org/abs/math/0404394) | R: página de resumo, sem leitura da prova | Critérios de positividade já possuem literatura; não priorizar cálculo repetitivo sem pergunta adicional |
| B9 | [Benjamini–Yekutieli, The control of the false discovery rate in multiple testing under dependency](https://www.math.tau.ac.il/~ybenja/depApr27.pdf) | R: resumo do texto primário; hipóteses detalhadas a conferir | Dependência importa para FDR; não atribuir garantia geral a BH sem verificar suas condições |
| B10 | [Burungale e Tian, A proof of Sylvester's conjecture](https://arxiv.org/abs/2609.14893) (arXiv:2609.14893v2, 15/09/2026; cópia local `archive/fontes_etapa11/2609.14893v2.pdf`, SHA-256 `7b9d0801…`) | L-parcial: resumo, sumário e início da §1.1 (pp. 1–2); prova **não** auditada; preprint recente, sem revisão por pares conhecida | Só contexto: aritmética (pontos racionais de E_p: y² = x³ + p²/4) lida por um zero central da função L de grau 2 (posto analítico 1, Gross–Zagier). Sem relação com RH e sem uso em nenhuma afirmação do projeto. Motivou a proposta futura P-R5 |

Leitura complementar localizada: [Main et al., Harmonic inversion as a general method for periodic orbit quantization](https://arxiv.org/abs/chao-dyn/9709009), somente página de resumo. O sentido da inferência deve ser conferido antes de importar o método.

## Consultas desta rodada

1. `Collatz 2 adic conjugacy shift Bernstein Lagarias periodic points dynamical zeta`.
2. `Riemann zeros finite height corrections pair correlation Bogomolny Keating 2013`.
3. `recover Dirichlet character from zeros L function inverse spectral`.
4. `site.arxiv.org Lagarias Bernstein 3x+1 conjugacy map 1996`.
5. `site.arxiv.org Tao almost all orbits Collatz attain almost bounded values`.
6. `site.arxiv.org reconstruction L functions zeros Booker coefficients`.
7. `Dirichlet L functions inverse problem recovering character finite zeros explicit formula`.
8. `Collatz autoconjugacy symmetry Monks Yazinski 2004`.
9. `site.arxiv.org Riemann zeros harmonic inversion Main prime numbers`.
10. `site.arxiv.org Li criterion Riemann hypothesis numerical coefficients`.
11. `The 3x+1 Conjugacy Map fixed point conjecture solved`.
12. `Benjamini Yekutieli dependency false discovery rate 2001 pdf`.

As consultas inversas de Dirichlet não produziram, nesta leitura, uma referência suficientemente próxima para resolver a questão de prioridade. Isso é **pendência de busca**, não ausência de trabalho anterior. A busca por atualização das conjecturas de B4 também não decidiu seu estado atual.

## Arquivo e rastreabilidade

Downloads e falhas: `archive/fontes_etapa11/hipoteses_20260919/aquisicao.json`. Os arquivos obtidos têm hash SHA-256, tamanho e hora de aquisição; o manifesto geral recebe as entradas ainda ausentes. URLs do arXiv sem versão foram preservadas; versões lidas no cabeçalho: B2 v1, B3 v1, B6 v7. O cabeçalho de B3 contém também uma data de composição posterior; ela não substitui o identificador arXiv.

O arquivo `tao_collatz.pdf` é **slides de 15/04/2020**, não o artigo. O artigo é `tao_artigo.pdf`. B4 foi legível via web, mas as tentativas locais retornaram 403 no autor e 429 no editor; não há hash de PDF local para essa leitura. B5 é versão do autor com data 10/07/2002 no texto, associada à publicação de 2004; não presumir identidade byte a byte com a versão editorial.

## Antes de reivindicar novidade

- Ler os textos completos mais próximos de cada alvo; comparar pergunta, hipóteses, observável, faixa e resto, e não apenas título.
- Fazer busca para trás e para frente nas citações; consultar MathSciNet/zbMATH quando disponíveis. Não realizada nesta sessão.
- Para P-R1/P-R2: procurar recuperação de coeficientes de funções L, identificação por zeros, estabilidade de problemas inversos e vazamento de janela.
- Para P-C1/P-C2: procurar zetas ponderadas de mapas ax+b, autoconjugação, filtros de ciclos, operadores de transferência e transientes. Parte dessa literatura já torna previsíveis os controles propostos.
- Redigir uma comparação com o trabalho mais próximo antes de classificar um achado C. Uma contribuição negativa ou um limite rigoroso pode ser o resultado final.
