from nltk.stem import PorterStemmer


# -------------------------------------------------------------
# Removes suffixes and rebuids the sentences.
# -------------------------------------------------------------
from lessons.lesson06_sentiment_analysis_ngram_modeling.stop_words import removeStopWords
from lessons.lesson06_sentiment_analysis_ngram_modeling.tokenizing import createTokenizedArray, reviewSentence

sentence1 = "Despite its fresh perspective, Banks's Charlie's Angels update " \
            + "fails to capture the energy or style that made it the beloved phenomenon it is."

sentence2 = "This 2019 Charlie's Angels is stupefyingly entertaining and " \
            + "hilarious. It is a stylish alternative to the current destructive blockbusters."

sentences = [sentence1, sentence2]

def stemWords(sentenceArrays):
    ps = PorterStemmer()
    stemmedSentences = []
    for sentenceArray in sentenceArrays:
        stemmedArray = []  # Declare empty array of words.
        for word in sentenceArray:
            stemmedArray.append(ps.stem(word))  # Add stemmed word.

        # Convert array back to sentence of stemmed words.
        delimeter = ' '
        sentence = delimeter.join(stemmedArray)

        # Append stemmed sentence to list of sentences.
        stemmedSentences.append(sentence)
    return stemmedSentences

if __name__ == '__main__':
    tokenizedList = createTokenizedArray(sentences)
    sentenceArrays = removeStopWords(tokenizedList)
    stemmedSentences = stemWords(sentenceArrays)
    print(stemmedSentences)
