# Hipóteses e programa de pesquisa

Criado em 19/09/2026. **Entrega documental; nenhum experimento novo executado.**

Pergunta orientadora proposta: **que informação aritmética distingue sistemas que parecem semelhantes pelo espectro, e qual informação se perde ao observar apenas uma lista finita?**

O objetivo é produzir uma previsão nova, uma restrição demonstrada ou um contraexemplo relevante. A validação do instrumento é a infraestrutura desse trabalho. Não há promessa de descoberta nem de prova de RH ou Collatz.

## Duas frentes, com ferramentas próprias

1. **Riemann e funções L:** terminar os controles delimitados da 11.6; depois testar previsões quantitativas sobre erros, informação recuperável e correções de altura finita.
2. **Collatz:** laboratório de dinâmica aritmética, ligado ao plano CL0–CL5 já existente. Estudar simetrias e perda de informação com aritmética exata. Estar fora do domínio do instrumento de Riemann não exclui uma pergunta desta frente.

Não se propõe que Collatz explique os zeros da zeta. Uma ponte futura precisaria definir os dois objetos e demonstrar uma relação entre eles; sem isso, temos comparação de métodos e limites do problema inverso.

## Leitura

- [Balanço do que existe](REVISAO_PROJETO.md): capacidades, limites e alcance da revisão.
- [Perguntas candidatas](CANDIDATAS.md): enunciados, alternativas, refutação e relação com a literatura.
- [Bibliografia e busca](BIBLIOGRAFIA.md): fontes, trechos consultados, falhas de acesso e buscas ainda necessárias.
- [Sequência de trabalho](PLANO.md): entregas pequenas, dependências e critérios de encerramento.
- [Revisão do poder e do registro v2](REVISAO_PODER_E_REGISTRO.md): pontos encontrados na atualização recebida durante esta revisão.

## Integração com o registro existente

O registro oficial de testes espectrais é [docs/REGISTRO_HIPOTESES.md](../docs/REGISTRO_HIPOTESES.md), sujeito ao [protocolo v2](../results/registro_hipoteses/PROTOCOLO_REGISTRO_v2.md). Esta pasta é um **caderno de propostas**, não um segundo protocolo congelado. IDs `P-*` não substituem `H-*`; a promoção de uma proposta exige triagem e declaração no registro apropriado. Não alteramos protocolos nem hashes existentes.

Os candidatos continuam **pendentes, sem resultado**. Os rótulos A/B/C/D classificam afirmações, não desejos de novidade. Nenhuma proposta desta pasta é classificada como achado C. Toda afirmação de lacuna é provisória até confronto com trabalhos próximos e busca por citações.

## Recomendação inicial

Priorizar **P-R1, previsão transferível dos erros**, aproveitando o trabalho existente; preparar **P-C1, simetrias e filtros aritméticos de Collatz**, como frente pequena e independente. P-R2, identificação sem rótulo, é uma segunda opção depois de resolver o vazamento de informação. Não abrir simultaneamente uma busca de Hamiltonianos, de padrões em Collatz e de anomalias estatísticas sem alvos definidos.

Os dias de geração de zeros de Dirichlet sustentam primeiro o controle declarado. Não compram automaticamente uma confirmação nova: depois da análise dos controles, esses dados são T0 segundo o protocolo v2. Uma confirmação posterior precisará de reserva adequada, definida antes do acesso.

## Atualização de 25/09/2026

- [Rodada bibliográfica](RODADA_BIBLIOGRAFICA_20260925.md): quatro fontes primárias arquivadas, leitura parcial e limites.
- [Novas perguntas e refinamento Collatz](PERGUNTAS_20260925.md): P-R5, P-R6 e P-C2a, ainda propostas.
- [Errata da CL0](../results/collatz_cl0/ERRATA_CL0_1.md): distinguir periodicidade binária de periodicidade sob Collatz.

P-R1 já originou H-004, com reserva e adendos próprios; a regra prospectiva vigente é a desses documentos. A recomendação inicial acima é histórica, não substitui essa declaração. Nenhum dado reservado foi consultado nesta atualização.

## Frente complementar escolhida — 25/09/2026

[Plano de dependências aritméticas e transientes de Collatz](PLANO_COLLATZ_DEPENDENCIAS_TRANSIENTES.md): revisão dirigida → alvo sobre dispersão das árvores inversas → formulação separada de transientes → decisão sobre piloto. Nenhuma enumeração nesta entrega.

## Ampliação solicitada: ponte direta Collatz–Riemann

[Roteiro específico](PLANO_PONTE_DIRETA_COLLATZ_RIEMANN.md): séries de Dirichlet e antecedente de Meinardus como primeira leitura; séries de órbitas/árvores como candidata; determinantes como rota de alto risco. A busca direta integra agora o objetivo, sem substituir a necessidade de identidade demonstrável nem afirmar que exista uma ligação entre as conjecturas.

## Direção experimental — 26/09/2026

[Hipóteses e escolhas de pesquisa](DIRECAO_EXPERIMENTAL_20260926.md): inversão do vazamento, perdas seletivas, identificação aritmética e contagens de ramos de Collatz. EXP26-* são propostas, não testes congelados. A ponte direta exige um mecanismo sensível aos zeros antes de procurar coincidências.

### Prioridade revista após revisão do usuário

EXP26-2 passa a principal após H-004. A [ficha prévia](FICHA_EXP26_2_PREVIA.md) está escrita, ainda sem congelamento ou execução. EXP26-1 depende de condicionamento e comparação com ajuste conjunto; EXP26-4 requer busca de antecedentes e benchmark. Ver revisão explícita em `DIRECAO_EXPERIMENTAL_20260926.md`.

### Conta sintética EXP26-2 concluída

[Relatório](../results/exp26_2_viabilidade_20260926/RELATORIO.md): sem critério de avanço satisfeito; parar B1 em k=6/30, inconclusivo em k=2/12. Não altera as prioridades mais recentes do ANDAMENTO (H-004 adiada; VN-1).
