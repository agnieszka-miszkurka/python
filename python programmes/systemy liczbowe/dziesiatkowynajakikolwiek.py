# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:01:44 2016

@author: miszk
"""

dziesiatkowa = int(input("wpisz liczbe dziesietna: "))
system = int(input("jaki system liczbowy? (dwojkowy - 2, osemkowy- 8 itd): "))

def z_dziesiatkowej(dziesiatkowa,system):
    cyfry = "0123456789abcdef" #string znakow ktorymi wypelnie tabele
    tab = []                #tabela w ktorej bd umieszczec reszty z dzielenia         
    while dziesiatkowa>0:       #koniec dzielenia - dzielna jest==0
        tab.append(cyfry[dziesiatkowa%system])  #dotab dodaje odpowiedni numer str
        dziesiatkowa = dziesiatkowa//system   
    tab.reverse()               #odwracam komorki tab kolejnoscia
    liczba = ""                 #towrze string liczba
    for i in tab:               #przepisuje komorki tab do liczby
        liczba = liczba + str(i)
    return liczba

