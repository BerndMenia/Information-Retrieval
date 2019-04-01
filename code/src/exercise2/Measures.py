import bisect

from code.src.exercise2.QueryParser import QueryParser
from code.src.exercise2.Helper import Helper


class Measures:
    def __init__(self):
        self.query_parser = QueryParser()
        self.documents = Helper().load_documents()

    def sim(self, query, document):
        query_tokens = self.query_parser.parse_query(query)
        document_tokens = self.query_parser.parse_query(document)
        count = 0

        for query_token in query_tokens:
            if query_token in document_tokens:
                count += 1

        return count / len(query_tokens)

    # Recall = No. of relevant documents retrieved / No. of total relevant documents
    def recall(self, total_relevant_documents, relevant_documents):
        if len(total_relevant_documents) > 0:
            return len(relevant_documents) / len(total_relevant_documents)
        else:
            return 0

    # Precision = No. of relevant documents retrieved / No. of total documents retrieved
    def precision(self, all_documents, relevant_documents):
        if len(all_documents) > 0:
            return len(relevant_documents) / len(all_documents)
        else:
            return 0

    # F - Score = 2 * Precision * Recall / (Precision + Recall)
    def f1score(self, recall_score, precision_score):
        if(precision_score+recall_score)>0:
            return 2*precision_score*recall_score / (precision_score+recall_score)
        else:
            return 0

    def query_sim(self, query):
        similarities = []

        for i in range(1, len(self.documents)+1):
            sim = self.sim(query, self.documents[i-1])
            similarities.append( (i, sim) )

        return similarities
