# Balanço para escolher perguntas

19/09/2026. Revisão de escopo e documentação; **não é auditoria integral do código nem reprodução das execuções**.

Foram consultados AGENTS.md, prompt.txt, PLANO_IMPLEMENTACAO.md, docs/ESTADO_ATUAL.md, docs/ANDAMENTO.md, RELATORIO_CONSOLIDADO, PLANO_COLLATZ, BUSCA_BIBLIOGRAFICA_MANUSCRITO; inventários de fontes/código/configurações; documentação do piloto Dirichlet. Também foram lidos o registro de hipóteses e seu protocolo v2, a análise de poder e seu script e o adendo do estádio recebidos durante o trabalho. A certificação é aqui descrita conforme o estado atual, sem revalidar seus lemas ou intervalos.

| Construção existente | O que permite | Limite para pesquisa nova |
|---|---|---|
| Transformada complexa, detector sem catálogo, controles e ajustes direcionados | Separar detecção de medição de coeficientes | Um ajuste direcionado não é identificação cega |
| m4 em 30 blocos | Base empírica para desenvolver modelos de erro e resolução | Os primeiros 100.000 zeros já foram usados; novas perguntas ali são exploratórias |
| Estatísticas C3 e comparação CUE | Investigar dependência com altura e procedimento de comparação | Rejeitar o GUE finito empregado não refuta universalidade assintótica |
| Certificado vigente, descrito em ESTADO_ATUAL | Distinguir fidelidade numérica N e ligação teórica T sob RH e H-tab | Não é teste independente de RH nem substitui auditoria externa |
| Matriz e correspondências da Etapa 11 | Evitar candidatos incompatíveis no escopo demonstrado | Uma classe condicional não vira hipótese testável sem previsão independente |
| Dirichlet, Maass e estádio | Comparar pesos aritméticos e dinâmica conhecida | Resultado de um controle não garante desempenho em toda a classe de sistemas |
| CL0–CL5 | Plano exato para dinâmica aritmética e problema inverso | Ainda não executado; não há ponte estabelecida com Riemann |

## O que falta para sair da validação

Uma hipótese científica precisa especificar algo que possa falhar mesmo com software correto. Exemplos: uma previsão de erro que não transfere para outra função; dois sistemas que permanecem indistinguíveis após acrescentar uma observável; um modelo de correções finitas que não prevê uma nova altura. Confirmar uma identidade conhecida ou elevar a precisão sozinho não demonstra novidade.

O ganho possível deve ser declarado antecipadamente: nova cota, classificação, contraexemplo, previsão fora do ajuste ou limite quantitativo de identificabilidade. Uma curva parecida, uma correlação sem controle ou a ausência de referência em busca breve não bastam.

## Estado móvel e preservação

Houve atualizações externas do repositório durante esta leitura: foram acrescentados registro v2, análise de poder, adendo do estádio e resultados Maass. A revisão incorpora esses documentos; não assume que a fotografia inicial do git permanece atual. Os arquivos alheios e execuções em andamento não foram modificados.

Os scripts m3/m4, certificado, protocolos e resultados congelados continuam preservados. As propostas desta pasta não ordenam reexecutar esses estudos nem interromper a aquisição Dirichlet em andamento. A preparação de retomada e a confirmação de convergência do gerador seguem recomendações técnicas da revisão anterior, não tarefas executadas nesta entrega.
