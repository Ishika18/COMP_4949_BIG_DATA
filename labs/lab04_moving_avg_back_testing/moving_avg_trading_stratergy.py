"""A common stock trading strategy involves using moving averages to predict when to buy or sell. When the short term 
moving average cross above the long term moving average buy. When the short term moving average falls below the long 
term moving average sell. """

import datetime
import pandas_datareader  as pdr
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

df = getStock('AMD', 1100)
print(df)

rolling_mean  = df['Close'].rolling(window=20).mean()
rolling_mean2 = df['Close'].rolling(window=50).mean()

#plt.figure(figsize=(10,30))
df['Close'].plot(label='AMD Close ', color='gray', alpha=0.3)
rolling_mean.plot(label='AMD 20 Day SMA', style='--', color='orange')
rolling_mean2.plot(label='AMD 50 Day SMA', style='--',color='magenta')

plt.legend()
plt.show()
