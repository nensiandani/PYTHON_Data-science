# wap of lemmatization

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

text="hello children"

tokens=word_tokenize(text)

lemmatizer=WordNetLemmatizer()

lemmatize_words=[lemmatizer.lemmatize(word)for word in tokens]

print("original tokens:",tokens)

print("Lemmatized words:",lemmatize_words)