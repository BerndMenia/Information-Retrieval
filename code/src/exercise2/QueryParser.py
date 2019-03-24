from code.src.exercise1.Tokenizer import Tokenizer

class QueryParser:
    def __init__(self):
        self.tokenizer = Tokenizer()

    def parse_query(self, query_string):
        # tokenize query
        tokens = self.tokenizer.tokenize_text(query_string)

        # remove punctuation and stopwords
        prep_tokens = self.tokenizer.remove_punctuation(tokens)
        tok_query = self.tokenizer.remove_stopwords(prep_tokens)

        # stem query
        stem_query = self.tokenizer.stem_words(tok_query)

        # return preprocessed query
        return stem_query



