from database import dataAccess


class training_app(object):

    def __init__(self):
        self.da = dataAccess()

    def save_project(self, project_name, dataset_file):
        self.da.call_add_project(project_name, dataset_file)

    def save_data(self, test_name, label_list, accuracy_list):

