def szyfrowanie_kluczem (klucz, tekst):
    alfa = "abcdefghijklmnopqrstuvwxyz"
    nowytekst = tekst.replace(' ', '')
    nowytekst = nowytekst.lower()
    zaszyfrowany = ''
    for i in range(len(nowytekst)):
        litera_w_kluczu = klucz[i % len(klucz)]
        przesuniecie = (alfa.find(litera_w_kluczu) + 1) % 26
        pozycja_litery = alfa.find(nowytekst[i])
        zaszyfrowany += alfa[(pozycja_litery + przesuniecie)%26]
    return zaszyfrowany

def odszyfrowywanie_kluczem (klucz,zaszyfrowany):
    alfa = "abcdefghijklmnopqrstuvwxyz"
    odszyfrowany = ''
    for i in range(len(zaszyfrowany)):
        litera_w_kluczu = klucz[i % len(klucz)]
        przesuniecie = (alfa.find(zaszyfrowany[i]) - alfa.find(litera_w_kluczu) - 1) % 26
        odszyfrowany += alfa[przesuniecie]
    return odszyfrowany

klucz = 'abc'
tekst = 'ZZAla ma kota'
zaszyfrowany = szyfrowanie_kluczem(klucz,tekst)
print(zaszyfrowany)
odszyfrowany = odszyfrowywanie_kluczem (klucz,zaszyfrowany)
print(odszyfrowany)