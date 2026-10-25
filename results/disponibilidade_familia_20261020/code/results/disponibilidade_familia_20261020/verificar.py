"""Verificações declaradas e tabela completa de disponibilidade de H."""
from pathlib import Path
import contextlib,csv,hashlib,io,json,resource,shutil,sys,time
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT),str(ROOT/"src")]
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
expected=(RUN/"DECLARACAO.sha256").read_text().split()[0]
assert hashlib.sha256((RUN/"DECLARACAO.md").read_bytes()).hexdigest()==expected
files=["collatz/family_availability.py","collatz/last_digit_rewrites.py","collatz/affine_rewrites.py","collatz/cost_residues.py","tests/test_collatz_family_availability.py","results/disponibilidade_familia_20261020/verificar.py"]
hashes={}
for name in files:
 source=ROOT/name;hashes[name]=hashlib.sha256(source.read_bytes()).hexdigest()
 target=RUN/"code"/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
start_cpu,start_wall=time.process_time(),time.perf_counter()
import pytest
out=io.StringIO()
with contextlib.redirect_stdout(out),contextlib.redirect_stderr(out):
 status=pytest.main(["-q","-s",str(ROOT/files[4])])
(RUN/"pytest.log").write_text(out.getvalue())
rows=[]
if status==0:
 from collatz.family_availability import family_group_counts
 from collatz.cost_residues import generator_counts,project_counts
 for depth in range(4,9):
  maximum=2*depth+2;groups=family_group_counts(depth,maximum);full=generator_counts(depth,maximum-depth)
  for total in range(2*depth-2,maximum+1):
   parents=project_counts(full[total-depth],depth-1);z=groups[total]
   rows.append(dict(ell=depth,S=total,palavras_total=sum(parents.values()),grupos_H=sum(z.values()),palavras_H=3*sum(z.values()),pais_atingidos=len(parents),pais_com_H=len(z),pais_sem_H=len(set(parents)-set(z))))
 with (RUN/"tabela.csv").open("w",newline="") as f:
  writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
 (RUN/"resumo.json").write_text(json.dumps(dict(perfis=len(rows),contraexemplo=dict(ell=8,S=16,pai_sem_H=299,pai_do_grupo_H=971),tabela=rows),indent=2)+"\n")
manifest=dict(declaracao_sha256=expected,arquivos=hashes,pytest_status=int(status),cpu_s=time.process_time()-start_cpu,parede_s=time.perf_counter()-start_wall,cpu_teto_s=30,python=sys.version,pytest=pytest.__version__,aritmetica="inteiros/Fraction",dados_zeros=False,orbitas_positivas=False)
(RUN/"manifesto.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
print(out.getvalue());print(json.dumps(manifest,ensure_ascii=False))
if rows:print(json.dumps(next(row for row in rows if row["ell"]==8 and row["S"]==16)))
raise SystemExit(int(status))
