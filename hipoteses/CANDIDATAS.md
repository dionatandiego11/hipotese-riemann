# Perguntas candidatas — nenhuma testada nesta entrega

Os enunciados abaixo são propostas do projeto (D), salvo os controles conhecidos explicitamente marcados. Não são afirmações de problemas abertos na literatura. As referências B1–B9 estão em [BIBLIOGRAFIA.md](BIBLIOGRAFIA.md).

## P-R1 — prever os erros antes de vê-los (prioridade principal)

**Pergunta:** o modelo de vazamento por janela, conjugado e linhas fora do catálogo prevê o desvio com sinal dos coeficientes em funções L diferentes, sem reajuste aos desvios de teste?

**Hipótese candidata:** fixado o modelo nos dados antigos de ζ e em sinais sintéticos, suas previsões reduzem o erro de previsão em um conjunto novo de linhas/blocos de Dirichlet, em relação ao modelo de desvio zero e a uma aproximação que despreza o conjugado.

- Observável: erro assinado do coeficiente real; para coeficiente teórico zero, usar erro absoluto com escala declarada, nunca dividir por zero.
- Modelo: projetar uma soma finita de contribuições conhecidas no estimador. Fixar corte, janela e tratamento do resto; estabilidade em alguns cortes não controla a cauda infinita.
- Alternativas: as discrepâncias são dominadas pelas ordenadas, pela densidade ou pelo erro numérico; o modelo não transfere.
- Teste futuro: perda de previsão pareada por bloco, com peso e tolerância fixados por erro numérico e efeito mínimo relevante. Fase é teste separado. Não selecionar linhas pelo desvio observado.
- Refutação operacional: ausência de ganho mínimo previamente declarado fora dos dados usados para escolher o modelo, ou erros sistemáticos fora da faixa de incerteza prevista.
- Dados: ζ antigo para desenvolvimento; controle Dirichlet para exploração após aberto; confirmação exige outro lote T1 conforme v2.
- Literatura: B1 e B2 impedem vender recuperação aritmética ou efeitos de truncamento em geral como novos. A lacuna a investigar é a previsão quantitativa **transferível para este estimador**.
- Entrega desejada: modelo que faz previsões verificáveis, inclusive de falhas. Custo inicial baixo com artefatos existentes; nenhum cálculo novo autorizado por este texto isoladamente.

## P-R2 — identidade aritmética sem rótulo

**Pergunta:** quais valores de χ e quais caracteres de uma família finita são distinguíveis usando somente informação espectral limitada?

**Hipótese candidata:** coeficientes recuperados permitem identificar o caráter entre candidatos previamente definidos, com possibilidade explícita de abstenção, melhor do que usar somente a densidade média.

- Entradas proibidas: nome do arquivo com caráter, q/κ verdadeiros, catálogo já multiplicado por χ ou configuração que entregue a resposta.
- Comparação justa: incluir candidatos com mesmo condutor e paridade quando possível; avaliar um método que usa só contagem/densidade. As duas funções atuais, de condutores distintos, são demonstração inicial fraca para esse propósito.
- Teste: matriz de confusão por função/lote, taxa de abstenção e robustez à janela e à precisão. A unidade de generalização é a função ou lote, não cada linha tratada como independente.
- Alternativa: o acerto vem só da densidade, ou caracteres concordam nos n acessíveis e não podem ser distinguidos nessa resolução.
- Refutação: ganho sobre a referência ausente ou desaparecendo ao controlar metadados. A indistinguibilidade também é uma entrega matemática possível.
- Dependências: instrumento validado; modelo de remoção da densidade sem rótulo; família e custos definidos antes de novos zeros.
- Novidade não estabelecida. Busca específica por reconstrução de funções L a partir de zeros ainda insuficiente; não chamar isto de lacuna encontrada.

## P-R3 — correções de altura finita (ligação com H-001)

**Pergunta:** uma previsão publicada, com parâmetros fixados analiticamente, explica a evolução de uma estatística em novas alturas melhor do que o limite assintótico e o controle matricial finito usado?

H-001 já cobre essa direção. B3 propõe correções para espaçamentos; isso não fornece automaticamente previsão para K_c. Escolher uma única observável primária e conferir o domínio antes do teste. Não repetir a análise secundária já feita em m4 como descoberta.

Alternativas: efeito da janela/unfolding ou aproximação fora do domínio. Refutação operacional: resíduos excedem erro de estimação mais um resto teórico justificável. Sem controle do resto na faixa usada, o teste é de aproximação empírica, não refutação do resultado assintótico. Prioridade posterior; novos dados em altura adequada podem custar mais que os atuais.

