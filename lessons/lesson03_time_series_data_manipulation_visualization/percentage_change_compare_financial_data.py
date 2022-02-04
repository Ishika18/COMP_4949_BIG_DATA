import pandas_datareader  as pdr
import datetime
import pandas             as pd
import matplotlib.pyplot  as plt
import matplotlib.dates   as mdates

# Show all columns.
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

def getStock(stk, ttlDays):
    numDays = int(ttlDays)
    dt      = datetime.date.today()
    dtPast  = dt + datetime.timedelta(days=-numDays)
    df      = pdr.get_data_yahoo(stk,
    start   = datetime.datetime(dtPast.year, dtPast.month, dtPast.day),
    end     = datetime.datetime(dt.year, dt.month, dt.day))
    return df

NUM_DAYS = 30
dfGoogle = getStock('GOOGL', NUM_DAYS)
dfApple  = getStock('AAPL', NUM_DAYS)
dfMicrosoft = getStock('MSFT', NUM_DAYS)

# Get a reference to the subplot.
# Two parameters are needed because subplots() returns
# the figure and axis object together.

# Ax lets us set axis properties.
fig, ax = plt.subplots()

# Plot data with markers at each point.
ax.plot(dfGoogle.index, dfGoogle['Close'].pct_change(), color='pink', label='Google')
ax.plot(dfApple.index, dfApple['Close'].pct_change(), '--', color='orange', label='Apple')
ax.plot(dfMicrosoft.index, dfMicrosoft['Close'].pct_change(), color='blue', label='Microsoft')

plt.setp( ax.xaxis.get_majorticklabels(), rotation=70 )
plt.legend(loc="best")
plt.show()
