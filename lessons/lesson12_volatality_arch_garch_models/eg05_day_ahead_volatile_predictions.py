from arch import arch_model
import matplotlib.pyplot as plt
from eg01_visualize_volatality import JPMReturns

TEST_DAYS = 170
JPM_LAGS  = 5
import numpy as np

def generatePredictions(returns, numLags):
    dayAheadPredictions = []
    for i in range(TEST_DAYS):
        train = returns[:-(TEST_DAYS - i)]

        # This code is just proofing out the fact that the forecast is for
        # 1 day ahead. The sample output generated is:
        # Most recent date in training data: 2020-10-26 00:00:00
        # Prediction is for date: 2020-10-27 00:00:00
        lastTrainingDate = returns.index[len(train) - 1]
        print("\nMost recent date in training data: " + str(lastTrainingDate))
        print("Prediction is for date: " + str(returns.index[len(train)]))

        # Fit the model, make the day-ahead prediction, add prediction to the list.
        model     = arch_model(train, p=numLags, q=0)
        model_fit = model.fit(disp='off')
        pred      = model_fit.forecast(horizon=1)  # Predict 1 day ahead
        dayAheadPredictions.append(pred.variance.values[-1, :][0])
    return dayAheadPredictions
jpmDayAheadPredictions  = generatePredictions(JPMReturns, JPM_LAGS)

def plotPredictedVolatility(returns, dayAheadPredictions, stockName):
    actualRecentData = returns[len(returns) - TEST_DAYS:]

    plt.plot(actualRecentData.index, actualRecentData, marker="o",
             label="Actual % Price Change")
    plt.plot(actualRecentData.index, dayAheadPredictions, marker="o",
             label="Predicted % Deviation")
    plt.axhline(y=0, color='gray', alpha=0.3)
    plt.legend()
    plt.xticks(rotation=60)
    plt.title("Predicted Daily σ (sigma) for " + stockName)
    plt.show()

plotPredictedVolatility(JPMReturns, np.sqrt(jpmDayAheadPredictions), "JPM")
