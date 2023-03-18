import gym
from stable_baselines3 import PPO

env_test = gym.make("procgen:procgen-coinrun-v0", num_levels=1, render_mode="human")
model = PPO.load("14-03-23-15_32_", env=env_test)
print("\nLoaded Model")

print("\nTesting Model")
vec_env = model.get_env()
obs = vec_env.reset()
for i in range(500):
    if (i % 10) == 0:
        print(str(i))
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = vec_env.step(action)
    vec_env.render()