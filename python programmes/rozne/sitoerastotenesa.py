# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 04:26:55 2016

@author: miszk
"""
import time
tab = []
do_ilu = int(input("jaki zakres?"))
start_time = time.time()
for i in range(2,do_ilu+1):
    tab.append(i)
    
x = int(do_ilu**(0.5))

for t in range(2,x+1):
    for i in range(2,do_ilu):
        usun = t*i
        if usun>do_ilu:
            break
        else:
            tab[usun-2] = 0

y = tab.count(0)
for i in range(0,y):
    tab.remove(0)
print(tab)
print("--- %s seconds ---" % (time.time() - start_time))