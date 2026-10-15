# Razões: contornos deslocados e controle exato CUE

13/10/2026. Continuação de R3, sem dados de zeros. A: identidades matemáticas no escopo indicado. B: controles sintéticos. A previsão completa para L e seus termos inferiores continuam pendentes. Não é demonstração de RH ou resultado classificado como novo.

## 1. Dois conjuntos de polos, sinais opostos

Para função holomorfa F numa vizinhança simétrica do segmento crítico, defina a reflexão holomorfa

    F#(s)=conj(F(1−conj(s))).

Para H holomorfa na mesma vizinhança e δ>0, considere

    Pδ(s)=H(s)H#(s−δ)/[F(s)F#(s−δ)].

Em ρ=1/2+iγ, zero simples de F, F#(ρ)=0 e (F#)'(ρ)=−conj(F'(ρ)). Se os polos indicados não colidem com outros polos/zeros, os resíduos são exatamente

    Resρ Pδ = H(ρ)H#(ρ−δ)/[F'(ρ)F#(ρ−δ)],
    Resρ+δ Pδ = H(ρ+δ)H#(ρ)/[F(ρ+δ)(F#)'(ρ)].

Por expansão local,

    limδ→0 δ Resρ Pδ = |H(ρ)/F'(ρ)|²,
    limδ→0 δ Resρ+δ Pδ = −|H(ρ)/F'(ρ)|².

Isso vale localmente; não depende de uma conjectura de razões. Para F=L(s,χ), F#(s)=L(1−s,conjχ). Para H=L(2s,χ²), H#(s)=L(2−2s,conjχ²): na linha, a conjugação envolve altura2t. Trabalhar longe da origem evita o polo auxiliar já identificado.

**Consequência para o contorno.** Um círculo fixo contendo o par de polos, com F e F# sem zeros sobre sua borda, satisfaz

    limδ→0 δ/(2πi) ∮ Pδ(s) ds = 0.

A integral na borda é uniformemente limitada e as partes singulares opostas se cancelam. Portanto esse contorno NÃO calcula o momento desejado. Um contorno que isola só os polos originais recupera o momento pelo limite dos resíduos, mas precisa depender de δ. Por exemplo, círculos de raioδ/3 isolam cada zero crítico simples quando δ é suficientemente pequeno frente às separações locais. Sua soma recupera os pesos, porém não é uma média longa pronta para aplicar CFZ.

Um retângulo de largura menor queδ separando as duas linhas de polos é outra possibilidade local. Controlar as integrais sobre suas bordas quando δ→0 é precisamente uma exigência de uniformidade, não uma solução gratuita. Não foi derivada aqui uma estimativa em T ou q dessas integrais.

Este lema fornece um teste de sinal para qualquer cálculo posterior: se ele inclui ambos os conjuntos sem separar suas contribuições, não pode extrair a soma positiva pretendida.

## 2. Modelo CUE: média de razões exata

Fonte primária arquivada: Conrey–Farmer–Zirnbauer, arXiv:0711.0718v1, pp.8–9, Teorema4.1, eq.(4.4); p.9 conferida visualmente nesta continuação. A fonte afirma validade para todos os tamanhos. Usamos N≥1 e a especialização K=L=0, Q=R=1, shifts iguais ε>0. Não há deslocamento de numerador enviado ao infinito.

Para U em U(N) com medida de Haar normalizada e ΛU(z)=det(I−zU*) (a troca U↔U* não altera esta média),

    E[1/|ΛU(e^(−ε))|²] = 1/(1−e^(−2ε)).

A invariância por rotação torna a mesma média válida em e^(−ε+iθ). Logo, para qualquer N≥1,

    C_N(ε) := (ε/π) E∫_0^(2π) |ΛU(e^(−ε+iθ))|^(−2) dθ
             = 2ε/(1−e^(−2ε)).

Tonelli justifica a troca aqui: o integrando é não negativo e a média é finita para ε>0. A expansão é

    C_N(ε)=1+ε+ε²/3−ε⁴/45+O(ε⁶).

Os termos em ε são viés de regularização. Não são correções em N, nem coeficientes inferiores de momentos de L. O tamanho N desaparece da expressão exata deste controle.

## 3. Momento discreto CUE: cálculo independente

Quase certamente os ângulos θ1,…,θN são distintos. Com zj=e^(iθj), a regularização radial para uma matriz fixa dá

    limε→0 (ε/π)∫_0^(2π)|ΛU(e^(−ε+iθ))|^(−2)dθ
        = Σj |ΛU'(zj)|^(−2).

