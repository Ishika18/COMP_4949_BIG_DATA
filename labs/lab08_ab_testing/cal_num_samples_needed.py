from statsmodels.stats.power import TTestIndPower
effect           = 2.36 # Obtained from previous step.
alpha            =  0.05 # Enable 95% confidence for two tail test.
power            =  0.95  # One minus the probability of a type II error.
                         # Limits possibility of type II error to 20%.
analysis         = TTestIndPower()
numSamplesNeeded = analysis.solve_power(effect, power=power, alpha=alpha)
print(numSamplesNeeded)
