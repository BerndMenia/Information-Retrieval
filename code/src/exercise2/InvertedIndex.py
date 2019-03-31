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
        self.index    = []
        self.index2   = {}
        self.monogram = {}
        self.bigram   = {}
        self.trigram  = {}
        self.ngrams   = [self.monogram, self.bigram, self.trigram]
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
        #print("l size:", len(l))
        #print(l, "\n")

        print("Index size:", len(self.index))
        print(self.index)

        # Sort index!
        # Even better: Insert indices sorted.
        # self.index.sort()


    def add_document2(self, document, count):
        keys = {key for key in self.index2.keys()}

        for i in range(len(document)):
            s = document[i]

            if not (s in keys):
                self.index2[s] = [(count, i)]
                keys.add(s)
            else:
                #self.index2[s].append((count, i))
                bisect.insort(self.index2[s], (count, i))

        #print(self.index2)


    # https://stackoverflow.com/questions/13902805/list-of-all-unique-characters-in-a-string
    def get_mono_words(self):
        full_string = ""

        for s in self.index2.keys():
            full_string += s

        return set(full_string)


    def get_bi_words(self):
        if not len(self.index2) > 0:
            return set()

        full_string = ""

        for s in self.index2.keys():
            full_string += "$" + s
        full_string += "$"

        bi_words = set()
        for i in range(len(full_string)-1):
            bi_words.add(full_string[i] + full_string[i+1])

        return bi_words


    def get_nwords(self, n):
        if not len(self.index2) > 0:
            return set()

        full_string = ""

        if n == 1:
            return set(''.join( [full_string + s for s in self.index2.keys()] ) )
            #return set(''.join(self.index2.keys()))
            #return set( [full_string + s for s in self.index2.keys()] )

        for s in self.index2.keys():
            full_string += "$" + s
        full_string += "$"

        nwords = set()
        for i in range(len(full_string) - (n-1)):
            nwords.add(full_string[i:i+n])

        return nwords


    def construct_monogram(self):
        mono_words = self.get_mono_words()

        for mono in mono_words:
            for key in self.index2.keys():
                if mono in key:
                    if not mono in self.monogram:
                        self.monogram[mono] = {key: self.index2[key]}
                    elif not key in self.monogram[mono]:
                        self.monogram[mono][key] = self.index2[key]


    def construct_bigram(self):
        bi_words = self.get_bi_words()

        for bi in bi_words:
            for key in self.index2.keys():
                if bi in key:
                    if not bi in self.bigram:
                        self.bigram[bi] = {key: self.index2[key]}
                    elif not key in self.bigram[bi]:
                        self.bigram[bi][key] = self.index2[key]


    def construct_ngram(self, n):
        if not 0 < n <= len(self.ngrams):
            return

        n_words = self.get_nwords(n)
        n_gram = self.ngrams[n-1]

        # Maybe replace with a switch()
        #if n == 1:
        #nwords = self.get_mono_words()
        #    ngram = self.monogram
        #elif n == 2:
        #nwords = self.get_bi_words()
        #    ngram = self.bigram
        #elif n == 3:
        #    ngram = self.trigram

        for word in n_words:
            for key in self.index2.keys():
                if word in key:
                    if not word in n_gram:
                        n_gram[word] = {key: self.index2[key]}
                    elif not key in n_gram[word]:
                        n_gram[word][key] = self.index2[key]



    def query(self, to_search):
        to_search = self.porter_stemmer.stem(to_search)

        for word,list_tuple in self.index:
            if word == to_search:
                return word, list_tuple

        return ()


    # The new query
    def query2(self, to_search):
        return self.index2[self.porter_stemmer.stem(to_search)]


    # Dummy query while bool_search() gets updated to query2()
    def query3(self, to_search):
        list_tuple = self.index2[self.porter_stemmer.stem(to_search)]

        if list_tuple:
            return to_search, list_tuple
        else:
            return ()


    def query_ngram(self, to_search):
        result = {}
        n = len(to_search)

        if 0 < n <= len(self.ngrams):
            n_gram  = self.ngrams[n-1]

            if to_search in n_gram:
                result = n_gram[to_search]

        return result

    # [("b", [(1,3), (1,2), (1,7)]),("a", [(1,9),(2,7)]),("c", [(3,3)])]