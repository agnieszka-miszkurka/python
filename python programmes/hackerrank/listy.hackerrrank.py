# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:49:21 2016

@author: miszk
"""

n = int(input())
tab = []
for i in range(0,n):
    x = input()
    print(x[0:1])
    if x[0:6]=="insert":
        y=int(x[7])
        z=int(x[9:])
        tab.insert(y,z)
    if x[0:5]=="print":
        print(tab)
    if x[0:6]=="remove":
        y=int(x[7:])
        tab.remove(y)
    if x[0:6]=="append":
        y=int(x[7:])
        tab.append(y)
    if x[0:4]=="sort":
        tab.sort()
    if x[0:3]=="pop":
        tab.pop()
    if x[0:7]=="reverse":
        tab.reverse()
    print(tab)