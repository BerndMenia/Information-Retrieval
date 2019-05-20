"""
Differences of the 4 algorithms (from the official documentation):

KNNBaseline:   A basic collaborative filtering algorithm taking into account a *baseline* rating.

KNNBasic:      A basic collaborative filtering algorithm.

KNNWithMean:   A basic collaborative filtering algorithm, taking into account the mean ratings of each user.

KNNWithZScore: A basic collaborative filtering algorithm, taking into account the z-score normalization of each user.

---------------------------------------------------------------------------------------------------------------------

Parameters for the creation of the different algorithms (from the official documentation):

k(int):
    The (max) number of neighbors to take into account for aggregation
    (see :ref:`this note <actual_k_note>`). Default is ``40``.

min_k(int):
    The minimum number of neighbors to take into account for
    aggregation. If there are not enough neighbors, the prediction is
    set the the global mean of all ratings. Default is ``1``.

sim_options(dict):
    A dictionary of options for the similarity measure.
    See :ref:`similarity_measures_configuration` for accepted options.

bsl_options(dict) (only for KNNBaseLine):
    A dictionary of options for the baseline estimates computation.
    See :ref:`baseline_estimates_configuration` for accepted options.

verbose(bool):
    Whether to print trace messages of bias estimation,
    similarity, etc.  Default is True.

---------------------------------------------------------------------------------------------------------------------

Parameters for the prediction of the KNN based algorithms:

uid     -> The user id on which the prediction shall be made. Make sure that uid exists in the database, otherwise the
           algorithm will not be able to predict (it will not fail however, just output a message).

iid     -> The item id (movie) that gets used in combination with the uid to clearly identify the uid iid pair.
           Just like for uid make sure that iid exists in the database or the algorithm will not produce meaningful output.

r_ui    -> The actual rating that user uid gave for movie iid. Can be used to compare the predicted result.
           Default is None

clip    -> True / False: From the documentation: Whether to clip the estimation into the rating scale.
           For example, if :math:`\\hat{r}_{ui}` is :math:`5.5` while the rating scale is :math:`[1, 5]`,
           then :math:`\\hat{r}_{ui}` is set to :math:`5`. Same goes if :math:`\\hat{r}_{ui} < 1`.
           Default is ``True``.

verbose -> True / False: Iff set to True then the resulting prediction with uid, iid, r_uid and est gets printed.
           Default is False.
"""


from surprise import KNNBaseline
from surprise import KNNBasic
from surprise import KNNWithMeans
from surprise import KNNWithZScore
from surprise import Dataset


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

r_ui1 = 4
r_ui2 = 4
r_ui3 = 1
r_ui4 = 3

verboseFlag = True

# get a prediction for specific users and items.
print("KNNBaseLine:")
predBaseLine = algoBaseLine.predict(uid1, iid1, r_ui = r_ui1, verbose = verboseFlag)
predBaseLine = algoBaseLine.predict(uid2, iid2, r_ui = r_ui2, verbose = verboseFlag)
predBaseLine = algoBaseLine.predict(uid3, iid3, r_ui = r_ui3, verbose = verboseFlag)
predBaseLine = algoBaseLine.predict(uid4, iid4, r_ui = r_ui4, verbose = verboseFlag)

print("\nKNNBasic:")
predBasic = algoBasic.predict(uid1, iid1, r_ui = r_ui1, verbose = verboseFlag)
predBasic = algoBasic.predict(uid2, iid2, r_ui = r_ui2, verbose = verboseFlag)
predBasic = algoBasic.predict(uid3, iid3, r_ui = r_ui3, verbose = verboseFlag)
predBasic = algoBasic.predict(uid4, iid4, r_ui = r_ui4, verbose = verboseFlag)

print("\nKNNWithMeans:")
predWithMeans = algoWithMeans.predict(uid1, iid1, r_ui = r_ui1, verbose = verboseFlag)
predWithMeans = algoWithMeans.predict(uid2, iid2, r_ui = r_ui2, verbose = verboseFlag)
predWithMeans = algoWithMeans.predict(uid3, iid3, r_ui = r_ui3, verbose = verboseFlag)
predWithMeans = algoWithMeans.predict(uid4, iid4, r_ui = r_ui4, verbose = verboseFlag)

print("\nKNNWithZScore:")
predWithZScore = algoWithZScore.predict(uid1, iid1, r_ui = r_ui1, verbose = verboseFlag)
predWithZScore = algoWithZScore.predict(uid2, iid2, r_ui = r_ui2, verbose = verboseFlag)
predWithZScore = algoWithZScore.predict(uid3, iid3, r_ui = r_ui3, verbose = verboseFlag)
predWithZScore = algoWithZScore.predict(uid4, iid4, r_ui = r_ui4, verbose = verboseFlag)