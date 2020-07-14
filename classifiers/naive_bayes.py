from utils.general_utils import calc_norm_prob, calc_class_prob
from statistics import mean, pstdev


##
# Run Naive Bayes.
# Input: 2 lists of "Data" objects.
# Output: List of "True" or "False" values.
#
def run_nb(training_list, testing_list):
    output = []
    classifier = _gen_nb_classifier(training_list)

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
# Make the classifier for Naive Bayes
# FIXME: Rework classifier to not be 2 lists inside a list.
#
def _gen_nb_classifier(data_list):
    # 0 is false, 1 is true. Contains tuples. Mean is 0 in tuple, stdev is 1.
    classifier = [[], []]

    attr_len = len(data_list[0].get_all_att())

    for attr_name in range(attr_len):
        attr_list_true = []
        attr_list_false = []

        for data_obj in data_list:
            if data_obj.get_class_val() is True:
                attr_list_true.append(data_obj.get_att(attr_name))
            elif data_obj.get_class_val() is False:
                attr_list_false.append(data_obj.get_att(attr_name))
            else:
                raise TypeError("Not a Boolean.")

        mean_val_true = mean(attr_list_true)
        stdev_true = pstdev(attr_list_true, mean_val_true)

        mean_val_false = mean(attr_list_false)
        stdev_false = pstdev(attr_list_false, mean_val_false)

        classifier[1].append((mean_val_true, stdev_true))
        classifier[0].append((mean_val_false, stdev_false))

    return classifier
