# Declaração — energia condicionada ao custo

19/10/2026. Escrita após a derivação analítica preliminar e antes da implementação e da enumeração de verificação. Não é teste confirmatório de novidade.

Alvo: verificar identidades auxiliares da nota a escrever em teorias/SYRACUSE_ENERGIA_CONDICIONADA_20261019.md. Nenhum dado de zeros ou órbita positiva será usado.

Domínio fixado: profundidades ell=1,...,5; custos totais s=ell,...,3ell. Enumerar composições positivas finitas. Duas famílias de eventos: total fixo sem limites e total fixo com a_i<=2*3**(ell-i), i=1,...,ell. Eventos vazios são identificados e não normalizados.

Verificações: (1) coeficiente do momento inclinado por enumeração direta de B(w)/3**ell contra fórmula com binomiais/CDF; (2) injetividade dos quocientes na fibra de custo/resíduo; (3) energia exata por resíduos <= 2*H(ell,s)/beta**2 <= 4/beta**2; (4) monotonicidade da energia sob projeção; (5) para s=2ell sem limites, energia <=64ell. Zero tolerância: inteiros e Fraction.

Teto 30 segundos de CPU, RLIMIT_CPU; execução única, sem ampliação em caso de êxito. Artefatos: manifesto, hashes e cópias do código, log de testes e resumo. Biblioteca em collatz/, teste sem rede. Falha será preservada e investigada; não mudar a grade para obter aprovação.
