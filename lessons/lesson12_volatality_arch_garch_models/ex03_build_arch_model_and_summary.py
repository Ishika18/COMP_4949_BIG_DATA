from eg01_visualize_volatality import zoomReturns
from arch import arch_model

JPM_LAGS = 5
model        = arch_model(zoomReturns, p=JPM_LAGS, q=0)
model_fit    = model.fit()
print(model_fit.summary())
