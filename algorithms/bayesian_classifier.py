import math


def split_data_by_class(dataset):
    split_dataset = { 0: [], 1: [] }

    for entity in dataset:
        if entity['survived'] == 0:
            split_dataset[0].append(entity)
        else:
            split_dataset[1].append(entity)

    return split_dataset


def average(values):
    return sum(values)/float(len(values))


def deviation(values):
    avg = average(values)
    return math.sqrt(sum([pow(x - avg, 2) for x in values])/(len(values) - 1))


def probability(x, attribute, dataset):
    if len(dataset) == 0:
        return 0

    values = []
    for entity in dataset:
        if entity[attribute] is not None:
            values.append(entity[attribute])

    avg = average(values)
    dev = deviation(values)

    if x == "":
        return 1

    exponent = math.exp(-(math.pow(float(x)-avg,2)/(2*math.pow(dev,2))))
    return (1 / (math.sqrt(2*math.pi) * dev)) * exponent


def probability_with_descrete_attribute(x, attribute, dataset):
    if len(dataset) == 0:
        return 0

    count = 0
    for entity in dataset:
        if entity[attribute] == x:
            count += 1

    return count / len(dataset)


def process_data(dataset):
    for entity in dataset:
        if entity['parch'] == "":
            entity['parch'] == None
        else:
            entity['parch'] = float(entity['parch'])
        if entity['sibsp'] == "":
            entity['sibsp'] == None
        else:
            entity['sibsp'] = float(entity['sibsp'])
        if entity['age'] == "":
            entity['age'] = None
        else:
            entity['age'] = float(entity['age'])
        if entity['fare'] == "":
            entity['fare'] = None
        else:
            entity['fare'] = float(entity['fare'])

    return dataset

def predict_class(dataset, input, descrete_attributes):
    split_data = split_data_by_class(dataset)
    probabilities = {}
    attributes = list(input.keys())
    attributes.remove('passengerid')
    for class_value in split_data.keys():
        probabilities[class_value] = 1
        for attribute in attributes:
            if attribute in descrete_attributes:
                probabilities[class_value] *= probability_with_descrete_attribute(input[attribute], attribute, split_data[class_value])
            else:
                probabilities[class_value] *= probability(input[attribute], attribute, split_data[class_value])

    match_class, max_probability = None, -1
    for value, prob in probabilities.items():
        if match_class == None or prob > max_probability:
            match_class = value
            max_probability = prob

    return match_class
