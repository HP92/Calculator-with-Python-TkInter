from tkinter import *
from tkinter import ttk
from functools import partial

# Our Constant variables
HEIGHT_BTN = 5
WIDTH_BTN = 5
COLOT_BTN = "gray"
SYMBOLS_DICT = {
            0:'C',
            1:9,
            2:8,
            3:7,
            4:chr(247),
            5:6,
            6:5,
            7:4,
            8:'x',
            9:3,
            10:2,
            11:1,
            12:'-',
            13:0,
            14:'.',
            15:'=',
            16:'+'
        }

# Our methods/functions
# Method to store our values in the label
def interactWithScreen(character,screen):
    if str(character) is 'C':
        screen["text"] = 0
        return
    elif str(character) is '=':
        screen["text"] = numEqualClick(screen["text"])
        return
    # If statment to not allow to add two plus symbols or minus and etc.
    #elif str(screen["text"])[-1]==chr(247) or str(screen["text"])[-1]=='x' or str(screen["text"])[-1]=='+' or str(screen["text"])[-1]== '-':
    #    return
    elif str(screen["text"])[0]!="0":
        screen["text"] = str(screen["text"]) + str(character)
        return
    else:
        if "Error" is str(screen["text"]):
            screen["text"] = " "
        screen["text"] = character
        return

# Function to calculate the result
def numEqualClick(screen):
    # make sure we work with strings (will remove some errors with replace method on int)
    screen = str(screen)
    result = 0
    # replace operators
    screen = screen.replace("x","*")
    screen = screen.replace(chr(247),"/")
    try:
        result = eval(screen)
    except ZeroDivisionError:
        result = "Error: Cannot divide by zero"
    return result

def generate_buttons(container1_buttons,screen):
    row_num = 0
    col_num = 0

    for num in range(17):
        if(col_num==4):
            col_num = 0
            row_num += 1

        # creating a partial function.
        action_with_arg = partial(interactWithScreen, SYMBOLS_DICT[num],screen)
        numButton = Button(container1_buttons,text=SYMBOLS_DICT[num],background=COLOT_BTN)
        numButton.config(height = HEIGHT_BTN, width = WIDTH_BTN,command= action_with_arg)
        numButton.grid(column=col_num,row=row_num)
        if(num==0):
            numButton.grid(column=col_num,row=row_num,columnspan = 4 )
            numButton.config(height = HEIGHT_BTN, width = WIDTH_BTN * 5)
            row_num += 1
            col_num = 0
            continue
        col_num += 1

def bind_kb_listener(root, screen):
    # keyboard listener
    def key_press(event):
        if event.char in [str(val) for val in SYMBOLS_DICT.values()]:
            interactWithScreen(event.char, screen)

    root.bind('<KeyRelease>', key_press)


    
def main():
    print("Welcome to python course for building calculator")

    root = Tk() # Our "TopLevel" container
    root.title("Calculator") #Setting attributes on our container like title
    root.resizable(0, 0)

    container1_buttons = Frame(root) # Creating a container for the buttons of the app
    container1_buttons.pack(side="bottom")

    container2_screen = Frame(root) # Creating a container for the screen of the app
    container2_screen.pack(side="top")

    screen = Label(container2_screen)
    screen["text"]="0"
    screen.config(height=10,width=20)
    screen.pack(side="top")

    generate_buttons(container1_buttons,screen)
    bind_kb_listener(root, screen)

    root.mainloop() # Execute the TopLevel container

if __name__ == '__main__':
    main()
