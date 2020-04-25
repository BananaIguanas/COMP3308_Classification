from sys import argv


##
# Process the command line arguments and return them as a tuple.
#
def process_args():
    training_file = argv[1]
    testing_file = argv[2]
    algorithm = argv[3][-2:]
    nn_k_value = argv[3][:-2]

    return training_file, testing_file, algorithm, nn_k_value
