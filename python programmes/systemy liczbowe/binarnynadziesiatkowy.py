# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 09:29:15 2016

@author: miszk
"""
liczba = 101   
n = len(str(liczba))        #len - dlugosc liczby
potega = 1      
suma = 0
for i in range (0,n):       #petla ma tyle iteracji co dlg liczby
    if liczba%10 == 1:      #jesli jest jedynka
        suma = suma + potega    #dodaj do liczby odpowiednia potege
    potega = potega*2           #przechodzimy do kolejnej potegi
    liczba = liczba//10     #zmniejszamy liczbe o ostatnia cyfre
    
print(suma)
  