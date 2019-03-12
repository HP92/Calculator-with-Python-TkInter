import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as mBox   # importing messagebox

root = tk.Tk()
root.title("My Python GUI APP")

def _quit():
    root.quit()
    root.destroy()  
    exit()

# defining the callback for the "About" command
def _about():
    mBox.showinfo("About 'My Python GUI APP'","This is our Python GUI APP,\ncreated with tkinter.\n\nVersion 1.0.0")
menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
# linking the callback to the command
help_menu.add_command(label="About", command=_about)
menu_bar.add_cascade(label="Help", menu=help_menu)


root.mainloop()