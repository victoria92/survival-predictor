from parser import TrainDataParser
from algorithms.decision_tree import id3, process_dataset, process_entity
from algorithms.bayesian_classifier import process_data, predict_class


if __name__ == '__main__':
    exclude_list = ['cabin', 'ticket', 'name']
    train_data_api = TrainDataParser(csv_file='data/train.csv')
    test_data_api = TrainDataParser(csv_file='data/test.csv')
    gendermodel_data_api = TrainDataParser(csv_file='data/gendermodel.csv')

    train_data_api.map_data_to_columns_exclude(['pclass'])
    # print(k_nearest_test.will_survive(this_survived))
    #dataset = process_dataset(train_data_api.map_data_to_columns_exclude(exclude_list=exclude_list))
    dataset = process_data(train_data_api.map_data_to_columns_exclude(exclude_list = exclude_list))

    guessed_right = 0

    for i in range(892, 1310):
        item = test_data_api.get_with_id(str(i), exclude_list=exclude_list)
        result_expected = gendermodel_data_api.get_with_id(str(item['passengerid']))['survived']

        #dt = id3(dataset, {
        #    'parch': [0, 1, 2],
        #    'pclass': ['1', '2', '3'],
        #    'sibsp': [0, 1, 2],
        #    'sex': ['male', 'female'],
        #    'age': [0, 1, 2, 3],
        #    'embarked': ['S', 'Q', 'C'],
        #    'fare': [0, 1, 2, 3],
        #})

        #result_actual = dt.predict_value(process_entity(item))
        result_actual = predict_class(dataset, item, ['pclass', 'sex', 'embarked'])


        if int(result_expected) == result_actual:
            guessed_right += 1

    print ((guessed_right / (1310 - 892)) * 100)
