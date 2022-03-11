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
attributeNames = [ 'Collision', 'Deductable', 'Roadside', 'Extra']

y = df[['Rank']]
X = df[attributeNames]
X = pd.get_dummies(X, columns =attributeNames )
X = sm.add_constant(X)
print(X)

def shortenColumnNames(X):
    XCopy = X.copy()
    for colName in X.keys():
        pos = colName.find('_')
        if(pos>0):
            X = X.rename(columns={colName: colName[pos+1:]})
    return X

X = shortenColumnNames(X)
print(X)

counter         = 0
NUM_QUESTIONS   = 9
start           = 0
end             = NUM_QUESTIONS

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
    '1mill_Collision',  '2mill_Collision', '5mill_Collision',
    'no_Extra',  'yes_Extra',  'no_Roadside',  'yes_Roadside'])

while(end<=len(df)):
    subDf = df.iloc[start:end, :]
    subDf = df.iloc[start:start+1, :]
    subX  = X[start:end][:]
    subY  = y[start:end][:]

    lr_model = sm.OLS(subY, subX).fit()
    print("***params")
    print(lr_model.params)
    dict = getPreferences(attributeNames, lr_model.params, X.keys())

    # Add demographic data to dictionary.
    dict['Age']                 = subDf.iloc[0]['Age']
    dict['KidsAtHomeWhoDrive']  = subDf.iloc[0]['KidsAtHomeWhoDrive']
    dict['Income']              = subDf.iloc[0]['Income']
    dict['VehicleYear']         = subDf.iloc[0]['VehicleYear']

    df2 = df2.append(dict, ignore_index=True)

    # Advance through dataframe.
    start += NUM_QUESTIONS
    end   += NUM_QUESTIONS

print(df2)
