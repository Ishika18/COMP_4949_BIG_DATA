# ADF test is used to determine if a series is stationary
# Ho: The time series is non-stationary (null hypothesis)
# H1: The time series is stationary (alternate hypothesis)
# If p-value < 0.05 then reject null hypo. and differencing
# is not needed

import numpy as np, pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.figsize':(9,7), 'figure.dpi':120})

# Import data
df = pd.read_csv(
"https://raw.githubusercontent.com/selva86/datasets/master/wwwusage.csv", \
                  names=['value'], header=0)
print(df)
df.value.plot()
plt.title("www usage")
plt.show()


# 2nd order differencing

# Perform differencing.
df = df.diff()

# Plot data after differencing.
plt.plot(df)
plt.xticks(rotation=75)
plt.show()

from statsmodels.tsa.stattools import adfuller
result = adfuller(df.value.dropna())
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])