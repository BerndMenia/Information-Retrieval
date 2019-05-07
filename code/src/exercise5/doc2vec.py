from os.path import abspath
from sklearn.datasets import load_files
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize


# NOTE: this script runs doc2vec; the model is saved in code/src/exercise5/vectors/doc2vec.bin, which allows to call the saved model in clusterdocs.py, which saves time

# NOTE: doc2vec is using two things when training the model, labels and the actual data (we take file names as labels)
# NOTE: doc2vec needs model training data in an TaggedDocument iterator object


########## load dataset and convert it to tagged docs ##########

path_traindata = abspath("../../../resources/C50train")
authorship_traindata = load_files(path_traindata)

raw_traindata = authorship_traindata.data

fileid_traindata = authorship_traindata.filenames

'''
print(len(fileid_traindata))
print(fileid_traindata[0])
print(len(raw_traindata))
print(raw_traindata[0])
'''

print("finished loading data")


########## prepare data for training ##########

tagged_traindocs = []
i = 0
for doc in raw_traindata:
    tagged_traindocs.append(TaggedDocument(words=word_tokenize(doc.decode('ASCII')), tags=[fileid_traindata[i]]))
    i += 1

print("finished preparing tagged docs")
#print(tagged_traindocs)

########## train the model ##########

doc2vec_model = Doc2Vec(vector_size=300, min_count=2, workers=12, alpha=0.025, min_alpha=0.025, dm=1)
doc2vec_model.build_vocab(tagged_traindocs)

print("finished building doc2vec")


########## train the model - create vector ##########

#NOTE: we define the number of passes (epochs) as parameter for doc2vec training func, hence we don't need to loop, one call of train suffices and
doc2vec_model.train(tagged_traindocs, total_examples=doc2vec_model.corpus_count, epochs=doc2vec_model.iter)
# decrease the learning rate
#doc2vec_model.alpha -= 0.002
# fix the learning rate
#doc2vec_model.min_alpha = doc2vec_model.alpha

print("finished building doc2vec vector")

########## save vector ##########

doc2vec_model.save("vectors/doc2vec.bin")


########## test the model ##########
# NOTE: to test the model enter any sentence or the whole document content and get the most sim document (to get more than only 1 increase the topn parameter
search_string = word_tokenize("Australian resources and steel group The Broken Hill Pty Co (BHP) disappointed the share market on Friday with a weaker than expected second-quarter profit to post first-half net earnings of A$683 million before abnormals. BHP, whose shares have been hammered since its key markets in steel and copper turned sour six months ago, booked an abnormal gain of A$107 million to boost the bottom line for the six months to November 30, but investors were not impressed.")
infer_vector = doc2vec_model.infer_vector(search_string)
similar_documents = doc2vec_model.docvecs.most_similar([infer_vector], topn=1)
print(similar_documents)
