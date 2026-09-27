import resource
resource.setrlimit(resource.RLIMIT_CPU,(600,600))
import hashlib,json,sys
from pathlib import Path
root=Path(__file__).resolve().parents[2]
folder=Path(__file__).resolve().parent
lock=json.loads((folder/'lock.json').read_text())
for name,h in lock.items():
 assert hashlib.sha256((root/name).read_bytes()).hexdigest()==h,name
assert not (folder/'checkpoint.json').exists(),'No silent rerun/overwrite'
sys.path.insert(0,str(root/'src'))
from riemann_spectra.loss_viability import run
run(folder)
