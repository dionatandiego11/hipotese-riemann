# Arquitetura da prova de Alpöge — primeira leitura

22/11/2026. Mapa de leitura, não auditoria independente da prova Lean nem afirmação de que esta nota reproduza todos os seus passos. Foram lidos a nota de Alpöge, o resumo e enunciados de verificação de Sutherland e trechos iniciais e de limitações de duas exposições em desenvolvimento. Não foram compilados os 175.187 módulos ou examinada sua árvore de dependências neste projeto. A situação das verificações pode mudar: consultar o registro atualizado antes de citá-la.

## 1. O que foi anunciado e o que foi verificado

Alpöge anunciou em 20/11/2026 uma prova formal da hipótese de Riemann e da hipótese generalizada para funções L de Dirichlet. As comunidades Lean e Mathlib certificaram a prova em seu [comunicado de 21/11](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/). O [registro de Sutherland](https://math.mit.edu/~drew/grh/), consultado na versão atualizada às 04:35 UTC de 22/11, descreve compilação, axiomas, checagem de módulos e comparações independentes dos enunciados.

O registro distingue testes: nanoda, con-leche e con-ron aceitaram verificações reportadas; a repetição pelo núcleo Lean de cada módulo passou; a repetição do *export completo* pelo núcleo padrão/paranoico e a execução integral de `lake comparator` ainda constavam em andamento naquele horário. Não confundir essas etapas nem tratar o trabalho de Sutherland como verificação executada por nós.

O escopo conferido dos teoremas inclui a RH para ζ e a faixa crítica para L de Dirichlet, para todos os caracteres. O registro especifica que funções L de Hecke, zetas de Dedekind e funções automórficas **em geral** não estão entre os enunciados então verificados. A ausência dessas conclusões da lista não afirma que sejam falsas ou impossíveis de deduzir em casos particulares.

## 2. Mapa de alto nível

Na [nota de quatro páginas](https://alpo.ge/remark.pdf), Alpöge descreve a estratégia como descendente do método de Stepanov em corpos finitos: lá, multiplicidades de zeros de uma função auxiliar ajudam a obter uma contagem. Para adaptar a ideia aos inteiros, a nota aponta uma cadeia de levantamentos theta como mecanismo análogo de multiplicidade. Sua lista cronológica de ideias não é, por si só, uma prova legível integral; o próprio autor admite que partes da descrição são provisórias.

A exposição em desenvolvimento de [Rubinstein e colaboradores](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper.pdf), §I.0–I.1, apresenta o seguinte esqueleto para ζ. Esta é a interpretação da exposição, não uma auditoria nossa das declarações Lean:

1. Introduzir uma soma suavizada de potências de primos e separar seu termo principal.
2. Reduzir a ausência de zeros à direita de 1/2 a uma **cota superior unilateral** para essa soma, em janelas longas de escalas.
3. Construir objetos aritméticos por levantamentos theta em campos auxiliares. Comparar divisibilidade local por primos com tamanho global de reticulados produz uma desigualdade principal, denominada (M) na exposição.
4. Usar estimativas de caracteres auxiliares para transformar (M) na cota da soma suavizada. A exposição descreve perdas da ordem x/m e m: equilibrá-las motiva uma cadeia de comprimento próximo de sqrt(x), de modo esquemático; os parâmetros efetivos e perdas têm que ser lidos nos enunciados completos.
5. Excluir zeros à direita da linha crítica e usar a equação funcional para obter o resultado no semiplano oposto.

O [resumo de Slijepčević](https://hexagonmath.org/pdf/2611.00812v1), §§1–2, apresenta a versão para caracteres: combinações positivas de somas torcidas, campos CM auxiliares, ganhos locais de reticulados e desigualdades de inclinação. É outra exposição em desenvolvimento, com trechos assumidamente ainda não compreendidos pelo autor; não a tratamos como revisão completa independente.

## 3. Objeto analítico e quantificadores

A exposição para ζ define, para x>=1,

    G(x) = sum_{n<=x} Λ(n)(x/n − 1) − x(log x − 1 − γ).

O peso é uma rampa; Λ concentra a soma em potências de primos. A parte subtraída é o termo principal. Para Re(s)>1, sua transformada de Mellin, antes da continuação, é

    ∫_1^∞ G(x)x^(−s−1)dx
      = −ζ'(s)/[ζ(s)s(s−1)] − 1/(s−1)^2 + (1+γ)/(s−1).

É essa combinação, com normalizações específicas, que entra na redução; não é a transformada de Hann usada no m4. Na exposição, para cada ε em faixa adequada, a meta é uma cota superior G(x)<=C_ε x^(1/2+ε), para todos os x em janelas [Y,Y^(3/2)] com Y arbitrariamente grande. A constante e as escolhas auxiliares devem respeitar os quantificadores dos lemas originais. Exigir a cota apenas em pontos isolados não é o mesmo enunciado. A conclusão usa um argumento de positividade/oscilações e a equação funcional; não decorre simplesmente de observar a soma num intervalo finito.

Na versão para Dirichlet, aparecem famílias de caracteres e combinações ponderadas, não apenas G da zeta. A formulação precisa depende dos enunciados da fonte e da ordem de escolha dos parâmetros.

**Ponto a conferir:** em Slijepčević, a introdução e a redução analítica falam em janelas [Y,Y^λ], mas a §1.5 extraída da versão consultada escreve [Y,λY]. Não identificamos nesta leitura se é erro de redação ou mudança de convenção. Não usar a largura de janela dessa exposição como premissa sem conferir os enunciados e a versão Lean. Rubinstein, §I.1, escreve explicitamente [Y,Y^(3/2)].

## 4. Onde está o trabalho difícil

Na exposição de Rubinstein e colaboradores, (M) aparece como entrada tomada do desenvolvimento Lean; o rascunho escreve algumas partes e lista outras ainda citadas. Elas incluem integridade dos núcleos theta, estimativas de fórmulas de traço, cotas cohomológicas e montagem da desigualdade. O texto não demonstra integralmente (M).

Slijepčević, §§1.4 e 11, explicita que não compreende ainda por completo o controle das perdas que liga ganhos locais dos reticulados às somas de primos e a construção dos dados de reticulados. Isso limita nossa compreensão humana atual; não equivale a uma refutação da verificação formal reportada.

## 5. Efeito no nosso projeto

- **RH e Dirichlet:** tratar como resultado formal externamente verificado no escopo acima, com atribuição e data; não modificar silenciosamente protocolos ou resultados históricos. Uma consequência precisa deve ser rastreada ao enunciado e às demais hipóteses que usa.
- **Simplicidade:** RH/GRH de Dirichlet localiza zeros; não afirma que todos sejam simples. Momentos com 1/|L'(ρ)| e argumentos locais continuam exigindo simplicidade, exclusão ou tratamento explícito de multiplicidade.
- **Momentos negativos:** a localização dos zeros não entrega automaticamente os termos inferiores, uma estimativa uniforme das médias de razões, nem o controle dos pares próximos/amplitudes. Conferir caso a caso as fórmulas de Andrew e do projeto.
- **Instrumento e H1:** o controle matemático do lado dos primos e a fórmula explícita são próximos do nosso tema, mas a soma G usa outro peso e outra pergunta. Nenhuma equivalência com a cauda Hann ou com os resíduos de S2-ratio′ foi provada. Revisar separadamente o certificado condicionado a RH e suas demais dependências.
- **Física e Collatz:** a prova relatada não identifica Hamiltoniano e não fornece ponte direta com Collatz. Interpretações ou transferência de técnicas são hipóteses futuras, não consequências.

## 6. Próximo trabalho verificável

1. Conferir a redução analítica da exposição de Rubinstein, Parte II §1, inclusive constante, quantificadores de ε e janelas, distinguindo lemas citados e demonstrados. Identificar os nomes Lean apenas após obter fonte confiável e conferir o caminho de dependências; não inferi-los a partir de resumos.
2. Criar uma matriz pequena dos nossos resultados condicionais: hipótese RH/GRH, simplicidade, uniformidade e outras entradas; apontar onde o novo resultado externo seria aplicável sem alterar o protocolo histórico.
3. Avaliar se um alvo independente sobre o núcleo suavizado G tem utilidade para momentos negativos ou física. O simples cálculo de G em dados finitos não testa a cota assintótica nem a prova.

## 7. Fontes e leitura efetiva

- Alpöge, [nota de 20/11/2026](https://alpo.ge/remark.pdf), 4 páginas, lida para visão e lista de ideias.
- Comunidades Lean e Mathlib, [comunicado de 21/11](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), lido integralmente.
- Sutherland, [verificações e enunciados](https://math.mit.edu/~drew/grh/), resumo e cinco enunciados consultados; versão de 22/11 às 04:35 UTC indicada na página.
- Rubinstein e colaboradores, [exposição de ζ](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper.pdf), rascunho de 21/11; resumo, aviso de escopo e §§I.0–I.1 consultados. A cópia de leitura baixada tem SHA-256 `667d88b3c375adf0466678094f452ca966aef0f4d368f6340d2bd5328b7fb706`; uma versão futura no mesmo URL pode diferir. Outros trechos citados são a lista de entradas não demonstradas pelo rascunho, não leitura integral dos 164+ páginas.
- Slijepčević, [outline](https://hexagonmath.org/pdf/2611.00812v1), resumo e §§1–2, com atenção às limitações; não lido integralmente nem verificado contra os módulos Lean nesta etapa.

Sem novos experimentos, alteração de protocolos, dados reservados, mudança de classificação automática, commit ou push nesta entrega.
