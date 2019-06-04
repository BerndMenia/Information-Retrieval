import math
import pandas as pd
import numpy as np
import functools

GR_COLS = ["user_id", "session_id", "timestamp", "step"]


def get_submission_target(df):
    """Identify target rows with missing click outs."""

    mask = df["reference"].isnull() & (df["action_type"] == "clickout item")
    df_out = df[mask]

    return df_out


def get_probabilities(df):
    """Calculate probabilities by the training set
    
    :param df: Full Train Data frame
    :return: Dictionary with probabilities 
        "Order" -> Vector of probabilities for position
        "Sort" -> Vector of probabilities for position
        "Interaction" -> Single probability value for Interaction
    """

    probs = {}

    mask = df["action_type"] == "clickout item"
    df_clicks = df[mask]
    # df_item_clicks = (
    #     df_clicks
    #         .groupby("reference")
    #         .size()
    #         .reset_index(name="n_clicks")
    #         .transform(lambda x: x.astype(int))
    # )

    # first look how the probable each position of the
    # impressions depends the picking
    # additionally check extra if a sorting was used and use
    # calculate different probability
    print("Find some Order Probabilities...")
    probPos = np.zeros(25)
    probPosFil = np.zeros(25)
    numFilTotal = 0
    for _, x in df_clicks.iterrows():
        imp = string_to_array(x["impressions"])
        try:
            probPos[imp.index(
                x["reference"])] += 1  # there is one case where the clickout item is not in the impressions?!?
            if isinstance(x["current_filters"], str) and "Sort" in x["current_filters"]:
                probPosFil[imp.index(x["reference"])] += 1
                numFilTotal += 1
        except:
            pass
    probs["Order"] = probPos / len(df_clicks.index)
    probs["Sort"] = probPosFil / numFilTotal

    # now use also all interactions
    # look if an interaction was on an item, and if it was chosen afterwards
    print("Find some Interaction Probabilities...")
    mask = (df["action_type"] == "clickout item") | ["interaction" in x for x in df["action_type"]]
    df_interatctions = df[mask]

    interactionTotal = 1
    interactionPos = 1
    interactionTotal = 0
    interactionPos = 0
    lastSession = ""
    interactions = set()
    for _, x in df_interatctions.iterrows():
        if x["session_id"] != lastSession:
            interactions = set()
        if "interaction" in x["action_type"]:
            interactions.add(x["reference"])
        else:
            interactionTotal += 1
            if x["reference"] in interactions:
                interactionPos += 1
        lastSession = x["session_id"]

    probs["Interaction"] = interactionPos / interactionTotal

    return probs


def array_to_string_submission(a):
    return ' '.join([str(x) for x in a])


def string_to_array(s):
    """Convert pipe separated string to array."""

    if isinstance(s, str):
        out = s.split("|")
    elif math.isnan(s):
        out = []
    else:
        raise ValueError("Value must be either string of nan")
    return out


def explode(df_in, col_expl):
    """Explode column col_expl of array type into multiple rows.
        Price row is automatically (and equally to impression) exploded"""

    df = df_in.copy()
    df.loc[:, col_expl] = df[col_expl].apply(string_to_array)
    df.loc[:, "prices"] = df["prices"].apply(string_to_array)

    columns = {col: np.repeat(df[col].values,
                              df[col_expl].str.len())
               for col in df.columns.drop(col_expl)}

    columns["price"] = np.concatenate(df["prices"].values)

    df_out = pd.DataFrame(
        columns
    )

    df_out.loc[:, col_expl] = np.concatenate(df[col_expl].values)
    df_out.loc[:, col_expl] = df_out[col_expl].apply(int)

    return df_out


def calc_probabilities(df_target, df_test, d_prob):
    """Calculate recommendations based on price of items.

    :param df_target: Data frame with impression list and price list
    :param df_text: full test data frame
    :param d_prob:  probabilities for some cases
    :return: Data frame with items and probabilty of clicking it
    """

    # mask = "interaction" in df_test["action_type"]
    mask = ["interaction" in x for x in df_test["action_type"]]
    df_interactions = df_test[mask]

    interactionsPSession = {}
    for _, x in df_interactions.iterrows():
        if not x["session_id"] in interactionsPSession:
            interactionsPSession[x["session_id"]] = set()
        interactionsPSession[x["session_id"]].add(x["reference"])
    sessionProb = {}
    for _, x in df_target.iterrows():
        if isinstance(x["current_filters"], str) and "Sort" in x["current_filters"]:
            sessionProb[x["session_id"]] = d_prob["Sort"]
        else:
            sessionProb[x["session_id"]] = d_prob["Order"]
        for i, item in enumerate(string_to_array(x["impressions"])):
            if x["session_id"] in interactionsPSession and item in interactionsPSession[x["session_id"]]:
                sessionProb[x["session_id"]][i] *= d_prob["Interaction"]
            else:
                sessionProb[x["session_id"]][i] *= (1 - d_prob["Interaction"])

    return sessionProb


def calc_recommendation_by_probab(df_target, sessionProb):
    df_out = df_target[GR_COLS + ["impressions"]].copy()

    df_out.loc[:, "impressions"] = df_out["impressions"].apply(string_to_array)

    for _, line in df_out.iterrows():
        some = [x for y, x in sorted(zip(sessionProb[line["session_id"]], line["impressions"]))]
        line["impressions"] = functools.reduce(lambda a, b: a + ' ' + b, some)

    df_out.loc[:, "impressions"] = df_out["impressions"].apply(lambda x: ' '.join(str(y) for y in x))
    df_out.rename(columns={'impressions': 'item_recommendations'}, inplace=True)

    return df_out
