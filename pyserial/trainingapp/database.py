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

    def call_add_project(self, project, dataset_file):
        proc_name = 'add_project'
        args = (project, dataset_file)
        try:
            self.cursor.callproc(proc_name, args)
            print(self.cursor.rowcount, " record inserted.")
            self.conn.commit()
        except Error as e:
            print(e)

    def close_database(self):
        self.conn.close()
        self.cursor.close()


if __name__ == '__main__':
    da = dataAccess()
    da.call_get_all_project()
    da.close_database()
