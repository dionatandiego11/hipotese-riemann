# Leitura da reconstrução de Adriazola e do resumo riemann-rev

Data: 26/11/2026. Esta nota completa a leitura textual da cópia de 287 páginas de Jimmie Adriazola, *The Alpöge proof of the Riemann hypothesis*, revisão `aa9c86bf2a7d29b08575641fecea19a2a603e87c`, SHA-256 `8ced945d3a2fcf7fb7a2a760db6859416cd8db2ed11617d8bc28b43b82ed3a94`, e acrescenta a leitura integral do resumo de quatro páginas de riemann-rev, *The condensed Lean proof of RH and GRH*.

A leitura percorreu o texto e as referências, incluindo a montagem final; não é uma verificação independente linha a linha das demonstrações, das citações ou do código Lean. A extração automática não preserva perfeitamente todas as fórmulas; uma auditoria de um enunciado específico deve consultar a página do PDF. Nenhuma execução Lean ou validação computacional das provas foi feita por nós. As conclusões abaixo são atribuições às fontes, não teoremas certificados pelo projeto.

## O novo resumo e sua procedência

O resumo consultado em [nasqret.github.io](https://nasqret.github.io/riemann-rev/summary/grh-condensed-summary.pdf) foi arquivado em `archive/leituras/nasqret_20261126/grh-condensed-summary.pdf`, SHA-256 `9656c8dbd5efb3da174425e738f4f7075dc78957eb9201090bfc36f31d70ad3d`. A cópia obtida do repositório riemann-rev na revisão `4a3e744875df72d810e8650413409c0fc9cf404a` tem o mesmo hash. O resumo declara examinar o repositório [lsernau/grh-lean](https://github.com/lsernau/grh-lean) na revisão `72fead102f663d5c7a407964a13dc0cf9d977207`. A data registrada no PDF é 26/11/2026.

Segundo o resumo, a versão condensada apresenta formalizações da hipótese de Riemann e da hipótese generalizada para funções L de Dirichlet. O resumo relata aceitação pelo kernel Lean, checagens adicionais e CI comunitária; relata também que sua própria reprodução estava em andamento e que a prova ainda não havia sido lida integralmente por matemáticos. Essas são informações da fonte na data e revisão indicadas: não repetimos essas verificações. O repositório comunitário mantém seu próprio estado em [leanprover-community/riemann-hypothesis](https://github.com/leanprover-community/riemann-hypothesis).

O resumo distingue a parte de resultados gerais (`Lib`) da parte específica (`New`) e apresenta três blocos: formas curtas, existência de formas suficientes e limite inferior para formas integrais. A comparação superior/inferior de covolumes cancela um termo principal; a economia atribuída a uma cadeia de aproximadamente √x passos entra na redução analítica. O resumo também ressalta que a edição condensada usa uma rota diferente da reconstrução original para um dos insumos cohomológicos. Portanto, a correspondência entre itens das duas exposições deve ser estabelecida pelo enunciado e pelas dependências, não presumida pelo nome.

## Mapa da leitura de Adriazola

| Seções e páginas | Conteúdo e dependência |
| --- | --- |
| 1–2, 4–10 | Programa e critério analítico em janelas para somas com positividade; é essencial a uniformidade na janela e em escalas arbitrariamente grandes. |
| 3–6, 11–44 | Sete desigualdades, média positiva de pesos, escolha de caracteres e primos auxiliares e redução do Teorema A a uma região livre de zeros. |
| 7–11, 45–105 | Modelos theta/Fock, divisibilidade local, composição e dados da cadeia. A construção exige normalizações e hipóteses N1–N3; nem todas são demonstradas no texto. |
| 12, 106–145 | Perdas e não degenerescência dos operadores de Hecke. A Hipótese 12.12 agrupa passos individuais ainda pendentes na exposição; o Teorema 12.54 prova uma peça posterior, de modo que não se deve classificar todo o capítulo como simplesmente aberto. |
| 13–14, 146–207 | Reticulados, Gram, inclinações e quase ortogonalidade. Os resultados são condicionados às hipóteses enunciadas; a Hipótese 14.61 reúne dados de pré-traço que o autor não prova ali. |
| 15, 208–240 | Normas, alturas e covolumes. A prova do Teorema 15.66 assume 15.69 e os insumos I1–I17; o autor informa que a construção da torre, a identidade exata nos primos bons e a passagem ao limite para 15.69 não estão escritas nessa versão. |
| 16, 240–246 | Contabilidade dos termos locais. O Teorema 16.6 é condicional às estimativas E1–E6; as Hipóteses 16.13 e 16.14 não são demonstradas no texto. |
| 17, 247–269 | Congruências, grupos de Selmer e lugares torcidos. As estimativas 17.11 e 17.24, bem como partes da passagem a representações e módulos de congruência, são hipóteses da exposição. |
| 18, 269–282 | Dados admissíveis e montagem. A prova de 18.6 assume 17.11 e 18.10; a p. 277 declara que a compatibilidade exata das constantes de 18.10 ainda não foi verificada linha a linha no manuscrito. A p. 282 declara que a implicação final permanece condicional às hipóteses listadas. |
| Referências, 282–287 | Bibliografia; seus enunciados e sua aplicabilidade não foram conferidos integralmente por nós. |

O texto apresenta na §17.4.3, pp. 260–262, um argumento alternativo para uma estimativa efetiva em cohomologia, com constante explícita proposta. O próprio autor diz que essa alternativa não foi formalizada em Lean e aguarda verificação humana independente. Não é correto atribuir automaticamente essa alternativa à prova formal original.

Na §17.4 o autor estuda uma consequência condicional na direção da conjectura de Vandiver: uma hipótese de controle dos grupos envolvidos implicaria anulações em certas componentes de grupos de classes sob condições adicionais. Não é, por si, uma demonstração incondicional de Vandiver.

## O que esta leitura permite concluir

1. A exposição convencional arquivada tem lacunas e hipóteses que o próprio autor identifica. Isso não estabelece uma falha no desenvolvimento formal, que é outro artefato e tem de ser examinado separadamente.
2. Um resultado relatado como verificado por máquina depende de conferir o enunciado formal, as definições e a base de confiança; uma prova legível por humanos e a comparação das fontes são tarefas adicionais. Não verificamos essas etapas.
3. O mecanismo útil para nosso estudo é o controle de famílias e de erros ao compor etapas. Uma cota média de Gram, isoladamente, não dá cota inferior uniforme do menor autovalor: `diag(0,1,…,1)` ilustra a perda de uma direção apesar da média próxima de 1. A nota `LEITURA_ADRIAZOLA_20261124_CADERNO_01.md` registra a análise local.
4. Não encontramos no que foi lido uma construção de Hamiltoniano auto-adjunto com os zeros de ζ como espectro, nem uma ponte demonstrada entre Collatz e Riemann. A aplicação de ideias de uniformidade às famílias de ramos de Collatz permanece uma proposta, não consequência dos textos.

## Próximo trabalho delimitado

- Conferir o enunciado formal e as dependências de uma peça pequena da edição condensada, fixando revisão e distinguindo o que é importado em `Lib` do que é provado em `New`.
- Se o objetivo for Collatz, enunciar primeiro um problema próprio de composição de operadores, espaços, pesos e uma estimativa uniforme; comparar depois sua estrutura com a técnica lida. Nenhuma transferência é automática.
- Para o Hamiltoniano, exigir domínio, auto-adjunticidade e uma identidade espectral ou de traço demonstrável, antes de interpretar matrizes numéricas como operador físico.

Este registro atualiza o escopo indicado na nota anterior `LEITURA_ADRIAZOLA_20261124.md`, que descrevia apenas uma leitura dirigida; não modifica seus registros históricos.
