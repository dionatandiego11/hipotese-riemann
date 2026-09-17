# Plano de comparação — implementação independente × referência

Congelado por hash (`independent/PLAN.lock.json`) **antes** de abrir arquivos de referência por bloco.

## Blocos (escolhidos antecipadamente, já analisados)

| Rótulo | Índices | Altura | Execução de referência | Motivo |
|---|---|---|---|---|
| baixo | 10.001–13.000 (`b01`) | 9.879–12.398 | `run_20260913_144429_m3_b01-…` e `run_20260913_160910_m2_m4_v1_m2` | menor altura da faixa M4 |
| intermediário | 22.001–25.000 (`b05`) | 19.617–21.943 | mesmas | log 131 inconclusivo na referência |
| alto | 67.001–70.000 (`c10`) | 52.2e3–54.5e3 | `run_20260913_173045_m3_c01-…` e `run_20260913_184711_m2_m4_v2_m2` | maior altura; log 127 inconclusivo |

Linhas acompanhadas explicitamente: fortes (log 2, log 3, log 5), fracas/limiares (log 127, log 131, log 139, 5², 2⁷), e todas as 47 do catálogo.

## Orçamentos independentes (sementes diferentes da referência)

σ: 200; limiar: 1.999; escore: 1.999; GUE secundário: 100 + 199; sintéticos: 40 + 40; controle de fase: 999;
M2: GUE 299 e Poisson 299. Sementes: 7_001 (baixo), 7_002 (intermediário), 7_003 (alto).

## Tolerâncias

### Grandezas determinísticas (mesmos dados e mesma especificação; diferença só numérica)

| Código | Grandeza | Tolerância | Justificativa |
|---|---|---|---|
| D1 | n_t; dt, FWHM, W(0) | igual; rel ≤ 1e-10 | fórmulas fechadas |
| D2 | termo suave I(t) na malha | máx abs ≤ 1e-8 | erro declarado da quadratura de referência ~1e-9 |
| D3 | F(t) na malha | máx abs ≤ 1e-7; mediana ≤ 1e-8 | NUFFT ~7e-10 × margem; |F| ≲ 600 |
| D4 | F em T_k (47 linhas, soma direta) | máx abs ≤ 1e-8 | idem |
| D5 | razão ao teórico, 3 variantes, 47 linhas | máx abs ≤ 1e-9 | erro de F propagado ~1e-11 |
| D6 | R e Q (mesmo conjunto elegível) | abs ≤ 1e-9 | função determinística de F |
| D7 | M2: Var(s), CDF, R₂ por bin, K_c | rel ≤ 1e-10 (Var, CDF, R₂); abs ≤ 1e-8 + rel 1e-8 (K_c) | aritmética direta |
| D8 | CUE: P₀, P₁, CDF predita, distâncias RMS ao limite/corrigida | P₀ ≤ 1e-7; P₁ ≤ 1e-4; CDF ≤ 1e-6; distâncias ≤ 1e-6 | quadraturas diferentes |
| D9 | catálogo | mesmas 47 entradas; períodos ≤ 1e-14 | exato |

### Grandezas com controles aleatórios independentes (comparar distribuições, não valores)

| Código | Grandeza | Critério | Justificativa |
|---|---|---|---|
| S1 | σ(t) na malha | mediana |σ_ind/σ_ref − 1| ≤ 0,03; percentil 99 ≤ 0,08 | ~2.000 amostras efetivas por ponto ⇒ EP relativo ~1,1% por execução |
| S2 | distribuição do máximo nulo | KS de duas amostras, p ≥ 0,001 | referência 9.999 × independente 1.999 |
| S3 | limiar | ICs 95% (A11) se sobrepõem | incerteza Monte Carlo |
| S4 | fração do conjunto-escore acima do limite superior | dentro da faixa binomial 99,9% em torno de 0,05 (p ~ 0,025–0,075 para B = 1.999) | calibração |
| S5 | decisões por linha do catálogo | idênticas para linhas **claramente decididas**: min(z_ref, z_ind) > 1,05·max(X_(u) ref, ind) ou max(z) < min(X_(l))/1,05. Linhas fora disso: relatar | 5% ≈ 3 EP combinados de σ |
| S6 | z nas linhas detectadas | |z_ind/z_ref − 1| ≤ 0,05 em ≥ 95% das linhas | deriva de S1 |
| S7 | escore S e detecções sem correspondência | |S_ind − S_ref| ≤ nº de linhas não claramente decididas; ambas sem correspondência = 0, ou explicado | S5 |
| S8 | p(S) | p_ind ≤ 0,01 quando p_ref está no piso | resoluções distintas |
| S9 | tolerância sintética; separação de resolução | razão ∈ [0,5; 2]; separação igual ou adjacente na lista | amostra pequena (quantil 0,99) |
| S10 | vereditos C1/C2 por bloco | iguais, salvo decisão por linha não claramente decidida (relatar) | S5 |
| S11 | p(Q) | ambos ≤ 0,01 | pisos |
| S12 | p dos envelopes M2 | se p_ref no piso (0,001): p_ind ≤ 2/300; senão |p_ind − p_ref| ≤ 3·√(p_ref(1−p_ref)/300) + 0,01 | EP binomial |
| S13 | escala de ruído amostral CUE | razão ∈ [0,75; 1,33] | ensemble aleatório |

## Tratamento de discrepâncias

Toda violação é investigada até uma das causas: (i) erro na implementação independente; (ii) erro na referência;
(iii) ambiguidade da especificação; (iv) variação Monte Carlo compatível com a incerteza; (v) causa não identificada.
Correções na implementação independente após a comparação são registradas com a versão anterior preservada; a referência
não é alterada. **Nenhum dado com índice > 70.000 é lido.**
