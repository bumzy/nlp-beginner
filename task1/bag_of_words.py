# Feature extraction from text
# Method: bag of words
# https://pythonprogramminglanguage.com

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    'All my cats in a row',
    'When my cat sits down, she looks like a Furby toy!',
    'The cat from outer space',
    'Sunshine loves to sit like this for some reason.'
]

vectorizer = CountVectorizer()
print(vectorizer.fit_transform(corpus).todense())
print(vectorizer.vocabulary_)

vectorizer = TfidfVectorizer()
print(vectorizer.fit_transform(corpus).todense())
print(vectorizer.vocabulary_)
