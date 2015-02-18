import csv

data = csv.reader(open("train.csv"))
header = next(data)
dataset = []

for row in data:
    dataset.append(row)

print(dataset)
