import numpy as np
from mpmath import mp
from collatz.height_transfer import rational_states_by_height, height_weight
from collatz.periodic_denominator import step
from riemann_spectra.prime_trace_kernel import prime_kernel


def test_collatz_cyclic_subspaces_and_eigenvalues():
    """Verify that transfer matrix eigenvalues match periodic cycle height products."""
    states = rational_states_by_height(10)
    idx = {s: i for i, s in enumerate(states)}
    N = len(states)

    for alpha in (0.5, 1.0, 2.0):
        M = np.zeros((N, N))
        for j, x in enumerate(states):
            y = step(x)
            if y in idx:
                M[idx[y], j] = float(height_weight(x, alpha))

        eigvals = np.linalg.eigvals(M)
        abs_eigs = np.sort(np.abs(eigvals))[::-1]

        # Top 2 eigenvalues must be 1.0 (from fixed points 0 and -1)
        assert abs(abs_eigs[0] - 1.0) < 1e-12
        assert abs(abs_eigs[1] - 1.0) < 1e-12

        # Next eigenvalues must be from 2-cycle {1, 2} with radius 2^(-alpha/2)
        expected_pos_radius = 2.0 ** (-alpha / 2.0)
        assert abs(abs_eigs[2] - expected_pos_radius) < 1e-12
        assert abs(abs_eigs[3] - expected_pos_radius) < 1e-12

        # Cycle {1/5, 4/5, 2/5} with radius 5^(-alpha)
        expected_5_radius = 5.0 ** (-alpha)
        found_5 = any(abs(abs(ev) - expected_5_radius) < 1e-10 for ev in eigvals)
        assert found_5

        # Spectral gap g = 1 - 2^(-alpha/2)
        spectral_gap = abs_eigs[1] - abs_eigs[2]
        assert abs(spectral_gap - (1.0 - expected_pos_radius)) < 1e-12


def test_resolvent_trace_tautological_concordance():
    """Verify that H_diag resolvent trace matches prime_kernel K(t) within tail truncation."""
    zeros = []
    with open('data/processed/zeros_10k.csv') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('gamma'):
                parts = line.split(',')
                val = parts[1] if len(parts) > 1 else parts[0]
                try:
                    zeros.append(float(val))
                except ValueError:
                    pass
            if len(zeros) >= 500:
                break

    zeros = np.array(zeros)
    with mp.workdps(30):
        for t_val in (0.5, 1.0):
            k_t = float(prime_kernel(t_val))
            # Pair sum over positive and negative zeros: 2 * sum cos(t*gamma)/(gamma^2 + 1/4)
            tr_diag = 2.0 * np.sum(np.cos(t_val * zeros) / (zeros**2 + 0.25))
            diff = abs(tr_diag - k_t)
            # Concordance within 1e-4 with 500 zeros (truncation tail error)
            assert diff < 1e-4


def test_sierra_laguna_spurious_infrared_states():
    """Verify that naive conformal discretization of Sierra-Laguna operator generates spurious modes below gamma_1."""
    N = 300
    L = 5.0
    u = np.linspace(-L, L, N)
    du = u[1] - u[0]
    g = 1.0 + np.exp(-2 * u)

    H = np.zeros((N, N), dtype=complex)
    for k in range(N - 1):
        val = 1j * (g[k] + g[k + 1]) / (4 * du)
        H[k, k + 1] = val
        H[k + 1, k] = -val

    eigvals = np.sort(np.linalg.eigvalsh(H))
    pos = eigvals[eigvals > 0]

    gamma_1 = 14.134725
    spurious = pos[pos < gamma_1]
    # Naive discretization has many spurious modes below the first Riemann zero
    assert len(spurious) >= 10

    # Spurious modes have roughly constant spacing delta E ~ pi / L
    spacings = np.diff(spurious[:5])
    assert np.std(spacings) < 0.1

    # Resolvent trace of H_SR has O(1) error due to near-zero modes
    tr_SR = np.sum(np.cos(0.5 * pos) / (pos**2 + 0.25))
    with mp.workdps(30):
        k_05 = float(prime_kernel(0.5))
    # Error is large (> 1.0) compared to K(0.5) ~ 0.006
    assert abs(tr_SR - k_05) > 1.0
