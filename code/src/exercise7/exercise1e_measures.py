from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from os.path import abspath
from surprise import Dataset
from surprise import Reader

from surprise import KNNBaseline
from surprise import KNNBasic
from surprise import KNNWithMeans
from surprise import KNNWithZScore


from collections import defaultdict
from surprise.model_selection import KFold
from surprise.model_selection import cross_validate


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


# load dataset
data_path = abspath("../../../resources/ml-100k/i.data")

# set rating range when loading in the dataset
reader = Reader(line_format='user item rating timestamp', sep='\t', rating_scale=(0,1))

# load the dataset
data = Dataset.load_from_file(data_path, reader=reader)

# calculate RMSE and MAE
for algo in [KNNBaseline(), KNNBasic(), KNNWithMeans(), KNNWithZScore()]:
    # Run 5-fold cross-validation and print results.
    cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)


for algo in [KNNBaseline(), KNNBasic(), KNNWithMeans(), KNNWithZScore()]:
    # Calculate precision and recall and f1score
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
