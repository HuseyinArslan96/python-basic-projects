from pip._vendor import requests
from bs4 import BeautifulSoup

imdburl = "https://www.imdb.com/chart/top/"

r = requests.get(imdburl)

soup = BeautifulSoup(r.content, "html.parser")

gelenVeri = soup.find_all("table",{"class":"chart full-width"})

filmTablosu = (gelenVeri[0].contents)[len(gelenVeri[0].contents)-2]

filmTablosu = filmTablosu.find_all("tr")

for film in filmTablosu:
    filmBasliklari = film.find_all("td", {"class":"titleColumn"})
    filmAdi = filmBasliklari[0].text
    filmAdi = filmAdi.replace("\n", "")
    filmRatingleri = film.find_all("td", {"class":"ratingColumn imdbRating"})
    filmPuani = filmRatingleri[0].text
    filmPuani = filmPuani.replace("\n", "")
    print(filmAdi + " ****** " + filmPuani)
