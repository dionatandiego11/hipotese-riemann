# Razões e momentos negativos: regularização, diagonais e uniformidade

13/10/2026. Nova prioridade a partir da orientação de Andrew comunicada
pelo usuário. Esta entrega corrige a base analítica antes de buscar termos
inferiores. Nenhum zero ou dado reservado foi consultado.

## 1. Pergunta e fontes efetivamente conferidas

Pearce-Crump, arXiv:2606.25094v1, Conjecturas 7/8, p.4; continuidade p.5,
identidades de Möbius/Liouville p.2. Cópia arquivada relida e p.4 renderizada.
Conrey–Snaith, cópia arquivada, Conjectura2.1, eqs.(2.10)–(2.11) e Remark2.2,
p.6 conferida visualmente. São conjecturas, não teoremas de momentos.

Para χ primitivo, sob GRH e zeros simples, as previsões são

    J_χ(T)=Σ_{0<γ≤T}|L'(ρ,χ)|^(−2) ~ A_q T/(2π),
    K_χ(T)=Σ_{0<γ≤T}|L(2ρ,χ²)/L'(ρ,χ)|² ~ R_q T/(2π),
    A_q=ζ(2)^(−1)∏_{p|q}p/(p+1),   R_q=φ(q)/q.

O autor espera uniformidade no condutor em sua faixa; esta entrega NÃO
estabelece essa uniformidade. A regularização exata abaixo vale em intervalo
fixo e para uma função fixa. Álgebra das diagonais é distinta de uma
previsão completa de razões ou de uma prova de J/K.

Classificações: A para identidades locais/algebraicas sob hipóteses;
B para verificações numéricas; D para extrapolações por conjectura das
razões ainda não fechadas. Novidade não estabelecida.

## 2. A falha da Etapa B anterior

A nota de28/09 passava de médias deslocadas ao momento discreto levando
α→0, mas mantinha um erro O(T^(1/2+η)) sem justificar sua dependência em α.
Também enviava shifts de numerador ao infinito dentro da fórmula CS(2.10).

Duas precisões da fonte são essenciais:

- Em CS(2.11), shifts do denominador obedecem Re δ ≳1/logT; os do numerador
  têm partes reais limitadas. O limite α→0 em T fixo sai desse domínio.
- Remark2.2 permite relaxamento com deslocamentos de numerador correspondentes,
  tendendo a zero na mesma taxa. Um numerador constante1 não fornece essa
  compensação. Enviar o numerador ao infinito também sai da faixa citada.

A receita geral de CFZ(5.12)–(5.15), lida nesta sessão, permite formular a
especialização de conjuntos vazios como cálculo formal de diagonais. Essa
é uma apresentação apropriada, em vez do limite de shifts do numerador;
ainda não fornece a uniformidade no limite singular. O tratamento do caso
sem numeradores deve ser explicitado, pois o enunciado impresso inclui
uma condição de shifts de numerador com K+L no denominador, vacuamente
interpretada se os conjuntos são vazios. Não tratar essa convenção como
uma extensão uniforme já provada.

Para C8, há ainda uma dependência em L(2s,χ²), portanto altura2t. A fórmula
padrão de razões com todos os fatores à mesma altura t não se aplica
literalmente: a receita ou a média local precisa tratar essa correlação.

**Retiradas:** erro quadrático-raiz e ausência de T/logT, T/log²T etc não
foram estabelecidos pela Etapa B. Os fatores aritméticos continuam corretos
como resíduos de diagonais. As tabelas MN e as fichas não foram alteradas.

## 3. Identidade local exata que recupera o momento

Se 0<a<b não são ordenadas de zeros, a função F(s)=L(s,χ) não tem polos
perto do segmento e todos os zeros do segmento são simples e estão na
linha crítica, então, para H holomorfa nessa vizinhança,

    Σ_{a<γ<b}|H(ρ)/F'(ρ)|²
      =lim_{ε↓0} (ε/π)∫_a^b |H(1/2+ε+it)/F(1/2+ε+it)|²dt.

