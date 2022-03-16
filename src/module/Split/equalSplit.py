
from src.Database import DatabaseConnector
from src.module.Operation.Add import AddTransaction
connecttoDB = DatabaseConnector.connectDB()
sqlclient = connecttoDB.cursor()


def equalSplit(groupName, description, emailId, amount):
    sqltofetchgroupMembers = 'Select memberemailId from group_name where groupname=\'' + str(groupName) + "\'"
    sqlclient.execute(sqltofetchgroupMembers)
    NoOfMembers = sqlclient.fetchall()[0][0].split("-")
    amount = round(amount / (len(NoOfMembers) - 1), 2)
    Dict = {}
    for i in NoOfMembers:
        if i != '':
            Dict[i] = amount
    AddTransaction(groupName, emailId, description, Dict)

# should be removed once the test cases are added
'''
equalSplit('Hawaii Trip',"test@gmail.com","Lunch", 300)
'''