from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from os.path import abspath
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from code.src.exercise4.Plot import Plot

# ------------------------------------------------- import the dataset ------------------------------------------------- #
path_traindata = abspath("../../../resources/C50train")
path_testdata = abspath("../../../resources/C50test")

authorship_traindata = load_files(path_traindata)
authorship_testdata = load_files(path_testdata)

# -------------------------------------------- prepare train and test data -------------------------------------------- #
# data is loaded into X, target categories are stored in y
# X is a list of 2500 string elements where each element corresponds to an author's papers
# y is a numpy array of 2500 entries, the numbers are 1-50 since we have 50 authors
X_train, y_train = authorship_traindata.data, authorship_traindata.target
X_test, y_test = authorship_testdata.data, authorship_testdata.target

class_names = authorship_testdata.target_names


# ---------------------------------------------------- VECTORIZERS ---------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------- extract features with tf-idf vectorizer -------------------------------------- #
# tf-idf vectors
tfidf_vectorizer = TfidfVectorizer() # for removing stopwords, set parameter stop_words='english'

tfidf_vec_train = tfidf_vectorizer.fit_transform(X_train)
tfidf_vec_test = tfidf_vectorizer.transform(X_test) # note: vectorizers should not be fit on test data
#print("len test: ", tfidf_vec_test.getnnz)
#print("len train: ", tfidf_vec_train.getnnz)

# ------------------------------------ extract features with word ngrams vectorizer ------------------------------------ #
# word ngrams
# TODO - NOTE: in order to user unigram enter ngram_range=(1,1), for bigram enter ngram_range=(2,2) and for trigram enter ngram_range=(3,3)
ngram_w_vectorizer = CountVectorizer(ngram_range=(2, 2), analyzer='word')

ngram_w_vec_train = ngram_w_vectorizer.fit_transform(X_train)
#print(ngram_w_vectorizer.get_feature_names())
ngram_w_vec_test = ngram_w_vectorizer.transform(X_test)

# ------------------------------------ extract features with char ngrams vectorizer ------------------------------------ #
# char ngrams
# TODO - NOTE: in order to user unigram enter ngram_range=(1,1), for bigram enter ngram_range=(2,2) and for trigram enter ngram_range=(3,3)
ngram_c_vectorizer = CountVectorizer(ngram_range=(2, 2), analyzer='char_wb')

ngram_c_vec_train = ngram_c_vectorizer.fit_transform(X_train)
#print(ngram_c_vectorizer.get_feature_names())
ngram_c_vec_test = ngram_c_vectorizer.transform(X_test)


# ---------------------------------------------------- CLASSIFIERS ---------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #
plot = Plot()

# -------------------------------------------------------- SVM -------------------------------------------------------- #
svm_clf = svm.SVC(gamma='auto')

# -------------------------------------------------- on TF-IDF data --------------------------------------------------- #
# train svm classifier on training data
svm_clf_tfidf = svm_clf.fit(tfidf_vec_train, y_train)
# predict response for test dataset using svm
y_predict_svm_tfidf = svm_clf_tfidf.predict(tfidf_vec_test)
print("SVM accuracy score [TF-IDF]: ", accuracy_score(y_predict_svm_tfidf, y_test)*100, "%")
plot.plot_confusion_matrix(y_test, y_predict_svm_tfidf, class_names, clf="SVM [TF-IDF]")

# ------------------------------------------------ on word ngram data ------------------------------------------------- #
# train svm classifier on training data
svm_clf_wng = svm_clf.fit(ngram_w_vec_train, y_train)
# predict response for test dataset using svm
y_predict_svm_wng = svm_clf_wng.predict(ngram_w_vec_test)
print("SVM accuracy score [word ngram]: ", accuracy_score(y_predict_svm_wng, y_test)*100, "%")
plot.plot_confusion_matrix(y_test, y_predict_svm_wng, class_names, clf="SVM [word ngrams]")

