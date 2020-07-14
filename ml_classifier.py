from classifiers.k_nearest_neighbours import run_knn
from classifiers.naive_bayes import run_nb
from utils.process_utils import process_args, process_data
from utils.general_utils import print_output

##
# Main Method.
#
if __name__ == "__main__":

    (training_file, testing_file, mode, k_value) = process_args()

    # Get list of "Data" objects from a file.
    training_list = process_data(training_file)
    testing_list = process_data(testing_file, training=False)

    if mode == "NB":
        output = run_nb(training_list, testing_list)
        print_output(output)
    elif mode == "NN":
        output = run_knn(training_list, testing_list, k_value)
        print_output(output)
