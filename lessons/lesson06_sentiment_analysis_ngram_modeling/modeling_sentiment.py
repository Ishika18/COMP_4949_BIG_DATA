from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from global_constants import  PATH

import pandas as pd
import math


# -------------------------------------------------------------
# Build model and predict scores.
#
# Parameters:
# X         - X contains the stemmed and vectorized sentences.
# target    - The target is the known rating (0 to 4).

# Returns X_test, y_test, and y_predicted values.
# -------------------------------------------------------------
from lessons.lesson06_sentiment_analysis_ngram_modeling.stemming import stemWords
from lessons.lesson06_sentiment_analysis_ngram_modeling.stop_words import removeStopWords
from lessons.lesson06_sentiment_analysis_ngram_modeling.tokenizing import createTokenizedArray
from lessons.lesson06_sentiment_analysis_ngram_modeling.vectorize_and_n_grams import vectorizeList


def modelAndPredict(X, target):
    # Create training set with 75% of data and test set with 25% of data.
    X_train, X_test, y_train, y_test = train_test_split(
        X, target, train_size=0.75
    )

    # Build the model with the training data.
    model = LogisticRegression().fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print("\n\n*** The accuracy score is: " + str(score))

    # Predict target values.
    y_prediction = model.predict(X_test)

    # Show faster way to calculate deviation between actual and predicted values.
    rmse2 = math.sqrt(metrics.mean_squared_error(y_test, y_prediction))
    print("The automated root mean square error calculation is: " + str(rmse2))

    # Your Python functions can return multiple values.
    return X_test, y_test, y_prediction


# Read in the file.

CLEAN_DATA = "cleanedMovieReviews.tsv"
df = pd.read_csv(PATH + CLEAN_DATA, skiprows=1, encoding="ISO-8859-1",
                 sep='\t', names=('PhraseId', 'SentenceId', 'Phrase', 'Sentiment'))

# Prepare the data.
df['PhraseAdjusted'] = createTokenizedArray(df['Phrase'])
df['PhraseAdjusted'] = removeStopWords(df['PhraseAdjusted'])
df['PhraseAdjusted'] = stemWords(df['PhraseAdjusted'])
vectorizedList = vectorizeList(df['PhraseAdjusted'])

# Get predictions and scoring data.
# Target is the rating that we want to predict.
X_test, y_test, y_predicted = modelAndPredict(vectorizedList, df['Sentiment'])
