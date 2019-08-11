#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 13:44:25 2019

@author: jiaruijiang
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:14:39 2019

@author: jiaruijiang
"""

'''
Ideas:
    create an n*n chekerboard on canvas, with each block has Length length. done
    draw squares with white filling at the beginning? done
    
    class for square? need a fucntion like update(), to update color after current 
    squre move to new position
    need a status variable to show "visited" or "not yet". once set "visited", update()
    will turn color to blue
    
    check validity?
    give each block a coordinate(x,y), like index of matrix element. 
    1. check if click within border (done)
    2. check if the clicked block has coordinate(x,y) that complies with rules (done using index)
    
    check click position?
    mouse may click on any place
    actual coodincate / length of block, no rounding, to get block coordinate
    
    !!!next step: functions to detect mouse click, transfer to index, get update!!!
    
'''

import Tkinter as Tk
import numpy as np
SquareLength = 30

class Square(object):
    #@staticmethod
   # def position_to_index(pos_x, pos_y):
   #     return (pos_x/SquareLength, pos_y/SquareLength) #since index starts from 0, no need to plus one
        
   # def position(self):
   #     pass
    def __init__(self, canvas,idx_x, idx_y): #take index of each square,start from 0,0
        self.status = 'not'
        self.canvas = canvas
        self.shape = self.canvas.create_rectangle(idx_x*SquareLength, idx_y*SquareLength, 
                                        (idx_x+1)*SquareLength, (idx_y+1)*SquareLength, fill='white')
        self.pos = self.canvas.coords(self.shape)
        self.index = (idx_x,idx_y)
    def get_status(self):
        return self.status
    def current_visit(self):
        self.status = 'current_visit'
    def visited(self):
        self.status = 'visited'
    def get_idx(self):
        return self.index
    
    
class Knight(object):
    previous_idxX = 0
    previous_idxY = 0
    count = 0
    def __init__(self, master, num): #create canvas, array for square storage, lay out white square, done
        self.num = num
        self.master = master
        self.Width = num*SquareLength
        self.canvas = Tk.Canvas(master, width=self.Width, height=self.Width, bg="white")
        self.canvas.pack()
        #create Num*Num rectangels? yes
        self.Square_group = np.empty([num, num], dtype=object) # a np array of square objects,with index-storage
        for i in range(num):
            for j in range(num):
                self.Square_spawner(i,j)
        self.canvas.bind("<Button-1>", self.move)    
        
    def Square_spawner(self,idxX, idxY): #create a square as indicated by index, store in array
        a_square = Square(self.canvas, idxX, idxY)
        self.Square_group[idxY][idxX] = a_square #store the new squre into the numpy array of square objects
                                                #note, idxX determines column, idxY determines row
        
    def Update_Square_current(self,idxX, idxY): #if square visited current round, update color to yellow
        self.canvas.itemconfig(self.Square_group[idxY][idxX],fill = "yellow")
        
    def Update_Square_visited(self,idxX, idxY): #if square visited before, keep color blue
        self.canvas.itemconfig(self.Square_group[idxY][idxX],fill = "blue")
    
    def position_to_index(self,pos_x, pos_y):
        return (pos_x/SquareLength, pos_y/SquareLength) #since index starts from 0, no need to plus one
    
    def move(self,event):
        idxX,idxY = self.position_to_index(event.x,event.y) #unpack tuple, get index of clicked square
        if self.move_valid(idxX,idxY):
            if self.Square_group[idxY][idxX].get_status == 'not':
                Knight.count += 1
                self.Square_group[idxY][idxX].get_status = 'visited'
            self.Update_Square_current(idxX, idxY)
            self.Update_Square_visited(Knight.previous_idxX,Knight.previous_idxY) #unpack tuple of previous square, pass to update function
            Knight.previous_idxX = idxX #update previous_square index
            Knight.previous_idxY = idxY
            
        else:
            pass
        
    def check_endgame(self):
        pass
        
    def move_valid(self, idxX,idxY):
        return True
        '''
        if idxX > self.Width or idxY > self.Width or idxX < 0 or idxY < 0:
            return False
        P_x = Knight.previous_idxX
        P_y = Knight.previous_idxY
        if (idxX == P_x + 1 and idxY == P_y -2) or (idxX == P_x + 2 and idxY == P_y -1) or \
            (idxX == P_x + 2 and idxY == P_y +1) or (idxX == P_x + 1 and idxY == P_y +2) or \
            (idxX == P_x - 1 and idxY == P_y +2) or(idxX == P_x -2 and idxY == P_y +1) or \
            (idxX == P_x -2 and idxY == P_y -1) or(idxX == P_x -1 and idxY == P_y -2): 
            return True
        '''
'''
i = w.create_line(xy, fill="red")

w.coords(i, new_xy) # change coordinates
w.itemconfig(i, fill="blue") # change color

w.delete(i) # remove

w.delete(ALL) # remove all items

#modify square color
'''

#print(Square.position_to_index(150, 225))  # Should print (11, 16) or (10, 15)

def knights_tour(n): 
    root = Tk.Tk()
    game = Knight(root,n)
    root.mainloop()
    
knights_tour(5)