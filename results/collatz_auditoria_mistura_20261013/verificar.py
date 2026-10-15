from pathlib import Path
from fractions import Fraction
import hashlib,json,resource,time
from collatz.residue_characters import reduce_polynomial
folder=Path(__file__).resolve().parent
expected=(folder/'DECLARACAO.sha256').read_text().split()[0]
assert hashlib.sha256((folder/'DECLARACAO.md').read_bytes()).hexdigest()==expected
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
wall,cpu=time.monotonic(),time.process_time()


def ring_product(a,b,n):
    out=[Fraction(0)]*n
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:
                    out[(i+j)%n]+=x*y
    return out


def conjugate(a,n):
    out=[Fraction(0)]*n
    for i,x in enumerate(a):
        out[-i%n]+=x
    return out


def character(values,h,n):
    out=[Fraction(0)]*n
    for a,x in enumerate(values):
        out[(h*a)%n]+=x
    return out

fourier=energies=masses=0
for level in (2,3):
    n=3**level
    nu=[Fraction((y+1)%4,7) for y in range(n)]
    for prefix in range(1,level):
        eta=[Fraction((2*b+1)%5,11) for b in range(3**(level-prefix))]
        for total in (prefix,prefix+2):
            scale=3**prefix*pow(2,-total,n)
            pushed=[Fraction(0)]*n
            for b,x in enumerate(eta):
                pushed[scale*b%n]+=x
            mu=ring_product(nu,pushed,n)
            assert sum(mu)==sum(nu)*sum(eta)
            masses+=1
            for h in range(n):
                direct=character(mu,h,n)
                product=ring_product(character(nu,h,n),character(pushed,h,n),n)
                assert reduce_polynomial(direct,level)==reduce_polynomial(product,level)
                fourier+=1
            full_energy=[Fraction(0)]*n
            for h in range(n):
                f=character(nu,h,n)
                sq=ring_product(f,conjugate(f,n),n)
                full_energy=[a+b for a,b in zip(full_energy,sq)]
            reduced=reduce_polynomial(full_energy,level)
            assert reduced==(n*sum(x*x for x in nu),)+(0,)*(len(reduced)-1)
            energies+=1
            for coarse in range(level+1):
                groups=3**coarse
                means=[sum(mu[a::groups])/Fraction(n,groups) for a in range(groups)]
                difference=[x-means[a%groups] for a,x in enumerate(mu)]
                spectral=[Fraction(0)]*n
                for h in range(n):
                    f=character(mu,h,n)
                    d=character(difference,h,n)
                    if h%(n//groups)==0:
                        assert not any(reduce_polynomial(d,level))
                    else:
                        assert reduce_polynomial(d,level)==reduce_polynomial(f,level)
                        sq=ring_product(f,conjugate(f,n),n)
                        spectral=[a+b for a,b in zip(spectral,sq)]
                reduced=reduce_polynomial(spectral,level)
                assert reduced==(n*sum(x*x for x in difference),)+(0,)*(len(reduced)-1)
                energies+=1
tails=0
for j in range(11):
    for numerator in range(3):
        probability=Fraction(1,2**j)
        # Cubar elimina a potência fracionária: 3b=3j+numerator.
        rhs=Fraction(2)**(3-3*j-numerator)
        assert probability**3<=rhs
        tails+=1
source=Path('archive/fontes_etapa11/collatz_stationnaire_20261012/tao_1909.03562v5.pdf')
assert hashlib.sha256(source.read_bytes()).hexdigest()=='99fa919e0e43f0c161fbdc8d9011069c92b57d2a2a09444ae2ca77ef826191dd'
result={'status':'validado em auditoria interna limitada','declaration_sha256':expected,
        'fourier_product_checks':fourier,'parseval_and_projection_checks':energies,
        'mass_checks':masses,'real_tail_checks':tails,
        'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-wall,
        'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'independent_review':False,'deep_tao_proof_reconstructed':False}
(folder/'resultados.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
