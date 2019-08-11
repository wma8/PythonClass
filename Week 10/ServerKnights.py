# -*- coding: utf-8 -*-
"""
#### SERVER SIDE #####

@author: Hangjie Ji
"""
#### SERVER SIDE #####

import socket
import Tkinter as Tk #or tkinter in v.3
        
"""We create a class and a function that together launch an 
nxn knight's tour game."""
     
class ktour:
    def __init__(self, master,n, connected_socket):
        self.n=n
        self.master = master
        self.canvas = Tk.Canvas(master, width=500, height=500)
        #draw the initial grid
        for i in range(n):
            for j in range(n):
                self.canvas.create_rectangle(i*(500/n),j*(500/n),(i+1)*(500/n),(j+1)*(500/n))
        #let the first position be [0,0]
        self.canvas.create_rectangle(0,0,(500/n),(500/n),fill="orange")
        self.current=[0,0]
        #create an array to keep track of which positions have been visited
        self.state=[[0]*n]*n
        self.canvas.pack()
        
#         self.canvas.bind("<Button-1>", self.click)
        
        self.socket = connected_socket
        self.receive_data()

    def click(self,ev):
        a=ev[0]+self.current[0]
        b=ev[1]+self.current[1]
        # update the board
        if a >= 0 and a < self.n and b>=0 and b<self.n:
            self.canvas.create_rectangle(self.current[0]*(500/self.n),self.current[1]*(500/self.n),(self.current[0]+1)*(500/self.n),(self.current[1]+1)*(500/self.n),fill="blue")
            self.canvas.create_rectangle(a*(500/self.n),b*(500/self.n),(a+1)*(500/self.n),(b+1)*(500/self.n),fill="orange")
            self.current=[a,b]
            self.state[a][b]=1
    
    def receive_data(self):
        data = self.socket.recv(1024)
        if(data):
            ev = (0,0)
            if (data == "w"):
                ev = (0,-1)
            elif (data == "s"):
                ev = (0,1)
            elif (data == "a"):
                ev = (-1,0)
            elif (data == "d"):
                ev = (1,0)
            self.click(ev)
            if (data =="q"):
                self.socket.close()
            else:
                self.master.after(50, self.receive_data)

def knights_tour(n):
    root = Tk.Tk()
    s = socket.socket()         # Create a socket object
    port = 12346                # Reserve a port for your service.   
    s.bind(("localhost", port))          # Bind to the port
    s.listen(5)                 # Now wait for client connection.
    c, addr = s.accept()     # Establish connection with client.
    
    print 'Got connection from', addr
    c.send('Thank you for connecting')
    gui=ktour(root, n, c)

    root.mainloop()

if __name__ == "__main__":
    knights_tour(5)

