import numpy as np
import re
import nltk
from sklearn.datasets import load_files
import pickle
from nltk.corpus import stopwords
from os.path import abspath


# import the dataset
path_traindata = abspath("../../../resources/C50train")
path_testdata = abspath("../../../resources/C50test")

authorship_traindata = load_files(path_traindata)
authorship_testdata = load_files(path_testdata)

# data is loaded into X, target categories are stored in y
# X is a list of 2500 string elements where each element corresponds to an author's papers
# y is a numpy array of 2500 entries, the numbers are 1-50 since we have 50 authors
X_train, y_train = authorship_traindata.data, authorship_traindata.target
X_test, y_test = authorship_testdata.data, authorship_testdata.target

