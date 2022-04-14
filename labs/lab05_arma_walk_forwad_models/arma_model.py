import statsmodels.api as sm
import statsmodels.tsa.arima.model as sma
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np


def getData():
    df = sm.datasets.sunspots.load_pandas().data[['SUNACTIVITY']]
    df.index = pd.date_range(start='1700', end='2009', freq='A')
    TEST_SZ = 5
    train = df[0:len(df) - TEST_SZ]
    test = df[len(df) - TEST_SZ:]
    return train, test


def buildModel(df, ar, i, ma):
    model = sma.ARIMA(df['SUNACTIVITY'], order=(ar, i, ma)).fit()

    return model


def predictAndEvaluate(model, test, title):
    print("\n***" + title)
    print(model.summary())
    predictions = model.predict(start='2010', end='2014')
    mse = mean_squared_error(predictions, test)
    rmse = np.sqrt(mse)
    print("RMSE: " + str(rmse))


train, test = getData()

for ar in range(0, 5):
    for ma in range(0, 5):
        model = buildModel(train, ar, 0, ma)
        title = str(ar) + "_0_" + str(ma)
        predictAndEvaluate(model, test, title)


"""
How to interpret p, d, q values
The first leading model candidate is ARIMA(0,1,2). 
The parameters for the first model candidate are p=0, d=1 and q=2.
In other words, p=0 implies there is no (AR) autoregressive component. 
The parameter d=1 implies first order differencing is required.
 q=2 implies that two lags of the (MA) moving average which are used. 
"""