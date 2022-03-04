# This is not as good as with genlogistic but is a somewhat reasonable alternative approach.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
from scipy.stats import kstest

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Load samples.
import seaborn
dataset = seaborn.load_dataset('titanic')
# Drop the null values.
samples = dataset.age.dropna()

# High p-values are preferred and low D scores (closer to 0)
# are preferred.
def runKolmogorovSmirnovTest(dist, loc, arg,
                             scale, samples):
    d, pvalue = kstest(samples.tolist(),
                       lambda x: dist.cdf(x,
                                          loc=loc, scale=scale, *arg),
                       alternative="two-sided")
    print("D value: " + str(d))
    print("p value: " + str(pvalue))
    dict = {"dist": dist.name, "D value": d, "p value": pvalue,
            "loc":loc, "scale":scale, "arg":arg}
    return dict

def fit_and_plot(dist, samples, df):
    print("\n*** " + dist.name + " ***")

    # Fit the distribution as best as possible
    # to existing data.
    params = dist.fit(samples)
    arg = params[:-2]
    loc = params[-2]
    scale = params[-1]

    # Generate 'x' values between 0 and 80.
    x = np.linspace(0, 80, 80)

    # Run test to see if generated data aligns properly
    # to the sample data.
    distDandP = runKolmogorovSmirnovTest(dist, loc, arg, scale, samples)
    df = df.append(distDandP, ignore_index=True)

    # Plot the test and actual values together.
    _, ax = plt.subplots(1, 1)
    plt.hist(samples, bins=80, range=(0, 80))
    ax2 = ax.twinx()
    ax2.plot(x, dist.pdf(x, loc=loc, scale=scale, *arg),
             '-', color="r", lw=2)
    plt.title(dist.name)
    plt.show()
    return df

distributions = [
    scipy.stats.norm,]

dfDistribution = pd.DataFrame()
# Grid search the continuous distributions.
for i in range(0, len(distributions)):
    dfDistribution = fit_and_plot(distributions[i], samples, dfDistribution)

meanAges = np.mean(samples)
ageSD    = np.std(samples)
minAge   = np.min(samples)
maxAge   = np.max(samples)
totalAges= len(dataset)

dfDistribution = dfDistribution.sort_values(by=['D value'])
print(dfDistribution.T) #
NUM_SIMULATIONS = totalAges

# Generate random samples.
randomNums = scipy.stats.norm.rvs(loc   = meanAges,
                      scale = ageSD,
                      size  = NUM_SIMULATIONS)
plt.xlim([minAge, maxAge])

# Show random samples in a histogram.
plt.hist(randomNums, bins=80)
plt.show()
