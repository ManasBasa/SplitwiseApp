from src.Database import DatabaseConnector

connecttoDB = DatabaseConnector.connectDB()
sqlclient = connecttoDB.cursor()


def createUser(uid, passwd, email):
    sql = 'insert into users(uname, passwd, emailId) values (%s,%s,%s)'
    values = (uid, passwd, email)
    sqlclient.execute(sql, values)
    connecttoDB.commit()
    print("user created successfully")

# Remove when test cases are added
'''
createUser("manas", "test", "test@gmail.com")
'''

def validateUserCredentials(uid, passwd):
    sql = 'Select passwd from users where uname=\'' + str(uid) + "\'"
    sqlclient.execute(sql)
    result = sqlclient.fetchone()
    if passwd == result[0]:
        return "true"


def validateUserExistence(id):
    sql = 'Select 1 from users where emailId=\"' + str(id) + "\""
    sqlclient.execute(sql)
    result = sqlclient.fetchone()
    if result is not None:
        if result[0] == 1:
            return "true"
    else:
        return "false"


