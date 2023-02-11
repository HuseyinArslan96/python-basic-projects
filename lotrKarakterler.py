from pip._vendor import requests
import operator
from bs4 import BeautifulSoup

while True:
    print("1: Aragorn")
    print("2: Legolas")
    print("3: Theoden")
    print("4: Gandalf")

    karakterSec = input("Bir Karakter Seçiniz (çıkmak için q'ya basınız): ")

    if karakterSec == "1":
        url = "https://ortadunya.com/aragorn-kimdir/"
        tumKelimeler = []
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        for kelimeGruplari in soup.find_all("p"):
            icerik = kelimeGruplari.text
            tumKelimeler.append(icerik)
        print(('{}'*len(tumKelimeler)).format(*tumKelimeler))

    elif karakterSec == "2":
        url = "https://ortadunya.com/legolas/"
        tumKelimeler = []
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        for kelimeGruplari in soup.find_all("p"):
            icerik = kelimeGruplari.text
            tumKelimeler.append(icerik)
        print(('{}'*len(tumKelimeler)).format(*tumKelimeler))

    elif karakterSec == "3":
        url = "https://ortadunya.com/theoden/"
        tumKelimeler = []
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        for kelimeGruplari in soup.find_all("p"):
            icerik = kelimeGruplari.text
            tumKelimeler.append(icerik)
        print(('{}'*len(tumKelimeler)).format(*tumKelimeler))

    elif karakterSec == "4":
        url = "https://ortadunya.fandom.com/wiki/Gandalf"
        tumKelimeler = []
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        for kelimeGruplari in soup.find_all("p"):
            icerik = kelimeGruplari.text
            tumKelimeler.append(icerik)
        print(('{}'*len(tumKelimeler)).format(*tumKelimeler))

    elif karakterSec == "q":
        print("Çıkılıyor...")
        break
    
    else:
        print("Yanlış seçim, tekrar deneyiniz.")