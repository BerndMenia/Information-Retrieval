from code.src.exercise2.QueryParser import QueryParser

class BooleanRetrieval:
    def __init__(self):
        self.query_parser = QueryParser()

    '''
    TODO
    push query string on stack
    pop an process step by step
    '''

    # NOTE: by now we can only process simple bool queries, containing only one binary bool operation and the ones of form "a NOT b"
    def bool_search(self, query, inverted_index):
        # split up query to get word1, bool op, word 2
        if query:
            query_string_list = query.split(' ')
            print(query_string_list)

            if len(query_string_list) == 3:
                token1 = query_string_list[0]
                bool_op = query_string_list[1]
                token2 = query_string_list[2]

                # send word1 and word2 to query preprocessor
                token1 = self.query_parser.parse_query(token1)
                token2 = self.query_parser.parse_query(token2)

                # get index entry for word1 and word2
                index_token1 = inverted_index.query3(token1[0])
                if not index_token1:
                    index_token1 = []
                index_token2 = inverted_index.query3(token2[0])
                if not index_token2:
                    index_token2 = []

                if index_token1 and index_token2:
                    # entry_token1 and 2 are not used anymore --> index_token1 and 2
                    # can be used directly instead I think.
                    entry_token1 = index_token1
                    entry_token2 = index_token2

                    # get posting lists for word1 and word2
                    #entry_token1 = index_token1[1]
                    postings_token1 = [i[0] for i in entry_token1]
                    postings_token1 = list(dict.fromkeys(postings_token1))
                    print("postings of "+query_string_list[0])
                    print(postings_token1)

                    #entry_token2 = index_token2[1]
                    postings_token2 = [i[0] for i in entry_token2]
                    postings_token2 = list(dict.fromkeys(postings_token2))
                    print("postings of "+query_string_list[2])
                    print(postings_token2)
                elif index_token1 and not index_token2:
                    entry_token1 = index_token1[1]
                    postings_token1 = [i[0] for i in entry_token1]
                    postings_token1 = list(dict.fromkeys(postings_token1))
                    print("postings of " + query_string_list[0])
                    print(postings_token1)

                    postings_token2 = []
                    print("postings of " + query_string_list[2])
                    print(postings_token2)

                elif index_token2 and not index_token1:
                    postings_token1 = []
                    print("postings of " + query_string_list[0])
                    print(postings_token1)

                    entry_token2 = index_token2[1]
                    postings_token2 = [i[0] for i in entry_token2]
                    postings_token2 = list(dict.fromkeys(postings_token2))
                    print("postings of " + query_string_list[2])
                    print(postings_token2)

                # call bool op with posting lists
                if bool_op == 'AND':
                    print("result for AND")
                    print(self.bool_and(postings_token1, postings_token2))
                elif bool_op == 'OR':
                    print("result for OR")
                    print(self.bool_or(postings_token1, postings_token2))
                elif bool_op == 'NOT':
                    print("result for NOT")
                    print(self.bool_not(postings_token1, postings_token2))
            else:
                print("Error: only simple queries in the format of \"a AND b\" or \"a OR b\" or \"a NOT b\" are possible")


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
            if j not in result:
                result.append(j)

        return result

    def bool_not(self, postings1, postings2):
        result = []

        for i in postings1:
            if i in postings2:
                continue
            else:
                result.append(i)

        return result
