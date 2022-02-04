"""Exponential smoothing provides a slightly better fit to the fluctuations in the time series because it places a
higher weight on more recent time steps. Exponential smoothing lags behind the actual data less than the simple
moving average. """

import datetime
import pandas_datareader as pdr
import matplotlib.pyplot as plt


def getStock(stk, ttlDays):
    numDays = int(ttlDays)
    dt = datetime.date.today()
    dtPast = dt + datetime.timedelta(days=-numDays)
    df = pdr.get_data_yahoo(stk,
                            start=datetime.datetime(dtPast.year, dtPast.month,
                                                    dtPast.day),
                            end=datetime.datetime(dt.year, dt.month, dt.day))
    return df


df = getStock('MSFT', 200)

# Calculating the moving averages.
rolling_mean2 = df['Close'].rolling(window=50).mean()

# Calculate the exponentially smoothed series.
exp50 = df['Close'].ewm(span=50, adjust=False).mean()
# alpha values
# higher alpha values assigns more importance to more
# current time lags.
exp20 = df['Close'].ewm(alpha=0.4).mean()


# plt.figure(figsize=(10,30))
df['Close'].plot(label='MSFT Close ', color='gray', alpha=0.3)
rolling_mean2.plot(label='MSFT 50 Day MA', style='--', color='magenta')
exp50.plot(label='MSFT 50 Day ES', style='--', color='blue', alpha=0.5)
plt.legend()
plt.show()
