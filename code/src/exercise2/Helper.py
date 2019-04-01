import csv
import json
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

    def load_json_to_dict(self):
        json_path = abspath("../../../resources/cranfield-data-list.json")
        with open(json_path, 'r') as f:
            cranfield_dict = json.load(f)

        document_filenames_dict = {}
        for cranfield in cranfield_dict:
            doc_id = cranfield['id']
            doc_txt = "/files/%d.txt" % (doc_id)
            document_filenames_dict[doc_id] = doc_txt

        return document_filenames_dict


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
