'''
A program that stores this book information:
Title, Author
Year, ISBN

User can:
- view all records
- search an entry
- add entry
- update entry
- delete
- close

See app_layout.png for a sketch layout.

THIS IS JUST THE FRONT END - with no connection to backend
'''


import tkinter as tk
import backend   # custom module to import the backend functionality of the app

# create the blank window
window = tk.Tk()

# create the labels and pin them to the grid (based on the layout)
l1 = tk.Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = tk.Label(window, text="Year")
l2.grid(row=0, column=2)

l3 = tk.Label(window, text="Author")
l3.grid(row=1, column=0)

l4 = tk.Label(window, text="ISBN")
l4.grid(row=1, column=2)

# create special data types to hold the user input value, which will be used in the entries
title_text = tk.StringVar()
year_text = tk.StringVar()
author_text = tk.StringVar()
ISBN_text = tk.StringVar()

# create the entries and pin them to the grid (based on the layout)
e1 = tk.Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

e2 = tk.Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

e3 = tk.Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

e4 = tk.Entry(window, textvariable=ISBN_text)
e4.grid(row=1, column=3)

# create the listbox and pin it to the grid (based on the layout)
# specifying only list1.grid(row=2, column=0) will not help, because it will occupy just that cell in the grid,
# so we need to indicate also how many cells we want it to span on x and y axis
list1 = tk.Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# create a scrollbar and pin it to the grid (based on the layout)
sb1 = tk.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# create a configure method to the scrollbar and the listbox to connect them
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# create the buttons and pin them to the grid (based on the layout)

b1 = tk.Button(window, text='View all', width=12)
b1.grid(row=2, column=3)

b2 = tk.Button(window, text='Search entry', width=12)
b2.grid(row=3, column=3)

b3 = tk.Button(window, text='Add entry', width=12)
b3.grid(row=4, column=3)

b4 = tk.Button(window, text='Update', width=12)
b4.grid(row=5, column=3)

b5 = tk.Button(window, text='Delete', width=12)
b5.grid(row=6, column=3)

b6 = tk.Button(window, text='Close', width=12)
b6.grid(row=7, column=3)


window.mainloop()

