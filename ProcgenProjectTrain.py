import gym
from stable_baselines3 import PPO
from datetime import datetime

print("\nBegin Learning")
env = gym.make("procgen:procgen-coinrun-v0", num_levels=1,
               render_mode="rgb_array")
model = PPO("CnnPolicy", env, verbose=1, 
            tensorboard_log="./tensorboard_logs/")

model.learn(total_timesteps=25_000)
print("\nLearning Complete")

model.save(datetime.now().strftime('%d-%m-%y-%H_%M_'))
del model  # delete trained model to demonstrate loading
print("\nSaved Model")