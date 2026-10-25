# Da energia à cobertura: a estimativa adicional

**Correção de convenção em19/10:** os expoentes cronológicos têm limites crescentes2,6,18,... . A ordem inversa foi corrigida no evento e na prova da base módulo3. [Reescritas e auditoria da ordem](SYRACUSE_REESCRITAS_CUSTO_20261019.md). Versão anterior preservada no diretório de resultados.

19/10/2026. Formulação analítica e consequências elementares A; os critérios de preenchimento aplicados à lei do projeto são alvos D, ainda não demonstrados. Sem cálculo numérico, enumeração, alteração de protocolos ou afirmação de novidade.

Base: [energia condicionada](SYRACUSE_ENERGIA_CONDICIONADA_20261019.md), [mistura condicionada](../hipoteses/COLLATZ_MISTURA_CONDICIONADA_20261013.md) e [auditoria dos limites do L1](../hipoteses/COLLATZ_AUDITORIA_MISTURA_20261013.md). Nenhuma fonte externa nova ou resultado profundo adicional é usado nas deduções finitas desta nota.

## 1. Objeto e alvo

Fixe comprimento ell e custo k, evento E_{ell,k} não vazio:

    sum_i a_i=s=ell+k; 1<=a_i<=2*3^{i-1}.

A palavra aplica Phi_a(x)=(3x+1)/2^a cronologicamente, partindo de 0. Todos os caminhos de E têm o mesmo peso. Escreva p^r(a) para a probabilidade de seu resíduo módulo 3^r, 1<=r<=ell, sob o MESMO evento E. U_r é o conjunto das unidades módulo 3^r, com |U_r|=2*3^{r-1}. As outras classes são estruturalmente impossíveis.

**Alvo de cobertura:** p^ell(a)>0 para todo a em U_ell, com quantificadores de comprimento/custo declarados. Não se define o alvo como o suporte já observado, o que tornaria a pergunta circular. Esta cobertura é uma propriedade das palavras com custo fixado; uma consequência para a conjectura de Collatz exigiria um argumento adicional.

## 2. A cota de energia admite buracos

A cota atual é 3^ell sum_a p^ell(a)^2<=4/beta², com beta=Pr(E). Ela dá um suporte grande, mas não exige massa positiva em cada unidade.

Exemplo geral, não atribuído à lei de Collatz: para N=3^ell e M=|U_ell|=2N/3, a lei uniforme em M-1 unidades deixa uma unidade vazia e tem energia N/(M-1). Isso difere do mínimo N/M=3/2 por apenas

    N/[M(M-1)],

quantidade de ordem 3^{-ell}. Portanto até energia muito próxima do mínimo permite um buraco; uma majorante O(ell) não o exclui.

A mistura L1 também permite buracos. O exemplo já registrado na auditoria remove uma classe em cada fibra grossa e tem oscilação 2*3^{m-ell}. Isso é exponencialmente pequeno quando m é uma fração fixa de ell. O controle agregado e o L1 existentes não bastam, mesmo combinados: esse exemplo tem também energia próxima de 3/2.

## 3. Critério direto por erro relativo máximo

Fixe m<ell e levante uniformemente a projeção grossa:

    q(a)=3^{m-ell} p^m(a mod 3^m).

Se p^m(b)>0 para toda unidade b e, para algum delta<1,

    sup_{a em U_ell} |p^ell(a)-q(a)|/q(a) <= delta,             (R)

então p^ell(a)>=(1-delta)q(a)>0 para toda unidade. Se alpha_m=min_{b em U_m}p^m(b), a minorante é

    min_{a em U_ell}p^ell(a)>=(1-delta)*3^{m-ell}*alpha_m.

(R) é uma condição suficiente ainda não demonstrada. Requer controle dos piores resíduos, não somente média. Ela explicita a força necessária de uma rota por mistura; escrevê-la não resolve o problema.

A alternativa via L1 absoluto exigiria

    ||p^ell-q||_1 < 2*min_a q(a),                              (R1)

pois, se p^ell(a)=0, a soma das diferenças é zero e o defeito q(a) naquele ponto precisa ser compensado nos demais: a norma L1 é pelo menos 2q(a). Para m fixo, min q tem escala exponencial 3^{-ell}. O decaimento superpolinomial disponível não implica (R1). Não se trocou uma cota assintótica polinomial por uma exponencial.

## 4. Critério local: preenchimento de cada dígito

Uma formulação mais próxima dos geradores é: para 1<=r<ell, cada a em U_r com p^r(a)>0 e cada j em {0,1,2}, demonstrar

    p^{r+1}(a+j*3^r) >= (eta_{ell,k,r}/3)*p^r(a),              (P)
    eta_{ell,k,r}>0.