## P-R4 — informação necessária para resolver estrutura aritmética (ligação com H-002)

**Pergunta:** qual fronteira entre largura em altura, posição, precisão e separação de linhas determina a recuperabilidade pelo nosso estimador?

B2 estuda uma tarefa e uma suavização específicas; não transportar seu expoente assintótico diretamente para Hann. Separar número de zeros, altura máxima, largura do bloco e espaçamento entre frequências. Trabalhar primeiro com sinais sintéticos conhecidos e intervalos de resolução; confirmar depois em espectros novos. FWHM não é um limite universal de todos os estimadores.

Uma possível entrega é um limite de identificabilidade ou uma comparação entre métodos sob a mesma informação e custo. Ajustar uma potência usando μ ≤ 148 não decide uma necessidade assintótica. O expoente atribuído à fonte deve ser corrigido antes da declaração: ver revisão do registro.

## P-C1 — simetrias de Collatz e informação que elas apagam (prioridade exploratória)

**Pergunta:** que observáveis aritméticas distinguem regras que a dinâmica simbólica trata como equivalentes?

Começar com T_a(x)=x/2 para x par e (ax+1)/2 para x ímpar, a=3,5, e separar os espaços positivos, racionais com denominador ímpar e inteiros 2-ádicos.

- Controle A: a conjugação do mapa 3x+1 com o shift está em B4. Reproduzir contagens simbólicas é B, não descoberta.
- Proposta D: filtros de integralidade/positividade ou pesos definidos independentemente da regra recuperam informação que a zeta simbólica simples perde. É preciso especificar qual informação e quais pares de mapas; diferenças triviais em ciclos já conhecidos não constituem novidade.
- Primeiro trabalho: CL0–CL1 já planejados, com períodos até 12; depois CL2–CL3, candidatos periódicos por frações exatas, canonicalização por rotações e comparação das assinaturas. Não enumerar milhões de órbitas sem essa base.
- Critério: uma assinatura proposta deve distinguir o conjunto declarado ou apresentar colisões explicitamente. Não inserir o valor de a como peso para obter classificação tautológica.
- Simetrias: estudar a autoconjugação de B5 como controle conhecido. Verificar quais espaços ela preserva antes de concluir algo sobre inteiros positivos; uma simetria 2-ádica não é automaticamente uma simetria dos positivos.
- Limite: ciclos e traços não registram todos os transientes. Não identificar ausência de ciclo novo com convergência de toda órbita.
- Ponte possível com Riemann: um exemplo rigoroso de não identificabilidade orienta o que uma reconstrução espectral precisa medir. Isso é uma lição sobre o problema inverso, não equivalência entre conjecturas.

## P-C2 — simetrias e transientes além das contagens periódicas

**Pergunta:** observáveis adicionais, definidas antes da simulação, distinguem comportamentos transitórios que os traços periódicos não distinguem?

Candidato: distribuições de primeira passagem e de escape em aproximações abertas, com amostragem e censura explícitas. Comparar a=3 e a=5 sem declarar divergente uma órbita que excedeu orçamento. Toda afirmação sobre espectro de operador deve fixar espaço, medida, domínio e fronteira; testar estabilidade antes de interpretar autovalores.

B6 é contexto: seu resultado de densidade logarítmica não é um modelo pronto para uma simulação uniforme finita. Um padrão empírico deve superar mudanças de fronteira, amostragem e truncamento. Falha nessas verificações encerra a interpretação espectral, mesmo com figuras convincentes. Prioridade posterior a P-C1.

## Propostas que não iniciar agora

- **Provar RH a partir de zeros na linha:** esses dados não testam zeros excluídos por construção.
- **Calcular mais coeficientes de Li:** B8 já trata o tema; um número finito de verificações não cobre todos os índices. Só retomar com novo alvo analítico e controle de restos.
- **Ajustar Hamiltoniano aos zeros:** exigir previsão independente e definição matemática antes de otimização; H-003 não é achado C.
- **Buscar picos parecidos em Collatz e ζ:** sem mapa e observável que conectem os sistemas, sem hipótese discriminante.
- **Conjecturas antigas sobre pontos fixos da conjugação:** B4 contém propostas específicas, mas seu estado atual não foi estabelecido nesta busca. Fazer busca por citações antes de tratá-las como abertas ou investir em enumeração maior.
