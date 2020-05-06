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
# Input: Location of file. Optional mapping for attribute name to index.
# Output: A list of "Data" objects representing each row of the file.
#
def process_data(data_file, mapping=None):
    data_list = []

    # Open up the file and create data objects.
    # First to second last items are attributes. Last item is class value.
    with open(data_file, "r") as f:
        for line in f:
            row_vals = line.strip().split(",")
            attributes = [float(val) for val in row_vals[:-1]]
            class_value = True if row_vals[-1] == "yes" else False

            if mapping:
                data_list.append(Data(attributes, class_value, mapping))
            else:
                data_list.append(Data(attributes, class_value))

    return data_list


##
# Calculate the Euclidean distance between 2 points.
# Input: 2 Lists of floats.
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
#
def print_output(boolean_list):
    for boolean in boolean_list:
        print('yes' if boolean is True else 'no')
