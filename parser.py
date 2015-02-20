import csv


class TrainDataParser():
    """
    Given a csv file, provides you with easy-to-use api for accessing the data
    """

    def __init__(self, csv_file='data/train.csv'):
        self.csv_file = csv_file
        self.column_names = []
        self.data = []
        self.populate_data()

    def populate_data(self):
        """
        Read the csv file line by line (first line is column names)
        NOTE: there MAY BE empty columns
        """
        with open(self.csv_file, newline='') as csvfile:
            csvfile_reader = csv.reader(csvfile)
            self.column_names = csvfile_reader.__next__()
            for row in csvfile_reader:
                self.data.append(row)

            # lower the column_names to make things more pythonic
            self.column_names = [x.lower() for x in self.column_names]

    def data_no_ids(self):
        return (row[1:] for row in self.data)

    def map_data_to_column_names(self):
        return (dict(zip(self.column_names, row)) for row in self.data)

    def map_data_to_column_names_no_id(self):
        return (dict(zip(self.column_names[1:], row)) for row in self.data_no_ids())
