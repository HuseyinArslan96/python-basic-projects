class Calisan():
    def __init__(self, isim, maas, departman):
        self.isim = isim
        self.maas = maas
        self.departman = departman
    def bilgileriGoster(self):
        print("Bilgiler gösteriliyor...")
        print(f"Ad Soyad: {self.isim} \nMaaş: {self.maas} \nDepartman: {self.departman}")
    def zamYapildi(self, zam):
        self.zam = zam
        self.maas += zam
        print(f"{self.zam} lira zam yapıldı. Maaş {self.maas} lira oldu.")
    def departmanDegisti(self, yeniDepartman):
        self.yeniDepartman = yeniDepartman
        
        self.departman = yeniDepartman
        print(self.isim, "terfi etti. Yeni departmanı: ", self.yeniDepartman)

class Yonetici(Calisan):
    def __init__(self, isim, maas, departman, kisiSayisi):
        super().__init__(isim, maas, departman)
        self.kisiSayisi = kisiSayisi
    def bilgileriGoster(self):
        print("Bilgiler gösteriliyor...")
        print(f"Ad Soyad: {self.isim} \nMaaş: {self.maas} \nDepartman: {self.departman} \nEkibindeki Kişi Sayısı: {self.kisiSayisi}")
    def artir(self, artir):
        print("Ekibindeki kişi sayısı artırıldı.")
        self.artir = artir
        self.kisiSayisi += artir

yonetici = Yonetici("Hüseyin Arslan", 30000, "Yazılım Geliştirme", 5)
yonetici.bilgileriGoster()
yonetici.departmanDegisti("İnsan Kaynakları")
yonetici.zamYapildi(10000)
yonetici.artir(10)
yonetici.bilgileriGoster()

class Ogrenci():
    def dersCalis(self):
        print("Öğrenci şu anda ders çalışıyor.")

class Personel():
    def calis(self):
        print("Personel şu anda ders çalışıyor.")

class Yazilimci(Ogrenci, Personel):
    pass

yazilimci = Yazilimci()
yazilimci.dersCalis()
yazilimci.calis()