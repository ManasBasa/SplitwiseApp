# use try catch before printing success message
from src.Database import DatabaseConnector

connecttoDB = DatabaseConnector.connectDB()
sqlclient = connecttoDB.cursor()


def makegroup(groupName, memberList):
    final_List =""
    for i in memberList:
        final_List=final_List+"-"+i
    sql = 'insert into group_name(groupname, memberemailId) values (%s,%s)'
    values = (groupName, final_List)
    sqlclient.execute(sql, values)
    connecttoDB.commit()
    print("group created successfully")
