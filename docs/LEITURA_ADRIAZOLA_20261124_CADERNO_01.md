# Caderno de leitura 01 — janelas, positividade e matrizes de Gram

Fonte e revisão: PDF de Jimmie Adriazola arquivado em `archive/leituras/adriazola_20261124/`, SHA-256 `8ced945d3a2fcf7fb7a2a760db6859416cd8db2ed11617d8bc28b43b82ed3a94`. Páginas indicadas segundo a numeração impressa. Este caderno é uma análise localizada; não certifica as provas restantes nem afirma que todo o manuscrito foi lido linha por linha.

## 1. Critério de janelas — pp. 7–11

### Enunciado e quantificadores

O Teorema 2.4 considera uma função real mensurável H em [1,∞), com |H(x)| ≤ Bx, cuja transformada de Mellin inicialmente definida para Re(s)>1 admite continuação meromorfa. Para um θ em [0,1), exige que os polos com parte real maior que θ sejam simples, tenham parte real menor que 1, e que todo polo real nessa região tenha resíduo positivo.

Se existem **constantes fixas** λ>1 e C tais que, para valores arbitrariamente grandes de Y, a desigualdade H(x) ≤ Cx^θ vale **para todo x** em [Y,Y^λ], o enunciado conclui que não há polos com Re(s)>θ. Aqui é essencial não trocar «arbitrariamente grandes» por um intervalo finito, nem «todo x da janela» por uma malha finita. O teorema é unilateral: ele não pede |H(x)| ≤ Cx^θ na janela.

### Mecanismo da prova

O texto escolhe um ponto real σ₁>1 e considera coeficientes de Taylor da transformada. Um polo mais próximo força coeficientes grandes e positivos para uma sequência frequente de índices: se o polo é real, usa-se o sinal positivo do resíduo; se é um par conjugado, usa-se o Lema 2.2 para encontrar fases com cosseno positivo. Os núcleos dos coeficientes se concentram em uma faixa logarítmica. A cota uniforme sobre [Y,Y^λ] controla a faixa central, enquanto |H(x)| ≤ Bx controla as duas caudas. Os limites são incompatíveis quando Y cresce.

Essa é uma leitura do argumento apresentado: não foi feita aqui uma auditoria independente de todos os detalhes de convergência e das referências que sustentam a continuação e os fatos sobre funções L.

### Positividade da família

No Corolário 2.5, toma-se uma família finita de caracteres e uma combinação com **pesos positivos fixos**. Em cada zero, a contribuição ao coeficiente do resíduo é uma soma de multiplicidades não negativas, inclusive as dos caracteres conjugados; portanto, a ausência de polo não decorre de cancelamento entre multiplicidades. A positividade é uma parte matemática da redução, e um resultado numérico para poucos zeros não prova a hipótese de janela.

O Teorema 6.3, pp. 43–44, enuncia explicitamente a dedução para cada caráter primitivo **assumindo o Teorema A**. O Teorema A, pp. 42–43, contém uma ordem de quantificadores importante: para cada caráter e ε admissível obtêm-se janelas arbitrariamente altas, e para **cada x** da janela devem existir dados e pesos com as propriedades exigidas. Os dados podem depender de x; isso não elimina a exigência de uma cota na janela inteira. A conexão entre os dados variáveis e a combinação positiva precisa manter os coeficientes e constantes exigidos pelo Corolário 2.5; não a verificamos integralmente nesta rodada.

## 2. Gram: o que o Lema 13.4 fornece — pp. 148–149

Para matrizes Aᵢ e pesos γᵢ>0, o artigo define Q=ΣᵢγᵢAᵢAᵢ*. O lema usa simultaneamente:

1. um controle agregado de Σᵢ‖γᵢAᵢ*Aᵢ−I‖²_HS;
2. uma cota superior de tr(Q²) relativa a (tr Q)²/D;
3. uma cota para a soma das codimensões dos subespaços Uᵢ.

Sua conclusão limita a **dimensão do complemento ortogonal** da soma das imagens Aᵢ(Uᵢ). É uma afirmação de posto/cobertura em dimensão finita, não uma estimativa pontual de cada autovalor nem, automaticamente, uma cota uniforme para a inversa de Q.

### Exemplo elementar de limitação

Para cada D≥2, tome Q_D=diag(0,1,…,1). Então tr(Q_D)=D−1 e tr(Q_D²)=D−1. A condição

`tr(Q_D²) ≤ (1+η)(tr Q_D)²/D`

vale com η=1/(D−1), que tende a zero, embora o menor autovalor seja exatamente zero para todo D. É possível realizar essa matriz como soma de AᵢAᵢ*, tomando D−1 vetores unitários da base e γᵢ=1; o defeito individual de normalização é zero. O exemplo é compatível com a conclusão de cobertura proporcional do lema e mostra por que ela não é um hiato espectral.

Para obter inversibilidade quantitativa, seria necessário um ingrediente adicional, por exemplo uma desigualdade coerciva Q ≥ cI com c>0 uniforme, ou outra estimativa que controle também os autovalores pequenos. A demonstração de um desses ingredientes para operadores de Collatz permanece aberta; nenhuma associação direta ao sistema de Adriazola foi estabelecida.

## 3. Próxima leitura dirigida

- Verificar a passagem completa da §6.3 ao Corolário 2.5, incluindo os coeficientes fixos e a dependência em ε e no caráter.
- Examinar o enunciado e a prova da Hipótese 18.10 e rastrear as constantes das sete desigualdades, sem confundir hipótese do manuscrito com teorema demonstrado.
- Se o objetivo for Collatz, definir uma família finita de operadores de ramos, o espaço e os pesos, e primeiro testar em álgebra exata se o análogo do controle de Gram identifica só posto ou uma coercividade efetiva. Esse seria um novo problema, não uma consequência da prova da zeta.
