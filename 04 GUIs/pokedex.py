from tkinter import *
from PIL import ImageTk, Image  # pip install pillow
import requests # pip install requests
from io import BytesIO

# Width and Height
WIDTH = 900
HEIGHT = 550

# Colors
WHITE = "#ffffff"
DARK_GREY = "#323232"
LIGHT_GREY = "#5c6370"

# Fonts
ARIAL_18 = ("Arial", 18)
ARIAL_14 = ("Arial", 14)
ARIAL_12 = ("Arial", 12)
ARIAL_12_BOLD = ("Arial", 18, "bold")

class MainGUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.setup_gui()
        self.pack(fill=BOTH, expand=1)

    def handle_submit(self):
        pokemon = self.entry.get().lower()
        self.entry.delete(0, END)
        
        if pokemon.isnumeric():
            pokemon = int(pokemon)

        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
            poke_data = response.json()  
            id = poke_data["id"]
            name = poke_data["name"].capitalize()
            image_url = poke_data["sprites"]["other"]["official-artwork"]["front_default"]
            
            res2 = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}")
            more_data = res2.json()

            flavor_text_entries = more_data["flavor_text_entries"]
            english_entries = []
            for entry in flavor_text_entries:
                if entry["language"]["name"] == "en":
                    english_entries.append(entry)

            if len(english_entries) != 0:
                description = english_entries[0]["flavor_text"].replace('\n', ' ')
            else:
                description = "No english description"   

            res3 = requests.get(image_url)
            image_data = res3.content
            
            img_file = BytesIO(image_data)
            PIL_img = Image.open(img_file)
            img = ImageTk.PhotoImage(PIL_img)
            self.panel["image"] = img
            self.panel.image = img

            self.id['text'] = str(id).zfill(3)
            self.name['text'] = name
            self.description['text'] = description
            
            
        except:
            img = ImageTk.PhotoImage(Image.open('pokeball.png').resize([500, 500]))
            self.panel["image"] = img
            self.panel.image = img
            
            self.id['text'] = "???"
            self.name['text'] = pokemon
            self.description["text"] = "Sorry, I don't know that Pokemon."


    def handle_return(self, event):
        self.handle_submit()

    def setup_gui(self):
        for row in range(10):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(10):
            Grid.columnconfigure(self, col, weight=1)

        # setup the place to hold the pokemon image
        PIL_image = Image.open('pokeball.png').resize([500, 500])
        img = ImageTk.PhotoImage(PIL_image)
        self.panel = Label(self, image=img, bg=DARK_GREY)
        self.panel.image = img 
        self.panel.grid(row=0, column=0, columnspan=5, sticky=NSEW)
        
        # display the id
        self.id = Label(self, fg=WHITE, bg=DARK_GREY, font=ARIAL_18, justify="left", padx=10)
        self.id.grid(row=0, column=5, columnspan=5, sticky=W)

        # display the name
        self.name = Label(self, fg=WHITE, bg=DARK_GREY, font=ARIAL_18, justify="left", padx=10)
        self.name.grid(row=1, column=5, columnspan=5, sticky=W)

        # description
        self.description = Label(self, fg=WHITE, bg=DARK_GREY, font=ARIAL_14, justify="left", wraplength=400, padx=10)
        self.description.grid(row=2, column=5, columnspan=5, sticky=W)

        # text field
        self.entry = Entry(self, fg=WHITE, bg=LIGHT_GREY, font=ARIAL_12)
        self.entry.bind('<Return>', self.handle_return)
        self.entry.grid(row=5, column=0, columnspan=8, sticky=EW)

        # button
        button = Button(self, text="Submit", fg=WHITE, bg=LIGHT_GREY, font=ARIAL_12_BOLD, command=self.handle_submit)
        button.grid(row=5, column=8, columnspan=2, sticky=NSEW)
        

window = Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")

p = MainGUI(window)
p.configure(bg = DARK_GREY)

window.mainloop()

