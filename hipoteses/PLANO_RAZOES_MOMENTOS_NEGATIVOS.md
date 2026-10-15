# Plano prioritário — razões e momentos negativos

13/10/2026. Orientação de Andrew comunicada pelo usuário: recuperar os
termos principais de C7/C8 e investigar os inferiores. Este plano substitui
como prioridade a expansão de volume e as rotas especulativas Collatz–RH.
Não abandona os resultados preservados de Collatz nem muda protocolos MN.

| Etapa | Entrega e critério | Estado |
|---|---|---|
| R0 — auditoria | Conferir fonte, domínio dos shifts e limite da Etapa B. Preservar original e corrigir afirmações sem suporte. | validado no escopo da auditoria interna; erro e ausência de inferiores retirados |
| R1 — regularização | Identidade local com fatores π/2π, extremos e polo auxiliar de C8. Controles artificiais sem zeros reais. | validado por derivação; controles B passaram |
| R2 — aritmética | Diagonais, resíduos κ7/κ8 e partes finitas B7/B8 com fatores p|q. Não confundir com inferiores discretos. | validado no escopo algébrico; conferência B |
| R3 — previsão completa | Receita geral sem limite ilegítimo de shifts de numerador; C8 trata altura2t. Reter resto/termos duais até extrair coeficiente singular no deslocamento. | em execução: formulado, cálculo completo não concluído |
| R4 — inferiores | Identificar a primeira escala subprincipal sobrevivente ao limite, explicitando suavização, condutor e hipótese de uniformidade. Não supor T/logT ou sua ausência. | pendente deR3 |
| R5 — confronto | Congelar previsão antes de comparar; dados já vistos serão exploratórios. Registrar peso dos pares próximos, extremos e influência das maiores parcelas. | pendente deR4 |

## Alvo matemático de R3

Para F=L e H=1 ou L(2s,χ²), primeiro fixar q e uma janela positiva,
com peso suave se necessário. Seja a média regularizada I_j(T,ε) e sua
diagonal D_j(2ε). Buscar uma expressão completa para

    lim_{ε↓0} ε[I_j(T,ε)−diagonal],

ou uma estimativa num regime conjunto ε=ε(T) que permita passar ao
momento discreto. Separar o polo na origem de C8 e as semimassas de
extremos quando presentes. Hipóteses devem declarar GRH, simplicidade,
faixa de shifts e se o condutor é fixo; uniformidade q≤T^A é objetivo
posterior, não implícito no caso fixo.

A parte finita da diagonal serve para diagnosticar a regularização, não
para preencher automaticamente uma tabela de termos inferiores.

## Dependências bibliográficas

- PC2026, C7/C8 e séries(1.1)/(1.2): conferidas no PDF arquivado.
- CS2007, Conj2.1, (2.11), Remark2.2: conferidos visualmente; não autorizam
  uniformidade até shift0 para uma média sem numerador correspondente.
- CFZ2007v1, receita geral(5.12)–(5.15): lida de forma dirigida. Especialização
  com conjuntos vazios deve ser explicitada; não estende por si a uniformidade.
- BGM2013v1, HKO e fórmula híbrida: introdução e enunciados iniciais lidos;
  derivação completa não auditada. Modelo apoia constantes, não elimina
  a necessidade de termos inferiores para o problema atual.
- Literatura2025 de Hughes/Pearce-Crump sobre momentos complexos/mistos:
  registros primários consultados; leitura integral pendente antes de
  afirmar ausência ou novidade de uma fórmula.

## Regras de trabalho

Sem novo cálculo longo para esta frente até existir previsão discriminante.
Primeiro álgebra/contornos/fontes; testes pequenos medem erros de implementação.
Não ajustar coeficientes aos resultados MN. Não usar a aparência de estabilidade
para declarar O(√T). Os pares raros devem ser considerados explicitamente
nas limitações numéricas; bootstrap de uma amostra não certifica sua cauda.

A passagem de R3 para R4 exige uma expressão cujo domínio suporte o limite
usado. Se isso não puder ser fechado, registrar a conjectura adicional
necessária e o alcance do cálculo formal. Não declarar a pergunta resolvida
por reproduzir somente as duas constantes conhecidas.

