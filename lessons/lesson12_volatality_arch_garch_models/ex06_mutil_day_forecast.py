import pandas as pd
from arch import arch_model
import matplotlib.pyplot as plt
from eg01_visualize_volatality import JPMReturns, zoomReturns
import datetime


TEST_DAYS = 170
JPM_LAGS  = 5
import numpy as np

def multiDayForecast(returns, pLags, color, stockName):
    train     = returns
    model     = arch_model(train, p=pLags, q=0)
    model_fit = model.fit(disp='off')

    NUM_DAYS_AHEAD = 7
    pred = model_fit.forecast(horizon=NUM_DAYS_AHEAD)
    future_dates = [returns.index[-1] + datetime.timedelta(days=i) for i in range(1,NUM_DAYS_AHEAD + 1)]
    pred = pd.Series(pred.variance.values[-1,:], index=future_dates)
    plt.plot([1,2,3,4,5,6,7], np.sqrt(pred),color=color,marker='o', label=stockName)

plt.figure(figsize=(10,4))
multiDayForecast(JPMReturns, JPM_LAGS, 'blue', 'JP Morgan')
ZOOM_LAGS = 1
multiDayForecast(zoomReturns, ZOOM_LAGS, 'red', 'Zoom')
plt.title('Volatility Prediction - Next 7 Days', fontsize=20)
plt.axhline(y=0, color='gray', alpha=0.3)
plt.legend(loc='best')
plt.show()
