# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 06:30:15 2016

@author: miszk
"""
import random
tab = []

for i in range (0,10):
    tab.append(random.randint(0,20))
print(tab)   
x = 3


def wartownik(x,tab):
    tab.append(x)
    for i, element in enumerate(tab):
        if element==x:
            y = i
            break
        else: 
            continue
    if y==10:
        return "nie ma tej liczby"
    else:
        return "jest ona tam na ", y, "pozycji"
        
print(wartownik(x,tab))