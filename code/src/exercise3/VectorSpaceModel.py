from code.src.exercise2.Helper import Helper
import math
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# NOTE: look here https://www.datasciencecentral.com/profiles/blogs/information-retrieval-document-search-using-vector-space-model-in for more information on VSM
class VectorSpaceModel:

    def __init__(self):
        self.helper = Helper()

    # given the documents body, this function calculates the term frequency - inverse document frequency (tf-idf)
    def calc_tf_idf(self, query):
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

        tfidf_list = []
        tfidf_entry = []
        for term in term_doc_matrix:
            i = 0
            for e in term:
                tfidf_entry.append(term[i]*idf_list[i])
                i+=1
            tfidf_list.append(tfidf_entry)

        return tfidf_list


    # TODO: calculate cosine similarity
    # given the term document matrix
    # this function returns the cosine similarity of these vectors
    # calculate the similarity score between each document vector and the query term vector by applying cosine similarity
    def calc_cosine_similarity(self, tfidf_matrix):
        query_vec = tfidf_matrix[-1]

        sim_value_list = []
        for tfidf_entry in tfidf_matrix[0:len(tfidf_matrix)]:
            if not (np.linalg.norm(tfidf_entry)*np.linalg.norm(query_vec))==0:
                sim_value = np.dot(tfidf_entry, query_vec)/(np.linalg.norm(tfidf_entry)*np.linalg.norm(query_vec))
                sim_value_list.append(sim_value)
            else:
                sim_value_list.append(0)

        return sim_value_list