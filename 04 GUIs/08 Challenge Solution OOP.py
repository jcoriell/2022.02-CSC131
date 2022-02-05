from tkinter import *

class ChallengeGUI(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

    def setup_GUI(self):
        l1 = Label(self.master, text="A Label")
        l1.grid(row=0, column=0, sticky=W)

        l2 = Label(self.master, text="Another Label")
        l2.grid(row=1, column=0, sticky=W)

        l3 = Label(self.master, text="A third label, centered")
        l3.grid(row=2, column=0, columnspan=2)

        img = PhotoImage(file="smile.gif") # note Photoimage only handles gifs
        l4 = Label(self.master, image=img)
        l4.image = img      # only have to do this when PhotoImage is part of a function
        l4.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=NSEW)

        entry1 = Entry(self.master)
        entry1.grid(row=0, column=1)

        entry2 = Entry(self.master)
        entry2.insert(0, 'user input')
        entry2.grid(row=1, column=1)

        c1 = Checkbutton(self.master, text="Some Checkbutton option")
        c1.grid(row=3, column=0, columnspan=2, sticky=W)

        b1 = Button(self.master, text="A button")
        b1.grid(row=3, column=2)

        b2 = Button(self.master, text="Another button")
        b2.grid(row=3, column=3)


window = Tk()
# window.geometry(f"{WIDTH}x{HEIGHT}")

ch = ChallengeGUI(window)
ch.setup_GUI()

window.mainloop()