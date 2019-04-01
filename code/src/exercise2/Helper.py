import csv
from os.path import abspath

class Helper:
    def get_documents(self):
        document_list = []
        path = "/files/"

        for i in range(1,1401):
            f = "%d.txt" % (i)
            doc = path+f
            document_list.append(doc)

        return document_list

    def get_sample_queries(self):
        file_path = abspath("../../../resources/queries.csv")

        query_list = []

        with open(file_path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            i=0
            for row in readCSV:
                query_list.append(row[i])

        return query_list

    def get_relevent_docs(self, row_num):
        file_path = abspath("../../../resources/queries.csv")

        with open(file_path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            num_relevant_docs=0
            for row in readCSV:
                num_relevant_docs = len(row[row_num]-2)
                break

        return num_relevant_docs

    def get_relevant_retrieved_docs(self):
        return

    def get_total_retrieved_docs(self):
        return
