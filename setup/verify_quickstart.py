from pathlib import Path
import tarfile,hashlib,json
root=Path('/home/bobywoby/eecs553/diffusion-forcing'); archive=root/'quickstart_atten.tar.gz.part'
with tarfile.open(archive) as tar:
 for m in tar.getmembers():
  dest=(root/m.name).resolve()
  if not dest.is_relative_to(root.resolve()) or m.issym() or m.islnk() or m.isdev(): raise ValueError(f'Unsafe archive member {m.name}')
 print('Archive members',len(tar.getmembers()))
 tar.extractall(root)
archive.rename(root/'quickstart_atten.tar.gz')
records={}
for f in sorted((root/'outputs').glob('*.ckpt')):
 h=hashlib.sha256()
 with f.open('rb') as s:
  for b in iter(lambda:s.read(8*1024*1024),b''):h.update(b)
 records[f.name]=dict(sha256=h.hexdigest(),bytes=f.stat().st_size)
print(json.dumps(records,indent=2))
Path('/home/bobywoby/eecs553/deliverables/checkpoints.json').write_text(json.dumps(records,indent=2))
print('Minecraft files',len(list((root/'data/minecraft').rglob('*'))))
