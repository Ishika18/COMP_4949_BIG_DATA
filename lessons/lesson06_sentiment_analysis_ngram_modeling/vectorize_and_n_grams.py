'''Vectorization transforms words to numbers so they can be used in different predictive machine learning algorithms.
Vectorization is used to create a master number vector that represents unique words for all documents. Then,
for each document (sentence in our case), the number of occurrences of each word are recorded with a copy of the
master number vector. Remember, you do not need to memorize the code but you will be asked to explain how it works. '''
from   sklearn.feature_extraction.text import CountVectorizer



#-------------------------------------------------------------
# Creates a matrix of word vectors.
#-------------------------------------------------------------
def vectorizeList(stemmedList):
    #cv  = CountVectorizer(binary=True, ngram_range=(1, 4))
    cv = CountVectorizer(binary=True)

    cv.fit(stemmedList)
    X   = cv.transform(stemmedList)
    print("\nNumber vector size: " + str(X.shape))
    return X

sampleSentences = ['the sky is blue', 'the day is bright']
sampleOutput = vectorizeList(sampleSentences)

# Assigns numbers to words.
print("\nTransformed words: \n" + str(sampleOutput))

# Shows number of times each word appears in the list.
print("Encoded list: \n" + str(sampleOutput.toarray()))

print("### VECTORIZE ####")
stemmedSentences = [
    'despit fresh perspect bank charli angel updat fail captur energi'
    ' style made belov phenomenon',
    'charli angel stupefyingli entertain hilari stylish '
    'altern current destruct blockbust'
]
# Vectorize Charlie's Angel's content.
vectorizedSentences = vectorizeList(stemmedSentences)

# Shows number of times each word appears in the list.
print("Encoded list: \n" + str(vectorizedSentences.toarray()))
