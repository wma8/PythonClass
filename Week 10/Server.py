# -*- coding: utf-8 -*-
"""
#### SERVER SIDE #####

@author: Hangjie Ji
"""

#### SERVER SIDE #####
import socket

s = socket.socket()         # Create a socket object
port = 12345                # Reserve a port for your service.   
s.bind(("", port))          # Bind to the port

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
c.send('Thank you for connecting')

l=[]
while len(l)<10:
    data=c.recv(1024)
    l.append(int(data))
    print(l)
    z = raw_input("Add an integer to the list: ")
    l.append(int(z))
    print(l)
    c.send(z)

c.close()