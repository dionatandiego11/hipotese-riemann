# Sequência de trabalho proposta

19/09/2026. Planejamento, **não protocolo de teste congelado**. Nenhum limite sugerido abaixo é resultado medido.

## 1. Concluir a validação delimitada

Manter os controles Dirichlet, Maass e estádio com seus resultados positivos, negativos ou inconclusivos. Um critério vazio ou de baixa sensibilidade precisa ser distinguido de uma falha física. Não condicionar a abertura do registro a todos os controles darem resultados positivos; o protocolo v2 exige resultado registrado.

Antes da produção do estádio: resolver as questões documentadas em REVISAO_PODER_E_REGISTRO.md, implementar a cadeia, fazer o piloto de convergência e oferecer comandos de produção ao usuário. Nenhuma execução longa é iniciada por esta entrega. A aquisição Dirichlet em andamento não foi interrompida.

## 2. Escolher uma pergunta principal e uma frente pequena

Recomendação: P-R1 como principal; P-C1 como laboratório. P-R2 fica como alternativa se a busca bibliográfica ou a sensibilidade tornarem P-R1 pouco informativo. Não aumentar a lista de testes só para procurar um resultado significativo.

Para cada candidato, concluir uma ficha de triagem com:

1. Enunciado que possa ser falso e alternativa concreta.
2. Referência mais próxima e diferença pretendida, ainda sem afirmar prioridade.
3. Dados e custo necessários; informação permitida ao algoritmo.
4. Estatística primária ou identidade exata, efeito mínimo e regra de inconclusão.
5. O que encerra a linha: equivalência conhecida, falta de identificabilidade, potência insuficiente ou falha de replicação.

## 3. Entregas pequenas antes de cálculos grandes

**Riemann — primeira entrega futura:** especificação de P-R1 e comparação bibliográfica com B1/B2 e modelos de janela existentes. Usar os dados antigos só como desenvolvimento. Congelar uma previsão antes de abrir o lote que será usado para avaliá-la. Se os controles já o consumiram, tratá-lo como T0 e reservar outro lote para confirmação. Não reutilizar o selo confirmatório de m4 para a pergunta nova.

**Collatz — primeira entrega futura:** CL0 e CL1 do plano existente. Definir mapa, espaço, medida quando aplicável e convenção de período; reproduzir exatamente os casos conhecidos até período 12. Esse passo é validação, não novidade. Depois, CL2–CL3 podem testar filtros de palavras periódicas e P-C1. Cada extensão terá declaração própria. Não aplicar o instrumento de zeros a uma sequência de órbita sem derivar a observável correspondente.

Código novo deve ficar fora dos caminhos cobertos pelos locks m3/m4. Os protocolos anteriores são referência, não arquivos a corrigir silenciosamente. Resultados futuros ganham pasta própria e manifesto; não salvar medições em tabelas desta pasta como se já existissem.

## 4. Poder, precisão e multiplicidade

Para testes estatísticos, simular o procedimento decisório completo sob a hipótese e sob alternativas de tamanho definido. Estimar probabilidades de sucesso e falso positivo com incerteza Monte Carlo, variando o espectro substituto externo e recalibrando os nulos quando o protocolo real o fizer. Não confundir número de embaralhamentos internos com número de experimentos independentes de poder.

Para identidades exatas de Collatz, substituir poder estatístico por cobertura de casos, invariantes e verificação independente. Não exigir valores-p para álgebra exata.

O protocolo v2 permanece vigente; recomendações sobre dependência e relatórios sequenciais na revisão anexa são propostas para versão futura, não mudanças aplicadas. Definir a família confirmatória e sua data de fechamento antes do teste. Blocos contíguos não devem ser tratados automaticamente como independentes.

## 5. Critério de ciência nova

Promover a achado apenas uma afirmação que:

- sobreviva a controles numéricos, de fronteira, precisão e seleção;
- seja distinta do que as fontes já demonstram;
- faça previsão fora dos dados usados para construí-la, ou tenha prova/contraexemplo verificável;
- tenha escopo e incerteza explícitos, inclusive quando negativa.

Encontrar uma nova interpretação visual não satisfaz esses critérios. Descobrir uma obstrução, uma impossibilidade de identificação ou um erro sistemático com previsão quantitativa pode satisfazê-los.

## Próxima tarefa concreta

Revisar as pendências da análise de poder antes da produção do estádio; em paralelo conceitual, terminar a triagem bibliográfica de P-R1 e a especificação CL0. Os experimentos de hipóteses espectrais aguardam o marco da 11.6 fixado no registro. Esta pasta permite avançar na formulação e na leitura sem consumir dados reservados.
