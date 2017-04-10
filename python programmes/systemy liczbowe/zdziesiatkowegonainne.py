# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 09:57:08 2016

@author: miszk
"""

liczba = 102

tab = []

for i in range(len(str(liczba))):
    tab.append(liczba%2)
    liczba = int(liczba/2)
    

print(tab[2:0])