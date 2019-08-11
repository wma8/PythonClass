#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 01:24:36 2018

@author: hangjieji
"""

def main():
    print "main() is running"

print "example3 is running"
print "its __name__ is", __name__ #__name__ is a global variable indicating
                            #whether the program is run directly or being imported as module
                            #if running directly, __name__ is __main__
                            #if imported as module, __name__ has name of original script
#main()
if __name__=="__main__":
    main()