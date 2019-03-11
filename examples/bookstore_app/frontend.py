"""
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

"""


import tkinter as tk
import backend as bknd  # custom module to import the backend functionality of the app


def get_selected_row(event):
    # the function has 1 param 'event' which will be passed automatically by tkinter.
    # we use the event just as a trigger in this case, then use the Listbox method to get the currently selected item
    global selected_row
    if list1.curselection():
        index = list1.curselection()[0]
        selected_row = list1.get(index)
        entries = [e1, e2, e3, e4]
        for e in entries:
            e.delete(0, tk.END)
            e.insert(tk.END, selected_row[entries.index(e) + 1])


def clear_entries():
    entries = [e1, e2, e3, e4]
    for e in entries:
        e.delete(0, tk.END)


def view_command():
    list1.delete(0, tk.END)
    for row in bknd.view():
        list1.insert(tk.END, row)


def search_command():
    list1.delete(0, tk.END)
    # input is taken from the input fields of the entry windows
    for row in bknd.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(tk.END, row)
    clear_entries()


def add_command():
    if title_text.get() == '' and author_text.get() == '' and year_text.get() == '' and isbn_text.get() == '':
        return
    bknd.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, tk.END)
    view_command()
    clear_entries()
    # list1.insert(tk.END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def delete_command():
    bknd.delete(selected_row[0])
    view_command()
    clear_entries()


def update_command():
    bknd.update(selected_row[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()
    clear_entries()


# create the blank window
window = tk.Tk()
window.wm_title('BookStore')
# create the labels and pin them to the grid (based on the layout)
l1 = tk.Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = tk.Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = tk.Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = tk.Label(window, text="ISBN")
l4.grid(row=1, column=2)

# create special data types to hold the user input value, which will be used in the entries
title_text = tk.StringVar()
year_text = tk.StringVar()
author_text = tk.StringVar()
isbn_text = tk.StringVar()

# create the entries and pin them to the grid (based on the layout)
e1 = tk.Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

e2 = tk.Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

e3 = tk.Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

e4 = tk.Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# create the listbox and pin it to the grid (based on the layout)
# specifying only list1.grid(row=2, column=0)K will not help, because it will occupy just that cell in the grid,
# so we need to indicate also how many cells we want it to span on x and y axis
list1 = tk.Listbox(window, height=10, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# create a scrollbar and pin it to the grid (based on the layout)
sb1 = tk.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# create a configure method to the scrollbar and the listbox to connect them
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# bind the special event <<ListboxSelect>> to the Listbox object. When event appears, the function will be called
# this will allow us to select a row from the Listbox, and get info out
list1.bind('<<ListboxSelect>>', get_selected_row)

# create the buttons and pin them to the grid (based on the layout)

b1 = tk.Button(window, text='View all', width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = tk.Button(window, text='Search entry', width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = tk.Button(window, text='Add entry', width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = tk.Button(window, text='Update', width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = tk.Button(window, text='Delete', width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = tk.Button(window, text='Close', width=12, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()
