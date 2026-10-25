# T008 — Concentração, colisões e regularidade de Syracuse

**Limite de custo em25/10:** [subaditividade, barreira combinatória e potencial](SYRACUSE_LIMITE_CUSTO_20261025.md). Nenhum bloco de1–4 passos poderia atingir custo máximo2r por cardinalidade; assintoticamente a barreira fica abaixo de2. Potencial de amortização formulado, não construído. A fonte de Wirsching exige ainda minorante relativa à média: cobertura não basta.

**Cobertura uniforme em25/10:** [política inversa e prova por indução](SYRACUSE_COBERTURA_UNIFORME_20261025.md). Todas as unidades são atingidas para3n+7<=S<=2*3^{n-1}+n-1, n>=4. Certificado finito exato e três testes concluídos; a faixa central2n+O(sqrt(n)), a revisão independente e a novidade continuam abertas. Próximo alvo: custo mínimo de políticas inversas e comparação bibliográfica.

**Complementaridade em20/10:** [três parcelas, período e preenchimento de custos](SYRACUSE_COMPLEMENTARIDADE_20261020.md). Duas parcelas não bastam universalmente na grade; o período completo é caro para o custo central. Uma injeção reduz a cobertura em vários custos a um custo inicial, ainda não provado.

**Semente completa em20/10:** [limite de prefixos4 e identidade de5](SYRACUSE_SEMENTE_COMPLETA_20261020.md). O catálogo máximo local não cobre todos os pais completos. Uma identidade com transferência de custo atravessa essa restrição; próximo alvo: complementaridade dos conjuntos de filhos ausentes.

**Disponibilidade em20/10:** [recorrência e contraexemplo central](SYRACUSE_DISPONIBILIDADE_20261020.md). A família H não aparece em todas as classes no caso ell8/S16; identidade local preservada. Disponibilidade eventual e famílias complementares permanecem abertas.

**Último dígito em19/10:** [família explícita de blocos de três](SYRACUSE_ULTIMO_DIGITO_20261019.md) preenche os três filhos preservando custo e classe grossa. Falta controlar a disponibilidade dessa família por classe; a identidade foi selecionada na exploração declarada.

**Reescritas em19/10:** [identidade dos três filhos e correção de ordem](SYRACUSE_REESCRITAS_CUSTO_20261019.md). Folga bilateral num par dá minorante local com multiplicidade3; a massa com folga por classe segue aberta. O último dígito exige mais que uma transferência adjacente.

**Cobertura formulada em19/10:** [critério por filhos](SYRACUSE_COBERTURA_CRITERIO_20261019.md), ainda não provado; identificada a limitação de prefixos variáveis com sufixo fixo. Próximo alvo: reescritas que preservem custo e limites.

**Atualização 19/10:** [energia condicionada ao custo](SYRACUSE_ENERGIA_CONDICIONADA_20261019.md): Energia(E)<=4/beta² para custo fixado, e O_C(ell) na janela central com os limites do projeto. Auditoria do antecedente e dois testes exatos concluídos; cobertura e novidade continuam abertas.

**Atualização 18/10:** recorrência de energia/correlação cruzada derivada e conferida exatamente em K≤4; [obstrução L² e limite inferior de crescimento](SYRACUSE_COLISOES_20261018.md). A obstrução L² tem antecedente bibliográfico identificado. Fechamento por majorante e transferência ao custo continuam em execução; o estado inicial abaixo é histórico.

15/10/2026. Conexão **D**. Primeiro alvo `pendente`; novidade não estabelecida. Extensão concreta de T004, sem nova enumeração.

**Intuição:** uma distribuição pode parecer espalhada e ainda concentrar massa em conjuntos muito pequenos. Queremos medir essas concentrações em vez de exigir desde o início uma estimativa uniforme em cada resíduo.

## Objeto já definido

Usamos a estacionária π em Z₃ e suas projeções π_K, conforme [a nota de regularidade](../hipoteses/COLLATZ_REGULARIDADE_PI_20261012.md). Sua identificação com a lei de Syracuse de Tao e suas hipóteses permanecem as da nota. Não é a distribuição de uma amostra arbitrária de órbitas positivas.

Com Haar μ de probabilidade, f_K=3^Kπ_K é constante nos cilindros. Definimos

    E_p(K)=∫f_K^p dμ=3^{K(p−1)} Σ_a π_K(a)^p,  p>1.

Para p=2, Σπ_K(a)^2 é a probabilidade de duas amostras **independentes da lei π** coincidirem módulo 3^K. A independência pertence à construção de duas cópias, não aos passos de uma órbita.

**Consequências elementares A:** pela projetividade e Jensen, E_p(K) não decresce. Se f é a densidade L¹ já derivada e f_K suas médias condicionais, sup_K E_p(K)<∞ equivale a f∈L^p. Uma direção usa Jensen; a outra usa convergência quase em toda parte das médias condicionais e Fatou.

Já existe no projeto a obstrução f∉L^p para p≥log3/log(3/2), vinda dos cilindros ao redor de −1. Ela é um limite superior, não a localização do verdadeiro limiar. Não propomos como novo o estudo de menor massa ou de regularidade em geral: há antecedentes de Tao e trabalhos posteriores a conferir.

## Alvo e possível falha

Escrever π=(D_*π+O_*π)/2, D(x)=x/2 e O(x)=(3x+1)/2. Para duas cópias, decompor a coincidência em DD, DO, OD e OO. O ramo O reduz a resolução efetiva em um dígito ternário, mas os termos cruzados guardam informação adicional.

**Alvo:** uma recorrência exata para E₂(K) e as correlações cruzadas necessárias, com todas as resoluções e normalizações explícitas. Depois decidir se existe um conjunto finito ou uma hierarquia controlável de observáveis que feche a recorrência.

**Pergunta D:** quais p>1, se houver, admitem energia uniformemente limitada? Não fixamos uma resposta. Se a hierarquia exigir cada vez mais correlações sem controle, isso localiza a dificuldade e impede anunciar uma lei de escala.

**Oportunidade posterior:** estender uma cota à distribuição condicionada ao custo usada no projeto. Uma cota para a estacionária não se transfere automaticamente ao condicionamento.

## Relação com Riemann

Em ambos os problemas, pesos grandes em eventos raros podem invalidar uma passagem de limite. A ferramenta comum seria controle de integrabilidade uniforme. Não foi construída correspondência entre cilindros 3-ádicos e pares de zeros, nem entre seus expoentes.

**Produto útil sem RH/Collatz:** uma cota de concentração ou um critério de fechamento para uma medida aritmética concreta. Antes de reivindicar lacuna ou novidade, revisar literatura posterior à fonte de Tao.
