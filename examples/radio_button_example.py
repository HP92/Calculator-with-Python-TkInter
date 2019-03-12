import tkinter as tk

root = tk.Tk()

# defining some global variables
# the values assigned, are tkinter keywords for colors
COLOR1 = "Red"
COLOR2 = "Blue"

# defining radio button callback
def radioCall():
    radio_select = radio_variable.get()
    if   radio_select == 1: root.configure(background=COLOR1)
    elif radio_select == 2: root.configure(background=COLOR2)

# creating a variable to store the values of the radio buttons
# we use a common one, so that it is easier to use it in our callback
radio_variable = tk.IntVar()
radio_1 = tk.Radiobutton(root, text=COLOR1, variable=radio_variable, value=1, command=radioCall)
radio_1.pack()

radio_2 = tk.Radiobutton(root, text=COLOR2, variable=radio_variable, value=2, command=radioCall)
radio_2.pack()

root.mainloop()