# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:48:56 2016

@author: miszk
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())
tab = [ [x,i,t] for x in range(x+1) for i in range(y+1) for t in range(z+1) if(x+i+t)!=n ]
print(tab)        