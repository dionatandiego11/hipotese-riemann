# Direção experimental — perguntas que os artefatos existentes permitem formular

26/09/2026. Pedido do usuário: hipóteses criativas e testáveis, com caminhos e prioridade. **Esta entrega formula; não executa testes nem constitui pré-registro.** IDs locais `EXP26-*` evitam a colisão já existente de `P-R5` entre documentos. Nenhuma hipótese foi promovida a H-* ou a achado C.

## Base disponível e acesso

- ζ: 100.000 zeros já consultados, resultados m4, janelas e estimadores, modelo de linhas e diagnósticos de vazamento. São T0 para novas perguntas.
- Maass: S1/S2 e desenvolvimento de H-004, já vistos. Usar somente no escopo de desenvolvimento; não presumir completude de uma faixa que não foi validada.
- Dirichlet: controle e seis blocos prospectivamente reservados para H-004. Não abrir para as propostas abaixo nem reaproveitar o caráter confirmatório de H-004. Qualquer reutilização posterior é exploratória para estas perguntas, salvo reserva específica válida.
- Estádio: diagnóstico parcial, encerrado por prioridade. Não reativar para alimentar esta lista.
- Collatz: fontes e formulações, sem campanha CL1 executada neste escopo. Dados de ζ não validam sozinhos uma dinâmica de Collatz.

Fonte do estado: `docs/ANDAMENTO.md`, declaração H-004 e notas B14/B18–B20. Não foram abertos arquivos de zeros ou resultados reservados nesta entrega. As notas das outras sessões foram consultadas; suas provas e correções não foram todas reauditadas.

## EXP26-1 — o vazamento permite inferir a estrutura omitida?

**Hipótese candidata D:** medidas complexas em várias janelas predefinidas contêm informação suficiente para identificar uma pequena componente omitida do modelo, com melhor previsão fora do ajuste que um modelo sem essa componente.

**Por que agora:** H-004 prevê erros a partir de linhas conhecidas. A nova pergunta inverte esse mecanismo: recuperar informação da causa a partir dos desvios, em vez de fornecer a causa ao preditor. Não presumir que prever o vazamento implique conseguir invertê-lo.

**Primeiro teste proposto:** gerar sinais conhecidos em desenvolvimento e retirar do modelo uma única linha, mantendo-a no sinal. Variar separação, amplitude e posição em relação à banda. O inversor recebe resíduos complexos e janelas; não recebe a frequência, o catálogo verdadeiro da linha omitida ou seu coeficiente. Comparar janelas múltiplas com uma única janela e com ausência de linha adicional.

**Regra antes do piloto:** fixar as janelas e região pesquisada, limite de componentes, conjunto de alternativas e observáveis. Ajustar em parte das janelas e prever os resíduos em janelas não usadas no ajuste. Declarar o erro de localização tolerado e a taxa máxima de detecções falsas. Ruído correlacionado entre janelas não conta como repetição independente. Estudar os valores singulares do problema inverso antes de escolher escalas supostamente recuperáveis.

**Referência obrigatória, revisão de prioridade:** ajuste conjunto direto das linhas do catálogo e de uma linha desconhecida, por mínimos quadrados não lineares ou método adequado de inversão harmônica/matrix pencil. Comparar com a mesma informação, ruído, faixa pesquisada e orçamento. Janelas e resíduos são transformações dos dados: não criam informação independente. Exigir condicionamento viável e ganho demonstrado sobre essa referência, ou uma garantia analítica específica que ela não forneça, antes de investir nesta rota. Se apenas reproduzir o mesmo estimador com mais passos, encerrar como reformulação.

**Negativo informativo:** construir duas frequências/componentes cujos resíduos sejam indistinguíveis no orçamento de erro; isso delimita uma impossibilidade prática de recuperação. Uma busca ilimitada fora da banda não é autorizada.

**Progressão:** substitutos → exploração nos artefatos ζ/Maass T0 → confirmação futura com geração e reserva próprias. Comparação com super-resolução/inversão harmônica é obrigatória; novidade pendente. Não é detecção cega se o catálogo oculto for usado na seleção ou na estimação.

## EXP26-2 — perdas seletivas deixam assinatura diferente de perdas aleatórias?

