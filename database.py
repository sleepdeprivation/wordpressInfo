import mysql.connector
def getConnection(dbname):
    cnx = mysql.connector.connect(user='??', password='??',
                                  host='??',
                                  database=dbname)
    return cnx

