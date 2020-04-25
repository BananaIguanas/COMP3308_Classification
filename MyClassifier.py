##
# Run Naive Bayes.
#
def run_nb():
    return


##
# Run K Nearest Neighbours.
#
def run_knn(k_value):
    return


if __name__ == "__main__":
    from general_utils import process_args

    (training, testing, mode, k_value) = process_args()

    if mode == "NB":
        run_nb()
    elif mode == "NN":
        run_knn(k_value)
