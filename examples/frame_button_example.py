import tkinter as tk

root = tk.Tk()

myContainer1 = tk.Frame(root)      # (1)
myContainer1.pack()                # (2)

# new code
button1 = tk.Button(myContainer1)  # (3)
button1["text"]= "Hello, World!"   # (4)
button1["background"] = "green"    # (5)
button1.pack()                     # (6)
#

root.mainloop()