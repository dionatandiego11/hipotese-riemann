# Erro do gerador: perfil polar exato e representação fora da diagonal

14/10/2026. Continuação deR3, primeiro em janela fixa. ClassificaçãoA: derivações sob as hipóteses locais indicadas; B: controles artificiais. A cota sublinear emaltura NÃO foi demonstrada. Sem novo dado de zeros e sem afirmação de novidade ou revisão independente.

## 1. Pergunta atacada

A nota de13/10 formulou a condição suficiente

    ε sup|u−ν|=ηε |Rj(T;u,ν,ε,ε)| ≤ M(T),  0<ν<ε/2,

comRj=Mj−(T−A)Gj. M(T)=o(T) implicaria o termo principal do momento. Agora identificamos a parte singular dessa família de erros e uma representação exata do resto numa região de convergência absoluta.

Não presumimos que controlarRj seja mais fácil que controlar o momento. A derivação abaixo mostra precisamente quanta informação do momento já está contida no termo polar da norma proposta.

## 2. Perfil da média real, com a razão de deslocamentos fixa

Mantenha as definições deMj,F,Hj e a janela[A,T] da nota anterior. F,Hj são holomorfas perto do segmento, F tem apenas zeros críticos simples internos na faixa considerada, e os extremos não são zeros. ParaL, GRH e simplicidade local são hipóteses suficientes. Janela, função e condutor são FIXOS nesta seção.

Fixeλ∈(0,1/2), η∈(0,1), |z|≤η e faça

    ν=λε, u=ν+εz, a=b=ε,
    Sj=ΣA<γ<T |Hj(ρ)/F'(ρ)|²,
    hλ(z)=1+z/(1+λ).

Então

    limε↓0 ε Mj(T;ν+εz,ν,ε,ε)=π Sj hλ(z),             (1)

uniformemente em|z|≤η, para cadaλ fixo. Não foi estabelecida uniformidade emalturaT, separação mínima de zeros ouλ↓0.

### Prova local

Perto deρ=1/2+iγ, escrevaF(s)=(s−ρ)fρ(s), comfρ limitada longe de zero num disco fixo. Ponhat=γ+εy. O peso e a razão satisfazem

    ε² |Hj(s+ε)/F(s+ε)|² → |Hj(ρ)/F'(ρ)|²/(1+y²),
    F(s+ν+εz)/F(s+ν) → 1+z/(λ+iy).

A razão dos fatores lineares é limitada por1+η/λ; a razão dos fatoresfρ é uniformemente limitada no disco. O integrando escalado é majorado porCλ/(1+y²). Convergência dominada, com convergência uniforme nos parâmetrosz em compacto, dá

    ∫R [1+z/(λ+iy)]/(1+y²)dy
         =π[1+z/(1+λ)].

A segunda integral éπ/(1+λ), por paridade da parte ímpar e frações parciais na parte real. Fora das vizinhanças dos polos, o integrando é limitado e sua contribuição após multiplicar porε tende a zero. Somar as contribuições prova(1).

O argumento preserva a função realF e os pesos de cada zero. Não substituiF por um modelo aleatório nem usa aproximação de valores tabulados.

## 3. Perfil aritmético e coeficiente desconhecido do erro

As diagonais calculadas anteriormente satisfazem

    limε↓0 ε Gj(ν+εz,ν,ε,ε;q)=(κj/2)hλ(z),            (2)

uniformemente no mesmo disco.

Para8, basta usarG8=D8(2ε)D7(ν+ε)/D7(ν+ε+εz) e os resíduos deD7,D8. Para7, Y7 tem perfilRq hλ(z)/(2ε), comRq=φ(q)/q; A7 tende uniformemente a1/L0(2), pois seu produto converge analiticamente perto dos deslocamentos zero. Rq/L0(2)=κ7.

Defina

    Δj(A,T)=πSj−κj(T−A)/2.

De(1) e(2),

    limε↓0 ε Rj(T;ν+εz,ν,ε,ε)=Δj(A,T)hλ(z).           (3)

Este é o perfil polar COMPLETO emz na escala analisada. Seu coeficiente é o próprio desvio do momento em relação ao termo principal.

Na circunferência|z|=η, a convergência uniforme implica

    limε↓0 ε sup|u−ν|=ηε |Rj|
       =|Δj(A,T)|[1+η/(1+λ)].                          (4)

O máximo é atingido emz=η. Não é necessário usar uma cota triangular entre a média e a diagonal para identificar esta norma polar.

## 4. Consequência para a hipótese de uniformidade

Se a condiçãoUj(M) anterior vale para todos0<ν<ε/2, ela vale em particular paraν=λε, para CADAλ fixo. Assim(4) impõe

    M(T)≥|Δj(A,T)|[1+η/(1+λ)]

para todoλ∈(0,1/2). Tomando o supremo dessas desigualdades escalares,

    M(T)≥(1+η)|Δj(A,T)|.                              (5)

Não trocamos limites nem alegamos uniformidade emλ↓0: primeiro a prova vale para cadaλ fixo; depois tomamos o supremo de desigualdades já obtidas. A condiçãoU, se válida, daria inclusive o limite necessário

    |Sj−κj(T−A)/(2π)|≤M(T)/[π(1+η)].                  (6)

A transferência porCauchy da nota anterior continua correta, mas sua constante era menos precisa. O refinamento não estimaM(T).

**Leitura científica:** o termo polar da condiçãoU já contém integralmente o desvio procurado. Isto não prova equivalência deU comC7/C8: U também controla deslocamentos finitos e partes não polares. Porém impede tratar uma cota sublinear paraU como um passo técnico simples independente da conjectura.

