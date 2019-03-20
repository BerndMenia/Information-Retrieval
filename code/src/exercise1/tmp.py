import nltk
from nltk.corpus import stopwords
from urllib.request import urlopen
from os.path import abspath


def read_in(file_path):
    file_path = abspath("../../../" + file_path)
    file = open(file_path, "r")
    return file.read().lower()


nltk.download('punkt')
nltk.download('stopwords')

# load data
dg_url = "https://www.gutenberg.org/cache/epub/174/pg174.txt"
# dg_raw = urlopen(dg_url).read().decode('utf-8')
dg_raw = read_in("books/the_raven.txt")

# tokenization: break up string into words an punctuation
dg_tokens = nltk.word_tokenize(dg_raw)
dg_text = nltk.Text(dg_tokens)

# remove punktuation and lowercase tokens
dg_prep_tokens = [word.lower() for word in dg_tokens if word.isalpha()]
dg_text = nltk.Text(dg_prep_tokens)

# total number of terms
dg_num_terms = str(len(dg_text))
print("Total number of terms: "+dg_num_terms)

# total number of unique terms
dg_num_unique_terms = str(len(set(dg_text)))
print("Number of unique terms: "+dg_num_unique_terms)

# frequency of each term
dg_term_freq = nltk.FreqDist(dg_text)
print("Total term frequencies: \n")
for word, frequency in dg_term_freq.most_common():
    print(u'{};{}'.format(word, frequency))

# list of the top-50 terms with the according frequency and rank over the whole text corpus
print("50 most common tokens: \n")
for word, frequency in dg_term_freq.most_common(50):
    print(u'{};{}'.format(word, frequency))
dg_term_freq.plot(50, cumulative=True, title="50 most common tokens")

# number of stopwords contained
dg_num_stopwords = str(len(set(stopwords.words('english'))))
print("Number of stopwords: "+dg_num_stopwords)

