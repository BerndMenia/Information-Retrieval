from code.src.exercise2.QueryParser import QueryParser

class BooleanRetrieval:
    def __init__(self):
        self.query_parser = QueryParser()

    # [word, [(document_count, position)] ]
    ''' TODO
    locate first word
    retrieve postings from first word
    locate second
    retrieve postings from second word
    intersect posting lists
    '''
    def bool_search(self, query, inverted_index): # note: by now we can only process simple bool queries, containing only one binary bool operation

        # split up query to get word1, bool op, word 2
        query_string_list = query.split(' ')
        print(query_string_list)
        token1 = query_string_list[0]
        bool_op = query_string_list[1]
        token2 = query_string_list[2]

        # send word1 and word2 to query preprocessor
        token1 = self.query_parser.parse_query(token1)
        token2 = self.query_parser.parse_query(token2)
        print("parsed query tokens")
        print(token1, token2)

        # get index entry for word1 and word2
        index_token1 = inverted_index.query(token1[0])
        index_token2 = inverted_index.query(token2[0])
        print("index tok1")
        print(index_token1)
        print("index tok2")
        print(index_token2)

        # get posting lists for word1 and word2
        entry_token1 = index_token1[1]
        postings_token1 = [i[0] for i in entry_token1]
        postings_token1 = list(dict.fromkeys(postings_token1))
        print(postings_token1)

        entry_token2 = index_token2[1]
        postings_token2 = [i[0] for i in entry_token2]
        postings_token2 = list(dict.fromkeys(postings_token2))
        print(postings_token2)

        # call bool op with posting lists
        if bool_op == 'AND':
            print(self.bool_and(postings_token1, postings_token2))
        elif bool_op == 'OR':
            print(self.bool_or(postings_token1, postings_token2))
        elif bool_op == 'NOT':
            print("op NOT called")


    def bool_and(self, postings1, postings2):
        result = []
        for i in postings1:
            for j in postings2:
                if i == j:
                    result.append(i)

        return result

    def bool_or(self, postings1, postings2):
        result = []
        for i in postings1:
            result.append(i)
        for j in postings2:
            result.append(j)

        return result

    def bool_not(self, postings1, postings2):
        result = []
        return result