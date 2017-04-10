# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:48:56 2016

@author: miszk
"""

x = int(input())
width = len(bin(x)[2:])
for i in range(1, x+1):
    print('{:>{width}} {:>{width}} {:>{width}} {:>{width}} '.format(i ,oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:], width=width))
