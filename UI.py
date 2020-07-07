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

# mycursor.execute("Create database if not exists std_info")
# mycursor.execute("Create table if not exists std_data (first_name VARCHAR(30), middle_name VARCHAR(30), last_name VARCHAR(30), roll_no VARCHAR(30))")
# mydb.commit()

#Creating the widgets
root = Tk()
root.title("Student Data")
root.geometry("500x400")

lst = ["First Name", "Middle Name", "Last Name", "Roll No", "Batch", "Specializaton", "State", "City"]
list_labels = ["first_name", "middle_name", "last_name", "roll_no", "batch", "specialization", "state", "city"]

def add_data_op():
    global frame_main
    try:
        frame_main.destroy()
    except:
        pass
    frame_main = Frame(root, padx=5, bd=5, bg="#EEE8AA")
    frame_main.pack(side=LEFT, fill=BOTH, expand=True)
    Label(frame_main, text="Student Data", font=("Pacifico", "30"), bg="#EEE8AA", anchor=CENTER).grid(row=0, column=0, columnspan=8)
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

    list_var = [first_name_entry, middle_name_entry, last_name_entry, roll_entry, batch_entry, spec_entry, state_entry, city_entry]

    def clean():
        for name in list_var:
            name.delete(0, END)

    def add_to_db():
        val = [name.get() for name in list_var]
        if not any(val):
            return 1
        elif not all(val):
            for index, x in enumerate(val):
                if not x:
                    val[index] = "NONE"
        query = "Insert into std_data values (%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(query, val)
        mydb.commit()

    def retrieve():
        view_data = Frame(frame_main, bg="#EEE8AA")
        view_data.grid(row=8, column=0, columnspan=4)
        query = "Select * from std_data"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for index, name in enumerate(lst):
            Label(view_data, text=name, bg="#EEE8AA").grid(row=0, column=index, padx=5, pady=5)
        for x in range(len(result)):
            for index, y in enumerate(result[x]):
                Label(view_data, text=y, bg="#EEE8AA", anchor=W).grid(row=x+1, column=index)

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

def view_data_op():
    # global list_labels
    global frame_main
    try:
        frame_main.destroy()
    except:
        pass
    frame_main = Frame(root, padx=5, bd=5, bg="#EEE8AA")
    frame_main.pack(side=LEFT, fill=BOTH, expand=True)
    heading = Label(frame_main, text="Student Data", font=("Pacifico", "30"), bg="#EEE8AA")
    heading.pack()#grid(row=0, column=0, columnspan=8)
    v = [IntVar() for _ in range(8)]
    for index, name in enumerate(lst):
        Checkbutton(frame_main, text=name, variable=v[index], bg="#EEE8AA", width=10, anchor=W).pack()

    def get_selected_options():
        view_data = Frame(frame_main, bg="#EEE8AA")
        view_data.pack()
        values = [value.get() for value in v]
        selected = [name for name, value in zip(list_labels, values) if value]
        selected_text = ','.join(selected)
        query = "Select {} from std_data".format(selected_text)
        mycursor.execute(query)
        result = mycursor.fetchall()
        for index, name in enumerate(selected):
            Label(view_data, text=name, bg="#EEE8AA").grid(row=0, column=index)
        for x in range(len(result)):
            for index, y in enumerate(result[x]):
                Label(view_data, text=y, bg="#EEE8AA", anchor=W).grid(row=x+1, column=index)

    selected_options = Button(frame_main, text="Submit", command=get_selected_options)
    selected_options.pack()


def modify_data_op():
    pass

frame_menu = Frame(root, padx=5,bd=5, bg="#696969")
frame_menu.pack(side=LEFT, fill=BOTH)
add_data = Button(frame_menu, text="Add Data", width=10, bg="#FFFFFF", command=add_data_op)
add_data.grid(row=0, column=0, padx=2, pady=2)
modify_data = Button(frame_menu, text="Modify Data", width=10, bg="#FFFFFF", command=modify_data_op)
modify_data.grid(row=1, column=0, padx=2, pady=2)
view_data = Button(frame_menu, text="View Data", width=10, bg="#FFFFFF", command=view_data_op)
view_data.grid(row=2, column=0, padx=2, pady=2)

root.mainloop()
