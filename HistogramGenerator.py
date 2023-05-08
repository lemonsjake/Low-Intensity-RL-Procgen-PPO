import matplotlib.pyplot as plt

x_1 = [8.5, 10, 9.7, 10, 0.4, 1.7, 7.6, 0, 0, 3.1]  #  Subset 1 Experimental Agents 1-10 Final Rewards (end_mean_rwd)
x_2 = [5.8, 7.3, 6.7, 3.3, 4.6, 5.8, 5.2, 6.4, 0.7, 5.9]  #  Subset 2 Experimental Agents 11-20 Final Rewards (end_mean_rwd)
x_3 = [5, 5.6, 4.2, 6.3, 6, 4.5, 4.6, 6.2, 2.4, 5.9]  #  Subset 3 Experimental Agents 21-30 Final Rewards (end_mean_rwd)
x_4 = [3.8, 2, 0.7, 2.7, 1.5, 4, 3.5, 2.9, 2.9, 3.6]  #  Subset 4 Experimental Agents 31-40 Final Rewards (end_mean_rwd)

plt.figure()
plt.suptitle("Experimental Agent Set Final Reward")  # Histogram Title
plt.subplots_adjust(wspace=0.3, hspace=0.5)  #left=0.2, bottom=0.2, right=0.8, top=0.8

plt.subplot(221)  # creates top left subplot -- subset 1, num_levels=1
plt.hist(x_1, bins="auto", facecolor='r', alpha=0.75)  # creates historgram as subplot
plt.xlabel("Final Reward")  # x-axis subplot label
plt.ylabel("# of Agents")  # y-axis subplot label
plt.title("Subset 1, num_levels=1")  # Subplot Title
plt.axis([0, 10, 0, 5])  # makes x-axis range [0-10], y-axis range [0-5]
plt.grid(True)  # shows gridlines on subplot

plt.subplot(222)  # creates top right subplot -- subset 2, num_levels=3
plt.hist(x_2, bins="auto", facecolor='g', alpha=0.75)
plt.xlabel("Final Reward")
plt.ylabel("# of Agents")
plt.title("Subset 2, num_levels=3")
plt.axis([0, 10, 0, 5])
plt.grid(True)

plt.subplot(223)  # creates bottom left subplot --  subset 3, num_levels=5
plt.hist(x_3, bins="auto", facecolor='b', alpha=0.75)
plt.xlabel("Final Reward")
plt.ylabel("# of Agents")
plt.axis([0, 10, 0, 5])
plt.title("Subset 3, num_levels=5")
plt.grid(True)

plt.subplot(224)  # creates bottom right subplot --  subset 4, num_levels=0
plt.hist(x_4, bins="auto", facecolor='y', alpha=0.75)
plt.xlabel("Final Reward")
plt.ylabel("# of Agents")
plt.title("Subset 4, num_levels=0")
plt.axis([0, 10, 0, 5])
plt.grid(True)

plt.show()

#  plt.hist(rewards, bins="auto")
#  final reward as the x-axis
#  y-axis shows how many runs achieved a final reward in that bin