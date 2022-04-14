import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime
from   arch import arch_model
import pandas as pd

# Retreive stock data.
def getStock(stockName):
    start = datetime.datetime(2019, 6, 1)
    end   = datetime.date.today()
    stk  = pdr.get_data_yahoo(stockName,
                              start=datetime.datetime(start.year,
                                    start.month,start.day),
                              end=datetime.datetime(end.year, end.month, end.day))
    return stk

stockJPM  = getStock('JPM')
stockZoom = getStock('ZM')

# Plot daily % returns.
JPMReturns  = 100 * stockJPM.Close.pct_change().dropna()
zoomReturns = 100 * stockZoom.Close.pct_change().dropna()

def gridSearchGarchModel(returns):

    df = pd.DataFrame(columns=['p', 'q', 'aic', 'bic'])

    MAX_LAGS = 10
    for p in range(1, MAX_LAGS):
        for q in range(1, MAX_LAGS):
            model     = arch_model(returns, p=p, q=q)
            model_fit = model.fit()
            df = df.append({'aic':model_fit.aic,
                            'bic': model_fit.bic, 'p':p, 'q':q},
                            ignore_index=True)
    df.sort_values("bic")
    print("ARCH Model Results")
    print(df)

gridSearchGarchModel(JPMReturns)

model        = arch_model(JPMReturns, p=1, q=1)
model_fit    = model.fit()
print(model_fit.summary())
