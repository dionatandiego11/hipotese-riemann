"""Exploração declarada: grade imutável, inteiros exatos."""
from pathlib import Path
from collections import Counter, defaultdict
import csv, hashlib, json, resource, shutil, sys, time
ROOT=Path(__file__).resolve().parents[2];RUN=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT),str(ROOT/"src")]
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
expected=(RUN/"DECLARACAO.sha256").read_text().split()[0]
assert hashlib.sha256((RUN/"DECLARACAO.md").read_bytes()).hexdigest()==expected
files=["collatz/block_rewrites.py","results/blocos_tres_20261019/explorar.py"]
hashes={}
for name in files:
 p=ROOT/name;hashes[name]=hashlib.sha256(p.read_bytes()).hexdigest()
 target=RUN/"code"/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
start_cpu,start_wall=time.process_time(),time.perf_counter()
from collatz.block_rewrites import triple_fibers,triple_numerator
rows=[];witnesses=[]
for position in (1,2,3):
 for total in range(3,19):
  fibers=triple_fibers(position,total)
  counts=Counter(len(children) for children in fibers.values())
  rows.append(dict(i=position,S=total,classes_1=counts[1],classes_2=counts[2],classes_3=counts[3],blocos=sum(len(w) for children in fibers.values() for w in children.values())))
  for coarse,children in sorted(fibers.items()):
   if len(children)==3:
    witnesses.append(dict(i=position,S=total,classe=coarse,palavras=[min(children[j]) for j in range(3)]))
first=defaultdict(list)
for a in (1,2):
 for b in range(1,7):
  first[triple_numerator((a,b,1))%9].append(dict(a=a,b=b,B=triple_numerator((a,b,1))))
assert all(len(v)==2 for v in first.values())
with (RUN/"tabela.csv").open("w",newline="") as f:
 writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
(RUN/"testemunhas.json").write_text(json.dumps(witnesses,indent=2)+"\n")
(RUN/"primeiro_bloco.json").write_text(json.dumps(dict(sorted(first.items())),indent=2)+"\n")
manifest=dict(declaracao_sha256=expected,arquivos=hashes,cpu_s=time.process_time()-start_cpu,parede_s=time.perf_counter()-start_wall,cpu_teto_s=30,python=sys.version,grade_registros=len(rows),fibras_com_3_filhos=len(witnesses),dados_zeros=False,orbitas_positivas=False)
(RUN/"manifesto_exploracao.json").write_text(json.dumps(manifest,indent=2)+"\n")
print(json.dumps(manifest))
for position in (1,2,3):
 print("i=",position,"primeira testemunha=",next((w for w in witnesses if w["i"]==position),None))
