# Text Classifier

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.naive_bayes import MultinomialNB

text=["AI is amazing","football is fun","python is great","Tennis is exciting"]

labels=[0,1,0,1]

vectorizer=CountVectorizer()

x=vectorizer.fit_transform(text)

model=MultinomialNB()
model.fit(x,labels)

new_text=['machine learning is poweful','I like tennis']
x_new=vectorizer.transform(new_text)

predictions=model.predict(x_new)
print(predictions)