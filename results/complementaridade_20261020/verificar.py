"""Diagnóstico declarado das parcelas positivas e ciclos aritméticos."""
from pathlib import Path
from collections import Counter
import contextlib,csv,hashlib,io,json,resource,shutil,sys,time
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT),str(ROOT/"src")]
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
expected=(RUN/"DECLARACAO.sha256").read_text().split()[0]
assert hashlib.sha256((RUN/"DECLARACAO.md").read_bytes()).hexdigest()==expected
files=["collatz/child_complementarity.py","collatz/cost_residues.py","tests/test_collatz_child_complementarity.py","results/complementaridade_20261020/verificar.py"]
hashes={}
for name in files:
 source=ROOT/name;hashes[name]=hashlib.sha256(source.read_bytes()).hexdigest()
 target=RUN/"code"/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
start_cpu,start_wall=time.process_time(),time.perf_counter()
import pytest
out=io.StringIO()
with contextlib.redirect_stdout(out),contextlib.redirect_stderr(out):
 status=pytest.main(["-q","-s",str(ROOT/files[2])])
(RUN/"pytest.log").write_text(out.getvalue())
summary={}
if status==0:
 from collatz.child_complementarity import predecessor_parts,minimum_cover
 from collatz.cost_residues import generator_counts,project_counts
 rows=[];profiles=[];witnesses={};known=None
 for depth in range(4,9):
  maximum=2*depth+2
  previous=generator_counts(depth-1,maximum-depth)
  full=generator_counts(depth,maximum-depth)
  for total in range(2*depth-2,maximum+1):
   fine=full[total-depth];parents=project_counts(fine,depth-1);classification=Counter()
   for a in sorted(parents):
    parts=predecessor_parts(depth,total,a,previous)
    cover=minimum_cover(parts)
    size=len(cover) if cover else 0;classification[size]+=1
    vector=[fine[a+j*3**(depth-1)] for j in range(3)]
    rows.append(dict(n=depth,S=total,pai=a,filho0=vector[0],filho1=vector[1],filho2=vector[2],min_parcelas=size,expoentes="|".join(map(str,cover)) if cover else "",parcelas_produtivas=sum(p["mask"]!=0 for p in parts)))
    key=str(size)
    data=dict(n=depth,S=total,pai=a,vector=vector,cobertura=cover,parcelas=parts)
    if key not in witnesses:witnesses[key]=data
    if depth==5 and total==9 and a==47:known=data
   profiles.append(dict(n=depth,S=total,pais=len(parents),incompletos=classification[0],uma=classification[1],duas=classification[2],tres=classification[3]))
 with (RUN/"pais_tabela.csv").open("w",newline="") as f:
  writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
 with (RUN/"perfis_tabela.csv").open("w",newline="") as f:
  writer=csv.DictWriter(f,fieldnames=list(profiles[0]));writer.writeheader();writer.writerows(profiles)
 summary=dict(pais=len(rows),perfis=len(profiles),primeiras_testemunhas=witnesses,caso_conhecido=known,caso_central=next(row for row in profiles if row["n"]==8 and row["S"]==16))
 (RUN/"resumo.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
manifest=dict(declaracao_sha256=expected,arquivos=hashes,pytest_status=int(status),cpu_s=time.process_time()-start_cpu,parede_s=time.perf_counter()-start_wall,cpu_teto_s=30,python=sys.version,pytest=pytest.__version__,aritmetica="inteiros exatos",dados_zeros=False,orbitas_positivas=False)
(RUN/"manifesto.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
print(out.getvalue());print(json.dumps(manifest,ensure_ascii=False))
if summary:
 print(json.dumps(dict(pais=summary['pais'],perfis=summary['perfis'],caso_central=summary['caso_central']),ensure_ascii=False))
 print("primeira cobertura de3:",json.dumps(summary['primeiras_testemunhas'].get('3'),ensure_ascii=False))
raise SystemExit(int(status))
