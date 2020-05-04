

##
# Run Naive Bayes.
# Input: 2 lists of "Data" objects.
# Output: List of "True" or "False" values.
#
def run_nb(training_list, testing_list):
    output = []

    for test_data_obj in testing_list:
        for train_data_obj in training_list:
            pass

    return output


##
# Run K Nearest Neighbours.
# Input: 2 arrays of "Data" objects. An integer value K.
# Output: Array of "True" or "False" values.
#
def run_knn(training_list, testing_list, k_value):
    return


##
# Main Method.
#
if __name__ == "__main__":
    from general_utils import process_args
    from general_utils import process_data

    (training_file, testing_file, mode, k_value) = process_args()

    # Get list of "Data" objects from a file.
    training_list = process_data(training_file)
    testing_list = process_data(testing_file)

    if mode == "NB":
        run_nb(training_list, testing_list)
    elif mode == "NN":
        run_knn(training_list, testing_list, k_value)
