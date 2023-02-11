import random
liste = ['Aragorn', 'Boromir', 'Gandalf', 'Legolas', 'Samwise']

karakter = random.choice(liste)
can = int(input('Kaç hak kullanmak istersiniz: '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = input('Hangi Orta Dünya karakterisiniz: ')

    if karakter == tahmin:
        puan = 100 - (100/can) * (sayac-1)
        puan = round(puan, 2)
        print(f'Tebrikler, {sayac}. defada bildiniz. Toplam puanınız: {puan}')
        break
    
    if hak == 0:
        print(f'Hakkınız bitti. Karakteriniz: {karakter}')