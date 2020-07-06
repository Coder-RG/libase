import mysql.connector
from tkinter import *

#Creating a connection to the database
mydb = mysql.connector.connect(
    host = "127.0.0.2",
    port = "3306",
    user = "root",
    password = "Rishabh#",
)
mycursor = mydb.cursor()

mycursor.execute("Create database if not exists std_info")
mycursor.execute("Use std_info")
mycursor.execute("Drop table if exists std_info")

mycursor.execute("Create table if not exists std_data (first_name VARCHAR(30), middle_name VARCHAR(30), last_name VARCHAR(30), roll_no VARCHAR(30))"
)

#Creating the widgets
root = Tk()
root.title("Student Data")
root.geometry("400x400")

Label(root, text="Student Data").grid(row=0, column=0, columnspan=2)

#Contains the function needed for the command option in Button

def retrieve():
    query = "Select * from std_data"
    mycursor.execute(query)
    result = mycursor.fetchall()
    for x in result:
        Label(root, text=x).grid(row=6, column=0)

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
first_name = Label(root, text="First Name: ")
first_name_entry = Entry(root)

middle_name = Label(root, text="Middle Name:")
middle_name_entry = Entry(root)

last_name = Label(root, text="Last Name: ")
last_name_entry = Entry(root)

roll = Label(root, text="Roll No")
roll_entry = Entry(root)

test = Button(root, text="Show data!", command=retrieve)

submit = Button(root, text="Submit", command=add_to_db)


#Objects in details using grid()
first_name.grid(row=1, column=0, sticky=W, padx=5, pady=5)
first_name_entry.grid(row=1, column=1, sticky=W, padx=5, pady=5)
middle_name.grid(row=2, column=0, sticky=W, padx=5, pady=5)
middle_name_entry.grid(row=2, column=1, sticky=W, padx=5, pady=5)
last_name.grid(row=3, column=0, sticky=W, padx=5, pady=5)
last_name_entry.grid(row=3, column=1, sticky=W, padx=5, pady=5)
roll.grid(row=4, column=0, sticky=W, padx=5, pady=5)
roll_entry.grid(row=4, column=1, sticky=W, padx=5, pady=5)
submit.grid(row=5, column=0, sticky=W, padx=5, pady=5)
test.grid(row=5, column=1, sticky=W, padx=5, pady=5)


root.mainloop()
