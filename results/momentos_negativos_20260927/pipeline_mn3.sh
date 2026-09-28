#!/bin/bash
# MN-3: pipeline sem supervisão. Cada etapa com teto próprio (ficha §6). Rodar a partir da raiz do repositório.
cd "$(dirname "$0")/../.."
D=results/momentos_negativos_20260927; PY=.venv/bin/python
( $PY $D/mn3_zeros.py --carater chi_8  --n 2000 --teto-cpu 28800 && $PY $D/mn3_derivadas.py --carater chi_8  --n 2000 --teto-cpu 3600 ) > $D/log_mn3_chi_8.txt 2>&1 &
( $PY $D/mn3_zeros.py --carater chi_12 --n 2000 --teto-cpu 28800 && $PY $D/mn3_derivadas.py --carater chi_12 --n 2000 --teto-cpu 3600 ) > $D/log_mn3_chi_12.txt 2>&1 &
( $PY $D/calc_derivadas.py --fonte zeta --n 27000 --teto-cpu 3600 && $PY $D/calc_zeta2rho.py --fonte zeta --n 27000 --teto-cpu 1800 ) > $D/log_mn3_zeta.txt 2>&1 &
wait
echo "pipeline MN-3 terminado $(date -Iseconds)" >> $D/log_mn3_fim.txt
