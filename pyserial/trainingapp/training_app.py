from database import dataAccess


class training_app(object):

    def __init__(self):
        self.da = dataAccess()

    def save_project(self, project_name, dataset_file):
        self.da.call_add_project(project_name, dataset_file)

    def save_test(self, test_name, project_id):
        self.da.call_add_test(test_name, project_id)
        return self.da.call_get_test(test_name, project_id)


    def save_label_test(self, test_id, label_list, accuracy_list):
        # sample input = (test_name_1, 'A', 45, 50)
        self.da.call_add_test_label(test_id, label, right_predict, wrong_predict)
    def save_k_test(self, test_id:
        # sample input = (test_name_1, 1, 99.99)
        self.da.call_add_test_k(test_id, k, accuracy)

