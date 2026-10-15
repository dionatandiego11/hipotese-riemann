# Declaração — fechamento dos filtros de congruência de Collatz

Data: 11/10/2026. Solicitação: resolver o primeiro alvo matemático sobre complexidade dos filtros sob repetição dos ramos. Esta declaração antecede a implementação e a avaliação. As identidades abaixo foram formuladas analiticamente antes do piloto; as verificações serão controles de classe B, sem alegação de descoberta.

Mapa: T(x)=x/2 para x par, T(x)=(3x+1)/2 para x ímpar. Ramos inversos b0(y)=2y, b1(y)=(2y−1)/3. Operador de contagem positivo L+ com ramo ímpar admitido apenas se inteiro. Filtro F(q,r)=1_{x≡r mod q}, q≥1. Nenhuma hipótese de convergência das órbitas.

Alvos analíticos: (i) fechamento em indicadores de congruência; (ii) limite do módulo e custo por palavra; (iii) impossibilidade de fechamento num módulo único fixo; (iv) norma uniforme após normalização explicitada; (v) distinguir filtros ímpares de funções contínuas em Z2.

Verificações exatas, sem dados:
- Todas as palavras binárias de comprimentos 0–5; q=1–12; todos r=0,…,q−1; raízes y=1–48. Comparar fórmula de congruência com composição literal dos ramos em frações, exigindo integridade em cada passo.
- q=1–12, todos r, profundidades 0–6, raízes y=1–48. Comparar soma de filtros com contagem independente por iteração DIRETA de T sobre 1≤x≤2^m·48; esse intervalo contém todos os ancestrais dessas raízes.
- m=1–7: verificar o período mínimo 3^m de L+^m 1, incluindo a diferença para o deslocamento 3^{m−1}. Conferir média de período (4/3)^m por frações exatas.
- Filtros 2-ádicos: d=0–6, m=0–8, raízes 0–31. Verificar que a média de todos os ramos em Z2 é 2^{−d} para m≥d, usando divisão modular por 3, distinta da admissão inteira.
- Testes rápidos de equações sem solução, q par, palavras vazias e exclusão do ramo ímpar em raiz 1.

Orçamento: no máximo 60 segundos-CPU para o piloto, aplicado por RLIMIT_CPU, sem extensão automática. Memória prevista inferior a 128 MiB. Processamento em fluxo; nenhum piloto CL1 ou enumeração de ciclos/transientes. Sem aleatoriedade. Sem zeros, catálogo de primos, dados reservados ou imports de riemann_spectra.

Saída: resultados exatos, contagens de verificações, CPU e parede, versões e hashes. Se uma identidade falhar, preservar a falha e diagnosticar antes do trabalho dependente. Esse controle finito não substitui as provas analíticas.
