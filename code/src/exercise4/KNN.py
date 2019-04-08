from sklearn.neighbors import KNeighborsClassifier

class KNN:
    def __init__(self):
        self.classifier = KNeighborsClassifier(n_neighbors=5)

    def clf_fit(self, X, y):
        return self.classifier.fit(X, y)

    def clf_predict(self, X):
        return self.classifier.predict(X)
