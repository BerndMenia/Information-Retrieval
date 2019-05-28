from os.path import abspath

import pandas as pd

from code.src.exercise8 import baseline as f

def main():

    # path to files
    train_csv = abspath("../../../resources/train.csv")
    test_csv = abspath("../../../resources/test.csv")
    subm_csv = abspath("../../../resources/myoutput.csv")

    print(f"Reading {train_csv} ...")
    df_train = pd.read_csv(train_csv)
    print(f"Reading {test_csv} ...")
    df_test = pd.read_csv(test_csv)

    print("Get popular items...")
    df_popular = f.get_popularity(df_train)

    print("Identify target rows...")
    df_target = f.get_submission_target(df_test)

    print("Get recommendations...")
    df_expl = f.explode(df_target, "impressions")
    df_out = f.calc_recommendation(df_expl, df_popular)

    print(f"Writing {subm_csv}...")
    df_out.to_csv(subm_csv, index=False)

    print("Finished calculating recommendations.")


if __name__ == '__main__':
    main()
