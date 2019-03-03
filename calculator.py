import tkinter as tk

def clickMe():
    action.configure(text="** I have been Clicked! **")
    screen.configure(foreground='red')

def generate_buttons(window):
    # Adding buttons
    num_buttons = []
    for number in range(1,10):
        newButton = tk.Button(window,text=number)
        for row_num in range(3):
            for col_num in range(3):
                newButton.grid(column=col_num,row=row_num)
        num_buttons.append(newButton)

    print(num_buttons)

def main():
    # Generate the window
    win = tk.Tk()
    # Change attributes of the window
    win.title("Calculator")
    win.resizable(0,0)

    # Adding a label which will be our screen
    screen = tk.Label(win,text="Welcome to our program")
    screen.grid(column=0,row=0)

    # Adding buttons
    generate_buttons(win)

    # Run the window
    win.mainloop()

if __name__ == "__main__":
    main()
