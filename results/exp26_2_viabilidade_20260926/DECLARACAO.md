# Conta sintética EXP26-2 — declaração anterior à implementação

26/09/2026. Sem acesso a zeros reais, resultados Dirichlet ou processos ativos. Estudo exploratório de viabilidade em GUE finito; não estima um teto bayesiano do B0 completo nem exclui ganhos de resíduos aritméticos conhecidos. Congelar SHA-256 deste texto antes de escrever o módulo de cálculo. Código e dependências terão lock adicional antes da execução.

## Desenho fixado

- 120 espectros pais independentes: 3.000 níveis centrais de matrizes GUE tridiagonais de dimensão 5.000, gerador existente `generate_gue_central_levels`, fração 0,6, unfolding pelo semicírculo. Não renormalizar espaçamentos pela amostra.
- Pais 0–39 desenvolvimento; 40–79 calibração; 80–119 avaliação. Separação antes de qualquer simulação. Semente de pai = 2026092600+i. Máscaras: SeedSequence([20260926,i,k,mecanismo,repeticao]); mecanismos MA=0, MP=1. Bootstrap: 26092699. Nenhum uso de hash() como semente.
- Remoções k={2,6,12,30}; oito máscaras por pai, severidade e mecanismo. MA: permutar candidatos a pares interiores adjacentes e selecionar gulosa e uniformemente na ordem, sem sobreposição de níveis. MP: mesma regra, restrita aos pares cujo espaçamento é ≤ percentil 10% dos pares elegíveis do pai completo. Isso define um modelo específico de seleção, não o algoritmo exato do D3.
- Preservar primeiro/último nível. MA=MJ para k=2 e mesma distribuição de início: não criar classe MJ separada. Esta conta compara apenas MP com MA. MR/M0/MJ denso são adiados ao piloto, se justificado.

## Observáveis

Hann com bordas e centro do pai fixos; 128 frequências igualmente espaçadas em τ∈[0,05;2]. μ pela integral analítica da Hann; Q=3L/8. A=Z−μ; K=|A|²/Q. Aplicar remoção pela soma D dos termos removidos. Verificar em primeiro pai, primeira máscara de cada mecanismo/severidade contra recomputação direta (erro absoluto ≤1e−9 em K); verificar a decomposição interferência+quadrático com mesma tolerância. Não alterar sub-blocos por índice: um bloco por pai.

Registrar, por pai/célula, média e média quadrática em frequências de ΔK, interferência e |D|²/Q; conservar vetores médios por pai para comparar variação entre espectros e correlação entre bins. A diferença completo−degradado é diagnóstico pareado, proibida como entrada dos classificadores.

B0: features dos espaçamentos observados em coordenada fixa: média, variância, máximo, quantis 0,1/0,5/0,9/0,99 e frações abaixo de 0,3/acima de 2/acima de 3/acima de 4 (11 features). Contagem observada é igual por severidade nos dois mecanismos, sem poder discriminante nesta conta.

B1: B0 + 8 médias de K em grupos contíguos de 16 bins + 8 médias da parte real e 8 da imaginária de A/√Q nos mesmos grupos (35 features). Sem catálogo ou linha aritmética.

Um classificador por severidade e conjunto de features: regressão logística, padronização só no desenvolvimento, penalização L2=0,01 na perda média (intercepto não penalizado); L-BFGS até 500 iterações, gradiente explícito, sem busca de hiperparâmetros. Falha de convergência: registrar e não decidir essa célula. Limiar = quantil empírico 95% dos escores MA de calibração, método higher, classificar MP só acima do limiar. Mesmo limiar aplicado à avaliação; não ajustar para obter FPR nominal.

## Experimento local de lacuna (k=2)

Guardar G=x[j+2]−x[j−1] na posição do par removido, revelada por oráculo. Estimar razão de verossimilhanças por histogramas fixos (passo 0,2 entre 0 e 8, mais cauda até infinito), pseudocontagem 0,5 por bin; treinamento/calibração/avaliação separados por pai. Reportar acurácia com priori 1/2, e sensibilidade/FPR no limiar calibrado. Não chamar o resultado de ótimo ou cota superior; trata-se de um discriminador escalar especificado. Não supor independência dos três espaçamentos.

## Incerteza e regra de leitura

Bootstrap pareado de 2.000 reamostragens de pais de avaliação; todas as máscaras ficam juntas. Intervalos percentis 95% pontuais condicionais ao classificador e limiar ajustados; não incluem incerteza de refazer o treinamento, não são certificados nem simultâneos. Sem valores-p ou afirmação confirmatória. Reportar TPR, FPR e ganho Δ=TPR(B1)−TPR(B0).

Ganho mínimo operacional fixado: 0,05 absoluto (5 pontos percentuais). Para cada severidade: parar o investimento neste B1/GUE se o extremo superior de Δ<0,05; seguir para piloto somente se extremo inferior de Δ>0,05 e extremo superior de FPR(B1)≤0,05; caso contrário inconclusivo. Prioridade esparsa: k=2 e 6; k=12/30 secundários. A regra é triagem exploratória do método específico, não teorema de impossibilidade e não decisão sobre dados de funções L.

Teto: 600 s-CPU acumulados, um processo, uma thread de BLAS, RLIMIT_CPU; parada cooperativa antes de 570 s com checkpoint por pai. CPU inclui verificações e análise; sem extensão após resultado. Se número de pais não completar, relatório parcial/inconclusivo, sem aplicar a decisão final. Não reutilizar saídas parciais como amostra de tamanho escolhido depois.

## Artefatos e verificações

Módulo novo em src/riemann_spectra/loss_viability.py (sem modificar módulos congelados), executor e resultados nesta pasta. Gravar arrays de resumos/features e lacunas, máscaras/sementes, hashes do conteúdo sintético por pai, lock de código/dependências, versões, CPU/parede, threads e manifesto. Não guardar tabelas sintéticas como dados reais. Controles: níveis ordenados, tamanho e bordas; máscara válida/disjunta; identidade da remoção; integridade dos hashes; nenhum espectro pai atravessa divisões. Relatório em português ao concluir ou parar.
