"""The following code uses location, scale and distribution type values from Example 4 along with the rvs() function
to generate 500 random samples. The approximation is not perfect but this is a decent initial set of data to work
with for a random simulation.
 eg 3 is grid_search_distributions.py
 """

import scipy.stats
NUM_SIMULATIONS = 500

loc   = 20.30555
scale = 9.717675

randomSamples = scipy.stats.genlogistic.rvs(
    c=1, # This is the shape of the array.
    size=NUM_SIMULATIONS, loc=loc, scale=scale)

# Get samples greater than 0.
truncatedSamples = [i for i in randomSamples if i >= 0]

import matplotlib.pyplot as plt
plt.hist(truncatedSamples, bins=80)
plt.title("Randomly generated samples with rvs()")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
