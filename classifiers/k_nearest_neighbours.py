from utils.general_utils import calc_euclid_dist


##
# Run K Nearest Neighbours.
# Input: 2 arrays of "Data" objects. An integer value K.
# Output: Array of "True" or "False" values.
#
def run_knn(training_list, testing_list, k_value):
    output = []

    for test_data_obj in testing_list:
        test_data_vals = test_data_obj.get_all_att()
        dist_tuple_list = []

        for train_data_obj in training_list:
            # Get the list of floats representing attributes.
            train_data_vals = train_data_obj.get_all_att()

            # Get the euclidean distance and class value.
            euclid_dist = calc_euclid_dist(test_data_vals, train_data_vals)
            class_val = train_data_obj.get_class_val()

            # Make tuple of euclid_dist and class_val and add to list.
            dist_tuple_list.append((euclid_dist, class_val))

        # Sort dist_tuple_list by distance.
        dist_tuple_list.sort(key=lambda x: x[0])

        # Take the majority of the first k class values.
        counter = 0
        for tuple_obj in dist_tuple_list[:k_value]:
            counter += 1 if tuple_obj[1] is True else -1

        # Append majority value to output. Break ties with True.
        output.append(True if counter >= 0 else False)

    return output
