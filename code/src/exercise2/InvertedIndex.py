from code.src.utils.Utils import binary_search
from code.src.utils.Utils import search_string

import nltk



class InvertedIndex:

    def __init__(self, text=[""]):
        self.porter_stemmer = nltk.stem.PorterStemmer()
        if len(text) == 0:
            self.text_list = "Such an analysis can reveal features that are not easily visible from the variations in the individual genes and can lead to a picture of expression that is more biologically transparent and accessible to interpretation".split()
        else:
            self.text_list = text

        # index --> list[("string", list[(doc, position))]
        # self.index = {}
        self.index = []
        self.document_count = 1


    def stem_string_list(self, list):
        return [self.porter_stemmer.stem(s) for s in list]


    # I think it's better to work with lists of strings at this point. So maybe delete this function.
    def stem_string(self, text):
        return [self.porter_stemmer.stem(s) for s in text.split()]


    # document = list(string)
    # document_count should maybe be a parameter, not sure
    def add_document(self, document):
        l = []
        words = [word for word,list_tuple in self.index]

        #for i in range(len(document)):
        for i in range(20):
            s = self.porter_stemmer.stem(document[i])
            l.append((i, s))

            # found_i = binary_search(words, s)

            # Word not yet in index
            # if found_i == -1:
            if not (s in words):
                self.index.append((s, [(self.document_count, i)]))
                words.append(s) # Update the words list so that a just appended word can be found
                print(words)
            else:
                j = search_string(words, s)
                _,list = self.index[j]
                list.append((self.document_count, i))
                self.index[j] = (s, list)



        print("l size:", len(l))
        print(l, "\n")

        print("Index size:", len(self.index))
        print(self.index)

        for index, word in l:
            self.index

        # Sort index!
        # self.index.sort()


    def query(self, to_search):
        to_search = self.porter_stemmer.stem(to_search)
        x = 1 # Placeholder

    # [("b", [(1,3), (1,2), (1,7)]),("a", [(1,9),(2,7)]),("c", [(3,3)])]