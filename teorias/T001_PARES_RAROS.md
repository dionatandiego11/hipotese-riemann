# T001 — Pares raros, camadas de transição e termos inferiores

**Atualização 18/10:** primeiro alvo concluído como controle A conhecido. [Derivação por regiões e lema condicional de pares](EVENTOS_RAROS_CUE_20261018.md). A proposta de transferência para L permanece D e aberta; o estado inicial abaixo é histórico.

14/10/2026. Natureza da conexão: **D — proposta exploratória**, sem novidade estabelecida. Primeiro alvo: `pendente`. Prioridade: alta.

**Em linguagem simples:** acontecimentos muito raros podem contribuir pouco para a média principal e, ainda assim, determinar a primeira correção. A ligação proposta é entre pares próximos de zeros, expansões assintóticas e limites que não comutam.

**Base disponível.** No nosso controle CUE, o momento discreto deslocado normalizado satisfaz

    E A_U(ε)=1+(N−1)tanh(ε/2).

Para cada matriz fixa, o coeficiente linear é (N−1)S_U; sua esperança é N−1. A derivada da média é (N−1)/2. Esta consequência foi derivada na nota de razões discretas, com base em CFZ; não foi classificada como novidade.

**Ideia D.** Separar a contribuição de pares com distância comparável a ε da contribuição de pares bem separados pode revelar a parcela perdida quando se faz a expansão antes da média. Para L, a pergunta é se uma descrição conjunta de separação e amplitude das derivadas explica alguma correção além do termo principal.

**Primeiro alvo matemático.** Reconstruir no CUE(2), por integração na distância angular φ, o defeito de −1/2 entre os coeficientes. A distância deve ser reescalada como φ=εy na região próxima de uma coincidência. O valor esperado é conhecido do controle completo: este primeiro passo seria calibração analítica, não descoberta. Fixar antes a convenção para φ, as duas extremidades do círculo e a ordem dos limites.

**Por que pode ajudar.** No CUE(2), o fator de Vandermonde suprime pares próximos, mas o peso inverso aumenta justamente neles. Precisamos quantificar o produto dos dois efeitos, não apenas contar pares raros.

**Depois da calibração.** Formular qual lei conjunta de gap e derivada seria suficiente para uma correção de momentos de L. Não presumir que o peso dependa somente do gap: os outros zeros e fatores aritméticos também importam.

**O que enfraquece a rota.** A correção depender de informação conjunta tão difícil quanto o momento original, sem produzir previsão independente. Conhecer apenas a distribuição de espaçamentos não basta.

**Ligação à ponte:** explica um possível mecanismo das correções e da falta de uniformidade, sem provar RH.

**Leituras locais:** [razões discretas, §§6–7](../hipoteses/RAZOES_DISCRETAS_MOMENTOS_NEGATIVOS_20261013.md); [controle CUE](../hipoteses/RAZOES_CONTORNOS_CUE_20261013.md); [CFZ, nota B37](../hipoteses/leituras/B37_RAZOES_20261013.md). Revisão bibliográfica específica de camadas de transição ainda pendente.

## Extensão em 15/10: média finita e variância infinita

Há um controle analítico simples que aproxima esta frente da estatística de eventos extremos. Para uma matriz Haar em U(2), seja φ∈[−π,π] a diferença angular com sinal entre os autovalores. A densidade é p(φ)=(1−cosφ)/(2π). Para o polinômio característico Λ,

    S=Σ_j |Λ'(z_j)|^{−2}=1/(1−cosφ).

Logo E S=1, mas E S²=(1/(2π))∫dφ/(1−cosφ)=∞. Além disso,

    Pr(S>x) ~ [√2/(3π)] x^{−3/2}.

Derivação: perto de zero, S~2/φ² e p(φ)~φ²/(4π); integrar entre ±√(2/x) dá a constante. As identidades são controles A do modelo, sem novidade estabelecida, sem nova simulação e sem revisão independente nesta entrega. O antecedente HKO para a faixa dos momentos está na [nota de fontes](../hipoteses/leituras/TEORIAS_FONTES_20261015.md).

**Proposta D adicional:** formular uma previsão da contribuição de pares raros e um procedimento de incerteza que não pressuponha variância finita. Primeiro estabelecer os teoremas probabilísticos necessários em amostras independentes do modelo; depois investigar dependência e fatores aritméticos antes de qualquer aplicação a zeros de L. Não inferir uma taxa de convergência ou distribuição limite para os blocos do projeto a partir deste exemplo. Uma lista finita de zeros também não tem, por si só, uma “variância populacional infinita”.

Este controle não resolve o alvo original da camada φ=εy nem fornece o termo inferior em T. Ele identifica outra pergunta: o ganho de precisão ao acrescentar dados é compatível com as hipóteses estatísticas utilizadas?
