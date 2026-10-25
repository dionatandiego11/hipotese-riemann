# T004 — Condicionamento, funções geradoras e operadores de transferência

14/10/2026. Natureza da conexão: **D — proposta exploratória**, sem novidade estabelecida. Primeiro alvo: `pendente`. Prioridade: exploratória.

**Em linguagem simples:** uma média pode se comportar bem e um grupo selecionado por uma condição rara se comportar muito mal. Isso aparece tanto na seleção de custos de Collatz quanto nas médias dominadas por zeros próximos.

**Base disponível.** O projeto já estudou custo e resíduo conjuntamente em Collatz, com dependência explícita de resultados de Tao e limites de condicionamento. Nas razões, diferenciar exige controle de uma família complexa, não apenas do ponto pareado.

**Ideia D.** Usar uma função geradora conjunta antes de condicionar:

    Z_n(z,ξ)=E[z^{S_n} exp(2πi ξX_n/3^n) 1_{limites individuais}].

O coeficiente de z^{n+k}, dividido pelo mesmo coeficiente em ξ=0, recupera o caráter condicionado quando a probabilidade é positiva. Com limites individuais finitos, a função é um polinômio em z. Sem esses limites, é necessário especificar seu domínio de convergência.

**Cuidado decisivo.** Multiplicar por z^{S_n} depois de fixar S_n=n+k não muda a lei condicionada: o fator é constante e cancela. A deformação precisa vir antes da extração do coeficiente.

**Primeiro alvo matemático.** Reescrever a construção já existente nessa notação e verificar se uma estimativa no plano complexo controla a extração de coeficientes sem perder uma potência da probabilidade do evento. Conferir sobreposição com as notas de custo conjunto antes de qualquer alegação de novidade.

**Alvo posterior.** Construir um operador que gere Z_n e estudar normas de seus produtos ou resolventes. Não chamar o parâmetro de “pressão” como se uma teoria termodinâmica completa já estivesse demonstrada.

**Ligação à ponte:** um problema comum de uniformidade sob deformação e condicionamento. Não transfere automaticamente resultados de Collatz para funções L.

**Leituras locais:** [custo conjunto](../hipoteses/COLLATZ_CUSTO_CONJUNTO_20261012.md); [mistura condicionada](../hipoteses/COLLATZ_MISTURA_CONDICIONADA_20261013.md); [auditoria](../hipoteses/COLLATZ_AUDITORIA_MISTURA_20261013.md); [Tao, nota B34](../hipoteses/leituras/B34_TAO_SYRACUSE_ESTACIONARIA_20261012.md).
