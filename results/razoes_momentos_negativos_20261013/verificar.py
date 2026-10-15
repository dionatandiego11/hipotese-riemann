from pathlib import Path
import hashlib,json,resource,time
import mpmath as mp
from riemann_spectra.negative_moments_ratios import (arithmetic_diagonal,
                                                   diagonal_laurent,two_zero_model)
folder=Path(__file__).resolve().parent
expected=(folder/'DECLARACAO.sha256').read_text().split()[0]
assert hashlib.sha256((folder/'DECLARACAO.md').read_bytes()).hexdigest()==expected
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
wall,cpu=time.monotonic(),time.process_time()
mp.mp.dps=70
rows=[]
for q in (1,4,5,8,12):
    for kind in (7,8):
        r,b=diagonal_laurent(q,kind)
        checks=[]
        for h in map(mp.mpf,('1e-4','1e-6','1e-8')):
            d1,d2=arithmetic_diagonal(h,q,kind),arithmetic_diagonal(2*h,q,kind)
            r_extrap=2*h*(d1-d2)
            b_extrap=2*(d1-r/h)-(d2-r/(2*h))
            checks.append({'alpha':str(h),'residue_extrapolation_error':mp.nstr(abs(r_extrap-r),25),
                           'finite_extrapolation_error':mp.nstr(abs(b_extrap-b),25)})
        rows.append({'q':q,'kind':kind,'residue':mp.nstr(r,40),'finite_part':mp.nstr(b,40),'checks':checks})
models=[]
for gap in map(mp.mpf,('1','0.01')):
    for ratio in map(mp.mpf,('1','0.1','0.01')):
        e=gap*ratio
        points=sorted(set([-mp.inf,-gap,-e,mp.mpf(0),e,gap/2,gap-e,gap,gap+e,2*gap,mp.inf]))
        f=lambda t:1/((e*e+t*t)*(e*e+(t-gap)**2))
        h=lambda t:(e*e+(t-gap/2)**2)*f(t)
        values={'reciprocal':e/mp.pi*mp.quad(f,points),
                'weighted':e/mp.pi*mp.quad(h,points)}
        formula=two_zero_model(gap,e)
        errors={name:abs(value-formula[name]) for name,value in values.items()}
        assert all(err<mp.mpf('1e-40')*max(1,abs(formula[name])) for name,err in errors.items())
        models.append({'gap':str(gap),'epsilon_over_gap':str(ratio),
                       'reciprocal_relative_to_discrete':mp.nstr(formula['reciprocal']/formula['reciprocal_target'],30),
                       'weighted_relative_to_discrete':mp.nstr(formula['weighted']/formula['weighted_target'],30),
                       'quadrature_errors':{name:mp.nstr(err,20) for name,err in errors.items()}})
result={'status':'verificações B; não certificação de razões ou termos inferiores discretos',
        'declaration_sha256':expected,'dps':mp.mp.dps,'laurent':rows,'synthetic_two_zero':models,
        'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-wall,
        'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'actual_zeros_read':False,
        'interval_certified':False}
(folder/'resultados.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('laurent','synthetic_two_zero')},indent=2))
