from gensim.models.doc2vec import Doc2Vec
from code.src.exercise5.kmeans import kmeans

########## load doc2ved model ##########
model = Doc2Vec.load("vectors/doc2vec.bin")

########## kmeans ##########
cluster = kmeans()
cluster.kmeans_cluster(model.docvecs.doctag_syn0)