Não é necessário assumir uma posição para zeros fora do segmento.
GRH é suficiente para a condição de posição; simplicidade é adicional.
Para J use H=1. Para K use H(s)=L(2s,χ²), holomorfa nessa vizinhança
quando a>0, mesmo se χ² é principal. GRH para χ² não é necessária à
identidade local.

**Prova.** Isole vizinhanças disjuntas dos finitíssimos zeros. Perto de ρ,
F(s)=(s−ρ)g_ρ(s), g_ρ(ρ)=F'(ρ)≠0. O integrando escalado é uma função
contínua multiplicada pelo núcleo ε/(ε²+(t−γ)²), cuja massa tende aπ.
Fora das vizinhanças, F é limitada longe de zero e a integral escalada
tende a0. A aproximação local também dá erro O_{F,H,a,b}(εlog(1/ε));
a constante depende das vizinhanças e separações. Não é cota uniforme
em altura, condutor ou separação mínima de zeros.

Se um extremo é um zero simples, o núcleo fornece metade de sua massa.
Não usar esse limite como se contasse integralmente um zero no extremo.
A escolha da altura de comparação com tabelas precisa respeitar isso.

## 4. Polo auxiliar na origem do momento ponderado

Se χ² é principal modq e F(1/2)≠0, H(s)=L(2s,χ²) tem perto de s=1/2

    H(s)=R_q/[2(s−1/2)]+O(1).

Assim, para b>0 que não é ordenada de zero,

    lim_{ε↓0}(ε/π)∫_0^b |H/F|²dt
       =K_χ(b)+R_q²/[8|L(1/2,χ)|²],

supondo zeros simples na linha no segmento e nenhum zero central.
A contribuição na origem vem da semimassa do núcleo e do fator1/2 no
resíduo de L(2s). Deve ser subtraída, ou evitada usando a>0 e registrando
separadamente o intervalo inicial. Se χ² não é principal, não há esse
polo; se F(1/2)=0, a situação exige outro tratamento e a fórmula acima
não foi declarada válida.

É uma correção exata da regularização, NÃO um termo inferior completo
conjecturado para K(T). Outros termos da média podem produzir ou cancelar
constantes na passagem para o momento discreto. Essa separação deve ser
mantida no cálculo seguinte.

## 5. Diagonais e primeiras partes de Laurent

Das séries absolutamente convergentes à direita de1, as diagonais formais
meromorficamente continuadas, com α=2ε, são

    D7(α;q)=Σ μ(n)²|χ(n)|² n^(−1−α)
           =L(1+α,χ0)/L(2+2α,χ0),
    D8(α;q)=Σ λ(n)²|χ(n)|² n^(−1−α)=L(1+α,χ0).

χ0 é principal modq; usa-se a representação imprimitive com os fatores
p|q retirados. Não se identifica χ² com χ0 a menos que seja realmente
principal; a identidade de Liouville continua válida para qualquer χ.