**Hipótese candidata D:** à mesma fração de níveis omitidos, retirada concentrada em pares próximos produz um vetor de mudanças em espaçamentos, fator de forma e transformada complexo distinguível de retirada aleatória ou de uma lacuna contígua.

**Motivação:** as notas de validação registram perdas seletivas no Dirichlet e lacuna no Maass. A teoria de Bohigas–Pato trata retirada aleatória; aplicá-la a essas falhas sem conferir o mecanismo não é justificado.

**Primeiro teste proposto:** em cópias T0 de ζ e em substitutos conhecidos, introduzir os três mecanismos, com igual quantidade de omissões. Preservar originais. Fixar o bloco e suas bordas antes de remover níveis; separar experimento de transformação em coordenada fixa de eventual recálculo do unfolding. Não entregar ao classificador o número original de níveis, a lista completa, ou outros metadados que o diagnóstico real não conheceria. A referência completa serve somente para medir o efeito na avaliação.

**Decisão:** previsão fora do conjunto de desenvolvimento com falso positivo controlado; comparar com diagnóstico só por contagem/espaçamentos. Usar réplicas completas como unidade. Escolher primária antes, sem selecionar retrospectivamente a estatística que separa melhor.

**Negativo informativo:** demonstrar sobreposição operacional entre dois mecanismos, ou ausência de ganho do resíduo complexo. Não alegar que esse mecanismo explica o C3 de ζ sem evidência adicional; trata-se de intervenção controlada, não de uma explicação já obtida para os dados reais.

## EXP26-3 — a identidade aritmética sobrevive quando escondemos o rótulo?

**Hipótese candidata D:** sinais e amplitudes recuperados distinguem caracteres dentro de uma família de mesmo condutor/paridade, e permitem prever coeficientes em frequências deliberadamente excluídas do ajuste.

**Diferencial procurado:** comparar identificação baseada nas linhas com identificação por densidade e com modelos de coeficientes independentes. A regra χ(p^r)=χ(p)^r é conhecida; a pergunta é sua recuperabilidade com informação finita, sem fornecer a resposta ao algoritmo.

**Primeiro passo sem novos zeros:** construir uma matriz de distinguibilidade dos caracteres pela faixa de frequências e pelo erro previsto do instrumento. Pares coincidentes nas linhas acessíveis são controles negativos obrigatórios. Esse cálculo, se executado futuramente, terá declaração separada. Não usar os dois caracteres atuais de condutores distintos para uma forte alegação de identificação cega.

**Progressão:** avaliar viabilidade matemática → testar pipeline em substitutos → só então decidir se uma pequena família de novos espectros justifica custo. Frequências omitidas deliberadamente não são o mesmo que previsão em dados estatisticamente independentes; observar o espectro inteiro pode revelar seus coeficientes indiretamente.

**Negativo informativo:** equivalência entre candidatos sob a informação disponível, ou acerto explicado apenas pela densidade/metadados. A contribuição potencial é uma fronteira de identificabilidade, não descobrir multiplicatividade.

## EXP26-4 — os ramos de Collatz têm leis de contagem próprias?

Definir A_m(x)=#{1≤n≤x : algum iterado de T(n) é m}, para m=5 e 16. As notas B19 distinguem essas contagens individuais de sua recomposição em ζ. Não pressupor que toda órbita atinja {1,2}.

**Pergunta D:** existem densidades δ_m e uma lei quantitativa de resto para A_m(x)−δ_m x? A primeira tarefa é verificar antecedentes e formular um regime; não ajustar uma potência livre e anunciá-la como lei.

**Redução da pergunta, revisão de 26/09:** para T acelerado, T⁻¹(8)={5,16}. As órbitas de 5 e 16 se juntam em 8 e seguem 4,2,1; por isso seus conjuntos de pré-imagens são disjuntos. Se todos os inteiros até X atingem 1, todo n≤X fora de {1,2,4,8} pertence a exatamente um desses conjuntos. Logo A₅(x)+A₁₆(x)=⌊x⌋−4 para 8≤x≤X. Basta estudar A₅; a outra contagem serve de invariante de implementação. Isso não pressupõe Collatz global.

