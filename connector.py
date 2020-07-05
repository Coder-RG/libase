import mysql.connector


mydb = mysql.connector.connect(
    host = "127.0.0.2",
    port = "3306",
    user = "root",
    password = "Rishabh#",
    database = "std_info"
)

mycursor = mydb.cursor()

# mycursor.execute("Create database if not exists std_info")
# mycursor.execute("Use std_info")
#
# mycursor.execute("Create table if not exists std_data (first_name VARCHAR(30), middle_name VARCHAR(30), last_name VARCHAR(30), roll_no VARCHAR(30))"
# )
#
# mycursor.execute(
#     "Insert into std_data (first_name, last_name, roll_no) values('Rishabh','Goel', '17/ICS/073')"
# )
# mydb.commit()

mycursor.execute("Select * from std_data")

result = mycursor.fetchall()

for x in result:
    print(x)


# class Student():
#     def __init__(self, first_name, middle_name, last_name, roll_no):
#         self.first_name = first_name
#         self.middle_name = middle_name
#         self.last_name = last_name
#         self.roll_no = roll_no
#
#     def add_to_db(self):
