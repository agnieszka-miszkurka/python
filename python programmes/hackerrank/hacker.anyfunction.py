# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:48:56 2016

@author: miszk
"""

s = input()

print(any(t.isalnum() for t in s))
print(any(t.isalpha() for t in s))
print(any(t.isdigit() for t in s))
print(any(t.islower() for t in s))
print(any(t.isupper() for t in s))