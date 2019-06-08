from os.path import abspath
from spotlight.datasets import _transport
from spotlight.interactions import Interactions
from spotlight.cross_validation import random_train_test_split
from spotlight.evaluation import sequence_mrr_score
from spotlight.sequence.implicit import ImplicitSequenceModel
import pandas as pd
import numpy as np


def _load_own_dataset(dataset):
    extension = '.csv'
    path = '../../../resources/'

    data = np.genfromtxt(path + dataset + extension, delimiter=',', names=True)

    user_id = data['user_id']
    session_id = data['session_id']
    timestamp = data['timestamp']
    step = data['step']
    action_type = data['action_type']
    reference = data['reference']
    platform = data['platform']
    city = data['city']
    device = data['device']
    current_filters = data['current_filters']
    impressions = data['impressions']
    prices = data['prices']

    return (user_id, session_id, timestamp, step, action_type, reference, platform, city, device, current_filters, impressions, prices)

def get_own_dataset(datafile):
    """returns interactions of interactions class instance spotlight.interactions.Interactions"""
    
    loc = datafile
    
    return Interactions(*_load_own_dataset(datafile))

# parameters: our sequence model, the dataframe of the dataset and a list of user ids out of the training set
def recommendation(model, df_out, df_data, user_ids):

    # save item recommendations in list (will be last row of our submission file)
    item_recommendations = []

    # generate rec for each user
    for user_id in user_ids:
        item_recommendations.append(model.predict(user_id))

        # for testing if something does not work
        #print("User %s" % user_id)
        #print(scores)

    df_out['user_id'] = df_data[['user_id']]
    df_out['session_id'] = df_data[['session_id']]
    df_out['timestamp'] = df_data[['timestamp']]
    df_out['step'] = df_data[['step']]
    df_out['item_recommendations'] = item_recommendations

    return df_out


print("Load Data")
#train_csv = abspath("../../../resources/train.csv")
#test_csv = abspath("../../../resources/test.csv")
#subm_csv = abspath("../../../resources/myoutput.csv")
own_dataset = abspath("../../../resources/min_trivago.csv")
dataset = get_own_dataset('min_trivago')
print(dataset)

train, test = random_train_test_split(dataset, random_state=np.random.RandomState(42))
print('Split into \n {} and \n {}.'.format(train, test))

print("Build and Fit Implicit Sequence Model")
model = ImplicitSequenceModel(n_iter=3, representation='lstm', loss='bpr')
model.fit(train, verbose=True)

print("Calculate MRR Score")
mrr = sequence_mrr_score(model, test)
print("MRR Result: ", mrr)

print("Calculate Recommendations")
# get data into dataframe for extracting user ids (I think we need the testset here?)
df_test = pd.read_csv(own_dataset)
user_ids = df_test[['user_id']]
# call recommendation algorithm
df_out = pd.DataFrame()
df_out = recommendation(model, df_out, df_test, user_ids)


# write result to csv file
subm_csv = abspath("../../../resources/myoutput.csv")
print(f"Writing {subm_csv}...")
df_out.to_csv(subm_csv, index=False)

