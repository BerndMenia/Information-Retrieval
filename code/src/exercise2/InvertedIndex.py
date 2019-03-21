import nltk

porter_stemmer = nltk.stem.PorterStemmer()
text = "Hello I am a sample text =]. Please give me more input, I need it! Banana "

print(text)
text = porter_stemmer.stem(text)
print(text)

list = [porter_stemmer.stem(s) for s in text.split()]
print(list)