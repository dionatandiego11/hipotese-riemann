# Ponte por razões discretas: constantes principais e correções sensíveis a pares próximos

13/10/2026. Continuação de R3. A: identidades locais e fatores aritméticos; B: verificações numéricas de controles; D: substituição das médias deL pelos fatores da receita. Não há prova deC7/C8 nem fórmula completa de termos inferiores.

## 1. Leitura dirigida: o que os artigos de2025 permitem

Hughes–Pearce-Crump, arXiv:2509.07788v1,17pp.: introdução/Conj.1, pp.1–2, e contexto dos modelos, pp.3–5. A p.1 foi conferida visualmente. O momento complexo (ζ'(ρ))^k NÃO é o momento absoluto |ζ'(ρ)|^(−2). Em particular, a discussão de k=−2 não pode ser usada para nosso alvo positivo; ela envolve fases e ausência do termo principal daquele momento complexo.

Hughes–Pearce-Crump, arXiv:2509.07792v1,29pp.: pp.1–3 e seção7, pp.18–21, lidas de forma dirigida; pp.3 e18 visualmente conferidas. O próprio texto restringe o método de diferenciação dos produtos a inteiros não negativos. Não substituímos k por um inteiro negativo na fórmula deles.

A seção7 fornece uma estrutura útil: contagem de zeros por F'/F e aplicação de razões a uma função geradora antes da diferenciação. Os erros de contorno apresentados lá para produtos positivos não são importados para fatores inversos. Leitura dirigida, não auditoria das provas completas.

## 2. Identidade exata de contagem ponderada

F=L(s,χ), χ primitivo; Xχ é seu fator funcional F(s)=Xχ(s)F#(s). Trabalhe numa janela positiva[A,B] cujos extremos não são zeros, com zeros críticos simples e nenhuma outra singularidade perto do segmento. GRH e simplicidade local são hipóteses suficientes; não foram demonstradas.

Para ε>0 pequeno, ponha s=1/2+it,

    Wj,ε(t)=|Hj(s+ε)/F(s+ε)|²,
    H7=1, H8=L(2s,χ²),
    ℓχ(t)=−Re[Xχ'/Xχ](1/2+it).

Se aχ∈{0,1} é a paridade,

    ℓχ(t)=log(q/π)+Re ψ((1/2+aχ+it)/2).

É uma função suave na janela. Na linha crítica, longe dos zeros, Re(F'/F)=−ℓχ/2. Perto de um zero, Re(F'/F)(1/2+ν+it) tem núcleo ν/[ν²+(t−γ)²] e uma parte regular. Assim, para ε FIXO,

    ΣA<γ<B Wj,ε(γ)
      = limν↓0 (1/π)∫A^B Wj,ε(t) Re[F'/F](s+ν)dt
        +(1/(2π))∫A^B ℓχ(t) Wj,ε(t)dt.                         (1)

A prova usa a massaπ do núcleo e o valor da parte regular; o peso é contínuo e limitado para cada ε>0. Nos extremos não há semimassa porque eles não são zeros. Multiplicando por ε² e depois tomando ε↓0,

    limε↓0 ε² Σ Wj,ε(γ)=Σ|Hj(ρ)/F'(ρ)|².                  (2)

A ordem ν→0 PRIMEIRO é parte da identidade. O termo com ℓ em(1), multiplicado por ε², tende a zero na janela fixa: ∫Wε=O(1/ε), pela regularização local já derivada. Não se inferiu um limite conjunto uniforme emB, condutor ou separações.

## 3. Diagonal com derivada logarítmica: os polos corretos

A nova média a calcular é Wε Re(F'/F)(s+ν), além da médiaWε. A diagonal pode ser extraída inicialmente das séries na região de convergência absoluta e continuada meromorficamente. Identificá-la com a média na linha crítica é etapa conjectural da receita.

Para7, H/F tem coeficientes μ(n)χ(n); para8, tem coeficientes λ(n)χ(n), pela identidade L(2s,χ²)/L(s,χ). Esta última preserva a correlação de altura2t; não substituímos L(2s) por L(s) nem por uma variável independente.

Escrevendo F'/F(s+ν)=−Σm Λ(m)χ(m)m^(−s−ν), a diagonal exige l=mn. No casoμ, m=p e p∤n; no casoλ, λ(mn)=λ(m)λ(n) e todas as potências de primo contribuem com sinais alternados. Resultam

    média formal[Wj,ε F'/F(s+ν)] = Dj(2ε;q) Pj(ν,ε;q),

    P7=Σp∤q logp p^(−1−ν−ε)/(1+p^(−1−2ε)),
    P8=Σp∤q logp/(p^(1+ν+ε)+1).                           (3)

Os fatores são reais para estes deslocamentos. D7,D8 são os já calculados.

No caso7, há também uma geração por razão com numerador pareado:

    F(s+u)/[F(s+v)F(s+ε)F#(s−ε)].

Diferenciar emu e depois pôru=v=ν produz a média buscada. No primo p∤q, a diagonal local é

    1−p^(−1−u−ε)+p^(−1−v−ε)+p^(−1−2ε).

Sua derivada logarítmica emu=v fornece o termo deP7. Isto evita enviar numeradores ao infinito. A uniformidade após diferenciação e ν→0 não está automaticamente garantida pela conjectura citada; é uma dependência explícita.

No caso8, usamos os coeficientes Liouville para formular a extensão da receita. Não declaramos que uma fórmula CFZ impressa com todos os fatores à mesma altura já prove essa média com altura2t.

## 4. Resíduos e recuperação formal deC7/C8

Defina Cq=B7^diag/κ7, já conhecido:

    Cq=γE−2ζ'(2)/ζ(2)+Σp|q logp/(p+1).

Os DOIS fatores satisfazem, paraν=0,

    Pj(0,ε;q)=1/ε−Cq+O(ε).                               (4)

Para8, isto segue diretamente de

    P8=−L0'/L0(1+ε)+2L0'/L0(2+2ε),

ondeL0=L(s,χ0). Para7, subtraia−ζ'/ζ(1+ε); a diferença é uma soma absolutamente convergente em torno deε=0. Emε=0, ela envolve2Σp logp/(p²−1)=−2ζ'(2)/ζ(2), e a retirada dos primos deq dá os fatores locais acima.

Portanto

    Dj(2ε)Pj(0,ε)
       =κj/(2ε²)+(Bj^diag−κj Cq/2)/ε+O(1).               (5)

Substituir as médias de(1) por estas diagonais, apenas como receita formal, recupera

    momento j ~ κj(B−A)/(2π),
    κ7=ζ(2)^(−1)∏p|q p/(p+1),    κ8=φ(q)/q.              (6)

Agora a constante vem de uma diagonal COM contagem de zeros e polo1/ε², não apenas de multiplicar uma média inversa contínua porε. Isso fornece uma ponte formal para ambas as constantes principais pedidas porAndrew. NÃO estabelece a assíntota: ainda falta controlar o resto desta média.

A primeira correção FORMAL emε do lado substituído é

    (ε/π)[(B−A)(Bj^diag−κj Cq/2)
                 +(κj/4)∫A^B ℓχ(t)dt].                  (7)

Ela não é um termo inferior emB ouT. A soma deslocada exata e a receita podem exigir restos nessa ordem, particularmente ao fazer médias que não são uniformes em pares próximos.

## 5. A hipótese que falta não pode ficar escondida

Seja

    Ej(ν,ε;A,B)=∫A^B Wj,ε Re(F'/F)(s+ν)dt
                      −(B−A)Dj(2ε)Pj(ν,ε).

Na janela fixa, (1)–(5) dão exatamente

    limε↓0 ε² limν↓0 Ej
      =πΣ|Hj(ρ)/F'(ρ)|²−κj(B−A)/2.                     (8)

Assim, um erro uniforme que desaparecesse após multiplicar porε² para TODA janela fixa seria falso em geral, como já visto para a regularização contínua. A meta é estimar este coeficiente quandoB cresce, por exemploo(B) para recuperar somente o termo principal, ou uma expansão explícita para obter inferiores.

Assumir que esse coeficiente éo(B) já contém, através de(8), a conclusão principal do momento. Não tratamos isso como hipótese independente já demonstrada nem como prova pela receita. Precisamos de uma previsão efetiva da média completa e do seu erro, e não apenas renomear o momento desconhecido como resto.

R3 avançou no cálculo formal dos fatores; seu critério de uniformidade continua aberto. R4, inferiores, não foi liberada por(6).

## 6. Controle CUE discreto: um viés que depende do tamanho

SeU éCUE(N), N≥1, Λ(z)=det(I−zU*), zj seus zeros e0<r<1, a densidade deVandermonde fornece uma identidade de condicionamento em um autovalor:

    (1−r)² E Σj |Λ(r zj)|^(−2)
        = E_CUE(N−1) |Λ(1)/Λ(r)|².                      (9)

Prova: fixe o índicej e rode o círculo para zj=1. O fator correspondente no denominador é(1−r)²; as interações deVandermonde entrej e os outros autovalores viram |Λ_{N−1}(1)|². A soma nosN índices cancela o fatorN na normalização, deixandoCUE(N−1). ParaN=1, o conjunto restante é vazio e o lado direito vale1.

A fórmulaCFZ Teorema4.1, com um numerador e denominador em cada lado, dá exatamente, paraM≥0,

    E_CUE(M)|Λ(1)/Λ(r)|²=1+M(1−r)/(1+r).                 (10)

Por exemplo, antes de tomar o deslocamento de numeradorh→0, a soma das duas trocas é

    [(1−r e^(−h))²−e^(−2(M+1)h)(1−r e^h)²]
          /[(1−e^(−2h))(1−r²)].

Os polos cancelam e o limite é(10). ParaM=0, a identidade também segue diretamente da matriz vazia.

Comr=e^(−ε), o momento discreto deslocado normalizado fica

    A_N(ε)=1+(N−1)tanh(ε/2).                            (11)

ParaN fixo, tende a1. Masε=c/N, c>0 fixo, dá

    limN→∞ A_N(c/N)=1+c/2,                              (12)

não1. Portanto mesmo neste controle EXATO uma escolha de deslocamento da ordem1/N mantém um viés de tamanho principal. Não se transfere automaticamente paraL; serve como teste rigoroso contra uma troca ingênua dos limites. A média contínua anterior era independente deN; a média nos autovalores não é a mesma observável.

## 7. Pares próximos: o primeiro coeficiente não comuta com a média

Há uma consequência ainda mais relevante para termos inferiores. Para uma matriz fixa com autovalores distintos, defina

    A_U(ε)=(1−e^(−ε))² Σj|Λ(e^(−ε) zj)|^(−2),
    S_U=Σj|Λ'(zj)|^(−2).

Cada parcela, após remover seu próprio fator(1−r)², é um produto deN−1 inversos de|1−r e^{iφ}|². Paraφ≠0,

    d/dε log |1−e^(−ε+iφ)|^(−2) emε=0 =1.

Logo, para cada matriz fixa,

    A_U(ε)=S_U+(N−1)S_U ε+O_U(ε²).                      (13)

JáE S_U=1, conforme cálculo anterior comVandermonde, enquanto(11) implica

    d/dε E A_U(ε) em0 = (N−1)/2,
    E[d/dε A_U(ε) em0] = N−1.                           (14)

ParaN≥2, os coeficientes NÃO coincidem. A derivada no deslocamento não pode ser trocada pela média, apesar de o termo principal coincidir. A constante do resto em(13) depende das separações; configurações com autovalores arbitrariamente próximos impedem a transferência automática da expansão local.

Isto não é uma descoberta anunciada como nova: é uma consequência matemática do controleCUE e da fórmula conhecida de razões, derivada aqui. Mostra de forma concreta por que a advertência deAndrew sobre pares próximos importa também no cálculo das correções, não só nas tabelas numéricas.

## 8. Verificações e escopo

Declaração anterior à implementação em results/razoes_discretas_20261013/. Nenhum dado de zeros.

P7 foi avaliado por uma diferença convergente de−ζ'/ζ, crivo até20.000 e majorante de cauda4(log20.000+1)/20.000. O termo por primo na diferença é majorado por4logp/p²; substituir primos por todos os inteiros e integrar fornece essa cota. Ela controla truncamento analítico, mas não certifica os arredondamentos de mpmath. P8 foi avaliado pela fórmula meromorfa deζ, sem truncamento de primos.

A fórmula(10) foi conferida independentemente por determinantes deToeplitz, tamanhosM=0,1,2,5,10 e raios0,25;0,9;0,99. Coeficientes usados:

    c0=2/(1+r),  ck=−[(1−r)/(1+r)] r^(|k|−1), k≠0.

Os coeficientes iniciais também foram conferidos por quadratura angular. Isso é controleB, não amostra de matrizes aleatórias. A identidade para todosN é analítica e o teste finito não é sua prova.

Próximo alvo deR3: a média completa do gerador com derivada logarítmica e seus termos duais/bordas, mantendoν eε separados. Os casos7/8 compartilham o polo principal, mas não presumimos restos ou inferiores iguais. Sem novos zeros, comparação comMN, publicação ou commit.

Execução: **22 testes passaram** (4 novos e18 pertinentes anteriores). CPU11.712s; parede11.322s; teto60s. Nenhuma falha. Testes e leituras não são revisão independente. Arquivos/fontes copiados ou referenciados comhash no manifesto da execução.
