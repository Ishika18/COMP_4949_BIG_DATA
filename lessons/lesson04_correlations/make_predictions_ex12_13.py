from pandas import read_csv
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
from math import sqrt

# Load the data.
from global_constants import PATH

series = read_csv(PATH + 'daily-min-temperatures.csv',
                  header=0, index_col=0, parse_dates=True, squeeze=True)

# Plot ACF.
from statsmodels.graphics.tsaplots import plot_acf

plot_acf(series, lags=20)
plt.show()

# Plot PACF.
from statsmodels.graphics.tsaplots import plot_pacf

plot_pacf(series, lags=7)
plt.show()

NUM_TEST_DAYS = 7

# Split dataset into test and train.
X = series.values
lenData = len(X)
train = X[0:lenData - NUM_TEST_DAYS]
test = X[lenData - NUM_TEST_DAYS:]

# Train.
model = AutoReg(train, lags=7)
model_fit = model.fit()
print('Coefficients: %s' % model_fit.params)

print(model_fit.summary())

# Make predictions.
predictions = model_fit.predict(start=len(train),
                                end=len(train) + len(test) - 1,
                                dynamic=False)

for i in range(len(predictions)):
    print('predicted=%f, expected=%f' % (predictions[i], test[i]))
rmse = sqrt(mean_squared_error(test, predictions))
print('Test RMSE: %.3f' % rmse)

# Plot results.
plt.plot(test, marker='o', label='actual')
plt.plot(predictions, color='brown', linewidth=4,
         marker='o', label='predicted')

plt.legend()
plt.show()


# Use model coefficients from autoregression to make a prediction.
def makePrediction(t_1, t_2, t_3, t_4, t_5, t_6, t_7):
    intercept = 1.11532391
    t1Coeff = 0.62630048
    t2Coeff = -0.07514724
    t3Coeff = 0.07405114
    t4Coeff = 0.06167809
    t5Coeff = 0.06602607
    t6Coeff = 0.04416757
    t7Coeff = 0.10296008

    prediction = intercept + t1Coeff * t_1 \
                 + t2Coeff * t_2 \
                 + t3Coeff * t_3 \
                 + t4Coeff * t_4 \
                 + t5Coeff * t_5 \
                 + t6Coeff * t_6 \
                 + t7Coeff * t_7

    return prediction


testLen = len(test)

t_1 = test[testLen - 1]
t_2 = test[testLen - 2]
t_3 = test[testLen - 3]
t_4 = test[testLen - 4]
t_5 = test[testLen - 5]
t_6 = test[testLen - 6]
t_7 = test[testLen - 7]

futurePredictions = []
for i in range(0, NUM_TEST_DAYS):
    prediction = makePrediction(
        t_1, t_2, t_3, t_4, t_5, t_6, t_7
    )
    futurePredictions.append(prediction)
    t_7 = t_6
    t_6 = t_5
    t_5 = t_4
    t_4 = t_3
    t_3 = t_2
    t_2 = t_1
    t_1 = prediction

print("Here is a one week temperature forecast: ")
print(futurePredictions)
