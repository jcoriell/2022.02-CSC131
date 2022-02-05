from tkinter import * 
from random import choice, randint

# constants
WIDTH = 400
HEIGHT = 400
POINT_COLORS = ["black", "red", "green", "blue"]
POINT_RADIUS = 0
NUM_POINTS = 2500

# our custom class
class Points(Canvas):
    
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    def plot_all_points(self, num_points):
        for i in range(num_points):
            x = randint(0, WIDTH - 1)
            y = randint(0, HEIGHT - 1)
            self.plot_point(x, y)


    def plot_point(self, x0, y0):
        rand_color = choice(POINT_COLORS)
        x1 = x0 + POINT_RADIUS * 2
        y1 = y0 + POINT_RADIUS * 2
        self.create_oval(x0, y0, x1, y1, outline=rand_color, fill=rand_color)

# main program

window = Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("POINTS!")

p = Points(window)
p.plot_all_points(NUM_POINTS)

window.mainloop()