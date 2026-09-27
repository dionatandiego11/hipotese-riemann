# EXP26-2 — ficha prévia de desenvolvimento

26/09/2026. **Estado: pendente.** Frente experimental principal após H-004. Versão documental para preparar o piloto; **não é declaração congelada nem autoriza abrir dados reservados**. Nenhuma simulação desta ficha foi executada.

## 1. Pergunta e duas afirmações distintas

**Mecanismo:** perdas concentradas em pares próximos podem ser discriminadas de outros mecanismos de omissão, usando somente o espectro observado e informação teórica disponível antes da perda?

**Valor adicional:** incluir informação espectral complexa melhora esse diagnóstico sobre uma referência que usa contagem e espaçamentos?

Distinguir as duas conclusões. Se a referência simples já separar os mecanismos e o espectro não acrescentar ganho, haverá um diagnóstico útil, mas não contribuição demonstrada do instrumento. Detectar uma suspeita não localiza necessariamente os zeros perdidos nem certifica completude. Não afirmar retrospectivamente que este diagnóstico teria evitado o D3 sem medir sua sensibilidade na escala das perdas reais.

## 2. Dados permitidos e unidade de avaliação

- Desenvolvimento e avaliação metodológica: cópias dos blocos antigos de ζ, classificados como T0; substitutos explicitamente declarados.
- Nenhum acesso ao Dirichlet reservado; valores de pares mencionados pelo usuário motivam o problema, mas não serão usados para escolher limiares. Aplicação futura ao Dirichlet exige encerrar H-004 e registrar seu estatuto exploratório nesta pergunta.
- Bloco original completo serve apenas para gerar a intervenção e avaliar a verdade. Diagnóstico recebe a lista degradada, bordas fixas e densidade teórica; não recebe lista original, máscara, número removido nem semente.
- A divisão entre desenvolvimento e avaliação é feita por bloco original **antes** de gerar máscaras. Todas as máscaras e mecanismos de um mesmo bloco ficam do mesmo lado. Nenhum espectro sintético pai aparece nos dois lados.
- Réplicas de omissão são independentes condicionalmente ao espectro pai quando geradas independentemente; não tornam blocos contíguos fisicamente independentes. Reportar desempenho por bloco e agregado, distinguindo incerteza das máscaras de generalização para outros espectros. Nenhuma alegação de confirmação física independente nos 100.000 zeros já vistos.

## 3. Intervenções propostas

Fixar A/B antes da intervenção e preservar seus pontos extremos para não confundir mecanismo com deslocamento da janela. Para cada severidade, igualar exatamente a quantidade de níveis removidos entre mecanismos:

| Modelo | Intervenção | O que controla |
|---|---|---|
| M0 | nenhum nível retirado | falso diagnóstico de perda seletiva (não certificado de completude) |
| MR | níveis interiores escolhidos uniformemente sem reposição | referência de retirada aleatória |
| MP | retirar ambos os membros de pares adjacentes próximos, sem sobreposição | mecanismo seletivo motivado pelas falhas reais |
| MA | retirar pares adjacentes aleatórios, sem preferir distância | separar seletividade por proximidade de simples remoção em grupos de dois |
| MJ | retirar uma sequência contígua de níveis interiores | lacuna localizada |

**Em k=2:** MA e MJ representam o mesmo mecanismo quando a escolha dos índices e as bordas são iguais. Unificar as etiquetas; MJ separado somente para k≥6. Não computar erro de classificação entre leis idênticas.

Não fixar “perda seletiva” como remover sempre o mesmo menor espaçamento: isso eliminaria a variabilidade entre máscaras e estreitaria demais a hipótese. A distribuição de seleção em MP e a regra de não sobreposição serão expressas por algoritmo antes da geração. Serão comparadas com a regra da varredura real, sem ajustar aos resultados reservados. MR é a referência mais próxima das hipóteses de Bohigas–Pato; as demais não herdam suas fórmulas.

**Escala proposta para o piloto:** blocos de 3.000 níveis, remoções pares {2, 6, 12, 30}; começar pela escala mais esparsa, sem presumir que seja identificável. Estas escolhas são propostas, não poder medido. Eventual conclusão deve indicar exatamente em quais escalas houve sensibilidade; não usar sucesso em 30 remoções para prometer diagnóstico de duas.

## 4. Referências obrigatórias e informação disponível

- **B0:** contagem observada comparada com contagem teórica, mais resumo de espaçamentos unfolded. Sem acesso à lista completa.
- **B1:** a mesma informação de B0 acrescida de resumos previamente definidos da transformada complexa/fator de forma. Modelo aritmético dirigido, se usado, é rotulado como tal.
- Mesma divisão de dados, severidades, orçamento de treinamento e regra de abstenção. Nenhum metadado do gerador pode indicar o mecanismo.
- Usar coordenadas de unfolding teóricas fixas como análise principal. Um recálculo da densidade a partir da lista incompleta será análise separada, declarada previamente, porque pode ocultar a perda.
- Escolher um algoritmo simples e um conjunto curto de resumos na etapa de desenvolvimento. Congelar versão, escalas, regularização, features, calibração e sementes antes da avaliação. Não experimentar vários classificadores no conjunto de avaliação.

