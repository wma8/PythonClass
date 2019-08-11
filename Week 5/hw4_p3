#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 22:00:53 2019

@author: jiaruijiang
"""

import matplotlib.pyplot as plt 
import numpy as np

karate = open("karate_edgeList1.txt").read()
pairs = [s.split('\t') for s in karate.splitlines()] #splitlines() takes strings and returns a list of each line as element
                                                    # s.split('\t') splits the elements in list further by each tab space

#print pairs #now pairs is a list of lists, with each friendship-pair as element
pairs = [[int(i) for i in j]for j in pairs] # cast to integer
n = max(max(j for j in pairs)) #get the max No of players??
adjMatrix = [[0]*n for _ in range(n)] #create an empty(0) mx for later manipulation

for p in pairs: # p is a list, like [1,31] means 1 and 31 are friends, note 1 and 31 are int
    adjMatrix[p[0]-1][p[1]-1]=1 #shift to match index that starts with 0
    adjMatrix[p[1]-1][p[0]-1]=1#

#now we've completed the adjMatrix. Next, use function to plot the Network
#print adjMatrix

N = adjMatrix

numrows = len(adjMatrix) 
sizeList = np.arange(numrows) 
print sizeList
for i in range(numrows):
    sizeList[i]=sum(adjMatrix[i]) 
print sizeList

n=len(N)
x=[np.cos(2*np.pi*i/n) for i in range(n)]
y=[np.sin(2*np.pi*i/n) for i in range(n)]
#print sum(adjMatrix[i])
for i in range(n):
    for j in range(i):
        if N[i][j]>=1: #only check the lower triangle of matrix, b/c mx is symmetric
            #print sum(N[i])
            plt.plot([x[i],x[j]],[y[i],y[j]],'r-')
            
    plt.plot(x[i],y[i],'bo',markersize = sizeList[i]) # nodes with more friends will be larger
    
            
plt.show()
    