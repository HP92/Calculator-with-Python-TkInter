import tkinter as tk

root = tk.Tk()

# creating a disabled check button

# assigning a variable. This will hold the state of the button
# the states are represented by 0 (unchecked) and 1 (checked)
check_button_disabled = tk.IntVar()
check_button_1 = tk.Checkbutton(root, text="Disabled", variable=check_button_disabled, state="disabled")
# pre-selecting it
check_button_1.select()
check_button_1.pack()

# creating an unchecked button

check_button_unchecked = tk.IntVar()
check_button_2 = tk.Checkbutton(root, text="UnChecked", variable=check_button_unchecked)
# un-checking the button (this is the default state)
check_button_2.deselect()
check_button_2.pack()

# creating a pre-checked button

check_button_checked = tk.IntVar()
check_button_3 = tk.Checkbutton(root, text="Checked", variable=check_button_checked)
# pre-selecting it
check_button_3.select()
check_button_3.pack()

root.mainloop()