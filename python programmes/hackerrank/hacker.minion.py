# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 14:45:39 2016

@author: miszk
"""

s = input()
kevscr = 0
stuscr = 0
vowels = "AEIOU"
for i in range(len(s)):
    if s[i] in vowels:
        kevscr += (len(s)-i)
    else:
        stuscr +=(len(s)-i)
if kevscr==stuscr:
    print("Draw")
if kevscr>stuscr:
    print("Kevin",kevscr)
if kevscr<stuscr:
    print("Stuart", stuscr)