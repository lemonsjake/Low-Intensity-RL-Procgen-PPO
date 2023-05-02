import matplotlib.pyplot as plt


#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #  Agent Number ??
x = 10  # Number of Agents in Subset (4 subsets of 10 agents each, 40 agents in total set)
y_1 = [8.5, 10, 9.7, 10, 0.4, 1.7, 7.6, 0, 0, 3.1]  #  Agent Final Reward (end_mean_rwd)
y_2 = [5.8, 7.3, 6.7, 3.3, 4.6, 5.8, 5.2, 6.4, 0.7, 5.9]
y_3 = [5, 5.6, 4.2, 6.3, 6, 4.5, 4.6, 6.2, 2.4, 5.9]
y_4 = [3.8, 2, 0.7, 2.7, 1.5, 4, 3.5, 2.9, 2.9, 3.6]

plt.figure()
plt.title("Experimental Agent Set Final Reward")  # Histogram Title

#  Experimental Agents 1-10 (Set 1 of Experimental Set, num_levels=1)
plt.subplot(221)
#plt.plot(y_1, x)
plt.hist(y_1, x, density=True, facecolor='r', alpha=0.75)
plt.xlabel("Agent # (out of 10)")
plt.ylabel("Final Reward")
plt.title("Agents 1-10, num_levels=1")  # Subplot 1 Tile, num_levels=1
plt.axis([1, 10, 0, 10])  # 1-10 on x (agent), 0-10 on y (rwd)
plt.grid(True)

#  Experimental Agents 11-20 (Set 2 of Experimental Set, num_levels=3)
plt.subplot(222)
#plt.plot(y_2, x)
plt.hist(y_2, x, density=False, facecolor='g', alpha=0.75)
plt.xlabel("Agent # (out of 10)")
plt.ylabel("Final Reward")
plt.title("Agents 11-20, num_levels=3")  # Subplot 2 Title, num_levels=3
plt.axis([1, 10, 0, 10])  # 1-10 on x (agent), 0-10 on y (rwd)
plt.grid(True)

#  Experimental Agents 21-30 (Set 3 of Experimental Set, num_levels=5)
plt.subplot(223)
#plt.plot(y_3, x)
plt.hist(y_3, x, density=True, facecolor='b', alpha=0.75)
plt.xlabel("Agent # (out of 10)")
plt.ylabel("Final Reward")
plt.title("Agents 21-30, num_levels=5")  # Subplot 3 Title, num_levels=5
plt.axis([1, 10, 0, 10])  # 1-10 on x (agent), 0-10 on y (rwd)
plt.grid(True)

#  Experimental Agents 31-40 (Set 4 of Experimental Set, num_levels=0)
plt.subplot(224)
#plt.plot(y_4, x)
plt.hist(y_4, x, density=False, facecolor='y', alpha=0.75)
plt.xlabel("Agent # (out of 10)")
plt.ylabel("Final Reward")
plt.title("Agents 31-40, num_levels=0")  # Subplot 4 Title, num_levels=0
plt.axis([1, 10, 0, 10])  # 1-10 on x (agent), 0-10 on y (rwd)
#plt.yscale("linear")
#plt.title("# of Levels = 0, Agents 31-40")  # Subplot 4 Title, num_levels=0
plt.grid(True)

plt.show()


'''
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
'''

'''
# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the open interval (0, 1)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()
'''