"""Caracteres da MN-3: reais primitivos (Kronecker (8/·) e (12/·)), pares. Usados sem editar dirichlet_zeros.py."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "results/etapa11_6_controles/dirichlet"))
import dirichlet_zeros as dz
CHARS = {"chi_8": dz.Character("chi_8", q=8, kappa=0, residues={1: 1, 7: 1, 3: -1, 5: -1}),
         "chi_12": dz.Character("chi_12", q=12, kappa=0, residues={1: 1, 11: 1, 5: -1, 7: -1})}
