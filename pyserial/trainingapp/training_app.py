from cross_validate import *
from training_process import *
from database import dataAccess
import os
DATASET_FILE_DIRECTORY = "C:/Users/jvgcalites/Documents/GitHub/Testing/pyserial/trainingapp/datasets/"


def open_existing_project():
    # TODO
    # show all the projects available
    da = dataAccess()
    project_list = da.call_get_all_project()
    da.close_database()
    # ask the user to select one
    open_project = input("Select one from existing projects : ")
    while 0 > project_select > len(entries) - 1:
        file_select = input("Invalid response. Please try again : ")
    # get the project's dataset file
    # return file name of the chosen project
    return dataset_file

def create_new_project():
    # ask for name of the project
    project_name = input("Enter the name of the project : ")

    # ask for dataset file
    entries = os.listdir(DATASET_FILE_DIRECTORY)
    for entry in entries:
        print("[%s] %s" %(entries.index(entry), entry))
    file_select = int(input("Select a file to be used as dataset : "))
    while 0 > file_select > len(entries) - 1:
        file_select = input("Invalid response. Please try again : ")
    file_selected = entries[file_select]

    # save to database
    da = dataAccess()
    da.call_add_project(project_name, file_selected)
    da.close_database()

    return file_selected

def show_optimal_k(accuracies):
    highest_accuracy = 0
    for accuracy in accuracies:
        # get the highest accuracy
        if accuracy[1] > highest_accuracy:
            highest_accuracy = accuracy[1]
            k = accuracy[0]
    print(accuracies)
    print("Optimal K = " + str(k))


if __name__ == '__main__':
    print("======Main Menu======")
    print("[1] Create a new project")
    print("[2] Open existing project")
    print("=====================")
    response = input("What would you like to do? : ")
    while response != "1" and response != "2":
        response = input("Invalid response. Please try again. : ")
    if response == "1":
        file_name = create_new_project()
    if response == "2":
        open_existing_project()

    # returns list of accuracy for each K
    accuracy_list = cross_validate(file_name)
    show_optimal_k(accuracy_list)

    i = 0
    test_name = input("Give a new test name: ")
    while test_name != "x":
        i += 1

        # returns a 2d list of labels and its prediction ratio
        label_list = training_process(file_name, k)
        print(label_list)

        # returns list of accuracy for each K
        accuracy_list = cross_validate(file_name)
        show_optimal_k(accuracy_list)

        save_data = input("Should we save the file?")
        if save_file == "y":
            # TODO
            save_data(test_name, label_list, accuracy_list)
        test_name = input("Give a new test name: ")





