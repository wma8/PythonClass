#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 00:15:35 2019

@author: jiaruijiang
"""
#hw4_p2
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
choice = pd.read_csv('choice1.csv') #note, use read_csv to read excel file, not read_table!!!

#print choice
'''
exp1 = choice['expt1']
exp2 = choice['expt2']
exp3 = choice['expt3']
exp4 = choice['expt4']
'''
MrA1 = (choice['expt1'] == 1) 
MrA2 = (choice['expt2'] == 1) 
MrA3 = (choice['expt3'] == 1)
MrA4 = (choice['expt4'] == 1)

MrB1 = (choice['expt1'] == 2) 
MrB2 = (choice['expt2'] == 2) 
MrB3 = (choice['expt3'] == 2)
MrB4 = (choice['expt4'] == 2)

No_Diff1 = (choice['expt1'] == 3) 
No_Diff2 = (choice['expt2'] == 3) 
No_Diff3 = (choice['expt3'] == 3)
No_Diff4 = (choice['expt4'] == 3)

#MrB = (choice['expt1'] == 2) | (choice['expt2'] == 2) | (choice['expt3'] == 2) | (choice['expt4'] == 2)
#No_Diff = (choice['expt1'] == 3) | (choice['expt2'] == 3) | (choice['expt3'] == 3) | (choice['expt4'] == 3)
barwidth=.2
plt.axis([-1, 4, 0, 100])
plt.ylabel('Frequency')
plt.xlabel("Mental Accounting and Consumer Choice")
plt.title("Choices of 'Who will be more upset?' in 4 Exps") 
plt.xticks(np.arange(4)+1/2,['Exp1','Exp2','Exp3','Exp4']) 

plt.bar(np.arange(4),[len(choice[MrA1].index),
                      len(choice[MrA2].index),
                      len(choice[MrA3].index), 
                      len(choice[MrA4].index)], 
        barwidth, color='r', label='Mr.A')
plt.bar(np.arange(4)+barwidth,[len(choice[MrB1].index),
                      len(choice[MrB2].index),
                      len(choice[MrB3].index), 
                      len(choice[MrB4].index)], 
        barwidth, color='b', label='Mr.B')
plt.bar(np.arange(4)+2*barwidth,[len(choice[No_Diff1].index),
                      len(choice[No_Diff2].index),
                      len(choice[No_Diff3].index), 
                      len(choice[No_Diff4].index)], 
        barwidth, color='g', label='No_Difference')

plt.legend()
plt.show()