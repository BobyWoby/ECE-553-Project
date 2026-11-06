import gym, d4rl, torch
from stable_baselines3.common.vec_env import DummyVecEnv
print('torch',torch.__version__,'CUDA',torch.cuda.is_available())
for name in ['maze2d-medium-v1','maze2d-large-v1']:
 env=DummyVecEnv([lambda: gym.make(name) for _ in range(2)])
 env.seed(0)
 x=env.reset(); out=env.step([env.action_space.sample() for _ in range(2)])
 print(name,'reset',x.shape,'step',out[0].shape,'reward',out[1].tolist())
 env.close()
print('PASS: setup only, no checkpoint evaluation')
