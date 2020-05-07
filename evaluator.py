from sys import exit
from MyClassifier import run_nb, run_knn
import argparse
from utils.general_utils import process_strat_data

##
# Setting up conditions for command line inputs.
#
parser = argparse.ArgumentParser(description="Evaluator for Classifiers")

parser.add_argument("training",
                    help="Location of training file to be split into training and testing lists")

parser.add_argument("mode", choices=["NB", "NN"], default="NB",
                    help="Run classifier with Naive Bayes algorithm")

parser.add_argument("-k", "--k_value",
                    help="K value to use with K Nearest Neighbour Algorithm.")

parser.add_argument("-f", "--folds", type=int, default=10,
                    help="Number of folds the Evaluator should run with")


##
# Organise the folds into a training list and testing list.
# Input: folds_list - A list of stratified lists, each representing a stratified fold.
#        curr_fold - The current fold we are using for test.
#        total_folds - Total number of folds.
# Output: A tuple with 2 lists. First list is training, second it testing.
#
def split_folds(folds_list, curr_fold, total_folds):
    training_list = []
    testing_list = folds_list[curr_fold]

    for i in range(curr_fold):
        training_list += folds_list[i]

    for i in range(curr_fold + 1, len(folds_list)):
        training_list += folds_list[i]

    return training_list, testing_list


##
# Run the Evaluation function to compare classifier output to true output.
# Input: 2 lists of True or False values.
# Output: Percentage value (float) of accuracy.
#
def evaluate(classifier_out, true_out):
    pass


##
# Gets the true classifications of the testing list.
# Input: A list of "Data" objects.
# Output: Array of 'true' or 'false' values.
# Note: 'true' represents a classification of 'yes', 'false' represents 'no'.
#
def get_true_output(testing_list):
    pass


##
# Main Method.
#
if __name__ == "__main__":
    cmd_args = parser.parse_args()
    total = 0

    if cmd_args.mode == "NN" and not cmd_args.k_value:
        print("Need to provide K value with Nearest Neighbour.")
        exit()

    # Grab a list containing lists which represent each stratified fold from a file.
    folds_list = process_strat_data(cmd_args.training)

    for fold in range(cmd_args.folds):
        # Take a list of fold lists and seperate into trainig and testing sets.
        (training_list, testing_list) = split_folds(folds_list, fold, cmd_args.folds)
        true_out = get_true_output(testing_list)

        if cmd_args.mode == "NB":
            total += evaluate(run_nb(training_list, testing_list), true_out)
        else:
            total += evaluate(run_knn(training_list, testing_list, cmd_args.k), true_out)

    print(f"Average accuracy of {cmd_args.folds} folds: {total/cmd_args.folds}%")
