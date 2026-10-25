from pathlib import Path
import hashlib,json,time,resource
import pytest
r=Path(__file__).resolve().parent
expected=(r/'DECLARACAO.sha256').read_text().split()[0]
assert hashlib.sha256((r/'DECLARACAO.md').read_bytes()).hexdigest()==expected
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
t=time.perf_counter();cpu=time.process_time()
status=pytest.main(['-q','tests/test_negative_moments_polar_profile.py','tests/test_negative_moments_ratios.py'])
(r/'resultado.json').write_text(json.dumps(dict(exit_code=status,wall_seconds=time.perf_counter()-t,cpu_seconds=time.process_time()-cpu,declaration_sha256=expected,real_zeros_used=False,classification='B; controle sintético do perfil polar, não cota do erro para L'),ensure_ascii=False,indent=2)+'\n')
raise SystemExit(status)
