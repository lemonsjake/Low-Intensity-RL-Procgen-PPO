import gym
from stable_baselines3 import PPO
from datetime import datetime

timestamp = datetime.now().strftime('%d-%m-%y-%H_%M')

print("\nBegin Learning")
env = gym.make("procgen:procgen-coinrun-v0", num_levels=0,
               render_mode="rgb_array")  # num_levels = 1, 10, 25, 50, 100

model = PPO("CnnPolicy", env, verbose=1, 
            tensorboard_log="./tensorboard_logs/")

model.learn(total_timesteps=25_000)  # total_timesteps = 5_000, 25_000, 50_000, 125_000
print("\nLearning Complete")

model.save("models/" + timestamp)

print("\nSaved Model")

### change num_levels (line 8), how does profficiency change? or a similar question.