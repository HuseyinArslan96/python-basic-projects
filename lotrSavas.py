import random

class Dusman:
    def __init__(self, isim = "Nazgul", can = 500, saldiriGucu = 10, buyu = 10):
        self.isim = isim
        self.can = can
        self.saldiriGucu = saldiriGucu
        self.buyu = buyu
    def saldir(self):
        print(f"{self.isim} saldırıyor...")
        print("Büyü gücü: ", self.saldiriGucu)
        harcananBuyu = random.randrange(0,10)
        print(f"Harcanan büyü sayısı: {harcananBuyu}")
        self.buyu -= harcananBuyu
        print(f"Kalan büyü sayısı: {self.buyu} ")
        verilenZarar = harcananBuyu * self.saldiriGucu
        print("Verilen zarar: ", verilenZarar)
        return (harcananBuyu, self.saldiriGucu, verilenZarar)
    def saldiriyaUgra(self, harcananBuyu, saldiriGucu):
        print(f"{self.isim}: Saldırıya uğruyorum...")
        print(f"Can: {self.can}")
        self.can -= harcananBuyu * saldiriGucu
    def buyuBittiMi(self):
        if self.buyu <= 0:
            print(str(self.isim) + " savaş meydanından çekiliyor.")
            return True
        return False
    def hayattaMi(self):
        if self.can <= 0:
            print(str(self.isim) + " öldü.")
        else:
            print("Kalan can: ", self.can)    
    def print(self):
        print("İsim:", self.isim, "\n" "Kalan Can:", self.can, "\n" "Saldırı Gücü:", self.saldiriGucu, "\n" "Kalan Büyü Sayısı:", self.buyu)

karakterler = """
İyiler:
(1) Manwe
(2) Gandalf
(3) Elrond
Kötüler:
(4) Melkor
(5) Sauron
(6) Nazgul
"""
print(karakterler)
karakter = int(input("Karakterinizi seçin: "))

melkor = Dusman("Melkor", 6000, 90, 150)
sauron = Dusman("Sauron", 2000, 30, 50)
nazgul = Dusman("Nazgul", 500, 10, 10)

manwe = Dusman("Manwe", 6500, 100, 170)
gandalf = Dusman("Gandalf", 2500, 40, 60)
elrond = Dusman("Elrond", 1500, 20, 15)

evil = [melkor, sauron, nazgul]
good = [manwe, gandalf, elrond]

i = 0
while i < 3:
    if karakter == 1:
        karakter = manwe
    if karakter == 2:
        karakter = gandalf
    if karakter == 3:
        karakter = elrond
    if karakter == 4:
        karakter = melkor
    if karakter == 5:
        karakter = sauron
    if karakter == 6:
        karakter = nazgul
    if karakter in evil:
        rastgele = random.choice(good)
    if karakter in good:
        rastgele = random.choice(evil)    
    donenDeger1 = karakter.saldir()
    rastgele.saldiriyaUgra(donenDeger1[0], donenDeger1[1])
    rastgele.buyuBittiMi()
    rastgele.hayattaMi()
    donenDeger2 = rastgele.saldir()
    karakter.saldiriyaUgra(donenDeger2[0], donenDeger2[1])
    karakter.buyuBittiMi()
    karakter.hayattaMi()
    if karakter.can > rastgele.can:
        print("Savaş bitti. Kazanan: ", karakter.isim)
    elif rastgele.can > karakter.can:
        print("Savaş bitti. Kazanan: ", rastgele.isim)
    else:
        print("Savaş berabere bitti.")
    i += 1