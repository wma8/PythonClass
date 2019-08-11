"""
PIC 16 - Winter 2019
QUIZ 1 SOLUTION
"""

"""The function mylists(L) that takes as input a list of numbers 
L = [a, b, c, . . .], and outputs a list of k lists (where k is the number of elements in L)
one with elements a+1, b+1, c+1, . . ., one with elements a+2, b+2, c+2, . . .,
etc, all the way up to a+k, b+k, c+k, . . ."""

def mylists(L):
    return [[i+(j+1) for i in L] for j in range(len(L))]
    
L = [2,3,1] 
print mylists(L)