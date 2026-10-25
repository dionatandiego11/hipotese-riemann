# Syracuse: energia com custo total fixado

**Correção de convenção em19/10:** os limites na ordem cronológica foram invertidos nesta revisão. A cota geral permanece válida; a identificação anterior da distribuição com os geradores não era correta. [Diagnóstico, testemunha e verificações](SYRACUSE_REESCRITAS_CUSTO_20261019.md). Cópia anterior preservada no diretório dessa execução.

19/10/2026. Estado da derivação: `validado` no escopo abaixo, sem revisão independente. A: consequências matemáticas com hipóteses explícitas; B: verificações finitas exatas. Novidade **não estabelecida**. T008 continua `em execução`: esta nota não fecha a questão de cobertura de resíduos nem a conjectura de Collatz.

## 1. Resultado e objeto

Sejam a_1,...,a_ell geometrias positivas independentes com Pr(a_i=j)=2^{-j}. A palavra aplica cronologicamente Phi_a(x)=(3x+1)/2^a. Para S=sum a_i,

    Phi_w(x)=(3^ell x+B(w))/2^S,
    B(w)=sum_{i=0}^{ell-1} 3^{ell-1-i} 2^{A_i},
    A_i=a_1+...+a_i, A_0=0,
    r(w)=2^{-S}B(w) mod 3^ell.

Fixe s>=ell e qualquer evento E contido em {S=s}, com probabilidade beta>0. E pode impor limites individuais e outras restrições às palavras. Seja p_E a lei de r(w) condicionada a E e

    Energia(E)=3^ell sum_v p_E(v)^2.

**Proposição:**

    Energia(E) <= 2 H(ell,s)/beta^2 <= 4/beta^2.                 (1)

Aqui H é um coeficiente explícito, não uma hipótese não demonstrada. A prova não requer RH, conjectura de Collatz ou mistura de Tao. Usa a injetividade por custo/resíduo conferida na fonte de Valbuena, cujo argumento elementar é reproduzido abaixo. A passagem à faixa central dos custos usa a estimativa de beta previamente derivada no projeto, identificada na §5.

A lei é de palavras aleatórias condicionadas. Não é uma amostra de órbitas positivas nem uma lei limite no comprimento. Cada ell define um objeto finito distinto.

## 2. Auditoria do antecedente

Fonte: Lucas Valbuena, *Quadratic cylinder energy and integrability of the Syracuse law*, commit a7275d5a73814d3d9a400c6fe6577de9542b03a3, [TeX do autor](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/quadratic-cylinder-energy.tex). Cópia e SHA em [nota de leitura](../hipoteses/leituras/SYRACUSE_ENERGIA_20261018.md). Numeração abaixo é da cópia TeX arquivada, não da renderização web.

Leitura ampliada às linhas 117–381. Conferidos:

- 143–195: decodificação da palavra a partir do numerador, com custo fixado, e contagem dos quocientes distintos;
- 198–298: Cauchy–Schwarz ponderada, lei inclinada normalizada, momentos geométricos e passagem monótona ao custo infinito. Sustentam E_K<=24K+8K²;
- 300–381: interpolação entre mistura L1 de Tao e energia quadrática, somabilidade dos incrementos em Lp, 1<p<2. O expoente escolhido A>(4p-2)/(2-p) dá expoente menor que -2. O argumento é válido aceitando a mistura citada;
- reconferida a normalização de Tao na cópia 1909.03562v5, p.11, Prop.1.14, eqs.(1.23)–(1.24). A fonte de Valbuena cita outra versão com outra numeração; não substituir os números silenciosamente.

Não foi encontrado erro nesses passos. Isso é auditoria matemática interna de um manuscrito do autor, não revisão editorial externa ou certificação Lean. A prova global de Tao e os artefatos Lean não foram reexecutados. A prova de f não pertencer a L2 já havia sido lida em 18/10. A combinação fornece, para a lei canônica, o intervalo de integrabilidade 1<=p<2, com Tao como entrada externa.

A adaptação abaixo evita a soma sobre todos os custos: no problema condicionado, S já está fixado. Não reivindicamos essa adaptação como inédita.

