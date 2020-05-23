from _csv import reader
from decimal import Decimal
import serial
from math import sqrt
import os
import matplotlib.pyplot as plt


# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
        # print('[%s] => %d' % (value, i))
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup


# Find the min and max values for each column
def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax


# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])


# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1):
        distance += (row1[i] - row2[i]) ** 2
    return sqrt(distance)


# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors


# Make a prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction


# Make a prediction with KNN on Iris Dataset
filename = 'data.txt'
dataset = load_csv(filename)
for i in range(len(dataset[0]) - 1):
    str_column_to_float(dataset, i)
# convert class column to integers
labels = str_column_to_int(dataset, len(dataset[0]) - 1)
dictList = []
for key, value in labels.items():
    temp = [key, value]
    dictList.append(temp)

recordList = list()
dataPoint = list()
correctPrediction = 0
wrongPrediction = 0
# define model parameter
num_neighbors = 5
ser = serial.Serial('COM5', baudrate=9600, timeout=1)
trainNum = 25
i = 0
while i < trainNum:
    raw_data = ser.readline().decode('ascii')
    if raw_data != "":
        i += 1
        # remove "#" and "~" and "/n"
        data = ""
        data = raw_data[1:len(data) - 3]
        # parse the data
        values = data.split(",")
        # contents of values array are string
        # convert them to double/decimal
        f1 = float(values[0])
        f2 = float(values[1])
        f3 = float(values[2])
        f4 = float(values[3])
        f5 = float(values[4])
        gx = float(values[5])
        gy = float(values[6])
        gz = float(values[7])
        ax = float(values[8])
        ay = float(values[9])
        az = float(values[10])

        # define a new record
        row = [f1, f2, f3, f4, f5, gx, gy, gz, ax, ay, az]
        # predict the label
        label = predict_classification(dataset, row, num_neighbors)
        predictLabel = ''
        for x in dictList:
            if x[1] == label:
                predictLabel = x[0]
        print('Data=%s, Predicted: %s' % (row, predictLabel))

        # ask if the label is correct
        validate = input("Is the predicted label correct? (y/n): ")
        if validate == 'y':
            # store it in a file
            f = open("data.txt", "a+")
            f.write("%s,%s\n" % (data, predictLabel))
            f.close()
            correctPrediction += 1
        elif validate == 'n':
            # store it in a separate file
            correctLabel = input("Enter the correct label: ")
            # store it in a file
            f = open("data.txt", "a+")
            f.write("%s,%s\n" % (data, correctLabel))
            f.close()
            wrongPrediction += 1
        else:
            print("ULET")
        recordList.append(wrongPrediction)

dataPoint = list(range(1, len(recordList) + 1, 1))
print("Correct Predictions: %s" % correctPrediction)
print("Wrong Predictions: %s" % wrongPrediction)
plt.plot(dataPoint, recordList, 'c')
plt.xlabel("Data Points")
plt.ylabel("Wrong Predictions")
plt.grid(True)
plt.show()
