# Investigação de uma ponte direta Collatz–Riemann

25/09/2026. Ampliação de escopo solicitada pelo usuário após o plano de dependências e transientes. **Entrega documental; nenhuma ponte nova demonstrada, nenhuma enumeração executada.** Este roteiro autoriza a formulação de perguntas ambiciosas, não a pressuposição das respostas. Não modifica CL0, H-004 ou critérios de validação.

## 1. O que procuramos

Uma relação matemática explícita entre uma construção determinada pela regra de Collatz e a função zeta de Riemann. Distinguir três níveis de sucesso:

1. **Relação funcional:** uma equação de Collatz tem ζ como solução ou se traduz em uma identidade de séries de Dirichlet. Já há antecedente localizado; reproduzi-lo é resultado conhecido, não descoberta.
2. **Relação com zeros:** demonstrar que zeros de ζ correspondem a uma propriedade definida independentemente no objeto de Collatz, com domínio e multiplicidades quando pertinentes.
3. **Consequência sobre localização:** provar uma restrição aos zeros a partir de propriedades demonstradas do objeto. Nem o nível 1 nem o 2 implica automaticamente RH. Qualquer uso de Collatz ou RH como hipótese deve permanecer explícito.

O objetivo de pesquisa é tentar chegar ao nível 2. Não temos evidência suficiente para conjecturar que a ponte desejada exista. Uma obstrução a uma classe concreta de construções será uma entrega útil.

## 2. Rota prioritária — Collatz em séries de Dirichlet

**Pista primária:** Günter Meinardus, *Some Analytic Aspects Concerning the Collatz Problem*, Mannheimer Manuskripte 261 (2001). O resumo institucional descreve um operador em um espaço de séries de Dirichlet e afirma que ter núcleo unidimensional gerado por ζ equivale à conjectura de Collatz. Isso é uma relação com ζ, não uma afirmação sobre RH.

Fonte: https://madoc.bib.uni-mannheim.de/1608/ . A busca apresentou o resumo e a primeira página indexada; a abertura atual e o download do PDF foram bloqueados (antibot/403). **Classe exata, hipóteses e demonstração não conferidas.** Registro em `archive/fontes_etapa11/ponte_collatz_20260925/aquisicao.json`. Não promover o resumo a teorema auditado.

**Atualização 25/09/2026 (P1 validado):** PDF obtido pelo usuário via Tor e lido; nota em [`leituras/B18_MEINARDUS_2001.md`](leituras/B18_MEINARDUS_2001.md). Confirmado o cenário da **Decisão** abaixo: ζ entra só como série da sequência constante, que é invariante sob **qualquer** mapa τ; a identidade Tζ = (1−2^{−s})ζ vale sem hipótese; os zeros de ζ não carregam informação de Collatz nessa construção. O objeto não trivial é o operador de composição a ↦ a∘τ (Koopman, cf. B11), de modo que a rota 1 converge para a rota 3. Citações posteriores continuam pendentes.

**Primeiro alvo:** obter a fonte, reconstruir a equação e verificar: domínio dos coeficientes; convergência; sentido de núcleo; tratamento de órbitas divergentes; equivalência alegada; continuação analítica. Procurar trabalhos posteriores que usem essa construção.

**Alvo de extensão:** perguntar se o operador fornece alguma informação sobre os zeros da sua solução ζ, além de identificar essa solução. Precisamos de uma identidade adicional demonstrável — por exemplo, uma relação entre invertibilidade de uma família dependente de s e o anulamento de ζ(s). O fato de ζ pertencer a um núcleo não fornece isso. Não fixamos essa relação como conjectura verdadeira antes da leitura.

**Decisão:** se ζ aparece somente porque uma sequência constante resolve uma equação que vale para uma ampla classe de mapas, registrar precisamente esse mecanismo e perguntar qual informação específica de Collatz resta. Uma identidade desse tipo é real, mas insuficiente para a ponte com zeros.

## 3. Segunda rota — séries aritméticas das órbitas e árvores

Construir, inicialmente no semiplano de convergência absoluta, séries de Dirichlet cujos coeficientes contem pré-imagens, pertença a componentes de órbitas ou eventos de chegada definidos sem assumir a conjectura. A revisão de dependências e transientes passa a alimentar esta construção.

**Alvo:** obter uma equação funcional fechada dessas séries sob a ação de T, identificar os termos de congruência e estudar se alguma fatoração ou continuação relaciona suas singularidades às de ζ. Especificar separadamente coeficientes de contagem e coeficientes indicadores: suas abscissas de convergência não são intercambiáveis.

**Controle de conteúdo:** somar n^{-s} sobre todos os inteiros produz ζ por definição. Uma partição em órbitas que apenas recompõe essa soma não é evidência de que a dinâmica explica os zeros. Queremos informação que se altere ao trocar a regra e que não seja inserida pelo peso ou pela normalização.

