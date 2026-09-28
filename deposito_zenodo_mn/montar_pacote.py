"""Monta o pacote do depósito Zenodo da nota (MN-1 a MN-3) em dist/mn_negative_moments_v1/. Não publica nada."""
import hashlib, json, shutil, sys
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "results/momentos_negativos_20260927"
OUT = ROOT / "dist/mn_negative_moments_v1"
if OUT.exists():
    shutil.rmtree(OUT)
for d in ("data", "code", "preregistration", "reports", "verification", "note"):
    (OUT / d).mkdir(parents=True)
cp = lambda src, dst: shutil.copy2(src, OUT / dst)

# --- dados de L(s,chi): só os zeros usados na nota (os blocos reservados da H-004 ficam de fora) ---
zsrc = {"chi_m4": (ROOT / "results/etapa11_6_controles/dirichlet/completude/zeros_chi_m4_12000_completo.txt", 3000),
        "chi_5": (ROOT / "results/etapa11_6_controles/dirichlet/completude/zeros_chi_5_12000_completo.txt", 3000),
        "chi_8": (R / "mn3_zeros_d3/zeros_chi_8_2000.txt", 2000),
        "chi_12": (R / "mn3_zeros/zeros_chi_12_2000.txt", 2000)}
for name, (src, n) in zsrc.items():
    z = np.loadtxt(src)[:n]
    d = np.loadtxt(R / f"derivadas_{name}_{n}.txt")
    assert np.allclose(z, d[:, 0], atol=0, rtol=0), name      # derivadas calculadas exatamente nesses zeros
    np.savetxt(OUT / f"data/zeros_{name}.txt", z, fmt="%.9f", header=f"ordinates of zeros 1-{n} of L(s,{name}), verified complete")
    cp(R / f"derivadas_{name}_{n}.txt", f"data/derivatives_{name}.txt")
    cp(R / f"L2rho_{name}_{n}.txt", f"data/L2rho_{name}.txt")

# --- zeta: só índice e valores calculados (ordenadas de Odlyzko não redistribuídas) ---
d27 = np.loadtxt(R / "derivadas_zeta_27000.txt"); l27 = np.loadtxt(R / "L2rho_zeta_27000.txt")
d20 = np.loadtxt(R / "derivadas_zeta_20000.txt"); l20 = np.loadtxt(R / "L2rho_zeta_20000.txt")
assert np.array_equal(d27[:20000], d20) and np.array_equal(l27[:20000], l20), "zeta 1-20000 difere entre MN-1/2 e MN-3"
np.savetxt(OUT / "data/zeta_values_1-27000.txt", np.column_stack([np.arange(1, 27001), d27[:, 1], l27[:, 1]]),
           fmt=["%d", "%.12e", "%.12e"], header="n |zeta'(rho_n)| |zeta(2 rho_n)|  (ordinates: Odlyzko zeros1, not included)")

# --- código ---
for f in ("src/riemann_spectra/discrete_moments.py", "tests/test_discrete_moments.py",
          "results/etapa11_6_controles/dirichlet/dirichlet_zeros.py",
          "results/etapa11_6_controles/dirichlet/completude/completude_d3.py"):
    cp(ROOT / f, "code/" + Path(f).name)
for f in ("calc_derivadas.py", "calc_zeta2rho.py", "analise.py", "analise_c8.py", "analise_mn3.py", "mn3_caracteres.py",
          "mn3_zeros.py", "mn3_derivadas.py", "mn3_derivadas_d3.py", "mn3_completude_chi8.py"):
    cp(R / f, "code/" + f)
cp(ROOT / "deposito_zenodo_mn/reproduce_table.py", "reproduce_table.py")

# --- pré-registro, relatórios, verificação dos zeros, nota ---
for f in ("FICHA_MOMENTOS_NEGATIVOS.md", "FICHA_MOMENTOS_NEGATIVOS.sha256", "FICHA_MOMENTOS_NEGATIVOS_C8.md",
          "FICHA_MOMENTOS_NEGATIVOS_C8.sha256", "FICHA_MOMENTOS_NEGATIVOS_MN3.md", "FICHA_MOMENTOS_NEGATIVOS_MN3.sha256",
          "DERIVACAO_ETAPA_A.md"):
    cp(ROOT / "hipoteses" / f, "preregistration/" + f)
for f in ("ADENDO_MN3_1.md", "ADENDO_MN3_2.md"):
    cp(R / f, "preregistration/" + f)
for f in ("RESULTADO.md", "RESULTADO_C8.md", "RESULTADO_MN3.md", "BUSCA_NOVIDADE.md", "analise.json", "analise_c8.json", "analise_mn3.json"):
    cp(R / f, "reports/" + f)
C = ROOT / "results/etapa11_6_controles/dirichlet/completude"
for src, dst in ((C / "manifesto_d3_chi_m4.json", "manifest_chi_m4.json"), (C / "manifesto_d3_chi_5.json", "manifest_chi_5.json"),
                 (R / "mn3_zeros/manifest_chi_8_2000.json", "manifest_chi_8_original_failedV2.json"),
                 (R / "mn3_zeros_d3/manifest_chi_8_2000.json", "manifest_chi_8_corrected.json"),
                 (R / "mn3_zeros/manifest_chi_12_2000.json", "manifest_chi_12.json")):
    cp(src, "verification/" + dst)
cp(ROOT / "nota_momentos_negativos/nota.pdf", "note/note_v1.pdf"); cp(ROOT / "nota_momentos_negativos/nota.tex", "note/note_v1.tex")
for f in ("README.md", ".zenodo.json", "LICENSE"):
    cp(ROOT / "deposito_zenodo_mn" / f, f)

# --- somas SHA-256 ---
lines = []
for p in sorted(OUT.rglob("*")):
    if p.is_file() and p.name != "SHA256SUMS":
        lines.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(OUT)}")
(OUT / "SHA256SUMS").write_text("\n".join(lines) + "\n")
print(f"pacote em {OUT}: {len(lines)} arquivos")
