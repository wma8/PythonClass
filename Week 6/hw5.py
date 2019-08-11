#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:14:39 2019

@author: jiaruijiang
"""

'''
Ideas:
    create an n*n chekerboard on canvas, with each block has Length length.
    draw squares with white filling at the beginning?
    
    class for square? need a fucntion like update(), to update color after current 
    squre move to new position
    need a status variable to show "visited" or "not yet". once set "visited", update()
    will turn color to blue
    
    check validity?
    give each block a coordinate(x,y), like index of matrix element. 
    1. check if click within border
    2. check if the clicked block has coordinate(x,y) that complies with rules
    
    check click position?
    mouse may click on any place
    actual coodincate / length of block, no rounding, to get block coordinate
    
'''

import Tkinter as Tk
SquareLength = 15

class Knight(object):
    def __init__(self, master, num):
        self.master = master
        self.canvas = Tk.Canvas(master, width=num*SquareLength, height=num*SquareLength, bg="white")
        self.canvas.pack()
        #create Num*Num rectangels? yes
        
'''
i = w.create_line(xy, fill="red")

w.coords(i, new_xy) # change coordinates
w.itemconfig(i, fill="blue") # change color

w.delete(i) # remove

w.delete(ALL) # remove all items

#modify square color
'''
class Square(object):
    @staticmethod
    def position_to_index(pos_x, pos_y):
        return (pos_x/SquareLength+1, pos_y/SquareLength+1)
        
    def position(self):
        pass
    def __init__(self, canvas,idx_x, idx_y): #take index of each square,start from 0,0
        self.status = 'not'
        self.canvas = canvas
        self.shape = self.canvas.create_rectangle(pos_x, pos_y, 
                                        pos_x+SquareLength, pos_y+SquareLength, fill='white')
        self.pos = self.canvas.coords(self.shape)
    def get_status(self):
        return self.status
    
print(Square.position_to_index(150, 225))  # Should print (11, 16) or (10, 15)

def knights_tour(n): 
    root = Tk.Tk()
    game = Knight(root,n)
    root.mainloop()
    
