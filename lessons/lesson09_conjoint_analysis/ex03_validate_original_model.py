import pandas as pd
import statsmodels.api as sm

from lessons.lesson09_conjoint_analysis.eg01_predict_user_ranking import get_lr_model
from global_constants import PATH

# read in conjoint survey profiles with respondent ranks
df = pd.read_csv(PATH + 'bike_conjoint_train.csv')

# Show all columns of data frame.
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df)

# This peforms a weighted regression for ranking with string variables as
# levels.
# Column names are set so their letter case matches part of level name.
attributeNames = ['gear', 'bike', 'Suspension', 'guards']

X, y, lr_model = get_lr_model(attributeNames, 'Rank', df)
print(lr_model.summary())

df_test = pd.read_csv(PATH + 'bike_conjoint_test.csv')
X_test = pd.get_dummies(df_test, columns=attributeNames)
X_test = X_test.drop(['Rank'], axis=1)

# add_constant() doesn't work if there is already a column with variance=0
# added 'has_constant' attribute as a result.
X_test = sm.add_constant(X_test, has_constant='add')

# Must add in this column since it does not exist in the data set.
# The model expects this column.
X_test['guards_Mudguards'] = 0

predictions = lr_model.predict(X_test.values)
print(df_test['Rank'].values)
print(predictions)

