import mysql.connector
from tkinter import *

#Creating a connection to the database
mydb = mysql.connector.connect(
    host = "127.0.0.2",
    port = "3306",
    user = "root",
    password = "Rishabh#",
    database = "std_info"
)
mycursor = mydb.cursor()

mycursor.execute("Create database if not exists std_info")

mycursor.execute("Create table if not exists std_data (first_name VARCHAR(30), middle_name VARCHAR(30), last_name VARCHAR(30), roll_no VARCHAR(30))"
)

# mycursor.execute(
#     "Insert into std_data (first_name, last_name, roll_no) values('Rishabh','Goel', '17/ICS/073')"
# )
# mydb.commit()
# mycursor.execute("Select * from std_data")
# result = mycursor.fetchall()

root = Tk()
root.title("Student Data")

heading = Label(root, text="Student Data")
details = Frame(root, padx=10, pady=10)
testing = Frame(root, padx=10, pady=10)

#Contains the function for needed for the command option in Label

def retrieve():
    query = "Select * from std_data"
    mycursor.execute(query)
    result = mycursor.fetchall()
    for x in result:
        Label(testing, text=x).pack(side=TOP)

def add_to_db():
    val = (
        first_name_entry.get(),
        middle_name_entry.get(),
        last_name_entry.get(),
        roll_entry.get()
    )
    query = "Insert into std_data values (%s,%s,%s,%s)"
    mycursor.execute(query, val)
    mydb.commit()
    # Label(details, text=mycursor.rowcount).pack()

#Contains all the text fields
first_name = Label(details, text="First Name: ")
first_name_entry = Entry(details)

middle_name = Label(details, text="Middle Name:")
middle_name_entry = Entry(details)

last_name = Label(details, text="Last Name: ")
last_name_entry = Entry(details)

roll = Label(details, text="Book Title")
roll_entry = Entry(details)

test = Button(testing, text="Show data!", command=retrieve)

more_options = Button(details, text="Submit", command=add_to_db)

#Frames are shown using pack()
details.pack()
testing.pack()

#Objects in details using grid()
first_name.grid(row=0, column=0)
first_name_entry.grid(row=0, column=1)
middle_name.grid(row=1, column=0)
middle_name_entry.grid(row=1, column=1)
last_name.grid(row=2, column=0)
last_name_entry.grid(row=2, column=1)
roll.grid(row=3, column=0)
roll_entry.grid(row=3, column=1)
more_options.grid(row=4, column=0, columnspan=2)

#Objects in testing using pack()
test.pack()#(row=5, column=1)


root.mainloop()
