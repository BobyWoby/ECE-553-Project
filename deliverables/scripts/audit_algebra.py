#!/usr/bin/env python3
"""Small independent numerical checks of the corrected proof; not experiments."""
import math
K=7
for j in range(1,K+1):
 assert sum(k<j for k in range(K+1))/(K+1)==j/(K+1)
p=[.05,.1,.2,.05,.15,.1,.25,.1]
assert abs(sum(p)-1)<1e-12
assert abs(sum(p[:3])-3*p[3])>.1
alpha=.8;abar_prev=.7;abar=alpha*abar_prev;beta=1-alpha
var=beta*(1-abar_prev)/(1-abar)
assert abs(var-1/(alpha/beta+1/(1-abar_prev)))<1e-12
x0=.4;eps=-.8;x=math.sqrt(abar)*x0+math.sqrt(1-abar)*eps
v=math.sqrt(abar)*eps-math.sqrt(1-abar)*x0
vhat=v+.3;xhat=math.sqrt(abar)*x-math.sqrt(1-abar)*vhat
assert abs((xhat-x0)**2-(1-abar)*(vhat-v)**2)<1e-12
q=[.3,.7];r=[.6,.4]
ratio=sum(a*math.log(b/a) for a,b in zip(q,r))
kl=sum(a*math.log(a/b) for a,b in zip(q,r))
assert abs(ratio+kl)<1e-12 and ratio<0
print('PASS: uniform counts, nonuniform counterexample, posterior variance, v-MSE identity, negative KL sign.')
