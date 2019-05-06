from os.path import abspath
from sklearn.datasets import load_files
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

# NOTE: the model is saved in code/src/exercise5/vectors/doc2vec.model

# NOTE: doc2vec is using two things when training the model, labels and the actual data (we take file names as labels)
# NOTE: doc2vec needs model training data in an LabeledSentence iterator object


########## load dataset and convert it to tagged docs ##########

path_traindata = abspath("../../../resources/C50train")
#path_testdata = abspath("../../../resources/C50test")
authorship_traindata = load_files(path_traindata)
#authorship_testdata = load_files(path_testdata)

raw_traindata = authorship_traindata.data
#raw_testdata = authorship_testdata.data

fileid_traindata = authorship_traindata.filenames
#fileid_testdata = authorship_testdata.filenames

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

doc2vec_model.save("vectors/doc2vec.model")


########## test the model ##########
# NOTE: to test the model enter any word which is within our trained vocabulary
print(doc2vec_model.most_similar('Czech'))

