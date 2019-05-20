from surprise import KNNBaseline
from surprise import KNNBasic
from surprise import KNNWithMeans
from surprise import KNNWithZScore
from surprise import Dataset


'''
Parameters for the KNN based algorithms: 
uid     -> The user id on which the prediction shall be made. Make sure that uid exists in the database, otherwise the 
           algorithm will not be able to predict (it will not fail however, just output a message). 
iid     -> The item id (movie) that gets used in combination with the uid to clearly identify the uid iid pair. 
           Just like for uid make sure that iid exists in the database or the algorithm will not produce meaningful output. 
r_ui    -> The actual rating that user uid gave for movie iid. Can be used to compare the predicted result. 
           Default is None
clip    -> True / False: 
verbose -> True / False: Iff set to True then the resulting prediction with uid, iid, r_uid and est gets printed. 
           Default is False. 
'''

# Load the movielens-100k dataset
data = Dataset.load_builtin('ml-100k')

# Retrieve the trainset.
trainset = data.build_full_trainset()

# Create instances of the 4 KNN based algorithms
algoBaseLine = KNNBaseline()
algoBasic = KNNBasic()
algoWithMeans = KNNWithMeans()
algoWithZScore = KNNWithZScore()

# Train the 4 algorithms on the training set
algoBaseLine.fit(trainset)
algoBasic.fit(trainset)
algoWithMeans.fit(trainset)
algoWithZScore.fit(trainset)

uid1 = str(196)  # raw user id (as in the ratings file). They are **strings**!
uid2 = str(73)
uid3 = str(423)
uid4 = str(504)

iid1 = str(306)  # raw item id (as in the ratings file). They are **strings**!
iid2 = str(514)
iid3 = str(977)
iid4 = str(370)

# get a prediction for specific users and items.
print("KNNBaseLine:")
predBaseLine = algoBaseLine.predict(uid1, iid1, r_ui=4, verbose=True)
predBaseLine = algoBaseLine.predict(uid2, iid2, r_ui=4, verbose=True)
predBaseLine = algoBaseLine.predict(uid3, iid3, r_ui=1, verbose=True)
predBaseLine = algoBaseLine.predict(uid4, iid4, r_ui=3, verbose=True)

print("\nKNNBasic:")
predBasic = algoBasic.predict(uid1, iid1, r_ui=4, verbose=True)
predBasic = algoBasic.predict(uid2, iid2, r_ui=4, verbose=True)
predBasic = algoBasic.predict(uid3, iid3, r_ui=1, verbose=True)
predBasic = algoBasic.predict(uid4, iid4, r_ui=3, verbose=True)

print("\nKNNWithMeans:")
predWithMeans = algoWithMeans.predict(uid1, iid1, r_ui=4, verbose=True)
predWithMeans = algoWithMeans.predict(uid2, iid2, r_ui=4, verbose=True)
predWithMeans = algoWithMeans.predict(uid3, iid3, r_ui=1, verbose=True)
predWithMeans = algoWithMeans.predict(uid4, iid4, r_ui=3, verbose=True)

print("\nKNNWithZScore:")
predWithZScore = algoWithZScore.predict(uid1, iid1, r_ui=4, verbose=True)
predWithZScore = algoWithZScore.predict(uid2, iid2, r_ui=4, verbose=True)
predWithZScore = algoWithZScore.predict(uid3, iid3, r_ui=1, verbose=True)
predWithZScore = algoWithZScore.predict(uid4, iid4, r_ui=3, verbose=True)