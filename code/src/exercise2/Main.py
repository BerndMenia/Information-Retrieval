import operator
import time
import random
from string import ascii_lowercase

from code.src.exercise1.Tokenizer import Tokenizer
from code.src.exercise2.InvertedIndex import InvertedIndex
from code.src.exercise2.BooleanRetrieval import BooleanRetrieval
from code.src.exercise2.Measures import Measures
from code.src.exercise2.Helper import Helper
from code.src.exercise3.VectorSpaceModel import VectorSpaceModel

# TODO: NOTE: when running Main - the computation takes much too long due to the time consuming matrix construction in Helper - this needs to be fixed

helper = Helper()
#list_file_paths = helper.get_documents() # TODO: NOTE: the get_documents function returns all files contained in the files directiory, for testing purposes by now we just use file 1 and 2
list_file_paths = ["files/1.txt", "files/2.txt"]
inverted_index = InvertedIndex()
count = 1 # The document counter

vsm = VectorSpaceModel()

#for file_path in list_file_paths:


#---------------From exercise 2!---------------------#

'''
for i in range(1, 1401):
    file_path = "files/" + str(i) + ".txt"
    #print("Indexing file: " + file_path)

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
    #print("Statistics for "+file_path)
    #print("Number of terms:", len(text_prep_punct))
    #print("Number of unique terms:", len(set(text_prep_punct)))
    #print("NLTK stopwords:", tokenizer.get_stopwords_list_length())
    #print("Number of stopwords in text:", tokenizer.count_stopwords(text_prep_punct))
    #print("Overall frequencies: ", tokenizer.print_frequency(frequencies, 0))
    #print("Top 50 frequencies: ", tokenizer.print_frequency(frequencies, 10))
    #print()

    # create inverted index
    inverted_index.text_list = text_prep_punct     # As of now this statement is actually useless because we don't utilized classes as they should be, but /we : P.
    inverted_index.add_document2(text_prep_stem, count)
    count += 1
'''


#---------------For exercise 3------------------#

documents = helper.load_documents()
tokenizer = Tokenizer()

print("Indexing files...")
start = time.time()

for i in range(1, 1401):
    string = documents[i-1]
    tokens = tokenizer.tokenize_text(string)
    text_prep_punct = tokenizer.remove_punctuation(tokens)
    text_prep_stop = tokenizer.remove_stopwords(text_prep_punct)
    text_prep_stem = tokenizer.stem_words(text_prep_stop)
    inverted_index.add_document2(text_prep_stem, count)
    count += 1

end = time.time()
inverted_index_time = end-start

print("Finished indexing!")
print("------------------------------------------------------------------------\n")
#print("Inverted Index:", inverted_index.index2, "\n")

count = 0
for key in inverted_index.index2.keys():
    if count > 1:
        break
    print(key, ":", inverted_index.index2[key])
    count += 1

print()


'''Inverted Index query times'''
index_times = []

for i in range(100):
    start = time.time()
    random_word = random.choice(list(inverted_index.index2.keys()))
    inverted_index.query2(random_word)
    end = time.time()
    index_times.append(end-start)

#--------------------------ngrams------------------------------------#

ngram_construction_times = []

for i in range(1, 4):
    start = time.time()
    inverted_index.construct_ngram(i)
    end = time.time()
    ngram_construction_times.append(end-start)

print("Index    construction time:", inverted_index_time, "seconds.")
print("Monogram construction time:", ngram_construction_times[0], "seconds")
print("Bigram   construction time:", ngram_construction_times[1], "seconds")
print("Trigram  construction time:", ngram_construction_times[2], "seconds\n")


'''Monogram'''
mono_words = inverted_index.get_nwords(1)
print("Monogram length:", len(mono_words))
count = 0

for key in inverted_index.monogram.keys():
    if count > 5:
        break
    #print(key, ":", inverted_index.monogram[key])
    count += 1

print(mono_words)
print("\n")


