import pandas_datareader as pdr
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Show all columns.
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


def getStock(stk, ttlDays):
    numDays = int(ttlDays)
    dt = datetime.date.today()
    dtPast = dt + datetime.timedelta(days=-numDays)
    df = pdr.get_data_yahoo(stk,
                            start=datetime.datetime(dtPast.year, dtPast.month, dtPast.day),
                            end=datetime.datetime(dt.year, dt.month, dt.day))
    return df


NUM_DAYS = 160
df = getStock('^GSPC', NUM_DAYS)

# Show the S&P point standard deviation and show it on a Monday.
df['Close'].resample('MS', loffset='1D').min().plot(marker='o', label='Monthly min')
df['Close'].resample('MS', loffset='1D').max().plot(marker='o', label='Monthly max')
df['Close'].resample('MS', loffset='1D').mean().plot(marker='o', label='Monthly mean')


plt.title("S&P Closing Points Per Month")
plt.legend(loc='best')
plt.show()
