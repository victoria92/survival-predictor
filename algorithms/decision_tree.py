MIN_EXAMPLES = 1


def mode(dataset):
    counts = { 0: 0, 1:0 }
    for entity in dataset:
        counts[entity[0]] += 1
# What if they are equal?
    if counts[0] > counts[1]:
        return 0
    else:
        return 1

# Attribute must be an index
def entities_with_attribute_value(attribute, value, dataset):
    subset = []
    for entity in dataset:
        if entity[attribute] == value:
            subset.push_back(entity)

    return subset


def entropy(dataset):
    counts = { 0:0, 1:0 }
    for entity in dataset:
        counts[entity[0]] += 1

    p0 = counts[0]/len(dataset)
    p1 = counts[1]/len(dataset)
    entropy = - p1 * log(p1, 2) - p2 * log(p2, 2)

    return entropy


def choose_best_attribute(dataset, attributes_with_values):
    best_gain = 0
    best_attribute = None
    for atrribute, values in attributes_with_values.iteritems():
        gain = entropy(dataset)
        for value in values:
            subset = entities_with_attribute_value(attribute, value, dataset)
            gain -= (len(subset)/len(dataset)) * entropy(subset)

        if best_gain < gain or best_attribute == None:
            best_gain, best_attribute = gain, attribute

    return attribute


class DecisionTree:
    def __init__(self):
        self.attribute = None
        self.label = None
        self.branches = {}

    def addBranch(value, subtree):
        self.branches[value] = subtree

    def predict_value(example):
        pass


def id3(dataset, attributes_with_values):
    node = DecisionTree()
    counts = { 0:0, 1:0 }
    for entity in dataset:
        counts[entity[0]] += 1

    if counts[0] == len(dataset):
        node.label = 0
        return node

    if counts[1] == len(dataset):
        node.label == 1
        return node

    if attributes == {} or len(dataset) < MIN_EXAMPLES:
        node.label = mode(dataset)
        return node

    best_attribute = choose_best_attribute(dataset, attributes_with_values)
    node.attribute = best_attribute

    for value in attributes_with_values[best_attribute]:
        entities = entities_with_attribute_value(best_attribute, value, dataset)
        if entities != []:
            copy_attributes = attributes_with_values.copy()
            del copy_attributes[best_attribute]
            node.addBranch(value, id3(entities, copy_attributes))

    return node
