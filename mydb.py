import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'CocoMonAnge123#.'
)

# Prepare Cursor Object
cursorObject = dataBase.cursor()

#create Database
cursorObject.execute("CREATE DATABASE consolejayco")

print("Database Created")