# Ataque ao Hamiltoniano e a Collatz a partir da redução de Riemann

22/11/2026. Nota de trabalho: duas perguntas distintas e um controle comum. As conclusões sobre RH são atribuídas às verificações externas identificadas em `ARQUITETURA_ALPOGE_20261122.md`; a expressão para G abaixo é da exposição em desenvolvimento de Rubinstein e colaboradores, §I.1. Não auditamos a prova Lean ou os candidatos de operador. Hipóteses novas são D; derivações são A sob as condições declaradas. Novidade bibliográfica não estabelecida.

## 1. Porta de entrada comum

Defina G(x)=Σ_{n<=x}Λ(n)(x/n−1)−x(log x−1−γ), para x>1. Na [exposição consultada](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper.pdf),

    G(x)=log(2π)−Σ_ρ x^ρ/[ρ(ρ−1)] + R_triv(x),
    R_triv(x)=O(x^−2),

com soma absolutamente convergente sobre zeros não triviais, contando multiplicidades. O símbolo R_triv representa a contribuição restante na fórmula citada; antes de um teste é obrigatório fixar sua expressão e cota, não ajustá-lo aos dados.

Usando RH, escreva ρ=1/2+iγ e t=log x>0. Então

    e^(−t/2)[G(e^t)−log(2π)−R_triv(e^t)]
      = Σ_γ e^(itγ)/(γ²+1/4).                              (1)

O lado direito é uma série absolutamente convergente e real, somando ±γ e multiplicidades. Essa identidade oferece um observável suavizado comum aos dois lados: primos e zeros. O ponto t=0 e a extensão para t<0 exigem as convenções da fórmula; como a medida espectral é simétrica, sua extensão natural é par. A expressão sem subtrair R_triv tem erro O(e^(−5t/2)) após normalização, para t grande; a constante ainda não foi determinada aqui.

## 2. Hamiltoniano: teste de traço do resolvente

Seja H autoadjunto, com espectro puramente discreto, multiplicidades finitas e (H²+1/4)^−1 de classe de traço. Se seus autovalores são precisamente as ordenadas γ, contadas com multiplicidade, então

    Tr[e^(itH)(H²+1/4)^−1] = Σ_γ e^(itγ)/(γ²+1/4).       (2)

Assim (1) propõe um **teste necessário**: calcular independentemente o traço suavizado de um candidato e comparar com o lado primo. A identidade global, para todo t real, com a medida espectral e a correção trivial fixadas, identifica a medida espectral ponderada pela unicidade da transformada de Fourier de medidas finitas. A equivalência integral requer demonstrar simetria, ausência de espectro adicional e as hipóteses analíticas; concordância em número finito de t não é suficiente.

**Controle negativo obrigatório:** em ℓ², H_diag e_j=γ_j e_j, com domínio {v:Σγ_j²|v_j|²<∞}, é autoadjunto e satisfaz (2) por construção quando se usam todas as ordenadas verdadeiras. Isso é um controle tautológico, não uma explicação dinâmica. O fato de RH tornar as ordenadas reais não seleciona domínio, interação, geometria ou um Hamiltoniano físico. O resultado externo fornece a realidade para ζ no escopo verificado, não a simplicidade dos zeros.

