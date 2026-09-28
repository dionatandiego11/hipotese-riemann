# Numerical evidence for conjectures on negative discrete second moments of Dirichlet L-functions — data and code

Dionatan Resende (Independent researcher), dionatandieresende@gmail.com — version 1, September 2026.

DOI: [10.5281/zenodo.23020957](https://doi.org/10.5281/zenodo.23020957)

This package contains the data, code and pre-registration documents behind the note *"Numerical evidence for conjectures
on negative discrete second moments of Dirichlet L-functions"* (`note/note_v1.pdf`). The note tests Conjectures 7 and 8
of A. Pearce-Crump (arXiv:2606.25094):

- Σ_{0<γ≤T} 1/|L′(ρ,χ)|² ∼ (A_q/2π) T, with A_q = (6/π²) ∏_{p|q} p/(p+1);
- Σ_{0<γ≤T} |L(2ρ,χ²)/L′(ρ,χ)|² ∼ (φ(q)/q) T/2π;

for the real primitive characters of conductor 4, 5, 8 and 12. The tests compare each L-function with ζ(s) at the same
local density of zeros.

## Reproducing Table 1

```
python3 reproduce_table.py --zeros1 /path/to/zeros1
```

Needs Python 3 and numpy. The ordinates of the zeros of ζ(s) are **not** redistributed here: download Odlyzko's table
`zeros1` from https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros1. The script checks its SHA-256
(`3436c916…`). With the pre-registered seeds, the script reproduces the published values and intervals exactly.

## Contents

| folder | content |
|---|---|
| `data/` | `zeros_<chi>.txt`: ordinates of the zeros used (1–3000 for χ₋₄, χ₅; 1–2000 for χ₈, χ₁₂), computed by sign changes of Z_χ and verified complete. `derivatives_<chi>.txt`: γ and \|L′(ρ,χ)\|. `L2rho_<chi>.txt`: γ and \|L(2ρ,χ²)\|. `zeta_values_1-27000.txt`: n, \|ζ′(ρ_n)\|, \|ζ(2ρ_n)\| for the first 27000 zeros of ζ |
| `verification/` | completeness manifests of the zero lists (checks V1–V4, completeness pass). For χ₈ both the original list (which **failed** the half-step rescan V2: 2000 against 2002) and the corrected list are included |
| `preregistration/` | the three pre-registration sheets (written and hashed **before** the corresponding computations), their SHA-256 files and addenda; the heuristic derivation of the arithmetic factors (`DERIVACAO_ETAPA_A.md`) |
| `reports/` | result reports and analysis outputs (JSON); the documented literature search |
| `code/` | the scripts actually used (zero finding, completeness pass, derivatives, analyses) and the module `discrete_moments.py` with its tests |
| `note/` | the note (PDF and LaTeX source) |

The pre-registration sheets and reports are in **Portuguese**; the note, this README and `reproduce_table.py` are in
English. The scripts in `code/` were written for the layout of the project repository and are included as a record;
`reproduce_table.py` is the self-contained entry point (the tests in `code/` import the module as part of the
project package and are included as a record).

## Methods in brief

- **Zeros of L(s,χ):** sign changes of Z_χ(t) = e^{iθ_χ(t)}L(½+it,χ); L by Hurwitz sums in mpmath (30 digits); scan
  step ≤ 1/8 of the mean spacing; refinement to 10⁻¹⁰.
- **Checks:** count against θ_χ/π (V1); independent rescan at half the step (V2); second evaluation (V3); reality of
  Z_χ (V4).
- **Missed close pairs** were recovered by rescanning large gaps at 1/32 of the mean spacing.
- **Derivatives:** |L′(ρ,χ)| = |Z_χ′(γ)| by central differences (step 10⁻⁶, 20 digits); |ζ′(ρ)| by `mpmath.siegelz`.
- **Statistic:** v = log(qγ/2π)/|L′|² (and the analogue w for the second moment), averaged and compared with ζ in ten
  density bins. 95% intervals from a block bootstrap (blocks of 100 zeros, 2000 replicates).

## Limitations

Low heights (γ < 3000); four real characters; a shared ζ reference; heavy-tailed summands (the bootstrap may
under-cover); the comparison with ζ assumes common finite-height corrections. This is numerical evidence, not a proof;
it says nothing about the Generalised Riemann Hypothesis.

## Use of AI

The computations, analysis and drafting were carried out with substantial assistance from an AI system (Claude,
Anthropic). The author checked the results and takes full responsibility for the content.

## Licence

Code: MIT. Data, documents and the note: CC BY 4.0. See `LICENSE`.
