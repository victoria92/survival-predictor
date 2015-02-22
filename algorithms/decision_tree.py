from math import log


MIN_EXAMPLES = 1
DEFAULT = 0


def mode(dataset):
    counts = {'0': 0, '1': 0}
    for entity in dataset:
        counts[entity['survived']] += 1
# What if they are equal?
    if counts['0'] > counts['1']:
        return 0
    else:
        return 1


def entities_with_attribute_value(attribute, value, dataset):
    subset = []
    for entity in dataset:
        if entity[attribute] == value:
            subset.append(entity)

    return subset


def entropy(dataset):
    counts = {'0': 0, '1': 0}
    for entity in dataset:
        counts[entity['survived']] += 1

    if counts['0'] == len(dataset) or counts['1'] == len(dataset):
        return 0

    p0 = counts['0']/len(dataset)
    p1 = counts['1']/len(dataset)
    entropy = - p0 * log(p0, 2) - p1 * log(p1, 2)

    return entropy


def choose_best_attribute(dataset, attributes_with_values):
    best_gain = 0
    best_attribute = None
    for attribute, values in attributes_with_values.items():
        gain = entropy(dataset)
        for value in values:
            subset = entities_with_attribute_value(attribute, value, dataset)
            if subset == []:
                continue
            gain -= (len(subset)/len(dataset)) * entropy(subset)

        if best_gain < gain or best_attribute is None:
            best_gain, best_attribute = gain, attribute

    return attribute


class DecisionTree:
    def __init__(self):
        self.attribute = None
        self.label = None
        self.branches = {}

    def addBranch(self, value, subtree):
        self.branches[value] = subtree

    def predict_value(self, example):
        node = self
<<<<<<< HEAD
        while node.label is None:
            try:
                node = node.branches[example[node.attribute]]
            except KeyError:
                return 1
=======
        while node.attribute is not None:
            node = node.branches[example[node.attribute]]
>>>>>>> Last minute fixes

        return node.label


def process_entity(entity):
    if entity['age'] == "":
        entity['age'] = 3
    elif float(entity['age']) < 15:
        entity['age'] = 0
    elif float(entity['age']) < 40:
        entity['age'] = 1
    else:
        entity['age'] = 2

    if float(entity['parch']) < 3:
        entity['parch'] = 0
    elif float(entity['parch']) < 6:
        entity['parch'] = 1
    else:
        entity['parch'] = 2

    if float(entity['sibsp']) < 3:
        entity['sibsp'] = 0
    elif float(entity['sibsp']) < 5:
        entity['sibsp'] = 1
    else:
        entity['sibsp'] = 2

<<<<<<< HEAD
    if entity['fare'] == '':
        entity['fare'] = 15

    if float(entity['fare']) < 15:
=======
    if entity['fare'] == "":
        entity['fare'] = 3
    elif float(entity['fare']) < 15:
>>>>>>> Last minute fixes
        entity['fare'] = 0
    elif float(entity['fare']) < 40:
        entity['fare'] = 1
    else:
        entity['fare'] = 2

    return entity


def process_dataset(dataset):
    dataset_copy = dataset.copy()
    for entity in dataset_copy:
        process_entity(entity)
    return dataset_copy


def id3(dataset, attributes_with_values):
    node = DecisionTree()
    counts = {'0': 0, '1': 0}

    for entity in dataset:
        counts[entity['survived']] += 1

    if counts['0'] == len(dataset):
        node.label = 0
        return node

    if counts['1'] == len(dataset):
        node.label == 1
        return node

    if len(attributes_with_values) == 0 or len(dataset) < MIN_EXAMPLES:
        node.label = mode(dataset)
        return node

    best_attribute = choose_best_attribute(dataset, attributes_with_values)
    node.attribute = best_attribute

<<<<<<< HEAD
    # print(best_attribute)
=======
>>>>>>> Last minute fixes
    for value in attributes_with_values[best_attribute]:
        entities = entities_with_attribute_value(best_attribute, value, dataset)
        if entities != []:
            copy_attributes = attributes_with_values.copy()
            del copy_attributes[best_attribute]
            node.addBranch(value, id3(entities, copy_attributes))
        else:
            leave = DecisionTree()
            leave.label = DEFAULT
            node.addBranch(value, leave)

    return node
