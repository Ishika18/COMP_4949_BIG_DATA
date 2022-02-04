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

NUM_DAYS = 300
df      = getStock('^GSPC', NUM_DAYS)

# Get a reference to the subplot.
# Two parameters are needed because subplots() returns
# the figure and axis object together.

# Ax lets us set axis properties.
fig, ax = plt.subplots()

# Plot data with markers at each point.
ax.plot(df.index, df['Close'], marker='*', linestyle='-')

# Set vertical major grid.
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=1, interval=4))
ax.xaxis.grid(True, which='major', linewidth=1, color='pink')

# Set vertical minor grid.
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday=1))
ax.xaxis.grid(True, which='minor', linewidth=1, color='#999999')


# Set vertical major grid.
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1,4,7,10),bymonthday=1))
ax.xaxis.grid(True, which = 'major', linewidth = 1, color = '#ff0000')

# Set vertical minor grid.
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday=1))
ax.xaxis.grid(True, which = 'minor', linewidth = 1, color = '#999999')

# Rotate x-ticks.
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, color='red')
plt.title("S&P 500")
plt.xlabel("Date")
plt.show()
