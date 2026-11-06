"""Fetch exact PyPI wheels in ranges; verify publisher index SHA256 before use."""
from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
import urllib.request,json,math,hashlib,time
out=Path('/home/bobywoby/eecs553/setup/remaining-wheelhouse');out.mkdir(exist_ok=True)
packages=[('triton','3.0.0'),('nvidia-cusparse-cu12','12.1.0.106')]
records=[]
for name,version in packages:
 with urllib.request.urlopen(f'https://pypi.org/pypi/{name}/{version}/json') as f:j=json.load(f)
 options=[v for v in j['urls'] if v['filename'].endswith('.whl') and 'x86_64' in v['filename'] and ('manylinux' in v['filename'] or 'linux_x86_64' in v['filename']) and ('cp310' in v['filename'] or 'py3-' in v['filename'])]
 assert len(options)==1,(name,[v['filename'] for v in options]);records.append(options[0])
(out/'manifest.json').write_text(json.dumps(records,indent=2))
def part(record,i):
 size=record['size'];chunk=math.ceil(size/16);lo=i*chunk;hi=min(size-1,lo+chunk-1);p=out/(record['filename']+f'.part{i}')
 if p.exists() and p.stat().st_size==hi-lo+1:return
 for attempt in range(3):
  try:
   existing=p.stat().st_size if p.exists() else 0
   req=urllib.request.Request(record['url'],headers={'Range':f'bytes={lo+existing}-{hi}'})
   with urllib.request.urlopen(req,timeout=120) as response,p.open('ab') as f:
    assert response.status==206,response.status
    while data:=response.read(1024*1024):f.write(data)
   assert p.stat().st_size==hi-lo+1;return
  except Exception:
   if attempt==2:raise
   time.sleep(2)
with ThreadPoolExecutor(max_workers=32) as pool:
 futures=[pool.submit(part,r,i) for r in records for i in range(16)]
 for n,f in enumerate(as_completed(futures),1):
  f.result()
  if n%16==0:print(f'{n}/{len(futures)} segments downloaded',flush=True)
for r in records:
 p=out/r['filename']
 with p.open('wb') as target:
  for i in range(16):
   pp=out/(r['filename']+f'.part{i}')
   with pp.open('rb') as src:
    while data:=src.read(8*1024*1024):target.write(data)
   pp.unlink()
 with p.open('rb') as f:actual=hashlib.file_digest(f,'sha256').hexdigest()
 assert actual==r['digests']['sha256'],p
 print('Verified',p.name,flush=True)
