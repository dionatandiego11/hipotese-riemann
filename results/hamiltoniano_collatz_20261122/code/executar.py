"""Bounded deterministic controls; frozen scope in DECLARACAO.md."""
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
import numpy as np
from mpmath import mp
from collatz.periodic_denominator import periodic_points, weighted_sum
from riemann_spectra.prime_trace_kernel import prime_kernel

OUT=Path(__file__).resolve().parent


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(60,60))
    expected='00a66149edf2aeb2636f477e2aa61db287e0418fc6c2198ecf735a8cb531853a'
    assert hashlib.sha256((OUT/'DECLARACAO.md').read_bytes()).hexdigest()==expected
    paths=['src/riemann_spectra/prime_trace_kernel.py',
           'collatz/periodic_denominator.py',
           'tests/test_hamiltonian_collatz_bridge.py',
           'results/hamiltoniano_collatz_20261122/executar.py']
    hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    (OUT/'code').mkdir(exist_ok=True)
    for p in paths:
        shutil.copyfile(ROOT/p,OUT/'code'/Path(p).name)
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu=time.process_time();wall=time.monotonic()
    run=subprocess.run([str(ROOT/'.venv/bin/python'),'-m','pytest','-q',
                        'tests/test_hamiltonian_collatz_bridge.py'],cwd=ROOT,
                       text=True,capture_output=True,timeout=50)
    (OUT/'pytest.log').write_text(run.stdout+run.stderr)
    if run.returncode:
        raise RuntimeError('Tests failed; see preserved pytest.log')
    rows=[]
    for n in range(1,9):
        for label,a,b in [('T',3,1),('S',1,-1)]:
            pts=[x for _,x in periodic_points(n,a,b)]
            rows.append({'n':n,'map':label,'points':len(pts),
                         'denominator_weighted_sum':str(weighted_sum(n,a,b)),
                         'positive_integer_fixed_points':sum(x>0 and x.denominator==1 for x in pts),
                         'max_denominator':max(x.denominator for x in pts)})
    with mp.workdps(60):
        nodes=[mp.mpf(0),mp.log(2)/2,mp.log(2),mp.log(3),mp.log(5),mp.log(8)]
        gram=np.array([[float(prime_kernel(t-u)) for u in nodes] for t in nodes])
        eig=np.linalg.eigvalsh(gram)
        kernel={'nodes':[mp.nstr(t,55) for t in nodes],
                'kernel_at_zero':mp.nstr(prime_kernel(0),55),
                'gram_float_eigenvalues':eig.tolist(),
                'psd_diagnostic':bool(eig.min()>=-1e-10),
                'certified':False,'zeros_read':False}
    (OUT/'resultados.json').write_text(json.dumps({'collatz':rows,'kernel':kernel},indent=2)+'\n')
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    total_cpu=time.process_time()-cpu+after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    manifest={'declaracao_sha256':expected,'arquivos':hashes,'tests_exit':run.returncode,
              'cpu_s':total_cpu,'wall_s':time.monotonic()-wall,
              'cpu_limit_s':60,'zero_data':False,'randomness':False,
              'precision':'mpmath 60 digits; exact Fraction; numpy eigvalsh diagnostic',
              'outputs':{f:hashlib.sha256((OUT/f).read_bytes()).hexdigest()
                         for f in ('resultados.json','pytest.log')}}
    (OUT/'manifesto.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'tests':run.stdout.strip(),'cpu_s':total_cpu,
                      'kernel':kernel,'collatz_period_two':rows[2:4]},indent=2))


if __name__=='__main__':
    main()
