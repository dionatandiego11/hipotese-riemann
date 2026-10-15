import hashlib
import json
import math
from pathlib import Path
import resource
import time
from fractions import Fraction
from collatz.cost_residues import (cost_counts, generator_counts, tuple_oracle,
                                  conditional_weights, tail_bound, project_counts)

folder = Path(__file__).resolve().parent
expected = (folder / 'DECLARACAO.sha256').read_text().split()[0]
assert hashlib.sha256((folder / 'DECLARACAO.md').read_bytes()).hexdigest() == expected
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
started, cpu = time.monotonic(), time.process_time()
identities = projections = tails = 0
rows = []
for level in range(1, 7):
    maximum = 2 * level
    maps = generator_counts(level, maximum)
    totals = cost_counts(level, maximum)
    for cost, counts in enumerate(maps):
        assert counts == tuple_oracle(level, cost)
        assert sum(counts.values()) == totals[cost]
        assert all(root % 3 for root in counts)
        if totals[cost]:
            assert sum(Fraction(n, totals[cost]) for n in counts.values()) == 1
        identities += 1
        for resolution in range(min(level, 3) + 1):
            direct = project_counts(counts, resolution)
            via = project_counts(project_counts(counts, level), resolution)
            assert direct == via and sum(direct.values()) == totals[cost]
            projections += 1
for level in (16, 24, 32, 64):
    for cost in (level, level + math.isqrt(level), 2 * level):
        weights = conditional_weights(level, cost)
        assert sum(weights) == 1
        for cutoff in (1, 2, 4, 8, 16):
            actual = sum(weights[cutoff:], Fraction(0))
            bound = tail_bound(level, cost, cutoff)
            assert actual <= bound
            rows.append({'level': level, 'cost': cost, 'cutoff': cutoff,
                         'tail_exact': str(actual), 'bound_exact': str(bound)})
            tails += 1
result = {'status': 'validado', 'declaration_sha256': expected,
          'generator_identities': identities, 'projections': projections,
          'tail_inequalities': tails, 'arithmetic': 'inteiros e Fraction',
          'cpu_seconds': time.process_time()-cpu,
          'wall_seconds': time.monotonic()-started,
          'peak_rss_kib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          'rows': rows,
          'limits': 'Não demonstra controle relativo uniforme por resíduo.'}
(folder / 'resultados.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'rows'}, indent=2))
