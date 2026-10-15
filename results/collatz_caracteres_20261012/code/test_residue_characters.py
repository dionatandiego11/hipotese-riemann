from collatz.cost_residues import tuple_oracle, cost_counts
from collatz.residue_characters import (character_sum, character_from_counts,
                                      reduce_polynomial, haar_character)


def test_primitive_root_relation_and_constant():
    for k in range(1, 5):
        m = 3**(k-1)
        polynomial = [0]*(2*m+1)
        for i in (0,m,2*m):
            polynomial[i] = 1
        assert not any(reduce_polynomial(polynomial,k))
        assert reduce_polynomial([1],k)[0] == 1


def test_character_recursion_against_affine_composition():
    for level in range(1,4):
        for cost in range(2*level+1):
            counts = tuple_oracle(level,cost)
            for k in range(1,level+1):
                for h in range(3**k):
                    assert character_sum(level,cost,k,h) == character_from_counts(counts,k,h)
            assert character_sum(level,cost,0,0) == (cost_counts(level,cost)[cost],)


def test_haar_character_is_not_zero_at_all_nonzero_frequencies():
    for k in range(1,5):
        n=3**k
        units={a:1 for a in range(n) if a%3}
        size=len(units)
        for h in range(n):
            result=character_from_counts(units,k,h)
            expected=haar_character(k,h)*size
            assert result == (expected,)+(0,)*(len(result)-1)
