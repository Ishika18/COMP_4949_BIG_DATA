def estimate_part_worth(X, lr_model, attributeNames):
    counter = 0
    levelNames = list(X.keys())  # Level names are taken directly from X column names.
    levelNames.pop(0)  # Remove constant for intercept.
    ranges = []
    # Store all part-worth (utility) values in a list.
    # The values are taken directly from the model coefficients.
    utilities = list(lr_model.params)
    utilities.pop(0)  # Removes the intercept value.

    # Iterate through all attributes to create part-worths.
    for attributeName in attributeNames:
        partWorths = []

        # Iterate through all levels.
        for levelName in levelNames:
            # If level name contains the attribute store the part worth.
            if (attributeName in levelName):
                partWorth = utilities[counter]  # Store corresponding model coefficient.
                print(" :", levelName + ": " + str(partWorth))
                partWorths.append(partWorth)
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

    return utilities, importances, levelNames
