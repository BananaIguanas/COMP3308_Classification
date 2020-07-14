from utils.general_utils import calc_euclid_dist, calc_norm_prob, gen_classifier, calc_class_prob


##
# Run Naive Bayes.
# Input: 2 lists of "Data" objects.
# Output: List of "True" or "False" values.
#
def run_nb(training_list, testing_list):
    output = []
    classifier = gen_classifier(training_list)

    prob_yes = calc_class_prob(True, training_list)
    prob_no = calc_class_prob(False, training_list)

    for test_data_obj in testing_list:
        prob_yes_norm = prob_yes
        prob_no_norm = prob_no
        attr_val_list = test_data_obj.get_all_att()

        for i in range(len(attr_val_list)):
            prob_yes_norm *= calc_norm_prob(i, attr_val_list[i], True, classifier)
            prob_no_norm *= calc_norm_prob(i, attr_val_list[i], False, classifier)

        output.append(True if prob_yes_norm >= prob_no_norm else False)

    return output


##
# Run K Nearest Neighbours.
# Input: 2 arrays of "Data" objects. An integer value K.
# Output: Array of "True" or "False" values.
#
def run_knn(training_list, testing_list, k_value):
    output = []

    for test_data_obj in testing_list:
        dist_tuple_list = []
        counter = 0

        for train_data_obj in training_list:
            # Get the list of floats representing attributes.
            test_data_vals = test_data_obj.get_all_att()
            train_data_vals = train_data_obj.get_all_att()

            # Get the euclidean distance and class value.
            euclid_dist = calc_euclid_dist(test_data_vals, train_data_vals)
            class_val = train_data_obj.get_class_val()

            # Make tuple of euclid_dist and class_val and add to list.
            dist_tuple = (euclid_dist, class_val)
            dist_tuple_list.append(dist_tuple)

        # Sort dist_tuple_list by distance.
        dist_tuple_list.sort(key=lambda x: x[0])

        # Take the majority of the first k class values.
        for tuple_obj in dist_tuple_list[:k_value]:
            counter += 1 if tuple_obj[1] is True else -1

        # Append majority value to output. Break ties with True.
        output.append(True if counter >= 0 else False)

    return output


##
# Main Method.
#
if __name__ == "__main__":
    from utils.general_utils import process_args, process_data, print_output

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
