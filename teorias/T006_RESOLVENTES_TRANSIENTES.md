# T006 — Amplificação, transientes e normas de resolventes

14/10/2026. Natureza da conexão: **D — proposta exploratória**, sem novidade estabelecida. Primeiro alvo: `pendente`. Prioridade: exploratória.

**Em linguagem simples:** um sistema pode parecer estável pelos seus autovalores e mesmo assim amplificar muito uma perturbação antes de ela desaparecer. Isso sugere olhar para normas e transientes, além do espectro.

**Base elementar.** Para J=[[r,K],[0,r]], com |r|<1,

    (I−J)^{-1}=[[1/(1−r),K/(1−r)^2],[0,1/(1−r)]].

O termo K pode tornar a resposta grande sem mudar os autovalores r. É um controle de álgebra linear, não um modelo já encontrado para a função zeta.

**Ideia D.** Em candidatos de transferência de Collatz, estudar resolventes e produtos condicionados antes de interpretar autovalores como explicação dos transientes. No lado de razões, perguntar se existe uma representação do gerador cuja norma explicite a amplificação perto dos polos.

**Primeiro alvo matemático.** Definir um único operador, espaço e norma a partir das construções existentes. Verificar se é normal; se não for, medir analiticamente quais estimativas espectrais deixam de controlar as normas relevantes. Não introduzir um operador feito a partir dos zeros desejados.

**Barreira.** Ainda não existe aqui uma representação de M_j por esse resolvente. A semelhança com polos é uma sugestão metodológica, não identidade.

**Ligação à ponte:** pode explicar por que conhecer espectros ou contrações isoladas não basta para uniformidade. É uma frente de risco alto.

**Leituras locais:** [transientes e dependências](../hipoteses/PLANO_COLLATZ_DEPENDENCIAS_TRANSIENTES.md); [fechamento de filtros e normas](../hipoteses/COLLATZ_FILTROS_FECHAMENTO_20261012.md).
