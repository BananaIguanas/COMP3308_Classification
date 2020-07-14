from sys import argv
from .data import Data


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
def process_data(data_file, mapping=None, training=True):
    data_list = []

    # Open up the file and create data objects.
    # First to second last items are attributes. Last item is class value.
    with open(data_file, "r") as f:
        for line in f:
            if training:
                (attributes, class_value) = _process_line(line)
                if mapping:
                    data_list.append(Data(attributes, class_value, mapping))
                else:
                    data_list.append(Data(attributes, class_value))
            else:
                (attributes, class_value) = _process_test_line(line)
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
# Private function to process a data row/line in a data file in general.
#
def _process_line(line):
    row_vals = line.strip().split(",")
    attributes = [float(val) for val in row_vals[:-1]]
    class_value = None

    if row_vals[-1] == "yes":
        class_value = True
    elif row_vals[-1] == "no":
        class_value = False

    return attributes, class_value


##
# Private function to process a data row/line in a data file in general.
#
def _process_test_line(line):
    row_vals = line.strip().split(",")
    attributes = [float(val) for val in row_vals]
    class_value = None

    return attributes, class_value