O parâmetro eta precisa valer para todas as classes e os três filhos naquele comprimento/custo/resolução. Pode depender desses parâmetros; uma constante uniforme positiva seria mais forte do que o necessário para mera cobertura. Normalizar eta<=1 não restringe uma cota válida.

Se as duas unidades módulo3 têm massa positiva, indução em r dá cobertura em U_ell e

    p^ell(a)>=p^1(a mod3)*3^{-(ell-1)}
              *prod_{r=1}^{ell-1}eta_{ell,k,r}.                (9)

Para cada ell finito, a positividade do produto basta. Uma minorante quantitativa uniforme requer controlar sua deterioração; não se assume que ela seja pequena ou grande.

**Base módulo3 no evento do projeto.** O resíduo é 2^{-a_ell} mod3; expoentes finais pares e ímpares produzem as duas unidades. Ambos são possíveis quando

    ell>=2; ell+1<=s<=3^ell-2.

De fato, as outras coordenadas têm soma mínima ell-1 e máxima R=3^{ell-1}-1 e percorrem todo o intervalo inteiro entre elas. Os expoentes finais possíveis formam o intervalo [max(1,s-R), min(2*3^{ell-1},s-ell+1)]. Para ell>=2 e s no intervalo exibido, ele contém pelo menos dois inteiros consecutivos, portanto as duas paridades. A janela s=2ell+O(sqrt(ell)) está contida nele para ell suficientemente grande. Esta base não prova (P) nas resoluções seguintes.

### Como transformar (P) num lema aritmético

Seja W_r(a) o conjunto de palavras de E com resíduo a mod3^r e N_r(a)=|W_r(a)|. Procurar transformações explícitas

    F_{r,a,j}: W_r(a) -> W_{r+1}(a+j*3^r)

que preservem comprimento, custo total e limites individuais, e cujas fibras tenham tamanho no máximo D_{ell,k,r}, simultaneamente nos a,j. Então

    N_{r+1}(a+j*3^r)>=N_r(a)/D_{ell,k,r},

o que prova (P) com eta=3/D, tomando D>=3. Esta construção é um alvo, não uma transformação que já tenhamos encontrado. Ela daria um mecanismo independente de preenchimento, em vez de presumir a minorante desejada. Para provar só existência, poderia haver um argumento mais fraco sem multiplicidades uniformes.

## 5. Obstrução a modificar apenas o prefixo

Divida a palavra em um prefixo não vazio e um sufixo v de r>=1 ramos. Mantendo esse sufixo fixo, seu mapa é

    Phi_v(x)=(3^r*x+B(v))/2^{t(v)}.

Qualquer prefixo não vazio termina em uma unidade 3-ádica x. Logo todas essas palavras caem na mesma classe

    a=2^{-t(v)}B(v) mod3^r,

e, módulo3^{r+1}, seus valores possíveis são no máximo as duas classes

    2^{-t(v)}(B(v)+3^r),
    2^{-t(v)}(B(v)+2*3^r).

São distintas; a terceira classe, correspondente a x=0 mod3, não pode ocorrer com esse sufixo. Se a é uma unidade, os três filhos de a são unidades: o filho faltante não é excluído pelo simples requisito de ser unidade.

Isso não demonstra um buraco na lei completa: outros sufixos podem preencher a classe. Mostra apenas que mexer no prefixo, mantendo um sufixo fixo, não prova (P) para seus três filhos. Uma estratégia de preenchimento deve combinar sufixos que preservem o resíduo grosso e o custo global, mudando o filho excluído. Não invalida as trocas de pares usadas no cancelamento de Fourier: elas tinham outro alvo.

## 6. Decisão de pesquisa

A estimativa adicional procurada é (P), ou uma alternativa como (R) que a substitua para cobertura total. A energia continua útil para limitar a concentração, mas não produz uma minorante por si só.

Próximo alvo matemático: construir, ou encontrar uma obstrução a construir, famílias de sufixos de mesmo custo que atinjam os três filhos de uma classe grossa, com limites individuais preservados. Antes de enumeração extensa, fixar o comprimento do bloco reescrito e derivar suas identidades afins. O argumento deve funcionar para todas as classes-alvo, não somente para as visitadas por um piloto. O possível fracasso de uma família de reescritas não refuta cobertura por outras famílias.

Na formulação inicial não houve cálculo. A correção posterior da convenção foi conferida na execução de reescritas referida no início. Os resultados originais de energia não foram alterados. Não se afirma que (P) seja verdadeira nem que sua prova conduziria, isoladamente, à conjectura de Collatz. Sem commit ou push.
