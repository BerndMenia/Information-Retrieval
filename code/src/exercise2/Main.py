from code.src.exercise1.Tokenizer import Tokenizer
from code.src.exercise2.InvertedIndex import InvertedIndex
from code.src.exercise2.QueryParser import QueryParser


# text = "Such an analysis can reveal features that are not easily visible from the variations in the individual genes and can lead to a picture of expression that is more biologically transparent and accessible to interpretation"


list_file_paths = ["books/the_raven.txt", "books/test.txt"]
inverted_index = InvertedIndex()
count = 1 # The document counter

for file_path in list_file_paths:
    tokenizer = Tokenizer()
    string = tokenizer.read_in(file_path)
    tokens = tokenizer.tokenize_text(string)
    # remove punctuation and stopwords
    text_prep_punct = tokenizer.remove_punctuation(tokens)
    text_prep_stop = tokenizer.remove_stopwords(text_prep_punct)
    # stem tokens
    text_prep_stem = tokenizer.stem_words(text_prep_stop)

    # get text statistics
    frequencies = tokenizer.get_frequency(text_prep_punct)

    print("Number of terms:", len(text_prep_punct))
    print("Number of unique terms:", len(set(text_prep_punct)))
    print("NLTK stopwords:", tokenizer.get_stopwords_list_length())
    print("Number of stopwords in text:", tokenizer.count_stopwords(text_prep_punct))
    #tokenizer.print_frequency(frequencies, 50)

    #inverted_index = InvertedIndex(text)
    inverted_index.text_list = text_prep_punct     # As of now this statement is actually useless because we don't utilized classes as they should be, but /we : P.

    #stemmed_text = inverted_index.stem_string_list(text)
    #print(stemmed_text)

    inverted_index.add_document(text_prep_stem, count)
    count += 1
    print(inverted_index.query("the"))
    print(inverted_index.query("raven"))
    print(inverted_index.query("hello"))

# testing query parser
query_parser = QueryParser()
print(query_parser.parse_query("this is a test for testing query parsing"))
