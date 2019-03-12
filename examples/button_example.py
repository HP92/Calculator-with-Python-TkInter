import tkinter as tk

root = tk.Tk()

my_label = tk.Label(root, text="My Label")
my_label.pack()

# defining the callback (event) handler for the button
def click_me():
    action.configure(text="** I have been clicked **")
    my_label.configure(foreground='red')

# adding a button
action = tk.Button(root, text="Click ME!", command=click_me)
action.pack()

root.mainloop()