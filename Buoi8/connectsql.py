import mysql.connector

def getConnection():
    connection = mysql.connector.connect(host='localhost',
                                        user='root',
                                        passwd='root',
                                        database='Quanlyhocvien')

    return connection