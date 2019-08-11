#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:05:07 2019

@author: jiaruijiang
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:22:10 2019

@author: jiaruijiang
"""


#HW3 P1 done
import re
def mytype(v):
    a = str(v)
    #print a
    #print type(a)
    if re.search(r'\[(\d, )*\d?\]',a) != None: #test list
        return "list"
    elif re.search(r'-?\d+\.\d+',a) != None: #test float
        return "float"
    elif re.search(r'^-?\d+$',a) != None: #test int
        return "integer"
    else: 
        return "string"
    
#HW3 P2 done    
def findpdfs(L):
    #l = str(L)
    return re.findall(r'\w+(?=\.pdf)',str(L)) #use backward search

##HW# P3 done
import urllib2
def findemail(url):
#url = "http://www.math.ucla.edu/~hangjie/contact"
    page=urllib2.urlopen(url).read() #get source code for the page
    page=page.replace(' [at] ', '@').replace(' at ', '@').replace(' AT ', '@').replace(' [AT] ','@').\
    replace(' [dot] ','.').replace(' [DOT] ','.').replace(' dot ','.').replace(' DOT ','.').replace('[at]', '@')\
    .replace('[AT]', '@').replace('[dot]','.').replace('[DOT]','.')#change to standard email form

    return re.findall(r'\w*@(?:[A-Za-z0-9]+\.)+\w+',page) #capture all emails, use ?: to indicate non-capturing group

#HW3 P4
import re
import happiness_dictionary as hd

def happiness(text):
    blocks = re.split(r'[\s,\.\?\!]',text.lower()) #split input string
    
    count =0
    score = 0
    for i in blocks:
        if i in hd.happiness_dictionary:
            print i
            print hd.happiness_dictionary[i]
            
            count += 1
            score += hd.happiness_dictionary[i]
            print count

    if count != 0:
        print score,count
        return score/count
    else:
        return 0
'''
#test    
test1 = "Wish all love can be realized"
test2 = "I want to share my world with you"
test3 = "even till now you are still my light at your b-day"
print happiness(test3)
'''