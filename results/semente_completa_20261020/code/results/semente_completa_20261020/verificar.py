"""Execução declarada: semente completa e mesma grade de transportes."""
from pathlib import Path
import contextlib,csv,hashlib,io,json,resource,shutil,sys,time
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT),str(ROOT/"src")]
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
expected=(RUN/"DECLARACAO.sha256").read_text().split()[0]
assert hashlib.sha256((RUN/"DECLARACAO.md").read_bytes()).hexdigest()==expected
files=["collatz/balanced_seed.py","collatz/affine_rewrites.py","collatz/cost_residues.py","collatz/family_availability.py","tests/test_collatz_balanced_seed.py","results/semente_completa_20261020/verificar.py"]
hashes={}
for name in files:
 p=ROOT/name;hashes[name]=hashlib.sha256(p.read_bytes()).hexdigest()
 target=RUN/"code"/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
start_cpu,start_wall=time.process_time(),time.perf_counter()
import pytest
out=io.StringIO()
with contextlib.redirect_stdout(out),contextlib.redirect_stderr(out):
 status=pytest.main(["-q","-s",str(ROOT/files[4])])
(RUN/"pytest.log").write_text(out.getvalue())
summary={}
if status==0:
 from collatz.balanced_seed import complete_four_seed,transport_group_seed
 from collatz.cost_residues import generator_counts,project_counts
 from collatz.family_availability import family_group_counts
 fine,seed,catalogue=complete_four_seed()
 seed_rows=[]
 for total in range(4,81):
  for a in range(27):
   if a%3:
    c=[fine[total][a+j*27] for j in range(3)]
    seed_rows.append(dict(S=total,pai=a,filho0=c[0],filho1=c[1],filho2=c[2],grupos=seed[total][a],resto=sum(c)-3*seed[total][a]))
 with (RUN/"semente_tabela.csv").open("w",newline="") as f:
  writer=csv.DictWriter(f,fieldnames=list(seed_rows[0]));writer.writeheader();writer.writerows(seed_rows)
 (RUN/"catalogo.json").write_text(json.dumps(catalogue,indent=2)+"\n")
 rows=[];first_gap=None;central_gap=None
 for depth in range(4,9):
  maximum=2*depth+2
  propagated=transport_group_seed(seed,depth,maximum)
  old=family_group_counts(depth,maximum)
  full=generator_counts(depth,maximum-depth)
  for total in range(2*depth-2,maximum+1):
   counts=full[total-depth];parents=project_counts(counts,depth-1);complete=0;with_groups=0
   for a in sorted(parents):
    c=[counts[a+j*3**(depth-1)] for j in range(3)]
    complete+=min(c)>0;with_groups+=propagated[total][a]>0
    if min(c)>0 and not propagated[total][a]:
     witness=dict(ell=depth,S=total,pai=a,contagens_filhos=c,grupos_prefixo4=0)
     if first_gap is None:first_gap=witness
     if depth==8 and total==16 and central_gap is None:central_gap=witness
   rows.append(dict(ell=depth,S=total,palavras_total=sum(parents.values()),pais_atingidos=len(parents),pais_completos=complete,pais_incompletos=len(parents)-complete,pais_com_grupos_prefixo4=with_groups,pais_completos_sem_grupos_prefixo4=complete-with_groups,pais_com_H=len(old[total]),grupos_prefixo4=sum(propagated[total].values())))
 with (RUN/"transporte_tabela.csv").open("w",newline="") as f:
  writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
 summary=dict(palavras_semente=11664,grupos_semente=len(catalogue),palavras_equilibradas=3*len(catalogue),palavras_restantes=11664-3*len(catalogue),primeira_classe_limite=first_gap,classe_limite_ell8_S16=central_gap,caso_central=next(row for row in rows if row["ell"]==8 and row["S"]==16))
 (RUN/"resumo.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
manifest=dict(declaracao_sha256=expected,arquivos=hashes,pytest_status=int(status),cpu_s=time.process_time()-start_cpu,parede_s=time.perf_counter()-start_wall,cpu_teto_s=30,python=sys.version,pytest=pytest.__version__,aritmetica="inteiros/Fraction",dados_zeros=False,orbitas_positivas=False)
(RUN/"manifesto.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
print(out.getvalue());print(json.dumps(manifest,ensure_ascii=False));print(json.dumps(summary,ensure_ascii=False))
raise SystemExit(int(status))
