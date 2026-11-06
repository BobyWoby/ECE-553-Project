import json,time,torch
from pathlib import Path
start=time.time()
assert torch.cuda.is_available(), 'CUDA unavailable in PyTorch'
x=torch.arange(1024,device='cuda',dtype=torch.float32)
assert torch.allclose(x.square().sum(),torch.tensor(sum(i*i for i in range(1024)),device='cuda',dtype=torch.float32))
a=torch.randn(512,512,device='cuda'); b=a@a.T
torch.cuda.synchronize()
assert torch.isfinite(b).all()
info={'torch':torch.__version__,'torch_cuda':torch.version.cuda,'device':torch.cuda.get_device_name(0),'vram_bytes':torch.cuda.get_device_properties(0).total_memory,'cuda_tensor_and_matmul_check':'PASS','wall_seconds':time.time()-start,'kind':'setup smoke test, not research experiment'}
Path('/home/bobywoby/eecs553/setup/cuda_check.json').write_text(json.dumps(info,indent=2));print(json.dumps(info,indent=2))
