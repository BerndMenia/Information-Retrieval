import bisect
import operator

from code.src.exercise2.QueryParser import QueryParser
from code.src.exercise2.Helper import Helper


class Measures:

    def __init__(self):
        self.query_parser = QueryParser()
        self.helper = Helper()
        self.documents = self.helper.load_documents()


    def sim(self, query, document):
        query_tokens = self.query_parser.parse_query(query)
        document_tokens = self.query_parser.parse_query(document)
        count = 0

        for query_token in query_tokens:
            if query_token in document_tokens:
                count += 1

        return count / len(query_tokens)


    # We regard every query with a sim value of >= 33.3% as relevant.
    def sim_cutoff(self, similarities):
        similarities.sort(key=operator.itemgetter(1), reverse=True)
        similarities_new = []

        for document_id, sim in similarities:
            if sim >= 1/3:
                similarities_new.append( (document_id, sim) )
            else:
                break

        return similarities_new


    def relevant_intersect_retrieved(self, row_num, similarities):
        if not len(similarities) > 0:
            return -1

        relevant_document_ids = self.helper.get_relevant_docs_ids(row_num)
        print("Relevant document ids:", relevant_document_ids)

        similarities_cutoff = self.sim_cutoff(similarities)
        print("Cutoff:", similarities_cutoff)

        relevant_documents = 0

        for document_id,_ in similarities_cutoff:
            if document_id in relevant_document_ids:
                relevant_documents += 1

        return relevant_documents


    # Recall = No. of relevant documents retrieved / No. of total relevant documents
    def recall(self, row_num, similarities):
        if not len(similarities) > 0:
            return -1

        intersection = self.relevant_intersect_retrieved(row_num, similarities)
        amount_relevant_docs = self.helper.get_relevent_docs(row_num)
        return  intersection / amount_relevant_docs


    # Precision = No. of relevant documents retrieved / No. of total documents retrieved
    def precision(self, row_num, similarities):
        if not len(similarities) > 0:
            return -1

        intersection = self.relevant_intersect_retrieved(row_num, similarities)
        return intersection / len(similarities)


    # F - Score = 2 * Precision * Recall / (Precision + Recall)
    def f1score(self, row_num, similarities):
        precision = self.precision(row_num, similarities)
        recall    = self.recall(row_num, similarities)
        return 2 * precision * recall / (precision + recall)


    def query_sim(self, query):
        similarities = []

        for i in range(1, len(self.documents)+1):
            sim = self.sim(query, self.documents[i-1])
            similarities.append( (i, sim) )

        return similarities

