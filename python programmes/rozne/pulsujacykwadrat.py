# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:49:21 2016

@author: miszk
"""

import math, time
def kwadrat(r, zmiana, y, x):
    srodekX = math.floor(x/2)
    srodekY = math.floor(y/2)
    
    for xx in range(0,x):   #zwiekszamy nr wiersza o 1
        s=""                #tworzymy nowy wiersz
        for yy in range(0,y):   #dla kazdego x(wiersza) idziemy po kolejnych kolumnach
            if (math.fabs(srodekX-xx)==r and (math.fabs(srodekY-yy))<=r) or (math.fabs(srodekY-yy)==r and (math.fabs(srodekX-xx)<=r)):
                s+='X'
            else:
                s+=" "
        print(s)
    
    if (zmiana == 1):                #jesli kwadrat rosnie
        if (r == min(srodekX,srodekY)):        #jesli kwadrat doszedl do konca 
            zmiana = -1              #to zaczynamy pomniejszac
            
    else:                       #jesli kwadrt maleje
        if (r == 0):        #jesli doszlismy do srodka
            zmiana = 1          #to zacznij powiekszac kwadrat

    r += zmiana                 #zwieksza lub zmneijsza promien
    time.sleep(0.5)                 
    print(chr(27) + "[2J")
    kwadrat(r, zmiana, y, x)
    
x = int(input("Ile rzedow?"))
y = int(input("Ile kolumn?"))
kwadrat(0, 1, y, x)