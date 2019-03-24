import nltk
from nltk.corpus import stopwords
from urllib.request import urlopen
from os.path import abspath
from nltk.stem import PorterStemmer


class Tokenizer:

    def __init__(self):
        self.stemmer = PorterStemmer()


    # Read in a text file from a local directory. Right now the books-directory  is placed in root.
    def read_in(self, file_path):
        file_path = abspath("../../../" + file_path)
        file = open(file_path, "r")
        return file.read().lower()


    # Load a text file from a URL.
    def load_data(self, url):
        return urlopen(url).read().decode('utf-8')


    # Split a given string up into tokens with NLTK
    def tokenize_text(self, string):
        tokens = nltk.word_tokenize(string)
        return nltk.Text(tokens)


    # Remove all punctuations from tokens.
    # Shouldn't we first remove punctuation and then tokenize it instead of the other way round like we do now?
    def remove_punctuation(self, tokens):
        prep_tokens = [word.lower() for word in tokens if word.isalpha()]
        return nltk.Text(prep_tokens)


    # For each word in the string count how many times it occurs in the whole string.
    def get_frequency(self, text):
        return nltk.FreqDist(text)


    # Nicely formatted frequency distribution output for the n most common words.
    def print_frequency(self, frequencies, n):
        #frequencies = nltk.FreqDist(text)

        if n == 0:
            n = len(frequencies)

        for word, frequency in frequencies.most_common(n):
            print(u'{};{}'.format(word, frequency))


    # Check the size of the stopword list imported from NLTK.
    def get_stopwords_list_length(self):
        return len(set(stopwords.words('english')))


    def count_stopwords(self, text):
        count = 0
        for s in text:
            if s in stopwords.words('english'):
                count += 1
        return count

    def remove_stopwords(self, tokens):
        stopword_list = set(stopwords.words('english'))

        filtered_sentence = [w for w in tokens if not w in stopword_list]

        return filtered_sentence

    def stem_words(self, tokens):
        stemmed_sentence = [self.stemmer.stem(t) for t in tokens]

        return stemmed_sentence


