# Declaração de auditoria documental e verificação limitada

Data de trabalho: 2026-10-07. Commit fixado: adc7f1241b42e322a6451854ab7e4b4c146bf78a.
Alvo: família 003, região Re(s)>7/8, prova de ζ e dependências; alternativa 11/12 e exclusão Siegel como contexto. Não é teste de dados.
Escopo: arquivo por commit/hash; mapa de imports e hipóteses; leitura dirigida de manuscrito e pontos de ligação; preparação de verificação isolada; consequência condicional para cauda projetada.
Critérios: só relatar verificação formal se execução do verificador terminar com sucesso e enunciado/axiomas forem conferidos. Busca textual não certifica prova. Ausência de ferramentas ou dependência indisponível resulta em bloqueio documentado, não invalidação matemática. Não compilar toda a coleção nem instalar globalmente.
Orçamento da tentativa formal: no máximo 600 segundos-CPU acumulados (processo e filhos), uma execução serial, até 4 GiB de espaço adicional e 2 GiB de RAM; 15 min de parede como limite operacional separado. Primeiro medir dependências e ferramentas. Preparação/download de fontes: até 150 MB e 2.000 módulos próprios; se exceder registrar mapa parcial. Sem experimento científico nem leitura de zeros. Sem commit/publicação.
Leituras preliminares já vistas antes desta declaração: README, catálogo, alvo Comparator e configuração, Nonvanishing, FinalAssemblyUnconditional, Foundation, lakefile, manifest e toolchain. Não se declara auditoria cega.
