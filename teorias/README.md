# Teorias — espaço de interconexões

**Limite de custo em25/10:** [subaditividade, barreira combinatória e potencial](SYRACUSE_LIMITE_CUSTO_20261025.md). Nenhum bloco de1–4 passos poderia atingir custo máximo2r por cardinalidade; assintoticamente a barreira fica abaixo de2. Potencial de amortização formulado, não construído. A fonte de Wirsching exige ainda minorante relativa à média: cobertura não basta.

**Cobertura uniforme em25/10:** [política inversa e prova por indução](SYRACUSE_COBERTURA_UNIFORME_20261025.md). Todas as unidades são atingidas para3n+7<=S<=2*3^{n-1}+n-1, n>=4. Certificado finito exato e três testes concluídos; a faixa central2n+O(sqrt(n)), a revisão independente e a novidade continuam abertas. Próximo alvo: custo mínimo de políticas inversas e comparação bibliográfica.

**Complementaridade em20/10:** [recorrência de ausências e custo acoplado](SYRACUSE_COMPLEMENTARIDADE_20261020.md). Regras exatas conferidas; redução por preenchimento do último expoente. Falta controlar os piores segmentos da órbita aritmética, com seu custo.

**Avanço em20/10:** [semente máxima e complementaridade de sufixos](SYRACUSE_SEMENTE_COMPLETA_20261020.md). Catálogo completo delimita o alcance do prefixo4; nova identidade de5 redistribui custo e equilibra o último dígito. Cobertura global continua aberta.

**Resultado negativo em20/10:** [disponibilidade de H](SYRACUSE_DISPONIBILIDADE_20261020.md) calculada por recorrência exata. No caso central ell8/S16, H cobre apenas1 dos1.250 pais atingidos; não é argumento de cobertura geral. Próximo alvo: sementes complementares e custo.

**Último dígito em19/10:** [reescrita explícita em três expoentes](SYRACUSE_ULTIMO_DIGITO_20261019.md). Existe o mecanismo; a distribuição de seus grupos por classe e custo segue aberta. Exploração pequena declarada e verificações exatas concluídas.

**Reescritas em19/10:** [mecanismo local e correção de convenção](SYRACUSE_REESCRITAS_CUSTO_20261019.md). Conferida a ordem dos geradores contra os dois métodos existentes; nenhuma cobertura global demonstrada. A cota de energia anterior permanece válida.

**Avanço 19/10/2026:** [cota de energia condicionada](SYRACUSE_ENERGIA_CONDICIONADA_20261019.md), com auditoria da fonte e transferência ao custo fixado. Controla concentração agregada; não assegura preenchimento de cada resíduo. Dois testes pequenos exatos passaram.

**Execução em 18/10/2026:** [pares raros no CUE](EVENTOS_RAROS_CUE_20261018.md) e [colisões de Syracuse](SYRACUSE_COLISOES_20261018.md). O primeiro alvo de T001 foi concluído; T008 produziu a recorrência exata e a obstrução em L², já localizada também na bibliografia. Cinco testes novos passaram. As extensões a L e ao custo condicionado seguem abertas.

**Ampliação em 15/10/2026:** [cinco apostas e ordem recomendada](DIRECOES_20261015.md), agora com busca dirigida em fontes primárias. Novas fichas: [concentração de Syracuse](T008_INTERMITENCIA_COLLATZ.md), [Hilbert, memória e transientes](T009_HILBERT_MEMORIA.md) e [ponte modular intermediária](T010_PONTE_MODULAR.md). A ausência de ligação direta Collatz–Riemann não impede resultados úteis em cada frente. As notas abaixo preservam o registro da seleção inicial.

Criado em14/10/2026. Aqui podemos propor conexões ousadas, reformular perguntas e registrar ideias que ainda não sabemos demonstrar. “Teorias” é o nome da pasta, não uma afirmação de que as propostas já sejam teorias estabelecidas.

**Nossa pergunta central:** que estrutura permite controlar o erro das médias de funções L e entender suas correções? Queremos também explorar se alguma ferramenta de dinâmica aritmética, incluindo Collatz, ajuda nessa tarefa.

A primeira seleção usa o material já construído e as notas de fontes disponíveis no projeto. **Não foi uma nova varredura bibliográfica externa.** Cada ficha aponta a base efetiva e o que ainda é especulação. Fontes novas entram no arquivo bibliográfico existente, sem duplicar PDFs nesta pasta.

## Por onde começar

1. **[T001 — Pares raros e correções](T001_PARES_RAROS.md):** a direção mais próxima da advertência de Andrew. Primeiro entender analiticamente onde nasce a correção no controle CUE, depois perguntar o que seria transferível para L.
2. **[T002 — Correlações e escalas](T002_CORRELACOES_ESCALAS.md):** a direção mais próxima da nossa fórmula do erro. Procurar cancelamento nas somas aritméticas que efetivamente apareceram.
3. **[T003 — Collatz e famílias de filtros](T003_FAMILIAS_COLLATZ_RIEMANN.md):** a frente mais direta para explorar uma conexão estrutural entre os dois projetos. Precisamos identificar uma operação ou estimativa comum, não apenas observar semelhanças.

As demais propostas estão no [mapa](MAPA_INTERCONEXOES.md). O [registro](REGISTRO.csv) permite acrescentar ideias sem perder seus estados e o [modelo de ficha](MODELO_FICHA.md) organiza novas contribuições.

## Como usamos este espaço

Ideias podem começar por uma analogia livre. Quando uma delas orientar uma conclusão ou um experimento, precisamos explicitar o objeto, as hipóteses, a previsão e o que distinguiria sucesso de fracasso. Um contraexemplo ou uma obstrução também é resultado útil.

Usamos os mesmos rótulos do projeto: A para matemática com hipóteses declaradas; B para reprodução numérica; C para achado experimental com novidade a investigar; D para proposta/conjectura. As sete interconexões iniciais são **D**. Bases A ou B citadas não promovem automaticamente a conexão inteira.

Esta pasta não muda os protocolos de `hipoteses/`, não libera dados reservados e não exige congelar cada pensamento. A exploração permanece leve; um teste científico futuro segue as regras já existentes. Não houve cálculo novo nesta criação.

## Onde estamos na ponte

A parte aritmética dos geradores foi calculada. A estimativa sublinear do erro e os termos inferiores continuam abertos. O perfil polar mostrou que a hipótese de uniformidade já contém o desvio do momento procurado. Precisamos de uma estrutura adicional que produza cancelamento ou uma previsão independente.

Leitura de entrada: [estado atual](../docs/ESTADO_ATUAL.md) e [erro/perfil polar](../hipoteses/RAZOES_ERRO_PERFIL_POLAR_20261014.md).
