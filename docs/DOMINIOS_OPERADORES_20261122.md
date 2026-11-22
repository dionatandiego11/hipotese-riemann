# Domínios do gerador de primos e do operador aritmético de Collatz

22/11/2026. Continuação de `ATAQUE_OPERADOR_PESO_ARITMETICO_20261122.md`. Derivações A nas hipóteses indicadas, controles B declarados. Novidade não estabelecida. A frente Hamiltoniano usa a fórmula explícita e RH para a positividade do núcleo, com a atribuição externa já registrada. A frente Collatz abaixo é incondicional e não assume convergência de órbitas positivas.

## 1. O vetor básico não pertence ao domínio do Hamiltoniano

Seja μ=Σ_γ m_γ/(γ²+1/4) δ_γ e H a multiplicação por λ em L²(μ), representação do gerador obtido pelo núcleo de primos. O vetor v_t corresponde a e^(itλ). Sua norma é finita, mas

    ∥H v_t∥² = Σ_γ m_γ γ²/(γ²+1/4) = ∞,

pois há infinitas ordenadas com |γ|→∞. Logo nenhum v_t está em D(H). Derivar formalmente esses vetores como se fossem vetores de energia finita seria um erro de domínio. A realidade do espectro não elimina esse problema.

Isso é visível sem tabela de zeros. Para 0<h<log2 a soma prima não tem termos não nulos, de modo que G(e^h)=e^h(1+γ−h). O resto trivial da nota anterior satisfaz

    R'(h)=e^h atanh(e^−h)−1
         = 1/2 log(2/h)−1+O(h log(1/h)).

Integre de0 a h e use K(h)=e^−h/2[G(e^h)−log(2π)−R(e^h)]. Obtém-se

    K(0)−K(h)=1/2 h log(1/h)
              +1/2(1−γ−log(2π))h+O(h²log(1/h)).        (1)

Consequentemente,

    ∥(v_h−v_0)/h∥² = 2[K(0)−K(h)]/h²
       = [log(1/h)+1−γ−log(2π)+O(h log(1/h))]/h → ∞.

A expansão é analítica, pelo comportamento elementar de log/exponencial, não ajuste numérico. A constante γ nesta seção é Euler; as ordenadas γ nos somatórios têm seu significado espectral habitual.

## 2. Domínio denso por vetores suavizados

