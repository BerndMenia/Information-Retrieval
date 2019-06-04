#from pathlib import Path

from os.path import abspath


import click
import pandas as pd
import functions as f

#current_directory = Path(__file__).absolute().parent
#current_directory = abspath()

#default_data_directory = current_directory.joinpath('..', '..', 'data')
default_data_directory = abspath("../../../../resources/")

@click.command()
@click.option('--data-path', default=None, help='Directory for the CSV files')
def main(data_path):
    # calculate path to files
    data_directory = abspath(data_path) if data_path else default_data_directory

    #train_csv = data_directory.joinpath('train_small.csv')
    #test_csv = data_directory.joinpath('test_small.csv')
    #subm_csv = data_directory.joinpath('submission_popular.csv')

    train_csv = abspath("../../../../resources/train.csv")
    test_csv = abspath("../../../../resources/test.csv")
    subm_csv = abspath("../../../../resources/submission_popular.csv")

    print(f"Reading {train_csv} ...")
    df_train = pd.read_csv(train_csv)

    # df_expl = f.explode(df_target, "impressions")

    print("Find some Probabilities...")
    d_prob = f.get_probabilities(df_train)
    
    del df_train
    
    print(f"Reading {test_csv} ...")
    df_test = pd.read_csv(test_csv)

    print("Identify target rows...")
    df_target = f.get_submission_target(df_test)
    
    print("Order Impressions by probabilities")
    d_sessionProb = f.calc_probabilities(df_target, df_test, d_prob)

    df_probably = f.calc_recommendation_by_probab(df_target, d_sessionProb)

    # print("Get recommendations...")
    #
    # df_out = f.calc_recommendation(df_expl, df_popular)
    #
    # print(f"Writing {subm_csv}...")
    # df_out.to_csv(subm_csv, index=False)

    # print("Get recommendations based on price...")
    # df_out = f.calc_recommendation_by_price(df_expl)

    print(f"Writing {subm_csv}...")
    df_probably.to_csv(subm_csv, index=False)

    print("Finished calculating recommendations.")


if __name__ == '__main__':
    main()
