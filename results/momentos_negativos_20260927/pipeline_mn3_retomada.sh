#!/bin/bash
# MN-3, retomada (ADENDO_MN3_1). Retoma dos checkpoints.
cd "$(dirname "$0")/../.."
D=results/momentos_negativos_20260927; PY=.venv/bin/python
( $PY $D/mn3_zeros.py --carater chi_8  --n 2000 --teto-cpu 10800 && $PY $D/mn3_derivadas.py --carater chi_8  --n 2000 --teto-cpu 3600 ) > $D/log_mn3r_chi_8.txt 2>&1 &
( $PY $D/mn3_zeros.py --carater chi_12 --n 2000 --teto-cpu 10800 && $PY $D/mn3_derivadas.py --carater chi_12 --n 2000 --teto-cpu 3600 ) > $D/log_mn3r_chi_12.txt 2>&1 &
( $PY $D/calc_derivadas.py --fonte zeta --n 27000 --teto-cpu 3600 && $PY $D/calc_zeta2rho.py --fonte zeta --n 27000 --teto-cpu 3600 ) > $D/log_mn3r_zeta.txt 2>&1 &
wait
echo "retomada MN-3 terminada $(date -Iseconds)" >> $D/log_mn3_fim.txt
