from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma



def get_random_normal_dist_samples(mean, sd, n_simulations):
    return norm.rvs(
                    loc=mean,
                    scale=sd,
                    size=n_simulations
    )


def get_random_uniform_distribution_samples(low, high, sample_size):
    return np.random.uniform(low, high, sample_size)


def plot_gamma_distribution(shape, scale, n):
    Gamma = gamma(a=shape, scale=scale)

    x = np.arange(1, n)
    plt.plot(Gamma.pdf(x), x)
    plt.xlabel("Duration of visit")
    plt.ylabel("Number of visitors")
    plt.show()
