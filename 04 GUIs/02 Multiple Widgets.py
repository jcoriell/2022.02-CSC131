from tkinter import *

window = Tk()

label1 = Label(
    window, 
    text="A", 
    bg="red", 
    fg="white"
    ) # bg is for background
                                                       # fg is for font color
label1.pack(fill=X)  

label2 = Label(window, text="B", bg="green", fg="white")
label2.pack(fill=X)

label3 = Label(window, text="C", bg="blue", fg="white")
label3.pack(fill=X)

window.mainloop()
