
# images
from tkinter import *

window = Tk()

l1 = Label(window, text="A Label")
l1.grid(row=0, column=0, sticky=W)

l2 = Label(window, text="Another Label")
l2.grid(row=1, column=0, sticky=W)

l3 = Label(window, text="A third label, centered")
l3.grid(row=2, column=0, columnspan=2)

img = PhotoImage(file="smile.gif") # note Photoimage only handles gifs
l4 = Label(window, image=img)
l4.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=NSEW)

entry1 = Entry(window)
entry1.grid(row=0, column=1)

entry2 = Entry(window)
entry2.insert(0, 'user input')
entry2.grid(row=1, column=1)

c1 = Checkbutton(window, text="Some Checkbutton option")
c1.grid(row=3, column=0, columnspan=2, sticky=W)

b1 = Button(window, text="A button")
b1.grid(row=3, column=2)

b2 = Button(window, text="Another button")
b2.grid(row=3, column=3)

window.mainloop()