# -*- coding: utf-8 -*-
"""
#### CLIENT SIDE #####

@author: Hangjie Ji
"""

#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '127.0.0.1'          # local interface host 
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)

l=[]
while len(l)<10:
    z = raw_input("Add an integer to the list: ")
    l.append(int(z))
    print(l)
    s.send(z)
    data = s.recv(1024)
    l.append(int(data))
    print(l)
        
s.close()