from math import sqrt, pi, e


##
# Calculate the Euclidean distance between 2 points.
# Input: first_list and second_list - List of floats representing attributes.
# Output: A float representing the Euclidean distance.
#
def calc_euclid_dist(first_list, second_list):
    diff = [first_list[i] - second_list[i] for i in range(len(first_list))]
    # List of all items from "diff" squared.
    diff_squared = list(map(lambda x: x**2, diff))

    return sqrt(sum(diff_squared))


##
# Calcualte the probability of a value using a normal distribution
# FIXME: Rework how classifiers are represented. Separate from tuples.
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
# Calcuate the probability of the class value.
#
def calc_class_prob(class_value, data_list):
    total = 0
    for data in data_list:
        if data.get_class_val() == class_value:
            total += 1

    return total/len(data_list)


##
# Print 'yes' or 'no' values depending on a Boolean value from a list.
# Input: boolean_list - List of True and False values.
#
def print_output(boolean_list):
    for boolean in boolean_list:
        print('yes' if boolean is True else 'no')