**Atualização 26/09/2026 (B19):** a fronteira natural das séries de potências das órbitas inversas (Bell–Lagarias 2015) **não** obstrui as séries de Dirichlet correspondentes; a continuação de D_m(s) = Σ_{n∈O⁻(m)} n^{−s} depende da distribuição de O⁻(m) nos inteiros grandes. Candidata a P2: densidade e termo de erro de O⁻(5) e O⁻(16), as séries individuais e não a soma (que recompõe ζ trivialmente se Collatz vale). Nenhum mecanismo conhecido liga isso aos zeros de ζ.

**Primeira entrega:** uma família definida, sua região de convergência e a equação que deve satisfazer, ou uma prova de que a tentativa não fecha no espaço proposto. Nenhuma procura de coincidência numérica entre zeros antes disso.

## 4. Terceira rota — operador, traço e determinante

**Pergunta de alto risco:** existe um operador de transferência associado naturalmente a Collatz, em espaço explicitamente definido, cujo determinante ou resolvente tenha uma relação demonstrável com ζ ou ξ?

O programa de Mayer para dinâmica modular é um precedente metodológico de relação entre operadores e zetas, mas envolve a zeta de Selberg; não é uma ponte pronta de Collatz a Riemann. Fonte primária indicada para leitura: D. Mayer, *Transfer Operators, the Selberg Zeta Function and the Lewis–Zagier Theory of Period Functions* (capítulo, 2012). Nesta rodada foi consultado somente o resumo editorial:
https://www.cambridge.org/core/books/abs/hyperbolic-geometry-and-applications-in-quantum-chaos-and-cosmology/transfer-operators-the-selberg-zeta-function-and-the-lewiszagier-theory-of-period-functions/FAAA7F82823AB755556A9CA24F291A61 .

Antes de propor um determinante, exigir espaço, medida, domínio, pesos e prova da propriedade analítica necessária. Um operador limitado em ℓ² não ganha automaticamente determinante de Fredholm. Se houver regularização, ela integra a definição e precisa de justificativa.

**Primeiro teste matemático:** verificar se os traços/ciclos do candidato contêm informação suficiente para o alvo. A zeta simbólica já conhecida (1−2z)^{-1} não se torna ζ de Riemann por compartilhar o nome. Pesos construídos a partir dos zeros ou dos primos para forçar a identidade não contam como explicação independente. Fatores de normalização devem ser fixados antes, sem absorver uma discrepância arbitrária.

## 5. Ordem de trabalho e critérios de decisão

| Passo | Entrega | Critério |
|---|---|---|
| P0 | Este roteiro | Ponte direta incluída no escopo, sem afirmação de existência |
| P1 | Nota de leitura de Meinardus e citações posteriores | Reconstruir a relação conhecida, com páginas e hipóteses; se acesso falhar, manter pendência. **Meinardus: validado (B18); varredura: nenhuma ligação com zeros (B18 §5); Bell–Lagarias (B19) e Siegel (B20) lidos: validado** |
| P2 | Ficha de uma construção candidata | Regra de Collatz, objeto analítico, relação desejada e mecanismo que evita inserir ζ artificialmente |
| P3 | Derivação local ou obstrução | Provar o primeiro passo não tautológico, ou delimitar por que a classe escolhida falha |
| P4 | Protocolo de teste eventual | Só se P3 gerar previsão independente com controles e orçamento |

P1 tem prioridade bibliográfica. P2 pode avançar formalmente pela rota de séries sem depender de obter o PDF, mas não atribuir novidade antes da comparação. Não desenvolver três implementações. A rota de determinantes fica como alternativa após a triagem analítica.

Um cálculo futuro deve distinguir identidades, aproximações, coincidências e hipóteses. O instrumento espectral só entra quando houver observável compatível com seu domínio. Não pressupor que gráficos de Collatz devam ter estatística GUE ou picos em log p.

## 6. Relação com o plano complementar

O [plano de dependências e transientes](PLANO_COLLATZ_DEPENDENCIAS_TRANSIENTES.md) continua como base matemática, mas deixa de ser o único destino da frente. Suas construções podem fornecer coeficientes e operadores para esta busca direta. Não se afirma que isso ocorrerá.

A próxima tarefa da frente direta é **conferir o antecedente de Meinardus e formular uma pergunta sobre zeros que vá além do resultado existente**. Não há nova demanda de produção de zeros nem autorização implícita de enumeração extensa. Os limites de custo e os documentos congelados continuam vigentes.

## Atualização de acesso — 26/09/2026

O usuário obteve o PDF via Tor na URL acima. A cópia local foi recebida e arquivada como `archive/fontes_etapa11/ponte_collatz_20260925/meinardus_2001.pdf`, 15 páginas, SHA-256 `08ebcc736ad2c72dad634394cdd9402f90f21a31af0fb77d6709bd8bf2ce297e`. Capa conferida (autor, título, Nr.261/2001); conteúdo matemático ainda não analisado. As falhas anteriores de acesso foram preservadas. A pendência de obtenção está resolvida; a de leitura permanece.
