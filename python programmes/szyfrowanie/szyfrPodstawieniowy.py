def szyfrPodstawieniowy(tekst, nowy_alfa):
    tekst = tekst.lower()
    tekst = tekst.replace(" ", "")
    zaszyfrowany = ""
    for i in range(len(tekst)):
        x = alfa.find(tekst[i])
        zaszyfrowany += nowy_alfa[x]
    return zaszyfrowany

def odszyfrPodstawieniowy(zaszyfrowany, nowy_alfa):
    odszyfrowany = ""
    for i in range(len(zaszyfrowany)):
        x = nowy_alfa.find(zaszyfrowany[i])
        odszyfrowany += alfa[x]
    return odszyfrowany

nowy_alfa = "qwertyuiopasdfghjklzxcvbnm"
alfa = "abcdefghijklmnopqrstuvwxyz"
tekst = "zzAbcdefla ma kota"
zaszyfrowany = szyfrPodstawieniowy(tekst, nowy_alfa)
odszyfrowany = odszyfrPodstawieniowy(zaszyfrowany, nowy_alfa)
print(zaszyfrowany)
print(odszyfrowany)