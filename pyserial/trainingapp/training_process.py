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


def record_wrong_predictions(filename, data, correct_label):
    # store it in a file
    f = open(filename, "a+")
    f.write("%s,%s\n" % (data, correct_label))
    f.close()


def add_separate_line(filename):
    f = open(filename, "a+")
    f.write("===================================================================")
    f.close()



def training_process(filename, k):
    dataset = load_csv(filename)
    for i in range(len(dataset[0]) - 1):
        str_column_to_float(dataset, i)
    # convert class column to integers
    labels = str_column_to_int(dataset, len(dataset[0]) - 1)
    dictList = []
    for key, value in labels.items():
        temp = [key, value]
        dictList.append(temp)

    record_list = list()
    label_list = [['A', 0, 0]]
    correct_prediction = 0
    wrong_prediction = 0

    # define model parameter
    num_neighbors = k
    ser = serial.Serial('COM5', baudrate=9600, timeout=1)
    validate = ""
    i = 0
    while validate != "xxx":
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
            predict_label = ''
            for x in dictList:
                if x[1] == label:
                    predict_label = x[0]
            # print('Data=%s, Predicted: %s' % (row, predict_label))
            print('Predicted: %s' % predict_label)

            # ask if the label is correct
            validate = input("Is the predicted label correct? (Y/N): ")
            if validate == 'Y':
                # store it in a file
                f = open(filename, "a+")
                f.write("%s,%s\n" % (data, predict_label))
                f.close()
                correct_prediction += 1
                # =========Saving label ==============
                label_exists = False
                # traverse through the list and check if label already exists
                for label in label_list:
                    if label[0] == predict_label:
                        label_exists = True
                        index = label_list.index(label)
                # check if the label is in the list
                if label_exists:
                    label_list[index] = [predict_label, label_list[index][1] + 1, label_list[index][2] + 1]
                else:
                    label_list.append([predict_label, 1, 1])
            # add the value
            elif validate == 'N':
                # store it in a separate file
                correct_label = input("Enter the correct label: ")
                # store it in a file
                f = open(filename, "a+")
                f.write("%s,%s\n" % (data, correct_label))
                f.close()
                wrong_prediction += 1
                # ================= added shit ==================
                record_wrong_predictions("wrong.txt", data, correct_label)
                # =========Saving label ==============
                label_exists = False
                # traverse through the list
                for label in label_list:
                    if label[0] == correct_label:
                        label_exists = True
                        index = label_list.index(label)
                # check if the label is in the list
                if label_exists:
                    label_list[index] = [correct_label, label_list[index][1], label_list[index][2] + 1]
                else:
                    # if the label is not in the list
                    label_list.append([correct_label, 0, 1])
            else:
                print("Data not saved")

            record_list.append(wrong_prediction)

    add_separate_line("wrong.txt")
    print("Correct Predictions: %s" % correct_prediction)
    print("Wrong Predictions: %s" % wrong_prediction)
    return label_list
