from pip._vendor import requests
import operator
from bs4 import BeautifulSoup

url = "https://ortadunya.com/halbrand/"
tumKelimeler = []
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

def sozlukOlustur(tumKelimeler):
    kelimeSayisi = {}
    for kelime in tumKelimeler:
        if kelime in kelimeSayisi:
            kelimeSayisi[kelime] += 1
        else:
            kelimeSayisi[kelime] = 1
    return kelimeSayisi

def sembolleriTemizle(tumKelimeler):
    sembolsuzKelimeler = []
    semboller = "!@#$/*()?_'+-,." + chr(775)
    for kelime in tumKelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol, "")
        if (len(kelime) > 0):
            sembolsuzKelimeler.append(kelime)
    return sembolsuzKelimeler

for kelimeGruplari in soup.find_all("p"):
    icerik = kelimeGruplari.text
    kelimeler = icerik.lower().split()
    for kelime in kelimeler:
        tumKelimeler.append(kelime)

tumKelimeler = sembolleriTemizle(tumKelimeler)
kelimeSayisi = sozlukOlustur(tumKelimeler)

for anahtar, deger in sorted(kelimeSayisi.items(), key = operator.itemgetter(1)):
    print(anahtar, deger)