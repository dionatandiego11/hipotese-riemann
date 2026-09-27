# Plano de trabalho — dependências aritméticas e transientes de Collatz

**Data:** 25/09/2026. **Estado:** em execução apenas quanto à preparação documental; revisão dirigida e pesquisa matemática pendentes. Plano solicitado pelo usuário, não protocolo experimental congelado. Nenhuma enumeração autorizada por este documento isoladamente.

## 1. Objetivo e resultado procurado

Identificar uma dependência aritmética específica que um modelo probabilístico de Collatz perde e formular uma consequência quantitativa verificável. O resultado desejado é uma identidade, desigualdade ou previsão com domínio e erro explícitos. Uma equivalência com um resultado conhecido ou uma impossibilidade de identificação também encerra legitimamente uma candidata.

**Alvo principal:** decompor e controlar a dispersão das árvores inversas através das dependências entre palavras de ramos. **Alvo secundário:** verificar que informação adicional seria necessária para controlar transientes diretos. Não abrir os dois como campanhas numéricas simultâneas.

Esta frente é independente da validação espectral e de H-004. Não usa zeros, primos do catálogo, arquivos reservados ou processos em execução. Não afirma prova de Collatz, RH ou ligação entre as conjecturas. Por nova solicitação do usuário, a busca de uma ligação direta foi incluída no [roteiro específico](PLANO_PONTE_DIRETA_COLLATZ_RIEMANN.md); este plano fornece sua base de dependências e transientes.

## 2. Convenções e restrições

Usar T(n)=n/2 para n par e T(n)=(3n+1)/2 para n ímpar, nos inteiros positivos. O ciclo conhecido é {1,2}. Não misturar essa unidade de tempo com o mapa ímpar-a-ímpar de Syracuse.

Distinguir três medidas: uniforme em um conjunto finito de inteiros iniciais; uniforme nas classes invertíveis módulo uma potência de 3; Haar no espaço 2-ádico. Um resultado sob uma delas não é automaticamente válido sob outra. A conjugação ao shift não torna trajetórias positivas finitas uma amostra de moedas independentes.

A [CL0](../results/collatz_cl0/README.md) e sua [errata](../results/collatz_cl0/ERRATA_CL0_1.md) são a base de convenções. Seus arquivos congelados não serão modificados. CL1 permanece não executada. O presente roteiro prioriza leitura e formulação antes da implementação CL1–CL5; não altera suas declarações. Código eventual fica em `collatz/`, sem importar `riemann_spectra`.

## 3. Revisão dirigida: perguntas que cada leitura deve resolver

| Núcleo | Fontes do acervo e pistas seguintes | Questão da revisão |
|---|---|---|
| Codificação | Bernstein–Lagarias; Monks–Yazinski | O que a conjugação preserva e o que não transporta para os positivos? |
| Árvores e dependência | Applegate–Lagarias, *The Distribution of 3x+1 Trees*, §§2, 5–6; Lagarias–Weiss, §§3–4 | Quais momentos, covariâncias e dependências entre ramos já foram calculados? O que é provado para a árvore real e só para o modelo? |
| Estado posterior | Kontorovich–Lagarias; Wirsching e trabalhos que citam as fontes anteriores | A função limite 3-ádica, sua regularidade e as conjecturas extremas tiveram avanços? Estado atual ainda a verificar. |
| Operadores | Leventides–Poulios, §§4–6 | Que afirmações espectrais são apenas reformulações de crescimento de pré-imagens já conhecido? |
| Transientes | Lagarias–Weiss; Kontorovich–Lagarias; Terras/Everett como pistas a obter; Tao | Quais distribuições, medidas e regimes de tempo têm resultados rigorosos? Onde a aproximação aleatória perde controle? |

As notas B11–B17 em `hipoteses/leituras/` são índices para as páginas, não substitutos da fonte. Não repetir como candidata nova: normas dos operadores, crescimento exponencial elementar das árvores, média (4/3)^k, diferença qualitativa entre extremos reais e do modelo, ou existência quase em toda parte da função limite já registrada.