## 3. Contagem dentro de uma fibra

Se ell>=2,

    B(w)-3^{ell-1}=2^{a_1} B(a_2,...,a_ell).

O numerador do sufixo é ímpar. A valoração 2-ádica recupera a_1; divisão e indução recuperam o sufixo, com o último expoente determinado pelo custo total. Para ell=1, o custo já determina a palavra.

Na fibra de custo s e resíduo v, B(w) tem resto fixo 2^s v mod 3^ell. Assim q(w)=floor(B(w)/3^ell) assume inteiros não negativos distintos. Se m_E(v) é o número de palavras de E na fibra, e Y=B/3^ell, ordenar esses quocientes dá

    m_E(v)^2 <= 2 sum_{w em E, r(w)=v} (1+Y(w)).               (2)

Se N_E é o número total de palavras de E, todas têm o mesmo peso 2^{-s}. Portanto beta=N_E 2^{-s}, p_E(v)=m_E(v)/N_E e

    Energia(E) <= (2/beta²) sum_{w em E} 3^ell 4^{-s}(1+Y(w))
               <= (2/beta²) H(ell,s),                          (3)

onde

    H(ell,s)=E_inclinada[(1+Y) 1_{S=s}],
    Pr_inclinada(a=j)=3*4^{-j}.

A segunda desigualdade só remove o indicador de E mantendo S=s; todos os termos são não negativos. Não divide uma soma de Fourier sujeita a cancelamentos. Essa distinção mantém intacta a ressalva da nota de regularidade sobre caracteres condicionados.

## 4. Cálculo do momento mantendo o custo fixado

Defina as funções geradoras normalizadas

    b(z)=3z/(4-z),    f(z)=z/(2-z).

Multiplicar o peso inclinado por 2^{A_i}/3^i troca as primeiras i coordenadas pela lei usual e deixa as demais inclinadas. Como Y=(1/3) sum_{i=0}^{ell-1} 2^{A_i}/3^i,

    H(ell,s)=[z^s]{b(z)^ell + (1/3) sum_{i=0}^{ell-1} f(z)^i b(z)^{ell-i}}.

A soma geométrica finita dá, como identidade de séries em torno de z=0,

    (1/3) sum_i f^i b^{ell-i}
       = (2-z)/(2(1-z)) (b^ell-f^ell).

O aparente denominador 1-z é usado apenas na extração de coeficientes; não se avalia a expressão separada em z=1. Escreva b_s=[z^s]b^ell, f_s=[z^s]f^ell, B_s=sum_{j<=s}b_j e F_s=sum_{j<=s}f_j. Então

    H(ell,s) = (3/2)b_s - (1/2)f_s + (1/2)(B_s-F_s).           (4)

São massas e probabilidades acumuladas de somas de geometrias. Logo

    0 <= H(ell,s) <= (3/2)b_s + (1/2)B_s <= 2.                (5)

A positividade vem da primeira expressão, sem cancelamento; a cota superior usa apenas f_s,F_s>=0 e b_s,B_s<=1. Explicitamente,

    b_s=binom(s-1,ell-1) 3^ell/4^s,
    f_s=binom(s-1,ell-1)/2^s,

ambas zero para s<ell. (3)–(5) provam (1). As constantes são deliberadamente conservadoras.

## 5. Aplicação aos custos do projeto e uniformidade

O evento existente é

    E_{ell,k}={sum a_i=ell+k; a_i<=2*3^{i-1}, i=1,...,ell},
    aqui na ordem cronológica de composição.

A nota de regularidade escreve o evento na ordem da raiz para a folha, com limites decrescentes e offset F_ell(a_ell,...,a_1). Para usar a composição cronológica r(w) desta nota, invertem-se conjuntamente a palavra e seus limites. Esta correção não altera a contagem total nem a probabilidade do evento, que é

    beta_{ell,k}=q_ell(k) 2^{-(ell+k)}.

Consequentemente, para qualquer evento não vazio, sem assíntota,

    Energia(E_{ell,k}) <= 4 * 4^{ell+k}/q_ell(k)^2.             (6)

