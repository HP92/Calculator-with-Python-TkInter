import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# we create a basic label and pin it to the grid based on x,y coordinates
tk.Label(root, text="label on root").grid(column=0, row=7)

# we create a basic Frame and pin it to the root
tk_frame = tk.Frame(root)
tk_frame.grid(column=1, row=8)

# we create 3 basic labels, and pin them in an horizontal fashion inside the tk_frame
tk.Label(tk_frame, text="label_1").grid(column=0, row=0)
tk.Label(tk_frame, text="label_2").grid(column=1, row=0)
tk.Label(tk_frame, text="label_3").grid(column=2, row=0)

# we create a ttk Frame (it can have a title) and pin it to the root
ttk_frame = ttk.LabelFrame(root, text="My Label Frame")
ttk_frame.grid(column=1, row=9)

# we create 3 more basic Labels, and pin them in a vertical fashion inside the ttk_frame
tk.Label(ttk_frame, text="label_1").grid(column=0, row=0)
tk.Label(ttk_frame, text="label_2").grid(column=0, row=1)
tk.Label(ttk_frame, text="label_3").grid(column=0, row=2)

root.mainloop()