**Método:** duas rodadas documentais delimitadas. Na primeira, ler os trechos diretamente pertinentes das fontes já arquivadas. Na segunda, seguir referências e citações posteriores somente para as lacunas identificadas. Registrar consultas, data, páginas, versões, hashes, hipóteses e falhas de acesso. Uma fonte inacessível deixa a afirmação pendente; não justifica presumir uma lacuna.

**Entregável proposto:** `hipoteses/collatz/REVISAO_DEPENDENCIAS.md` e tabela de evidências com campos `afirmacao`, `objeto`, `medida`, `quantificadores`, `fonte`, `pagina`, `leitura`, `hipoteses`, `estado_atual`, `consequencia`. Esses arquivos ainda não existem.

A busca de planejamento localizou a bibliografia de Lagarias e trabalhos recentes sobre tempos de parada; são pistas, não evidências técnicas lidas: https://websites.umich.edu/~lagarias/doc/3x%2B1bib.pdf e https://arxiv.org/abs/2603.04479 . Nenhuma alegação recente de solução ou recorde foi adotada.

## 4. Alvo matemático principal — dispersão de árvores inversas

### Objeto proposto

Seja N*_k(a) o número de nós na profundidade k da árvore inversa podada, retirando os nós divisíveis por 3, conforme a definição da fonte original. Conferir a equivalência exata dessa convenção antes da derivação. Seja A_k uniforme nas classes invertíveis módulo 3^{k+1} e

    X_k = N*_k(A_k)/(4/3)^k,     V_k = E[(X_k−1)^2].

A média usada na normalização é conhecida; demonstrá-la novamente é controle A/B, não alvo de novidade. A variação de A_k mede heterogeneidade entre raízes, não variabilidade temporal numa trajetória.

### Pergunta que deve ser decidida antes de enumerar

**É possível obter uma identidade ou cota explícita para V_k que isole uma dependência entre ramos ausente de um modelo de ramificação publicado, sem ajustar parâmetros a contagens novas?**

Plano de derivação, ainda não executado: representar N*_k(a) por soma de indicadores I_w(a) de admissibilidade de palavras inversas. Classificar as interseções de condições de congruência que entram em E[I_w I_v]. A expansão de variância em covariâncias é elementar; a candidata é uma redução ou estimativa não trivial dessas interseções, com quantificadores explícitos.

Não pressupor sinal negativo das covariâncias nem que a menor faixa de extremos implique menor variância. Não usar ramos independentes como referência sem definir uma distribuição compatível. Escolher **um** modelo B[3^j] da literatura, após conferir suas definições, e igualar raiz, profundidade, poda e normalização. O índice j será fixado antes de qualquer avaliação.

### Forma exigida do enunciado final

Uma destas entregas, escolhida antes do cálculo:

- identidade/recorrência exata para o segundo momento, com condições iniciais e prova;
- cota para uma classe declarada de covariâncias e para o resto, válida em profundidades especificadas;
- previsão quantitativa da diferença entre V_k real e do modelo, com intervalo ou resto declarado e sem ajuste ao conjunto de teste.

**Critério de continuação:** a revisão identifica a diferença em relação ao resultado mais próximo e a formulação produz uma consequência quantitativa. **Critério de encerramento:** resultado já conhecido, mera expansão tautológica, custo essencialmente equivalente à enumeração original sem ganho analítico, ou ausência de resto útil. Nesse caso registrar a candidata encerrada, sem ampliar k para procurar um padrão.

Não se afirma nesta entrega que o enunciado exista, seja verdadeiro ou esteja aberto na literatura.

## 5. Alvo secundário — o que se pode dizer sobre transientes?

Só avança após a decisão sobre o alvo principal; não depende de ele ter resultado positivo.

