from pathlib import Path
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import unquote,urljoin,urldefrag
from concurrent.futures import ThreadPoolExecutor
import subprocess,hashlib,json
out=Path('/home/bobywoby/eecs553/setup/official-wheelhouse');out.mkdir(exist_ok=True)
pkgs=[('torch','2.4.1+cu121'),('nvidia-cudnn-cu12','9.1.0.70'),('nvidia-cublas-cu12','12.1.3.1'),('triton','3.0.0'),('nvidia-cusparse-cu12','12.1.0.106'),('nvidia-nccl-cu12','2.20.5'),('nvidia-cusolver-cu12','11.4.5.107')]
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  if tag=='a':self.links.append(dict(attrs).get('href',''))
records=[]
for name,v in pkgs:
 base=f'https://download.pytorch.org/whl/cu121/{name}/';p=Links()
 with urlopen(base,timeout=30) as f:p.feed(f.read().decode())
 choices=[]
 for raw in p.links:
  full=urljoin(base,raw);url,fragment=urldefrag(full);filename=unquote(url.rsplit('/',1)[1])
  if filename.startswith(name.replace('-','_')+'-'+v+'-') and 'x86_64' in filename and ('linux' in filename) and ('cp310' in filename or 'py3-' in filename):choices.append((url,fragment.removeprefix('sha256='),filename))
 if name=='triton':choices=[c for c in choices if '-3.0.0-cp310-' in c[2]]
 assert len(choices)==1,(name,choices)
 url,sha,filename=choices[0];assert len(sha)==64
 records.append(dict(url=url,sha256=sha,filename=filename))
(out/'manifest.json').write_text(json.dumps(records,indent=2))
def fetch(r):
 path=out/r['filename'];part=path.with_suffix('.part')
 subprocess.run(['curl','-L','--fail','--retry','2','-sS',r['url'],'-o',str(part)],check=True)
 with part.open('rb') as f:h=hashlib.file_digest(f,'sha256').hexdigest()
 assert h==r['sha256'],(r['filename'],h)
 part.rename(path);print('Verified',r['filename'],flush=True)
with ThreadPoolExecutor(max_workers=7) as pool:list(pool.map(fetch,records))
