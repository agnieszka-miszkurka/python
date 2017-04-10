# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:48:56 2016

@author: miszk
"""
import string
import time
s = string.ascii_lowercase

def dywan(wykon, zmiana, x):
    L=[]
    for i in range(wykon):
        a= '-'.join(s[wykon-1:i:-1]+s[i:wykon])
        L.append(a.center(4*x-3,'-'))
        
    for t in range(x-wykon):
        L.append('-'*(4*x-3))
    
    print('\n'.join(L[::-1]+L[1:]))
    if zmiana==-1:
        if wykon+zmiana==-1:
            zmiana=1
    else:
        if wykon+zmiana>x:
            zmiana=-1
    wykon=wykon+zmiana
            
    time.sleep(0.5)
    print(chr(27) + "[2J")
    dywan(wykon,zmiana,x)
         
x = int(input())
dywan(x,-1,x)
        
        