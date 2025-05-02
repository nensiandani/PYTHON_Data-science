#part of speech (pos) tagging

from nltk.tokenize import word_tokenize
from nltk import pos_tag

text="nlp helps computers understand"

tokens=word_tokenize(text)

pos_tag=pos_tag(tokens)

print("pos Tages:",pos_tag)
