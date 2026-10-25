# T008 — Recorrência de colisões e obstrução em L²

18/10/2026. Derivações A com hipóteses declaradas e verificações racionais exatas. Não houve revisão independente da entrega. O argumento de não pertinência a L² também foi localizado em fonte externa, conforme §6; não reivindicamos novidade.

## 1. Objeto e dependências

π é a estacionária em Z₃ dos mapas aleatórios independentes D(x)=x/2 e O(x)=(3x+1)/2, cada um com probabilidade 1/2. Não é uma escolha aleatória de ramos ao longo da órbita determinística de um inteiro positivo.

Usamos π_K, sua projeção módulo 3^K, e Haar μ de probabilidade em Z₃. π₀=(1). Defina C_K=Σ_aπ_K(a)² e E_K=3^K C_K. Pela projetividade, E_K é a energia L² da densidade por cilindros f_K=3^Kπ_K.

Para as conclusões sobre a densidade limite, usamos a existência de f∈L¹ e sua positividade quase em toda parte nas unidades, derivadas no projeto aceitando a Proposição 1.14 de Tao; ver [nota de regularidade](../hipoteses/COLLATZ_REGULARIDADE_PI_20261012.md). Não se assume Collatz nem RH.

## 2. Identidade exata em cada resolução

Para K≥1, a estacionariedade dá

    π_K(a)=(1/2)π_K(2a)
            +(1/2)1_{a≡2 mod3}π_{K−1}((2a−1)/3).

O argumento da segunda parcela é tomado módulo 3^(K−1). Não substituir π_{K−1} por uma massa individual em resolução K.

Defina a correlação entre resoluções

    H_K=Σ_{b mod3^(K−1)}π_K(3b+1)π_{K−1}(b).

Ao elevar ao quadrado e somar, as parcelas DD, OO, DO e OD são, respectivamente,

    C_K/4,  C_{K−1}/4,  H_K/4,  H_K/4.

Logo

    3C_K=C_{K−1}+2H_K,
    E_K−E_{K−1}=2·3^(K−1)H_K.

Esta é uma recorrência exata, mas ainda não fecha apenas em E_K: precisamos controlar H_K. Ela identifica a correlação cruzada que a soma separada das contribuições dos ramos perde. Não foi demonstrada impossibilidade de outro fechamento finito.

Em termos das densidades por cilindros, ponha

    J_K=∫f_K(3x+1)f_{K−1}(x)dμ(x).

Então J_K=3^K H_K e E_K−E_{K−1}=(2/3)J_K. A mudança de variável tem módulo 1/3; esse fator é essencial.

## 3. A densidade não pode pertencer a L²

Suponha, por absurdo, f∈L². A equação de densidades é f=g_D+g_O, onde

    g_D(a)=(1/2)f(2a),
    g_O(a)=(3/2)1_{a≡2 mod3}f((2a−1)/3).

Mudanças de variável dão

    ||g_D||²₂=(1/4)||f||²₂,
    ||g_O||²₂=(3/4)||f||²₂,
    2<g_D,g_O>=(1/2)∫f(3x+1)f(x)dμ(x).

Sob a hipótese L², a última integral é finita por Cauchy–Schwarz. Ela é estritamente positiva: f(x)>0 quase em toda parte nas unidades; 3x+1 é sempre unidade; a imagem inversa de conjuntos Haar-nulos por x→3x+1 é nula. As unidades têm medida 2/3.

Portanto

    ||f||²₂=||f||²₂+(1/2)∫f(3x+1)f(x)dμ(x),

contradição. Assim f∉L² e, como μ é probabilidade, f∉L^p para todo p≥2. Isso melhora o limite anterior do projeto p≥log3/log(3/2), sem demonstrar pertencimento para 1<p<2.

O mecanismo não é apenas a concentração de um ramo repetido ao redor de −1: no expoente 2, as duas contribuições quadráticas já esgotam a energia disponível, e sua sobreposição positiva torna uma energia finita impossível.

## 4. Consequência para a energia finita

As médias condicionais f_K convergem quase em toda parte a f. O mesmo vale após compor com 3x+1, pois essa transformação preserva a nulidade de pré-imagens. Fatou fornece

    liminf J_K≥J:=∫f(3x+1)f(x)dμ(x)>0,

permitindo J=∞. Logo existe c>0 e K₀ tal que E_K−E_{K−1}≥c para K≥K₀. Em particular E_K cresce pelo menos linearmente e diverge. As constantes não foram avaliadas; não se afirma crescimento exatamente linear, quadrático ou uma assíntota ajustada aos dados.

Não há contradição com mistura L¹: uma distribuição pode se aproximar em massa total enquanto suas concentrações fazem a energia L² crescer.

## 5. Verificação finita e fronteira do trabalho

K=0..4, no máximo 81 resíduos. Massas obtidas pela construção geométrica anterior e, para K≤2, conferidas contra eliminação racional independente. Todas as equações de ramo, projeções e quatro parcelas foram verificadas em Fraction. Os primeiros valores são E₀=1, E₁=5/3, E₂=15/7; os demais estão no JSON.

Esses exemplos verificam a implementação, não provam divergência ou uma taxa. A prova é a dos §§3–4. Nenhuma órbita positiva foi enumerada e nenhuma estatística condicionada ao custo foi calculada.

Próximo alvo: uma majorante para H_K ou J_K, preservando as correlações cruzadas, e sua comparação com a literatura localizada. Só depois perguntar que parte se transfere para os custos condicionados. Um intervalo de integrabilidade abaixo de 2 não foi provado nesta entrega.

## 6. Antecedente bibliográfico encontrado nesta sessão

A busca dirigida identificou *Quadratic cylinder energy and integrability of the Syracuse law*, de Lucas Valbuena, no repositório do autor. O texto foi consultado especificamente para a falha L² por sobreposição dos ramos e declara resultados mais fortes. Esse mesmo mecanismo não será apresentado como descoberta nova nossa. Registro com commit, SHA-256, escopo e limitações em [nota de leitura](../hipoteses/leituras/SYRACUSE_ENERGIA_20261018.md).

Não auditamos aqui a majorante quadrática, o intervalo completo de integrabilidade nem os arquivos Lean anunciados. Eles não foram usados como premissas da derivação ou das verificações. O próximo trabalho bibliográfico é conferir esses resultados antes de tratar uma majorante como lacuna aberta da literatura.
