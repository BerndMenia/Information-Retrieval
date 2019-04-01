import csv
import json
from os.path import abspath
from code.src.exercise2.QueryParser import QueryParser
from code.src.exercise1.Tokenizer import Tokenizer


class Helper:
    def __init__(self):
        self.query_parser=QueryParser()

    def get_documents(self):
        document_list = []
        path = "/files/"

        for i in range(1,1401):
            f = "%d.txt" % (i)
            doc = path+f
            document_list.append(doc)

        return document_list

    def load_documents(self):
        document_paths = self.get_documents()
        tokenizer = Tokenizer()
        return [tokenizer.read_in(document_path) for document_path in document_paths]

    def get_sample_queries(self):
        file_path = abspath("../../../resources/queries.csv")

        query_list = []

        with open(file_path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            i=0
            for row in readCSV:
                query_list.append(row[i])

        return query_list

    # return a dictionary containing the word vector representation for each document
    # document_dict = { document-id: [word1, word2, word3,...]
    # note that the document content was preprocessed before creating the word vector
    def get_term_doc_vector(self):
        json_path = abspath("../../../resources/cranfield-data-list.json")
        with open(json_path, 'r') as f:
            cranfield_dict = json.load(f)

        document_dict = {}
        for cranfield in cranfield_dict:
            doc_id = cranfield['id']
            doc_body = cranfield['body']
            doc_body = self.query_parser.parse_query(doc_body)
            document_dict[doc_id] = doc_body

        return document_dict

    def get_term_doc_matrix_rows(self, doc_dict, query):
        query = self.query_parser.parse_query(query)
        list_word_vectors = []
        for doc_id, doc_body in doc_dict.items():
            list_word_vectors.append(doc_body)
        list_word_vectors.append(query)

        list_matrix_rows = []
        for vec in list_word_vectors:
            list_matrix_rows = list(set().union(list_matrix_rows, vec))

        return list_matrix_rows

    # return a matrix with column-count=document-count and row-count=unique-terms-count-of-all-documents
    # the matrix is filled with 0 and 1
    # 0 for each term not contained in the corresponding document
    # 1 for each term contained in the corresponding document
    # the last column contains the corresponding presentation for the query string given as parameter
    # TODO: this function is very time consuming... - we could save this matrix for speedup
    def get_term_doc_matrix(self, doc_dict, query):
        query = self.query_parser.parse_query(query)
        list_word_vectors = []
        for doc_id, doc_body in doc_dict.items():
            list_word_vectors.append(doc_body)
        #print("len before query add: ", len(list_word_vectors))
        list_word_vectors.append(query)
        #print("len after query add: ", len(list_word_vectors))

        list_matrix_rows = []
        for vec in list_word_vectors:
            list_matrix_rows = list(set().union(list_matrix_rows, vec))

        # matrix = [[0]*columns for x in range(rows)]
        matrix = [[0]*len(list_word_vectors) for x in range(len(list_matrix_rows))]
        row=0
        for term in list_matrix_rows:
            col=0
            for word_vec in list_word_vectors:
                for w in word_vec:
                    if w == term:
                        matrix[row][col] = 1
                col+=1
            row+=1

        #print("matrix rows: ", len(matrix))
        #print("matrix columns for first row: ", len(matrix[0]))

        return matrix

    # ----------------------------------------- MEASURES ----------------------------------------- #

    def get_relevent_docs(self, row_num):
        file_path = abspath("../../../resources/queries.csv")

        with open(file_path) as csvfile:
            read_csv = csv.reader(csvfile, delimiter=',')
            list_csv = list(read_csv)

            if 0 < row_num < len(list_csv):
                n = len(list_csv[row_num-1])

                if (n - 1) % 2 == 0:
                    return (n - 1) // 2

        # Return -1 if an error occurred.
        return -1

    def get_relevant_retrieved_docs(self):
        return

    def get_total_retrieved_docs(self):
        return
