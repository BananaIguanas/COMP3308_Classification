from sys import argv
from math import sqrt, pi, e
from .data import Data
from statistics import mean, pstdev


##
# Process the command line arguments and return them as a tuple.
#
def process_args():
    training_file = argv[1]
    testing_file = argv[2]
    algorithm = argv[3][-2:]
    nn_k_value = None

    if argv[3][:-2] != '':
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
            if line.strip().startswith("fold"):
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
    len_first = len(first_list)
    len_second = len(second_list)
    diff = []

    if len_first > len_second:
        diff = [first_list[i] - second_list[i] for i in range(len_second)]

        for i in range(len_second, len_first):
            diff.append(max(abs(first_list[i]), abs(1 - first_list[i])))

    elif len_second > len_first:
        diff = [first_list[i] - second_list[i] for i in range(len_first)]

        for i in range(len_first, len_second):
            diff.append(max(abs(second_list[i]), abs(1 - second_list[i])))

    else:
        diff = [first_list[i] - second_list[i] for i in range(len_first)]

    # List of all items from "diff" squared.
    diff_squared = list(map(lambda x: x**2, diff))

    return sqrt(sum(diff_squared))


##
# Calcualte the probability of a value using a normal distribution
#
def calc_norm_prob(attr_name, attr_val, class_val, classifier):

    class_val = 1 if class_val else 0
    mean_val = classifier[class_val][attr_name][0]
    stdev = classifier[class_val][attr_name][1]

    multiple = 1/(stdev * sqrt(2 * pi))
    base = e
    pow_denominator = (2 * (stdev**2))
    power = -(((attr_val - mean_val)**2)/pow_denominator)

    return multiple * (base**power)


##
# Make the classifier for Naive Bayes
#
def gen_classifier(data_list):
    # 0 is false, 1 is true. Contains tuples. Mean is 0 in tuple, stdev is 1.
    classifier = [[], []]

    attr_len = len(data_list[0].get_all_att())

    for attr_name in range(attr_len):
        attr_list_true = []
        attr_list_false = []

        for data_obj in data_list:
            if data_obj.get_class_val():
                attr_list_true.append(data_obj.get_att(attr_name))
            else:
                attr_list_false.append(data_obj.get_att(attr_name))

        mean_val_true = mean(attr_list_true)
        stdev_true = pstdev(attr_list_true, mean_val_true)

        mean_val_false = mean(attr_list_false)
        stdev_false = pstdev(attr_list_false, mean_val_false)

        classifier[1].append((mean_val_true, stdev_true))
        classifier[0].append((mean_val_false, stdev_false))

    return classifier


##
# Print 'yes' or 'no' values depending on a Boolean value from a list.
# Input: boolean_list - List of True and False values.
#
def print_output(boolean_list):
    for boolean in boolean_list:
        print('yes' if boolean is True else 'no')
