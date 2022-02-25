import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.tsa.arima.model as sma
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
dta = sm.datasets.sunspots.load_pandas().data

import datetime
import pandas_datareader as pdr

def getStock(stk, ttlDays):
    numDays = int(ttlDays)
    dt = datetime.date.today()
    dtPast = dt + datetime.timedelta(days=-numDays)
    df = pdr.get_data_yahoo(stk,
                            start=datetime.datetime(dtPast.year, dtPast.month,
                                                    dtPast.day),
                            end=datetime.datetime(dt.year, dt.month, dt.day))
    return df


stkName = 'MSFT'
dfStock = getStock(stkName, 400)

# Split the data.
NUM_TEST_DAYS = 5
lenData = len(dfStock)
dfTrain = dfStock.iloc[0:lenData - NUM_TEST_DAYS, :]
dfTest = dfStock.iloc[lenData - NUM_TEST_DAYS:, :]

start = len(dfTrain)
end = start + len(dfTest) - 1

plt.plot(dfStock.index, dfStock['Open'])
plt.show()

def buildModel(df, ar, i, ma):
    model = sma.ARIMA(df['Open'], order=(ar, i, ma)).fit()
    return model

def predictAndEvaluate(model, test, title, ar, ma):
    print("\n***" + title)
    print(model.summary())
    predictions = model.predict(start=start, end=end, dynamic=True)
    mse = mean_squared_error(predictions, test['Open'])
    plotActualVsPredicted(test['Open'], predictions)
    rmse = np.sqrt(mse)
    print("RMSE: " + str(rmse))
    plt.plot(test['Open'].values, label='Actual', marker='o', color='blue')
    plt.plot(predictions.values, label='Predictions', marker='o', color='orange')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plotActualVsPredicted(true_value, predicted_value):
    plt.figure(figsize=(9, 9))
    plt.scatter(true_value, predicted_value, c='green')
    plt.yscale('log')
    plt.xscale('log')

    p1 = max(max(predicted_value), max(true_value))
    p2 = min(min(predicted_value), min(true_value))
    plt.plot([p1, p2], [p1, p2], '*-')
    plt.xlabel('Actual', fontsize=15)
    plt.ylabel('Predicted', fontsize=15)
    plt.title("Model" + str(2) + "_0_" + str(0))
    plt.axis('equal')
    plt.show()



model = buildModel(dfTrain, 4, 0, 1)
title = str(4) + "_0_" + str(1)
predictAndEvaluate(model, dfTest, title, 4, 1)
