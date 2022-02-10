# transform undifferenced data set into differenced data set

import pandas as pd
import datetime

import matplotlib.pyplot as plt
from global_constants import PATH
FILE = 'shampoo.csv'
df   = pd.read_csv(PATH + FILE, index_col=0)
df.info()

# Plot data before differencing.
df.plot()
plt.xticks(rotation=45)
plt.show()

# Perform differencing.
df = df.diff()

# Plot data after differencing.
plt.plot(df)
plt.xticks(rotation=75)
plt.show()
