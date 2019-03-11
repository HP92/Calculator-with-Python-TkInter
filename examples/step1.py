import tkinter as tk

def clickMe():
    action.configure(text="** I have been Clicked! **")
    screen.configure(foreground='red')

# Generate the window
win = tk.Tk()
# Change attributes of the window
win.title("Calculator")
win.resizable(0,0)

# Adding a label which will be our screen
screen = tk.Label(win,text="Welcome to our program")
screen.grid(column=0,row=0)

# Adding buttons
action = tk.Button(win,text="Click Me!",command=clickMe)
action.grid(column=1,row=0)

# Run the window
win.mainloop()
