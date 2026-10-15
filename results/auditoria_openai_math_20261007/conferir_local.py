"""Conferências exatas e estáticas; não executa Lean nem consulta zeros."""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib, re, shutil, resource
P=Path(__file__).resolve().parent
ROOT=P.parents[1]
A=ROOT/'archive/fontes_etapa11/openai_math_adc7f124'
class Poly(dict):
 def __init__(self,x=0):
  super().__init__(x if isinstance(x,dict) else {(0,0):F(x)})
 def __add__(self,b):
  b=Poly(b);r=Poly(self)
  for k,v in b.items():r[k]=r.get(k,0)+v
  return Poly({k:v for k,v in r.items() if v})
 __radd__=__add__
 def __neg__(self):return Poly({k:-v for k,v in self.items()})
 def __sub__(self,b):return self+-Poly(b)
 def __rsub__(self,b):return Poly(b)+-self
 def __mul__(self,b):
  b=Poly(b);r={}
  for (i,j),v in self.items():
   for (k,l),w in b.items():r[i+k,j+l]=r.get((i+k,j+l),0)+v*w
  return Poly({k:v for k,v in r.items() if v})
 __rmul__=__mul__
 def __pow__(self,n):
  r=Poly(1)
  for _ in range(n):r=r*self
  return r
y=Poly({(1,0):F(1)});d=Poly({(0,1):F(1)})
v=51+41*y;py=7+18*y+8*y**2
jy=185+170*y+(-138+12*y+96*y**2)*d
lhs=v*(2*jy*(1+(3+8*y)*d)-468*(F(5,6)-d)*d*py)
rhs=(3+5*y)*((4*v*d-79)**2+49)+4*y*(4*v*d*((1+3*y)*(15+32*y)*d+9-13*y)+265+3485*y)
assert not lhs-rhs
# Cross-check that the helper can detect an altered identity.
assert lhs-(rhs+1)
J=(F(5,6)-d)*F(1,18)*(37+34*y)+d*F(1,9)*py
assert not J*108-jy
assert F(49,440640)>F(1,10000)
files=json.loads((P/'fontes.json').read_text())
failed=[r['path'] for r in files if hashlib.sha256((A/r['path']).read_bytes()).hexdigest()!=r['sha256']]
assert not failed
imports=json.loads((P/'imports.json').read_text())
missing=sorted({i for im in imports.values() for i in im if i.startswith('OAI.') and i not in imports})
external=sorted({i for im in imports.values() for i in im if not i.startswith('OAI.')})
hits=[]
for m in imports:
 t=(A/('lean/'+m.replace('.','/')+'.lean')).read_text()
 for n,l in enumerate(t.splitlines(),1):
  if re.search(r'\b(sorry|sorryAx|admit|axiom|unsafe|cheat)\b',l):hits.append({'module':m,'line':n,'text':l})
result={'scope':'exact polynomial identity + lexical scan of PARTIAL import graph; NOT formal proof verification',
 'records':len(files),'oai_modules':len(imports),'frontier_missing':missing,
 'external_imports_observed':external,'lexical_hits_including_comments':hits,
 'all_source_hashes_match':not failed,'eq_20_9_exact':not lhs-rhs,
 'J_identity_exact':not J*108-jy,'strict_margin_exact':str(F(49,440640)-F(1,10000)),
 'gaussian_exponent_old':str(F(1,8)),'gaussian_exponent_with_7_8':str(F(9,128)),
 'exponent_ratio':str(F(9,16)),
 'tools':{s:shutil.which(s) for s in ['lean','lake','elan','comparator','landrun','lean4export']},
 'cpu_seconds':resource.getrusage(resource.RUSAGE_SELF).ru_utime+resource.getrusage(resource.RUSAGE_SELF).ru_stime}
(P/'conferencia_local.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['external_imports_observed','frontier_missing','lexical_hits_including_comments']},indent=2))
print('frontier',len(missing),'external roots',sorted({s.split('.')[0] for s in external}),'lexical hits',len(hits))
