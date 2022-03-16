import mysql.connector  # run pip install mysql-connector-python

def connectDB():
    mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootroot",
        database="Splitwise"
    )
    return mysqldb