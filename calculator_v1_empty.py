'''
Libraries to import
'''
from tkinter import *

'''
Constant Variables
'''
HEIGHT_BTN = 5
WIDTH_BTN = 5

'''
Function for the actions of the buttons.
'''
def num1Click(event):
    '''
    Add code for when we press number 1
    '''
    pass

def num2Click(event):
    pass

def num3Click(event):
    pass

def num4Click(event):
    pass

def num5Click(event):
    pass

def num6Click(event):
    pass

def num7Click(event):
    pass

def num8Click(event):
    pass

def num9Click(event):
    pass

def num0Click(event):
    pass

def numPlusClick(event):
    pass

def numMinusClick(event):
    pass

def numMultiClick(event):
    pass

def numDivClick(event):
    pass

def numCommaClick(event):
    pass

def numEqualClick(event):
    pass

'''
Functions for separiting code in parts
'''

def generate_buttons(container1_buttons):
    '''
    Add code for generating the buttons for a calculator
    '''
    pass

'''
Main Code for execution of our application
'''
print("Welcome to python course for building calculator")

root = Tk()                         # Our "TopLevel" container
root.title("Calculator")            #Setting attributes on our container like title

container1_buttons = Frame(root)    # Creating a container for the buttons of the app
container1_buttons.pack()           # Fill the correct value for the position of the
                                    # buttons
container2_screen = Frame(root)     # Creating a container for the screen of the app
container2_screen.pack()            # Fill the correct value for the position of
                                    # screen

screen =                            # Use widget to simulate a calcluator screen
                                    # What widget do you need?
generate_buttons(container1_buttons)

root.mainloop()                     # Execute the TopLevel container
