#!/bin/bash
# MN-3, ADENDO_MN3_2: correção de χ₈ + conclusão de ζ, em paralelo. Rodar a partir de qualquer pasta.
cd "$(dirname "$0")/../.."
D=results/momentos_negativos_20260927; PY=.venv/bin/python
sha256sum $D/ADENDO_MN3_2.md $D/mn3_completude_chi8.py $D/mn3_derivadas_d3.py $D/pipeline_mn3_adendo2.sh >> hipoteses/FICHA_MOMENTOS_NEGATIVOS_MN3.sha256
( $PY $D/mn3_completude_chi8.py && $PY $D/mn3_derivadas_d3.py --carater chi_8 --n 2000 --teto-cpu 3600 ) > $D/log_mn3a2_chi_8.txt 2>&1 &
( $PY $D/calc_derivadas.py --fonte zeta --n 27000 --teto-cpu 1800 && $PY $D/calc_zeta2rho.py --fonte zeta --n 27000 --teto-cpu 3600 ) > $D/log_mn3a2_zeta.txt 2>&1 &
wait
echo "adendo 2 MN-3 terminado $(date -Iseconds)" >> $D/log_mn3_fim.txt
