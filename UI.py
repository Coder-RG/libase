from tkinter import *

root = Tk()
root.title("Student Data")

heading = Label(root, text="Student Data")
details = Frame(root, padx=10, pady=10)
testing = Frame(root, padx=10, pady=10)

#Contains the function for needed for the command option in Label

def retrieve():
    Label(testing, text=first_name_entry.get()).pack()
    Label(testing, text=middle_name_entry.get()).pack()
    Label(testing, text=last_name_entry.get()).pack()
    Label(testing, text=roll_entry.get()).pack()

#Contains all the text fields
first_name = Label(details, text="First Name: ")
first_name_entry = Entry(details)

middle_name = Label(details, text="Middle Name:")
middle_name_entry = Entry(details)

last_name = Label(details, text="Last Name: ")
last_name_entry = Entry(details)

roll = Label(details, text="Book Title")
roll_entry = Entry(details)

test = Button(testing, text="Test here!", command=retrieve)

more_options = Button(details, text="Show more fields? Click Here!")

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
