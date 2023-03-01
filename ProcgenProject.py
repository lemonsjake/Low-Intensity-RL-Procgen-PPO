#import matplotlib.pyplot as plt  #
#import numpy as np  #
#import seaborn as sns  #

import gym3
from procgen import ProcgenGym3Env
from stable_baselines3 import PPO

env = ProcgenGym3Env(num=2, env_name="coinrun")#, render_mode="rgb_array")
#env = gym3.ViewerWrapper(env, info_key="rgb")
model = PPO("CnnPolicy", env, verbose=1)  #MlpPolicy --> CnnPolicy (because input is image)
model.learn(total_timesteps=10_000)
print("DONE LEARNING")
#print(env.get_combos())  #
#step = 0
#step_limit = 1_000  #
vec_env = model.get_env()
obs = vec_env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = vec_env.step(action)
    vec_env.render()
    # VecEnv resets automatically
    # if done:
    #   obs = env.reset()

'''
Look for stable-baselines3 for procgen implementation


while step <= step_limit:  #True
    sample_act = gym3.types_np.sample(env.ac_space, bshape=(env.num,))  #
    env.act(sample_act)  #gym3.types_np.sample(env.ac_space, bshape=(env.num,))
    #print(f"\nACTION: {sample_act}")  #
    rew, obs, first = env.observe()
    #print(f"OBSERVATION: {obs}")  #
    print(f"step {step} reward {rew} first {first}")
    step += 1


import gym
from stable_baselines3 import PPO

env = gym.make("CartPole-v1")

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10_000)

vec_env = model.get_env()
obs = vec_env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = vec_env.step(action)
    vec_env.render()
    # VecEnv resets automatically
    # if done:
    #   obs = env.reset()

env.close()


import githubimport
from openai.procgen import env, interactive
interactive.main()


git status
git add a
git commit -m "changed xyz"
git push

git pull



PPO Main Idea:
policy, simulator (evaluates)
x_num trajectories = evaluated policies
PPO wants to update the policy little by little

'''