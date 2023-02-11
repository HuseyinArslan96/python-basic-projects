#     Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#     1. Bakım => 1. yıl
#     2. Bakım => 2. yıl
#     3. Bakım => 3. yıl
#     * Süre hesabını alınan gün, ay ve yıl bazlı hesaplayınız.
#     ** Datetime modülünü kullanmanız gerekiyor.
import datetime
from datetime import date 
tarih = input('Aracınız hangi tarihte trafiğe çıktı (2010/10/10): ')
tarih = tarih.split('/') # split metoduyla aldığımız tarih bilgisini yıl, ay, gün biçiminde parçalara böldük.
trafigeCikis = datetime.date(int(tarih[0]), int(tarih[1]), int(tarih[2]))
bugun = date.today()
fark = bugun - trafigeCikis
days = fark.days
print(f"Bugünün tarihi: {bugun}; fark: {fark}")
if days <= 365:
    print("1. servis aralığı")
elif days >= 365 and days <= 365*2:
    print("2. servis aralığı")
elif days >= 365*2 and days <= 365*3:
    print("3. servis aralığı")
elif days >= 365*3 and days <= 365*4:
    print("4. servis aralığı")
else:
    print("Geçersiz tarih bilgisi")
#%%
from datetime import date
from datetime import datetime, timedelta  
bugun = date.today()
print(f"Bu günün tarihi: {bugun}") #günün tarihini ekrana yazdırdık.
a = int(input("Lütfen yılı girin: ")) # a isimli bir değişken tanımlayıp, kullanıcıdan integer olarak doğduğu yılı girmesini istedik.
b = int(input("Lütfen ayı girin: "))  # b isimli bir değişken tanımlayıp, kullanıcıdan integer olarak doğduğu ayı girmesini istedik.
c = int(input("Lütfen günü girin: ")) # c isimli bir değişken tanımlayıp, kullanıcıdan integer olarak doğduğu günü girmesini istedik.
trafikCikis = date(a, b, c) # trafikCikis isimli değişkene date fonksiyonunu atadık.
bakimZamani = bugun - trafikCikis   # bakimZamani adlı değişken oluşturduk ve bugun adlı değişkenden trafikCikis adlı değişkeni çıkardık.
print(bakimZamani) # son olarak da bakimZamani değişkeninin sonucunu ekrana yazdırdık.
if (bakimZamani <= timedelta(days = 365)):
    print("Aracınızın birinci bakım zamanı gelmiştir.")
if (bakimZamani >= timedelta(days = 365)) and (bakimZamani <= timedelta(days = 365*2)):
    print("Aracınızın ikinci bakım zamanı gelmiştir.")
if (bakimZamani >= timedelta(days = 730)) and (bakimZamani <= timedelta(days = 365*3)):
    print("Aracınızın üçüncü bakım zamanı gelmiştir.")
if (bakimZamani >= timedelta(days = 1460)) and (bakimZamani <= timedelta(days = 365*4)):
    print("Aracınızın dördüncü bakım zamanı gelmiştir.")