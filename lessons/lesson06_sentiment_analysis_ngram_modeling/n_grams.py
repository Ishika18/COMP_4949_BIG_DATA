from lessons.lesson06_sentiment_analysis_ngram_modeling.stemming import stemWords
from lessons.lesson06_sentiment_analysis_ngram_modeling.stop_words import removeStopWords
from lessons.lesson06_sentiment_analysis_ngram_modeling.tokenizing import createTokenizedArray
from collections import Counter
from nltk.util import ngrams
from global_constants import PATH
import pandas as pd

CLEAN_DATA = "cleanedMovieReviews.tsv"
df = pd.read_csv(PATH + CLEAN_DATA, skiprows=1, encoding="ISO-8859-1",
                 sep='\t', names=('PhraseId', 'SentenceId', 'Phrase', 'Sentiment'))

# Prepare the data.
df['PhraseAdjusted'] = createTokenizedArray(df['Phrase'])
df['PhraseAdjusted'] = removeStopWords(df['PhraseAdjusted'])
df['PhraseAdjusted'] = stemWords(df['PhraseAdjusted'])

def generateWordList(wordDf, scoreStart, scoreEnd, n_gram_size):
    resultDf = wordDf[(wordDf['Sentiment'] >= scoreStart) & \
                      (wordDf['Sentiment'] <= scoreEnd)]

    sentences = [sentence.split() for sentence in resultDf['PhraseAdjusted']]
    wordArray = []
    for i in range(0, len(sentences)):
        wordArray += sentences[i]

    counterList = Counter(ngrams(wordArray, n_gram_size)).most_common(80)

    print("\n***N-Gram")
    for i in range(0, len(counterList)):
        print("Occurrences: ", str(counterList[i][1]), end=" ")
        delimiter = ' '
        print("  N-Gram: ", delimiter.join(counterList[i][0]))

    return counterList


# Create two column matrix.
dfSub = df[['Sentiment', 'PhraseAdjusted']]
SCORE_RANGE_START = 4
SCORE_RANGE_END = 4
SIZE = 1
counterList = generateWordList(dfSub, SCORE_RANGE_START, SCORE_RANGE_END, SIZE)

SIZE = 3
counterList = generateWordList(dfSub, SCORE_RANGE_START, SCORE_RANGE_END, SIZE)

