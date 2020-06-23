import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Rishabh#",
    database = "mydatabase"
)

mycursor = mydb.cursor()
#Created a database:
mycursor.execute("CREATE DATABASE mydatabase")

#Added table customers:
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), address VARCHAR(20))")

#Added one row into customers:
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John","Highway 21")
mycursor.execute(sql, val)

#Used to commit changes to the database:
mydb.commit()

#print the row count that were inserted:
print(mycursor.rowcount, "record inserted.")
