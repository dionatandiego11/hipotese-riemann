# Perguntas propostas — 25/09/2026

Estado: **pendente**. Caderno de pesquisa, não protocolo de teste. Nenhuma hipótese abaixo recebeu rótulo C ou foi confirmada. H-004 permanece prioritária e congelada; seus dados reservados não entram no desenvolvimento destas propostas.

## P-R5 — distinguir níveis ausentes de erro de truncamento

**Pergunta:** o resíduo complexo permite localizar omissões interiores de níveis e separá-las do vazamento previsto por H-004, melhor que usar apenas contagem e espaçamentos?

Ponto de partida elementar (A, por linearidade): mantendo bordas, densidade e normalização fixas, remover um nível E_* de uma transformada Σw(E)exp[−it(E−E_c)] altera-a por −w(E_*)exp[−it(E_*−E_c)]. Se a convenção do instrumento tiver outro sinal ou fator, a identidade precisa acompanhá-lo. Nas bordas da Hann, w=0: não pode existir garantia uniforme de detectar qualquer omissão. Frequências limitadas, níveis próximos e erros de densidade também limitam a identificação.

**Hipótese de trabalho D:** num domínio interior e numa classe de defeitos previamente delimitados, a fase do resíduo contém informação discriminante adicional. O contraste é com a hipótese de que o ganho desapareça após igualar falso positivo, acesso à informação e custo.

**Próxima entrega, só texto:** especificar defeitos aleatórios e agrupados, falsos níveis, deslocamentos, catálogo incompleto e densidade incorreta; fixar observáveis, referências de comparação, região excluída junto às bordas, métricas de localização e regra de decisão. A alternativa de truncamento deve ser construída sem ajustar o erro observado de teste. Qualquer estudo futuro usa primeiro substitutos e T0 sob declaração própria; não se acessa Dirichlet reservado.

**Resultado negativo útil:** delimitar defeitos indistinguíveis na banda observada ou mostrar ausência de ganho sobre diagnósticos simples. Isso pode impedir uma falsa alegação de completude espectral.

Antecedentes: [Bohigas–Pato](https://arxiv.org/abs/nucl-th/0403006), espectros incompletos; [Candès–Fernandez-Granda](https://arxiv.org/abs/1203.5871), recuperação por Fourier. A contribuição candidata seria a discriminação quantitativa entre mecanismos nesta classe aritmética, não a ideia geral de recuperação. Novidade pendente de busca por citações.

## P-R6 — quais informações os zeros não identificam?

**Pergunta analítica:** quais hipóteses adicionais precisamos fixar antes de interpretar a recuperação de frequências como identificação de uma estrutura aritmética?

Usar o contraexemplo conhecido de Grosswald–Schnitzer, descrito na [rodada bibliográfica](RODADA_BIBLIOGRAFICA_20260925.md), como controle conceitual. Preparar uma tabela que separe: divisor de zeros; polos; fator gama; equação funcional; fatores de Euler; classe de coeficientes; crescimento. Comparar a identidade explícita completa, não somente seu lado de zeros.

**Alvo inicial A, de síntese:** escrever com precisão o que já é não identificável e o que o projeto de fato fixa. Não formular uma nova conjectura de unicidade antes de confrontar os teoremas existentes. Sucesso aqui pode ser um limite demonstrado de interpretação, sem qualquer geração de zeros. Isso não contradiz a recuperação m4 dentro da fórmula da zeta fixada.

## P-C2a — transientes que o espectro de um corte de Collatz perde

Refinamento da P-C2 existente, sem substituir CL0/CL1. Fixar T(n)=n/2 para n par e (3n+1)/2 para n ímpar. No corte 1≤n≤N, definir P_N e_n=e_{T(n)} se T(n)≤N e zero caso contrário: saída absorvente, sem reinjeção artificial.

**Pergunta:** que informação sobre duração dos transientes e escape é perdida ao conservar só os autovalores? Que estimativas podem permanecer válidas quando N muda?

Primeira tarefa analítica: separar ciclos internos e árvores que desembocam em ciclos ou na saída; confrontar autovalores, potências e tempos de sobrevivência. A equivalência entre sobrevivência no corte e não sair até um tempo finito é elementar; ela não decide convergência global de uma órbita positiva. A distribuição dos transientes, não apenas a contagem simbólica de ciclos, é o objeto candidato.

**Hipótese de trabalho D, ainda a quantificar:** observáveis de potências/resolvente distinguem comportamentos que os autovalores dos cortes não distinguem. Antes de promovê-la a teste, procurar se já é consequência direta da teoria de grafos funcionais e ler os resultados de potências/raio espectral do artigo de Leventides–Poulios. Se for conhecida, registrá-la como A e buscar uma previsão especificamente aritmética, ou encerrar a proposta. Não tratar comportamento de cortes como aproximação espectral garantida do operador infinito.

## Sequência recomendada

1. Concluir H-004 como autorizado, sem adaptação motivada por estas propostas.
2. Revisão documental de CL0 conforme a [errata](../results/collatz_cl0/ERRATA_CL0_1.md), preservando o congelamento. CL1 não executada nesta rodada.
3. Especificar P-R5 e aprofundar as referências; produzir a tabela analítica P-R6.
4. Em Collatz, estudar P-C2a no papel e decidir se sobra uma pergunta não resolvida pelas fontes próximas.

Não há justificativa nesta entrega para novas execuções longas. A pergunta, o resultado negativo informativo e a diferença em relação ao que já se sabe devem existir antes do orçamento computacional.
