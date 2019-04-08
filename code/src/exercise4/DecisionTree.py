from sklearn.tree import DecisionTreeClassifier

class DecisionTree:
    def __init__(self):
        self.classifier = DecisionTreeClassifier()

    def clf_fit(self, X, y):
        return self.classifier.fit(X, y)

    def clf_predict(self, X):
        return self.classifier.predict(X)
