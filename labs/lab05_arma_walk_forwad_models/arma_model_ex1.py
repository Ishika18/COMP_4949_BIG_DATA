import numpy as np
import matplotlib.pyplot as plt
import statsmodels.tsa.arima.model as sma


import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
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


def buildModel(df, ar, i, ma):
    model = sma.ARIMA(df['Open'], order=(ar, i, ma)).fit()
    return model


def predictAndEvaluate(model, test, title):
    print("\n***" + title)
    print(model.summary())
    start = len(dfTrain)
    end = start + len(dfTest) - 1
    predictions = model.predict(start=start, end=end, dynamic=True)
    # plotActualVsPredicted(test, predictions)
    plt.plot(test, label='Actual', marker='o', color='blue')
    plt.plot(predictions, label='Predictions', marker='o', color='orange')
    plt.legend()
    plt.title("AR Model")
    plt.show()

    mse = mean_squared_error(predictions, test)
    rmse = np.sqrt(mse)
    print("RMSE: " + str(rmse))


def plotActualVsPredicted(true_value, predicted_value):
    plt.figure(figsize=(10, 10))
    plt.scatter(true_value, predicted_value, c='crimson')
    plt.yscale('log')
    plt.xscale('log')

    p1 = max(max(predicted_value), max(true_value))
    p2 = min(min(predicted_value), min(true_value))
    plt.plot([p1, p2], [p1, p2], 'b-')
    plt.xlabel('True Values', fontsize=15)
    plt.ylabel('Predictions', fontsize=15)
    plt.axis('equal')
    plt.show()

for ar in range(0, 5):
    for ma in range(0, 5):
        model = buildModel(dfTrain, ar, 0, ma)
        title = str(ar) + "_0_" + str(ma)
        predictAndEvaluate(model, dfTest["Open"], title)