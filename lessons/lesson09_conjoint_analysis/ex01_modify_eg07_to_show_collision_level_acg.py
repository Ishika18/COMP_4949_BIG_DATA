import pandas as pd
import statsmodels.api as sm

from global_constants import PATH

# read in conjoint survey profiles with respondent ranks
df = pd.read_csv(PATH + 'insuranceMarketing.csv')

# Show all columns of data frame.
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df)

# This performs a weighted regression for ranking with string variables as
# levels.
attributeNames = ['Collision', 'Deductable', 'Roadside', 'Extra']

y = df[['Rank']]
X = df[attributeNames]
X = pd.get_dummies(X, columns=attributeNames)
X = sm.add_constant(X)
print(X)


def shortenColumnNames(X):
    XCopy = X.copy()
    for colName in X.keys():
        pos = colName.find('_')
        if (pos > 0):
            X = X.rename(columns={colName: colName[pos + 1:]})
    return X


X = shortenColumnNames(X)
print(X)

counter = 0
NUM_QUESTIONS = 9
start = 0
end = NUM_QUESTIONS


def getPreferences(attributeNames, utilities, levelNames):
    utilityDict = {}
    levelNames = list(levelNames)
    counter = 1
    levelNames.pop(0)  # Remove constant for intercept.
    ranges = []

    # Iterate through all attributes to create part-worths.
    for attributeName in attributeNames:
        partWorths = []

        # Iterate through all levels.
        for levelName in levelNames:
            # If level name contains the attribute store the part worth.
            if (attributeName in levelName):
                partWorth = utilities[counter]  # Store corresponding model coeff.
                print(" :", levelName + ": " + str(partWorth))
                partWorths.append(partWorth)
                utilityDict[levelName] = round(partWorth, 4)
                counter += 1

        # Summarize utility range for the attribute.
        partWorthRange = max(partWorths) - min(partWorths)
        ranges.append(partWorthRange)

    # Calculate relative importance scores for each attribute.
    importances = []
    for i in range(0, len(ranges)):
        importance = 100 * ranges[i] / sum(ranges)
        importances.append(importance)
        print(attributeNames[i] + " importance: " + str(importance))
        utilityDict[attributeNames[i]] = round(importance, 4)

    # Return dictionary containing level preferences
    # and attribute importance.
    return utilityDict


import pandas as pd

df2 = pd.DataFrame(columns=[
    # Demographic
    'Age', 'Income', 'KidsAtHomeWhoDrive', 'VehicleYear',
    # Attribute importance
    'Roadside', 'Deductable', 'Extra', 'Collision',
    # Levels
    '300_Deductable', '500_Deductable', '1000_Deductable',
    '1mill_Collision', '2mill_Collision', '5mill_Collision',
    'no_Extra', 'yes_Extra', 'no_Roadside', 'yes_Roadside'])

while (end <= len(df)):
    subDf = df.iloc[start:end, :]
    subDf = df.iloc[start:start + 1, :]
    subX = X[start:end][:]
    subY = y[start:end][:]

    lr_model = sm.OLS(subY, subX).fit()
    print("***params")
    print(lr_model.params)
    dict = getPreferences(attributeNames, lr_model.params, X.keys())

    # Add demographic data to dictionary.
    dict['Age'] = subDf.iloc[0]['Age']
    dict['KidsAtHomeWhoDrive'] = subDf.iloc[0]['KidsAtHomeWhoDrive']
    dict['Income'] = subDf.iloc[0]['Income']
    dict['VehicleYear'] = subDf.iloc[0]['VehicleYear']

    df2 = df2.append(dict, ignore_index=True)

    # Advance through dataframe.
    start += NUM_QUESTIONS
    end += NUM_QUESTIONS

#### FACTOR ANALYSIS ####

factorColumns = [
    # Demographic
    'Age', 'Income', 'KidsAtHomeWhoDrive', 'VehicleYear',

    # Levels
    '300_Deductable', '500_Deductable', '1000_Deductable',
    '1mill_Collision', '2mill_Collision', '5mill_Collision',
    'no_Extra', 'yes_Extra', 'no_Roadside', 'yes_Roadside']

df3 = df2[factorColumns]

# Bartlett's test of sphericity checks for enough correlation.
# A small p-value indicates that enough correlation exists.
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity

chi_square_value, p_value = calculate_bartlett_sphericity(df3.astype(float))

print("\nBartlett's test chi-square value: ")
print(chi_square_value)

print("\nBartlett's test p-value: ")
print(p_value)

# Kaiser-Meyer-Olkin (KMO) test checks for common variance.
# Factor analysis is suitable for scores of 0.6 (and
# sometimes 0.5) and above.
from factor_analyzer.factor_analyzer import calculate_kmo

kmo_all, kmo_model = calculate_kmo(df3)
print("\nKaiser-Meyer-Olkin (KMO) Test")
print(kmo_model)

# Create components loading vectors without rotation
# and obtain the Eigenvalues.
# pip install factor-analyzer
from factor_analyzer import FactorAnalyzer

fa = FactorAnalyzer(rotation=None)
fa.fit(df3)

ev, v = fa.get_eigenvalues()
print("\nEignenvalues:")
print(ev)

# Pick factors where eigenvalues are greater than 1.
fa = FactorAnalyzer(rotation="varimax", n_factors=4)
fa.fit(df3)

# Create formatted factor loading matrix.
dfFactors = pd.DataFrame(fa.loadings_)
dfFactors['Categories'] = list(df3.keys())

dfFactors = dfFactors.rename(columns={0: 'Factor 1',
                                      1: 'Factor 2', 2: 'Factor 3', 3: 'Factor 4'})
print("\nFactors: ")
print(dfFactors)

#### SUMMARY QUERIES ####
import pandas as pd
from sqlalchemy import create_engine


# Placed query in this function to enable code re-usuability.
def showQueryResult(sql, df):
    # This code creates an in-memory table called 'Inventory'.
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Insurance', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult


# Unfortunately column names cannot start with numbers with SQL Alchemy.
df4 = df3.rename({
    '300_Deductable': 'ThreeDeduc', '500_Deductable': 'FiveDeduc',
    '1000_Deductable': 'ThouDeduc', '1mill_Collision': 'OneMillCollision',
    '2mill_Collision': 'TwoMillCollision', '5mill_Collision': 'FiveMillCollision'
}, axis=1)

avgQuery = "SELECT " + \
           " AVG(AGE),AVG(Income),AVG(KidsAtHomeWhoDrive),AVG(VehicleYear),AVG(ThreeDeduc)," + \
           " AVG(FiveDeduc), AVG(ThouDeduc), AVG(OneMillCollision)," \
           " AVG(TwoMillCollision), AVG(FiveMillCollision) FROM Insurance WHERE "

newFilter = " Age>=16 AND Age<25 "
youngFilter = " Age>=25 AND Age<35 "
midFilter = " Age>=35 AND Age<60 "
seniorFilter = " Age>=60 "

# Build a UNION to generate summaries for four different groups.
unionQuery = avgQuery + newFilter + " UNION " \
             + avgQuery + youngFilter + " UNION " \
             + avgQuery + midFilter + " UNION " \
             + avgQuery + seniorFilter

results = showQueryResult(unionQuery, df4)
print("Full query results")
print(results)
