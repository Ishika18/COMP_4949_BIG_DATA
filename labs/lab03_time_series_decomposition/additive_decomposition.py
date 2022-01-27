from statsmodels.tsa.seasonal import seasonal_decompose
import pandas                 as pd
import matplotlib.pyplot      as plt
from global_constants import PATH
# Import data.

FILE = "AirPassengers.csv"
df   = pd.read_csv(PATH + FILE,  parse_dates=['date'], index_col='date')
type(df.index)

# Perform decomposition using multiplicative decomposition.
tseries = seasonal_decompose(df['value'], model='additive', extrapolate_trend="freq")

tseries.plot()
plt.show()

# Extract the Components ----
# Actual Values = Product of (Seasonal * Trend * Resid)
dfComponents = pd.concat([tseries.seasonal, tseries.trend,
                          tseries.resid, tseries.observed], axis=1)
dfComponents.columns = ['seas', 'trend', 'resid', 'actual_values']
print(dfComponents.head())

print('"date", "value"')

for i, row in dfComponents.iterrows():
    value = row['seas'] * row['trend'] * row['resid']
    print(f"{i.strftime('%Y-%m-%d')}, {'{:.6f}'.format(value)}")