'''Bigram'''
bi_words = inverted_index.get_nwords(2)
print("Bigram length:", len(bi_words), bi_words)
count = 0

for key in inverted_index.bigram.keys():
    if count > 5:
        break
    print(key, ":", inverted_index.bigram[key])
    count += 1

print("\n")


'''Trigram'''
tri_words = inverted_index.get_nwords(3)
print("Trigram length:", len(tri_words), tri_words)
count = 0

for key in inverted_index.trigram.keys():
    if count > 5:
        break
    print(key, ":", inverted_index.trigram[key])
    count += 1

print("\n")

'''Query ngrams'''
print("Searching for e:")
print(inverted_index.query_ngram("e"), "\n")

print("Searching for xp:")
print(inverted_index.query_ngram("xp"), "\n")

print("Searching for agr:")
print(inverted_index.query_ngram("agr"), "\n")

print("Searching for my:")
print(inverted_index.query_ngram("my"))
print("------------------------------------------------------------------------\n")

#---------------------Query ngrams for measurement----------------#

ngram1_times = []
ngram2_times = []
ngram3_times = []
n = 100

for i in range(n):
    s1 = random.choice(ascii_lowercase)
    s2 = random.choice(ascii_lowercase)
    s3 = random.choice(ascii_lowercase)

    #print(query)
    start = time.time()
    inverted_index.query_ngram(s1)
    end = time.time()
    ngram1_times.append(end-start)

    start = time.time()
    inverted_index.query_ngram(s1 + s2)
    end = time.time()
    ngram2_times.append(end - start)

    start = time.time()
    inverted_index.query_ngram(s1 + s2 + s3)
    end = time.time()
    ngram3_times.append(end - start)

print("Index    average query time:", sum(index_times)  / n)
print("Monogram average query time:", sum(ngram1_times) / n)
print("Bigram   average query time:", sum(ngram2_times) / n)
print("Trigram  average query time:", sum(ngram3_times) / n, "\n")

#-------------------------Boolean Retrieval---------------------------------------------#


# here we get the first query out of queries.csv
query_list = helper.get_sample_queries()
sample_query = query_list[0]

'''
print(sample_query)

test_query = "theoretical OR problem" # TODO: NOTE: using this query I get the error that the index_token1 has no attribute get - index_token1 is constructed using query2()
#test_query = "construct OR model" # TODO: NOTE: using this query I get the error that the key 'construct' is not found
# TODO: NOTE: this was just for testing the boolean retrieval since such queries are not given in queries.csv ?
bool_retrieval = BooleanRetrieval()
bool_retrieval.bool_search(test_query, inverted_index)
'''

#-------------------------------Similarity----------------------------------#

# calculate similarity and evaluation measures
measures = Measures()
sim_result = measures.sim(sample_query, tokenizer.read_in(list_file_paths[1]))
print("Similarity: ", sim_result, "\n")

sim_result1 = measures.sim(query_list[0], tokenizer.read_in("files/184.txt"))
sim_result2 = measures.sim(query_list[0], tokenizer.read_in("files/29.txt"))
sim_result3 = measures.sim(query_list[0], tokenizer.read_in("files/31.txt"))
sim_result4 = measures.sim(query_list[0], tokenizer.read_in("files/12.txt"))
sim_result5 = measures.sim(query_list[0], tokenizer.read_in("files/51.txt"))
print("Similarity1: ", sim_result1)
print("Similarity2: ", sim_result2)
print("Similarity3: ", sim_result3)
print("Similarity4: ", sim_result4)
print("Similarity5: ", sim_result5)

# TODO: unsure about the parameters for precision and recall - i think we need the overall set of postings for the corresponding document together with the set of postings specific for our query
relevant_docs = [] # TODO: parameter in queries csv
retrieved_relevant_docs = [] # TODO: count of retrieved postings with relation to the actually relevant docs out of queries csv
total_retrieved_docs = [] # TODO: count of retrieved postings
recall_measure = measures.recall(1, [])
print("Recall: ", recall_measure)
precision_measure = measures.precision(1, [])
print("Precision:", precision_measure)
#f1_score = measures.f1score(recall_measure, precision_measure)
f1_score = measures.f1score(1, [])
print("F1-score: ", f1_score, "\n")

