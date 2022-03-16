# TODO: validate the emailId against the existence
# TODO: Validate the group Name existence

from src.Database import DatabaseConnector
from src.module.Operation.Add import AddTransaction

connecttoDB = DatabaseConnector.connectDB()
sqlclient = connecttoDB.cursor()


def exactSplit(groupName, emailId, description, emailIdToAmountDict):
    Dict = {}
    for email, amount in emailIdToAmountDict.items():
        Dict[email] = amount
    AddTransaction(groupName, emailId, description, Dict)


# should be removed once the test cases are added
'''
Local_dict={'test@gmail.com': 30.0, 'test2@gmail.com': 89.0, 'test3@gmail.com': 60.0}
exactSplit('Hawaii Trip', 'basamanas@gmail.com',"Lunch", Local_dict)
'''