A página primária de Barina registra verificação de todos os n<2^71 em 15/01/2025: https://pcbarina.fit.vutbr.cz/ . Página consultada em 26/09/2026; não reexecutamos nem auditamos essa verificação. Dentro dessa faixa, a convergência é resultado computacional externo disponível, mas a rotina local ainda precisa determinar **qual ramo**. Limite de passos/tempo pode produzir classificação local incompleta, mesmo havendo convergência conhecida; não é indecidibilidade matemática nem pode ser convertida em ramo por suposição. Preferir classificação exata completa da faixa escolhida e declarar execução incompleta se o teto impedir terminá-la.

**Antes do piloto:** busca OEIS e literatura para a divisão 5/16, com tradução explícita entre o mapa acelerado e o mapa usual (onde 5 passa por 16). Fixar modelos concorrentes, por exemplo constante, correção por potência e deriva lenta logarítmica, com complexidade e escalas fora do ajuste declaradas. Uma faixa finita não distingue todas as derivas lentas nem prova densidade. O custo até 10^9 ou 10^10 não está medido: benchmark deve incluir memória, inteiros seguros e classificação, não importar a velocidade de algoritmos que apenas verificam convergência. Nenhuma enumeração nessa escala autorizada aqui.

**Objetivo inicial:** testar se algum modelo finito de resíduos prediz o resto em escalas fora do ajuste. Uma estabilidade numérica de A_m(x)/x não prova a existência de densidade. Cotas de erro de contagem podem implicar continuação de séries sob condições adequadas; o sentido inverso exige hipóteses adicionais, não é equivalência automática.

**Por que serve à ponte:** a série D_m(s)=Σ_{n∈O⁻(m)}n^{−s} contém informação específica do ramo. Ainda falta qualquer mecanismo que ligue suas singularidades aos zeros de ζ.

## EXP26-5 — critério para admitir um teste direto Collatz–Riemann

Esta é uma **pergunta matemática de alto risco, ainda sem hipótese numérica testável**: existe uma equação das séries D_5/D_16, ou de um operador derivado de T, em que zeros de ζ tenham efeito não trivial e demonstrável?

Para virar teste, o candidato deve produzir uma destas coisas antes de consultar coincidências: localização prevista de singularidades/resonâncias; uma fatoração com fatores restantes controlados; ou uma lei de contagem com termos oscilatórios e coeficientes determinados pela dinâmica. Não basta pôr ζ no denominador nem somar séries que recompõem ζ por definição.

Se aparecerem previsões em termos de ordenadas γ, os parâmetros e amplitudes precisam ser determinados independentemente dos dados de zeros usados para avaliar. Ajustar muitos senos aos mesmos zeros é um controle de ajuste, não ponte. Trocar T por outro mapa deve fornecer um controle que esclareça o papel específico de Collatz.

**Estado da literatura local:** Meinardus e as notas sobre Siegel não fornecem essa previsão; ζ aparece por uma componente constante. A fronteira natural de uma série de potências não decide sozinha a continuação de sua série de Dirichlet. Não há atualmente um experimento de zeros do projeto capaz de substituir o passo matemático faltante.

## Escolha e sequência — revista em 26/09/2026

1. Concluir controle Dirichlet e H-004 exatamente como declarados.
2. **EXP26-2 é a frente experimental principal.** A [ficha prévia](FICHA_EXP26_2_PREVIA.md) distingue detecção do mecanismo e ganho sobre diagnósticos simples. Ela ainda não é declaração congelada.
3. **EXP26-1 condicionada a dois filtros:** identificabilidade/condicionamento e comparação com ajuste conjunto direto. Pode ter interesse por garantia analítica específica; não há vantagem presumida de informação.
4. **EXP26-4/5 como frente complementar:** busca bibliográfica/OEIS, modelos de escala e benchmark antes do piloto. A redução a A₅ foi incorporada; custo permanece a medir.
5. EXP26-3 mais tarde, pois uma comparação forte provavelmente exige uma família diferente das duas funções atuais.

Revisão motivada pelas ressalvas do usuário, antes de qualquer teste destas propostas. A recomendação inicial priorizava EXP26-1; a presente ordem a substitui explicitamente. Todos os dados vistos permanecem exploratórios para as novas perguntas. Não há poder medido, custo de produção medido ou novidade estabelecida nesta nota.
