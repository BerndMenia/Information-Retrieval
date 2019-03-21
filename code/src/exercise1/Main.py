from code.src.exercise1.Tokenizer import Tokenizer

list_file_paths = ["books/the_raven.txt"]

for file_path in list_file_paths:
    tokenizer = Tokenizer()
    string = tokenizer.read_in(file_path)
    tokens = tokenizer.tokenize_text(string)
    text = tokenizer.remove_punctuation(tokens)
    frequencies = tokenizer.get_frequency(text)

    print("Number of terms:", len(text))
    print("Number of unique terms:", len(set(text)))
    print("NLTK stopwords:", tokenizer.get_stopwords_list_length())
    print("Number of stopwords in text:", tokenizer.count_stopwords(text))
    tokenizer.print_frequency(frequencies, 50)


'''
dg_raw = read_in("books/the_raven.txt")
print("dg_raw", type(dg_raw), "\n")

# load data
dg_url = "https://www.gutenberg.org/cache/epub/174/pg174.txt"
#  dg_raw = urlopen(dg_url).read().decode('utf-8')
# dg_raw = read_in("books/the_raven.txt")

# tokenization: break up string into words an punctuation
dg_tokens = nltk.word_tokenize(dg_raw)
print(dg_tokens)
print("dg_tokens", type(dg_tokens), "\n")

# dg_text = nltk.Text(dg_tokens)
# print("dg_text", type(dg_text), "\n")

# remove punktuation and lowercase tokens
# I would lower case everything directly at the start when reading in the file.
dg_prep_tokens = [word.lower() for word in dg_tokens if word.isalpha()]
print(dg_prep_tokens)
print("dg_prep_tokens", type(dg_prep_tokens), "\n")

dg_text = nltk.Text(dg_prep_tokens)
print(dg_text)
print("dg_text", type(dg_text), "\n")


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
print("Stopwords in text:", count_stopwords(dg_text))
'''