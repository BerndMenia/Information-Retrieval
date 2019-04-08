from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics import accuracy_score
from os.path import abspath
from code.src.exercise4.SVM import SVM
from code.src.exercise4.KNN import KNN
from code.src.exercise4.DecisionTree import DecisionTree


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

tfidf_vec_train = tfidf_vectorizer.fit_transform(X_train)
tfidf_vec_test = tfidf_vectorizer.transform(X_test) # note: vectorizers should not be fit on test data
#print("len test: ", tfidf_vec_test.getnnz)
#print("len train: ", tfidf_vec_train.getnnz)

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
#print(bigram_c_vectorizer.get_feature_names())

trigram_c_vec_train = trigram_c_vectorizer.fit_transform(X_train)
#print(trigram_c_vectorizer.get_feature_names())


# train svm classifier on training data
svm = SVM()
clf_svm = svm.clf_fit(tfidf_vec_train, y_train)
# predict response for test dataset using svm
y_predict_svm = svm.clf_predict(tfidf_vec_test)
print("SVM accuracy score: ", accuracy_score(y_predict_svm, y_test)*100, "%")

# train knn classifier on training data
knn = KNN()
clf_knn = knn.clf_fit(tfidf_vec_train, y_train)
# predict response for test dataset using knn
y_predict_knn = knn.clf_predict(tfidf_vec_test)
print("KNN accuracy score: ", accuracy_score(y_predict_knn, y_test)*100, "%")

# train decision tree classifier on training data
dt = DecisionTree()
clf_dt = dt.clf_fit(tfidf_vec_train, y_train)
# predict response for test dataset using decision tree
y_predict_dt = dt.clf_predict(tfidf_vec_test)
print("Decision Tree accuracy score: ", accuracy_score(y_predict_dt, y_test)*100, "%")
