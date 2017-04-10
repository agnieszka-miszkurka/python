# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 05:29:13 2016

@author: miszk
"""

import random, time

def rain(x,y):
    baseline = " "*y
    tab = [baseline]*x
    while True:  
        for t in tab:
            print(t)
        z = random.randint(1,y)
        s = "-"*(z-1) + "O" + " "*(y-z)
        tab.insert(0,s)
        tab.pop(x)
        time.sleep(0.09)
        print(chr(27) + "[2J")
        
x = int(input("How many rows: "))
y = int(input("How many columns: "))
rain(x,y)