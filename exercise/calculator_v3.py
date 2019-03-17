from tkinter import *
from functools import partial

HEIGHT_BTN = 5
WIDTH_BTN = 5
COLOT_BTN = "gray"

def interactWithScreen(character):
    print("interactWithScreen = " + str(character))
    if character == 'C':
        screen["text"] = 0

    if str(screen["text"])[0]!="0":
        screen["text"] = str(screen["text"]) + str(character)
    else:
        screen["text"] = character

def actionNumButton(symbol):
    interactWithScreen(symbol)

# def numClearClick(event):
#     screen["text"] = '0'
#
# def numEqualClick(event):
#     temp = screen["text"]
#
#     temp = temp.replace("x","*")
#     temp = temp.replace(chr(247),"/")
#
#     result = eval(str(temp))
#     screen["text"] = result

def generate_buttons(container1_buttons):
    symbols_dict = {
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

    row_num = 0
    col_num = 0

    for num in range(17):
        if(col_num==4):
            col_num = 0
            row_num += 1

        action_with_arg = partial(actionNumButton, symbols_dict[num])
        numButton = Button(container1_buttons,text=symbols_dict[num],background=COLOT_BTN)
        numButton.config(height = HEIGHT_BTN, width = WIDTH_BTN,command= action_with_arg)
        numButton.grid(column=col_num,row=row_num)
        if(num==0):
            row_num += 1
            col_num = 0
            continue
        col_num += 1

print("Welcome to python course for building calculator")

root = Tk() # Our "TopLevel" container
root.title("Calculator") #Setting attributes on our container like title

container1_buttons = Frame(root) # Creating a container for the buttons of the app
container1_buttons.pack(side="bottom")

container2_screen = Frame(root) # Creating a container for the screen of the app
container2_screen.pack(side="top")

screen = Label(container2_screen)
screen["text"]="0"
screen.config(height=10,width=20)
screen.pack(side="top")

generate_buttons(container1_buttons)

root.mainloop() # Execute the TopLevel container
