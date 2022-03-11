import pandas as pd
import statsmodels.api as sm

from lessons.lesson09_conjoint_analysis.eg01_predict_user_ranking import get_lr_model
from lessons.lesson09_conjoint_analysis.eg02_estimate_part_worths import estimate_part_worth
from lessons.lesson09_conjoint_analysis.eg04_attribute_and_level_visualizations import plot_attr_imp, \
    plot_level_part_worth

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

utilities, importance, levelNames = estimate_part_worth(X, lr_model, attributeNames)
plot_attr_imp(attributeNames, importance)
plot_level_part_worth(levelNames, utilities)