# Declaração — razões discretas com derivada logarítmica

13/10/2026, antes de implementar/verificar. Sem zeros reais ou dados MN.

Verificar a aritmética diagonal do gerador F'/F vezes |H/F|² deslocado: P7(ν,ε)=Σp∤q logp p^(−1−ν−ε)/(1+p^(−1−2ε)); P8(ν,ε)=Σp∤q logp/(p^(1+ν+ε)+1). Estes são fatores formais da receita, não médias demonstradas. q={1,4,5,12}, ν=0, ε={0,001;0,0001;0,00001}; 50 dígitos. P7 por diferença convergente do log-derivado deζ, crivo até20.000, cauda analítica≤4(log20.000+1)/20.000; não certifica aritmética mpmath. P8 porζ e fatores locais. Verificar εPj→1 e ε²Dj(2ε)Pj→κj/2 com erro relativo≤0,01 nesta grade. Verificar parte constante comum Pj−1/ε contra−B7/κ7, tolerância0,02 na grade. Conferir álgebra localP7 por derivar produto de um primo em u=v, p={2,5,11}, shiftspositivos distintos.

Controle CUE discreto: determinantetoeplitz do peso |1−e^{iθ}|²/|1−r e^{iθ}|² para M={0,1,2,5,10}, r={0,25;0,9;0,99}; tolerância relativa1e−35 contra1+M(1−r)/(1+r). M=1 Fourierpor quadratura para r=0,25; tolerância1e−35. Nenhuma matriz Haar aleatória será gerada. Mostrar ε=c/N, c={0,5;1}, N={10,100,1000}, pela fórmula fechada, sem inferir uniformidade paraL.

Teto60sCPU. Preservar todos os resultados negativos. Não extrair nem ajustar termos inferiores emT aos dados; leitura bibliográfica dirigida com páginas e hashes.
