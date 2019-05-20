"""
Results from running 5-fold cross validation with SVD on ml-100k:

                  Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Mean    Std
RMSE (testset)    0.9391  0.9392  0.9303  0.9348  0.9441  0.9375  0.0046
MAE (testset)     0.7401  0.7399  0.7325  0.7383  0.7429  0.7387  0.0034
Fit time          4.64    4.79    4.58    4.72    4.66    4.68    0.07
Test time         0.18    0.18    0.17    0.18    0.18    0.18    0.00
"""


from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate

# Load the movielens-100k dataset (download it if needed).
data = Dataset.load_builtin('ml-100k')

# Use the famous SVD algorithm.
algo = SVD()

# Run 5-fold cross-validation and print results.
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

