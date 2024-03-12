import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Sub123@#'
)

# create a cursor object
cursorObject = db.cursor()

# create a database
cursorObject.execute("CREATE DATABASE dreamkitchen")

print("Database created successfully")
