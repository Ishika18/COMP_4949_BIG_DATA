"""The next step involves performing the test. This can be done using 23 observations from days when the old table
card is used and with 23 observations from days when the new card is used. It happens that the variance for both
distributions is the same but we will treat the variances as if they are independent so equal_var is set to False. """

from scipy import stats
old_case_count = [10, 11, 6, 18, 11, 9, 13, 9, 3, 12, 3, 13, 14, 4, 12, 8, 18, 17, 15, 18, 6, 1, 13, 9, 11, 15, 11, 7, 12, 14]

new_case_count = [5, 7, 3, 12, 0, 7, 0, 8, 9, 5, 5, 2, 2, 2, 4, 6, 6, 7, 1, 6, 10, 1, 0, 2, 2, 4, 5, 1, 4, 3]

testResult = stats.ttest_ind(new_case_count,
                             old_case_count, equal_var=False)

import numpy as np
print("Hypothesis test p-value: " + str(testResult))
print("New cases mean: " + str(np.mean(new_case_count)))
print("New casess std: " + str(np.std(new_case_count)))
