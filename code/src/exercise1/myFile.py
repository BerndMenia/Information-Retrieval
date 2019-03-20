from os.path import abspath
from collections import Counter
from spacy.tokenizer import Tokenizer
from spacy.vocab import Vocab

import string
import spacy


# Stop words
STOP_WORDS = set(
    """
a about above across after afterwards again against all almost alone along
already also although always am among amongst amount an and another any anyhow
anyone anything anyway anywhere are around as at

back be became because become becomes becoming been before beforehand behind
being below beside besides between beyond both bottom but by

call can cannot ca could

did do does doing done down due during

each eight either eleven else elsewhere empty enough even ever every
everyone everything everywhere except

few fifteen fifty first five for former formerly forty four from front full
further

get give go

had has have he hence her here hereafter hereby herein hereupon hers herself
him himself his how however hundred

i if in indeed into is it its itself

keep

last latter latterly least less

just

made make many may me meanwhile might mine more moreover most mostly move much
must my myself

name namely neither never nevertheless next nine no nobody none noone nor not
nothing now nowhere n't

of off often on once one only onto or other others otherwise our ours ourselves
out over own

part per perhaps please put

quite

rather re really regarding

same say see seem seemed seeming seems serious several she should show side
since six sixty so some somehow someone something sometime sometimes somewhere
still such

take ten than that the their them themselves then thence there thereafter
thereby therefore therein thereupon these they third this those though three
through throughout thru thus to together too top toward towards twelve twenty
two

under until up unless upon us used using

various very very via was we well were what whatever when whence whenever where
whereafter whereas whereby wherein whereupon wherever whether which while
whither who whoever whole whom whose why will with within without would

yet you your yours yourself yourselves

'd 'll 'm 're 's 've
""".split()
)


def read_in(file_path):
    file_path = abspath("../../../" + file_path)
    file = open(file_path, "r")
    return file.read().lower()


def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))


def total_number_of_terms(text):
    return len(text.split())


def unique_terms(text):
    lst = []
    for s in text:
        if not s in lst:
            lst.append(s)
    return lst


def calculate_frequency(text):
    counts = Counter(text)  # Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
    counts.most_common()
    return counts


def get_top_50(frequency):
    lst = frequency.most_common(50)

    for i in range(len(lst)):
        term, amount = lst[i]
        lst[i] = (i + 1, term, amount)

    return lst


def count_stopwords(text):
    count = 0
    for s in text:
        if s in STOP_WORDS:
            count += 1
    return count


text = read_in("books/the_raven.txt")
# print(text)

text = remove_punctuation(text)
# print(text)

print("Total number of terms:", total_number_of_terms(text))

text_split = text.split()
print("Total number of unique terms:", len(unique_terms(text_split )))

frequency = calculate_frequency(text_split)
print("Frequencies:", frequency)

# Returns a list in contrast to calculate_frequency()!
frequency_top_50 = get_top_50(frequency)
print("Frequencies top 50:", frequency_top_50)

nlp = spacy.load('en_core_web_sm')
print("Stop words:", count_stopwords(text_split))

###############################################

doc = nlp(read_in("books/the_raven.txt"))
print("SpaCy length:", len(doc))


#tokenizer = Tokenizer(nlp.vocab)
#vocabulary = tokenizer.vocab
#vocabulary = vocabulary.__init__()

#vocab = Vocab(strings=read_in("books/the_raven.txt"))
#print("SpaCy length:", len(vocab))
#lexemes = vocab.lexemes_from_bytes()
