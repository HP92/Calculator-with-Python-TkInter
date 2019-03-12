import tkinter as tk

root = tk.Tk()

my_listbox = tk.Listbox(root)
for item in ["one", "two", "three", "four"]:
    my_listbox.insert(tk.END, "Choice " + item)
my_listbox.pack()

root.mainloop()