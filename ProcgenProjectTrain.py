from os import times
import gym
from stable_baselines3 import PPO
from datetime import datetime

#timestamp = datetime.now().strftime('%d-%m-%y-%H_%M')
#for i in range(1, 11):
    #print("i: ", i)

timestamp = datetime.now().strftime('%d-%m-%y-%H_%M')
print(timestamp)
            
print("\nBegin Learning")
env = gym.make("procgen:procgen-coinrun-v0", num_levels=0,
                render_mode="rgb_array")  # num_levels = 1, 3, 5

model = PPO("CnnPolicy", env, verbose=1, 
                tensorboard_log="./tensorboard_logs/")

model.learn(total_timesteps=125_000)
print("\nLearning Complete")

model.save("models/" + timestamp)
#model.save("models/" + timestamp)
print("\nSaved Model")