Escreva D_j=κ_j/α+B_j+O(α). O cálculo dá

    κ7=A_q,
    B7=A_q[γ_E−2ζ'(2)/ζ(2)+Σ_{p|q}log p/(p+1)],
    κ8=R_q,
    B8=R_q[γ_E+Σ_{p|q}log p/(p−1)].

Derivação: ζ(1+α)=1/α+γ_E+O(α). A derivada logarítmica do fator local
(1−p^(−1−α))/(1−p^(−2−2α)) em0 é logp/(p+1); a do fator simples do
numerador é logp/(p−1). No primeiro caso há a derivada −2ζ'(2)/ζ(2).

Os κ_j/(2π) são os coeficientes principais previstos em C7/C8. Isso
recupera a parte aritmética da diagonal, não a derivação completa por
razões. As primeiras partes finitas estão explicitadas e verificadas,
mas NÃO são coeficientes inferiores das somas discretas.

Se alguém escolhe ε=c/logT e aplica só a diagonal, o termo B_j produz
cB_j T/(πlogT). Ele depende do parâmetro arbitrário c da regularização.
Para chamá-lo de termo do momento discreto seria preciso remover o viés
ou demonstrar a passagem conjunta de limites; nada disso foi feito aqui.

## 6. Por que o resto tem uma singularidade relevante

Para intervalo fixo a,b como no§3 e H correspondente ao momento j, ponha

    I_j(ε)=∫_a^b |H/F|²dt,
    E_j(ε)=I_j(ε)−(b−a)D_j(2ε;q).

As identidades anteriores implicam exatamente

    lim_{ε↓0} ε E_j(ε)
      =π S_j(a,b)−(b−a)κ_j/2.

Em geral o resto da aproximação diagonal tem, portanto, parte de ordem
1/ε. Em um intervalo sem zeros, S_j=0 e esse coeficiente é não nulo.
Uma estimativa uniformemente O(T^(1/2+η)) no deslocamento não pode ser
transportada assim até0: se fosse, eliminaria essa contribuição.

A demonstração não refuta que um momento discreto possa ter certo erro
em T; refuta a transferência usada para justificá-lo. Se a constante do
O antigo depende singularmente de ε, a conclusão em T não segue. O
contraexemplo em intervalo local também não contradiz o domínio de CS.

**Alvo analítico concreto seguinte:** calcular o coeficiente singular do
resto, incluindo termos não diagonais, duais, horizontais e bordas, ou
obter um regime conjunto onde a passagem para o momento seja controlada.
Não descartar esses termos antes de extrair seu comportamento no shift.

## 7. Modelo exato de dois zeros: sensibilidade ao par próximo

Use zeros artificiais ρ1=1/2, ρ2=1/2+id, d>0, e
F(s)=(s−ρ1)(s−ρ2). Integrando sobre toda a reta,

    (ε/π)∫_R |F(1/2+ε+it)|^(−2)dt=2/(d²+4ε²),
    Σ_{j=1,2}|F'(ρ_j)|^(−2)=2/d².

A razão é d²/(d²+4ε²). Para erro relativo ≤τ, 0<τ<1, exige-se

    ε≤(d/2)sqrt(τ/(1−τ)).

Logo uma regularização fixada sem levar a separação em conta pode perder
massa importante nos pares próximos. O modelo demonstra um mecanismo,
não a distribuição real de pares de zeros nem um teorema sobre seu mínimo.

Para H(s)=s−(ρ1+ρ2)/2, holomorfa, o modelo ponderado dá

    (ε/π)∫_R |H/F|²dt=(d²+8ε²)/[2(d²+4ε²)],
    Σ|H(ρ_j)/F'(ρ_j)|²=1/2.

Aqui H não é L(2s,χ²); é um controle da identidade geral de regularização.
O modelo de borda adicional usa denominador constante, sem zeros, e
numerador R/[2(s−1/2)], cuja integral escalada na semirreta é R²/(8|g|²).

## 8. O que foi executado e limites

Declaração anterior: `results/razoes_momentos_negativos_20261013/DECLARACAO.md`,
SHA-256 0ff243327a7dc5903baa49c2399265696493ef85c0d634fe6f7e4c00c853c297.
Adendo de borda anterior às verificações adicionais, com hash próprio.

- q=1,4,5,8,12: resíduos e partes finitas conferidos por extrapolação em
  α=10^(−4),10^(−6),10^(−8), a70 dígitos. Erro final das partes finitas
  ≤3,2·10^(−17) na grade; estabilidade numérica B, não cota certificada.
- 6 controles de dois zeros, com12 quadraturas, bateram com as formas
  fechadas dentro da tolerância relativa1e−40; não certificadas por intervalos.
- 2 controles do polo de borda passaram dentro de1e−30 nos testes rápidos.
- 9 testes pertinentes passaram em1,57s (5 novos e4 já existentes);
  teste anterior à inclusão do controle de borda:8 passaram em1,68s.
- Piloto principal:4,047s CPU,4,093s parede, RSS244.616KiB reportado;
  RLIMIT_CPU60s. O custo dos testes não foi medido em CPU separadamente.
- Rascunho local v3 corrigido e compilado com recursos TeX já em cache.
  PDF novo na pasta própria; PDFs/pacotes anteriores preservados.

Nenhum zero real, dado reservado ou tabela MN foi aberto/recalculado.
Sem publicação, mensagem externa ou commit. Não foi produzida uma fórmula
completa de termos inferiores. O plano registra exatamente a dependência
que precisa ser resolvida para isso.
