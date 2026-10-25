# Declaração — ordem dos geradores e reescritas pares

19/10/2026. Redigida após a derivação preliminar das identidades e a descoberta de uma troca de ordem nas notas anteriores; antes da implementação e da enumeração desta entrega. Não é teste confirmatório nem de novidade.

Correção a verificar: a ordem cronológica de Phi_a(x)=(3x+1)/2^a usa limites a_i<=2*3^(i-1). A ordem da raiz para a folha na árvore inversa é a reversa, com limites decrescentes. Manter o mesmo evento e não apenas reverter o resíduo.

Grade fixa: ell=1,...,5, soma s=ell,...,3ell, todos os pares adjacentes. Enumerar apenas composições positivas com limites cronológicos crescentes. Comparar todos os contadores de resíduos com generator_counts e tuple_oracle existentes. Não normalizar evento vazio.

Verificar exatamente: igualdade dos mapas com expoentes reversos à fórmula da árvore inversa; identidade afim de transferir h=+2,-2 entre expoentes adjacentes; quando 3<=a_i<=cap_i-2 para ambos os expoentes, os três resíduos têm mesmo módulo3^r e filhos distintos módulo3^(r+1), r=ell-i com i indexado a partir de1. Seleção do filho desejado tem no máximo3 pré-imagens; contar todos os caminhos com folga por classe e conferir N_filho>=G_classe/3.

Incluir testemunhas algébricas fixas: palavra cronológica (3,1) versus palavra da árvore inversa (1,3), e a diferença entre limitar em ordem crescente ou decrescente; bloco com par (3,3) em posições2,3 (limites6,18), com um prefixo e um sufixo unitários; bloco de expoentes todos1 não admite reescrita de mesmo comprimento/custo. São controles de convenção e identidade, não evidência assintótica.

A verificação relata casos vazios e classes sem caminhos com folga. Não muda o alvo se aparecerem zeros e não conclui que a fração de caminhos com folga seja uniformemente positiva. Teto30s de CPU com RLIMIT_CPU, inteiros e Fraction, sem aleatoriedade, órbitas positivas, dados de zeros ou rede. Uma execução; falhas preservadas e corrigidas mediante registro.
