BunyaminHesap = {
    "adSoyad": "Bünyamin Arslan",
    "hesapNo": "147621721",
    "bakiye": 6000,
    "ekHesap": 700
}

HasanHesap = {
    "adSoyad": "Hasan Arslan",
    "hesapNo": "127621721",
    "bakiye": 2000,
    "ekHesap": 1000
}

HuseyinHesap = {
    "adSoyad": "Hüseyin Arslan",
    "hesapNo": "137621721",
    "bakiye": 3000,
    "ekHesap": 2000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['adSoyad']}.")
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranızı alabilirsiniz.")
        bakiyeSorgula(hesap)        
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if (toplam >= miktar):
            ekHesapKullanimi = input(f"Bakiye yetersiz ({hesap['bakiye']} lira). Ek hesap ({hesap['ekHesap']} lira) kullanılsın mı? (E/H)")
            if ekHesapKullanimi == "E":
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print(f"Paranızı alabilirsiniz.")
                bakiyeSorgula(hesap)                  
            else:                
                print(f"{hesap['hesapNo']} nolu hesabınızda bakiyeniz {hesap['bakiye']} liradır. Ek hesap limitiniz ise {hesap['ekHesap']} liradır.")
        else:
            print("Bakiye yetersiz.")
            bakiyeSorgula(hesap)

def paraYatir(hesap, miktar):
    print(f"Merhaba {hesap['adSoyad']}")
    hesap['bakiye'] = hesap['bakiye'] + miktar
    print("Para yatırma işlemi tamamlandı.")
    bakiyeSorgula(hesap)
    
def bakiyeSorgula(hesap):
    if hesap['bakiye'] > 0:
        print(f"Bakiyeniz {hesap['bakiye']} liradır. Ek hesap limitiniz ise {hesap['ekHesap']} liradır.")
    elif hesap['bakiye'] <= 0:
        print(f"Ek hesap limitiniz {hesap['ekHesap']} liradır.")

def operasyon(hesap):
    while True:
        print(f"Merhaba {hesap['adSoyad']}")
        operasyon = int(input("Para yatırmak için 1'i, çekmek için 2'yi seçiniz: "))
        if operasyon == 1:
            tutar = int(input("Para yatırmak istediğiniz tutarı giriniz: "))
            paraYatir(hesap, tutar)
            cikis = int(input("Menüye dönmek için 1'i, çıkış yapmak için 2'yi tuşlayınız: "))
            if cikis == 1:
                continue
            if cikis == 2:
                break
        if operasyon == 2:
            tutar = int(input("Çekmek istediğiniz tutarı giriniz: "))
            paraCek(hesap, tutar)
            cikis = int(input("Menüye dönmek için 1'i, çıkış yapmak için 2'yi tuşlayınız: "))
            if cikis == 1:
                continue
            if cikis == 2:
                break
        else:
            print("Hatalı tuşlama yaptınız. Lütfen tekrar deneyiniz.")

operasyon(BunyaminHesap)
operasyon(HasanHesap)
operasyon(HuseyinHesap)
