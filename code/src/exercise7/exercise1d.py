# For precision and recall
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from collections import defaultdict
from surprise.model_selection import KFold

from surprise import SVDpp
from surprise.model_selection import cross_validate

from os.path import abspath
from surprise import Dataset
from surprise import Reader

from surprise.model_selection import train_test_split

from surprise import KNNBaseline
from surprise import KNNBasic
from surprise import KNNWithMeans
from surprise import KNNWithZScore




# read the file with ratings changed to 1 (for 4 and 5 star ratings) and 0 (for 1-3 star ratings)
data_path = abspath("../../../resources/ml-100k/i.data")

# set rating range when loading in the dataset
reader = Reader(line_format='user item rating timestamp', sep='\t', rating_scale=(0,1))

# load the dataset
data = Dataset.load_from_file(data_path, reader=reader)

# sample random trainset and testset (choose testset of 25% of the ratings)
trainset, testset = train_test_split(data, test_size=.25)

# to get uid and iid contained in the training set
#print(trainset.ir)
# uids: 256, 60, 169, 22
#print(trainset.ur)
# iids: 50, 1223, 131, 395
# r: 2, 2, 1, 1


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

uid1 = str(256)  # raw user id (as in the ratings file). They are **strings**!
uid2 = str(60)
uid3 = str(169)
uid4 = str(22)

iid1 = str(50)  # raw item id (as in the ratings file). They are **strings**!
iid2 = str(1223)
iid3 = str(131)
iid4 = str(395)

r_ui1 = 1
r_ui2 = 0
r_ui3 = 1
r_ui4 = 0

verboseFlag = True

# get a prediction for specific users and items.
print("KNNBaseLine:")
predBaseLine1 = algoBaseLine.predict(uid1, iid1, r_ui = r_ui1, verbose = verboseFlag)
predBaseLine2 = algoBaseLine.predict(uid2, iid2, r_ui = r_ui2, verbose = verboseFlag)
predBaseLine3 = algoBaseLine.predict(uid3, iid3, r_ui = r_ui3, verbose = verboseFlag)
predBaseLine4 = algoBaseLine.predict(uid4, iid4, r_ui = r_ui4, verbose = verboseFlag)

print("\nKNNBasic:")
predBasic1 = algoBasic.predict(uid1, iid1, r_ui = r_ui1, verbose = verboseFlag)
predBasic2 = algoBasic.predict(uid2, iid2, r_ui = r_ui2, verbose = verboseFlag)
predBasic3 = algoBasic.predict(uid3, iid3, r_ui = r_ui3, verbose = verboseFlag)
predBasic4 = algoBasic.predict(uid4, iid4, r_ui = r_ui4, verbose = verboseFlag)

print("\nKNNWithMeans:")
predWithMeans1 = algoWithMeans.predict(uid1, iid1, r_ui = r_ui1, verbose = verboseFlag)
predWithMeans2 = algoWithMeans.predict(uid2, iid2, r_ui = r_ui2, verbose = verboseFlag)
predWithMeans3 = algoWithMeans.predict(uid3, iid3, r_ui = r_ui3, verbose = verboseFlag)
predWithMeans4 = algoWithMeans.predict(uid4, iid4, r_ui = r_ui4, verbose = verboseFlag)

print("\nKNNWithZScore:")
predWithZScore1 = algoWithZScore.predict(uid1, iid1, r_ui = r_ui1, verbose = verboseFlag)
predWithZScore2 = algoWithZScore.predict(uid2, iid2, r_ui = r_ui2, verbose = verboseFlag)
predWithZScore3 = algoWithZScore.predict(uid3, iid3, r_ui = r_ui3, verbose = verboseFlag)
predWithZScore4 = algoWithZScore.predict(uid4, iid4, r_ui = r_ui4, verbose = verboseFlag)


def precision_recall_at_k(predictions, k=10, threshold=3.5):
    # Return precision and recall at k metrics for each user.

    # First map the predictions to each user.
    user_est_true = defaultdict(list)
    for uid, _, true_r, est, _ in predictions:
        user_est_true[uid].append((est, true_r))

    precisions = dict()
    recalls = dict()
    f1scores = dict()

    for uid, user_ratings in user_est_true.items():

        # Sort user ratings by estimated value
        user_ratings.sort(key=lambda x: x[0], reverse=True)

        # Number of relevant items
        n_rel = sum((true_r >= threshold) for (_, true_r) in user_ratings)

        # Number of recommended items in top k
        n_rec_k = sum((est >= threshold) for (est, _) in user_ratings[:k])

        # Number of relevant and recommended items in top k
        n_rel_and_rec_k = sum(((true_r >= threshold) and (est >= threshold))
                              for (est, true_r) in user_ratings[:k])

        # Precision@K: Proportion of recommended items that are relevant
        precisions[uid] = n_rel_and_rec_k / n_rec_k if n_rec_k != 0 else 1
        precision = precisions[uid]

        # Recall@K: Proportion of relevant items that are recommended
        recalls[uid] = n_rel_and_rec_k / n_rel if n_rel != 0 else 1
        recall = recalls[uid]

        # F - Score = 2 * Precision * Recall / (Precision + Recall)
        f1scores[uid] = 2 * precision * recall / (precision + recall) if (precision + recall) else 0

    return precisions, recalls, f1scores


# Use the SVD++ algorithm since this one is capable of dealing with implicit info.
algo = SVDpp()

# Run 5-fold cross-validation and print results.
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)


# Calculate precision and recall
kf = KFold(n_splits=5)
fold_count = 1

for trainset, testset in kf.split(data):
    algo.fit(trainset)
    predictions = algo.test(testset)
    precisions, recalls, f1scores = precision_recall_at_k(predictions, k=5, threshold=4)

    # Precision and recall can then be averaged over all users
    print("Fold", fold_count)
    fold_count += 1

    print("Precision:", sum(prec    for prec    in precisions.values()) / len(precisions))
    print("Recall:",    sum(rec     for rec     in recalls.values()   ) / len(recalls)   )
    print("F1Score:",   sum(f1score for f1score in f1scores.values()  ) / len(precisions))
    print()