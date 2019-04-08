import numpy as np
import re
import nltk
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pickle
from nltk.corpus import stopwords
from os.path import abspath


# import the dataset
path_traindata = abspath("../../../resources/C50train")
path_testdata = abspath("../../../resources/C50test")

authorship_traindata = load_files(path_traindata)
authorship_testdata = load_files(path_testdata)

# data is loaded into X, target categories are stored in y
# X is a list of 2500 string elements where each element corresponds to an author's papers
# y is a numpy array of 2500 entries, the numbers are 1-50 since we have 50 authors
X_train, y_train = authorship_traindata.data, authorship_traindata.target
X_test, y_test = authorship_testdata.data, authorship_testdata.target


# extract features with vectorizer
# tf-idf vectors
tfidf_vectorizer = TfidfVectorizer() # for removing stopwords, set parameter stop_words='english'

# tokenize and build vocabulary
tfidf_tok_train = tfidf_vectorizer.fit(X_train)
#print(tok_train.vocabulary_)
#print(tok_train.idf_)

# encode document
tfidf_vec_train = tfidf_tok_train.transform(X_train)
#print(tfidf_vectorizer.get_feature_names())
#print(vec_train.shape)
#print(vec_train.toarray())

# NOTE: stuff above could also be done in one step: vec_train = vectorizer.fit_transform(X_train), but in order to see whats happening i split it up here

# word ngrams
unigram_w_vectorizer = CountVectorizer(ngram_range=(1, 1), analyzer='word')
bigram_w_vectorizer = CountVectorizer(ngram_range=(2, 2), analyzer='word')
trigram_w_vectorizer = CountVectorizer(ngram_range=(3, 3), analyzer='word')

unigram_w_vec_train = unigram_w_vectorizer.fit_transform(X_train)
#print(unigram_w_vectorizer.get_feature_names())

bigram_w_vec_train = bigram_w_vectorizer.fit_transform(X_train)
#print(bigram_w_vectorizer.get_feature_names())

trigram_w_vec_train = trigram_w_vectorizer.fit_transform(X_train)
#print(trigram_w_vectorizer.get_feature_names())

# char ngrams
unigram_c_vectorizer = CountVectorizer(ngram_range=(1, 1), analyzer='char_wb')
bigram_c_vectorizer = CountVectorizer(ngram_range=(2, 2), analyzer='char_wb')
trigram_c_vectorizer = CountVectorizer(ngram_range=(3, 3), analyzer='char_wb')

unigram_c_vec_train = unigram_c_vectorizer.fit_transform(X_train)
#print(unigram_c_vectorizer.get_feature_names())

bigram_c_vec_train = bigram_c_vectorizer.fit_transform(X_train)
print(bigram_c_vectorizer.get_feature_names())

trigram_c_vec_train = trigram_c_vectorizer.fit_transform(X_train)
#print(trigram_c_vectorizer.get_feature_names())