print("Number of relevant documents:")
print("Query 1:", helper.get_relevent_docs(1))
print("Query 2:", helper.get_relevent_docs(2))
print("Query 3:", helper.get_relevent_docs(3))
print("Query 4:", helper.get_relevent_docs(4))
print("Query 5:", helper.get_relevent_docs(5))
print()

#-----------------------Measurements-----------------------#


row_num1 = 4
query1 = query_list[row_num1-1]

print("Amount documents:", len(measures.documents))
sim_query1 = measures.query_sim(query1)

# https://stackoverflow.com/questions/8459231/sort-tuples-based-on-second-parameter
sim_query1.sort(key=operator.itemgetter(1), reverse=True)
n = len(sim_query1)

sim_query1_cut = [sim_query1[i] for i in range(20) if i < n]
#print("Hi:", sim_query1_cut)

print("Similarities for query", row_num1, ":")
for sim in sim_query1_cut:
    print(sim)

print()
print("Precision for query", row_num1, ":", measures.precision(row_num1, sim_query1_cut))
print("Recall    for query", row_num1, ":", measures.recall(row_num1, sim_query1_cut))
print("F1 Score  for query", row_num1, ":", measures.f1score(row_num1, sim_query1_cut))




print("\n-----------------------------------@k-----------------------------------------\n")

#--------------------------@k------------------------------#

k_range = 1


for row_num in range(1, 5):
    query = query_list[row_num-1]
    print(query)
    similarities = measures.query_sim(query)
    similarities.sort(key=operator.itemgetter(1), reverse=True)
    n = len(similarities)

    filePrecision = open("./report/graphs/Precision" + str(row_num) + ".csv", "w")
    fileRecall    = open("./report/graphs/Recall" + str(row_num) + ".csv", "w")
    fileF1Score   = open("./report/graphs/F1Score" + str(row_num) + ".csv", "w")

    for k in range(0, 1401, k_range):
        if k == 0:
            k = 1

        similarities_cut = [similarities[i] for i in range(k) if i < n]
        precision = measures.precision(row_num, similarities_cut)
        recall    = measures.recall(row_num, similarities_cut)
        f1score   = measures.f1score_precalculated(precision, recall)

        #print("Precision", k, ":", precision)
        #print("Recall   ", k, ":", recall)
        #print("F1 Score ", k, ":", f1score, "\n")

        filePrecision.write(str(k) + ", " + str(precision) + "\n")
        fileRecall.write(str(k) + ", " + str(recall) + "\n")
        fileF1Score.write(str(k) + ", " + str(f1score) + "\n")

    filePrecision.close()
    fileRecall.close()
    fileF1Score.close()


helper.get_term_doc_matrix(helper.get_term_doc_vector(), sample_query)


# NOTE: below is for testing cosine similarity results
#result = vsm.calc_cosine_similarity(helper.get_term_doc_matrix(helper.get_term_doc_vector(), sample_query))
#for i in result:
#    print(i)

cosine_similarity_result_list = vsm.calc_cosine_similarity(helper.get_term_doc_matrix(helper.get_term_doc_vector(), query_list[0]))
c_sim_result1 = cosine_similarity_result_list[184]
c_sim_result2 = cosine_similarity_result_list[29]
c_sim_result3 = cosine_similarity_result_list[31]
c_sim_result4 = cosine_similarity_result_list[12]
c_sim_result5 = cosine_similarity_result_list[51]
print("Cosine Similarity1: ", c_sim_result1)
print("Cosine Similarity2: ", c_sim_result2)
print("Cosine Similarity3: ", c_sim_result3)
print("Cosine Similarity4: ", c_sim_result4)
print("Cosine Similarity5: ", c_sim_result5)
