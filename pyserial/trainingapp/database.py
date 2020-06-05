from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


class dataAccess(object):

    def __init__(self):
        self.db_config = read_db_config()
        self.conn = MySQLConnection(**self.db_config)
        self.cursor = self.conn.cursor()

    def call_get_all_project(self):
        try:
            self.cursor.callproc('get_all_project')

            # print out the result
            for result in self.cursor.stored_results():
                print(result.fetchall())

        except Error as e:
            print(e)

    def call_get_all_test(self):
        try:
            self.cursor.callproc('get_all_test')
            for result in self.cursor.stored_results():
                print(result.fetchall())
        except Error as e:
            print(e)

    def call_get_all_k(self):
        try:
            self.cursor.callproc('get_all_k')
            for result in self.cursor.stored_results():
                print(result.fetchall())
        except Error as e:
            print(e)

    def call_get_all_label(self):
        try:
            self.cursor.callproc('get_all_label')
            for result in self.cursor.stored_results():
                print(result.fetchall())
        except Error as e:
            print(e)

    def call_get_all_k_test(self):
        try:
            self.cursor.callproc('get_all_k_test')
            for result in self.cursor.stored_results():
                print(result.fetchall())
        except Error as e:
            print(e)

    def call_get_all_label_test(self):
        try:
            self.cursor.callproc('get_all_label_test')
            for result in self.cursor.stored_results():
                print(result.fetchall())
        except Error as e:
            print(e)

    def call_add_project(self, project, dataset_file):
        proc_name = 'add_project'
        args = (project, dataset_file)
        try:
            self.cursor.callproc(proc_name, args)
            print(self.cursor.rowcount, " record inserted.")
            self.conn.commit()
        except Error as e:
            print(e)

    def call_add_test(self, test_name, project_id):
        proc_name = 'add_test'
        args = (test_name, project_id)
        try:
            self.cursor.callproc(proc_name, args)
            print(self.cursor.rowcount, " record inserted.")
            self.conn.commit()
        except Error as e:
            print(e)

    def call_add_k(self, k_sample):
        proc_name = 'add_k'
        args = (k_sample, )
        try:
            self.cursor.callproc(proc_name, args)
            print(self.cursor.rowcount, " record inserted")
            self.conn.commit()
        except Error as e:
            print(e)

    def call_add_label(self, label_name):
        proc_name = 'add_label'
        args = (label_name, )
        try:
            self.cursor.callproc(proc_name, args)
            print(self.cursor.rowcount, " record inserted")
            self.conn.commit()
        except Error as e:
            print(e)

    def call_add_label_test(self, test_id, label_id, right_predict, total_predict):
        proc_name = 'add_label_test'
        args = (test_id, label_id, right_predict, total_predict)
        try:
            self.cursor.callproc(proc_name, args)
            print(self.cursor.rowcount, " record inserted")
            self.conn.commit()
        except Error as e:
            print(e)

    def call_add_k_test(self, test_id, k_id, accuracy):
        proc_name = 'add_k_test'
        args = (test_id, k_id, accuracy)
        try:
            self.cursor.callproc(proc_name, args)
            print(self.cursor.rowcount, " record inserted")
            self.conn.commit()
        except Error as e:
            print(e)

    def close_database(self):
        self.conn.close()
        self.cursor.close()


if __name__ == '__main__':
    da = dataAccess()
    # da.call_add_project("testProject", "data.txt")
    # da.call_add_test("testTest", 1)
    # da.call_add_label('A')
    # da.call_add_k(1)
    # da.call_add_label_test(2, 1, 1, 2)
    # da.call_add_k_test(2, 1, 97.012)
    da.call_get_all_project()
    da.call_get_all_k()
    da.call_get_all_k_test()
    da.call_get_all_label()
    da.call_get_all_label_test()
    da.call_get_all_test()

    da.close_database()
