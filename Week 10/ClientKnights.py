# -*- coding: utf-8 -*-
"""
#### CLIENT SIDE #####

@author: Hangjie Ji
"""

#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '127.0.0.1'          # local interface host 
port = 12346               # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)

while True:
    z = raw_input("w = up, s = down, a = left, d = right, q = quit: ")
    s.send(z)
    if (z == "q"):
        s.close()
        break
        
s.close()