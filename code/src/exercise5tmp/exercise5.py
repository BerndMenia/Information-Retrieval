from gensim.models import Word2Vec
from nltk.corpus import brown, movie_reviews, treebank

# https://streamhacker.com/2014/12/29/word2vec-nltk/


b = Word2Vec(brown.sents())
mr = Word2Vec(movie_reviews.sents())
t = Word2Vec(treebank.sents())

print("money")
print("Brown:", b.most_similar('money', topn=5))
# [('pay', 0.6832243204116821), ('ready', 0.6152011156082153), ('try', 0.5845392942428589), ('care', 0.5826011896133423), ('move', 0.5752171277999878)]

print("MovRev:", mr.most_similar('money', topn=5))
# [('unstoppable', 0.6900672316551208), ('pain', 0.6289106607437134), ('obtain', 0.62665855884552), ('jail', 0.6140228509902954), ('patients', 0.6089504957199097)]

print("Treebank:", t.most_similar('money', topn=5), "\n")
# [('short-term', 0.9459682106971741), ('-LCB-', 0.9449775218963623), ('rights', 0.9442864656448364), ('interested', 0.9430986642837524), ('national', 0.9396077990531921)]


print("great")
print("Brown:", b.most_similar('great', topn=5))
# [('new', 0.6999611854553223), ('experience', 0.6718623042106628), ('social', 0.6702290177345276), ('group', 0.6684836149215698), ('life', 0.6667487025260925)]

print("MovRev:", mr.most_similar('great', topn=5))
#[('wonderful', 0.7548679113388062), ('good', 0.6538234949111938), ('strong', 0.6523671746253967), ('phenomenal', 0.6296845078468323), ('fine', 0.5932096242904663)]

print("Treebank:", t.most_similar('great', topn=5), "\n")
# [('won', 0.9452997446060181), ('set', 0.9445616006851196), ('target', 0.9342271089553833), ('received', 0.9333916306495667), ('long', 0.9224691390991211)]


print("company")
print("Brown:", b.most_similar('company', topn=5))
# [('industry', 0.6164317727088928), ('technical', 0.6059585809707642), ('orthodontist', 0.5982754826545715), ('foamed', 0.5929019451141357), ('trail', 0.5763031840324402)]

print("MovRev:", mr.most_similar('company', topn=5))
# [('colony', 0.6689200401306152), ('temple', 0.6546304225921631), ('arrival', 0.6497283577919006), ('army', 0.6339291334152222), ('planet', 0.6184555292129517)]

print("Treebank:", t.most_similar('company', topn=5))
# [('panel', 0.7949466705322266), ('Herald', 0.7674347162246704), ('Analysts', 0.7463694214820862), ('amendment', 0.7282689809799194), ('Treasury', 0.719698429107666)]