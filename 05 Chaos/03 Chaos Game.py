from tkinter import * 
from random import choice, randint

# constants
WIDTH = 1000
HEIGHT = 1000
POINT_COLORS = ["black", "red", "green", "blue"]
POINT_RADIUS = 0
NUM_POINTS = 50000

# our custom class
class ChaosGame(Canvas):
    
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    def plot_all_points(self, num_points):
        # Plot the vertices of an equilateral triangle
        v1 = [0, HEIGHT - 1]
        v2 = [(WIDTH-1) / 2, 0]
        v3 = [WIDTH - 1, HEIGHT - 1]
        vertices = [v1, v2, v3]

        self.plot_point(v1[0], v1[1])
        self.plot_point(v2[0], v2[1])
        self.plot_point(v3[0], v3[1])
        
        # Choose two vertices (randomly)
        p1 = choice(vertices)
        p2 = choice(vertices)

        # Find the midpoint between them
        mid = [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]
        
        # Plot the midpoint
        self.plot_point(mid[0], mid[1])

        # Repeat for many times
        for _ in range(num_points):
            # Choose a random vertex
            p1 = choice(vertices)
            # Find the midpoint between previous midpoint and new vertex
            new_mid = [(p1[0]+mid[0])/2, (p1[1]+mid[1])/2]
            # plot new midpoint
            self.plot_point(new_mid[0], new_mid[1])
            # set old midpoint as new midpoint
            mid = new_mid


    def plot_point(self, x0, y0):
        rand_color = choice(POINT_COLORS)
        x1 = x0 + POINT_RADIUS * 2
        y1 = y0 + POINT_RADIUS * 2
        self.create_oval(x0, y0, x1, y1, outline=rand_color, fill=rand_color)

# main program

window = Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("POINTS!")

p = ChaosGame(window)
p.plot_all_points(NUM_POINTS)

window.mainloop()