from code.src.utils.Utils import binary_search
from code.src.utils.Utils import search_string

import nltk
import bisect


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


    def add_document(self, document, count):
        l = []

        # Get all words that are in the index (at the start this should be empty)
        words = [word for word,list_tuple in self.index]

        # Iterate over the document and insert each word into the Inverted Index
        for i in range(len(document)):
            #s = self.porter_stemmer.stem(document[i])
            s = document[i]

            # Just for testing, can ignore.
            l.append((i, s))

            # If the current word of the document is not in the Inverted Index append it to the end (Not yet sorted!)
            if not (s in words):
                self.index.append((s, [(count, i)]))
                words.append(s) # Update the words list so that a just appended word can be found

            # If it is already in the Inverted Index find the index of the word and add another tuple to the word
            # with (document_count, position)
            else:
                j = search_string(words, s)
                _,list = self.index[j]

                # This should insert the tuples of a word in order.
                bisect.insort(list, (count, i))
                # list.append((self.document_count, i))
                self.index[j] = (s, list)

        # Just for testing, can ignore.
        print("l size:", len(l))
        print(l, "\n")

        print("Index size:", len(self.index))
        print(self.index)

        # Sort index!
        # Even better: Insert indices sorted.
        # self.index.sort()


    def query(self, to_search):
        to_search = self.porter_stemmer.stem(to_search)

        for word,list_tuple in self.index:
            if word == to_search:
                return word, list_tuple

        return ()

    # [("b", [(1,3), (1,2), (1,7)]),("a", [(1,9),(2,7)]),("c", [(3,3)])]