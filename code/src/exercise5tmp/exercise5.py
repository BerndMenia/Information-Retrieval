from gensim.models import Word2Vec
from nltk.corpus import brown, movie_reviews, treebank

# https://streamhacker.com/2014/12/29/word2vec-nltk/


b = Word2Vec(brown.sents())
mr = Word2Vec(movie_reviews.sents())
t = Word2Vec(treebank.sents())

money = "money"
great = "great"
company = "company"
france = "France"

print("money")
print("Brown:", b.most_similar(money, topn=5))
# Brown: [('care', 0.9203847646713257), ('job', 0.9120237827301025), ('trouble', 0.9073654413223267), ('chance', 0.8856830596923828), ('getting', 0.8842267394065857)]

print("Brown2:", b.most_similar("Money", topn=5))

print("MovRev:", mr.most_similar(money, topn=5))
# MovRev: [('him', 0.7500324249267578), ('home', 0.7491098046302795), ('chance', 0.7342701554298401), ('trouble', 0.7290754318237305), ('attention', 0.7274935841560364)]

print("Treebank:", t.most_similar(money, topn=5), "\n")
# Treebank: [('traders', 0.9998961687088013), ('new', 0.9998897314071655), ('even', 0.9998819828033447), ('since', 0.9998773336410522), ('into', 0.9998763799667358)]


print("great")
print("Brown:", b.most_similar(great, topn=5))
# Brown: [('common', 0.8723435401916504), ('experience', 0.856053352355957), ('limited', 0.808241069316864), ('part', 0.8045881390571594), ('sense', 0.8003120422363281)]

print("MovRev:", mr.most_similar(great, topn=5))
# MovRev: [('wonderful', 0.8285278081893921), ('nice', 0.823311448097229), ('decent', 0.8028441071510315), ('good', 0.7920763492584229), ('strong', 0.7473284006118774)]

print("Treebank:", t.most_similar(great, topn=5), "\n")
# Treebank: [('market', 0.999237596988678), ('because', 0.999198317527771), ('what', 0.9991917014122009), ('time', 0.9991852641105652), ('The', 0.9991787672042847)]


print("company")
print("Brown:", b.most_similar(company, topn=5))
# Brown: [('conviction', 0.9396542310714722), ('decision', 0.9332501888275146), ('heritage', 0.931989312171936), ('profession', 0.9315740466117859), ('party', 0.9282490015029907)]

print("MovRev:", mr.most_similar(company, topn=5))
# MovRev: [('army', 0.9050424695014954), ('band', 0.8675254583358765), ('plans', 0.8508973121643066), ('church', 0.8501453399658203), ('murdered', 0.8488762974739075)]

print("Treebank:", t.most_similar(company, topn=5), "\n")
# Treebank: [('is', 0.9996266961097717), ('they', 0.9995608925819397), ('*T*-3', 0.9995567798614502), ('does', 0.9994494915008545), ('have', 0.9993588924407959)]


print("France")
print("Brown:", b.most_similar(france, topn=5))
#

print("MovRev:", mr.most_similar(france, topn=5))
#

print("Treebank:", t.most_similar(france, topn=5))
#