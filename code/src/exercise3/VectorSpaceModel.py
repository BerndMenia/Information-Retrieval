from code.src.exercise2.Helper import Helper
from code.src.exercise2.InvertedIndex import InvertedIndex
import math
from sklearn.metrics.pairwise import cosine_similarity
from itertools import groupby

# NOTE: look here https://www.datasciencecentral.com/profiles/blogs/information-retrieval-document-search-using-vector-space-model-in for more information on VSM
class VectorSpaceModel:

    def __init__(self):
        self.helper = Helper()
        #self.indexer = InvertedIndex()

    # given the documents body, this function calculates the term frequency - inverse document frequency (tf-idf)
    def calc_tf_idf(self, query, indexer):
        total_num_docs = 1400
        all_docs_dict = self.helper.get_term_doc_vector()

        term_doc_matrix = self.helper.get_term_doc_matrix(all_docs_dict, query)

        # this list contains the document frequency for each term (excluding the query)
        df_list = []
        count=1
        for term in term_doc_matrix:
            if count == len(term_doc_matrix):
                break
            df_list.append(sum(term))
            count += 1

        idf_list = []
        for df in df_list:
            idf_list.append(math.log(total_num_docs/df))

        # TODO: calculate number of times a term occurs in a document in order to calculate tf-idf (tf X idf)
        tf_list = []
        list_words = []
        for doc_id, doc_body in all_docs_dict.items():
            list_words.append(doc_body)

        postings_list = []
        for words in list_words:
            for w in words:
                all_postings = indexer.query_without_stem(w) # TODO: fix mysteries in query2()
                postings = [i[0] for i in all_postings]
                posting_frequencies = [len(list(group)) for key, group in groupby(postings)]
                #postings = list(dict.fromkeys(postings))
                #postings_list.append(postings)
                #print("posting freq of ", w, ": ", posting_frequencies)



    # TODO: calculate cosine similarity
    # given the tf-idf vector representation for a document and the query
    # this function returns the cosine similarity of these vectors
    # calculate the similarity score between each document vector and the query term vector by applying cosine similarity
    def calc_cosine_similarity(self, doc_vec, query_vec):
        return cosine_similarity(doc_vec, query_vec)