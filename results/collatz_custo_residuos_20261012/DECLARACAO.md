# Declaração anterior à implementação e ao cálculo — 12/10/2026

Alvo: verificar identidades dos geradores g_ℓ(k,a) de Wirsching e uma cota
analítica de cauda do custo condicionado. Não testar RH, convergência de
órbitas, conjectura de densidade positiva nem escolher parâmetros pela saída.

1. ℓ=1..6, k=0..2ℓ: comparar construção por levantamento modular com
   enumeração independente de tuplas de custos e congruência da composição
   afim. Conferir a soma em resíduos contra coeficientes do produto
   Q_ℓ(z)=∏_{i=1}^ℓ(1+...+z^{2·3^{i−1}−1}).
2. ℓ∈{16,24,32,64}, k∈{ℓ,ℓ+floor(sqrt(ℓ)),2ℓ}, J∈{1,2,4,8,16}:
   verificar com inteiros/frações a cauda de w_{ℓ,k}(j)=q_{ℓ−1}(k−j)/q_ℓ(k)
   e sua majorante min(1,5(4/5)^J). Não construir resíduos módulo 3^ℓ
   nesses níveis; apenas coeficientes até 2ℓ.
3. Conferir normalização e projeções das pequenas distribuições.

Teto: RLIMIT_CPU=60 segundos; sem processos filhos, aleatoriedade ou dados
de zeros. Memória: relatar pico; matrizes densas proibidas. Se o teto vencer,
registrar execução parcial/inconclusiva, sem ampliar. Não produzir mínimos
experimentais para inferir uma cota uniforme em resíduos. Critério técnico:
todas as identidades e desigualdades declaradas devem valer exatamente.
Código independente em collatz/, sem importar riemann_spectra. Sem commit.