Fixar separadamente tempo de chegada H(n)=inf{j≥0:T^j(n)∈{1,2}} e tempo de saída E_N(n)=inf{j≥0:T^j(n)>N}. Para uma distribuição μ explicitamente suportada em {1,…,N}, propor

    S_{μ,N}(h) = Pr_μ[H>h e E_N>h].

Isso é sobrevivência antes de chegada ou saída no corte, não probabilidade de divergência. Guardar chegada, saída e esgotamento do horizonte como eventos distintos. Não pressupor H finito.

**Alvo:** antes de simular, derivar a identidade finita com o operador de transporte que mata trajetórias na chegada e na saída, e identificar quais dependências de resíduos impedem o fechamento de um modelo com memória finita. A identidade de transporte, sozinha, será controle conhecido. Uma contribuição candidata exigiria uma cota explícita para o erro na previsão de S_{μ,N}(h), em μ, N e h declarados.

Não transferir V_k para S_{μ,N} sem teorema que relacione os objetos. Não interpretar autovalores de um corte como espectro do operador infinito. Comparação com 5x+1 fica adiada; só entra se discriminar o mecanismo matemático escolhido.

## 6. Sequência de entregas e decisões

| Etapa | Entrega | Condição de saída | Estado |
|---|---|---|---|
| C-D0 | Este plano e vínculos à CL0 | Escopo e alvos definidos, sem resultados inventados | validado (documental) |
| C-D1 | Revisão dirigida e tabela de evidências | Separar conhecido, fonte pendente e pergunta candidata | pendente |
| C-D2 | Nota matemática de V_k e comparação com um modelo | Enunciado preciso, prova ou obstáculo localizado; decisão continuar/encerrar | pendente |
| C-D3 | Especificação dos transientes | Identidade finita e uma pergunta adicional à teoria conhecida | pendente |
| C-D4 | Declaração de um piloto, somente se houver alvo sobrevivente | Objetivo, cobertura, orçamento e interpretação negativa congelados | não executado |
| C-D5 | Piloto e decisão sobre extensão | Nenhuma ampliação automática; avaliar ganho científico | não executado |

A revisão/derivação não exige enumerar previamente CL1. Se houver implementação, listar quais controles CL1–CL4 são necessários; não ampliar silenciosamente o protocolo CL1 para testar a nova pergunta.

## 7. Regras para eventual computação

Esta entrega não inicia nem autoriza uma execução. A declaração futura deve fixar palavras/classes, profundidades, sementes quando aplicáveis, horizontes, dados de desenvolvimento e de teste, método exato e critério de parada. Uma varredura completa finita não precisa de significância estatística; um teste com amostragem precisa considerar a dependência e justificar a unidade de inferência.

Proposta de teto inicial: **0,5 hora-CPU acumulada**, incluindo controles e pilotos, sem extensão automática. Custo deve ser estimado antes. Se não couber, concluir “inconclusivo por orçamento”, sem trocar a pergunta depois de ver resultados. Execuções maiores continuam sujeitas ao adendo de custo e suas erratas; não exigir poder estatístico artificial para provar identidades exatas.

Para parâmetros selecionados na exploração, confirmação em profundidades/faixas diferentes não equivale a independência estatística. A validação analítica e a implementação independente têm papéis distintos. Arquivar configurações, hashes, custos e resultados negativos em diretório novo; nenhuma alteração dos artefatos congelados ou de H-004.

## 8. O que contará como avanço

Um lema novo após confronto bibliográfico, um limite útil para dependências aritméticas, uma previsão transferível para transientes ou uma obstrução demonstrada. Encontrar apenas o que as fontes já contêm é revisão concluída, não descoberta. A frente pode terminar legitimamente sem enumeração extensa.

**Próxima tarefa concreta:** C-D1, começando pelos segundos momentos e dependências em Applegate–Lagarias e Lagarias–Weiss, depois Wirsching e citações posteriores. Entregar a tabela de evidências e uma decisão sobre a viabilidade de C-D2 antes de escrever código.
