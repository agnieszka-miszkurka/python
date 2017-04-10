# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:50:48 2016

@author: miszk
"""
#                           PYTHONIC ONE
#n = int(input())
#marksheet = [[input(), float(input())] for _ in range(n)]
#
#second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
#print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

x = int(input("ile osob? "))
tab = []
grades = []
names = []
for i in range(x):
    name = input("imie: ")
    grade = float(input("ocena: "))
    tab1 = [name, grade ]
    tab.append(tab1)
    grades.append(grade)
    
grades.sort()
i=0
while (grades[i+1]==grades[i] and i<len(grades)):
    i+=1
min2=grades[i+1]

for t in tab:
    if min2 in t:
        names.append(t[0])
        names.sort()

for t in names:
    print(t)