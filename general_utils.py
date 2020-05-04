from sys import argv
from Data import Data


##
# Process the command line arguments and return them as a tuple.
#
def process_args():
    training_file = argv[1]
    testing_file = argv[2]
    algorithm = argv[3][-2:]
    nn_k_value = argv[3][:-2]

    return training_file, testing_file, algorithm, nn_k_value


##
# Process a data file by extracting the data from each row.
# Output: A list of "Data" objects representing each row of the file.
#
def process_data(data_file, mapping=None):
    data_arr = None

    # Open up the file and create data objects.
    # First to second last items are attributes. Last item is class value.
    with open(data_file, "r") as f:
        for line in f:
            row_vals = line.strip().split(",")
            attributes = row_vals[:-1]
            class_value = True if row_vals[-1] == "yes" else False

            if mapping:
                data_arr.append(Data(attributes, class_value, mapping))
            else:
                data_arr.append(Data(attributes, class_value))

    return data_arr
