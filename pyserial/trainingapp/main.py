from cross_validate import *
from training_process import *
from training_app import training_app
import os

DATASET_FILE_DIRECTORY = "C:/Users/jvgcalites/Documents/GitHub/Testing/pyserial/trainingapp/datasets/"


def show_line():
    print("===========================================================================================================")


def choose_dataset_file():
    show_line()
    entries = os.listdir(DATASET_FILE_DIRECTORY)
    for entry in entries:
        print("[%s] %s" % (entries.index(entry), entry))
    file_select = int(input("Select a file to be used as dataset : "))
    while 0 > file_select > len(entries) - 1:
        file_select = int(input("Invalid response. Please try again : "))
    file_selected = entries[file_select]
    complete_file_name = os.path.join(DATASET_FILE_DIRECTORY, file_selected)
    return complete_file_name


def choose_existing_project(existing_projects):
    chosen_project = int(input("Select an existing project : "))
    while 0 > chosen_project > len(existing_projects) - 1:
        chosen_project = int(input("Invalid response. Please try again"))
    project_selected = existing_projects[chosen_project]
    print("You have chosen: %s %s %s " % (project_selected[1], project_selected[2], project_selected[3]))
    return project_selected


def show_optimal_k(accuracies):
    highest_accuracy = 0
    for accuracy in accuracies:
        # get the highest accuracy
        if accuracy[1] > highest_accuracy:
            highest_accuracy = accuracy[1]
            optimal_k = accuracy[0]
    print(accuracies)
    print("Optimal K = " + str(optimal_k))
    return optimal_k


if __name__ == '__main__':
    ta = training_app()
    show_line()
    print("[1] Create a new project")
    print("[2] Open existing project")

    response = input("What would you like to do? : ")
    while response != "1" and response != "2":
        response = input("Invalid response. Please try again. : ")

    if response == "1":
        show_line()
        project_name = input("Enter the name of the project : ")
        dataset_file = choose_dataset_file()
        project_id = ta.save_project(project_name, dataset_file)
    if response == "2":
        existing_projects = ta.show_all_projects()
        project = choose_existing_project(existing_projects)
        project_id = project[0]
        dataset_file = project[3]

    show_line()
    # returns list of accuracy for each K
    accuracy_list = cross_validate(dataset_file)
    optimal_k = show_optimal_k(accuracy_list)

    show_line()
    test_name = input("Give a new test name: ")
    while test_name != "x":
        # returns a 2d list of labels and its prediction ratio
        label_list = training_process(dataset_file, optimal_k)
        print(label_list)

        # returns list of accuracy for each K
        accuracy_list = cross_validate(dataset_file)
        show_optimal_k(accuracy_list)

        save_data = input("Should we save the file?")
        if save_data == "y":
            test_id = ta.save_test(test_name, project_id)
            ta.save_label_test(test_id, label_list)
            ta.save_k_test(test_id, accuracy_list)
        show_line()
        test_name = input("Give a new test name: ")
