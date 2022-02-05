from tkinter import *

window = Tk()       # the window is a Tk object
text = Label(window, text="Hello World! (again)") # creates a label widget and attaches it to..
                                                # the window

text.pack()     # pack is a geometry manager. 

window.mainloop()
