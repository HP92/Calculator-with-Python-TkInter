import tkinter as tk
from tkinter import Menu

root = tk.Tk()

# creating the callback for the File->Exit menu command
def _quit():
    root.quit()     # quits the tcl interpreter
    root.destroy()  # destroy this and all descendants widgets
    exit()          # exit python interpreter


# creating the menu_bar object
menu_bar = Menu(root)
root.config(menu=menu_bar)

# now we add a menu to the bar and also assign some menu items to the menu

# creating the menu object
# `tearoff` property eliminates the dotted line that is added by default
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")                 # adding "New" command
file_menu.add_separator()                          # adding a separator
file_menu.add_command(label="Exit", command=_quit) # adding "Exit" command
# inserting the file_menu menu, into a label File, attached to the menu_bar
menu_bar.add_cascade(label="File", menu=file_menu)

# adding the Help-About menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)


root.mainloop()