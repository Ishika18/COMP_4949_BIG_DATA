import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.linear_model import LinearRegression
from sklearn.impute import IterativeImputer
from global_constants import PATH

df = pd.read_csv(f'{PATH}babysamp-98.txt', sep='\t')

# Show all columns.
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df.describe())

numericColumns = ['MomAge','DadAge','MomEduc',
                  'MomMarital','numlive','dobmm','gestation',
                   'weight','prenatalstart']

# only obtain numerical columns
df = df[numericColumns]
print(df.tail(20))


# Define regressor.
lr = LinearRegression()
imputer = IterativeImputer(estimator=lr, verbose=2, max_iter=20)

# Transform the data.
imputedDataMatrix = imputer.fit_transform(df)

# Convert imputed matrix back to dataframe.
dfAdjusted = pd.DataFrame(imputedDataMatrix, columns=df.columns)
print(dfAdjusted.tail(20))
