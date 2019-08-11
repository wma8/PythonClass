#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 00:07:12 2019

@author: jiaruijiang
"""

#hw4_p1
def n_gons(n):
    if n >= 3:
        import turtle as ttl
        angle = (180*(n-2))/float(n)
        for _ in range(n):
            ttl.fd(300/n)
            ttl.right(180-angle)
    ttl.done()
    
#test
#n_gons(3)
#n_gons(4)
#n_gons(4)