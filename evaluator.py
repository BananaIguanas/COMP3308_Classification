from sys import exit
from MyClassifier import run_nb, run_knn
import argparse

##
# Setting up conditions for command line inputs.
#
parser = argparse.ArgumentParser(description="Evaluator for Classifiers")

parser.add_argument("training",
                    help="Location of training file to be split into training and testing sets")

parser.add_argument("mode", choices=["NB", "NN"], default="NB",
                    help="Run classifier with Naive Bayes algorithm")

parser.add_argument("-k", "--k_value",
                    help="K value to use with K Nearest Neighbour Algorithm.")

parser.add_argument("-f", "--folds", type=int, default=10,
                    help="Number of folds the Evaluator should run with")


##
# Split the data into training and testing sets.
# Output: A tuple. First value is training_set, second is testing_set.
#
def seperate_set(fold, total_folds):
    pass


##
# Run the Evaluation function to compare classifier output to true output.
# Output: Percentage value (float) of accuracy.
#
def evaluate(classifier_out, true_out):
    pass


##
# Gets the true classifications of the testing set.
# Output: Array of 'true' or 'false' values.
# Note: 'true' represents a classification of 'yes', 'false' represents 'no'.
#
def get_true_output(testing_set):
    pass


##
# Main Method.
#
if __name__ == "__main__":
    cmd_args = parser.parse_args()
    total = 0

    if cmd_args == "NN" and not cmd_args.k_value:
        print("Need to provide K value with Nearest Neighbour.")
        exit()

    for fold in range(cmd_args.folds):
        (training_set, testing_set) = seperate_set(fold, cmd_args.folds)
        true_out = get_true_output(testing_set)

        if cmd_args.mode == "NB":
            total += evaluate(run_nb(training_set, testing_set), true_out)
        else:
            total += evaluate(run_knn(training_set, testing_set, cmd_args.k), true_out)

    print(f"Average accuracy of {cmd_args.folds} folds: {total/cmd_args.folds}%")
