#wap of removing stop words

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text="NLP allows computers to understand human language."

tokens=word_tokenize(text)

stop_words=set(stopwords.words('English'))

filterd_tokens=[word for word in tokens if wordlower() not in stop_words]

print("original tokens:",tokens)
print("filtered tokens(without stopwords:)",filterd_tokens)

