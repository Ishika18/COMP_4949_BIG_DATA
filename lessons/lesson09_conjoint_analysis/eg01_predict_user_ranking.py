import pandas as pd
import statsmodels.api as sm

from global_constants import PATH


def get_lr_model(x_features, target, df):
    y = df[[target]]
    X = df[x_features]
    X = pd.get_dummies(X, columns=x_features)
    X = sm.add_constant(X)

    lr_model = sm.OLS(y, X).fit()
    return X, y, lr_model


def main():
    # read in conjoint survey profiles with respondent ranks
    df = pd.read_csv(PATH + 'insuranceMarketing_OnePerson.csv')

    # Show all columns of data frame.
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    # This performs a weighted regression for ranking with string variables as
    # levels.
    x_features = ['Collision', 'Deductible', 'Roadside', 'Extra']
    target = "Rank"
    X, y, lr_model = get_lr_model(x_features, target, df)
    print(lr_model.summary())


if __name__ == '__main__':
    main()