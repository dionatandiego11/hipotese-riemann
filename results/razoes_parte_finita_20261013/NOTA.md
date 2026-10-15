# Primeira correção local: parte finita, simetrização e duas escalas

13/10/2026. Continuação analítica de R3. A: derivação em janela fixa, sob hipóteses abaixo. B: controles artificiais a60 dígitos. Não há expansão emT, termos inferiores completos deL, classificação de novidade ou prova deRH.

## 1. Enunciado com hipóteses locais

Sejam 0<A<B, F eH holomorfas numa vizinhança do segmento {1/2+it:A≤t≤B}. Suponha que os únicos zeros deF numa faixa suficientemente estreita em torno do segmento sejam os finitíssimos zeros simples internos ρj=1/2+iγj, que F não se anule nos extremos e que H/F não tenha outros polos nessa faixa. Escreva

    Q(s)=H(s)/F(s)=aj/(s−ρj)+bj+O(s−ρj),
    aj=H(ρj)/F'(ρj),
    bj=H'(ρj)/F'(ρj)−H(ρj)F''(ρj)/(2F'(ρj)²).

H pode se anular emρj; entãoaj=0 e a contribuição de momento ali é zero. Não se presume GRH global: ela, junto à simplicidade local e ausência de polos, é suficiente para estas condições no segmento. Uma faixa menor pode excluir outros zeros próximos, pois a função fixa tem zeros isolados.

Paraε>0, defina

    C±(ε)=(ε/π)∫A^B |Q(1/2±ε+it)|² dt,
    S=Σj|aj|².

A parte finita é definida com exclusões simétricas em torno de cadaγj:

    FP=limr→0 [∫[A,B]\∪j(γj−r,γj+r) |Q(1/2+it)|²dt
                   −(2/r)Σj|aj|²].

Usar r menor que as distâncias às bordas e que metade das separações. O limite existe: a densidade local tem termo|aj|²/(t−γj)², termo ímpar proporcional a1/(t−γj) e resto contínuo. A exclusão simétrica cancela o divergente logarítmico ímpar e a subtração remove o termo1/r.

A expansão local é

    C±(ε)=S+ε B±+O_{F,H,A,B}(ε²),
    B±=FP/π ±2Σj Re(aj conj(bj)).

Este é um enunciado para uma função e uma janela FIXAS. As constantes e o intervalo de validade podem piorar com as separações, distâncias às bordas e normas locais deQ. Não fornece uniformidade em alturaT, condutorq ou menor separação.

## 2. Justificativa da primeira correção e do resto

Isole cada zero em intervalos simétricos fixos, disjuntos, e separe a região sem polos. Nesta última, a densidade depende suavemente deε; multiplicar a integral porε dá o termo linear da integral emε=0 e restoO(ε²).

Perto de um polo, ponha x=t−γ e z=±ε+ix. A parte principal produz

    ∫−d^d ε|a|²/(π(ε²+x²)) dx
      =|a|²−2ε|a|²/(πd)+O(ε³).

O segundo termo coincide com a parte finita de|a|²/x² no intervalo. O produto com o termo regular constante é

    2 Re[a conj(b)/(±ε+ix)].

A integral de seu termo par é±2π Re(a conj(b))+O(ε), antes de multiplicar porε/π. Sua parte ímpar tem integral zero nesse intervalo simétrico, como no valor principal da densidade na linha.

Escreva o termo regular como b+z c(z), c holomorfa e limitada com suas derivadas em uma vizinhança fixa. Os demais produtos possuem limite integrável na linha. Sua integral difere desse limite porO(ε): os termos aparentemente singulares adicionais vêm comε/(±ε+ix); separar seu coeficiente suave no valor emx=0 e no restoO(x) deixa integrais limitadas. O restante regular tem variação integradaO(ε). Multiplicando porε/π, o erro éO(ε²). Somar os intervalos e a região externa cancela as bordas artificiais da partição e dá aFP global e a soma dos termos locais acima.

A prova não usa uma majoração absoluta que transforme1/x emlog(1/ε); preserva o valor principal e a paridade do termo ímpar. As cotas são locais e não foram avaliadas para as funçõesL do projeto.

## 3. O que simetrizar resolve

A média das duas margens tem expansão

    [C+(ε)+C−(ε)]/2 = S+(ε/π)FP+O(ε²).

Ela cancela a contribuição2ΣRe(aj conj(bj)), mas NÃO a parte finita. Portanto não elimina em geral o primeiro viés. A parte finita contém bordas e estrutura entre polos, além de contribuições da região sem zeros.

Exemplo exato: Q(s)=exp(k(s−ρ))/(s−ρ), k real, ρ=1/2+iγ; janela[γ−l,γ+r], l,r>0. Então

    C±(ε)=exp(±2kε)[arctan(l/ε)+arctan(r/ε)]/π,
    S=1, FP=−1/l−1/r, a=1, b=k,
    B±=−(1/l+1/r)/π ±2k.

Mesmo comk=0, quando os dois lados já são idênticos, o coeficiente linear de borda permanece. Esta é uma resposta negativa ao alvo inicial de eliminar todo viés por simetrização; não é um resultado negativo sobre conjecturas de momentos.

**Diagonais dos dois lados.** Também não se pode substituir a média à esquerda porD_j(−2ε) apenas continuando meromorficamente a diagonal à direita. Ela tem resíduo−κ_j/(2ε), enquanto a integral real de|Q|² é positiva e tem parte principalπS/ε. A conjectura de razões citada exige deslocamentos positivos dos denominadores; o lado esquerdo precisaria de equação funcional e tratamento apropriado. A média formal dessas duas diagonais cancela seu polo, ao contrário do que ocorre com o momento real. Não adotamos essa operação.

## 4. Duas escalas: melhora local sem uniformidade

Se C+(ε)=S+εB++O(ε²), segue por álgebra

    2C+(ε/2)−C+(ε)=S+O(ε²).

É a extrapolação de Richardson de primeira ordem. Pode remover um viés de regularização em janela fixa, sem precisar conhecerB+. Contudo seus coeficientes têm sinais; não preserva positividade, nem dá um limite superior/inferior universal. Não é implementada aqui como análise dos zeros existentes.

No modelo de dois zeros na reta inteira já derivado, com separaçãod,

    C(ε)=2/(d²+4ε²), S=2/d²,
    [2C(ε/2)−C(ε)]/S
       =2/[1+(ε/d)²]−1/[1+4(ε/d)²]
       =1+2(ε/d)²+O((ε/d)⁴).

Ali o termo linear já era zero; a extrapolação não melhora a ordem. O erro absoluto continua da ordemε²/d⁴ e o erro relativo da ordem(ε/d)². Na grade examinada, a extrapolação passa para cima do alvo. Pares próximos continuam exigindo controle da razãoε/d; não se resolveu a dificuldade destacada porAndrew.

## 5. O que deve aparecer numa média completa de razões

Defina I+(ε)=∫A^B |Q(1/2+ε+it)|²dt eD_j(2ε)=κ_j/(2ε)+Bj^diag+O(ε). A expansão local impõe

    I+(ε)−(B−A)D_j(2ε)
       =[πS−(B−A)κ_j/2]/ε
        +[FP+2πΣRe(aj conj(bj))−(B−A)Bj^diag]+O(ε).

Ela refina a identidade anterior do coeficiente singular: agora a parte constante do resto também está identificada como objeto matemático. Não está avaliada nem estimada uniformemente paraL. ReescreverS no resto não é uma fórmula para preverS; esta identidade é uma condição de consistência de qualquer futura previsão.

ParaC7: H=1, aj=1/L'(ρ), bj=−L''(ρ)/(2L'(ρ)²).

