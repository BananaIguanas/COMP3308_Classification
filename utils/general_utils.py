from sys import argv
from math import sqrt
from .data import Data


##
# Process the command line arguments and return them as a tuple.
#
def process_args():
    training_file = argv[1]
    testing_file = argv[2]
    algorithm = argv[3][-2:]
    nn_k_value = int(argv[3][:-2])

    return training_file, testing_file, algorithm, nn_k_value


##
# Process a data file by extracting the data from each row.
# Input: data_file - Location of file
#        mapping - Optional mapping for attribute name to index.
# Output: A list of "Data" objects representing each row of the file.
#
def process_data(data_file, mapping=None):
    data_list = []

    # Open up the file and create data objects.
    # First to second last items are attributes. Last item is class value.
    with open(data_file, "r") as f:
        for line in f:
            (attributes, class_value) = _process_line(line)

            if mapping:
                data_list.append(Data(attributes, class_value, mapping))
            else:
                data_list.append(Data(attributes, class_value))

    return data_list


##
# Process a stratified data file into a list of stratified lists. Each stratified list
# represents a stratified fold.
#
def process_strat_data(data_file):
    folds_list = []

    with open(data_file, "r") as f:
        fold = []

        for line in f:
            if line.strip().startwith("fold"):
                fold = []
            elif not line.strip():
                folds_list.append(fold)
            else:
                (attributes, class_value) = _process_line(line)
                fold.append(Data(attributes, class_value))

        # Python has no way to detect EOF in a nice manner, so once we finish
        # going through all the lines, just add the fold to the folds_list
        folds_list.append(fold)

    return folds_list


##
# Private function to process a data row/line in a data file.
#
def _process_line(line):
    row_vals = line.strip().split(",")
    attributes = [float(val) for val in row_vals[:-1]]
    class_value = True if row_vals[-1] == "yes" else False

    return attributes, class_value


##
# Calculate the Euclidean distance between 2 points.
# Input: first_list and second_list - List of floats representing attributes.
# Output: A float representing the Euclidean distance.
#
def calc_euclid_dist(first_list, second_list):
    # List of all items from "first_list" minus "second_list"
    diff = [first_list[i] - second_list[i] for i in range(len(first_list))]
    # List of all items from "diff" squared.
    diff_squared = list(map(lambda x: x**2, diff))

    return sqrt(sum(diff_squared))


##
# Print 'yes' or 'no' values depending on a Boolean value from a list.
# Input: boolean_list - List of True and False values.
#
def print_output(boolean_list):
    for boolean in boolean_list:
        print('yes' if boolean is True else 'no')
