import mysql.connector


mydb = mysql.connector.connect(
    host = "127.0.0.2",
    user = "root",
    password = "Rishabh#"
)

mycursor = mydb.cursor()

mycursor.execute("Create database if not exists std_info")
mycursor.execute("Use std_info")

mycursor.execute("Create table if not exists std_data (first_name VARCHAR(30), middle_name VARCHAR(30), last_name VARCHAR(30), roll_no VARCHAR(30))"
)

mycursor.execute(
    "Insert into std_data (first_name, last_name, roll_no) values('Rishabh','Goel', '17/ICS/073')"
)
mydb.commit()

mycursor.execute("Select * from std_data")

result = mycursor.fetchall()

print(result)
