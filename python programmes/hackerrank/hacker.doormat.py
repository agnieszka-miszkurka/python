# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 15:46:23 2016

@author: miszk
"""
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.

for i in range(1,N,2): 
    print("-"*(int((int(M)-i*3)/2)) + ".|."*i + "-"*(int((int(M)-i*3)/2))) 
print("-"*int((int(M)-7)/2)+"WELCOME" + "-"*int((M-7)/2))
for i in range(N-2,-1,-2): 
    print("-"*(int((int(M)-i*3)/2)) + ".|."*i + "-"*(int((int(M)-i*3)/2))) 