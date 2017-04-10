# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 05:59:57 2016

@author: miszk
"""

import random
tab = []
for i in range(0,10):
    tab.append(random.randint(0,20))

    
def funkcja(tab):
    x = tab[0]
    for i, liczba in enumerate(tab):
        if  i==9:
            break
        if tab[i+1]>x:
            x = tab[i+1]
    return x

print(tab)
print(funkcja(tab))