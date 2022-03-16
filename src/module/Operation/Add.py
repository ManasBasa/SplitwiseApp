# TODO Add validation for all values
from src.Database import DatabaseConnector

connecttoDB = DatabaseConnector.connectDB()
sqlclient = connecttoDB.cursor()


def AddTransaction(groupName,emailId, description, Dictionary):
    addedBy = emailId
    sql = 'insert into Transactions(groupName, emailId, amount,addedBy,Description) values (%s,%s,%s,%s,%s)'
    for emailId, amount in Dictionary.items():
        values = (groupName, emailId, amount, addedBy, description)
        sqlclient.execute(sql, values)
    connecttoDB.commit()
