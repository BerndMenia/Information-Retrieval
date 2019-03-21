import nltk

class InvertedIndex:

    def __init__(self, text=""):
        self.porter_stemmer = nltk.stem.PorterStemmer()
        text = "Such an analysis can reveal features that are not easily visible from the variations in the individual genes and can lead to a picture of expression that is more biologically transparent and accessible to interpretation"


    def stem_string_list(self, list):
        return [self.porter_stemmer.stem(s) for s in list]


    # I think it's better to work with lists of strings at this point. So maybe delete this function.
    def stem_string(self, text):
        return [self.porter_stemmer.stem(s) for s in text.split()]