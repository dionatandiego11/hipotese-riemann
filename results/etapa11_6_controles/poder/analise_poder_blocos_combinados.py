"""
Reprodução versionada dos números do bloco único G (12.000 níveis) e da combinação g01+g02 (7.000 níveis) citados em
ANALISE_PODER_11_6.md §3. Eles foram obtidos, em 19/09/2026, por um comando avulso (python -c) que chamava
`analise_poder.power_block` com semente 5 e |C| do bloco g02 (D1-E) como amplitude média de L = 2. Este arquivo refaz
exatamente essa chamada (ver ANALISE_PODER_11_6_ERRATA.md).

Uso (da raiz):  .venv/bin/python3 results/etapa11_6_controles/poder/analise_poder_blocos_combinados.py
"""
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import analise_poder as ap  # noqa: E402

ROOT = HERE.parents[2]


def main():
    nbar, dbar, _ = ap.stadium()
    C1 = abs(complex(*json.loads((ROOT / "results/etapa11_6_controles/estadio/d1e_verificacoes.json").read_text())["blocks"]["g02"]["C_fit"]))
    out = {}
    for A, B, n, lab in ((85.4699, 304.0528, 12000, "G_12000"), (85.4699, 223.5316, 7000, "g01+g02_7000")):
        r = ap.power_block(A, B, n, nbar, dbar, [(2.0, C1, "bb m=1 (|C| de g02 como média)"), (4.0, C1 / math.sqrt(2), "m=2")], "goe", 5)
        out[lab] = {"fwhm": r["fwhm"], "threshold_z": r["threshold_z"], "z_L2": r["lines"][0]["z_pred"], "clear_L2": r["lines"][0]["clear"]}
        print(lab, "FWHM=%.4f limiar=%.2f z(L=2)=%.2f clara=%s" % (r["fwhm"], r["threshold_z"], r["lines"][0]["z_pred"], r["lines"][0]["clear"]))
    (HERE / "analise_poder_blocos_combinados.json").write_text(json.dumps(out, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
