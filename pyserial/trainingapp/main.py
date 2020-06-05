from cross_validate import *
from training_process import *
# from database import dataAccess
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


def choose_dataset_file():
    print("========================================================================================")
    entries = os.listdir(DATASET_FILE_DIRECTORY)
    for entry in entries:
        print("[%s] %s" % (entries.index(entry), entry))
    file_select = int(input("Select a file to be used as dataset : "))
    while 0 > file_select > len(entries) - 1:
        file_select = input("Invalid response. Please try again : ")
    file_selected = entries[file_select]
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
    print("============================================================================================")
    print("[1] Create a new project")
    print("[2] Open existing project")

    response = input("What would you like to do? : ")
    while response != "1" and response != "2":
        response = input("Invalid response. Please try again. : ")

    if response == "1":
        print("========================================================================================")
        project_name = input("Enter the name of the project : ")
        dataset_file = choose_dataset_file()
        # TODO
        project_id = save_project(project_name, dataset_file)
    if response == "2":
        open_existing_project()

    print("========================================================================================")
    # returns list of accuracy for each K
    accuracy_list = cross_validate(dataset_file)
    show_optimal_k(accuracy_list)

    print("========================================================================================")
    test_name = input("Give a new test name: ")
    test_id = save_test(test_name, project_id)
    while test_name != "x":
        # returns a 2d list of labels and its prediction ratio
        label_list = training_process(dataset_file, k)
        print(label_list)

        # returns list of accuracy for each K
        accuracy_list = cross_validate(dataset_file)
        show_optimal_k(accuracy_list)

        save_data = input("Should we save the file?")
        if save_file == "y":
            # TODO
            save_data(test_id, label_list, accuracy_list)
        print("========================================================================================")
        test_name = input("Give a new test name: ")
        test_id = save_test(test_id, project_id)
