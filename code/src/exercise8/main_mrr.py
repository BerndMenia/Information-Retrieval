from os.path import abspath

from code.src.exercise8 import mrr as f

def main():

    # path to files
    gt_csv = abspath("../../../resources/ground_truth.csv")
    subm_csv = abspath("../../../resources/myoutput.csv")

    mrr = f.score_submissions(subm_csv, gt_csv, f.get_reciprocal_ranks)

    print(f'Mean reciprocal rank: {mrr}')


if __name__ == '__main__':
    main()