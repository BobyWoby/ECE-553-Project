"""Synthetic smoke tests only; outputs stay outside deliverables/runs."""
import sys,tempfile
from pathlib import Path
import torch,numpy as np
sys.path.insert(0,'/home/bobywoby/eecs553/deliverables/scripts')
from divergence import measure
from torchmetrics.image.lpip import LearnedPerceptualImagePatchSimilarity
model=LearnedPerceptualImagePatchSimilarity(net_type='alex',normalize=True).cuda().eval()
torch.manual_seed(123)
x=torch.rand(5,2,3,64,64); x[1]=x[0]; valid=torch.ones(5,2,dtype=torch.bool);valid[4,1]=False
rows,mse,lp=measure(x,valid,model,'cuda')
assert mse.shape==lp.shape==(4,2)
assert np.allclose(mse[0],0) and np.allclose(lp[0],0,atol=1e-7)
assert np.isnan(mse[-1,1]) and np.isnan(lp[-1,1]) and rows[-1]['n_valid']==1
with torch.no_grad():
 public=float(model(x[1].cuda(),x[2].cuda()).cpu())
assert np.isclose(public,lp[1].mean(),rtol=1e-5), (public,lp[1])
print('PASS: per-video LPIPS mean equals public TorchMetrics wrapper; identical-frame and padding checks pass.')
