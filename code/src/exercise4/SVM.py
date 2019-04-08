from sklearn import svm

class SVM:
    def __init__(self):
        self.classifier = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')

    # fit the training dataset on the classifier
    def clf_fit(self, X, y):
        return self.classifier.fit(X, y)

    # predict the labels on validation dataset (test)
    def clf_predict(self, X):
        return self.classifier.predict(X)
