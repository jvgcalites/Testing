from database import *


class training_app:

    def __init__(self):
        self.da = dataAccess()

    # save a project, then return the project id
    def save_project(self, project_name, dataset_file):
        self.da.call_add_project(project_name, dataset_file)
        project_list = self.da.call_get_all_project()
        for project in project_list:
            if project[1] == project_name:
                project_id = project[0]
                print(project[0])
        return project_id

    # save a test, then return the test id
    def save_test(self, test_name, project_id):
        self.da.call_add_test(test_name, project_id)
        test_list = self.da.call_get_all_test()
        test_id = 0
        for test in test_list:
            if test[1] == test_name:
                if test[2] == project_id:
                    test_id = test[0]
                    print(test_id)
        return test_id

    # save the list of label and its right and total prediction in label_test table
    # if label is not yet saved, add one to the label table
    def save_label_test(self, test_id, label_list):
        # check if label already exists
        label_exists = False
        stored_labels = self.da.call_get_all_label()
        for label in label_list:
            for label_name in stored_labels:
                if label[0] == label_name[1]:
                    label_exists = True
            if not label_exists:
                self.da.call_add_label(label[0])
            label_exists = False

        # store all contents of label_list
        for label in label_list:
            self.da.call_add_label_test(test_id, label[0], label[1], label[2])

    # add the list of k and its accuracies to k_test table
    # if k is not saved yet, add one to the k table
    def save_k_test(self, test_id, accuracy_list):
        # check if label already exists
        k_exists = False
        stored_k = self.da.call_get_all_k()
        for k in accuracy_list:
            for k_sample in stored_k:
                if k[0] == k_sample[1]:
                    k_exists = True
            if not k_exists:
                self.da.call_add_k(k[0])
            k_exists = False

        # store all contents of label_list
        for k_test in accuracy_list:
            self.da.call_add_k_test(test_id, k_test[0], k_test[1])


if __name__ == '__main__':
    ta = training_app()
    #ta.save_k_test(9, [[1, 99.243], [3, 99.243], [5, 99.243], [7, 99.243], [9, 99.243]])
    #ta.save_label_test(9, [['A', 5, 5], ['B', 5, 5], ['C', 5, 5], ['D', 5, 5], ['E', 5, 5], ])




