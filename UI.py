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
# mycursor.execute("Drop database std_info")
# mycursor.execute("Create database if not exists std_info")
# mycursor.execute("Drop table if exists std_info")
# mycursor.execute("Create table if not exists std_data (first_name VARCHAR(30), middle_name VARCHAR(30), last_name VARCHAR(30), roll_no VARCHAR(30))"
# )
# mycursor.execute("Update std_data set middle_name='NONE' where middle_name=''")
# mydb.commit()

#Creating the widgets
root = Tk()
root.title("Student Data")
root.geometry("500x400")

frame_menu = Frame(root, padx=5,bd=5, bg="#696969")
frame_menu.pack(side=LEFT, fill=BOTH)
Button(frame_menu, text="Add Data", width=10, bg="#FFFFFF").grid(row=0, column=0, padx=2, pady=2)
Button(frame_menu, text="Modify Data", width=10, bg="#FFFFFF").grid(row=1, column=0, padx=2, pady=2)
Button(frame_menu, text="View Data", width=10, bg="#FFFFFF").grid(row=2, column=0, padx=2, pady=2)

frame_main = Frame(root, padx=5, bd=5, bg="#EEE8AA")
frame_main.pack(side=LEFT, fill=BOTH, expand=True)

Label(frame_main, text="Student Data", font=("Pacifico", "30"), bg="#EEE8AA", anchor=CENTER).grid(row=0, column=0, columnspan=8)

#Contains the function needed for the command option in Button
lst = ['First Name', "Middle Name", "Last Name", "Roll No", "Batch", "Specialzation", "State", "City"]
def retrieve():
    view_data = Frame(frame_main, bg="#EEE8AA")
    view_data.grid(row=8, column=0, columnspan=4)
    query = "Select * from std_data"
    mycursor.execute(query)
    result = mycursor.fetchall()
    for index, name in enumerate(lst):
        Label(view_data, text=name, bg="#EEE8AA", font=("12")).grid(row=0, column=index, padx=5, pady=5)
    for x in range(len(result)):
        for index, y in enumerate(result[x]):
            Label(view_data, text=y, bg="#EEE8AA", anchor=W, font=("12")).grid(row=x+1, column=index)

def add_to_db():
    val = [
        first_name_entry.get(),
        middle_name_entry.get(),
        last_name_entry.get(),
        roll_entry.get()
    ]
    if not any(val):
        return 1
    elif not all(val):
        for index, x in enumerate(val):
            if not x:
                val[index] = "NONE"
    query = "Insert into std_data values (%s,%s,%s,%s)"
    mycursor.execute(query, val)
    mydb.commit()
    return 0
    # Label(root, text=mycursor.rowcount).grid(row=6, column=1)

def clean():
    first_name_entry.delete(0, END)
    middle_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    roll_entry.delete(0, END)

#Contains all the text fields
first_name = Label(frame_main, text="First Name", width=11, bg="#EEE8AA", anchor=W)
first_name_entry = Entry(frame_main, width=25)

middle_name = Label(frame_main, text="Middle Name", width=11, bg="#EEE8AA", anchor=W)
middle_name_entry = Entry(frame_main, width=25)

last_name = Label(frame_main, text="Last Name", width=11, bg="#EEE8AA", anchor=W)
last_name_entry = Entry(frame_main, width=25)

roll = Label(frame_main, text="Roll No", width=11, bg="#EEE8AA", anchor=W)
roll_entry = Entry(frame_main, width=25)

batch = Label(frame_main, text="Batch", width=11, bg="#EEE8AA", anchor=W)
batch_entry = Entry(frame_main, width=25)

spec = Label(frame_main, text="Specializaton", width=11, bg="#EEE8AA", anchor=W)
spec_entry = Entry(frame_main, width=25)

state = Label(frame_main, text="State", width=11, bg="#EEE8AA", anchor=W)
state_entry = Entry(frame_main, width=25)

city = Label(frame_main, text="City", width=11, bg="#EEE8AA", anchor=W)
city_entry = Entry(frame_main, width=25)

test = Button(frame_main, text="Show data!", command=retrieve)
clear = Button(frame_main, text="Clear fields", command=clean)
submit = Button(frame_main, text="Submit", command=add_to_db)


#Placing the widgets using grid()
first_name.grid(row=1, column=0, sticky=W, padx=5, pady=5)
first_name_entry.grid(row=1, column=1, sticky=W, padx=5, pady=5)
middle_name.grid(row=1, column=2, sticky=W, padx=5, pady=5)
middle_name_entry.grid(row=1, column=3, sticky=W, padx=5, pady=5)
last_name.grid(row=1, column=4, sticky=W, padx=5, pady=5)
last_name_entry.grid(row=1, column=5, sticky=W, padx=5, pady=5)
roll.grid(row=2, column=0, sticky=W, padx=5, pady=5)
roll_entry.grid(row=2, column=1, sticky=W, padx=5, pady=5)
batch.grid(row=3, column=0, sticky=W, padx=5, pady=5)
batch_entry.grid(row=3, column=1, sticky=W, padx=5, pady=5)
spec.grid(row=4, column=0, sticky=W, padx=5, pady=5)
spec_entry.grid(row=4, column=1, sticky=W, padx=5, pady=5)
state.grid(row=5, column=0, sticky=W, padx=5, pady=5)
state_entry.grid(row=5, column=1, sticky=W, padx=5, pady=5)
city.grid(row=6, column=0, sticky=W, padx=5, pady=5)
city_entry.grid(row=6, column=1, sticky=W, padx=5, pady=5)
submit.grid(row=7, column=0, sticky=W, padx=5, pady=5)
test.grid(row=7, column=1, sticky=W, padx=5, pady=5)
clear.grid(row=7, column=2, sticky=W, padx=5, pady=5)



root.mainloop()
