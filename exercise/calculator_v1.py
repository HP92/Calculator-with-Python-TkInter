from tkinter import *

HEIGHT_BTN = 5
WIDTH_BTN = 5

def num1Click(event):
    screen["text"] = 1

def num2Click(event):
    screen["text"] = 2

def num3Click(event):
    screen["text"] = 3

def num4Click(event):
    screen["text"] = 4

def num5Click(event):
    screen["text"] = 5

def num6Click(event):
    screen["text"] = 6

def num7Click(event):
    screen["text"] = 7

def num8Click(event):
    screen["text"] = 8

def num9Click(event):
    screen["text"] = 9

def num0Click(event):
    screen["text"] = 0

def numPlusClick(event):
    screen["text"] = '+'

def numMinusClick(event):
    screen["text"] = '-'

def numMultiClick(event):
    screen["text"] = 'x'

def numDivClick(event):
    screen["text"] = chr(247)

def numCommaClick(event):
    screen["text"] = '.'

def numEqualClick(event):
    screen["text"] = '='


def generate_buttons(container1_buttons):
    button1 = Button(container1_buttons) # Creating the button for num1
    # Setting the attributes
    button1["text"] = "1"
    button1["background"] = "gray"
    button1.grid(column=1,row=1)
    button1.config(height = HEIGHT_BTN, width = WIDTH_BTN)
    button1.bind("<Button-1>",num1Click)

    button2 = Button(container1_buttons) # Creating the button for num1
    # Setting the attributes
    button2["text"] = "2"
    button2["background"] = "gray"
    button2.grid(column=2,row=1)
    button2.config(height = HEIGHT_BTN, width = WIDTH_BTN)
    button2.bind("<Button-1>",num2Click)

    button3 = Button(container1_buttons) # Creating the button for num1
    # Setting the attributes
    button3["text"] = "3"
    button3["background"] = "gray"
    button3.grid(column=3,row=1)
    button3.config(height = HEIGHT_BTN, width = WIDTH_BTN)
    button3.bind("<Button-1>",num3Click)

    button4 = Button(container1_buttons) # Creating the button for num1
    # Setting the attributes
    button4["text"] = "4"
    button4["background"] = "gray"
    button4.grid(column=1,row=2)
    button4.config(height = HEIGHT_BTN, width = WIDTH_BTN)
    button4.bind("<Button-1>",num4Click)

    button5 = Button(container1_buttons) # Creating the button for num1
    # Setting the attributes
    button5["text"] = "5"
    button5["background"] = "gray"
    button5.grid(column=2,row=2)
    button5.config(height = HEIGHT_BTN, width = WIDTH_BTN)
    button5.bind("<Button-1>",num5Click)

    button6 = Button(container1_buttons) # Creating the button for num1
    # Setting the attributes
    button6["text"] = "6"
    button6["background"] = "gray"
    button6.grid(column=3,row=2)
    button6.config(height = HEIGHT_BTN, width = WIDTH_BTN)
    button6.bind("<Button-1>",num6Click)

    button7 = Button(container1_buttons) # Creating the button for num1
    # Setting the attributes
    button7["text"] = "7"
    button7["background"] = "gray"
    button7.grid(column=1,row=3)
    button7.config(height = HEIGHT_BTN, width = WIDTH_BTN)
    button7.bind("<Button-1>",num7Click)

    button8 = Button(container1_buttons) # Creating the button for num1
    # Setting the attributes
    button8["text"] = "8"
    button8["background"] = "gray"
    button8.grid(column=2,row=3)
    button8.config(height = HEIGHT_BTN, width = WIDTH_BTN)
    button8.bind("<Button-1>",num8Click)

    button9 = Button(container1_buttons) # Creating the button for num1
    # Setting the attributes
    button9["text"] = "9"
    button9["background"] = "gray"
    button9.grid(column=3,row=3)
    button9.config(height = HEIGHT_BTN, width = WIDTH_BTN)
    button9.bind("<Button-1>",num9Click)

    buttonZero = Button(container1_buttons) # Creating the button for num1
    # Setting the attributes
    buttonZero["text"] = "0"
    buttonZero["background"] = "gray"
    buttonZero.grid(column=1,row=4)
    buttonZero.config(height = HEIGHT_BTN, width = WIDTH_BTN)
    buttonZero.bind("<Button-1>",num0Click)

    buttonComma = Button(container1_buttons) # Creating the button for num1
    # Setting the attributes
    buttonComma["text"] = "."
    buttonComma["background"] = "gray"
    buttonComma.grid(column=2,row=4)
    buttonComma.config(height = HEIGHT_BTN, width = WIDTH_BTN)
    buttonComma.bind("<Button-1>",numCommaClick)

    buttonEqual = Button(container1_buttons)
    buttonEqual.config(height=HEIGHT_BTN,width=WIDTH_BTN,text="=",background="gray")
    buttonEqual.grid(column=3,row=4)
    buttonEqual.bind("<Button-1>",numEqualClick)

    buttonPlus = Button(container1_buttons)
    buttonPlus.config(height=HEIGHT_BTN,width=WIDTH_BTN,text="+",background="gray")
    buttonPlus.grid(column=4,row=4)
    buttonPlus.bind("<Button-1>",numPlusClick)

    buttonMinus = Button(container1_buttons)
    buttonMinus.config(height=HEIGHT_BTN,width=WIDTH_BTN,text="-",background="gray")
    buttonMinus.grid(column=4,row=3)
    buttonMinus.bind("<Button-1>",numMinusClick)

    buttonMultiply = Button(container1_buttons)
    buttonMultiply.config(height=HEIGHT_BTN,width=WIDTH_BTN,text="X",background="gray")
    buttonMultiply.grid(column=4,row=2)
    buttonMultiply.bind("<Button-1>",numMultiClick)

    buttonDivision = Button(container1_buttons)
    buttonDivision.config(height=HEIGHT_BTN,width=WIDTH_BTN,text=chr(247),background="gray")
    buttonDivision.grid(column=4,row=1)
    buttonDivision.bind("<Button-1>",numDivClick)


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
