# T001 — A contribuição dos pares raros, calculada por regiões

18/10/2026. Primeiro alvo de T001 concluído como controle analítico A de um modelo conhecido; novidade não estabelecida. Derivação e verificações internas, sem revisão independente. Não foram usados zeros de funções L.

## 1. Convenções e identidade exata

U é Haar em U(2). A diferença angular com sinal entre autovalores é φ∈[−π,π], com densidade p(φ)=(1−cosφ)/(2π). As duas proximidades em torno de zero estão incluídas; não acrescentar outro fator 2.

Defina q(φ)=1−cosφ, ε>0, r=exp(−ε) e a=coshε−1. O momento discreto e sua regularização são

    S(φ)=1/q(φ),
    Aε(φ)=2/[(1−r)²+2r q(φ)]=exp(ε)/(q(φ)+a).

Os valores em φ=0 do peso não regularizado são infinitos; esse evento tem probabilidade zero. E S=1. Para cada φ≠0, Aε=S+εS+O_φ(ε²). A constante desse resto depende do gap.

É útil retirar exp(ε)S em vez de apenas (1+ε)S:

    (Aε−exp(ε)S)p = −exp(ε)a/[2π(q+a)].

O lado direito é integrável. A identidade ∫_{−π}^{π}dφ/(a+1−cosφ)=2π/√(a(a+2)), obtida por tan(φ/2), dá

    E[Aε−exp(ε)S]/ε = −exp(ε)tanh(ε/2)/ε → −1/2.

Como [exp(ε)−(1+ε)]/ε→0, o mesmo defeito −1/2 aparece se retirarmos a expansão linear pontual. Recuperamos E Aε=1+tanh(ε/2), coerente com o controle CUE anterior. O cálculo identifica o mecanismo de uma fórmula conhecida, não um coeficiente novo de L.

## 2. Isolar a camada de pares próximos

Fixamos δ=√ε e 0<ε≤1/16. Escreva o defeito escalado como I_in+I_out, integrando respectivamente |φ|≤δ e δ<|φ|≤π.

No trecho interno, faça φ=εy. O integrando, incluindo dφ e a divisão por ε, é

    −exp(ε)a/[2π(1−cos(εy)+a)] dy
        → −dy/[2π(1+y²)].

A convergência não é apenas pontual: para |φ|≤δ,

    1−φ²/12 ≤ 2(1−cosφ)/φ² ≤ 1,
    1 ≤ 2a/ε² ≤ 1+ε².

Escrevendo esses dois fatores como c e b, o erro de b/(b+cy²) contra 1/(1+y²) é limitado por 2(ε²+δ²/12)/(1+y²). Incluindo exp(ε), uma majorante suficiente é 4ε/(1+y²). A integral dessa diferença e a cauda |y|>δ/ε dão

    |I_in+1/2| ≤ 2ε+√ε/π.

No trecho externo, q(φ)≥2φ²/π². Portanto

    |I_out| ≤ exp(ε)a π/(2εδ) ≤ √ε.

Assim a região cujo tamanho encolhe como √ε contém todo o defeito no limite; dentro dela, a escala efetiva do par é φ da ordem ε. O trecho afastado contribui zero após a divisão por ε. A integração da função limite resulta em −1/2.

Para checagem independente, a integral interna fechada é

    I_in(ε,δ)=−[2exp(ε)tanh(ε/2)/(πε)]
                    ·atan(coth(ε/2)tan(δ/2)).

O limite do argumento em δ=π dá o defeito total. As cotas por regiões são deliberadamente mais fracas que a expansão da fórmula total: sua função é localizar a contribuição.

## 3. Um lema de transferência para modelos de pares

Este lema A é condicional a uma lei conjunta especificada; não afirmamos que as hipóteses valham para zeros de L. É uma consequência elementar de reescala e convergência dominada, sem novidade estabelecida.

Seja d>0 o gap e A≥0 um fator de amplitude. Suponha que a intensidade ponderada tenha densidade m(d)=∫A j(d,A)dA, com

    m(d)/d²→C<∞ quando d↓0,
    m(d)/d² limitada numa vizinhança de zero,
    ∫_{d₀}^{∞}m(d)d^{−4}dd<∞ para algum d₀>0.

Para b>0 fixo, defina diretamente a diferença combinada, evitando subtrair integrais possivelmente divergentes:

    Dε=2∫₀^∞[1/(d²+b²ε²)−1/d²]m(d)dd.

Então Dε/ε→−πbC. De fato, escrevendo g(d)=m(d)/d² e d=bεy, o trecho próximo vira

    −2b∫ g(bεy)/(1+y²)dy → −πbC.

A hipótese de cauda limita o trecho afastado, dividido por ε, por uma constante vezes ε. Não há troca de limites sem essas majorantes.

**O que isso torna preciso:** precisamos da repulsão ponderada pela amplitude, não apenas da densidade de gaps. Dois modelos podem ter os mesmos espaçamentos e valores distintos de C ao mudar as amplitudes. O parâmetro b é determinado pelo observável regularizado; não é universal. No limite local de CUE(2), b=1 e C=1/(2π), reproduzindo −1/2.

Para funções L ainda seria necessário justificar a aproximação por pares, identificar a amplitude com os demais zeros/numeradores, controlar aglomerados maiores e demonstrar uniformidade em altura. O lema não entrega essas estimativas nem converte uma expansão em ε numa expansão em T.

## 4. Execução efetiva e próximo alvo

Declaração prévia: `results/eventos_concentracao_20261018/DECLARACAO.md`. Testes novos a 50 dígitos: quadratura dos pesos contra a média CUE já implementada, integrais interna/externa contra a fórmula fechada, cotas por regiões e constante de cauda. Nenhum Monte Carlo.

O total escalado é aproximadamente −0,520336 em ε=0,04; −0,505021 em ε=0,01; −0,501251 em ε=0,0025. Os valores completos estão no JSON. São controles B, não certificação intervalar.

Próximo alvo: identificar uma estatística conjunta ponderada que determine C sem assumir o próprio momento final e conferir os antecedentes dessa transferência. A calibração CUE está encerrada; repetir mais valores de ε não resolve essa dependência.

Base: [T001](T001_PARES_RAROS.md), [razões discretas](../hipoteses/RAZOES_DISCRETAS_MOMENTOS_NEGATIVOS_20261013.md) e [fontes HKO/CFZ](../hipoteses/leituras/TEORIAS_FONTES_20261015.md).
