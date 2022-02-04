import numpy as np, pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
import datetime
import pandas_datareader as pdr

def getStock(stk, ttlDays):
    numDays = int(ttlDays)
    dt      = datetime.date.today()
    dtPast  = dt + datetime.timedelta(days=-numDays)
    df      = pdr.get_data_yahoo(stk,
    start   = datetime.datetime(dtPast.year, dtPast.month, dtPast.day),
    end     = datetime.datetime(dt.year, dt.month, dt.day))
    return df

NUM_DAYS = 70
df = getStock('MSFT', NUM_DAYS)
print(df)

# Plot ACF for stock.
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(df['Open'])
plot_pacf(df['Open'])
plt.show()
