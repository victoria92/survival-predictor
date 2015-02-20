from parser import TrainDataParser
from algorithms.k_nearest import KNearestNeighbours


if __name__ == '__main__':
    to_determine = {
        'parch': '0',
        'cabin': '',
        'ticket': 'A/5 21171',
        'pclass': '3',
        'sibsp': '1',
        'sex': 'male',
        'passengerid': '1',
        'name': 'Braund, Mr. Owen Harris',
        'age': '22',
        'embarked': 'S',
        'fare': '7.25',
    }

    data_api = TrainDataParser()
    k_nearest_test = KNearestNeighbours(data=data_api.map_data_to_column_names())
    # print(k_nearest_test.will_survive(this_survived))
