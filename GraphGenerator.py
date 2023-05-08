import matplotlib.pyplot as plt

#  key=agent_num/18 : [b=final_rwd, c=num_lvls, d=timesteps]
correlated_agent_dict = {"16":[1.8, 0, 5_000], "1":[2.1, 1, 25_000], "2":[1.7, 10, 25_000], "3":[3.8, 25, 25_000], "4":[2, 50, 25_000], "5":[1.8, 100, 25_000],
                       "17":[3.9, 0, 25_000], "6":[0, 1, 5_000], "7":[3.3, 10, 5_000], "8":[1.8, 25, 5_000], "9":[1.1, 50, 5_000], "10":[3.3, 100, 5_000],
                       "18":[3.3, 0, 125_000], "11":[10, 1, 125_000], "12":[3.9, 10, 125_000], "13":[2.2, 25, 125_000], "14":[3.7, 50, 125_000], "15":[3.1, 100, 125_000]}

for nl in correlated_agent_dict.values():
    if nl[1] == 0:
        nl[1] = 1
    elif nl[1] == 1:
        nl[1] = 2
    elif nl[1] == 10:
        nl[1] = 3
    elif nl[1] == 25:
        nl[1] = 4
    elif nl[1] == 50:
        nl[1] = 5
    elif nl[1] == 100:
        nl[1] = 6

x_levels = ["0", "1", "10", "25", "50", "100"]
x_custom_spread = [1, 2, 3, 4, 5, 6]
timestep_color = ""
timestep_marker = ""

plt.figure()
plt.xticks(x_custom_spread, x_levels)  #  0, 1, 10, 25, 50, 100
plt.gca().update(dict(title="Initial Agent Set Final Reward", xlabel="# of Levels (num_levels)", ylabel="Final Reward"))  #  Code influence via https://stackoverflow.com/users/2749397/gboffi, https://stackoverflow.com/questions/42223587/how-to-add-title-and-xlabel-and-ylabel

i = 0
while i < 18:
    for val in correlated_agent_dict.values():
        r, n, t = val  #  r-reward, n-num_levels, t-timesteps
        if t == 5_000:
            timestep_color = 'r'  #  assign color red
            timestep_symbol = 's'  #  assign symbol square
            if i == 0:
                plt.scatter(n, r, color=timestep_color, marker=timestep_symbol, label="5_000 Timesteps")
        elif t == 25_000:
            timestep_color = 'g'  #  assign color green
            timestep_symbol = 'o'  #  assign symbol circle
            if i == 6:
                plt.scatter(n, r, color=timestep_color, marker=timestep_symbol, label="25_000 Timesteps")
        elif t == 125_000:
            timestep_color = 'b'  #  assign color blue
            timestep_symbol = '^'  #  assign symbol triangle
            if i == 12:
                plt.scatter(n, r, color=timestep_color, marker=timestep_symbol, label="125_000 Timesteps")
        plt.scatter(n, r, color=timestep_color, marker=timestep_symbol)
        i += 1

plt.grid(True)
plt.legend()

plt.show()



'''
3.9 - 0   - 25k (17 /18)

2.1 - 1   - 25k
1.7 - 10  - 25k
3.8 - 25  - 25k
2   - 50  - 25k
1.8 - 100 - 25k

1.8 - 0   - 5k (16 /18)

0   - 1   - 5k
3.3 - 10  - 5k
1.8 - 25  - 5k
1.1 - 50  - 5k
3.3 - 100 - 5k

3.3 - 0   - 125k (18 /18)

10  - 1   - 125k
3.9 - 10  - 125k
2.2 - 25  - 125k
3.7 - 50  - 125k
3.1 - 100 - 125k

1.8 - 0   - 5k
3.9 - 0   - 25k
3.3 - 0   - 125k


#  x-axis is num_levels
#  y-axis is final reward
#  then plot 3 lines on the same graph, for the data associated with the total_timesteps [5_000, 25_000, 125_000]

#x_levels = [0, 1, 10, 25, 50, 100]  # not scaled 0-100, but x-axis evenly split into 6 sections, 1 for each num_levels, labels
#y_reward = [2.1, 1.7, 3.8, 2, 1.8, 0, 3.3, 1.8, 1.1, 3.3, 10, 3.9, 2.2, 3.7, 3.1, 1.8, 3.9, 3.3]
#timesteps = [5_000, 25_000, 125_000]  # 5k: red, 25k: green, 125k: blue
#  scatterplot with colored boxes where box color represents timesteps
'''