A aproximação local usa 1−e^(−ε)~ε e |zj|=1. A integração é no círculo inteiro, portanto não aparece a semimassa de uma borda artificial de intervalo.

Não deduzimos a esperança desse limite por uma troca não demonstrada. Calculamos diretamente com a densidade CUE dos ângulos rotulados:

    p_N(θ)= |Δ(e^(iθ1),…,e^(iθN))|² / [N!(2π)^N].

Em cada parcela j,

    |ΛU'(zj)|²=∏m≠j |zj−zm|².

O denominador cancela exatamente os fatores de Vandermonde que envolvem zj. A integral restante é a normalização de N−1 partículas, (N−1)!(2π)^(N−1), vezes 2π pela coordenada j. Cada parcela tem esperança1/N; somando N parcelas,

    E Σj |ΛU'(zj)|^(−2)=1,  N≥1.

A normalização usada também se verifica sem integração numérica: expandir o determinante de monômios da Vandermonde e usar a ortogonalidade das exponenciais no círculo deixa N! termos. Para N=1, a Vandermonde vazia vale1 e o resultado é imediato.

Assim, neste modelo, o momento discreto exato e o limite da média de razões coincidem, ambos1. Essa coincidência é estabelecida por dois cálculos, não presumida pela troca de limites. É um controle conhecido e consistente com o fator HKO em k=−1; não o apresentamos como novidade.

## 4. O que este controle resolve, e o que não transfere

Resolve no modelo:

- normalização do limite singular e do momento discreto;
- ausência de correção de tamanho N para este momento CUE específico;
- separação entre termos do deslocamento ε e termos da variável de tamanho;
- sinal dos polos de um contorno deslocado por cálculo local independente.

Não resolve para L:

- controle uniforme da média de razões até ε=0;
- coeficiente singular do resto além da diagonal aritmética;
- efeitos de condutor, extremos e altura2t no numerador de C8;
- presença ou ausência dos termos inferiores pedidos por Andrew.

Multiplicar o resultado CUE pelo fator A_q reproduz a constante prevista em C7 como modelagem formal; não estabelece a precisão da aproximação por L nem suas correções. Para C8 não foi definido um numerador CUE justificado que reproduza L(2s,χ²); nenhuma extensão foi presumida.

## 5. Próximo alvo mais preciso

R3 passa a exigir uma expressão para a média L que retenha o coeficiente de1/ε, em um regime de médias suficientemente largo e com erro cujo comportamento no deslocamento seja declarado. A opção por contorno precisa separar os dois conjuntos de polos antes de fazer qualquer simplificação. O controle CUE acima é uma referência exata que a fórmula proposta deve recuperar quando seus fatores aritméticos forem retirados no modelo correspondente.

Um termo finito B_j da diagonal continua insuficiente: o controle mostra explicitamente como uma série em deslocamento pode existir sem representar uma expansão subprincipal na variável de tamanho. Não foi escolhido um ajuste de termos inferiores aos dados.

## 6. Execuções e limites

Declaração prévia: results/razoes_contornos_cue_20261013/DECLARACAO.md e .sha256. Código científico novo: src/riemann_spectra/negative_moments_contours.py; testes: tests/test_negative_moments_contours.py.

Primeira execução: 1 falha, 13 aprovações. O teste adicionava monotonicidade estrita do erro que não constava da declaração. Para polinômio linear com H=1, o resultado é exato para todoδ; discrepâncias ~10^−49 são arredondamento e não têm monotonicidade. Teste e saída preservados; adendo gravado antes da correção permite piso1e−40 nesse requisito adicional. Fórmulas, grade e tolerâncias declaradas permanecem.

Verificações B, não certificação intervalar: resíduos em 1/2+it artificial, círculo isolado, quadratura angular N=1 e série em ε. Nenhuma amostra Haar/Monte Carlo foi gerada, nem integrados numericamente N>1: a identidade para todos N é analítica. Sem zeros reais, tabelas MN, H-004 ou dados reservados. Nenhuma publicação ou commit.

Execução corrigida: **14 testes passaram**, parede4,677s, CPU4,258s (processo de pytest, sem filhos computacionais), teto60s. Cinco testes novos e nove pertinentes existentes. Primeira falha permanece registrada no adendo e resultado_exec1.json.
