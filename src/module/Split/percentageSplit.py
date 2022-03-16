# TODO: Add validation if percentage exceed
# TODO: validate the emailId against the existence

from src.Database import DatabaseConnector
from src.module.Operation.Add import AddTransaction

connecttoDB = DatabaseConnector.connectDB()
sqlclient = connecttoDB.cursor()

def percentSplit(groupName, emailId, amount,description, splitDictionarypercents):
    Dict = {}
    for email, amnt in splitDictionarypercents.items():
        Dict[email] = (amount*amnt)/100
    AddTransaction(groupName, emailId, description, Dict)

# should be removed once the test cases are added
'''
Local_dict={'basamanas@gmail.com': 30, 'raghu@gmail.com': 89, 'tall@gmail.com': 60}
percentSplit('Hawaii Trip', 'basamanas@gmail.com',300,"Lunch", Local_dict)
'''