**Alvo H-P1 (D):** existe uma classe de operadores definida sem inserir os zeros, com domínio, auto-adjunticidade e espectro especificados, cujo traço (2) reproduza a função do lado primo sem ajustar constantes por zero. Enunciar primeiro uma família concreta e um teorema de traço. Comparar com H_diag, um controle de espectro conhecido e o resultado estabelecido de [Connes](https://arxiv.org/abs/math/9811068), onde o espectro de absorção tem interpretação e sinal próprios. Não substituir uma identidade de emissão por absorção sem estabelecer a tradução.

**Critério de progresso:** para cada família, registrar lei de contagem, tipo de espectro, fórmula de traço, termo suave, sinal e multiplicidades; uma violação demonstrada em hipóteses precisas exclui aquela família, não todo operador. Em implementação futura, usar um alvo t e uma incerteza pré-definidos, referência sem zeros inseridos, e um candidato cujo traço seja efetivamente calculável; um teste discreto apenas discrimina candidatos naquela resolução.

## 3. Collatz: controle exato que separa dinâmica e aritmética

No mapa acelerado por paridade T(x)=x/2 para x par e (3x+1)/2 para x ímpar sobre Z₂, a conjugação ao deslocamento binário é um resultado conhecido de [Bernstein–Lagarias](https://websites.umich.edu/~lagarias/doc/bernstein.pdf). Por isso, o número de pontos fixos de T^n em Z₂ é 2^n e a zeta formal de pontos periódicos é

    ζ_T(z)=exp(Σ_{n>=1} #Fix(T^n) z^n/n)=1/(1−2z),   |z|<1/2.

Esta conta inclui todos os pontos periódicos 2-ádicos, com a convenção de pontos fixos de T^n; não é uma contagem dos ciclos inteiros positivos. A zeta sem peso nessa escolha de espaço não apresenta os zeros não triviais da zeta de Riemann. Esse é um **controle negativo para uma ponte ingênua**, não uma impossibilidade para outros espaços, pesos ou observáveis. Não inferir a conjectura de Collatz da conjugação: quais pontos 2-ádicos correspondem a inteiros positivos continua sendo informação aritmética adicional.

**Alvo C-P1 (D):** especificar um peso aritmético independente dos zeros, uma função-teste e um operador de transferência de ramos que produza um objeto não trivial, com domínio, convergência e significado definidos. Primeiro demonstrar que distingue o mapa 3x+1 de outro mapa com a mesma dinâmica simbólica; depois buscar uma relação precisa com a soma (1). A sintonia artificial de pesos com os zeros é controle de ajuste, não ponte explicativa.

**Primeiro teste finito proposto:** comparar T e o deslocamento binário S conjugado em palavras de paridade de comprimentos pequenos fixados antecipadamente. Controle 0: peso constante, onde os dois sistemas têm zeta 1/(1−2z). Desafio: escolher previamente um peso aritmético que não seja apenas transportado pela conjugação, provar ou calcular o efeito, e verificar se a diferença persiste sob normalização. Um resultado diferente mostra dependência do peso; por si só não aproxima ζ de Riemann nem prova convergência de Collatz. Controles e dados independentes devem ser declarados antes de qualquer rodada.

## 4. Sequência com critérios de parada

1. **H-P0:** conferir rigorosamente (1), incluindo a expressão de R_triv, o domínio em t e a soma com multiplicidade; calcular (2) exatamente para H_diag como controle, sem chamá-lo descoberta. Um piloto finito é apenas aproximação e precisa limitar a cauda dos zeros.
2. **H-P1:** escolher uma classe existente da matriz bibliográfica, ler fonte e especificar domínio/traço. Só executar quando houver uma previsão independente da lista de zeros e incerteza; excluir a classe se ela violar o critério no escopo provado.
3. **C-P0:** conferir conjugação, pontos periódicos e zeta formal. Este controle é fechado por argumento simbólico, sem enumeração extensa.
4. **C-P1:** definir peso aritmético e espaço, registrar o enunciado e suas hipóteses, e verificar primeiro se a literatura já estudou o mesmo peso. Um experimento tem que diferenciar T de S no peso escolhido; caso contrário, reformular ou encerrar essa construção.
5. **Ponte:** exigir uma identidade entre objetos efetivamente definidos, incluindo normalização, domínio e erros. Sem essa identidade, manter as frentes separadas.

Nenhum experimento, alteração dos resultados anteriores ou prova de relação Collatz–Riemann foi feito nesta nota. RH não resolve Collatz nem produz automaticamente o operador físico. Revisão independente e investigação bibliográfica continuam necessárias.