Para f em C_c^∞(R), defina v_f=∫f(t)v_t dt. A integral existe em norma, pois ∥v_t∥ é constante e f é integrável. Na representação espectral,

    v_f(λ)=f_hat_+(λ)=∫f(t)e^(itλ)dt,
    H v_f = i v_{f'},    H^j v_f = i^j v_{f^(j)}.

O sinal +i decorre da convenção U(a)=exp(iaH) e do Fourier com +itλ. Todas as derivadas de f têm suporte compacto, e sua transformada tem decaimento mais rápido que qualquer potência; como μ é finita, v_f pertence a D(H^j) para todo j. A ação diferencial é sobre os coeficientes f com produto interno não local definido por K, não uma demonstração de partícula livre em L²(dt).

O conjunto D₀={v_f:f em C_c^∞} é denso: se g é ortogonal a ele, a transformada de Fourier da medida finita g μ é nula como distribuição; pela unicidade, g=0 em L²(μ). A medida é finita por Cauchy–Schwarz.

Esse domínio é um núcleo essencialmente autoadjunto para H. Para conferir as deficiências, se g é ortogonal a (H±i)D₀, a medida localmente finita (λ±i)conjugado(g)μ define uma distribuição temperada cuja transformada é nula. Ela é temperada porque ∫(1+|λ|)^−2 |λ±i||g|dμ é finita por Cauchy–Schwarz e μ finita. Portanto essa distribuição é zero e g=0. Os dois espaços de deficiência são nulos; o operador simétrico em D₀ tem fecho autoadjunto, que coincide com H. O sinal na medida depende da convenção de produto interno; a conclusão usa que ambos λ+i e λ−i não se anulam na reta.

Temos agora um domínio explícito sobre o qual a derivada faz sentido. Stone e o método de suavização são conhecidos; [notas de teoria espectral](https://perso.univ-rennes1.fr/christophe.cheverry/spectral-theory.pdf) e [notas de representações unitárias](https://www.math.fau.de/wp-content/uploads/2024/01/rep14.pdf) foram identificadas como referências para conferência, sem alegar leitura integral nesta etapa.

**Energia positiva:** H tem espectro simétrico e ilimitado nos dois sentidos. O candidato não tem limite inferior de energia. |H| é autoadjunto e não negativo; a restrição ao subespaço par f(−λ)=f(λ) seleciona uma cópia por ordenada positiva distinta. Essa mudança preserva uma realização espectral, mas troca a dinâmica e não fornece posição, potencial ou localidade. O problema de geometria física permanece.

## 3. O peso de denominadores não vive como função contínua em Z₂

Seja A=Q∩Z₂, o conjunto dos racionais com denominador reduzido ímpar. Para s>0, w_s(x)=d(x)^−s é definido em A. Tome

    x_k=1+2^k/5^k.

Seu denominador reduzido é5^k e x_k→1 em Z₂, pois |x_k−1|₂=2^−k. Contudo w_s(x_k)=5^(−ks)→0 e w_s(1)=1. Logo **não existe extensão contínua a Z₂** que preserve esses valores. Em particular, não se pode simplesmente colocá-lo no operador usual de funções Hölder no espaço compacto 2-ádico.

A também é contável e de medida de Haar zero. Se estendermos w_s por0 fora de A, ele representa a função nula em L²(Haar); o operador ponderado usual seria nulo como operador de classes quase em toda parte. Outras extensões mensuráveis podem dar operadores diferentes, mas os valores em A não determinam sua classe de Haar. Essa obstrução diz respeito ao espaço e peso propostos; não exclui medidas ou espaços aritméticos alternativos.

## 4. Transferência bem definida nos racionais

Em ℓ²(A), com medida de contagem, considere

    (L_s f)(y)=w_s(2y)f(2y)
               +w_s((2y−1)/3)f((2y−1)/3),   s>=0.       (2)

As duas preimagens são racionais de denominador ímpar, uma par e outra ímpar, e T as envia para y. Toda coordenada x contribui para exatamente uma saída T(x). Como 0<w_s<=1,

    ∥L_s f∥² <= 2 Σ_x |f(x)|²,    ∥L_s∥<=sqrt2.

O adjunto na base tem

    L_s* δ_y = w_s(2y)δ_{2y}
               +w_s((2y−1)/3)δ_{(2y−1)/3}.

Para y=3k+2, k inteiro, as duas preimagens são inteiras, logo seus pesos são1. As fibras de y distintos são disjuntas e

    L_s L_s* δ_{3k+2}=2δ_{3k+2}.

Isso prova ∥L_s∥=sqrt2 para todo s>=0 e prova que **L_s não é compacto**, pois L_s L_s* tem autovalor2 com multiplicidade infinita. Não é operador de classe de traço, nem se obtém dele diretamente um determinante de Fredholm usual. A penalização do denominador não amortece o setor infinito dos inteiros.

## 5. O que a zeta periódica representa nesse espaço

Para cada x em A, o coeficiente diagonal de L_s^n é zero salvo se T^n x=x; nesse caso vale Π_{j=0}^{n−1}w_s(T^j x). Como os denominadores são invariantes nas órbitas periódicas, a soma desses coeficientes é exatamente Z_n(s) da rodada anterior. Há2^n pontos fixos, logo a soma diagonal é finita para cada n.

Isso é uma **soma diagonal na base escolhida**, não a afirmação de que L_s^n possui um traço canônico de classe de traço. A zeta periódica exp(ΣZ_n(s)z^n/n) continua definida para |z|<1/2; a identidade com det(I−zL_s)^−1 não foi estabelecida e o determinante usual é inaplicável ao L_s acima.

Em particular, já em s=0 temos Z_n(0)=2^n, enquanto ∥L_0∥=sqrt2. A comparação reforça que o crescimento da contagem de pontos periódicos não deve ser identificado com o traço usual ou raio espectral desse operador em ℓ²(A).

## 6. Controles e próximo alvo

Declaração anterior: `results/dominios_operadores_20261122/DECLARACAO.md`, SHA-256 `880770ff38936a3534de3fe36b0b0c42b71421719c115b0daa1bd6a3235e4774`. Código novo em `collatz/denominator_transfer.py`; kernel da rodada anterior preservado. Testes independentes de ação/adjunto em preimagens, testemunhas racionais de não compacidade e de descontinuidade e derivada de R por diferenciação numérica. A tabela da expansão(1) é diagnóstico a80 dígitos, não prova/certificado intervalar. Nenhuma ordenada de zero foi usada.

**Execução:**4 testes passaram em0,12s; CPU acumulada0,693161s, parede0,911943s, teto30s. Oito fibras y=2,5,...,23 deram Gram exato2I e L_sL_s*δ_y=2δ_y. Oito testemunhas x_k verificaram denominadores e distância2-ádica exatamente. O diagnóstico da constante2(K(0)−K(h))/h−log(1/h) passou de−1,397690668 em h=0,01 para−1,415092714 em h=1e-8, contra o limite analítico−1,415092731. Não se inferiu taxa da tabela; a expansão é derivada na§1. Hashes do código/saídas e do código congelado da rodada anterior foram conferidos.

**Alvo seguinte:** para H, investigar representação geométrica do produto interno não local e uma dinâmica de energia positiva, com comparação a Weil/Suzuki. Para Collatz, qualquer tentativa de operador compacto terá de controlar também o tamanho dos inteiros, e não só denominadores, ou trabalhar com outro tipo de traço. Antes de escolher uma medida que faça isso, determinar o efeito da nova norma sobre ação de T e sobre as contagens; amortecer numericamente as saídas alteraria o problema. As obstruções desta nota delimitam a construção, não provam impossibilidade de uma ponte.
