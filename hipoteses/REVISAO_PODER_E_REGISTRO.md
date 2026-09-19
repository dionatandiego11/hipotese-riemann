# Revisão da atualização recebida em 19/09/2026

Leitura do script `results/etapa11_6_controles/poder/analise_poder.py`, da análise, do adendo estádio 1 e do registro v2. **Não foram reexecutados cálculos nem alterados esses documentos.** A análise é útil para detectar critérios mal dimensionados; os pontos abaixo limitam a interpretação, não apagam os resultados.

## 1. Viabilidade por sinal/ruído não é ainda poder estimado

`power_block` gera um espectro substituto por chamada, estima σ e limiar por embaralhamentos e calcula `z_pred = abs(c)*W0/(2*sigma)`. Não injeta o sinal previsto em múltiplas realizações e não aplica o detector completo a essas alternativas. Portanto não estima P(critério passar | modelo), nem sua incerteza.

As 200 e 999 realizações são calibração interna. Não são 1.199 réplicas de sucesso do experimento sob a hipótese. O resultado atual é uma **triagem de detectabilidade baseada em um modelo substituto**. O teste com ζ prevê 13 linhas e observa 15; isso sustenta aproximação de escala, não contagem exata.

Recomendação para entrega seguinte: simular uma alternativa com sinal e fase previstos, em mais de um espectro substituto, incluindo localização na grade, seleção de picos, sobreposição, ajuste, elegibilidade e critérios conjuntos. Fixar efeito mínimo, número de réplicas e intervalo de incerteza antes do cálculo. Não prometer poder contra qualquer hipótese falsa: existem alternativas arbitrariamente próximas.

## 2. Nulo de embaralhamento e erro de coeficiente são objetos diferentes

A distribuição do nulo depende dos espaçamentos fornecidos, da janela, da grade, do condicionamento e da cadeia de estimadores. Um rótulo GOE/GUE/Poisson e uma densidade não determinam sozinhos o caso real. Similaridade em três comparações conhecidas é evidência de utilidade, não garantia de transferência.

A escala 1/z pode ser uma aproximação orientativa para ruído relativo, mas não é a variância do ajuste complexo demonstrada. Não conclui poder de amplitude, de sinais ou de ausência de linhas. Conjuntos elegíveis não vazios não garantem todos os critérios D-C*.

## 3. Estádio: explicitar a regra do bloco G

O bloco G pode melhorar a detectabilidade, mas z≈3,84 > 2,97 não significa sucesso certo ou probabilidade já medida. Também fica abaixo de 1,5×2,97. O adendo diz "detecção clara": explicitar se significa ultrapassar `z_high` ou cumprir a regra de elegibilidade 1,5×limiar. São regras distintas; não mudar uma para a outra após ver níveis.

A ausência de detecção, nesse regime, não refuta sozinha a amplitude física. A comparação de amplitude usa fórmula assintótica: separar erro de discretização, ajuste e resto teórico antes de interpretar uma falha de 10%.

Outro ponto de rastreabilidade: o texto relata G e uma combinação de 7.000 níveis, mas o `main` do script inspecionado monta apenas os blocos retornados por `stadium()` (n=3.000 por bloco). Localizar o comando/script específico e a saída que produziram as combinações antes de tratá-las como reproduzíveis pelo comando documentado. Isso não afirma que não foram executadas.

## 4. Precisões no registro de hipóteses

- **H-002:** a fonte B2, resumo e HTML §1, usa μ log^(3/2)μ, não μ log²μ. O regime do artigo não deve ser convertido automaticamente em lei para Hann. Corrigir o registro/CSV com nota de revisão antes de declarar o teste.
- **H-003:** uma classe de operadores ainda a triar não é achado C. Usar estado de proposta, deixando o rótulo científico dependente da afirmação concreta.
- **Collatz fora do instrumento:** isso é correto como escopo do registro espectral, mas não encerra sua utilidade para a frente CL. Manter registro separado de construção e testes próprios, como nesta pasta.
- **F5/J1:** o estado atual já registra avanços bibliográficos. Não transportar pendências históricas da revisão de 17/09 como se fossem o estado presente.

## 5. BH, dependência e versões futuras

O v2 propõe BH a 10% para todas as hipóteses confirmatórias na data de cada relatório. B9 chama atenção para hipóteses de dependência; não há aqui justificativa de independência/PRDS para os valores-p do projeto. Relatórios repetidos e uma família que cresce também exigem regra de uso para não converter inspeções sucessivas em garantia fixa indevida.

Antes do primeiro teste confirmatório, propor adendo que fixe família e encerramento e justifique o procedimento. Holm a 5% já aparece como análise complementar; pode ser considerado critério principal com valores-p válidos, ou estudar uma alternativa apropriada à dependência. Nada foi substituído retroativamente. Leitura integral da fonte estatística continua necessária para a escolha.

## Consequência prática

Manter a triagem atual e suas previsões como classe B/modelo. Completar a análise necessária para o critério primário antes de investir na produção do estádio; código e piloto de convergência continuam úteis. Não concluir que os dias de Dirichlet garantem sucesso: o controle é informativo precisamente porque pode falhar.
