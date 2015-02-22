from parser import TrainDataParser
from algorithms.decision_tree import id3, process_dataset

if __name__ == '__main__':
    exclude_list = ['cabin', 'ticket', 'name']
    train_data_api = TrainDataParser(csv_file='data/train.csv')
    test_data_api = TrainDataParser(csv_file='data/test.csv')
    gendermodel_data_api = TrainDataParser(csv_file='data/gendermodel.csv')

    train_data_api.map_data_to_columns_exclude(['pclass'])
    # print(k_nearest_test.will_survive(this_survived))
    dataset = process_dataset(train_data_api.map_data_to_columns_exclude(exclude_list=exclude_list))

    baba = test_data_api.get_with_id('895')
    baba_result = gendermodel_data_api.get_with_id('895')

    guessed_right = 0

    for i in range(892, 1310):
        item = test_data_api.get_with_id(str(i), exclude_list=exclude_list)
        result_expected = gendermodel_data_api.get_with_id(str(item['passengerid']))['survived']
        # result expected is '0' or '1'

    # result = id3( dataset, item)
