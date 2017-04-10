# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:56:05 2016

@author: miszk
"""


def na_dziesietny(liczba, system):
    cyfry = "0123456789abcdef" #string znakow ktorymi operuje
    liczba = liczba[::-1]       #odwracam moja liczbe
    potega = 1                  #pierwsza pozycja w kazdym systemie
    dziesiatkowa = 0                    #to bedzei moja dziesiatkowa
    for i in range(0,len(liczba)):  #petla ma tyle iteracji co dlg liczby
        dziesiatkowa += potega*int(cyfry.find("{}".format(liczba[i]))) #*
        potega *= system      #zwiekszam potege bo przechodze dalej
    return dziesiatkowa
    
x = na_dziesietny("1111011",2)
print(x)
#*szukam numeru pozycji w stringu cyfry dla danego fragmentu liczby