A nota [custo conjunto, §3](../hipoteses/COLLATZ_CUSTO_CONJUNTO_20261012.md) e a [identificação do evento, §6](../hipoteses/COLLATZ_REGULARIDADE_PI_20261012.md) dão beta>=b_C/sqrt(ell) para |k-ell|<=C sqrt(ell), ell suficientemente grande, com C fixo e b_C>0 não avaliada. Usando esse resultado anterior,

    Energia(E_{ell,k}) <= (4/b_C²) ell                         (7)

uniformemente nessa janela. A desigualdade (1) é explícita; a constante de (7) para os limites individuais do projeto não foi numericamente avaliada ou certificada.

Como exemplo **distinto**, sem limites individuais e com s=2ell,

    beta=(1/2) binom(2ell,ell)/4^ell >= 1/(4 sqrt(ell)),
    Energia(S=2ell) <= 64ell.                                 (8)

A desigualdade binomial segue por indução: d_ell=binom(2ell,ell)/4^ell, d_1=1/2, d_{ell+1}/d_ell=(2ell+1)/(2ell+2)>=sqrt(ell/(ell+1)); ao quadrado, a diferença dos numeradores é 1. A constante 64 NÃO é atribuída ao evento com limites individuais.

A projeção da mesma lei condicionada a módulo 3^K, K<=ell, não aumenta a energia normalizada (Jensen por fibras). Não identifica as leis em comprimentos diferentes nem prova existência de uma densidade limite condicionada.

## 6. O que fica controlado e o que permanece aberto

Por Cauchy–Schwarz, para qualquer conjunto R de resíduos,

    p_E(R) <= sqrt(|R| Energia(E)/3^ell).

Além disso,

    |suporte(p_E)| >= 3^ell/Energia(E) >= beta² 3^ell/4.

Na janela central isso garante suporte de pelo menos c_C 3^ell/ell. É uma forma de controle da concentração agregada na resolução completa, mesmo após fixar custo e limites. Pode ser não informativa para ell pequeno; não é afirmação de preenchimento de todos os resíduos admissíveis.

Continuam abertos: uma minorante por resíduo, a dependência fina entre custo e localização residual, crescimento exato da energia condicionada e uma consequência sobre órbitas positivas. Uma lei uniforme sobre apenas uma fração dos resíduos já mostra por que uma cota de energia não garante cobertura total. Não é prova de Collatz ou ligação direta com os zeros de Riemann.

**Próximo alvo recomendado:** comparar (6) e a mistura condicionada já obtida com o requisito exato de cobertura do projeto. Identificar uma estimativa adicional suficiente para controlar os resíduos ausentes. Não iniciar enumeração extensa ou repetir o limiar Lp canônico. Na frente Riemann, o próximo alvo continua sendo a intensidade conjunta de gap e amplitude; este resultado não a fornece.

## 7. Verificação efetivamente realizada

Declaração em `results/energia_condicionada_20261019/DECLARACAO.md`, SHA-256 55eb3458d59cec8db23e490ffeba90c8ac0798a7712b38f92e7d6e596e91f148, anterior à implementação/enumeração, posterior ao rascunho analítico. Não é pré-registro anterior à formulação.

Comando:

    .venv/bin/python results/energia_condicionada_20261019/verificar.py

Dois testes passaram em 0,11s; execução total 0,416887s CPU, 0,420688s de parede, teto 30s. Inteiros e Fraction: 35 momentos por enumeração direta contra (4), 69 eventos não vazios para a cota e projeções, um evento vazio preservado sem normalização. ell=1,...,5, s=ell,...,3ell, com e sem limites decrescentes na ordem cronológica então usada. Esses eventos estão cobertos pela proposição geral, mas sua distribuição não é a dos geradores do projeto; a identificação corrigida foi conferida na execução de reescritas. Os scripts e resultados originais foram preservados. Conferidos também quocientes distintos e (8) nos casos centrais sem limites.

Isso detecta erros de implementação e convenção em casos pequenos; a prova geral é §§3–5. Sem zeros reais, reservados, órbitas positivas, Monte Carlo ou novo custo prolongado. Não foi repetida a suíte inteira. Código e manifesto copiados no diretório da execução. Sem commit ou push.