## 5. Decisão a especificar antes da avaliação

O diagnóstico poderá responder MP, outro mecanismo ou abstenção. Não será obrigado a classificar um bloco sem informação suficiente.

**Primária proposta:** sensibilidade para MP à taxa máxima de falso diagnóstico seletivo de 5%, verificada separadamente sob M0, MR, MA e MJ e por severidade. Fixar o limiar no conjunto de calibração; medir erros no conjunto de avaliação. Usar limite superior de confiança, não só estimativa pontual, para afirmar controle de falso positivo. Intervalos simultâneos ou uma decisão primária única devem ser definidos antes da avaliação; não declarar controle global a partir de vários intervalos marginais de 95%.

**Valor adicional proposto:** diferença pareada de sensibilidade B1−B0 à mesma exigência de falso positivo. Um ganho mínimo de interesse e a incerteza apropriada devem ser fixados na declaração antes da avaliação. Não basta B1 superar o acaso.

**Saídas:** matriz de confusão incluindo abstenções; sensibilidade e falsos positivos por mecanismo, escala e bloco; diferença B1−B0; custo; falhas e casos indistinguíveis. Não somar máscaras como se fossem novos sistemas físicos.

**Leituras:** sucesso apenas no domínio declarado; insuficiência quando a precisão permite excluir a sensibilidade mínima escolhida; inconclusivo quando orçamento ou incerteza não permitem decidir. Se não houver ganho de B1, manter B0 como resultado e encerrar a alegação de benefício espectral.

## 6. Desenvolvimento em duas etapas

1. **Piloto metodológico T0:** definir seleção MP, observáveis e referência B0; obter benchmark pequeno e estimar a escala de separação. Congelar antes deste piloto quais dados são desenvolvimento. Os valores encontrados não serão relatados como avaliação confirmatória.
2. **Avaliação com procedimento congelado:** só após fixar os itens abaixo. Mesmos espectros T0 implicam avaliação de intervenções controladas; a separação por blocos não apaga seu histórico de consulta.

Itens obrigatórios ainda pendentes para a declaração de execução: lista/hash dos blocos e divisão; algoritmo MP; features e algoritmo B0/B1; número de réplicas por célula; sementes inteiras; regra de intervalos/dependência/multiplicidade; sensibilidade mínima e ganho mínimo; código/configuração; orçamento medido e retomada. Fechar esses itens antes de chamar esta ficha de pré-registro.

**Teto proposto para o piloto:** 0,5 hora-CPU acumulada, sem ampliar automaticamente. Uma avaliação completa só recebe orçamento após benchmark. Transformadas podem aproveitar a linearidade em pontos fixos, mas qualquer atalho deve ser conferido contra recomputação direta; não confundir equivalência algébrica com tempos já medidos. Não iniciar os ensembles completos de m4 como padrão automático.

## 7. Escopo científico

O antecedente é Bohigas–Pato, *Missing levels in correlated spectra*, e a nota B14. A hipótese específica é discriminação de mecanismos de perda sob acesso restrito à informação, especialmente pares próximos. A novidade depende de busca adicional sobre thinning dependente de espaçamentos e níveis não resolvidos. A ficha não muda C1–C3, não explica por si só a rejeição de GUE em ζ, não elimina validações de completude e não gera evidência para RH.

## Revisão antes do piloto — 26/09/2026

A [nota de viabilidade](EXP26_2_REVISAO_VIABILIDADE.md) precede o piloto: inclui a interferência em ΔK_c, delimita o experimento bayesiano de uma lacuna, distingue V1 de contagem certificada e propõe conta sintética sob teto de 600 s-CPU. Nenhuma conta foi executada. Falta a declaração curta com escolhas e critérios fechados. O resultado terá escopo restrito ao ensemble e às features avaliadas.

Possível objetivo posterior: ordenar reexames por recuperação em orçamento de CPU, comparando D3, largura normalizada e escores locais/espectrais. Não chamar uma regra de ótima sem demonstração. A nota descreve métricas e limites; essa mudança ainda não é protocolo de execução.

## Conta sintética concluída — 26/09/2026

A conta curta posterior está no [relatório](../results/exp26_2_viabilidade_20260926/RELATORIO.md): 120 pais GUE, 113,25 s-CPU na execução concluída. Pela regra declarada, parar esta versão B1 em k=6/30; inconclusivo em k=2/12. Nenhuma autorização de avanço científico ao piloto completo. O estudo local não é teto bayesiano. O piloto T0 desta ficha continua não executado.
