from tkinter import *

WIDTH = 300
HEIGHT = 300

window = Tk()

label1 = Label(window, text="A label")
label1.grid(row=0, column=0, sticky=E)

label2 = Label(window, text="B label akfjghakjkjdfjk")
label2.grid(row=1, column=0)

entry1 = Entry(window)
entry1.grid(row=0, column=1)

entry2 = Entry(window)
entry2.grid(row=1, column=1)

window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("WORKING WITH GRID!")
window.mainloop()