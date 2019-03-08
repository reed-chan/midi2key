#coding:utf-8

from tkinter import *

def setKey(key):
    print(key)

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.keyPanel()


    def keyPanel(self):
        keyName = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        ]
        for row in range(0, len(keyName)):
            for column in range(0, len(keyName[row])):
                self.keyButtonPanel(keyName[row][column], row, column)

    def keyButtonPanel(self, keyName, x, y):
            self.keyButton = Button(self, text=keyName, command=lambda: setKey(keyName),width=8,height=2)
            self.keyButton.grid(row=x, column=y)

app = Application()
#app.master.wm_maxsize(400,400)
app.master.title('Midi2Key')
app.mainloop()