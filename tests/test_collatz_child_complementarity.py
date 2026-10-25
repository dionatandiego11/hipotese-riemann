from collatz.child_complementarity import exponent_state,minimum_cover,predecessor_parts
from collatz.cost_residues import generator_counts,project_counts


def test_vector_recursion_masks_and_minimum_covers():
    parents_checked = 0
    for depth in range(4,9):
        maximum = 2*depth+2
        previous = generator_counts(depth-1,maximum-depth)
        full = generator_counts(depth,maximum-depth)
        for total in range(2*depth-2,maximum+1):
            fine = full[total-depth]
            parents = project_counts(fine,depth-1)
            for a in parents:
                parts = predecessor_parts(depth,total,a,previous)
                expected = tuple(fine[a+j*3**(depth-1)] for j in range(3))
                assert tuple(sum(p['vector'][j] for p in parts) for j in range(3)) == expected
                absent = {0,1,2}
                for part in parts:
                    absent &= {j for j in range(3) if not part['vector'][j]}
                assert absent == {j for j in range(3) if not expected[j]}
                cover = minimum_cover(parts)
                assert (cover is not None) == all(expected)
                if cover:
                    chosen = [p for p in parts if p['e'] in cover]
                    assert all(any(p['vector'][j] for p in chosen) for j in range(3))
                    if len(cover) > 1:
                        assert not any(p['mask'] == 7 for p in parts)
                    if len(cover) == 3:
                        assert not any(p['mask'] | q['mask'] == 7 for p in parts for q in parts)
                assert len({p['b'] for p in parts}) == len(parts)
                parents_checked += 1
    parts = predecessor_parts(5,9,47,generator_counts(4,4))
    assert [(p['e'],p['vector']) for p in parts] == [(1,(0,1,0)),(3,(1,0,1)),(5,(0,0,0))]
    assert minimum_cover(parts) == (1,3)
    print(f"pais conferidos exatamente={parents_checked}")


def test_exponent_orbit_exact_period_and_rotation():
    cases = 0
    for depth in (3,4,5,6):
        r = 3**(depth-2)
        for a in (1,2,4,5):
            e0 = 1 if a % 3 == 2 else 2
            states = [exponent_state(depth,a,e0+2*t) for t in range(3*r)]
            assert len({c % (3*r) for c,_,_ in states}) == 3*r
            assert len({b for _,b,_ in states[:r]}) == r
            for t,(c,b,k) in enumerate(states):
                next_c,_,_ = exponent_state(depth,a,e0+2*(t+1))
                assert next_c == 4*c+1
                _,rotated_b,rotated_k = exponent_state(depth,a,e0+2*t+2*r)
                assert rotated_b == b
                assert rotated_k == (k+1) % 3
            cases += 1
    print(f"órbitas algébricas conferidas={cases}")
