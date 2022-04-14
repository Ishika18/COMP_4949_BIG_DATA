from statsmodels.graphics.tsaplots import plot_pacf
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime


# Retreive stock data.
def getStock(stockName):
    start = datetime.datetime(2019, 6, 1)
    end   = datetime.date.today()
    stk  = pdr.get_data_yahoo(stockName,
                              start=datetime.datetime(start.year,
                                    start.month,start.day),
                              end=datetime.datetime(end.year, end.month, end.day))
    return stk

stockZoom    = getStock('ZM')

# Plot closing stock prices.
plt.plot(stockZoom.index, stockZoom.Close, label='Zoom', color='red')
plt.title("Stock Closing Prices", fontsize=20)
plt.xticks(rotation=70)
plt.legend()
plt.show()

# Plot daily % returns.
zoomReturns    = 100 * stockZoom.Close.pct_change().dropna()
plt.plot(zoomReturns.index, zoomReturns, label='Zoom', color='red', alpha=0.3)
plt.ylabel('Percent Return')
plt.title('Daily Percent Returns', fontsize=20)
plt.xticks(rotation=70)
plt.legend()
plt.show()


#### PLOT GRAP - AUTOCORRELATION GRAPH ####
plot_pacf(zoomReturns**2, lags=50)
plt.show()
###########################################