ParaC8: H=L(2s,χ²),

    aj=L(2ρ,χ²)/L'(ρ,χ),
    bj=2L'(2ρ,χ²)/L'(ρ,χ)
         −L(2ρ,χ²)L''(ρ,χ)/(2L'(ρ,χ)²).

A janela positiva evita o polo auxiliar de altura zero. Não há hipótese implícita de que a altura2γ possa ser substituída porγ ou tratada como independente.

**Próximo alvo:** obter a previsão para o coeficiente singular do resto por uma média de razões cujo domínio suporte o limite; a nova parte finita oferece um segundo teste de consistência. Nenhum coeficiente inferior emT foi produzido. As escalas emε não são as escalas emT queAndrew pediu.

## 6. Controles previstos e execução

Declaração: results/razoes_parte_finita_20261013/DECLARACAO.md e.sha256, anterior à implementação. Código central: src/riemann_spectra/negative_moments_finite_part.py.

Controles: um polo com fator holomorfo exponencial e janela finita; dois polos com parte finita calculada por frações parciais; modelo de pares próximos. Para os dois polos emγ=1,3 e janela[0,4],

    FP=−2/3+(log3)/2, S=1/2,

porque a densidade é

    1/[(t−1)²(t−3)²]
      =(1/4)[(t−1)^(−2)+(t−3)^(−2)]
        +(1/4)[(t−1)^(−1)−(t−3)^(−1)].

A subtração em intervalos perfurados é apenas controle B da definição; a identidade da parte finita é algébrica. Nenhum valor deF=L, F', F'' ouH nos zeros reais foi calculado. Testes numéricos não certificam a derivação analítica, nem oferecem cota intervalar.

Execução: **18 testes passaram** (4 novos e14 pertinentes anteriores), CPU7,769s, parede7,568s, teto60s. Nenhuma falha nesta execução. Recursos são do processo medido, sem inferência de monothread. Código e testes copiados com hash na pasta da execução. Sem publicação, mensagem externa ou commit.
