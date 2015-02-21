from parser import TrainDataParser
from algorithms.k_nearest import KNearestNeighbours
from algorithms.decision_tree import id3, DecisionTree, process_dataset, process_entity

if __name__ == '__main__':
    to_determine = {
        'parch': '0',
        'cabin': '',
        'ticket': 'A/5 21171',
        'pclass': '3',
        'sibsp': '1',
        'sex': 'female',
        'passengerid': '1',
        'name': 'Braund, Mr. Owen Harris',
        'age': '47',
        'embarked': 'S',
        'fare': '7',
    }

    data_api = TrainDataParser()
    k_nearest_test = KNearestNeighbours(data=data_api.map_data_to_column_names())
    # print(k_nearest_test.will_survive(this_survived))
    dataset = process_dataset(data_api.map_data_to_columns_exclude(['cabin', 'ticket', 'passengerid', 'name']))
    dt = id3(dataset, {
        'parch': [0, 1, 2],
        'pclass': ['1', '2', '3'],
        'sibsp': [0, 1, 2],
        'sex': ['male', 'female'],
        'age': [0, 1, 2, None],
        'embarked': ['S', 'Q', 'C'],
        })
    print(dt.predict_value(process_entity(to_determine)))
