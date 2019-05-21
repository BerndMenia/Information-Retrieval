"""
Results from running 5-fold cross validation with SVD on ml-100k:

                  Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Mean    Std
RMSE (testset)    0.9391  0.9392  0.9303  0.9348  0.9441  0.9375  0.0046
MAE (testset)     0.7401  0.7399  0.7325  0.7383  0.7429  0.7387  0.0034
Fit time          4.64    4.79    4.58    4.72    4.66    4.68    0.07
Test time         0.18    0.18    0.17    0.18    0.18    0.18    0.00

Exercise 1d:
The similarity measures (sim_options) choose what kind of measurements shall be performed on the algorithm. The default
value hereby for the similarity itself is MSD, however the user can also choose other options like cosine similarity
or pearson_baseline similarity.
There is also an option to choose if the algorithm should perform a user_based (default) or item_based evaluation.

In our example we first let an alorithm run with the default values and then with the sim_options set to cosine
similarity and item_based evaluation. What we noticed is that when setting the sim_options to the aforementioned values
then the precision increases a lot, but on the other hand recall and f1score drop dramatically when compared to the
default value of the sim_options.

For example when using KNNBasic the 5th fold gives the following result with default sim_options:
Fold 5
Precision: 0.8482130219391371
Recall: 0.28468985537884717
F1Score: 0.36859701095108555

When the sim_optsions are set to cosine similarity and item_based evaluation the results changes strongly.
Fold 5
Precision: 0.9378096249115354
Recall: 0.1492095899425385
F1Score: 0.17856802637120095

As we can see the precision went up by about 9% whereas the recall dropped by roughly 14% (almost half), and the
f1score by about 19% (close to half). We don't know exactly why this is the case though.

Note that we also only measured the impact on precision, recall and f1score, but not on execution time.


Example from the documentation:
sim_options = {'name': 'cosine',
               'user_based': False  # compute  similarities between items
               }
algo = KNNBasic(sim_options=sim_options)
"""

# For precision and recall
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from collections import defaultdict
from surprise.model_selection import KFold

from surprise import KNNBaseline
from surprise import KNNBasic
from surprise import KNNWithMeans
from surprise import KNNWithZScore

from surprise import Dataset
from surprise.model_selection import cross_validate


def precision_recall_f1_at_k(predictions, k=10, threshold=3.5):
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
        f1scores[uid] = 2 * precision * recall / (precision + recall) if (precision + recall) else 0

    return precisions, recalls, f1scores


# Load the movielens-100k dataset (download it if needed).
data = Dataset.load_builtin('ml-100k')

# Run 5-fold cross-validation and print results.
for algo in [KNNBaseline(verbose=False), KNNBasic(verbose=False), KNNWithMeans(verbose=False), KNNWithZScore(verbose=False)]:
    cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

print("\n-----------------------------------------------------\n")

sim_options = {'name': 'cosine',
               'user_based': False  # compute  similarities between items
               }

# Calculate precision and recall
for algo in [KNNBaseline(verbose=False), KNNBaseline(sim_options=sim_options, verbose=False), KNNBasic(verbose=False),
             KNNBasic(sim_options=sim_options, verbose=False), KNNWithMeans(verbose=False), KNNWithMeans(sim_options=sim_options, verbose=False),
             KNNWithZScore(verbose=False), (KNNWithZScore(sim_options=sim_options, verbose=False))]:
    kf = KFold(n_splits=5)
    fold_count = 1
    print(str(algo))

    for trainset, testset in kf.split(data):
        algo.fit(trainset)
        predictions = algo.test(testset)
        precisions, recalls, f1scores = precision_recall_f1_at_k(predictions, k=5, threshold=4)

        # Precision and recall can then be averaged over all users
        print("Fold", fold_count)
        fold_count += 1

        print("Precision:", sum(prec    for prec    in precisions.values()) / len(precisions))
        print("Recall:",    sum(rec     for rec     in recalls.values()   ) / len(recalls)   )
        print("F1Score:",   sum(f1score for f1score in f1scores.values()  ) / len(precisions))
        print()

    print("\n-----------------------------------------------------\n")