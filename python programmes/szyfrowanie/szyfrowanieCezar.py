def szyfrCezara(tekst, przesuniecie):
    alfa = "abcdefghijklmnopqrstuvwxyz"

    tekst = tekst.lower()
    tekst = tekst.replace(" ", "")

    zaszyfrowany = ""
    for i in range(len(tekst)):
        x = alfa.find(tekst[i])
        zaszyfrowany += alfa[(x + przesuniecie)%26]

    return zaszyfrowany

def odszyfrCezara(zaszyfrowany, przesuniecie):
    alfa = "abcdefghijklmnopqrstuvwxyz"
    odszyfrowany = ""

    for i in range(len(zaszyfrowany)):
        x = alfa.find(zaszyfrowany[i])
        odszyfrowany += alfa[(x - przesuniecie) % 26]
    return odszyfrowany

tekst = "Ala ma kota"
przesuniecie = 5
zaszyfrowany = szyfrCezara(tekst, przesuniecie)
odszyfrowany = odszyfrCezara(zaszyfrowany, przesuniecie)