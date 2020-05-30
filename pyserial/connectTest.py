from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def call_add_files(fileName):

    proc_name = 'add_files'
    args = (fileName, )

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        # execute the query
        cursor = conn.cursor()
        cursor.callproc(proc_name, args)

        print(cursor.rowcount, " record inserted.")

        # accept the change
        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def call_get_all_files():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        cursor.callproc('get_all_files')

        # print out the result
        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    call_get_all_files()
    call_add_files('fileName3')