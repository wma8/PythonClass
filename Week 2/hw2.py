#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:04:55 2019

@author: jiaruijiang
"""
import math


def solve(listOfF,initial,tolerance):
    x = float(initial) #get ready for calculation involving decimals
    print "initial x value is", x
    i =0 #set counter
    while abs(listOfF(x)[0])>tolerance: #condition for Newtown method to continue
        x = x - listOfF(x)[0]/listOfF(x)[1] #operation to get next x
        i+=1 #update counter
        #print "x at iteration",i, "is", x
        if i >10000:
            print "too many iteration, break!!!"
            break
    print "x =", x, "iteration is",i

'''
print solve(lambda x: [x**2-1, 2*x], 3, 0.001)
print solve(lambda x: [x**2-1, 2*x], 3, 0.0001)
# x = 1.00000528956, f(x) = 1.05791479794e-05 < 0.0001, correct
print solve(lambda x: [x**2-1, 2*x], 3, 1e-4)
print solve(lambda x: [x**2-1, 2*x], 3, 1e-5)
print solve(lambda x: [x**2-1, 2*x], 3, 1e-6)
print solve(lambda x: [x**2-1, 2*x], 3, 1e-7)
print solve(lambda x: [x**2-1, 2*x], 3, 1e-8)
print solve(lambda x: [x**2-1, 2*x], 3, 1e-9)
print solve(lambda x: [x**2-1, 2*x], 3, 1e-10)
print solve(lambda x: [x**2-1, 2*x], 3, 1e-11)
print solve(lambda x: [x**2-1, 2*x], 3, 1e-12)
print solve(lambda x: [x**2-1, 2*x], 3, 1e-13)
print solve(lambda x: [x**2-1, 2*x], 3, 1e-14)
print solve(lambda x: [x**2-1, 2*x], 3, 1e-15)
print solve(lambda x: [x**2-1, 2*x], 3, 1e-16)


print solve(lambda x: [x**2-1, 2*x], -1, 0.001)
print solve(lambda x: [x**2-1, 2*x], -1, 0.0001)
#x = -1, f(x) = 0 < 0.0001, correct
print solve(lambda x: [x**2-1, 2*x], -1, 0.00001)
'''

print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 0.001)
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 0.0001)
# x = 1.5641107899e-06, f(x)= 1.56411201302e-06 < 0.0001, correct
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 1e-5)
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 1e-6)
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 1e-7)
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 1e-8)
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 1e-9)
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 1e-10)
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 1e-11)
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 1e-12)
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 1e-13)
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 1e-14)
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 1e-15)
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 1e-16)
print solve(lambda x: [math.exp(x)-1, math.exp(x)], 1, 1e-17)

'''

print solve(lambda x: [math.sin(x), math.cos(x)], 0.5, 0.001)
print solve(lambda x: [math.sin(x), math.cos(x)], 0.5, 0.0001)
# x =3.31180213264e-05, f(x)= 3.31180213203e-05 < 0.0001, correct
print solve(lambda x: [math.sin(x), math.cos(x)], 0.5, 0.0001)

'''