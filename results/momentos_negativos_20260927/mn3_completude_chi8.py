"""MN-3, ADENDO_MN3_2 §1: passe de completude D3 para χ₈ (funções de completude_d3.py importadas sem alteração)."""
import json, resource, sys, time
from pathlib import Path
OUT = Path(__file__).parent
ROOT = OUT.parents[1]
sys.path.insert(0, str(ROOT / "results/etapa11_6_controles/dirichlet/completude"))
import numpy as np
import completude_d3 as d3                       # importa dirichlet_zeros congelado
from mn3_caracteres import CHARS

resource.setrlimit(resource.RLIMIT_CPU, (7200, 7260))
ch = CHARS["chi_8"]
src = OUT / "mn3_zeros" / "zeros_chi_8_2000.txt"
zeros = [float(x) for x in np.loadtxt(src)]
dst = OUT / "mn3_zeros_d3"; dst.mkdir(exist_ok=True)
ck = dst / "progresso_d3_chi_8.json"
state = json.loads(ck.read_text()) if ck.exists() else {}
rec_a, a_log = d3.stage_a(ch, zeros, state=state.setdefault("etapa_a", {}), ckpt_path=ck)
corr = d3.merge(zeros, rec_a)
cert = d3.certificate(d3.s_values(corr, ch))
rec_c, c_log = [], {"rounds": []}
if not cert["passed"]:
    rec_c, c_log = d3.stage_c(ch, corr, cert)
    corr = d3.merge(corr, rec_c)
    cert = d3.certificate(d3.s_values(corr, ch))
work = corr[:2000]
checks = d3.reverify(ch, work)
ok = len(corr) == 2002 and cert["passed"] and all(checks[k]["passed"] for k in ("V1", "V3", "V4"))
d3.dz.write_zeros(dst / "zeros_chi_8_2000.txt", work)
man = {"adendo": "ADENDO_MN3_2", "entrada": {"arquivo": str(src.relative_to(ROOT)), "sha256": d3.dz.sha256_of(src)},
       "n_recuperados_a": len(rec_a), "n_recuperados_c": len(rec_c), "recuperados": sorted(rec_a + rec_c),
       "n_corrigida": len(corr), "contagem_v2": 2002, "certificado": cert,
       "verificacoes": {k: {"passed": v["passed"]} for k, v in checks.items()},
       "all_checks_passed": bool(ok), "etapa_a": {k: v for k, v in a_log.items() if k != "intervals_with_zeros"},
       "saida_sha256": d3.dz.sha256_of(dst / "zeros_chi_8_2000.txt"), "terminado": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
(dst / "manifest_chi_8_2000.json").write_text(json.dumps(man, indent=1, ensure_ascii=False), encoding="utf-8")
print(json.dumps({k: man[k] for k in ("n_recuperados_a", "n_recuperados_c", "n_corrigida", "all_checks_passed")}))
