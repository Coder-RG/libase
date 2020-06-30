import tkinter as tk

window = tk.Tk()

# greeting = tk.Label(
#     text='Hello!',
#     foreground='white',
#     background='black',
#     width=10,
#     height=10
# )
# greeting.pack()

# button = tk.Button(
#     text='ckick me!',
#     width=25,
#     height=5,
#     bg='blue',
#     fg='yellow'
# )
# button.pack()
#
# entry = tk.Entry(
#     fg='yellow',
#     bg='blue',
#     width=50
# )
# entry.pack()

label = tk.Label(text="Name")
entry = tk.Entry()
label.pack()
entry.pack()
name = entry.get()


# window.mainloop()
