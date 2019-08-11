# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 21:09:32 2019

@author: Minghan Li 13105
"""
import Tkinter as Tk

color = "orange"
past_color = "blue"

WIDTH = 800.0
HEIGHT = 800.0  # the board is going to stay 800x800, the sizes of rectangles depend on n

test_n = 5

class knights_tour_game(object):
    def __init__(self, master, n):
        self.master = master
        self.current_row = -1 # constantly update position when the user clicks the right position
        self.current_column = -1
        self.canvas = Tk.Canvas(master, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.rectangles = [[self.canvas.create_rectangle\
                            (i*800.0/n,j*800.0/n,i*800.0/n+800.0/n,j*800.0/n+800.0/n, fill="white")\
                            for i in range(n)] for j in range(n)]
        self.canvas.bind("<Button-1>", self.orange_cell)
        
    def change_color(self, c, row, column):
        self.canvas.itemconfig(self.rectangles[row][column], fill= c)
    
    def orange_cell(self, event):
        for a in range (len(self.rectangles)):
            for b in range(len(self.rectangles)):
                my_coords = self.canvas.coords(self.rectangles[a][b])
                if (event.x >= my_coords[0] and event.y >= my_coords[1]
                    and event.x < my_coords[2] and event.y < my_coords[3]):
                    if self.current_column < 0:
                        self.change_color(color, a,b)
                        self.current_row = a
                        self.current_column = b
                    elif ((abs(a-self.current_row)==1 and abs(b-self.current_column)==2)
                            or (abs(a-self.current_row)==2 and abs(b-self.current_column)==1)):
                            self.change_color(color, a,b)
                            self.change_color(past_color,self.current_row,self.current_column)
                            self.current_row = a
                            self.current_column = b
                    else:
                        print "Please click again!"
 
def knights_tour(n):
    root = Tk.Tk()
    knights_tour_game(root,n)
    root.mainloop()
    root.destroy()
    
def main(): 
    knights_tour(n)
    
if __name__ == '__main__':
    main()
