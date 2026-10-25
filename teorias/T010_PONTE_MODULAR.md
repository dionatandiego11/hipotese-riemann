# T010 — Comparar Collatz com uma ponte dinâmica–zeta já existente

15/10/2026. Proposta **D**, risco alto. Primeiro alvo de construção `pendente`; novidade não estabelecida. A obstrução algébrica abaixo é elementar, com escopo restrito.

## Por que introduzir um terceiro objeto

Mayer fornece um exemplo em que dinâmica, operador e zeta se relacionam por um teorema. Para o grupo modular, a Proposição 3 escreve

    Z_Selberg(s)=det(I−L_s)det(I+L_s)=det(I−L_s²),  Re s>1/2,

com o operador e o espaço especificados na fonte; o Corolário 3 trata a continuação. PDF p. 9, impressa p. 8, conferida visualmente. O operador nasce da dinâmica de frações contínuas. A zeta de Selberg não é a zeta de Riemann. As especulações da p. 10 do preprint não são premissas desta proposta.

Fonte: [Mayer, MPI/90-86](https://archive.mpim-bonn.mpg.de/346/1/preprint_1990_86.pdf). A prova integral e o estado posterior das especulações não foram auditados nesta rodada.

## Uma obstrução que podemos ver antes de calcular

Os ramos inversos de Collatz são b₀(y)=2y e b₁(y)=(2y−1)/3, com a restrição aritmética no segundo. Como transformações projetivas, têm matrizes

    B₀=[[2,0],[0,1]],  B₁=[[2,−1],[0,3]].

Todos os produtos são triangulares superiores e fixam ∞. Qualquer conjugação projetiva única preserva a existência de um ponto fixo comum.

Os ramos de Gauss g_a(x)=1/(a+x), a≥1, têm matrizes [[0,1],[1,a]]. Não possuem ponto fixo comum: um ponto finito comum a g₁ e g₂ teria de satisfazer x²+x=1 e x²+2x=1, impossíveis simultaneamente; ∞ também não é fixo.

**Conclusão A restrita:** não existe uma única conjugação de Möbius que identifique essas duas famílias completas de ramos. Não exclui codificações simbólicas, mapas induzidos, extensões de estado ou outros entrelaçamentos.

## A proposta ousada, mas ainda formulada como pergunta

Investigar uma extensão natural que registre simultaneamente tamanho real, condições 2-ádicas e resíduos 3-ádicos dos caminhos de Collatz. “Natural” significa deduzida das transformações existentes, com projeção de volta à dinâmica original — não adicionar uma inversão x→1/x apenas para fabricar semelhança com Gauss.

**Primeiro alvo:** construir e verificar uma tabela de espaços, ramos, pesos, restrições de integridade e transformações de observáveis. Se houver candidato a ponte, exigir uma aplicação J e uma identidade do tipo J P_C = P_G J em domínio declarado, ou uma identidade de traços com resto controlado. Nenhuma delas foi encontrada.

**Filtro antes de espectros:** a construção distingue 3x+1 de variantes ax+b? Preserva a informação sobre inteiros positivos? Os pesos são determinados sem usar primos ou zeros desejados? Uma operação genérica disponível para qualquer mapa não explica a aritmética específica.

**Resultado útil possível:** excluir uma classe precisa de representações ou encontrar uma relação funcional nova. Reconstruir o resultado conhecido de Mayer seria preparação, não novidade. Só avançar à ligação com ζ após identificar exatamente o objeto intermediário e conferir a teoria espectral correspondente.

Conexões: [T003](T003_FAMILIAS_COLLATZ_RIEMANN.md), [T009](T009_HILBERT_MEMORIA.md) e [plano anterior da ponte direta](../hipoteses/PLANO_PONTE_DIRETA_COLLATZ_RIEMANN.md).
