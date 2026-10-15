# Correção do teste de monotonicidade

13/10/2026, após primeira execução e antes da alteração. A declaração pede erro≤20δ, não monotonicidade estrita. O teste acrescentou monotonicidade estrita e falhou no polinômio linear com numerador1, cujos resíduos escalados são exatamente ±1 para todoδ. As discrepâncias de ~10^−49 são arredondamento a50 dígitos. A condição adicional passa a aceitar o piso1e−40, sem alterar a regra declarada, fórmulas ou grade. Execução1 e teste original preservados. Não se transforma a falha original em aprovação retrospectiva.
