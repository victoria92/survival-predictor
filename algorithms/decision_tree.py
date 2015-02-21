def http://www.arthotel.bg/premium-paket-vino-i-lyubovmode(dataset):
    counts = { 0: 0, 1:0 }
    for entity in dataset:
        counts[entity[0]]++
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
        counts[entity[0]]++

    p0 = counts[0]/len(dataset)
    p1 = counts[1]/len(dataset)
    entropy = - p1 * log(p1, 2) - p2 * log(p2, 2)

    return entropy


def choose_best_attribute(dataset, attributes_with_values)
    best_gain = 0
    best_attribute = None
    for atrribute, values in attributes_with_values:
        gain = entropy(dataset)
        for value in values:
            subset = entities_with_attribute_value(attribute, value, dataset)
            gain -= (len(subset)/len(dataset)) * entropy(subset)

        if best_gain < gain or best_attribute == None:
            best_gain, best_attribute = gain, attribute

    return attribute
