# Declaração — contornos deslocados e controle CUE

13/10/2026. Antes de implementar/verificar. Nenhum dado de zeros.

Alvos: identidade de resíduos de F(s)F#(s−δ) em modelos polinomiais com zeros simples na linha; sinal oposto dos dois conjuntos de polos; regularização CUE exata por CFZ Teorema4.1, p.9. Não deriva termos inferiores para L.

Verificações: polinômios artificiais com 1, 2 e 3 zeros, numeradores 1 e s+2; δ em {0,02; 0,002; 0,0002}, 50 dígitos; verificar convergência de resíduos com erro ≤20δ na grade (somente controle B). Quadratura de círculo isolando um polo, raioδ/3, uma configuração, erro relativo≤1e−35. Identidade CUE N=1 por quadratura angular com ε={0,1;0,3}, erro relativo≤1e−35. Expansão 1+ε+ε²/3−ε⁴/45 confrontada com forma fechada ε={0,01;0,02}, resto absoluto≤ε⁶. Limite total de CPU60s; sem Monte Carlo, sem dados MN/H-004.

O modelo CUE tem densidade de Vandermonde explicitamente definida. Seu resultado exato não autoriza troca de limites para L, nem prediz ausência de inferiores. Contornos fixos com ambos os polos não isolam o momento desejado.
