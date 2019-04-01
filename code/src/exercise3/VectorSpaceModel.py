from code.src.exercise2.Helper import Helper
import math

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

        # TODO: calculate number of times a term occurs in a document in order to calculate tf-idf (tf X idf)
        tf_list = []
        list_words = []
        for doc_id, doc_body in all_docs_dict.items():
            list_words.append(doc_body)


    # TODO: calculate cosine similarity
    def calc_cosine_similarity(self):
        return