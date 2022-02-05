from tkinter import *

window = Tk()

style1 = {
    "bg": "red",
    "fg": "white"
}

style2 = {
    "bg": "green",
    "fg": "white"
}

# style1["bg"] <- how to get the value red

label1 = Label(window, text="A", **style1) # bg is for background
                                           # fg is for font color
label1.pack(fill=X)  

label2 = Label(window, text="B", **style2)
label2.pack(fill=X)

label3 = Label(window, text="C", bg="blue", fg="white")
label3.pack(fill=X)

window.mainloop()
