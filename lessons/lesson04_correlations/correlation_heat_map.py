import matplotlib.pyplot as plt
import pandas as pd
import datetime
import seaborn as sns
import pandas_datareader as pdr

# Show all columns.
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Do not show warning.
pd.options.mode.chained_assignment = None  # default='warn'

##################################################################
# CONFIGURATION SECTION
NUM_DAYS = 1200
NUM_TIME_STEPS = 2
TEST_DAYS = 30


##################################################################

def getStock(stk, ttlDays):
    numDays = int(ttlDays)
    dt = datetime.date.today()
    dtPast = dt + datetime.timedelta(days=-numDays)
    df = pdr.get_data_yahoo(stk,
                            start=datetime.datetime(dtPast.year, dtPast.month,
                                                    dtPast.day),
                            end=datetime.datetime(dt.year, dt.month, dt.day))
    return df


# Creates time shifted columns for as many time steps needed.
def backShiftColumns(df, originalColName, numTimeSteps):
    dfNew = df[[originalColName]].pct_change()

    for i in range(1, numTimeSteps + 1):
        newColName = originalColName[0] + 't-' + str(i)
        dfNew[newColName] = dfNew[originalColName].shift(periods=i)
    return dfNew


def prepareStockDf(stockSymbol, columns):
    df = getStock(stockSymbol, NUM_DAYS)

    # Create data frame with back shift columns for all features of interest.
    mergedDf = pd.DataFrame()
    for i in range(0, len(columns)):
        backShiftedDf = backShiftColumns(df, columns[i], NUM_TIME_STEPS)
        if (i == 0):
            mergedDf = backShiftedDf
        else:
            mergedDf = mergedDf.merge(backShiftedDf, left_index=True,
                                      right_index=True)

    newColumns = list(mergedDf.keys())

    # Append stock symbol to column names.
    for i in range(0, len(newColumns)):
        mergedDf.rename(columns={newColumns[i]: stockSymbol + \
                                                "_" + newColumns[i]}, inplace=True)

    return mergedDf


columns = ['Open', 'Close']
msftDf = prepareStockDf('MSFT', columns)
aaplDf = prepareStockDf('AAPL', columns)
mergedDf = msftDf.merge(aaplDf, left_index=True, right_index=True)
mergedDf = mergedDf.dropna()
print(mergedDf)


corr = mergedDf.corr()
plt.figure(figsize=(8, 4))
ax = sns.heatmap(corr[['MSFT_Open']],
                 linewidth=0.5, vmin=-1,
                 vmax=1, cmap="YlGnBu")
plt.show()
