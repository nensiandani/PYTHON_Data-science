from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

text = "i am radha"
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
named_entities = ne_chunk(pos_tags)
print("named entities")
print("named_entities")

