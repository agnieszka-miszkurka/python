# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 03:40:29 2016

@author: miszk
"""
x = "To jest napis w ktorym zamienie litery"
y = ""

for i in range(0,len(x)):
    if i%2==0:
        b = x[i]
        b = b.upper()
        y += b
    else:
        b = x[i]
        b = b.lower()
        y += b

print(y)

