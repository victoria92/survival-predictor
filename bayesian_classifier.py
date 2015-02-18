import math

def split_data_by_class(dataset):
    split_dataset = { 0: [], 1: [] }

    for entity in dataset:
        if entity[1] == 0:
            split_dataset[0].append(entity)
        else:
            split_dataset[1].append(entity)

    return split_dataset


def average(values):
    return sum(values)/float(len(values))


def deviation(values):
    avg = average(values)
    return math.sqrt(sum([pow(x - avg, 2) for x in values])/(len(values) - 1))


def probability(x, average, deviation):
    exponent = math.exp(-(math.pow(x-average,2)/(2*math.pow(deviation,2))))
    return (1 / (math.sqrt(2*math.pi) * deviation)) * exponent


def measures_by_class(dataset):
    measures = {}

    for class_value, entities in dataset.iteritems():
        measures[class_value] = [(average(x), deviation(x)) for x in zip(*entities)][1:]

    return measures


def predict_class(measures, input):
    probabilities = {}
    for class_value, class_measures in measures.iteritems():
        probabilities[class_value] = 1
        for i in range(len(class_measures)):
            x = input[i]
            average, deviation = class_measures[i]
            probabilities[class_value] *= probability(x, average, deviation)

    match_class, max_probability = None, -1
    for value, probability in probabilities.iteritems():
        if match_class == None or probability > max_probability:
            match_class = value
            max_probability = probability

    return match_class
