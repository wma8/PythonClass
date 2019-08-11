#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Koch Square using Turtle module

"""

import turtle as t

def koch_square(n,L):
    if n==0:
        t.fd(20)
    else:
        koch_square(n-1,L/3)
        t.left(90)
        koch_square(n-1,L/3)
        t.right(90)
        koch_square(n-1,L/3)
        t.right(90)
        koch_square(n-1,L/3)
        t.left(90)
        koch_square(n-1,L/3)

koch_square(3,500)
t.done()
