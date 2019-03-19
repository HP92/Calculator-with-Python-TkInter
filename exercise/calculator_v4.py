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

# Our objects
class ScreenContainer(Frame):
    def __init__(self,root,nSide):
        Frame.__init__(self,root)
        self.pack(side=nSide)
        self.generateScreen()

    def generateScreen(self):
        self.screen = Label(self)
        self.screen["text"]="0"
        self.screen.config(height=10,width=20)
        self.screen.pack(side="top")

    def getScreen(self):
        return self.screen


class ButtonsContainer(Frame):
    def __init__(self,root,nSide,screen):
        Frame.__init__(self,root)
        self.pack(side=nSide)
        self.generate_buttons(screen)

    # Method to store our values in the label
    def interactWithScreen(self,character,screen):
        if str(character) is 'C':
            screen["text"] = 0
            return
        elif str(character) is '=':
            screen["text"] = self.numEqualClick(screen["text"])
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
    def numEqualClick(self,screen):
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

    def generate_buttons(self,screen):
        row_num = 0
        col_num = 0

        for num in range(17):
            if(col_num==4):
                col_num = 0
                row_num += 1

            # creating a partial function.
            action_with_arg = partial(self.interactWithScreen, SYMBOLS_DICT[num],screen)
            numButton = Button(self,text=SYMBOLS_DICT[num],background=COLOT_BTN)
            numButton.config(height = HEIGHT_BTN, width = WIDTH_BTN,command= action_with_arg)
            numButton.grid(column=col_num,row=row_num)
            if(num==0):
                numButton.grid(column=col_num,row=row_num,columnspan = 4 )
                numButton.config(height = HEIGHT_BTN, width = WIDTH_BTN * 5)
                row_num += 1
                col_num = 0
                continue
            col_num += 1

class MainWindow(Tk):
    def __init__(self,title):
        Tk.__init__(self)
        self.title(title)
        self.resizable(0,0)

        myScreen = ScreenContainer(self,"top")
        myButtons = ButtonsContainer(self,"bottom",myScreen.getScreen())

        self.bind_kb_listener(self,myButtons, myScreen.getScreen())

        self.mainloop()

    def bind_kb_listener(self,root,buttons, screen):
        # keyboard listener
        def key_press(event):
            if event.char in [str(val) for val in SYMBOLS_DICT.values()]:
                buttons.interactWithScreen(event.char, screen)

        root.bind('<KeyRelease>', key_press)

def main():
    print("Welcome to python course for building calculator")
    myWindow = MainWindow("Calculator")

if __name__ == '__main__':
    main()
