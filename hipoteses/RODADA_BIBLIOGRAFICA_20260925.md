# Rodada bibliográfica — 25/09/2026

Entrega documental. Nenhuma simulação, CL1 ou leitura de dados reservados. A pesquisa consumiu recursos normais de rede, leitura e hashing; “sem CPU” aqui significa sem nova computação científica longa. Não constitui busca sistemática exaustiva nem comprovação de novidade.

## Fontes primárias obtidas e trechos lidos

Os quatro PDFs estão em [arquivo local](../archive/fontes_etapa11/hipoteses_20260925/); URL, horário, tamanho e SHA-256 completos constam de [aquisicao.json](../archive/fontes_etapa11/hipoteses_20260925/aquisicao.json) e do manifesto geral. Versões abaixo foram identificadas no conteúdo. Leitura parcial; nenhuma indicação de leitura integral.

| Fonte | Versão; trechos lidos | Consequência para o projeto |
|---|---|---|
| Leventides–Poulios, *Koopman operators and the 3x+1-dynamical system* | arXiv:2010.12987v1; pp. 1–3 e 8–10, definições e Teoremas 4.2–4.3 | Operadores em espaços de sequências e Fourier de Collatz já são uma linha existente. |
| Grosswald–Schnitzer, *A class of modified ζ and L-functions* | Pacific J. Math. 74(2), 1978; pp. 357–359, especialmente Teorema 1 | A lista de zeros não identifica automaticamente os fatores de Euler. |
| Bohigas–Pato, *Missing levels in correlated spectra* | arXiv:nucl-th/0403006v2; pp. 1–3 | Estatísticas de espectros incompletos já têm antecedentes; “detectar falta de níveis” não basta como novidade. |
| Candès–Fernandez-Granda, *Towards a Mathematical Theory of Super-Resolution* | arXiv:1203.5871v3; pp. 1–2 | Recuperação de medidas discretas a partir de Fourier é problema conhecido; não transportar seus limites de separação diretamente à nossa janela. |

**Resultado conhecido relevante (A, com escopo):** Grosswald–Schnitzer permitem substituir cada primo p_n por um real q_n no intervalo [p_n,p_{n+1}]. O produto modificado tem os mesmos zeros, com multiplicidades, em Re(s)>0. Em geral não conserva a equação funcional. Portanto isso é uma obstrução à identificação numa classe ampla, não um contraexemplo à unicidade numa classe que fixe todas as condições de uma função L. [Fonte, Teorema 1, p. 358](https://msp.org/pjm/1978/74-2/pjm-v74-n2-p09-s.pdf).

**Correspondência conhecida para CL0 (A):** no mapa acelerado T, o operador de transporte Lf(n)=Σ_{T(m)=n}f(m) tem norma 2^{1−1/p} em ℓᵖ; o operador de composição Uf=f∘T tem norma 2^{1/p}. Assim os valores 1, √2 e 2 de L não são uma descoberta do projeto. Atenção à nomenclatura: o artigo chama L de “forward” e U de “backward”. [Fonte, Teoremas 4.2–4.3](https://arxiv.org/abs/2010.12987).

## Busca realizada e limites

Consultas incluíram: “Collatz transfer operator spectrum Koopman”; “Collatz finite sections spectrum”; “Collatz autoconjugacy rational periodic points”; “Grosswald Schnitzer zeros”; “missing zeros explicit formula recover”; “Missing levels correlated spectra Bohigas Pato”; “super-resolution Fernandez-Granda”. Resultados sem leitura de fonte primária não foram promovidos a evidência. Preprints que anunciam soluções de Collatz não foram adotados como resultados estabelecidos.

Falta seguir citações sobre localização de níveis ausentes, variantes dos operadores de Collatz e classes de unicidade de funções L. Não se afirma que as propostas seguintes sejam problemas novos para a literatura. [Perguntas propostas](PERGUNTAS_20260925.md).
