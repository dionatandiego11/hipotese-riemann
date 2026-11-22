import hashlib
import json
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from mpmath import mp
from collatz.denominator_transfer import adjoint_basis,transfer
from riemann_spectra.prime_trace_kernel import prime_kernel

OUT=Path(__file__).resolve().parent


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(30,30))
    expected='880770ff38936a3534de3fe36b0b0c42b71421719c115b0daa1bd6a3235e4774'
    assert hashlib.sha256((OUT/'DECLARACAO.md').read_bytes()).hexdigest()==expected
    paths=['collatz/denominator_transfer.py','collatz/periodic_denominator.py',
           'src/riemann_spectra/prime_trace_kernel.py','tests/test_operator_domains.py',
           'results/dominios_operadores_20261122/executar.py']
    hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    (OUT/'code').mkdir(exist_ok=True)
    for p in paths:shutil.copyfile(ROOT/p,OUT/'code'/Path(p).name)
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu=time.process_time();wall=time.monotonic()
    run=subprocess.run([str(ROOT/'.venv/bin/python'),'-m','pytest','-q',
                        'tests/test_operator_domains.py'],cwd=ROOT,
                       capture_output=True,text=True,timeout=25)
    (OUT/'pytest.log').write_text(run.stdout+run.stderr)
    if run.returncode:raise RuntimeError('tests failed; log preserved')
    with mp.workdps(80):
        c=1-mp.euler-mp.log(2*mp.pi)
        rows=[]
        for hs in ('0.01','0.0001','0.000001','0.00000001'):
            h=mp.mpf(hs);diff=2*(prime_kernel(0)-prime_kernel(h))/h
            rows.append({'h':hs,'ratio':mp.nstr(diff/mp.log(1/h),65),
                         'constant_corrected':mp.nstr(diff-mp.log(1/h),65),
                         'difference_quotient_norm_squared':mp.nstr(diff/h,65)})
        result={'kernel':rows,'predicted_constant':mp.nstr(c,65),
                'transfer':{str(y):{str(x):str(v) for x,v in transfer(adjoint_basis(y)).items()}
                            for y in range(2,24,3)},
                'zeros_read':False,'certified_interval':False}
    (OUT/'resultados.json').write_text(json.dumps(result,indent=2)+'\n')
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    total_cpu=time.process_time()-cpu+after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    manifest={'declaracao_sha256':expected,'arquivos':hashes,
              'outputs':{p:hashlib.sha256((OUT/p).read_bytes()).hexdigest()
                         for p in ('pytest.log','resultados.json')},
              'tests_exit':run.returncode,'cpu_s':total_cpu,
              'wall_s':time.monotonic()-wall,'cpu_limit_s':30,
              'precision':'Fraction; mpmath80; no zero data'}
    (OUT/'manifesto.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'tests':run.stdout.strip(),'cpu_s':total_cpu,'results':result},indent=2))


if __name__=='__main__':main()
