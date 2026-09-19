# Benchmark limitado do `ctrl-dirichlet-v1` (Adendo 2, §5) — 19/09/2026

Script `../dirichlet/benchmark_dirichlet.py`; resultados brutos em `benchmark_chi_m4.json` e `benchmark_chi_5.json`.
Os dois caracteres rodaram **em paralelo**, como no cálculo completo. Código de busca: `dirichlet_zeros.py` com o
Adendo 2. Os dados do benchmark não são usados pelo instrumento.

## Medidas (10 avaliações depois do aquecimento; varredura real de 5 zeros a partir de t)

| t | χ₋₄: s/avaliação | χ₋₄: aval./zero | χ₋₄: s/zero | χ₅: s/avaliação | χ₅: aval./zero | χ₅: s/zero |
|---|---|---|---|---|---|---|
| 1.000 | 0,12 | 23,2 | 3,1 | 0,25 | 21,8 | 5,9 |
| 3.000 | 0,42 | 25,8 | 9,5 | 0,80 | 23,6 | 16,2 |
| 6.000 | 0,63 | 24,0 | 15,7 | 1,24 | 25,4 | 32,1 |
| T₁₂₀₀₀ (9.750 / 9.507) | 0,67 | 18,4 | 12,0 | 1,25 | 22,0 | 27,4 |

- Refinamento: no máximo 26 iterações de Illinois; **nenhum** recurso à bisseção.
- χ₅ custa cerca de 2 vezes χ₋₄, como esperado: a soma de Hurwitz tem 4 termos não nulos para χ₅ (a = 1, 2, 3, 4) e 2
  para χ₋₄ (a = 1, 3).

## Estimativa do cálculo completo

Integração do custo por zero (interpolação linear em t; abaixo de t = 1.000, a média do piloto) sobre a contagem
θ_χ(T)/π, em passos de 250 zeros. A V2 é o recálculo dos zeros 9.001–12.000 com passo pela metade, estimado em cerca de
8 avaliações extras por zero. A V3 e a V4 somam menos de 1 hora.

| | Varredura (12.000 zeros) | V2 | **Total estimado** |
|---|---|---|---|
| χ₋₄ | ~38 h | ~15 h | **~53 h (~2,2 dias)** |
| χ₅ | ~76 h | ~32 h | **~108 h (~4,5 dias)** |

A incerteza é de ±30%: a varredura de 5 zeros por altura é uma amostra pequena, e a carga da máquina varia. **Esta
estimativa substitui a de `REGISTRO_PILOTO.md` (20–35 h e 35–55 h)**, que extrapolava medidas isoladas sem a disputa
entre os dois processos.

## Comandos (executados pelo usuário, da raiz do repositório)

Os dois rodam em paralelo e continuam depois de fechar o terminal (`nohup`). O progresso é gravado a cada 25 zeros ou
120 s. Para retomar depois de qualquer interrupção (queda de energia, reinício, Ctrl+C), **basta rodar o mesmo comando**.

```bash
cd ~/Downloads/hipotese-riemann
mkdir -p results/etapa11_6_controles/dados
nohup .venv/bin/python3 results/etapa11_6_controles/dirichlet/dirichlet_zeros.py --carater chi_m4 --n 12000 \
      --saida results/etapa11_6_controles/dados >> results/etapa11_6_controles/dados/log_chi_m4.txt 2>&1 &
nohup .venv/bin/python3 results/etapa11_6_controles/dirichlet/dirichlet_zeros.py --carater chi_5 --n 12000 \
      --saida results/etapa11_6_controles/dados >> results/etapa11_6_controles/dados/log_chi_5.txt 2>&1 &
```

**Acompanhar o progresso:**

```bash
cd ~/Downloads/hipotese-riemann/results/etapa11_6_controles/dados
for c in chi_m4 chi_5; do python3 -c "
import json; s=json.load(open('progresso_${c}_12000.json'))
k=s.get('scan') or s.get('v2scan') or {}
print('$c', s['phase'], len(k.get('zeros', s.get('final',{}).get('zeros',[]))), 'zeros; t =', round(k.get('a',0),1), '; retomadas:', s['resumes'], '; gravado', s['updated'])"; done
```

- **Interromper de propósito:** `pkill -f dirichlet_zeros.py`. Isso envia SIGTERM, e o progresso é gravado antes de sair.
- **Suspensão do notebook:** o cálculo pausa e continua sozinho ao acordar. Se a máquina desligar, rode os comandos de
  novo.
- **Fim:** cada comando grava `zeros_<carater>_12000.txt` e `manifest_<carater>_12000.json`. O log termina com
  `"all_checks_passed"`. Os 500 primeiros zeros devem coincidir com os do piloto (Adendo 2, §4); essa conferência é
  feita pelo agente.
