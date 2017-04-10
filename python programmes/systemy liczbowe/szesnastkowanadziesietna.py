# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:56:05 2016

@author: miszk
"""


def na_dziesietny(liczba, system):
    cyfry = "0123456789abcdef"
    liczba = liczba[::-1]
    potega = 1
    suma = 0
    for i in range(0,len(liczba)):
        suma += potega*int(cyfry.find("{}".format(liczba[i])))
        potega *= system
    return suma
    
x = na_dziesietny("1111011",2)
print(x)