# ------------------------------------------------ on char ngram data ------------------------------------------------- #
# train svm classifier on training data
svm_clf_cng = svm_clf.fit(ngram_c_vec_train, y_train)
# predict response for test dataset using svm
y_predict_svm_cng = svm_clf_cng.predict(ngram_c_vec_test)
print("SVM accuracy score [char ngram]: ", accuracy_score(y_predict_svm_cng, y_test)*100, "%")
plot.plot_confusion_matrix(y_test, y_predict_svm_cng, class_names, clf="SVM [char ngrams]")

# -------------------------------------------------------- KNN -------------------------------------------------------- #
knn_clf = KNeighborsClassifier(n_neighbors=5)

# -------------------------------------------------- on TF-IDF data --------------------------------------------------- #
# train knn classifier on training data
knn_clf_tfidf = knn_clf.fit(tfidf_vec_train, y_train)
# predict response for test dataset using knn
y_predict_knn_tfidf = knn_clf_tfidf.predict(tfidf_vec_test)
print("KNN accuracy score [TF-IDF]: ", accuracy_score(y_predict_knn_tfidf, y_test)*100, "%")
plot.plot_confusion_matrix(y_test, y_predict_knn_tfidf, class_names, clf="KNN [TF-IDF]")

# ------------------------------------------------ on word ngram data ------------------------------------------------- #
# train knn classifier on training data
knn_clf_wng = knn_clf.fit(ngram_w_vec_train, y_train)
# predict response for test dataset using knn
y_predict_knn_wng = knn_clf_wng.predict(ngram_w_vec_test)
print("KNN accuracy score [word ngram]: ", accuracy_score(y_predict_knn_wng, y_test)*100, "%")
plot.plot_confusion_matrix(y_test, y_predict_knn_wng, class_names, clf="KNN [word ngrams]")

# ------------------------------------------------ on char ngram data ------------------------------------------------- #
# train knn classifier on training data
knn_clf_cng = knn_clf.fit(ngram_c_vec_train, y_train)
# predict response for test dataset using knn
y_predict_knn_cng = knn_clf_cng.predict(ngram_c_vec_test)
print("KNN accuracy score [char ngram]: ", accuracy_score(y_predict_knn_cng, y_test)*100, "%")
plot.plot_confusion_matrix(y_test, y_predict_knn_cng, class_names, clf="KNN [char ngrams]")

# -------------------------------------------------- Decision Tree ---------------------------------------------------- #
dt_clf = DecisionTreeClassifier()
# -------------------------------------------------- on TF-IDF data --------------------------------------------------- #
# train decision tree classifier on training data
dt_clf_tfidf = dt_clf.fit(tfidf_vec_train, y_train)
# predict response for test dataset using decision tree
y_predict_dt_tfidf = dt_clf_tfidf.predict(tfidf_vec_test)
print("Decision Tree accuracy score [TF-IDF]: ", accuracy_score(y_predict_dt_tfidf, y_test)*100, "%")
plot.plot_confusion_matrix(y_test, y_predict_dt_tfidf, class_names, clf="DT [TF-IDF]")

# ------------------------------------------------ on word ngram data ------------------------------------------------- #
# train decision tree classifier on training data
dt_clf_wng = dt_clf.fit(ngram_w_vec_train, y_train)
# predict response for test dataset using decision tree
y_predict_dt_wng = dt_clf_wng.predict(ngram_w_vec_test)
print("Decision Tree accuracy score [word ngram]: ", accuracy_score(y_predict_dt_wng, y_test)*100, "%")
plot.plot_confusion_matrix(y_test, y_predict_dt_wng, class_names, clf="DT [word ngrams]")

# ------------------------------------------------ on char ngram data ------------------------------------------------- #
# train decision tree classifier on training data
dt_clf_cng = dt_clf.fit(ngram_c_vec_train, y_train)
# predict response for test dataset using decision tree
y_predict_dt_cng = dt_clf_cng.predict(ngram_c_vec_test)
print("Decision Tree accuracy score [char ngram]: ", accuracy_score(y_predict_dt_cng, y_test)*100, "%")
plot.plot_confusion_matrix(y_test, y_predict_dt_cng, class_names, clf="DT [char ngrams]")

