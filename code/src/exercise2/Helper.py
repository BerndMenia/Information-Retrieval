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
