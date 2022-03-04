import numpy as np
import matplotlib.pyplot as plt
LOW             = 0
HIGH            = 24
SIZE            = 100
NUM_SIMULATIONS = 5

bankrupts = []
plt.subplots(nrows=5, ncols=1,  figsize=(14,7))
for i in range(1,NUM_SIMULATIONS + 1):
    # Randomize data
    x = np.random.uniform(LOW, HIGH, SIZE)
    plt.subplot(2, 3, i)
    plt.hist(x, 24, density=True)
    # there are 2 bankrupt options
    # for sake of convenience
    # 0, 1 represents those
    bankrupts.append(len(np.where(x<2)[0]))
plt.show()

bankrupt_rate = np.mean(bankrupts) / SIZE
print(f"Bankrupt Rate: {bankrupt_rate}")