Uma majoração absoluta separada das duas parcelas tem, nessa escala, tamanho governado porπSj+κj(T−A)/2. Mesmo seSj=O(T) estivesse disponível, isso forneceria apenas ordemT, sem o cancelamento que exigeM(T)=o(T). Não é prova de impossibilidade de outras técnicas; é o limite dessa majoração.

## 5. Onde o cancelamento aritmético aparece explicitamente

Podemos escrever o resto exatamente fora da região singular, antes de tentar continuá-lo. Considere agora deslocamentos comRe u,Re v,Re a,Re b>1/2. Todas as séries deDirichlet abaixo convergem absolutamente na retas=1/2+it.

Ponhaα7(n)=μ(n), α8(n)=λ(n), e

    cj(m;u,v,a)=Σkℓh=m μ(ℓ)αj(h) k^(−u)ℓ^(−v)h^(−a).

O fatorχ(m) fica fora decj. As identidades deDirichlet deF eHj/F dão

    Mj = Σm,n cj(m) αj(n)χ(m)conjχ(n)
                /[sqrt(mn)n^b] K_A,T(log(n/m)),

    K_A,T(ω)=∫A^T e^(itω)dt
       = e^(i(A+T)ω/2)·2sin((T−A)ω/2)/ω,
    K_A,T(0)=T−A.                                     (7)

Convergência absoluta permite integrar e reagrupar. A parcelam=n é exatamente(T−A)Gj, logo

    Rj=Σm≠n cj(m) αj(n)χ(m)conjχ(n)
                 /[sqrt(mn)n^b] K_A,T(log(n/m)).        (8)

É uma identidade exata nesta região, não um enunciado assintótico. Não exigeGRH ali, desde que os argumentos deF estejam na região deEuler sem zeros. O gerador aritmético resulta do mesmo coeficiente constante local já derivado.

A função núcleo satisfaz

    |K_A,T(ω)|≤min(T−A,2/|ω|).

Para m,n próximos, log(n/m) é pequeno. Portanto não há uma cota uniformemente pequena do núcleo que elimine as parcelas fora da diagonal. São necessárias estimativas das somas aritméticas com seus sinais e fases, ou outra ferramenta que preserve esse cancelamento.

## 6. A derivada seleciona correlações deMöbius/Liouville

Na região de convergência absoluta, diferenciar emu e depois pôru=v=ν é legítimo. A convolução log∗μ=Λ dá

    ∂u cj(m)|u=v=ν
       =−Σdh=m Λ(d)αj(h)d^(−ν)h^(−a).

Consequentemente,

    ∂u Rj|u=v=ν
      =−Σd,h,n:n≠dh Λ(d)αj(h)αj(n)χ(dh)conjχ(n)
           /[d^(1/2+ν)h^(1/2+a)n^(1/2+b)]
           ·K_A,T(log(n/(dh))).                        (9)

A região n≈dh destaca as correlações responsáveis pelo erro da média. O caso7 envolveMöbius; o8 envolveLiouville, com a torção periódica do caractere. O termo diagonal n=dh é oDjPj já calculado.

**Barreira:** não se pode usar(8) ou(9) como séries ordinariamente convergentes quando os deslocamentos tendem a zero. Uma passagem para truncamentos finitos, somação regularizada ou continuação analítica precisa de justificativa e de erro controlado. Não foi obtida aqui. Definir a continuação através da média exata não fornece, por si só, uma estimativa dela.

Assim o próximo alvo útil é uma decomposição truncada de(8)/(9) com controle do resto na região de pequenos deslocamentos; a cota sublinear exigirá cancelamento nessa decomposição. Acrescentar apenas um erroO(√T) à diagonal não resolve a barreira.

## 7. Controles e resultados

Declaração anterior à implementação: results/razoes_perfil_polar_20261014/DECLARACAO.md e.sha256. Sem dados de zeros.

Para um polo artificial, F(s)=s−ρ, H=1, janela simétrica de meia largurad, a integral escalada possui forma fechada:

    εM = 2arctan(d/ε)
        +2z[λ arctan(d/ε)−arctan(d/(λε))]/(λ²−1).

Ela foi confrontada com quadratura independente e com o perfilπhλ. O controle com dois polos temS=1/2 calculado diretamente das derivadas do polinômio. O perfil aritmético8 foi comparado com o gerador fechado, emq=4,5. Os controles não demonstram os limites gerais; a justificativa deles está nas seções2–3. Não há taxa uniforme emλ↓0 nem emaltura inferida dos testes.

## 8. Estado e próximo passo

- Fechado por derivação local: perfil polar real e aritmético, coeficiente do erro e consequência necessária paraU.
- Fechado na região absolutamente convergente: representação do resto fora da diagonal e de sua derivada.
- Aberto: continuação/truncamento com erro controlado na faixa de pequenos deslocamentos, cancelamento sublinear emaltura e termos inferiores.
- R3 continua em execução; nenhum confronto novo comMN/H-004, alteração de protocolos, publicação ou commit nesta entrega.

A tentativa NÃO produziuM(T)=o(T). Produziu uma identificação exata do que a estimativa teria de controlar e uma representação aritmética que torna a dificuldade concreta.

Execução controlada: **8 testes passaram** (3 novos e5 pertinentes de fatores/regularização), CPU10.099s, parede10.240s, teto60s. Nenhuma falha. Precisão50 dígitos nos controles novos; aritmética não certificada. A cadeia anterior de26 testes não foi repetida.
