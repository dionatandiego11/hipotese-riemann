# EXP26-2 — conta sintética de viabilidade, 26/09/2026

**Resultado: nenhum caso autorizou avançar com B1 pela regra declarada.** Para k=6 e 30, parar esta versão no ensemble GUE; para k=2 e 12, inconclusivo. Classe B, exploratória. Não é demonstração de ausência de informação espectral.

## Execução e escopo

Declaração e código congelados antes da geração. Foram gerados 120 espectros pais GUE independentes, com 3.000 níveis centrais cada: 40 para desenvolvimento, 40 para calibração e 40 para avaliação. Oito máscaras por mecanismo e severidade em cada pai; máscaras não contam como espectros independentes. MA remove pares adjacentes aleatórios; MP restringe a escolha ao décimo inferior dos espaçamentos. Nenhum zero real ou reservado foi lido.

B0 usa 11 resumos dos espaçamentos. B1 acrescenta 24 resumos espectrais (módulo e partes real/imaginária), com classificador logístico fixado. Não representa todos os métodos locais ou espectrais possíveis. Limiares calibrados visando 5% de falsos positivos. Intervalos pontuais de 95% por bootstrap de pais na avaliação, condicionais ao modelo e limiar treinados; não incluem incerteza do treinamento nem cobertura simultânea.

## Resultado por severidade

| Níveis removidos | Sensibilidade B0 | Sensibilidade B1 | Falso positivo B0 / B1 | Ganho B1−B0, IC95 (p.p.) | Regra |
|---|---:|---:|---:|---:|---|
| 2 | 3.44% | 7.81% | 2.50% / 7.50% | 4.38 [-0.62; 10.00] | inconclusivo |
| 6 | 10.31% | 6.88% | 3.75% / 3.44% | -3.44 [-8.12; 1.25] | parar esta versão B1 |
| 12 | 11.25% | 14.69% | 2.19% / 5.00% | 3.44 [-5.00; 12.81] | inconclusivo |
| 30 | 27.19% | 19.38% | 3.12% / 3.75% | -7.81 [-16.56; 0.94] | parar esta versão B1 |

Ganho mínimo declarado: 5 pontos percentuais. Parar quando o extremo superior do intervalo do ganho fica abaixo disso. Avançar exigiria extremo inferior acima de 5 pontos e extremo superior do falso positivo de B1 ≤5%. Nenhum caso atende. Os falsos positivos realizados diferem: estes ganhos são os dos procedimentos calibrados, não diferenças a uma mesma taxa efetiva de falso positivo. Não recalibramos usando a avaliação.

## Conta do fator de forma e da lacuna

Para k=2, o RMS da mudança de K foi 0,03335 (MA) e 0,02586 (MP), praticamente igual ao RMS da interferência. O termo quadrático médio foi 0,000738 e 0,000580. Portanto k/N não descreve sozinho a alteração realizada. O desvio padrão mediano por bin do espectro completo foi 0,774; o desvio da média em frequências foi 0,0820. São diagnósticos pareados, não entradas que revelam o espectro original ao classificador. A matriz de correlação está exportada; seu posto efetivo amostral não é uma estimativa certificada de bins independentes.

O discriminador histográfico da lacuna, recebendo sua localização verdadeira, teve acurácia com classes equiprováveis de 55,47% [52,19%; 58,91%]. No limiar calibrado: sensibilidade 3,125% e falso positivo 0,625%. A discretização cria empates e um limiar conservador. Este discriminador estimado não é o Bayes ótimo e não limita o B0 completo. Não calculamos um teto informacional.

## Verificações, custo e falha preservada

As oito comparações de atualização linear contra recomputação direta passaram: maior diferença absoluta 5,11e-15, abaixo de 1e-9. Os oito ajustes convergiram; contagens, ordenação, extremos preservados e máscaras sem sobreposição foram verificados durante a execução. Após a execução, os sete hashes do lock coincidiram e os arrays completos têm dimensões esperadas e valores finitos.

Execução concluída: 113.248 s-CPU e 113.937 s de parede medidos pelo script (parede exclui importações). Um thread medido durante a geração. Teto original 600 s-CPU. A primeira tentativa falhou na importação de threadpoolctl, antes de qualquer espectro; está preservada em tentativa1_importacao/. O adendo técnico trocou a inspeção de threads por /proc, sem instalar dependências nem mudar o desenho. Seu custo não foi medido separadamente: reservados conservadoramente 10 s, com limite da execução corrigida de 590 s. Não se apresenta 113 s como total exato de todas as tentativas.

## Decisão e próximo passo

Conta concluída; decisão científica de avanço inconclusiva em k=2/12 e negativa para o ganho mínimo desta versão em k=6/30. Não ampliar amostra, mudar features ou iniciar automaticamente o piloto completo. O resultado não exclui métodos aritméticos dirigidos, nem demonstra impossibilidade de localizar perdas.

Se esta frente continuar, a pergunta operacional adequada é recuperação por orçamento de reexame: comparar ordenação D3, largura normalizada e um escore local, contabilizando custo do diagnóstico e do reexame. Exige ficha própria, custos e avaliação separados; não foi implementada aqui. Não há economia de CPU demonstrada nem novidade estabelecida. Esta entrega não altera a decisão mais recente do ANDAMENTO de adiar H-004 e priorizar VN-1.

Artefatos: DECLARACAO.md, ADENDO_TECNICO_1.md, lock.json, executar.py, resumo.json, pais.json, sinteticos_resumos.npz, correlacao_bins_avaliacao.npy e execucao.log. Fonte científica nova: src/riemann_spectra/loss_viability.py. Sem commit.
