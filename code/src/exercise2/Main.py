from code.src.exercise1.Tokenizer import Tokenizer
from code.src.exercise2.InvertedIndex import InvertedIndex
from code.src.exercise2.BooleanRetrieval import BooleanRetrieval
from code.src.exercise2.Measures import Measures
from code.src.exercise2.Helper import Helper

helper = Helper()
#list_file_paths = helper.get_documents() # TODO: NOTE: the get_documents function returns all files contained in the files directiory, for testing purposes by now we just use file 1 and 2
list_file_paths = ["files/1.txt", "files/2.txt"]
inverted_index = InvertedIndex()
count = 1 # The document counter

#for file_path in list_file_paths:
for i in range(1, 11):
    file_path = "files/" + str(i) + ".txt"

    # preprocess input text
    tokenizer = Tokenizer()

    string = tokenizer.read_in(file_path)

    tokens = tokenizer.tokenize_text(string)
    # remove punctuation and stopwords
    text_prep_punct = tokenizer.remove_punctuation(tokens)
    text_prep_stop = tokenizer.remove_stopwords(text_prep_punct)
    # stem tokens
    text_prep_stem = tokenizer.stem_words(text_prep_stop)

    # print text statistics
    frequencies = tokenizer.get_frequency(text_prep_punct)
    print("Statistics for "+file_path)
    print("Number of terms:", len(text_prep_punct))
    print("Number of unique terms:", len(set(text_prep_punct)))
    print("NLTK stopwords:", tokenizer.get_stopwords_list_length())
    print("Number of stopwords in text:", tokenizer.count_stopwords(text_prep_punct))
    #print("Overall frequencies: ", tokenizer.print_frequency(frequencies, 0))
    print("Top 50 frequencies: ", tokenizer.print_frequency(frequencies, 10))
    print()

    # create inverted index
    inverted_index.text_list = text_prep_punct     # As of now this statement is actually useless because we don't utilized classes as they should be, but /we : P.
    inverted_index.add_document2(text_prep_stem, count)
    count += 1

print(inverted_index.index2)

inverted_index.construct_ngram(1)
inverted_index.construct_ngram(2)
inverted_index.construct_ngram(3)

'''Monogram'''
mono_words = inverted_index.get_nwords(1)
#inverted_index.construct_monogram()

print(len(mono_words), mono_words)
print(inverted_index.monogram, "\n")


'''Bigram'''
bi_words = inverted_index.get_nwords(2)
#inverted_index.construct_bigram()

print(len(bi_words), bi_words)
print(inverted_index.bigram, "\n")


'''Trigram'''
tri_words = inverted_index.get_nwords(3)
print(len(tri_words), tri_words)
print(inverted_index.trigram, "\n")


'''Query ngrams'''
print("Searching for e:")
print(inverted_index.query_ngram("e"), "\n")

print("Searching for xp:")
print(inverted_index.query_ngram("xp"), "\n")

print("Searching for agr:")
print(inverted_index.query_ngram("agr"), "\n")

print("Searching for my:")
print(inverted_index.query_ngram("my"), "\n")

# here we get the first query out of queries.csv
query_list = helper.get_sample_queries()
sample_query = query_list[0]
print(sample_query)

test_query = "theoretical OR problem" # TODO: NOTE: using this query I get the error that the index_token1 has no attribute get - index_token1 is constructed using query2()
#test_query = "construct OR model" # TODO: NOTE: using this query I get the error that the key 'construct' is not found
# TODO: NOTE: this was just for testing the boolean retrieval since such queries are not given in queries.csv ?
bool_retrieval = BooleanRetrieval()
bool_retrieval.bool_search(test_query, inverted_index)

# calculate similarity and evaluation measures
measures = Measures()
sim_result = measures.sim(sample_query, tokenizer.read_in(list_file_paths[1]))
print("Similarity: ", sim_result)
# TODO: unsure about the parameters for precision and recall - i think we need the overall set of postings for the corresponding document together with the set of postings specific for our query
relevant_docs = [] # TODO: parameter in queries csv
retrieved_relevant_docs = [] # TODO: count of retrieved postings with relation to the actually relevant docs out of queries csv
total_retrieved_docs = [] # TODO: count of retrieved postings
recall_measure = measures.recall([], [])
print("Recall: ", recall_measure)
precision_measure = measures.precision([], [])
print("Precision:", precision_measure)
f1_score = measures.f1score(recall_measure, precision_measure)
print("F1-score: ", f1_score)
