import pandas as pd
from global_constants import PATH
import matplotlib.pyplot as plt
import pmdarima as pm

FILE_NAME = "Energy_Production.csv"


# Import
data = pd.read_csv(PATH + FILE_NAME, index_col=0)

data.index = pd.to_datetime(data.index)

# Seasonal - fit stepwise auto-ARIMA
smodel = pm.auto_arima(data, start_p=1, start_q=1,
                       test='adf',
                       max_p=3, max_q=3, m=12,
                       start_P=0, seasonal=True,
                       d=None, D=1, trace=True,
                       error_action='ignore',
                       suppress_warnings=True,
                       stepwise=True)

print(smodel.summary())

# Forecast
NUM_TIMESTEPS = 24
fitted, confint = smodel.predict(n_periods=NUM_TIMESTEPS, return_conf_int=True)
index_of_fc = pd.date_range(data.index[-1], periods=NUM_TIMESTEPS, freq='MS')

# make series for plotting purpose
fitted_series = pd.Series(fitted, index=index_of_fc)
lower_series = pd.Series(confint[:, 0], index=index_of_fc)
upper_series = pd.Series(confint[:, 1], index=index_of_fc)

# Plot
plt.plot(data)
plt.plot(fitted_series, color='darkgreen')
plt.fill_between(lower_series.index,
                 lower_series,
                 upper_series,
                 color='k', alpha=.15)

plt.title("SARIMA - Energy Production")
plt.show()
