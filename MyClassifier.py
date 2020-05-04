

##
# Run Naive Bayes.
# Input: 2 arrays of "Data" objects.
# Output: Array of "True" or "False" values.
#
def run_nb(training_set, testing_set):
    return


##
# Run K Nearest Neighbours.
# Input: 2 arrays of "Data" objects. An integer value K.
# Output: Array of "True" or "False" values.
#
def run_knn(training_set, testing_set, k_value):
    return


##
# Main Method.
#
if __name__ == "__main__":
    from general_utils import process_args
    from general_utils import process_data

    (training_file, testing_file, mode, k_value) = process_args()
    training_set = process_data(training_file)
    testing_set = process_data(testing_file)

    if mode == "NB":
        run_nb(training_set, testing_set)
    elif mode == "NN":
        run_knn(training_set, testing_set, k_value)
