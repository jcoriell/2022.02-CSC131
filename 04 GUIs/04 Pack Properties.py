from tkinter import *

WIDTH = 300
HEIGHT = 300

window = Tk()
label1 = Label(window, text="A", bg="red", fg="white") # bg is for background
                                                       # fg is for font color
label1.pack(side=LEFT, expand=1, fill=X)  

label2 = Label(window, text="B", bg="green", fg="white")
label2.pack(side=LEFT, expand=1, fill=BOTH)

label3 = Label(window, text="C", bg="blue", fg="white")
label3.pack(side=LEFT, expand=1, fill=X)

window.geometry(f"{WIDTH}x{HEIGHT}")
window.mainloop()
