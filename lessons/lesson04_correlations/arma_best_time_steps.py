import warnings
import statsmodels.api as sm


def find_best_time_steps_arma(df, max_ar=10, max_ma=0, ic='bic'):
    print("\n*** Comparing AR Model Time Steps")
    warnings.filterwarnings("ignore")
    res = sm.tsa.arma_order_select_ic(df, max_ar=max_ar, max_ma=max_ma, ic=ic)
    print(res.values())
    return res.values()
