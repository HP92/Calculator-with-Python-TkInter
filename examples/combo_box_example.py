import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# we need a variable to store the value from the combobox
number = tk.StringVar()
number_chosen = ttk.Combobox(root, textvariable=number)
# we assign a tuple with default values, which will appear in the drop-down list
number_chosen['values'] = (1, 2, 4, 14, 100)
# we assign the default value based on the index of our list
number_chosen.current(0)

number_chosen.pack()

root.mainloop()