import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='Localhost',
                                         database='trainingapp',
                                         user='root',
                                         password='2015104503')
    cursor = connection.cursor()
    cursor.callproc('GetAllFiles')
    # print results
    print("Printing laptop details")
    for result in cursor.stored_results():
        print(result.fetchall())

except mysql.connector.Error as error:
    print("Failed to execute stored procedure: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")