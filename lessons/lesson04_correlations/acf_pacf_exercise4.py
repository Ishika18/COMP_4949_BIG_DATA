import numpy as np

import matplotlib.pyplot as plt
import statsmodels.api as sm

dta = sm.datasets.sunspots.load_pandas().data
print(dta)
plt.plot(dta['YEAR'], dta['SUNACTIVITY'])
plt.show()

# Show autocorrelation function.
# General correlation of lags with past lags.
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(dta['SUNACTIVITY'], lags=50)
plt.show()

# Show partial-autocorrelation function.
# Shows correlation of 1st lag with past lags.
from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(dta['SUNACTIVITY'], lags=50)
plt.show()

print(dta)

# Create back-shifted columns for an attribute.
def addBackShiftedColumns(df, colName, timeLags):
    for i in range(1, timeLags + 1):
        newColName = colName + "_t-" + str(i)
        df[newColName] = df[colName].shift(i)
    return df

# Build dataframe for modelling.
columns = ['SUNACTIVITY']
modelDf = dta.copy()
NUM_TIME_STEPS = 50
for i in range(0, len(columns)):
    modelDf = addBackShiftedColumns(modelDf, columns[i], NUM_TIME_STEPS)

modelDf = modelDf.dropna()
y = modelDf[['SUNACTIVITY']]
X = modelDf[['SUNACTIVITY_t-1']]

# Add intercept for OLS regression.
X = sm.add_constant(X)
TEST_DAYS = 10

# Split into test and train sets. The test data includes
# the latest values in the data.
lenData = len(X)
X_train = X[0:lenData - TEST_DAYS]
y_train = y[0:lenData - TEST_DAYS]
X_test = X[lenData - TEST_DAYS:]
y_test = y[lenData - TEST_DAYS:]



# Model and make predictions.
model = sm.OLS(y_train, X_train).fit()
print(model.summary())
predictions = model.predict(X_test)

# Show RMSE.
from sklearn import metrics

print('Root Mean Squared Error:',
      np.sqrt(metrics.mean_squared_error(y_test, predictions)))

# Plot the data.
xaxisValues = list(y_test.index)
plt.plot(xaxisValues, y_test, label='Actual', marker='o')
plt.plot(xaxisValues, predictions, label='Predicted', marker='o')
plt.xticks(rotation=45)
plt.legend(loc='best')
plt.title("Sunspot activity")
plt.show()
