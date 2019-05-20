"""
Results from running 5-fold cross validation with SVD on ml-100k:

                  Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Mean    Std
RMSE (testset)    0.9391  0.9392  0.9303  0.9348  0.9441  0.9375  0.0046
MAE (testset)     0.7401  0.7399  0.7325  0.7383  0.7429  0.7387  0.0034
Fit time          4.64    4.79    4.58    4.72    4.66    4.68    0.07
Test time         0.18    0.18    0.17    0.18    0.18    0.18    0.00
"""

# For precision and recall
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from collections import defaultdict
from surprise.model_selection import KFold

from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate


def precision_recall_at_k(predictions, k=10, threshold=3.5):
    '''Return precision and recall at k metrics for each user.'''

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
        f1scores[uid] = 2 * precision * recall / (precision + recall)

    return precisions, recalls, f1scores


# Load the movielens-100k dataset (download it if needed).
data = Dataset.load_builtin('ml-100k')

# Use the famous SVD algorithm.
algo = SVD()

# Run 5-fold cross-validation and print results.
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)


# Calculate precision and recall
data = Dataset.load_builtin('ml-100k')
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