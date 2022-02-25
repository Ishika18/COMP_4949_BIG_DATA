'''Stop words are words that do not have any importance in search queries. A stop word is a commonly used word (such
as “the”, “a”, “an”, “in”) that a search engine has been programmed to ignore, both when indexing entries for
searching and when retrieving them as the result of a search query. '''
import nltk
from nltk.corpus import stopwords

# To get stop words.
from lessons.lesson06_sentiment_analysis_ngram_modeling.tokenizing import createTokenizedArray, reviewSentence

nltk.download('stopwords')


# -------------------------------------------------------------
# Create array of words with no punctuation or stop words.
# -------------------------------------------------------------
def removeStopWords(tokenList):
    stopWords = set(stopwords.words('english'))
    print("#### STOP WORDS - START ####")
    print(stopWords)
    print("#### STOP WORDS - END####")
    shorterSentences = []  # Declare empty array of sentences.

    for sentence in tokenList:
        shorterSentence = []  # Declare empty array of words in single sentence.
        for word in sentence:
            if word not in stopWords:

                # Remove leading and trailing spaces.
                word = word.strip()

                # Ignore single character words and digits.
                if (len(word) > 1 and word.isdigit() == False):
                    # Add remaining words to list.
                    shorterSentence.append(word)
        shorterSentences.append(shorterSentence)
    return shorterSentences


tokenizedList = createTokenizedArray([reviewSentence])

#  pass in list of lists
sentenceArrays = removeStopWords(tokenizedList)
print(sentenceArrays)
