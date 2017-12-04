from agent import agent
import pylab as plt

run = agent(30)

plt.plot(run.data.T)
plt.xlabel('T')
plt.ylabel('Reward')
plt.show()