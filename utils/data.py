class Data:

    ##
    # Constructor
    # Input: attributes - List of floats, class_values - Boolean, att_mapping - Set.
    #
    def __init__(self, attributes, class_value, att_mapping=None):
        self.attributes = attributes
        self.class_value = class_value
        self.att_mapping = att_mapping

    ##
    # Get a specific attribute
    #
    def get_att(self, value, use_mapping=False):
        if use_mapping and self.att_mapping:
            index = self.att_mapping[value]
            return self.attributes[index]
        elif not use_mapping:
            return self.attributes[value]
        else:
            print("Cannot find attribute, returning None")
            return None

    ##
    # Get all attributes
    # Output: A list containing the attributes.
    #
    def get_all_att(self):
        return self.attributes

    ##
    # Get the attribute mapping
    # Output: A set containing the mapping between attribute name and index.
    #
    def get_att_map(self):
        if self.att_mapping:
            return self.att_mapping
        else:
            print("No mapping was found")

    ##
    # Get the classification of the data entry.
    # Output: Returns a boolean value representing "yes" or "no".
    #
    def get_class_val(self):
        return self.class_value
