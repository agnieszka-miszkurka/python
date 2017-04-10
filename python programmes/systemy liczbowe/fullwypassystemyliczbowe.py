# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:48:26 2016

@author: miszk
"""
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

def na_dziesietny(liczba, system):
    cyfry = "0123456789abcdef" #string znakow ktorymi operuje
    liczba = liczba[::-1]       #odwracam moja liczbe
    potega = 1                  #pierwsza pozycja w kazdym systemie
    dziesiatkowa = 0                    #to bedzei moja dziesiatkowa
    for i in range(0,len(liczba)):  #petla ma tyle iteracji co dlg liczby
        dziesiatkowa += potega*int(cyfry.find("{}".format(liczba[i]))) #*
        potega *= system      #zwiekszam potege bo przechodze dalej
    return dziesiatkowa
    
instrukcja1 = 'Wybierz z jakiego systemu chcesz przekonwertowac: \n 2-dwojkowy \n 4-czworkowy itp.. \n '
instrukcja2 = 'Wybierz na jaki system chcesz przekonwertowac: \n 2-dwojkowy \n 4-czworkowy itp.. \n '
instrukcja3 = 'podaj liczbe do zmiany: '

x = int(input(instrukcja1))
y = int(input(instrukcja2))
liczba = input(instrukcja3)

if x==10:
    liczba = int(liczba)
    wynik = z_dziesiatkowej(liczba,y)
else:
    prawie = na_dziesietny(liczba,y)
    wynik = z_dziesiatkowej(prawie,y)
print(wynik)
    