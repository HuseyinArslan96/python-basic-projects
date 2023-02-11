'''ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '123123'
    },
    '125': {
        'ad': 'Ahmet',
        'soyad': 'Yılmaz',
        'telefon': '123456'
    },
    '130': {
        'ad': 'Mehmet',
        'soyad': 'Yılmaz',
        'telefon': '456789'
    }
}
1. Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary (sözlük veri tipi) içinde saklayın.
2. Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''
ogrenciler = {}
ogrenciNumara = str(input("Öğrencinin numarası: "))
ogrenciAd = input("Öğrencinin adı: ")
ogrenciSoyad = input("Öğrencinin soyadı: ")
ogrenciTelefon = input("Öğrencinin telefonu: ")
ogrenciler.update({
    ogrenciNumara: {
        'ad': ogrenciAd,
        'soyad': ogrenciSoyad,
        'telefon': ogrenciTelefon
    }
})

# ogrenciler[ogrenciNumara] = {
#         'ad': ogrenciAd,
#         'soyad': ogrenciSoyad,
#         'telefon': ogrenciTelefon
#     } => alternatif kod

ogrenciNumara = str(input("Öğrencinin numarası: "))
ogrenciAd = input("Öğrencinin adı: ")
ogrenciSoyad = input("Öğrencinin soyadı: ")
ogrenciTelefon = input("Öğrencinin telefonu: ")
ogrenciler.update({
    ogrenciNumara: {
        'ad': ogrenciAd,
        'soyad': ogrenciSoyad,
        'telefon': ogrenciTelefon
    }
})

ogrenciNumara = str(input("Öğrencinin numarası: "))
ogrenciAd = input("Öğrencinin adı: ")
ogrenciSoyad = input("Öğrencinin soyadı: ")
ogrenciTelefon = input("Öğrencinin telefonu: ")
ogrenciler.update({
    ogrenciNumara: {
        'ad': ogrenciAd,
        'soyad': ogrenciSoyad,
        'telefon': ogrenciTelefon
    }
})
print('*'*50)
number = input("Öğrenci numarasını girin: ")
ogrenci = ogrenciler[number]
print(f"Aradığınız {number} numaralı öğrencinin adı {ogrenci['ad']}, soyadı {ogrenci['soyad']} ve telefonu {ogrenci['telefon']} şeklindedir.")