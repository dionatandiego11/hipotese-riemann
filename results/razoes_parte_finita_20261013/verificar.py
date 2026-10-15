from pathlib import Path
import hashlib,json,time,resource
import pytest
r=Path(__file__).resolve().parent
expected=(r/'DECLARACAO.sha256').read_text().split()[0]
assert hashlib.sha256((r/'DECLARACAO.md').read_bytes()).hexdigest()==expected
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
t=time.perf_counter();cpu=time.process_time()
status=pytest.main(['-q','tests/test_negative_moments_finite_part.py','tests/test_negative_moments_contours.py','tests/test_negative_moments_ratios.py','tests/test_discrete_moments.py'])
(r/'resultado.json').write_text(json.dumps(dict(exit_code=status,wall_seconds=time.perf_counter()-t,cpu_seconds=time.process_time()-cpu,declaration_sha256=expected,real_zeros_used=False,classification='B; controles sintéticos, não certificação ou inferiores de L'),ensure_ascii=False,indent=2)+'\n')
raise SystemExit(status)
