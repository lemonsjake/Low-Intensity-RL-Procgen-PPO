import gym
from stable_baselines3 import PPO


env_test = gym.make("procgen:procgen-coinrun-v0", num_levels=0, render_mode="human")
model = PPO.load("models/30-04-23-15_54", env=env_test)
print("\nLoaded Model")

print("\nTesting Model")
vec_env = model.get_env()
obs = vec_env.reset()
for i in range(1000):
    if (i % 100) == 0:
        print("step = " + str(i))
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = vec_env.step(action)
    vec_env.render()


### nl1_4: blu/snw- stnd still, lava- death, grnYlw/brwn- success, blk/brwn- success, rock/grn- success, 3/5, stnd still 1/5, death 1/5
### nl5_1: blu/snw- success, lava- walk/jmp then stnd still, grnYlw/brn- success, blk/brwn- success, rock/grn- jmp same spot agnst back wall, 3/5, stnd still / jmp 2/5
### nl5_10: blu/snw- success, lava- death, grnYlw/brn- success, blk/brwn- success, rock/grn- stnd still, 3/5, stnd still 1/5, death 1/5
### nl5_1 < nl1_4 < nl5_10, nl1_4 better than nl5_1 because success and death vs stnd still / jmp and nl5_10 better than nl1_4 better because faster