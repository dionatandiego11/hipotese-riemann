from fractions import Fraction
from collatz.central_residues import projected_generators,geometric_limit,stationary_half
from collatz.cost_residues import generator_counts,project_counts,cost_counts


def test_projected_cost_counts_against_full_generator():
    for level in range(1,5):
        full=generator_counts(level,2*level)
        for k in range(1,min(2,level)+1):
            projected=projected_generators(level,2*level,k)
            assert projected==[dict(project_counts(row,k)) for row in full]


def test_limit_and_independent_stationary_equation():
    for k in (1,2):
        law=geometric_limit(k)
        assert law==stationary_half(k)
        assert sum(law)==1
        assert all(not law[a] for a in range(0,len(law),3))
    assert geometric_limit(1)==[0,Fraction(1,3),Fraction(2,3)]
    assert geometric_limit(2)==[0,Fraction(8,63),Fraction(16,63),0,
                              Fraction(11,63),Fraction(4,63),0,
                              Fraction(2,63),Fraction(22,63)]


def test_limits_project_and_cost_mass_is_conserved():
    fine=geometric_limit(2)
    assert [sum(fine[a::3]) for a in range(3)]==geometric_limit(1)
    for level in (8,16):
        projected=projected_generators(level,2*level,2)
        assert [sum(row.values()) for row in projected]==cost_counts(level,2*level)
