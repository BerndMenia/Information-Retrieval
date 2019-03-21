import nltk
from nltk.corpus import stopwords
from urllib.request import urlopen
from os.path import abspath


# Read in a text file from a local directory. Right now the books-directory  is placed in root.
def read_in(file_path):
    file_path = abspath("../../../" + file_path)
    file = open(file_path, "r")
    return file.read().lower()


# Load a text file from a URL.
def load_data(url):
    return urlopen(url).read().decode('utf-8')


# Split a given text up into tokens with NLTK
def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    return nltk.Text(tokens)


# Remove all punctuations from tokens.
# Shouldn't we first remove punctuation and then tokenize it instead of the other way round like we do now?
def remove_punctuation(tokens):
    prep_tokens = [word.lower() for word in tokens if word.isalpha()]
    return nltk.Text(prep_tokens)


# For each
def get_frequency(text):
    return nltk.FreqDist(text)


# Nicely formatted frequency distribtuion output for the n most common words.
def print_frequency(n):
    for word, frequency in dg_term_freq.most_common():
        print(u'{};{}'.format(word, frequency))


# Check the size of the stopword list imported from NLTK.
def get_stopword_list_length():
    len(set(stopwords.words('english')))


def count_stopwords(text):
    count = 0
    for s in text:
        if s in stopwords:
            count += 1
    return count


dg_raw = read_in("books/the_raven.txt")




# load data
dg_url = "https://www.gutenberg.org/cache/epub/174/pg174.txt"
dg_raw = urlopen(dg_url).read().decode('utf-8')
# dg_raw = read_in("books/the_raven.txt")

# tokenization: break up string into words an punctuation
dg_tokens = nltk.word_tokenize(dg_raw)
dg_text = nltk.Text(dg_tokens)

# remove punktuation and lowercase tokens
dg_prep_tokens = [word.lower() for word in dg_tokens if word.isalpha()]
dg_text = nltk.Text(dg_prep_tokens)
print("TYPE:", dg_text)

# total number of terms
dg_num_terms = str(len(dg_text))
print("Total number of terms: "+dg_num_terms)

# total number of unique terms
dg_num_unique_terms = str(len(set(dg_text)))
print("Number of unique terms: "+dg_num_unique_terms)

# frequency of each term
dg_term_freq = nltk.FreqDist(dg_text)
#print("Total term frequencies: \n")
#for word, frequency in dg_term_freq.most_common():
#    print(u'{};{}'.format(word, frequency))

# list of the top-50 terms with the according frequency and rank over the whole text corpus
#print("50 most common tokens: \n")
#for word, frequency in dg_term_freq.most_common(50):
#    print(u'{};{}'.format(word, frequency))
#dg_term_freq.plot(50, cumulative=True, title="50 most common tokens")

# number of stopwords contained
dg_num_stopwords = str(len(set(stopwords.words('english'))))
print("Number of stopwords: "+dg_num_stopwords)
#print("Stopwords in text:", count_stopwords(dg_text))
