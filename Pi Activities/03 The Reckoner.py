from tkinter import *

button_data = [
    {"row": 1, "col": 0, "value": "("},
    {"row": 1, "col": 1, "value": ")"},
    {"row": 1, "col": 2, "value": "AC"},
    {"row": 1, "col": 3, "value": "**"},

    {"row": 2, "col": 0, "value": "7"},
    {"row": 2, "col": 1, "value": "8"},
    {"row": 2, "col": 2, "value": "9"},
    {"row": 2, "col": 3, "value": "/"},

    {"row": 3, "col": 0, "value": "4"},
    {"row": 3, "col": 1, "value": "5"},
    {"row": 3, "col": 2, "value": "6"},
    {"row": 3, "col": 3, "value": "*"},

    {"row": 4, "col": 0, "value": "1"},
    {"row": 4, "col": 1, "value": "2"},
    {"row": 4, "col": 2, "value": "3"},
    {"row": 4, "col": 3, "value": "-"},

    {"row": 5, "col": 0, "value": "0"},
    {"row": 5, "col": 1, "value": "."},
    {"row": 5, "col": 2, "value": "="},
    {"row": 5, "col": 3, "value": "+"},

]


USING_RPI = False

class MainGUI(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        if USING_RPI:
            master.attributes("-fullscreen", True)
        self.setupGUI()

    def make_button(self, row, col, value):
        bg_color = "#cccccc"
        if value == "=":
            bg_color = "blue"

        button = Button(
            self,
            font=("TexGyreAdventor", 30),
            text = value,
            bg=bg_color,
            highlightbackground=bg_color,   # for macs
            borderwidth=0,
            highlightthickness=0,
            width=5,
            activebackground="white",
            command= lambda : self.handle_button_press(value)
        )

        button.grid(row=row, column=col, sticky=NSEW)

    def setupGUI(self):
        # setup the display and manage its geometry (grid)
        self.display = Label(self, text="", anchor=E, bg="white", fg="black", height=1, font=("TexGyreAdventor", 40))
        self.display.grid(row=0, column=0, columnspan=4, sticky=NSEW)

        # configure our rows and columns
        for row in range(7):
            Grid.rowconfigure(self, row, weight=1)
        
        for col in range(4):
            Grid.columnconfigure(self, col, weight=1)

        # create the buttons
        for button in button_data:
            self.make_button(button["row"], button["col"], button["value"])

        # manage the gui's geometry (pack)
        self.pack(fill=BOTH, expand=1)

        # keep track of error or calculation
        self.errored = False
        self.calculated = False

    def handle_button_press(self, button_value):
        display = self.display["text"]
        clear = button_value == "AC"
        evaluate = button_value == "="
        numeric = button_value in list("0123456789")

        if clear:
            self.display["text"] = ""
            return

        if evaluate:
            try:
                result = str(eval(display))
                self.display["text"] = result
                self.calculated = True
            except:
                self.display["text"] = "ERROR"
                self.errored = True

            return

        if self.errored:
            self.display["text"] = ""
            self.errored = False
            self.display["text"] += button_value
            return

        if self.calculated and numeric:
            self.display["text"] = ""
            self.calculated = False
            self.display["text"] += button_value
            return

        self.display["text"] += button_value
        self.calculated = False
        return
        

window = Tk()
window.title("Reckoner")
r = MainGUI(window)
window.mainloop()



