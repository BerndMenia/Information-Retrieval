from os.path import abspath
from spotlight.evaluation import sequence_mrr_score
from spotlight.sequence.implicit import ImplicitSequenceModel
from spotlight.cross_validation import user_based_train_test_split
import pandas as pd


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
train_csv = abspath("../../../resources/train_small_no_header.csv")
test_csv = abspath("../../../resources/test.csv")
subm_csv = abspath("../../../resources/myoutput.csv")

print(f"Reading {train_csv} ...")
df_train = pd.read_csv(train_csv)

train, test = user_based_train_test_split(train_csv)
train = train.to_sequence()
test = test.to_sequence()


#print(f"Reading {test_csv} ...")
#df_test = pd.read_csv(test_csv)

print("Build and Fit Implicit Sequence Model")
model = ImplicitSequenceModel(n_iter=3, representation='cnn', loss='bpr')
#model.fit(df_train)

model.fit(train)

print("Calculate MRR Score")
mrr = sequence_mrr_score(model, test_csv)
print("MRR Result: ", mrr)

print("Calculate Recommendations")
# get data into dataframe for extracting user ids (I think we need the testset here?)
df_test = pd.read_csv(test_csv)
user_ids = df_test[['user_id']]
# call recommendation algorithm
df_out = pd.DataFrame()
df_out = recommendation(model, df_out, df_test, user_ids)


# write result to csv file
print(f"Writing {subm_csv}...")
df_out.to_csv(subm_csv, index=False)
