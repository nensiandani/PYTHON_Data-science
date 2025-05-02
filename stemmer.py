#wap of stemmer

from nltk.stem import porterstremmer
from nltk.tokenize import word_tokenize

text='I am Running'

tokens = word_tokenize(text)

stemmer=porterstremmer()

stemmed_word=[stemmer.stem(word)for word in tokens]

print("original tokens:",tokens)
print("stemmed words:",stemmed_word)