Documentos atuais: `RAZOES_REGULARIZACAO_20261013.md`; artefatos em
`results/razoes_momentos_negativos_20261013/`. Rascunho local v3 é revisão
interna, sujeita à revisão matemática do autor, sem envio/publicação nesta sessão.

## Continuação R3 — contornos e controle CUE (13/10/2026)

Derivados os resíduos de sinais opostos nos polos originais e deslocados: um contorno fixo que inclui ambos perde a contribuição desejada no limite. Recuperado exatamente o momento negativo CUE, para todo N≥1, por razões (CFZ Teorema4.1) e cálculo independente com Vandermonde. As correções em deslocamento não são correções em N.

Nota: `RAZOES_CONTORNOS_CUE_20261013.md`. Controle B:14 testes, CPU4,258s; primeira falha de teste adicional preservada e corrigida por adendo. Nenhum zero real. R3 permanece `em execução`: falta transportar o cálculo para L com controle do coeficiente singular do resto; C8 mantém a dependência em altura2t. Nenhum termo inferior de L foi declarado calculado.

## Continuação R3 — primeira correção local (13/10/2026)

Derivada em janela fixa a expansão C±(ε)=S+ε[FP/π±2ΣRe(a conj b)]+O(ε²), com parte finita definida e hipóteses locais. A simetrização não elimina a contribuiçãoFP. Duas escalas cancelam o termo linear, mas não fornecem uniformidade em separações/altura e podem ultrapassar o alvo. A parte constante do resto da diagonal também foi identificada como objeto, sem ser estimada paraL.

Nota: `RAZOES_PARTE_FINITA_LOCAL_20261013.md`.18 testes passaram; CPU7,769s. R3 segue `em execução`, R4/R5 não liberadas. Próximo trabalho continua sendo a previsão do coeficiente singular do resto de razões com domínio uniforme; não usar correções emε como inferiores emT.

## R3 — ponte discreta e recuperação formal deC7/C8 (13/10/2026)

A leitura deHughes–Pearce-Crump2025 delimitou momentos complexos e método para inteiros não negativos. Construída uma identidade exata de contagem ponderada porF'/F, com ordemν→0 antes deε→0. Sua diagonal formalDjPj tem poloκj/(2ε²), recuperando as duas constantes principais. Isto é cálculo formal da receita, não estimativa uniforme da média.

O controleCUE de razões nos autovalores fornece1+(N−1)tanh(ε/2). Uma escolhaε=c/N conserva viés principal; a primeira correção de matrizes fixas também não comuta com a esperança, por falta de uniformidade em separações. Nota: `RAZOES_DISCRETAS_MOMENTOS_NEGATIVOS_20261013.md`.

R3 permanece `em execução`: próximo alvo é a média COMPLETA do gerador, com termos duais/bordas e controle dos dois deslocamentos. A hipótese que controla o resto foi explicitada e não presumida. R4 ainda não liberada. Não expandir controles locais como substituto dessa tarefa.

## R3 — geradores completos da diagonal e domínio do erro (13/10/2026)

Fechada a álgebra deG7=Y7A7 eG8=D8(a+b)D7(v+b)/D7(u+b). A média completa deL NÃO está fechada: suas demais contribuições ficam no restoRj. A hipótese suficiente agora é explícita em círculos complexos de raioηε emu: ε sup|Rj|≤M(T), uniforme nos deslocamentos indicados. Cauchy dá erro de momento≤M(T)/(πη). M(T) não foi estimada; nenhuma taxa emT foi adotada.

Nota: `RAZOES_GERADORES_UNIFORMIDADE_20261013.md`.26 testes passaram; nenhum zero real. A justificativa para deslocamentos pareados não basta no círculo fora do pareamento. Próximo trabalho: decompor e estimar o resto da média real, primeiroC7, q fixo. R3 `em execução`, R4/R5 pendentes. Não ampliar testes algébricos sem uma nova necessidade: as verificações atuais passaram.
