import tkinter as tk

root = tk.Tk()

# create a variable that will be bound to the Entry
name = tk.StringVar()
# create the Entry widget. We can use the width property to give 
# it a fixed size
name_entered = tk.Entry(root, width=12, textvariable=name)
name_entered.pack()

root.mainloop()