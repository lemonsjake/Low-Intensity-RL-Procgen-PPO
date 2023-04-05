from os import times
import gym
from stable_baselines3 import PPO
from datetime import datetime

#timestamp = datetime.now().strftime('%d-%m-%y-%H_%M')

for n_levels in [1,3,5]:
    print("n_levels: ", n_levels)

    if n_levels == 1:
        for i in range(3, 11):
            print("i: ", i)

            timestamp = datetime.now().strftime('%d-%m-%y-%H_%M')
            print(timestamp)
            
            print("\nBegin Learning")
            env = gym.make("procgen:procgen-coinrun-v0", num_levels=n_levels,
                        render_mode="rgb_array")  # num_levels = 1, 3, 5

            model = PPO("CnnPolicy", env, verbose=1, 
                        tensorboard_log="./tensorboard_logs/multi_policy_experiment/")

            model.learn(total_timesteps=25_000)
            print("\nLearning Complete")

            model.save("models/experimental/" + "nl" + str(n_levels) + "_" + str(i) + "__" + timestamp)
            #model.save("models/" + timestamp)
            print("\nSaved Model")
    else:
        for i in range(1, 11):
            print("i: ", i)

            timestamp = datetime.now().strftime('%d-%m-%y-%H_%M')
            print(timestamp)
            
            print("\nBegin Learning")
            env = gym.make("procgen:procgen-coinrun-v0", num_levels=n_levels,
                        render_mode="rgb_array")  # num_levels = 1, 3, 5

            model = PPO("CnnPolicy", env, verbose=1, 
                        tensorboard_log="./tensorboard_logs/multi_policy_experiment/")

            model.learn(total_timesteps=25_000)
            print("\nLearning Complete")

            model.save("models/experimental/" + "nl" + str(n_levels) + "_" + str(i) + "__" + timestamp)
            #model.save("models/" + timestamp)
            print("\nSaved Model")

### change num_levels (line 8), how does profficiency change? or a similar question.