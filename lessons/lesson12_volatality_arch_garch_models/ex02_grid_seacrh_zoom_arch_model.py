from arch import arch_model
import pandas as pd
from eg01_visualize_volatality import zoomReturns


def gridSearchArchModel(pRange, returns):
    df = pd.DataFrame(columns=['p', 'aic', 'bic'])

    for p in range(1, pRange):
        model = arch_model(returns, p=p, q=0)
        model_fit = model.fit()
        df = df.append({'aic': model_fit.aic, 'bic': model_fit.bic, 'p': p},
                       ignore_index=True)
    print("ARCH Model Results")
    print(df)


MAX_P = 14
gridSearchArchModel(MAX_P, zoomReturns)
