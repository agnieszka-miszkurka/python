# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:42:54 2016

@author: miszk
"""

import random
tab = []
for i in range(10):
    tab.append(random.randint(0,20))

print(tab)

def szukaj(tab,n):
    i=0
    for liczba in tab:
        if n==liczba:
           return i
        i+=1
    return -1
        
x = szukaj(tab,4)
print(x)
        
        